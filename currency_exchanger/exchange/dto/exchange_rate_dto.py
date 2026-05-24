from dataclasses import dataclass

from exchange.models import Currency


@dataclass
class ExchangeRateDto:
    base_currency: Currency
    target_currency: Currency
    rate: float

@dataclass
class RequestExchangeRateDto:
    base_currency_id: int
    target_currency_id: int
    rate: float