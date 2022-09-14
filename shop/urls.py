from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('buy/',views.list_good),
    path('history/',views.list_history),
    path('home',views.home)
]
