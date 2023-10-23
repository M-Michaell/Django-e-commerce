from rest_framework import serializers

from category.models import Category


class CatergoryModelSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'