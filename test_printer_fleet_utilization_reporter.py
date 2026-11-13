import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import report

def row(printer, model, pages, capacity):
    return {"printer": printer, "model": model,
            "pages_per_month": str(pages),
            "rated_monthly_capacity": str(capacity)}

class TestFleetUtilization(unittest.TestCase):
    def test_utilisation_computed(self):
        self.assertEqual(report([row("P-1", "HP", 15000, 30000)])[0][4], 50.0)

    def test_overused_at_90_percent(self):
        self.assertEqual(report([row("P-1", "HP", 45000, 50000)])[0][5], "OVERUSED")

    def test_underused_below_10_percent(self):
        self.assertEqual(report([row("P-1", "HP", 2000, 50000)])[0][5], "UNDERUSED")

    def test_ok_in_middle(self):
        self.assertEqual(report([row("P-1", "HP", 15000, 30000)])[0][5], "OK")

    def test_exactly_10_percent_is_ok(self):
        self.assertEqual(report([row("P-1", "HP", 5000, 50000)])[0][5], "OK")

    def test_zero_capacity_is_zero_percent(self):
        r = report([row("P-1", "HP", 100, 0)])[0]
        self.assertEqual((r[4], r[5]), (0.0, "UNDERUSED"))

    def test_highest_first(self):
        r = report([row("P-1", "HP", 1000, 50000), row("P-2", "HP", 40000, 50000)])
        self.assertEqual(r[0][0], "P-2")

    def test_empty_input(self):
        self.assertEqual(report([]), [])
