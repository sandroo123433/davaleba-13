from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from myapp.models import Product, CartItem
import json
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"




class CartView(View):
    def get(self, request, *args, **kwargs):
        user = request.user 
        cart_items = CartItem.objects.filter(user=user)
        cart_data = [
            {
                "product": item.product.name,
                "price": float(item.product.price),
                "quantity": item.quantity,
                "total_price": float(item.product.price) * item.quantity
            }
            for item in cart_items
        ]
        return JsonResponse({"cart": cart_data}, status=200)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = json.loads(request.body)  

        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)  

        product = get_object_or_404(Product, id=product_id)

       
        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return JsonResponse(
            {"message": "Product added to cart", "product": product.name, "quantity": cart_item.quantity},
            status=201
        )




class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


    products = models.ManyToManyField(Product, related_name='tags')





class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class FavoriteProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

