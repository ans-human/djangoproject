from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import forms
from .models import Article

# Create your views here.
class articles_list(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'articles/articles_list.html'

# def articles_list(request):
#     article = Article.objects.all().order_by('-date')
#     return render(request, 'articles/articles_list.html', {'articles':article})

class article_detail(DetailView):
    model = Article
    slug_url_kwarg = 'slug'
    template_name = 'articles/article_detail.html'

# def article_detail(request, slug):
#     article = Article.objects.get(slug=slug)
#     return render(request, 'articles/article_detail.html', {'article': article})

# @login_required(login_url="/accounts/login/")
class article_create(CreateView):
    model = Article
    form_class = forms.CreateArticle
    template_name = 'articles/article_create.html'
    def post(self, request):
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
        
class article_update(UpdateView):
    model = Article
    slug_url_kwarg = 'slug'
    form_class = forms.CreateArticle
    template_name = 'articles/article_update.html'


class article_delete(DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles:list')


# def article_create(request):
#     if request.method == 'POST':
#         form = forms.CreateArticle(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.author = request.user
#             instance.save()
#             return redirect('articles:list')
#     else:
#         form = forms.CreateArticle()
#     return render(request, 'articles/article_create.html', { 'form': form })