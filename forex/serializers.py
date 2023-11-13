from rest_framework import serializers
from forex.models import CurrencyPairs


class CurrencyPairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyPairs
        fields = "__all__"
