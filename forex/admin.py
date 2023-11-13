from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter

from .models import CurrencyPairs, DailyRates


class DailyRatesInline(admin.TabularInline):
    model = DailyRates

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    readonly_fields = ("date", "high", "low", "close", "last_updated")


class CurrencyPairsModelAdmin(admin.ModelAdmin):
    actions = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    search_fields = ["source_currency", "target_currency"]
    readonly_fields = ["symbol", "source_currency", "target_currency"]
    inlines = [DailyRatesInline]
    list_filter = (
        ("source_currency", DropdownFilter),
        ("target_currency", DropdownFilter),
    )


admin.site.register(CurrencyPairs, CurrencyPairsModelAdmin)
