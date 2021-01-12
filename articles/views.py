from django.shortcuts import render
from .models import Article

# Create your views here.
def articles_list(request):
    article = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles':article})