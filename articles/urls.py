from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.articles_list),
    path( '<slug:slug>', views.article_detail )
]