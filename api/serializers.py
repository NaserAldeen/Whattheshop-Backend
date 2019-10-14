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

    class Meta:
        model = Product
        exclude = ['description', ]


class ProductDetailSerializer(serializers.ModelSerializer):
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


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


class CartItemCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CartItem
        fields = "__all__"


# class CartCreateSerializer(serializers.)