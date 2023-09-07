from django.shortcuts import get_object_or_404, render
from random import randint
from .models import Author, Post

def index(request):
    context = {"name": "Главная страница проекта Django Красножен Е.Л."}
    return render(request, "myapp4/index.html", context)


def about(request):
    my_list = ['Красножен', 'Екатерина', 'Леонидовна']
    my_dict = {
        'группа': 'разработчик python',
        'поток': '2023',
        'программа': 'Университет 2025',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp4/about.html', context)


def text(title, result):
    return f'<h1>{title}<h1>' \
        f'<p> Результат для вас: {result}<p>'
        
        
def coin(request, count):
    
    title = 'Бросок монеты'
    res_data = []
    res = ''
    for i in range(1, count+1):
        temp = randint(1, 2)
        if temp == 1:
            res = 'решка'
        else:
            res = 'орел'
        res_data.append([i, res])
        
    context = {'title': title, 'result': res_data}
    return render(request, 'myapp4/base_games.html', context)
        
        
def cube(request, count):
    title = 'Бросок кубика'
    res_data = []
    for i in range(1, count+1):
        res = randint(1, 6)
        res_data.append([i, res])
    context = {'title': title, 'result': res_data}
    return render(request, 'myapp4/base_games.html', context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'myapp4/author_posts.html', {'author': author, 'posts': posts})


def post(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    return render(request, 'myapp4/posts.html', {'post': post})