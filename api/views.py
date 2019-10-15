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

class PreviousOrdersListView(ListAPIView):
	serializer_class=CartListSerializer
	permissions=[IsAuthenticated]

	def get_queryset(self):
		return Cart.objects.filter(profile=self.request.user.profile, completed=True)

class UserCart(ListAPIView):
	serializer_class=CartListSerializer
	permissions=[IsAuthenticated]

	def get_queryset(self):
		return Cart.objects.filter(profile=self.request.user.profile, completed=False)

class CartItemCreateView(APIView):
	

	def post(self, request, format=None):
		if (request.user.is_anonymous):
			return Response("Please login in order to add to your cart")

		validated_data = request.data
		product_id = int(validated_data["item"])
		quantity = int(validated_data['quantity'])

		cart, created = Cart.objects.get_or_create(profile=request.user.profile, completed=False)
		# cart_item, created2 = CartItem.objects.get_or_create(item__id=product_id, cart=cart)
		cart_item = CartItem.objects.filter(item__id=product_id, cart=cart)
		if quantity == 0:
			if not cart_item.exists():
				return Response("You can't add 0 products to the cart!")
			elif cart_item.exists():
				cart_item.delete() 
				return Response("Item deleted")
		elif quantity > 0:	
			if created:
				cart.profile = request.user.profile
				cart.save()

			if not cart_item.exists():
				cart_item = CartItem.objects.create(item=Product.objects.get(id=product_id), cart=cart, quantity=int(validated_data['quantity']))
			else:
				cart_item = cart_item[0]
				cart_item.quantity = quantity
				cart_item.save()
			return Response(CartItemCreateSerializer(cart_item).data)
		
		

		
	


class CheckoutView(APIView):
	def get(self, request, format=None):
		if request.user.is_anonymous:
			return Response("What are you doing bro?")
		cart=Cart.objects.filter(completed=False, profile=request.user.profile)
		if not cart: return Response("What are you doing bro? You can't checkout when you don't have items in your cart!")
		cart=cart[0]
		if cart.products.all().exists():
			for cart_item in cart.products.all():
				prod = cart_item.item
				prod.quantity = prod.quantity-cart_item.quantity
				prod.save()
			cart.completed = True
			cart.save()
			# Cart.objects.create(profile=request.user.profile)
			return Response("Checked out successfully!")
		return Response("Add products to your cart")