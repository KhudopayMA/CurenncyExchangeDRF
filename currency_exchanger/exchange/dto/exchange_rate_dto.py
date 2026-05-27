from dataclasses import dataclass
from decimal import Decimal

from exchange.models import Currency


@dataclass
class ExchangeRateDto:
    base_currency_id: int
    target_currency_id: int
    rate: Decimal

@dataclass
class RequestExchangeRateDto:
    base_currency_id: int
    target_currency_id: int
    rate: Decimal

@dataclass
class CreateExchangeRateDTO:
    base_currency_code: str
    target_currency_code: str
    rate: Decimal
