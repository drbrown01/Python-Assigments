from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

# Create your models here.print post
class UserManager(models.Manager):
    def validateUser(self, post):
        is_valid = True
        errors = []
        if len(post.get('name')) == 0:
            is_valid = False
            errors.append('Name field cannot be blank')
	    if not re.search(r'\w+\@\w+\.\w+', post.get('email')):
                is_valid = False
                errors.append('You must provide a valid email address')
        if len(post.get('password')) == 0:
            is_valid = False
            errors.append('Password cannot be blank')
	if post.get('password') != post.get('password_confirmation'):
            is_valid = False
            errors.append('Your passwords do not match')
	return (is_valid, errors)

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
