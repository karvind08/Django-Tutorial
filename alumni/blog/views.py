from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Arvind',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date-posted': 'March 13,2021',
    },
    {
        'author': 'Amit',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date-posted': 'March 12,2021',
    },
    {
        'author': 'Kukku',
        'title': 'Blog Post 3',
        'content': 'Third Post Content',
        'date-posted': 'March 14,2021',
    }
]


def home(request):
    content = {
        'posts': posts
    }
    return render(request, 'blog/home.html', content)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
