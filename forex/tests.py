from django.test import TestCase
from forex.models import CurrencyPairs, DailyRates
from django.utils import timezone
from django.urls import reverse


class ForexTest(TestCase):
    # Test currencypairs
    def create_currencypairs(
        self, symbol="SGDMYR=X", source_currency="SGD", target_currency="MYR"
    ):
        return CurrencyPairs.objects.create(
            symbol=symbol,
            source_currency=source_currency,
            target_currency=target_currency,
        )

    def test_currencypairs_creation(self):
        cur = self.create_currencypairs()
        self.assertTrue(isinstance(cur, CurrencyPairs))
        self.assertEqual(cur.__str__(), cur.symbol)

    # Test dailyrates model
    def create_dailyrates(
        self,
        date=timezone.now(),
        high="3.4693",
        low="3.4617",
        close="3.4651",
        last_updated=timezone.now(),
    ):
        cur = self.create_currencypairs()
        return DailyRates.objects.create(
            currency_pairs=CurrencyPairs.objects.get(id=cur.id),
            date=date,
            high=high,
            low=low,
            close=close,
            last_updated=last_updated,
        )

    def test_dailyrates_creation(self):
        r = self.create_dailyrates()
        self.assertTrue(isinstance(r, DailyRates))
        self.assertEqual(r.__str__(), "SGDMYR=X")

    # Test GET API for currency list
    def test_currencypairs_list_view(self):
        cur = self.create_currencypairs()
        url = reverse("forex:currency")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        print(cur.symbol)
        print(resp.content)
        self.assertIn(cur.symbol.encode(), resp.content)
