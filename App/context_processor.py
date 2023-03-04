from .models import*
from django.db.models import Sum
import re
def add_variable_to_context(request):
    product = Product.objects.filter(status=1)
    amount = product.values('amount').aggregate(Sum('amount'))
    amount = re.findall(r'[0-9]+', str(amount))
    # amount = re.findall(r'[[]]+',''.join(amount))
    amount = '[]'.join(amount)
    price = product.values('total').aggregate(Sum('total'))
    price = re.findall(r'[0-9]+', str(price))
    price = '[]'.join(price)

    search = request.GET.get('q')
    if search == None:
        search = ''



    
    return {
        'amount': amount,
        'price': price,
        'search': search,
    }