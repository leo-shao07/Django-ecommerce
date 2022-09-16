from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from shop.models import Good, Order
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoodSerializer,OrderSerializer
# Create your views here.

def list_good(request):
    if request.method == 'POST':
        data = request.POST.dict()
        order = Order()
        order.purchase_name = data.get("your_name")
        order.quantity = data.get("quantity")
        order.good = Good(pk=data.get("good_id"))

        order.save()
        return redirect(home)
    else:
        query_set = Good.objects.all()
        print(list(query_set))
        return render(request,'buy.html',{'goods':list(query_set)})

# def buy_good(request):
#     data = request.POST.dict()
#     order = Order()
#     order.purchase_name = data.get("your_name")
#     order.quantity = data.get("quantity")
#     order.good = Good(pk=data.get("good_id"))
#     order.save()
#     return redirect(home)

def list_history(request):
    queryset = Order.objects.select_related('good').all()
    return render(request,'history.html',{'orders':list(queryset)})

def home(request):
    return render(request,'home.html')

# @api_view()
# def list_good(request):
#     query_set = Good.objects.all()
#     serializer = GoodSerializer(query_set,many=True)
#     # print(list(query_set))
#     return Response(serializer.data)


# @api_view(['GET','POST'])
# def list_history(request):
#     if request.method == 'GET':
#         queryset = Order.objects.select_related('good').all()
#         ser = OrderSerializer(queryset,many=True)
#         return Response(ser.data)
#     elif request.method == 'POST':
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.validated_data
#             return Response('ok')
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

