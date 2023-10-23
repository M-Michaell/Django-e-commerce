from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import  APIView

# import modules from your app
from category.models import Category
from category.api.modelserializer import CatergoryModelSerializer

class CategoryAPIView(APIView):

    def get(self, request):

        categories = Category.get_all()
        serialized_category = CatergoryModelSerializer(categories, many=True)
        return Response({"data": serialized_category.data}, status=status.HTTP_200_OK)

    def post(self,request):
        serialized_category = CatergoryModelSerializer(data=request.data)
        if serialized_category.is_valid():
            serialized_category.save()
            return Response({"data": serialized_category.data}, status=status.HTTP_201_CREATED)

        return Response({"errors": serialized_category.errors}, status=status.HTTP_400_BAD_REQUEST)
