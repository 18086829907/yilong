from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app_asj/home.html')

def market(request):
    return render(request, 'app_asj/market.html')

def cart(request):
    return render(request, 'app_asj/cart.html')

def mine(request):
    return render(request, 'app_asj/mine.html')

def base(request):
    return render(request, 'app_asj/base1.html')