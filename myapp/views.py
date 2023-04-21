from django.http import HttpResponse
from django.shortcuts import render


def blogs(request):
    return render(request, 'blogs.html')


def about(request):
    return HttpResponse("Потенциально тут будет страница с описанием нашего блога.")


def empty(request):
    return HttpResponse(".")


def show_one_blog(request):
    return render(request, 'about_blog.html')


def comment(request):
    return HttpResponse("Урл для добавления коментария к посту.")


def create(request):
    return render(request, 'create_post.html')


def update(request):
    return HttpResponse("Обновление существующего поста")


def delete(request):
    return HttpResponse("Удаление поста")


def profile(request):
    return HttpResponse("Личная страница пользователя")


def change_password(request):
    return HttpResponse("Страничка для смены пароля")


def register(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return HttpResponse("Логаут")
