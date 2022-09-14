from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def say_hello(request):
    # return HttpResponse('hello world')
    query_set = Product.objects.all()
    product = Product.objects.filter(id=1).first()
    exists = Product.objects.filter(id=1).exists()
    try:
        product = Product.objects.get(id=1)
    except ObjectDoesNotExist:
        pass
    for product in query_set:
        print(product)

    list(query_set)
    query_set[0:5] 
    return render(request,'hello.html',{'name':'Mosh'})
