from django.shortcuts import render, HttpResponse, redirect
from django.template.loader import render_to_string
from .models import*

# Create your views here.
# context = {}
# amount = Product.objects.all().values_list('amount', flat=True)
# context['amount'] = amount
# print('amount', amount)
# render_to_string('base.html', context)

def home(request):
    context = {}
    product = Product.objects.all()
    context['product'] = product
    id = product.values_list('id', flat=True)
    context['id'] = id
    print('id', id)
    return render(request, 'test.html', context)

def product_type(request):
    context = {}
    product = Product.objects.all()
    context['product'] = product
    if request.GET.get('beers'):
        # product_type = request.GET.get('product_type')
        # product = Product.objects.filter(product_type=product_type)
        # context['product'] = product
        # print('product_type', product_type)
        # return render(request, 'test.html', context)
        print('beers')
        product_type = request.GET.get('beers')
    # return render(request, 'test.html', context)
    return HttpResponse('product_type')

def product_detail(request, id):
    context = {}
    product = Product.objects.get(id=id)
    context['product'] = product
    return render(request, 'product.html', context)
    # return HttpResponse('product_detail')

def add_to_cart(request, id):
    context = {}
    amount = request.GET.get('amount')
    print('amount', amount)
    product = Product.objects.get(id=id)
    product.amount = amount
    product.total = int(amount) * product.price
    product.status = 1
    product.save()
    
    context['product'] = product
    context['added'] = product.status = 1
    # return render(request, 'cart.html', context)
    return redirect('basket')
    # return HttpResponse('add_to_cart')

def basket(request):
    context = {}
    products = Product.objects.filter(status=1)
    context['products'] = products
    return render(request, 'basket.html', context)

def destroy(request, id):
    context = {}
    product = Product.objects.get(id=id)
    product.status = 0
    product.save()
    context['product'] = product
    return redirect('basket')