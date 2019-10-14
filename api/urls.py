from django.urls import path
from .views import UserCreateAPIView, ProductListView, ProductDetailView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', ProductListView.as_view(), name='list-view'),
    path('detail/<int:product_id>/',
         ProductDetailView.as_view(), name='detail-view'),

]
