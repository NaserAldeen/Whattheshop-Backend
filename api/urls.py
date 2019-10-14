from django.urls import path
from .views import UserCreateAPIView,CartItemCreateView, CheckoutView,ProductListView, ProductDetailView, MyTokenObtainPairView, CartListView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ProductListView.as_view(), name='list-view'),
    path('detail/<int:product_id>/',
         ProductDetailView.as_view(), name='detail-view'),
    path('cart_list/',
         CartListView.as_view(), name='cart-list'),
    path('add_product/',
         CartItemCreateView.as_view(), name='item-create'),

    path('checkout/',
         CheckoutView.as_view(), name='checkout'),

]
