#!/usr/bin/env python3
# BY: SCOUT@CL | MODEL: Claude Opus 5.5【自報】 | CHARTER: AIM-C1.2 | EMITS: tools/sec.py
"""tools/sec.py — SEC EDGAR fetcher for AIM (fair-access compliant).

SEC requires a declared User-Agent (name + contact email) and <= 10 req/s.
There is no registration or approval step. efts.sec.gov (full-text search)
is blocked by this environment's egress policy; use data.sec.gov JSON and
www.sec.gov/Archives instead.

Usage:
  python tools/sec.py cik NVDA                     # ticker -> 10-digit CIK
  python tools/sec.py filings NVDA [--form 10-Q] [--n 10]
  python tools/sec.py facts NVDA [--concept Revenues]
  python tools/sec.py doc <sec.gov URL> [--out path]
  python tools/sec.py doc <URL> --grep "egress fee" --grep telemetry [--ctx 400]
      # full-text grep over the whole filing (no 100k truncation); prints
      # each hit with surrounding plain text, verbatim
"""
import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request

USER_AGENT = "AIM-research kimiochang@yahoo.com.tw"   # SEC-required contact
MIN_INTERVAL = 0.125                                  # <= 8 req/s
_last = 0.0


def get(url: str, retries: int = 4) -> bytes:
    """GET with declared UA, rate limit and backoff on 403/429/5xx."""
    global _last
    host = url.split("/")[2]
    if host == "efts.sec.gov":
        sys.exit("efts.sec.gov is blocked by egress policy; use filings/facts.")
    for attempt in range(retries):
        wait = MIN_INTERVAL - (time.time() - _last)
        if wait > 0:
            time.sleep(wait)
        _last = time.time()
        req = urllib.request.Request(url, headers={
            "User-Agent": USER_AGENT,
            "Accept-Encoding": "identity",
            "Host": host,
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 500, 502, 503) and attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("unreachable")


def cik(ticker_or_cik: str) -> str:
    """Resolve ticker to zero-padded 10-digit CIK."""
    s = ticker_or_cik.strip()
    if s.isdigit():
        return s.zfill(10)
    data = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
    for row in data.values():
        if row["ticker"].upper() == s.upper():
            return str(row["cik_str"]).zfill(10)
    sys.exit(f"ticker not found: {s}")


def filings(t: str, form: str | None, n: int) -> list[dict]:
    c = cik(t)
    sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{c}.json"))
    r = sub["filings"]["recent"]
    out = []
    for i in range(len(r["form"])):
        if form and r["form"][i] != form:
            continue
        acc = r["accessionNumber"][i]
        out.append({
            "form": r["form"][i],
            "filed": r["filingDate"][i],
            "period": r["reportDate"][i],
            "accession": acc,
            "url": (f"https://www.sec.gov/Archives/edgar/data/{int(c)}/"
                    f"{acc.replace('-', '')}/{r['primaryDocument'][i]}"),
        })
        if len(out) >= n:
            break
    return out


def facts(t: str, concept: str | None) -> dict:
    c = cik(t)
    if concept:
        url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{c}/us-gaap/{concept}.json"
    else:
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json"
    return json.loads(get(url))


def to_text(body: bytes) -> str:
    """Strip HTML/iXBRL tags to plain text, collapse whitespace."""
    t = body.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style|ix:header).*?</\1>", " ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t))


def grep(text: str, terms: list[str], ctx: int) -> None:
    for term in terms:
        hits = [m.start() for m in re.finditer(re.escape(term), text, re.I)]
        print(f"== {term!r}: {len(hits)} hit(s)")
        for i in hits:
            print(f"[@{i}] ..." + text[max(0, i - ctx): i + len(term) + ctx] + "...")


def main() -> None:
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("cik").add_argument("t")
    f = sp.add_parser("filings")
    f.add_argument("t"); f.add_argument("--form"); f.add_argument("--n", type=int, default=10)
    x = sp.add_parser("facts")
    x.add_argument("t"); x.add_argument("--concept")
    d = sp.add_parser("doc")
    d.add_argument("url"); d.add_argument("--out")
    d.add_argument("--grep", action="append"); d.add_argument("--ctx", type=int, default=400)
    a = p.parse_args()

    if a.cmd == "cik":
        print(cik(a.t))
    elif a.cmd == "filings":
        print(json.dumps(filings(a.t, a.form, a.n), indent=1, ensure_ascii=False))
    elif a.cmd == "facts":
        res = facts(a.t, a.concept)
        if not a.concept:   # full companyfacts is large: list concepts only
            res = {"entity": res.get("entityName"),
                   "us-gaap": sorted(res.get("facts", {}).get("us-gaap", {}))}
        print(json.dumps(res, indent=1, ensure_ascii=False))
    elif a.cmd == "doc":
        body = get(a.url)
        if a.grep:
            text = to_text(body)
            print(f"{len(text)} chars plain text")
            grep(text, a.grep, a.ctx)
        elif a.out:
            open(a.out, "wb").write(body)
            print(f"{len(body)} B -> {a.out}")
        else:
            sys.stdout.write(body.decode("utf-8", "replace"))


if __name__ == "__main__":
    main()
