from dataclasses import dataclass

from exchange.models import Currency


@dataclass
class ExchangeRateDto:
    base_currency: Currency
    target_currency: Currency
    rate: float
    amount: float
    converted_amount: float


@dataclass
class GetExchangeDto:
    from_currency_code: str
    to_currency_code: str
    amount: float
