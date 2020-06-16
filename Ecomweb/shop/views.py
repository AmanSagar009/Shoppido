from django.shortcuts import render
from .models import Product,Contact
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    #products = Product.objects.all()
    #print(products)
    #n = len(products)
    #nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    #allProds = [[products, range(1, nSlides), nSlides],
     ##           [products, range(1, nSlides), nSlides]]


    allProds = []
    catprods = Product.objects.values('catagory', 'id')
    cats = {item['catagory'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}

    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print(name,email)
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request,myid):
    #Fetch the poduct using id

    product = Product.objects.filter(id=myid)

    return render(request, 'shop/prodView.html', {'product': product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')

def register(request):
    return render(request, 'shop/register.html')

def login(request):
    return render(request, 'shop/login.html')

def cart(request):
    return render(request, 'shop/cart.html')

def wishlist(request):
    return render(request, 'shop/wishlist.html')