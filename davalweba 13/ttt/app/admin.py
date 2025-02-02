from django.contrib import admin
from myapp.models import Product, Tag

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)