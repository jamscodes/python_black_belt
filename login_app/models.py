from django.db import models
import re, datetime
import logging

logger = logging.getLogger(__name__)

# Create your models here.

class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = {}

        cur_date = datetime.datetime.today()
        delta = datetime.timedelta(days=4745)
        min_age_date = cur_date - delta

        if len(postData['pw']) < 8:
            errors['pw'] = 'Password should be at least 8 characters in length'
        if len(User.objects.filter(email = postData['email'])) > 0:
            errors['unq_email'] = 'There is already and account associated with this email'
        if datetime.datetime.strptime(postData.get('dob'), "%Y-%m-%d") > min_age_date:
            errors['not_old_enough'] = 'You must be at least 13 years old to register'
        
        return errors

class User(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    dob = models.DateField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # wishes = Wish.objects.get(id=user_id)
    # likes = Like.objects.get(id=user_id)

    def __repr__(self):
        return f'User: {self.f_name} {self.l_name}'