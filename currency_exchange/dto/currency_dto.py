from dataclasses import dataclass


@dataclass
class CurrencyDto:
    """
    Dto contains all field of currency model except id
    """
    name: str
    code: str
    sign: str
