from rest_framework import serializers
from category.models import Category
# from rest_framework.validators import UniqueValidator

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=400, allow_blank=True, required=False)
    image = serializers.ImageField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


    def create(self,validate_data):
        return Category.objects.create(**validate_data)
    
    def update(self,instance,validate_data):
        instance.title= validate_data['name']
        instance.description= validate_data['description']
        instance.image= validate_data['image']
        instance.save()
        return instance
