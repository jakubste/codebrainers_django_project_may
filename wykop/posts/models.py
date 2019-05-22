from django.db import models
from django.db.models import deletion

from wykop.accounts.models import User


class Post(models.Model):
    title = models.CharField(default='', max_length=150)
    text = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, deletion.PROTECT)

    def __str__(self):
        return self.title
