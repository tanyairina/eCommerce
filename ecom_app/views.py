from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Products.objects.all()
    # Search bar
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is  not None:
        product_objects = product_objects.filter(title__icontains=item_name)
    # Paginator code
    paginator = Paginator(product_objects,4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    # products_objects is passed as a context
    return render(request, 'shop/index.html',{'product_objects':product_objects})

def detail(request, item_id):
    product_object = Products.objects.get(id=item_id)
    return render(request, 'shop/detail.html',{'product_object':product_object})

def checkout(request):
    if request.method == "POST":
        items = request.POST.get('items', '')
        fname = request.POST.get('fname',"")
        lname = request.POST.get('fname',"")
        address_ship = request.POST.get('address_ship',"")
        address_ship2 = request.POST.get('address_ship2',"")
        city_ship = request.POST.get('city_ship',"")
        state_ship = request.POST.get('state_ship',"")    
        zipcode_ship = request.POST.get('zipcode_ship',"")
        total = request.POST.get('total',"")
        order = Order(
            items=items,
            fname=fname,
            lname=lname, 
            address_ship=address_ship,
            address_ship2=address_ship2,
            city_ship=city_ship,
            state_ship=state_ship,
            zipcode_ship=zipcode_ship, 
            total=total
            )
        order.save()
    return render(request, 'shop/checkout.html')

def thankyou(request):
    if request.method == "GET":
        return redirect('/')
    return render(request, "shop/thankyou.html")

def emptycart(request):
    return redirect("/")

def customerservice(request):
    return render(request, "shop/custservc.html")

