from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','slug','discription','price','image','stock','is_available','category','created_date','modified_date')
    prepopulated_fields={'slug':('product_name',)}


   
admin.site.register(Product, ProductAdmin)