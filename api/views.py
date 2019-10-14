from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import CartListSerializer, UserCreateSerializer, ProductListSerializer,CartItemCreateSerializer, ProductDetailSerializer, MyTokenObtainPairSerializer
from .models import Product, Cart, CartItem
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

class CartItemCreateView(APIView):
	

	def post(self, request, format=None):

		validated_data = request.data
		cart_id = int(validated_data['cart'])
		product_id = int(validated_data["item"])
		quantity = int(validated_data['quantity'])

		cart, created1 = Cart.objects.get_or_create(profile__user=request.user, status=False)
		cart_item, created2 = CartItem.objects.get_or_create(item__id=product_id, cart=cart)
		
		if created1:
			cart.profile = request.user.profile
			cart.save()
		if created2:
			cart_item.item = Product.objects.get(id=product_id)
			cart_item.cart = cart
		elif quantity == 0:
			cart_item.delete() 
			return Response("Item deleted")
		
		cart_item.quantity = int(validated_data['quantity'])
		cart_item.save()
		return Response("Item created/updated")
	


class CheckoutView(APIView):
	def get(self, request, format=None):
		if request.user.is_anonymous:
			return Response("What are you doing bro?")
		cart=Cart.objects.get(status=False, profile=request.user.profile)
		if cart.products.all().exists():
			for cart_item in cart.products.all():
				prod = cart_item.item
				prod.quantity = prod.quantity-cart_item.quantity
				prod.save()
			cart.status = True
			cart.save()
			# Cart.objects.create(profile=request.user.profile)
			return Response("Checked out successfully!")
		return Response("Add products to your cart")