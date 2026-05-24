from dataclasses import dataclass

@dataclass
class CurrencyDto:
    name: str
    code: str
    sign: str