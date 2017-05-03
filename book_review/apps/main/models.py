from __future__ import unicode_literals

from django.db import models

import re, bcrypt
# Create your models here


class UserManager(models.Manager):
    def validateUser(self, post):
        is_valid = True
        errors = []
        if len(post.get('name')) == 0:
            errors.append('Name must not be blank')
            is_valid = False
        user = User.objects.filter(email=post.get('email')).first()
        if user:
            errors.append('This email is already registered')
            is_valid = False
        if not re.search(r'^\w+\@\w+\.\w+', post.get('email')):
            errors.append('You must use a valid email')
            is_valid = False
        # if len(post.get('password'))<4:
        #     errors.append('You must use more than 4 letters in PW')
        #     is_valid = False
        # if post.get('password') != post.get('confirm'):
        #     errors.append('Your passwords do not match')
        #     is_valid = False
        return {'status' : is_valid, 'errors': errors}

    def createUser(self, post):
        return User.objects.create(
        name=post.get('name'),
        email=post.get('email'),
        password=bcrypt.hashpw(post.get('password').encode(), bcrypt.gensalt())
        )


    def loginUser(self, post):
        user = User.objects.filter(email=post.get('email')).first()
        if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
            return {"status" : True, 'user' : user }
        else:
            return {'status': False, 'message' : "invalid user."}






class User(models.Model):
    name = models.CharField(max_length=255)
    email   = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="book")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reviews(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
