import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.urls import path
from controllers import view


urlpatterns = [
   path('hello/', view.hello),
   path('2/', view.hello)
]