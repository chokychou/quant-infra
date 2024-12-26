import src.asset_pb2 as asset_pb2

from dataclasses import dataclass
from enum import Enum


def LookupEquity(options: asset_pb2.Options) -> asset_pb2.Equity:
    NotImplemented


class Order:

    def __init__(self, order: asset_pb2.Order | None = None):
        self._order = order

    def PlaceOrder(self) -> None:
        NotImplemented

    def CancelOrder(self) -> None:
        NotImplemented

    def ReplaceOrder(self) -> None:
        NotImplemented

    def CancelAllPendingOrders(self) -> None:
        NotImplemented
