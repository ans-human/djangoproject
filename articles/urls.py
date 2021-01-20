from django.urls import path, include
from . import views
app_name = 'articles'
urlpatterns = [
    path('', views.articles_list.as_view(), name = "list"),
    path('create/', views.article_create.as_view(), name="create"),
    path( '<slug:slug>', views.article_detail.as_view(), name = "detail" ),
    path('update/<slug:slug>', views.article_update.as_view(), name="update"),
    path('delete/<slug:slug>', views.article_delete.as_view(), name="delete"),
]