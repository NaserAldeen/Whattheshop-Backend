from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
	UserCreateAPIView,CartItemCreateView, CheckoutView,ProductListView,
	ProductDetailView, MyTokenObtainPairView, CartListView
)


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('products/', ProductListView.as_view(), name='list-view'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='detail-view'),
    path('cart_list/', CartListView.as_view(), name='cart-list'),
    path('add_product/', CartItemCreateView.as_view(), name='item-create'),

    path('checkout/', CheckoutView.as_view(), name='checkout'),

]
