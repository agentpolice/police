"""Station run: 16 boards in parallel, 7 test points each."""
from station.instruments import Bench

results = []


def check(name, value, low, high, uut):
    ok = low <= value <= high
    results.append((uut, name, value, ok))
    return ok


def run(bench=None):
    bench = bench or Bench()
    results.clear()
    for ch in range(1, 17):
        bench.route(ch)
        check("VCC_3V3", bench.measure("VCC_3V3"), low=3.20, high=3.40, uut=ch)
        check("VIN_12V", bench.measure("VIN_12V"), low=11.40, high=12.60, uut=ch)
        check("VDD_CORE", bench.measure("VDD_CORE"), low=1.17, high=1.23, uut=ch)
        check("I_STBY", bench.measure("I_STBY"), low=0.00, high=12.0, uut=ch)
        check("CLK_FREQ", bench.measure("CLK_FREQ"), low=24.99, high=25.01, uut=ch)
        check("RST_HIGH", bench.measure("RST_HIGH"), low=2.90, high=3.40, uut=ch)
        check("RIPPLE_3V3", bench.measure("RIPPLE_3V3"), low=0.00, high=30.0, uut=ch)
    return results


if __name__ == "__main__":
    res = run()
    units = sorted({u for u, *_ in res})
    bad = sorted({u for u, _, _, ok in res if not ok})
    for u, name, v, ok in res:
        if not ok:
            print(f"FAIL  UUT{u:02d}  {name} = {v}")
    print(f"{len(units) - len(bad)}/{len(units)} PASS · {len(res)} tests")
