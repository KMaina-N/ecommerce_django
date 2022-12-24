from django.shortcuts import render, HttpResponse, redirect
from .models import*

# Create your views here.
def home(request):
    print('home')
    context = {}
    product = Product.objects.all()
    context['product'] = product
    id = product.values_list('id', flat=True)
    context['id'] = id
    print('id', id)
    return render(request, 'test.html', context)

def product_detail(request, id):
    context = {}
    product = Product.objects.get(id=id)
    context['product'] = product
    return render(request, 'product.html', context)
    # return HttpResponse('product_detail')