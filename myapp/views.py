from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})


def about(request):
    return HttpResponse("Потенциально тут будет страница с описанием нашего блога.")



def show_one_blog(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'about_blog.html', {'post': post})


def comment(request):
    return HttpResponse("Урл для добавления коментария к посту.")


def create(request):
    return render(request, 'create_post.html')


def update(request):
    return HttpResponse("Обновление существующего поста")


def delete(request):
    return HttpResponse("Удаление поста")


def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


def change_password(request):
    return HttpResponse("Страничка для смены пароля")


def register(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return HttpResponse("Логаут")
