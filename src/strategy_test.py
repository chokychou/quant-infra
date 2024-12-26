import unittest
import src.asset_pb2 as asset_pb2

from src.strategy import HedgeRolling


class HedgeRollingTest(unittest.TestCase):

    def test_AtTheMoneyDoesNotSatisfyCondition(self):
        option = asset_pb2.Options(
            strike_price=100,
        )
        equity = asset_pb2.Equity(market_price=100)
        self.assertFalse(HedgeRolling().HasSatisfiedCondition(option, equity))

    def test_SatisfyConditionReturnTrue(self):
        option = asset_pb2.Options(
            strike_price=100,
        )
        equity = asset_pb2.Equity(market_price=90)
        self.assertTrue(HedgeRolling().HasSatisfiedCondition(option, equity))

    def test_OkToHedgeDownAndCreateOrder(self):
        NotImplemented

    def test_NotOkToTradeUpReturnsEmptyList(self):
        NotImplemented

    def test_NotOkToHedgeDownReturnsEmptyList(self):
        NotImplemented


if __name__ == "__main__":
    unittest.main()
