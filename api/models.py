from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(blank=True)

	def __str__(self):
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	bio = models.TextField()
	phone_num = models.CharField(max_length=8)
	gender = models.CharField(max_length=10)
	image = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.user.username

class Cart(models.Model):
	profile = models.OneToOneField(Profile, related_name='cart', on_delete=models.CASCADE)

	def __str__(self):
		return self.profile.user.username

class Product(models.Model):
	price = models.PositiveIntegerField()
	name = models.CharField(max_length=100)
	quantity = models.PositiveIntegerField()
	manufacturer = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(blank=True, null=True)
	category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class CartItem(models.Model):
	item = models.OneToOneField(Product, on_delete=models.CASCADE)
	cart = models.ForeignKey(Cart, related_name="products", on_delete=models.CASCADE)

	def __str__(self):
		return self.item.name