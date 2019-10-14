from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer, ProductListSerializer, ProductDetailSerializer, MyTokenObtainPairSerializer
from .models import Product
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    print("mi")
    serializer_class = MyTokenObtainPairSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'
