from typing import final
from dataclasses import dataclass


@final
@dataclass(slots=True, frozen=True)
class CurrencyDto:
    """
    Dto contains all field of currency model except id
    """
    name: str
    code: str
    sign: str
