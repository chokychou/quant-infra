import src.asset_pb2 as asset_pb2

from abc import ABC
from dataclasses import dataclass
from src.market import Order


class Strategy(ABC):
    """Defines a trading strategy interface."""

    pass


class HedgeRolling(Strategy):

    def HasSatisfiedCondition(
        self,
        option: asset_pb2.Options,
        market: asset_pb2.Equity,
        tolerance: float = 0.0,
    ) -> bool:
        # Equivalent to: (p - m*t) - m
        diff = market.market_price - option.strike_price * (1 + tolerance)
        return abs(diff) > 0

    @staticmethod
    def CreateOrder(option: asset_pb2.Options) -> Order:
        """Build bear put spread if bullish and bull put spread if bearish.

        Args:
            position: of the put position.
            market: of the stock at market value.
        """
        NotImplemented

    def Run(self, portfolio: asset_pb2.Portfolio) -> None:
        """Main function

        If the position is a put option, create an order to hedge.

        Args:
            portfolio: account portfolio.
            market: of the stock at market value.
        """
        for position in portfolio.positions:
            if not position.options:
                return
            options = position.options
            if options.option_type != asset_pb2.Options.OptionType.PUT:
                return
            ref_equity = LookupEquity(options)

            # Step 1: create an order
            if not self.HasSatisfiedCondition(options, ref_equity):
                return
            order = self.CreateOrder(options)

            # step 2: if there is an existing open order before, cancel that and replace with the new one
            order.CancelAllPendingOrders()
            order.PlaceOrder()
