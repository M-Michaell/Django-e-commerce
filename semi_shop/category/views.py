from django.shortcuts import render,redirect ,reverse,get_object_or_404
from category.form import CategoryForm
from category.models import Category

# Create your views here.



def categories(request):
    categories= Category.objects.all()
    return render(request, 'category/categories.html', context={'categories': categories})

def create_category(request) :
    form=CategoryForm()
    if request.POST:
        form= CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            name=request.POST['name']
            description=request.POST['description']
            image=None
            if "image" in request.FILES:
                image=request.FILES['image']
            category = Category.objects.create(name=name,description=description,image=image)
            url=reverse("noon.category")
            return redirect(url)
    return render( request,"category/create.html",context={"form":form})
    

def show_datails(request,id):
    category=get_object_or_404(Category, pk=id)
    return render(request,'category/show.html',context={'category':category})
