import unittest

from src.market import Option, Instrument, Position, Market
from src.strategy import HedgeRolling


class HedgeRollingTest(unittest.TestCase):
    
    def test_PutOptionDoesNotSatisfyCondition(self):
        strat = HedgeRolling()
        self.assertFalse(strat.HasSatisfiedCondition(Position(), Market()))

    def test_SatisfyConditionReturnFalse(self):
        instrument = Instrument(
            instrument_type=Instrument.InstrumentType.PUT_OPTION
        )
        position = Position(
            instrument=instrument,
            number=Position.Number(strike_price=100)
        )
        market = Market(
            instrument= instrument,
            number=Market.Number(market_value=100)
        )
        strat = HedgeRolling()
        self.assertFalse(strat.HasSatisfiedCondition(position, market))

    def test_SatisfyConditionReturnTrue(self):
        instrument = Instrument(
            instrument_type=Instrument.InstrumentType.PUT_OPTION
        )
        position = Position(
            instrument=instrument,
            number=Position.Number(strike_price=100)
        )
        market = Market(
            instrument= instrument,
            number=Market.Number(market_value=95),
        )
        strat = HedgeRolling()
        self.assertTrue(strat.HasSatisfiedCondition(position, market))

    def test_OkToHedgeDownAndCreateOrder(self):
        NotImplemented

    def test_NotOkToTradeUpReturnsEmptyList(self):
        NotImplemented

    def test_NotOkToHedgeDownReturnsEmptyList(self):
        NotImplemented


if __name__ == "__main__":
    unittest.main()
