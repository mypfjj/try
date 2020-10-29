from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
#views.index（处理函数）用到url里面
