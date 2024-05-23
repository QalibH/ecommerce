from django.shortcuts import render
from product.models import Product
from product.models import Blog
# from django.contrib.auth.models import User

def home(request):
    # user = User.objects.get(username='Qalib')
    products = Product.objects.all()
    return render(request, 'web/home.html', {'products':products})

def calculator_view(request):
    result = None
    numb1 = request.GET.get('numb1')
    numb2 = request.GET.get('numb2')
    if numb1 and numb2:
        result = numb1 + numb2
    
    context = {
        'result': result
    }
    return render(request, 'web/calculator.html', context)


import requests
from django.shortcuts import render

def currency_converter_view(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')

        api_key = '80c34514425aa133d57e39f7'
        url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            conversion_rate = data['conversion_rate']
            converted_amount = amount * conversion_rate

            context = {
                'amount': amount,
                'from_currency': from_currency,
                'to_currency': to_currency,
                'converted_amount': converted_amount,
            }
        else:
            context = {
                'error': f"Error: {data['error']}"
            }

        return render(request, 'web/currency_converter.html', context)

    return render(request, 'web/currency_converter.html')
