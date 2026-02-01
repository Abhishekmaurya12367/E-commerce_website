from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('',views.store,name='store'),
    path('category/<slug:category_slug>/',views.store,name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name='product_by_detail'),
    path('search/',views.search,name='search'),
    
]
