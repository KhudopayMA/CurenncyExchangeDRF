from django.db import models


class Currency(models.Model):
    id = models.BigAutoField(
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
