from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class TopicManager(models.Manager):
    def first_three(self):
        return self.all()[:3]

class TopicManager(models.Manager):
    def first_three(self):
        return self.all()[:3]


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    objects = TopicManager()

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, related_name="user_posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    topic = models.ManyToManyField(Topic, related_name="related_posts",
                                   validators=[MinLengthValidator(1, message="At least one topic is required.")])

    @property
    def short_description(self):
        return ' '.join(self.content.split()[:50]) + '...'

    def save(self, *args, **kwargs):
        if self.created_at:
            self.slug = slugify(self.title + '-' + str(self.created_at.date()))
        else:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)


