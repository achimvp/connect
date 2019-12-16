from django.urls import path
from .views import ProductDetailView, ProductCreateView, ProductListView
from .views import product_list

urlpatterns = [
   # path('', product_list, name="products"),
    path('product-list/', ProductListView.as_view(
            template_name="products/product_list.html",
        ), name="product-list"
    ),
    path('detail/<int:pk>/', ProductDetailView.as_view(
            template_name="products/product_detail.html"
        ), name="product-detail"
    ),
    path('add/', ProductCreateView.as_view(
            template_name = 'products/create_new_product.html'
        ), name='add-product'
    ),
]
