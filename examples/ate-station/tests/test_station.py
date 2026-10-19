import unittest
import station_run


class StationTest(unittest.TestCase):
    def test_runs_every_unit_and_point(self):
        res = station_run.run()
        self.assertEqual(len({u for u, *_ in res}), 16)
        self.assertEqual(len(res), 16 * 7)

    def test_check_limits(self):
        self.assertTrue(station_run.check("X", 3.3, low=3.2, high=3.4, uut=1))
        self.assertFalse(station_run.check("X", 3.45, low=3.2, high=3.4, uut=1))


if __name__ == "__main__":
    unittest.main()
