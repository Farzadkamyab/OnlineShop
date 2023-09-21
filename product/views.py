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
    
