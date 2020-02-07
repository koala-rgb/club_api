from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Member(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.first + " " + self.last

class Interest(models.Model):
    name = models.CharField(max_length=40)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.name