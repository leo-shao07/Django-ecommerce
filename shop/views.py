from datetime import datetime
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
# from shop.models import Good, Order
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import GoodSerializer,OrderSerializer
# Create your views here.
from pymongo import MongoClient

client = MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.cos8g7p.mongodb.net/sandbox')

def list_good(request):
    if request.method == 'POST':
        data = request.POST.dict()
        mycol = client['django-data']['GoodsAndHistory']
        inputdata = { "name": data.get("your_name"), "quantity": int(data.get("quantity")),"time": datetime.now()}
        mycol.update_one({'goods_name': data.get("goods_name")}, {'$push': {"history":inputdata}})

        return redirect(home)
    else:
        filter={}
        project={
            'goods_name': 1,
            '_id':0
        }

        result = client['django-data']['GoodsAndHistory'].find(filter=filter,projection=project)
        l = []
        for r in result:
            map = {}
            map["goods_name"] = r["goods_name"]
            l.append(map)
        return render(request,'buy.html',{'goods':l})

def list_history(request):
    result = client['django-data']['GoodsAndHistory'].aggregate([
        {
            '$unwind': {
                'path': '$history'
            }
        }
    ])
    return render(request,'history.html',{'orders':list(result)})

def home(request):
    return render(request,'home.html')

