from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category
        
    except Category.DoesNotExist:
        
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)

        

def index(request):
    #get top 5 most liked categories
    category_list = Category.objects.order_by('-likes')[:5]
    #get top 5 most viewed pages
    page_list = Page.objects.order_by('-views')[:5]

    #create dictionary to pass into the template
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    # Renders the template with the information I have passed in
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage' : 'This tutorial has been put together by Karl'}
    return render(request, 'rango/about.html', context=context_dict)
