from dataclasses import dataclass
from decimal import Decimal
from typing import final


@final
@dataclass(slots=True, frozen=True)
class ExchangeRateDto:
    """
    Dto contains all field of exchange rate model except id
    """
    base_currency_id: int
    target_currency_id: int
    rate: Decimal


@final
@dataclass(slots=True, frozen=True)
class GetRequestExchangeRateDto:
    """
    Dto for get request of exchange rate
    """
    base_currency_id: int
    target_currency_id: int
    rate: Decimal


@final
@dataclass(slots=True, frozen=True)
class CreateExchangeRateDTO:
    """
    Dto for create request of exchange
    """
    base_currency_code: str
    target_currency_code: str
    rate: Decimal


@final
@dataclass(slots=True, frozen=True)
class UpdateExchangeRateDTO:
    """
    Dto for update request of exchange
    """
    base_currency_code: str
    target_currency_code: str
    rate: Decimal

