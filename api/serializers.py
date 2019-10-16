from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Category, Cart, CartItem
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    manufacturer = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Product
        exclude = ['description', ]


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    manufacturer = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Product
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class CartItemCreateSerializer(serializers.ModelSerializer):
    # hash
    item = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    price = serializers.SerializerMethodField() 
    product_id = serializers.SerializerMethodField() 
    image = serializers.SerializerMethodField() 
    class Meta: 
        model = CartItem
        exclude = ["cart"]
    def get_price(self,obj):
        return obj.item.price

    def get_product_id(self,obj):
        return obj.item.id

    def get_image(self,obj):
        return self.context['request'].build_absolute_uri(obj.item.image.url)


class CartListSerializer(serializers.ModelSerializer):
    cart_items = CartItemCreateSerializer(many=True)
    total = serializers.SerializerMethodField()
    class Meta:
        model = Cart
        fields = "__all__"
    
    def get_total(self, obj):
        return sum([x.quantity*x.item.price for x in obj.cart_items.all()])



        



