from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('save_article/', views.db_save_article),
    path('get_article/', views.db_get_article),
    path('db_update_article/', views.db_update_article),
    path('template_view/',
         TemplateView.as_view(template_name="article/index.html")),
    path('view_class/', views.ArticleClass.as_view(), name='detail'),
]