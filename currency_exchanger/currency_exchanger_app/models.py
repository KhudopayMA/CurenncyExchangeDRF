from django.db import models

class Currency(models.Model):
    currency_id = models.BigAutoField(
        primary_key=True,
        unique=True,
        db_column='ID'
    )
    code = models.CharField(
        max_length=3,
        unique=True,
        db_column="Code"
    )
    name = models.CharField(
        max_length=100,
        unique=True,
        db_column="FullName"
    )
    sign = models.CharField(
        max_length=3,
        unique=True,
        db_column="Sign"
    )

    class Meta:
        db_table = "Сurrencies"

class ExchangeRate(models.Model):
    exchange_rate_id = models.BigAutoField(
        primary_key=True,
        db_column='ID'
    )
    base_currency_id = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        db_column='BaseCurrencyId',
        related_name='base_currencies'
    )
    target_currency_id = models.ForeignKey(
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
