from django.contrib import admin
from .models import Category, Product, Profile, Cart, CartItem


class CartItemInline(admin.TabularInline):
	model = CartItem
	extra = 1


class ProductInline(admin.TabularInline):
	model = Product
	extra = 1


class CartAdmin(admin.ModelAdmin):
	list_display = ('profile','completed')
	list_filter = ['completed', ]
	inlines = [
		CartItemInline,
	]


class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'quantity','manufacturer')
	list_filter = ['category']


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'phone_num','gender')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Cart, CartAdmin)