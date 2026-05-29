from exchange.dto import GetExchangeDto, ExchangeRateDto
from exchange.services import ExchangeRateService


class ExchangeService:

    @staticmethod
    def get_exchange(dto: GetExchangeDto) -> ExchangeRateDto:
        exchange_rate = ExchangeRateService.get_exchange_rate(dto.from_currency_code+dto.to_currency_code)
        converted_amount = exchange_rate.rate * dto.amount
        return ExchangeRateDto(
            base_currency=exchange_rate.base_currency,
            target_currency=exchange_rate.target_currency,
            rate=exchange_rate.rate,
            amount=dto.amount,
            converted_amount=converted_amount
        )
