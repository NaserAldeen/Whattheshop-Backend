from django.contrib import admin
from .models import Category, Product, Profile, Cart, CartItem


class CartItemInline(admin.TabularInline):
	model = CartItem

class CartAdmin(admin.ModelAdmin):
	list_display=('profile','completed')
	inlines = [
		CartItemInline,
	]

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Cart, CartAdmin)