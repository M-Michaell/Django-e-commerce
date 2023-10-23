from rest_framework import serializers
from noon.models import Product
from category.api.serializer import CategorySerializer
# from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=400, allow_blank=True, required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock = serializers.IntegerField(default=0, allow_null=True, required=False)
    image = serializers.ImageField(required=False)
    # category=CategorySerializer(read_only=True)
    category_id=serializers.IntegerField(read_only=True ,required=False)
    category_name=serializers.CharField(source='category' ,required=False,read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self,validate_data):
        return Product.objects.create(**validate_data)
    
    def update(self,instance,validate_data):
        instance.title= validate_data['title']
        instance.description= validate_data['description']
        instance.price= validate_data['price']
        instance.stock= validate_data['stock']
        instance.image= validate_data['image']
        instance.save()
        return instance
