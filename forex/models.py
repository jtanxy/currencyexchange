from django.db import models
from django.contrib import admin


class CurrencyPairs(models.Model):
    symbol = models.CharField(max_length=50, unique=True)
    source_currency = models.CharField(max_length=50)
    target_currency = models.CharField(max_length=50)

    def __str__(self):
        return str(self.symbol)


class DailyRates(models.Model):
    currency_pairs = models.ForeignKey(CurrencyPairs, on_delete=models.CASCADE)
    date = models.DateField()
    high = models.DecimalField(decimal_places=4, max_digits=11)
    low = models.DecimalField(decimal_places=4, max_digits=11)
    close = models.DecimalField(decimal_places=4, max_digits=11)
    last_updated = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["currency_pairs", "date"], name="unique_daily_rate"
            )
        ]

    def __str__(self):
        return str(self.currency_pairs)
