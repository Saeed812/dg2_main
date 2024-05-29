from django.shortcuts import render
from .models import product

def home(request):
    all_products = product.objects.all()

    
    return render(request,"index.html",{'product': all_products})