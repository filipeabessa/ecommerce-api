from ecommerce.product.models import Product
from django.contrib import admin

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation', 'price')
    search_fields = ('title', 'price')
    ordering = ('-creation',)
    readonly_fields = ('creation',)
    

admin.site.register(Product, ProductAdmin)