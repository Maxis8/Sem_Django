from django.urls import path
from .views import my_view, OrderProductsView, ProductsByDateView, ProductView, UpProductView

urlpatterns = [

    path('', my_view, name='index'),
    path('order_list/<int:pk>', OrderProductsView.as_view(), name='order_list'),
    path('orders_by_year/<int:pk>/<int:year>', ProductsByDateView.as_view(), name='order_by_year'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_page'),
    path('up_product/<int:pk>/', UpProductView.as_view(), name='up_product'),
]

