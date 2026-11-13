# printer-fleet-utilization-reporter

Report printer fleet utilisation from a CSV: utilisation % = pages per month / rated monthly capacity × 100 — OVERUSED at or above 90%, UNDERUSED below 10%, otherwise OK, highest utilisation first.

Sample input is included (sample.csv with three printers).

## How to run

```sh
python3 main.py sample.csv
```

## Example output

```
PRN-1 (HP LaserJet Pro): OVERUSED (45000/50000 pages, 90.0% utilisation)
PRN-3 (Brother HL-L5100): OK (15000/30000 pages, 50.0% utilisation)
PRN-2 (HP LaserJet Pro): UNDERUSED (2000/50000 pages, 4.0% utilisation)
1 overused, 1 underused.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
