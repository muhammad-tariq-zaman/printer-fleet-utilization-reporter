"""Report printer fleet utilisation and flag over/under-used printers.

Usage: python3 main.py printers.csv
CSV columns: printer,model,pages_per_month,rated_monthly_capacity.
Utilisation % = pages per month / rated monthly capacity x 100.
- OVERUSED: utilisation at or above 90% - the printer is near its
  rated duty cycle; move load or plan a replacement.
- UNDERUSED: utilisation below 10% - the printer is barely used;
  consider relocating or retiring it.
- OK: between 10% and 90%.
Highest utilisation first.
"""
import argparse, csv, sys

def report(rows):
    out = []
    for row in rows:
        pages = int(row["pages_per_month"])
        capacity = int(row["rated_monthly_capacity"])
        pct = round(pages / capacity * 100, 1) if capacity else 0.0
        if pct >= 90:
            verdict = "OVERUSED"
        elif pct < 10:
            verdict = "UNDERUSED"
        else:
            verdict = "OK"
        out.append((row["printer"].strip(), row["model"].strip(),
                    pages, capacity, pct, verdict))
    return sorted(out, key=lambda r: (-r[4], r[0]))

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        results = report(list(csv.DictReader(f)))
    for printer, model, pages, capacity, pct, verdict in results:
        print(f"{printer} ({model}): {verdict} ({pages}/{capacity} pages, {pct:.1f}% utilisation)")
    print(f"{sum(1 for *_, v in results if v == 'OVERUSED')} overused, "
          f"{sum(1 for *_, v in results if v == 'UNDERUSED')} underused.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
