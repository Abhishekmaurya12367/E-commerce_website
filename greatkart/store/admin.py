from django.contrib import admin
from .models import Product,Variation

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','slug','discription','price','image','stock','is_available','category','created_date','modified_date')
    prepopulated_fields={'slug':('product_name',)}

class VariationAdmin(admin.ModelAdmin):
   list_display = (
        'product',
        'variation_category',
        'variation_value',
        'is_active',
        'created_date',
    )

   
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation,VariationAdmin)
