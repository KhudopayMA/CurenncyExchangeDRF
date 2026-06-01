from dataclasses import asdict

from django.db import IntegrityError

from exchange.exceptions import DatabaseOperationException
from exchange.exceptions.database_operation_exception import NotFound
from exchange.models import Currency
from exchange.dto import CurrencyDto


class CurrencyRepository:

    @staticmethod
    def get_all() -> list[Currency]:
        """
            Returns all currencies.
        Returns:
            list[Currency]
        """
        return list(Currency.objects.all())

    @staticmethod
    def create(data: CurrencyDto) -> Currency:
        """

        Args:
            data (CurrencyDto): CurrencyDto object with data for currency creation

        Returns:
            Currency: created currency object

        Raises:
            DatabaseOperationException: It is called in case of database errors and contains a message with
             a domain description of the cause of the error, abstracting from the technical part.
        """
        try:
            return Currency.objects.create(**asdict(data))
        except IntegrityError as e:
            error_msg = str(e)
            if "UNIQUE constraint failed" in error_msg:
                filed = error_msg.split(".")[-1].lower()
                raise DatabaseOperationException(
                    f"Field {filed} with value {getattr(data, filed)} already exists."
                )

    @staticmethod
    def get_by_code(code: str) -> Currency:
        """
        Find currency by code and return it.

        Args:
            code (str): Currency code

        Returns:
            Currency: found currency

        Raises:
            Currency.DoesNotExist: Raised if Currency not found
        """
        try:
            return Currency.objects.get(code)
        except Currency.DoesNotExist:
            raise NotFound(f"Currency with code {code} not found")

