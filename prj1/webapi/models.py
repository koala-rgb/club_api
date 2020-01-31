from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

class Member(models.Model):
    first = models.CharField(max_length=20, default = ' ')
    last = models.CharField(max_length=20, default=' ')
    email = models.EmailField(max_length=50, default=' ')
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.first + " " + self.last

    def addInterest(self):
        interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

class Interest(models.Model):
    name = models.CharField(max_length=40, default=' ')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return self.name