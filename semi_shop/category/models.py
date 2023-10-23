from django.db import models
from django.core.exceptions import ValidationError
from django.shortcuts import reverse


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField(max_length=400 ,null=True)
    image = models.ImageField (upload_to="category/images", null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    def clean_name(self):
        found=Category.objects.filter(name=self.cleaned_data["name"]).exists()
        if found :
            raise ValidationError("Category name already exists")
        return self.cleaned_data["name"]
    

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    def get_show_url(self):
          return  reverse('category.category_details', args=[self.id])

    def get_image_url(self):
        return f"/media/{self.image}"