from django.shortcuts import get_object_or_404, redirect, render
from random import randint
from .models import Author, Post, Comment
from .forms import GameForm, AuthorForm, PostForm, CommentForm

rnd = randint


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


def rand_int(request, count):
    title = 'Случайное число'
    res_list = []
    for i in range(1, count+1):
        res_list.append([i, randint(1, 6)])
    context = {'title': title, 'result': res_list}
    return render(request, 'myapp4/base_games.html', context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'myapp4/author_posts.html', {'author': author, 'posts': posts})


def post(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    return render(request, 'myapp4/posts.html', {'post': post})


def gamer_form(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data['game']
            count = form.cleaned_data['count']
            if game == '1':
                #redirect('cube', count=count)
                return cube(request, count=count)
            elif game == '3':
                return coin(request, count=count)
            elif game == '2':
                return rand_int(request, count=count)
    else:
        form = GameForm()
    return render(request, 'myapp4/game_form.html', {'form': form})


def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            author = Author(name=name, email=email)
            author.save()
    else:
        form = AuthorForm()
    return render(request, 'myapp4/author_form.html', {'form': form})


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            post_ = Post(title=title, content=content, author=author)
            post_.save()
    else:
        form = PostForm()
    return render(request, 'myapp4/post_form.html', {'form': form})


def comment_form(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            post_id = form.cleaned_data['post']
            post = Post.objects.filter(pk=post_id).first()
            comment = form.cleaned_data['comment']
            comment_ = Comment(author=author, post=post, comment=comment)
            comment_.save()
    else:
        form = CommentForm()
    return render(request, 'myapp4/comment_form.html', {'form': form})
