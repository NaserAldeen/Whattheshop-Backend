from django.contrib import admin
from .models import Category, Product, Profile, Cart, CartItem


class CartItemInline(admin.TabularInline):
	model = CartItem

	def get_extra(self, request, obj=None, **kwargs):
		return 1


class ProductInline(admin.TabularInline):
	model = Product

	def get_extra(self, request, obj=None, **kwargs):
		return 1


class CartAdmin(admin.ModelAdmin):
	list_display=('profile','completed')
	inlines = [
		CartItemInline,
	]


class CategoryAdmin(admin.ModelAdmin):
	inlines = [
		ProductInline,
	]


class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'quantity','manufacturer')


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user','bio','phone_num','gender')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Cart, CartAdmin)
