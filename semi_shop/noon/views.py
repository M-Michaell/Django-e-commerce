from django.shortcuts import render,redirect ,reverse,get_object_or_404
from django.http import HttpResponse 
from noon.models import Product
from noon.forms import ProductForm 
from category.models import Category
from django.contrib.auth.decorators import login_required


def products (request):
    # products = Product.objects.all()
    products=Product.get_all()
    return render(request, "noon2/products.html",context={"products":products})

def show_product(request,id):
    product = get_object_or_404(Product ,pk=id)
    return render (request, "noon2/show_product.html",context={"product":product})

@login_required()
def delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    url =reverse("noon2.products")
   
    return redirect(url) 


def contact (request):
    return render( request,"noon2/contact.html")

def about (request):
      return render( request,"noon2/about.html")

def search (request):
    text=request.POST.get('search')
    if text :
        data= Product.objects.filter(title__istartswith=text)
        list(data)
        return render( request,"noon2/search.html",context={"data":data ,"text":text})

@login_required()
def create(request):
    form=ProductForm()
    if request.POST:
        form= ProductForm(request.POST,request.FILES)
        if form.is_valid():
            title=request.POST['title']
            description=request.POST['description']
            price=request.POST['price']
            stock=request.POST['stock']
            category = form.cleaned_data['category']
            image=None
            owner=request.user
            if "image" in request.FILES:
                image=request.FILES['image']
            product = Product.objects.create(title=title,description=description,price=price,stock=stock,image=image,category=category,owner=owner)

            return redirect(product.get_show_url())
    return render( request,"noon2/create.html",context={"form":form})


@login_required()
def update(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()

    if request.method == 'POST':
        product.title = request.POST.get('title')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')

        # Handle image upload
        image = request.FILES.get('image')
        if image:
            product.image = image

        # Get the Category object for the selected category
        category = request.POST.get('category')
        category_object = Category.objects.get(name=category)

        # Assign the Category object to the product
        product.category = category_object

        product.save()

        return redirect('noon2.show_product', id=id)

    else:
        context = {
            'product': product,
            'categories': categories,
        }
        return render(request, 'noon2/update.html', context)
