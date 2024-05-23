from django.urls import path
from web.views import home
from web.views import calculator_view
from web.views import currency_converter_view

urlpatterns =[
    path('', home, name='home'),
    path('calculator', calculator_view, name='calculator'),
    path('currency', currency_converter_view, name='currency'),
]