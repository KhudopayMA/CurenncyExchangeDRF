from django.db import models

from currency_exchange.models import Currency


class ExchangeRate(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        db_column='ID'
    )
    base_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        db_column='BaseCurrencyId',
        related_name='base_currencies'
    )
    target_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        db_column='TargetCurrencyId',
        related_name='target_currencies'
    )
    rate = models.DecimalField(
        decimal_places=6,
        max_digits=10,
        db_column='Rate'
    )

    class Meta:
        db_table = "ExchangeRates"
        constraints = [
            models.UniqueConstraint(
                fields=['base_currency_id', 'target_currency_id'],
                name='target_currency_id_base_currency'
            )
        ]