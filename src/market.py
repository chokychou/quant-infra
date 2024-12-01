from dataclasses import dataclass
from enum import Enum


@dataclass
class Instrument:
    cusip: str | None = None
    symbol: str | None = None
    instrument_id: str | None = None


class Order:

    @dataclass
    class Options:
        long_quantity: int = 0

    instrument: Instrument | None = None
    options: Options | None = None

    def PlaceOrder(self) -> None:
        NotImplemented

    def CancelOrder(self) -> None:
        NotImplemented

    def ReplaceOrder(self) -> None:
        NotImplemented


@dataclass
class Position:

    @dataclass
    class Number:
        short_quantity: int = 0
        long_quantity: int = 0
        average_price: float = 0.0
        market_value: float = 0.0
        strike_price: float = 0.0

    instrument: Instrument | None = None
    number: Number | None = None


@dataclass
class Market:

    @dataclass
    class Number:
        market_value: float = 0.0

    instrument: Instrument | None = None
    number: Number | None = None
    nextOtmInstrument: Instrument | None = None


class Greeks:
    NotImplemented


class Option:

    class OptionState(Enum):
        ATM = 1
        ITM = 2
        OTM = 3
        UNKNOWN = 100

    def IsPutOption(self, instrument: Instrument) -> bool:
        NotImplemented

    def CalculatePutOptionState(
        self, position: Position, market: Market, tolerance=0
    ) -> OptionState:
        """Computes option state based on defition, and deviates with tolerance.

        Args:
            position: of the put position.
            market: of the stock at market value.
            tolerance: A percentage of risk tolerance that we count towards ATM. Use this as an adjustment factor to fine-tune the strategy.
        """
        if market.number.market_value == 0 or position.number.strike_price == 0:
            return self.OptionState.UNKNOWN

        # Equivalent to: (p - m*t) - m
        diff = market.number.market_value - position.number.strike_price * (
            1 + tolerance
        )

        if diff == 0:
            return self.OptionState.ATM
        elif diff > 0:
            return self.OptionState.OTM
        else:
            return self.OptionState.ITM
