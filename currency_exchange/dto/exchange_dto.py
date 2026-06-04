from typing import final
from dataclasses import dataclass
from decimal import Decimal

from currency_exchange.models import Currency


@final
@dataclass(slots=True, frozen=True)
class GetExchangeResponseDto:
    """
    Dto contains all field of exchange rate model except id
    """
    base_currency: Currency
    target_currency: Currency
    rate: Decimal
    amount: Decimal
    converted_amount: Decimal


@final
@dataclass(slots=True, frozen=True)
class GetExchangeRequestDto:
    """
    Dto for get request of exchange
    """
    from_currency_code: str
    to_currency_code: str
    amount: Decimal
