from django.shortcuts import render
import string
from random import *

# Create your views here.


def homepage(request):
    return render(request, 'generator/homepage.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    number = ''
    symbols = ''
    upper = ''
    lower = ''
    length = int(request.GET.get('length'))
    if(request.GET.get('number')):
        number = string.digits
    if(request.GET.get('symbols')):
        symbols = string.punctuation[1:6]
    if(request.GET.get('uppercase')):
        upper = string.ascii_letters[-26:]
    lower = string.ascii_letters[:26]
    characters = upper+symbols + number+lower
    password = "".join(choice(characters)
                       for x in range(randint(length, length)))
    return render(request, 'generator/password.html', {'password': password})
