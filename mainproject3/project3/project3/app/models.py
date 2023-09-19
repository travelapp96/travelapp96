from django.db import models


class Place(models.Model):  # here places is table name
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    profile = models.ImageField(upload_to='pics')
    name_1 = models.CharField(max_length=250)
    about = models.TextField()

    def __str__(self):
        return self.name_1
