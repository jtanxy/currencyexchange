from django.urls import path
from .views import CurrencyPairList


urlpatterns = [
    path("currency/", CurrencyPairList.as_view(), name="currency"),
]
