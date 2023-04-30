from django.http import HttpResponse
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def blogs(request):
    posts = Post.objects.all()
    posts_info = []
    for post in posts:
        related_topics = post.topic.all()[:3]
        short_text = ' '.join(post.content.split()[:50]) + '...'
        num_comments = post.post_comments.count()
        posts_info.append({
            'title': post.title,
            'created_at': post.created_at,
            'related_topics': related_topics,
            'short_text': short_text,
            'num_comments': num_comments,
            'slug': post.slug,
        })
    return render(request, 'blogs.html', {'posts_info': posts_info})


def about(request):
    return HttpResponse("Потенциально тут будет страница с описанием нашего блога.")


def empty(request):
    posts = Post.objects.all()
    posts_info = []
    for post in posts:
        related_topics = post.topic.all()[:3]
        short_text = ' '.join(post.content.split()[:50]) + '...'
        num_comments = post.post_comments.count()
        posts_info.append({
            'title': post.title,
            'created_at': post.created_at,
            'related_topics': related_topics,
            'short_text': short_text,
            'num_comments': num_comments,
            'slug': post.slug,
        })
    return render(request, 'blogs.html', {'posts_info': posts_info})


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


def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_info = {
        'username': user.username,
        'email': user.email,
        'posts': Post.objects.filter(user=user)
    }
    return render(request, 'profile.html', {'user_info': user_info})


def change_password(request):
    return HttpResponse("Страничка для смены пароля")


def register(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return HttpResponse("Логаут")
