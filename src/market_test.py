import unittest

from src.market import Option, Instrument, Position, Market

positions = [
    Position(
        instrument=Instrument(cusip="1", symbol="a", instrument_id="test_1"),
        number=Position.Number(market_value=100, strike_price=100),
    ),
    Position(
        instrument=Instrument(cusip="2", symbol="b", instrument_id="test_2"),
        number=Position.Number(market_value=110, strike_price=105),
    ),
    Position(
        instrument=Instrument(cusip="3", symbol="c", instrument_id="test_3"),
        number=Position.Number(market_value=90, strike_price=95),
    ),
    Position(
        instrument=Instrument(cusip="4", symbol="d", instrument_id="test_4"),
        number=Position.Number(market_value=120, strike_price=115),
    ),
    Position(
        instrument=Instrument(cusip="5", symbol="e", instrument_id="test_5"),
        number=Position.Number(market_value=80, strike_price=85),
    ),
]

markets = [
    Market(
        instrument=Instrument(cusip="1", symbol="a", instrument_id="test_1"),
        number=Market.Number(market_value=100),
    ),
    Market(
        instrument=Instrument(cusip="2", symbol="b", instrument_id="test_2"),
        number=Market.Number(market_value=110),
    ),
    Market(
        instrument=Instrument(cusip="3", symbol="c", instrument_id="test_3"),
        number=Market.Number(market_value=90),
    ),
    Market(
        instrument=Instrument(cusip="4", symbol="d", instrument_id="test_4"),
        number=Market.Number(market_value=120),
    ),
    Market(
        instrument=Instrument(cusip="5", symbol="e", instrument_id="test_5"),
        number=Market.Number(market_value=80),
    ),
]



class OptionTest(unittest.TestCase):

    tolerances = [0.05, 0.1, 0.2, 1]

    def test_UnkownPriceReturnsUnknownState(self):
        option = Option()
        self.assertEqual(
            option.CalculatePutOptionState(
                Position(
                    number=Position.Number(strike_price=100),
                ),
                Market(
                    number=Market.Number(),
                ),
            ),
            Option.OptionState.UNKNOWN,
        )
        self.assertEqual(
            option.CalculatePutOptionState(
                Position(
                    number=Position.Number(),
                ),
                Market(
                    number=Market.Number(market_value=100),
                ),
            ),
            Option.OptionState.UNKNOWN,
        )

    def test_SimpleOptionStateCoverageTest(self):
        option = Option()

        expected_result = [
            Option.OptionState.ATM,
            Option.OptionState.OTM,
            Option.OptionState.ITM,
            Option.OptionState.OTM,
            Option.OptionState.ITM,
        ]
        for p, m, e in zip(positions, markets, expected_result):
            self.assertEqual(option.CalculatePutOptionState(p, m), e)

    def test_PositiveTolerance(self):
        # 5% 10% 20% 100%
        NotImplemented

    def test_NegativeTolerance(self):
        # 5% 10% 20% 100 %
        NotImplemented

    def test_InfiteTolerance(self):
        NotImplemented


if __name__ == "__main__":
    unittest.main()
