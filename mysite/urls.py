"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
import myapp.views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blogs/", v.blogs, name="blogs"),
    path('blogs/<str:topic_name>/', v.blogs, name='blogs_topic'),
    path("about/", v.about, name="about"),
    path("", v.empty),
    path("login_view/", v.login_view, name="login_view"),
    path("comment/", v.comment),
    path("create/", v.create, name="create"),
    path("update/", v.update),
    path("delete/", v.delete),
    path("profile/<str:username>/", v.profile, name="profile"),
    path("change_password/", v.change_password),
    path("register/", v.register, name="register"),
    path("logout_view/", v.logout_view, name="logout_view"),
    path("<slug:slug>/", v.show_one_blog, name="show_one_blog")
]
