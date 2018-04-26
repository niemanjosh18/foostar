from django.db import models

# Create your models here.

class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')


class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)

class Location(models.Model):
        location = models.IntegerField(default=0)

class Player(models.Model):
        username = models.CharField(max_length=50)
        pin = models.IntegerField(default=0)
        ratingS = models.IntegerField(default=0)
        ratingD = models.IntegerField(default=0)
        dateAdd = models.DateTimeField('date add')
        firstN = models.CharField(max_length=20)
        lastN = models.CharField(max_length=20)
        avatarId = models.IntegerField(default=0)
        locationId = models.ForeignKey(Location, on_delete=models.CASCADE)

class Singles(models.Model):
        date = models.DateTimeField("Game Date")
        sp1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="sp1")
        sp2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="sp2")
        p1Score = models.IntegerField(default=0)
        p2Score = models.IntegerField(default=0)

class Doubles(models.Model):
        date = models.DateTimeField("Game Date")
        dp1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="dp1")
        dp2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="dp2")
        dp3 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="dp3")
        dp4 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="dp4")
        t1Score = models.IntegerField(default=0)
        t2Score = models.IntegerField(default=0)

