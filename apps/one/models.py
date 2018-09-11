from django.db import models
import bcrypt
import re
from datetime import datetime
import time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class UserManager(models.Manager):
    def validations(self,postData):
        errors={}
        if len(postData['display_name']) < 1:
            errors['display_name'] = "Cannot be empty"
        elif len(postData['display_name']) < 4:
            errors['display_name'] = "No fewer than 4 characters for name;"
        if len(postData['first_name']) < 1:
            errors['first_name'] = "Cannot be empty"
        elif len(postData['first_name']) < 3:
            errors['first_name'] = "No fewer than 3 characters for name;"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Cannot be empty"
        elif len(postData['last_name']) < 3:
            errors['last_name'] = "No fewer than 3 characters for name;"         
        elif len(postData['email']) < 1:
            errors['email'] = "Cannot be empty"        
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        else: 
            same_email = self.filter(email=postData['email'])
            if len(same_email) > 0:
                errors['email'] = 'Email is taken'
        if len(postData['email']) < 1:
            errors['email'] = "Email is required"
        if len(postData['password']) < 8:
            errors['password'] = "No fewer than 8 characters in length for"
        elif postData['password'] != postData['confirm_password']:
            errors['password'] = "Passwords must match"
        if len(errors):
            result = {
                'errors': errors
            }
        else:
            hashed_pw =bcrypt.hashpw(postData['password'].encode(),bcrypt.gensalt())
            user= self.create(
                display_name=postData['display_name'],
                first_name = postData['first_name'],
                last_name = postData['last_name'],
                email = postData['email'],
                password = hashed_pw,
                dob = postData['birthday']
            )
            result ={
                'user_add' : user
            }
        return result

class User(models.Model):
    display_name=models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    dob = models.DateField(max_length=8)
    gold = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    favorite_weapon = models.TextField(default="")
    favorite_background = models.TextField(default="")
    favorite_aura = models.TextField(default="")
    favorite_head = models.TextField(default="")
    programming_language=models.TextField(default='')
    location = models.CharField(max_length=30,default='')
    created_at = models.DateTimeField(auto_now_add=True)

    objects=UserManager()

class Question(models.Model):
    content = models.TextField()
    difficulty = models.CharField(max_length=10)
    category = models.CharField(max_length=20,default ='python')
    created_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    content = models.TextField()
    correct = models.BooleanField()
    question = models.ForeignKey(Question, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)

class Weapon(models.Model):
    name = models.TextField()
    image =models.TextField(default="")
    owner = models.ManyToManyField(User, related_name="weapons")
    price = models.IntegerField(default=0)
class Aura(models.Model):
    name = models.TextField()
    image =models.TextField(default="")
    owner = models.ManyToManyField(User, related_name="auras")
    price = models.IntegerField(default=0)
class Background(models.Model):
    name = models.TextField()
    image = models.TextField(default="")
    owner = models.ManyToManyField(User, related_name="backgrounds")
    price = models.IntegerField(default=0)
class Gold(models.Model):
    amount = models.IntegerField()
    price = models.IntegerField()


