from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer  
from noon.models import Product

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response({'message': 'Product is successfully received', 'product': product.data}, status=201)
        else:
            return Response(product.errors, status=400)

    elif request.method == 'GET':
        products = Product.objects.all()
        serialized_products = ProductSerializer(products, many=True).data

        return Response({'message': 'data received', 'products': serialized_products})

@api_view(['GET',"DELETE","PUT"])
def get_product(request,id):
    product=Product.objects.filter(id=id).first()
    if request.method == 'GET':
        serialized_item = ProductSerializer(product)
        return Response({'message': 'data received', 'product':serialized_item.data}, status=200)

    elif request.method =="DELETE":
        product.delete()
        return Response({'message': 'product deleted'}, status=205)
     
    elif request.method=="PUT":
        serialized_item = ProductSerializer(instance=product,data=request.data)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response({'message': 'product saved', 'data': serialized_item.data}, status=201)
        return Response(serialized_item.errors ,status=401)
    