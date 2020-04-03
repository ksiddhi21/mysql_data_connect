from django.contrib import admin
from django.urls import path

from dbconnect_app.views import *

app_name = 'dbconnect_app'

urlpatterns = [

path('',index,name='index'),

]