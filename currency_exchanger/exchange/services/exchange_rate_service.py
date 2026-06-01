from typing import Optional

from exchange.dto.exchange_rate_dto import CreateExchangeRateDTO, ExchangeRateDto, UpdateExchangeRateDTO
from exchange.exceptions.database_operation_exception import NotFound
from exchange.models import ExchangeRate
from exchange.repository import CurrencyRepository, ExchangeRateRepository


class ExchangeRateService:

    @staticmethod
    def create_exchange_rate(dto: CreateExchangeRateDTO) -> ExchangeRate:
        """
        Contains buisness logic of exchange rate creation.

        Args:
            dto (CreateExchangeRateDTO): CreateExchangeRateDTO object with data for currency creation

        Returns:
            ExchangeRate: created exchange rate
        """
        base_currency = CurrencyRepository.get_by_code(
            code=dto.base_currency_code
        )
        target_currency = CurrencyRepository.get_by_code(
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
    def get_exchange_rate(code_pair: str) -> Optional[ExchangeRate]:
        """
        Contains buisness logic of get exchange rate by code pair.

        Args:
            code_pair (str): currencies code_pair

        Returns:
            ExchangeRate: found exchange rate
        """
        base_currency = CurrencyRepository.get_by_code(
            code=code_pair[0:3]
        )
        target_currency = CurrencyRepository.get_by_code(
            code=code_pair[3:6]
        )
        try:
            exchange_rate = ExchangeRateRepository.get(
                base_currency_id=base_currency.id,
                target_currency_id=target_currency.id,
            )
            return exchange_rate
        except NotFound:
            return None

    @staticmethod
    def update_exchange_rate(dto: UpdateExchangeRateDTO) -> ExchangeRate:
        """
        Contains buisness logic of update exchange rate.

        Args:
            dto (UpdateExchangeRateDTO): UpdateExchangeRateDTO object with data for currency update

        Returns:
            ExchangeRate: updated exchange rate
        """
        base_currency = CurrencyRepository.get_by_code(
            code=dto.base_currency_code
        )
        target_currency = CurrencyRepository.get_by_code(
            code=dto.target_currency_code
        )
        exchange_rate_dto = ExchangeRateDto(
            base_currency_id=base_currency.id,
            target_currency_id=target_currency.id,
            rate=dto.rate,
        )
        try:
            exchange_rate = ExchangeRateRepository.update(exchange_rate_dto)
        except NotFound:
            raise NotFound("Exchange rate for code pair not found")
        return exchange_rate
