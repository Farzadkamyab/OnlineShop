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
