
from product.views import product_list, product_detail
from second.urls import path

urlpatterns = [
    path("products/", product_list, name="product_list"),
    path("products/<slug:product_slug>", product_detail, name="product_detail"),
]