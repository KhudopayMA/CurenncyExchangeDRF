from exchange.dto.exchange_rate_dto import CreateExchangeRateDTO, ExchangeRateDto
from exchange.models import ExchangeRate
from exchange.repository import CurrencyRepository, ExchangeRateRepository

class ExchangeRateService:

    @staticmethod
    def create_exchange_rate(dto: CreateExchangeRateDTO) -> ExchangeRate:
        base_currency = CurrencyRepository.get(
            code=dto.base_currency_code
        )
        target_currency = CurrencyRepository.get(
            code=dto.target_currency_code
        )
        exchange_rate_dto = ExchangeRateDto(
            base_currency_id=base_currency.id,
            target_currency_id=target_currency.id,
            rate=dto.rate,
        )
        exchange_rate = ExchangeRateRepository.create(exchange_rate_dto)
        return exchange_rate
