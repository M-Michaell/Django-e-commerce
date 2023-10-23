from django.db import models 
from category.models import Category
from django.shortcuts import  reverse
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400 ,null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock = models.IntegerField(default=0 ,null=True)
    image = models.ImageField (upload_to="noon/images", null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True, blank=True,on_delete=models.CASCADE,related_name="product")
    owner = models.ForeignKey(User, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='owner')


    def __str__(self):
        return f"{self.title }"

    @classmethod
    def get_all(cls):
        return cls.objects.all()
    
    def get_image_url(self):
        return f"/media/{self.image}"

    def get_show_url(self):
        return  reverse('noon2.show_product', args=[self.id])


    def get_delete_url(self):
        return  reverse('noon.delete', args=[self.id])
    
    def update (self):
        return reverse("noon.update", args  = [self.id])


    