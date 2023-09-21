from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class ProductView(APIView, PageNumberPagination):
    permission_classes = [AllowAny, ]
    page_size = 15
    def post(self, request, cat_id):
        cat_obj = Category.objects.get(id=cat_id)
        products_query = Product.objects.filter(category=cat_obj)
        result = self.paginate_queryset(products_query, request, view=self)
        ser_data = ProductSerializer(result, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
    
class SearchProductView(APIView, PageNumberPagination):
    permission_classes = [AllowAny, ]
    page_size = 15
    def get(self, request):
        search_word = request.GET["search_word"]
        cat_query = Category.objects.filter(name=search_word)
        cat_result = self.paginate_queryset(cat_query, request, view=self)
        product_query = Product.objects.filter(name=search_word)
        product_result = self.paginate_queryset(product_query, request, view=self)

        category_ser_data = CategorySerializer(cat_result, many=True)
        product_ser_data = ProductSerializer(product_result, many=True)
        context = {
            "category_result": category_ser_data.data,
            "product_result": product_ser_data.data
        }
        return Response(context, status=status.HTTP_200_OK)
    
class AddToCardView(APIView):
    permission_classes = [AllowAny, IsAuthenticated]

    def post(self, request, product_id):
        quantity = request.POST["quantity"]
        product_obj = Product.objects.get(id=product_id)
        data = {            
                "name": product_obj.name,
                "price": product_obj.price,
                "quantity": int(quantity),
                "total": product_obj.price * int(quantity)
            }
        
        if request.session.has_key('products'):
            products_list = request.session["products"]

            for item in products_list:
                if item["name"] == product_obj.name:
                    item["quantity"] += int(quantity)
                    item["total"] += data["total"]
                else:
                    products_list.append(data)

            request.session["products"] = products_list
        else:
            products_list = [data, ]
            request.session['products'] = products_list
        return Response({"message": "added to card successfully..."}, status=status.HTTP_200_OK)

class ShopCardView(APIView, PageNumberPagination):
    permission_classes = [AllowAny, IsAuthenticated]
    
    def get(self, request):
        products = request.session["products"]
        return Response(products, status=status.HTTP_200_OK)
