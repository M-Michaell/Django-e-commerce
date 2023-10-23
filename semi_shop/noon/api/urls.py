from django.urls import path
from .views import index,get_product


urlpatterns = [

   path("",index),
   path("<int:id>/",get_product)


]