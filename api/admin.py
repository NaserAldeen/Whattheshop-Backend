from django.contrib import admin
from .models import Category, Product, Profile, Cart, CartItem, Manufacturer

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'phone_number','gender')

class CartItemInline(admin.TabularInline):
	model = CartItem
	extra = 1


class ProductInline(admin.TabularInline):
	model = Product
	extra = 1


class CartAdmin(admin.ModelAdmin):
	list_display = ('profile','completed')
	list_filter = ('completed', )
	readonly_fields = ("Phone", "Name", "Email")
	inlines = [
		CartItemInline
	]

	def Phone(self, obj):
		return obj.profile.phone_number
	def Name(self, obj):
		return obj.profile.user.first_name + " " + obj.profile.user.last_name
	def Email(self,obj): 
		return obj.profile.user.email


  
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'quantity',)
	list_filter = ('category', 'manufacturer')



admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Manufacturer)