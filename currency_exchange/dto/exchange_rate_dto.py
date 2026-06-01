from dataclasses import dataclass
from decimal import Decimal


@dataclass
class ExchangeRateDto:
    """
    Dto contains all field of exchange rate model except id
    """
    base_currency_id: int
    target_currency_id: int
    rate: Decimal


@dataclass
class GetRequestExchangeRateDto:
    """
    Dto for get request of exchange rate
    """
    base_currency_id: int
    target_currency_id: int
    rate: Decimal


@dataclass
class CreateExchangeRateDTO:
    """
    Dto for create request of exchange
    """
    base_currency_code: str
    target_currency_code: str
    rate: Decimal


@dataclass
class UpdateExchangeRateDTO:
    """
    Dto for update request of exchange
    """
    base_currency_code: str
    target_currency_code: str
    rate: Decimal

