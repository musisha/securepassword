from django.shortcuts import render
from django.http import HttpResponse
import random
import string
from .models import Article

# Home page view function
def home(request):
    article = Article.objects.order_by('-date')[:1]
    return render(request, 'generator/home.html', {'issue': article})

#Password generator function view
def password(request):
    characters = []
    for letters in string.ascii_lowercase:
        characters.append(letters)
    
    length = int(request.GET.get('length', 12))
    thepassword = ''

    if request.GET.get('uppercase'):
        for i in string.ascii_uppercase:
            characters.extend(i)

    if request.GET.get('numbers'):
        characters.extend(string.digits)
    
    if request.GET.get('special'):
        characters.extend(string.punctuation)


    for i in range(length):     
        thepassword+=random.choice(characters)


    return render(request, 'generator/password.html', {'password': thepassword})


#About view
def about(request):
    return render(request, 'generator/about.html')