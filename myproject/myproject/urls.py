from django.contrib import admin
from django.urls import path
from myapp.views import home, products, add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # This maps the root URL to your home view
    path('products/', products, name='products'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]
