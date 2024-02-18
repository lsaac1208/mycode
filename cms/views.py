from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'cms/home.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'cms/article_detail.html', {'article': article})

