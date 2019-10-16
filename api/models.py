from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Category(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(blank=True)

	class Meta:
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name


class Profile(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	OTHER = 'O'
	GENDER_CHOICES = [
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		(OTHER, 'Other'),
	]
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	bio = models.TextField()
	phone_number = models.CharField(max_length=8)
	gender = models.CharField(
		max_length=2,
		choices=GENDER_CHOICES,
		default=MALE,
	)
	image = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.user.username


class Cart(models.Model):
	profile = models.ForeignKey(Profile, related_name='carts', on_delete=models.CASCADE, blank=True, null=True)
	completed = models.BooleanField(default=False)

	def complete(self):
		self.completed = True
		self.save()

	def __str__(self):
		return self.profile.user.username


# class Manufacturer(models.Model):
# 	name = models.CharField(max_length=50)

# 	def __str__(self):
# 		return self.name


class Product(models.Model):
	price = models.PositiveIntegerField()
	name = models.CharField(max_length=100)
	quantity = models.PositiveIntegerField()
	description = models.TextField()
	image = models.ImageField(blank=True, null=True)
	category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

	def update_quantity(self, quantity):
		self.quantity += quantity
		self.save()

	def __str__(self):
		return self.name



class CartItem(models.Model):
	item = models.ForeignKey(Product, related_name="cart_items", on_delete=models.CASCADE, blank=True, null=True)
	cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.item.name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)