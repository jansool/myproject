from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse('Hiiiiiiiiii')


def blogs(request):
    return HttpResponse("Домашняя страница, потенциально, однажды там будут блоги :)")


def about(request):
    return HttpResponse("Потенциально тут будет страница с описанием нашего блога.")


def empty(request):
    return HttpResponse(".")


def show_one_blog(request):
    return HttpResponse("""Потенциальная страница для просмотра одного блога. 
    Динамический контент, который потенциально будет ходить в базу данных""")


def comment(request):
    return HttpResponse("Урл для добавления коментария к посту.")


def create(request):
    return HttpResponse("Создание нового поста")


def update(request):
    return HttpResponse("Обновление существующего поста")


def delete(request):
    return HttpResponse("Удаление поста")


def profile():
    return HttpResponse("Личная страница пользователя")


def change_password():
    return HttpResponse("Страничка для смены пароля")


def register():
    return HttpResponse("Регистрация пользователя")


def login():
    return HttpResponse("Логин")


def logout():
    return HttpResponse("Логаут")
