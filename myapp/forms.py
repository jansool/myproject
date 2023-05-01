from django import forms
from django.contrib.auth.models import User
from .models import Post, Topic


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            self.add_error('confirm_password', 'Паролі не збігаються')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Користувач з таким ім\'ям вже існує')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.check_password(password):
                self.add_error('password', 'Пароль невірний')
        else:
            self.add_error('username', 'Користувача з таким ім\'ям не існує')


class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)
    topic = forms.ModelChoiceField(queryset=Topic.objects.all())


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
