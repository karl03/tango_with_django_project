from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Dictionary to pass to template, key is is the name of the modifiable var
    # in the template, value is what is passed into this var
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Renders the template with the message I have passed in
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage' : 'This tutorial has been put together by Karl'}
    return render(request, 'rango/about.html', context=context_dict)
