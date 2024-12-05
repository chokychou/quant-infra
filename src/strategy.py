from abc import ABC
from dataclasses import dataclass
from src.market import Order, Position, Market, Option, Instrument


class Strategy(ABC):
    """Defines a trading strategy interface."""

    pass


class HedgeRolling(Strategy):

    option = Option()

    @staticmethod
    def _IsOkToHedgeDown(position: Position, market: Market) -> bool:
        """Fine tune"""
        return True

    @staticmethod
    def _IsOkToTradeUp(position: Position, market: Market) -> bool:
        """Fine tune"""
        NotImplemented

    def HasSatisfiedCondition(self, position: Position, market: Market) -> bool:
        option = self.option
        if not option.IsPutOption(position.instrument):
            return False
        match option.CalculatePutOptionState(position, market):
            case option.OptionState.ATM:
                return False
            case option.OptionState.ITM:
                return True if self._IsOkToHedgeDown(position, market) else False
            case option.OptionState.OTM:
                return True if self._IsOkToTradeUp(position, market) else False
            case option.OptionState.UNKNOWN:
                return False
            case _:
                raise Exception("HedgeRolling encounters an unexpected option state.")

    @staticmethod
    def CreateOrder(position: Position, market: Market) -> Order:
        """stack same quantities to the next OTM, create a vertical roll
        Args:
            position: of the put position.
            market: of the stock at market value.
        """
        order = Order()
        # sell to close
        order.instrument.append(position)
        order.options.append(Order.Options(sell_quantity=position.number.long_quantity))
        # buy to open
        order.instrument.append(market.nextOtmInstrument)
        order.options.append(Order.Options(buy_quantity=position.number.long_quantity))

        return order

    def Run(self, position: Position, market: Market) -> None:
        """
        Args:
            position: of the put position.
            market: of the stock at market value.
        """
        # Step 1: create an order
        if not self.HasSatisfiedCondition(position, market):
            return
        order = self.CreateOrder(position, market)
        # step 2: if there is an existing open order before, cancel that and replace with the new one
        order.CancelAllPendingOrders()
        order.PlaceOrder()
