from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from myapp.models import Product, Tag
import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class CartView(View):
    ...



class ProductTagsView(View):
    def get(self, request, *args, **kwargs):
        
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)

     
        tags = product.tags.all()
        tag_data = [{"tag_name": tag.name} for tag in tags]
        
        return JsonResponse({"tags": tag_data}, status=200)

    def post(self, request, *args, **kwargs):
      
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        
        
        data = json.loads(request.body)
        tag_name = data.get('tag_name')

        if not tag_name:
            return JsonResponse({"error": "tag_name is required"}, status=400)
        
        if product.tags.filter(name=tag_name).exists():
            return JsonResponse({"error": f"Tag '{tag_name}' already exists for this product."}, status=400)

        
        tag, created = Tag.objects.get_or_create(name=tag_name)
        product.tags.add(tag)

        return JsonResponse({"message": f"Tag '{tag_name}' added to product '{product.name}'"}, status=201)





@method_decorator(login_required, name='dispatch')
class ProductTagsView(View):
    ...




class FavoriteProductsView(View):
    def get(self, request, *args, **kwargs):

        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)


        favorite_products = FavoriteProduct.objects.filter(user=user)
        favorite_data = [
            {"product_name": fp.product.name, "price": float(fp.product.price)}
            for fp in favorite_products
        ]

        return JsonResponse({"favorite_products": favorite_data}, status=200)

    def post(self, request, *args, **kwargs):

        user_id = kwargs.get('user_id')
        product_id = json.loads(request.body).get('product_id')

        user = get_object_or_404(User, id=user_id)
        product = get_object_or_404(Product, id=product_id)


        if FavoriteProduct.objects.filter(user=user, product=product).exists():
            return JsonResponse({"error": "Product already in favorite list"}, status=400)


        FavoriteProduct.objects.create(user=user, product=product)

        return JsonResponse({"message": f"Product '{product.name}' added to favorite list"}, status=201)






@method_decorator(login_required, name='dispatch')
class FavoriteProductsView(View):
    ...


