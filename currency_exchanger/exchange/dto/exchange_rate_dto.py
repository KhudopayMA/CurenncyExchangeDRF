from dataclasses import dataclass
from decimal import Decimal

from exchange.models import Currency


@dataclass
class ExchangeRateDto:
    base_currency_id: int
    target_currency_id: int
    rate: Decimal

@dataclass
class GetRequestExchangeRateDto:
    base_currency_id: int
    target_currency_id: int
    rate: Decimal

@dataclass
class CreateExchangeRateDTO:
    base_currency_code: str
    target_currency_code: str
    rate: Decimal

@dataclass
class UpdateExchangeRateDTO:
    base_currency_code: str
    target_currency_code: str
    rate: Decimal

