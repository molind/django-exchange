from django.contrib import admin
from exchange.models import Currency, ExchangeRate

admin.site.register(Currency)
admin.site.register(ExchangeRate)
