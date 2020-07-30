from django.contrib import admin
from .models import Stock,Category
from .forms import StockCreateForm
# Register your models here.
class StockCreateAdmin(admin.ModelAdmin):
    form = StockCreateForm
    list_display = ['category','product_name','quantity']
    list_filter = ['category']
    search_fields = ['category','product_name']


admin.site.register(Stock,StockCreateAdmin)
admin.site.register(Category)


