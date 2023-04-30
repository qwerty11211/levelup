from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    score=models.IntegerField(default=0)
    def __str__(self):
        return self.username

class Battle(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    end_date = models.DateTimeField()

    challenge_amount=models.CharField(max_length=100)
    created_by=models.CharField(max_length=100)
    number_of_users=models.IntegerField(default=0)
    cash_pool=models.IntegerField(default=0)

class History(models.Model):
    battle_id=models.IntegerField(default=1)
    message=models.CharField(max_length=100)

class Checkin(models.Model):
    image = models.ImageField(upload_to='images/')

class Money(models.Model):
    user_id=models.IntegerField()
    user_name=models.CharField(max_length=100)
    money=models.IntegerField()