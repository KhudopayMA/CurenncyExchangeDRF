from typing import Optional

from exchange.dto import GetExchangeDto, ExchangeRateDto
from exchange.exceptions.database_operation_exception import NotFound
from exchange.services import ExchangeRateService


class ExchangeService:

    @classmethod
    def get_exchange(cls, dto: GetExchangeDto) -> ExchangeRateDto:
        exchange_rate = cls.__get_exchange_by_direct_exchange_rate(dto)
        if exchange_rate:
            return exchange_rate
        exchange_rate = cls.__get_exchange_by_reverse_exchange_rate(dto)
        if exchange_rate:
            return exchange_rate
        exchange_rate = cls.__get_cross_exchange_by_base_usd(dto)
        if exchange_rate:
            return exchange_rate
        raise NotFound("Exchange rate not found.")

    @classmethod
    def __get_exchange_by_direct_exchange_rate(cls, dto: GetExchangeDto) -> Optional[ExchangeRateDto]:
        exchange_rate = ExchangeRateService.get_exchange_rate(dto.from_currency_code + dto.to_currency_code)
        if exchange_rate is None:
            return None
        converted_amount = exchange_rate.rate * dto.amount
        return ExchangeRateDto(
            base_currency=exchange_rate.base_currency,
            target_currency=exchange_rate.target_currency,
            rate=exchange_rate.rate,
            amount=dto.amount,
            converted_amount=converted_amount
        )

    @classmethod
    def __get_exchange_by_reverse_exchange_rate(cls, dto: GetExchangeDto) -> Optional[ExchangeRateDto]:
        exchange_rate = ExchangeRateService.get_exchange_rate(dto.to_currency_code + dto.from_currency_code)
        if exchange_rate is None:
            return None
        converted_amount = 1 / exchange_rate.rate * dto.amount
        return ExchangeRateDto(
            base_currency=exchange_rate.target_currency,
            target_currency=exchange_rate.base_currency,
            rate=exchange_rate.rate,
            amount=dto.amount,
            converted_amount=converted_amount
        )

    @classmethod
    def __get_cross_exchange_by_base_usd(cls, dto: GetExchangeDto) -> Optional[ExchangeRateDto]:
        usd_to_base_currency_exchange = ExchangeRateService.get_exchange_rate("USD" + dto.from_currency_code)
        usd_to_target_currency_exchange = ExchangeRateService.get_exchange_rate("USD" + dto.to_currency_code)
        if usd_to_base_currency_exchange is None or usd_to_target_currency_exchange is None:
            return None
        rate = usd_to_target_currency_exchange.rate / usd_to_base_currency_exchange.rate
        converted_amount = dto.amount * rate
        return ExchangeRateDto(
            base_currency=usd_to_base_currency_exchange.target_currency,
            target_currency=usd_to_target_currency_exchange.target_currency,
            rate=rate,
            amount=dto.amount,
            converted_amount=converted_amount
        )
