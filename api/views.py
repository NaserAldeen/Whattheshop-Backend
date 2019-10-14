from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import CartListSerializer, UserCreateSerializer, ProductListSerializer,CartItemCreateSerializer, ProductDetailSerializer, MyTokenObtainPairSerializer
from .models import Product, Cart
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwner

class MyTokenObtainPairView(TokenObtainPairView):
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

class CartListView(ListAPIView):

	serializer_class=CartListSerializer
	permissions=[IsAuthenticated]

	def get_queryset(self):
		return Cart.objects.filter(profile=self.request.user.profile)

class CartItemCreateView(CreateAPIView):
	serializer_class = CartItemCreateSerializer

class CheckoutView(APIView):
	# permissions=[IsAuthenticated]
	def get(self, request, format=None):
		cart=Cart.objects.get(status=False, profile=request.user.profile)
		if len(cart.products.all())>0:
			cart.status = True
			cart.save()
			Cart.objects.create(profile=request.user.profile)
			return Response("Checked out successfully!")
		return Response("Add products to your cart")