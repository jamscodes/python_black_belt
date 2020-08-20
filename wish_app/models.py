from django.db import models
from login_app.models import User

# Create your models here.

class Wish(models.Model):
    wish = models.CharField(max_length=255)
    desc = models.TextField()
    wisher = models.ForeignKey(User, related_name='wishes', on_delete=models.CASCADE)
    granted = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # likes = Like.objects.get(id=wish_id)

    def __repr__(self):
        return f'{self.wisher.f_name}\'s wish: {self.wish}'

class Like(models.Model):
    wisher = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    wish = models.ForeignKey(Wish, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)