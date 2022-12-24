from django.shortcuts import render
from .models import*

# Create your views here.
def home(request):
    context = {}
    product = Product.objects.all()
    context['product'] = product
    return render(request, 'home.html', context)