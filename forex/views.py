from rest_framework.generics import ListAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CurrencyPairsSerializer
from forex.models import CurrencyPairs

from forex.currencypairlist import save_currency_pairs


class CurrencyPairList(ListAPIView):
    queryset = CurrencyPairs.objects.all()
    serializer_class = CurrencyPairsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["symbol", "source_currency", "target_currency"]
    ordering_fields = ["source_currency"]
