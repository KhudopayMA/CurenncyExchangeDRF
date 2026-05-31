from dataclasses import dataclass
from decimal import Decimal

from exchange.models import Currency


@dataclass
class ExchangeRateDto:
    base_currency: Currency
    target_currency: Currency
    rate: Decimal
    amount: Decimal
    converted_amount: Decimal


@dataclass
class GetExchangeDto:
    from_currency_code: str
    to_currency_code: str
    amount: Decimal
