from django.shortcuts import render, redirect 
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if 'user_id' in request.session:
        messages.success(request, "You have already loggedin!")
        return render(request, "shop/index.html")
    else:
        if request.method == "GET":
            return render(request, "users/register.html")
        errors = User.objects.validate(request.POST)
        if errors:
            for e in errors.values():
                messages.error(request, e)
            return render(request, "users/register.html")
        else:
            new_user = User.objects.register(request.POST)
            request.session['user_id'] = new_user.id
            messages.success(request, "You have successfully registered!")
            return render(request, "shop/index.html")

def login(request):
    if request.method == "GET":
        return redirect("/")
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect("/")
    loggedin_user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = loggedin_user.id
    messages.success(request, "You have successfully logged in!")
    return render(request,"shop/index.html")

def logout(request):
    if 'user_id' in request.session:
        messages.success(request, "Succefully Logout!")
        request.session.clear()
        return render(request, "users/register.html")
    else: 
        messages.success(request, "Please log in!")
        return redirect("/")

def profile(request):
    if 'user_id' not in request.session:
        messages.success(request, "Please log in!")
        return render(request, "users/register.html")    
    else:
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
            context = {
                'user': user
            }
            return render(request, 'users/profile.html', context)

def update(request, user_id):
        to_update = User.objects.get(id=user_id)
        to_update.first_name = request.POST['first_name']
        to_update.last_name = request.POST['last_name']
        to_update.telephone = request.POST['telephone']
        to_update.address = request.POST['address']
        to_update.address2 = request.POST['address2']
        to_update.city= request.POST['city']
        to_update.state= request.POST['state']
        to_update.zipcode= request.POST['zipcode']
        to_update.save()
        return redirect('/profile')

def edit(request, user_id):
    if 'user_id' not in request.session:
        messages.success(request, "Please log in!")
        return render(request, "users/register.html")    
    else:
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
            context = {
                'user': user
            }
            return render(request, 'users/edit.html', context)


