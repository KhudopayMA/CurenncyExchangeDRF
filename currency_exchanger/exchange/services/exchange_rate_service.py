from exchange.dto.exchange_rate_dto import CreateExchangeRateDTO, ExchangeRateDto
from exchange.exceptions.database_operation_exception import NotFound
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

    @staticmethod
    def get_exchange_rate(code_pair: str) -> ExchangeRate:
        base_currency = CurrencyRepository.get(
            code=code_pair[0:3]
        )
        target_currency = CurrencyRepository.get(
            code=code_pair[3:6]
        )
        try:
            exchange_rate = ExchangeRateRepository.get(
                base_currency_id=base_currency.id,
                target_currency_id=target_currency.id,
            )
        except NotFound:
            raise NotFound("Exchange rate for code pair not found")
        return exchange_rate
