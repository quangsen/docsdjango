from django.contrib import admin
from .models import Metric, Category, Datum


@admin.register(Category)
class CategoryAmdin(admin.ModelAdmin):
    list_display = ('name', 'position')


@admin.register(Datum)
class DatumAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'metric', 'measurement')


class MetricAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'position',
                    'show_on_dashboard', 'show_sparkline', 'period')

for MC in Metric.__subclasses__():
    admin.site.register(MC, MetricAdmin)



