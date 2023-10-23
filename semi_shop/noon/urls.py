
from django.contrib import admin
from django.urls import path,include
from noon.views import contact, about,products,show_product ,delete,search,create,update

urlpatterns = [

    path("",products,name="noon2.products"),
    path("show_product/<int:id>" ,show_product,name="noon2.show_product"),
    path("contact" ,contact,name="noon.contant"),
    path("about" ,about,name="noon.about"),
    path('<int:id>/delete',delete,name="noon.delete"),
    path('search',search,name="noon.search"),
    path('create',create,name="noon.create"),
    path('update/<int:id>',update,name="noon.update"),
    path('api/',include('noon.api.urls'))
 
]
