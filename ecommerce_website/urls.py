"""ecommerce_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecom_app import views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home', views.index, name='home'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('logout', user_views.logout, name='logout'),
    path('login', user_views.login, name='login'),
    path('emptycart', views.emptycart, name='emptycart'),
    path('checkout', views.checkout, name='checkout'),
    path('customerservice', views.customerservice, name='customerservice'),
    path('register', user_views.register, name='register'),
    path('profile', user_views.profile, name='profile'),
    path('profile/<int:user_id>/edit', user_views.edit, name='edit'),
    path('checkout/thankyou', views.thankyou, name='thankyou'),
]
