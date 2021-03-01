from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "R Shopping"
admin.site.index_title = "Manage R Shopping"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'category')
    search_fields = ('title', 'price', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)


