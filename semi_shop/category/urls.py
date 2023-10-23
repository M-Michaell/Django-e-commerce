from django.contrib import admin
from django.urls import path,include
from category.views import categories, create_category,show_datails
urlpatterns = [

    path('',categories,name="noon.category"),
    path('create',create_category,name="noon.create_category"),
    path('category_product',create_category,name="noon.show_category_product"),
    path('<int:id>',show_datails,name="category.category_details"),
    path('api/',include('category.api.urls'))
]
