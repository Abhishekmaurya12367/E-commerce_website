from django.contrib import admin
from .models import Product,variation

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','slug','discription','price','image','stock','is_available','category','created_date','modified_date')
    prepopulated_fields={'slug':('product_name',)}

class variation(admin.ModelAdmin):
    list_display=('product','slug','discription','price','image','stock','is_available','category','created_date')
    prepopulated_fields={'slug':('product_name',)}

   
admin.site.register(Product, ProductAdmin)
admin.site.register(variation)
