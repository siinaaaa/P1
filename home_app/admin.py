from django.contrib import admin
from .models import Color, Size, Product, Order, Category, Contact

admin.site.register(Color)
admin.site.register(Size)

admin.site.register(Category)


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price']
    list_per_page = 10
    list_filter = ['category']
    search_fields = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subj']
    list_per_page = 10
    search_fields = ('subj', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['username', 'quantity', 'product_name']
    list_per_page = 10
    list_filter = ['quantity']
    search_fields = ('product_name',)
