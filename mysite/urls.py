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
import myapp.views as v

urlpatterns = [
    path("blogs/", v.blog),
    path("about/", v.about),
    path("/", v.empty),
    path("//", v.show_one_blog),
    path("/comment/", v.comment),
    path("create/", v.create),
    path("/update/", v.update),
    path("/delete/", v.delete),
    path("profile//", v.profile),
    path("change_password/", v.change_password),
    path("register/", v.register),
    path("login/", v.login),
    path("logout/", v.logout)
]
