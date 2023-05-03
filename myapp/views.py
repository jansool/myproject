from django.http import HttpResponse
from .models import Post, Topic, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm, CreatePostForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login_view/')
def blogs(request, topic=None):
    search = request.GET.get('search')
    topics = Topic.objects.all()
    if search:
        posts = Post.objects.filter(title__icontains=search)
    elif topic:
        topic = Topic.objects.get(title=topic)
        posts = Post.objects.filter(topic=topic.id)
    else:
        posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts, 'topics': topics})


@login_required(login_url='/login_view/')
def about(request):
    return HttpResponse("Потенциально тут будет страница с описанием нашего блога.")


@login_required(login_url='/login_view/')
def show_one_blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            text = form.cleaned_data.get('text')
            Comment.objects.create(user=user, post=post, content=text)
            form = CommentForm()
    else:
        form = CommentForm()

    return render(request, 'about_blog.html', {'post': post, 'form': form})


@login_required(login_url='/login_view/')
def comment(request):
    return HttpResponse("Урл для добавления коментария к посту.")


@login_required(login_url='/login_view/')
def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('text')
            topic = form.cleaned_data.get('topic')
            post = Post.objects.create(user=user, title=title, content=content)
            post.topic.add(topic)
            return redirect('blogs')
    else:
        form = CreatePostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required(login_url='/login_view/')
def update(request):
    return HttpResponse("Обновление существующего поста")


@login_required(login_url='/login/')
def delete(request):
    return HttpResponse("Удаление поста")


@login_required(login_url='/login_view/')
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


@login_required(login_url='/login_view/')
def change_password(request):
    return HttpResponse("Страничка для смены пароля")


def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login_view')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='/login_view/')
def logout_view(request):
    logout(request)
    return redirect('login_view')