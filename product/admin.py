from django.contrib import admin
from product.models import *



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('created_at',)
    search_fields = ('name', 'price')


admin.site.register(Product, ProductAdmin)