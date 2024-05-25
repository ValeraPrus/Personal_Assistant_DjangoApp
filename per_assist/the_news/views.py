from django.shortcuts import render, redirect, get_object_or_404
from django.core.management import call_command
# import subprocess
from .models import News


def news_list(request):
    news = News.objects.all().order_by('-published_date')
    selected_category = request.GET.get('categories')
    request_path = request.path

    if selected_category and selected_category != '':
        news = news.filter(category__contains=selected_category).order_by('-published_date')
    return render(request, 'news/news_list.html', {'news': news, 'selected_category': selected_category, 'request_path': request_path})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})


# def news_category(request, category):
#     news = News.objects.filter(category=category)
#     return render(request, 'news/news_list.html', {'news': news})


# def fetch_news():
#     subprocess.Popen(['python', 'manage.py', 'fetch_news'])

def fetch_news_view(request):
    call_command('fetch_news')
    return redirect('the_news:news_list')
