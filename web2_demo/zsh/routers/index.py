import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.contrib import admin
from controllers import index
from django.urls import path

urlpatterns = [
    path('index/',index.index),
    path('list/',index.list),
    path('filter/',index.filter),
    path('test_val/',index.test_val),
]