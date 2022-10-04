from enum import unique
from django.db import models

# Create your models==class here.
# Django will create SQL DB

class User(models.Model):
    firstN = models.CharField(max_length=60)
    lastN = models.CharField(max_length=60)
    email = models.CharField(max_length=60)

class Page(models.Model):
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12,unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Contect', blank=True)

    def __str__(self) -> str:
        return self.title + self.bodytext

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self) -> str:
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic,models.CASCADE) 
    name = models.CharField(max_length=264)
    url = models.URLField()

    def __str__(self) -> str:
        return self.name

# class AccessRecord(models.Model,models.CASCADE):
#     name = models.ForeignKey(WebPage)
#     date = models.DateField()

#     def __str__(self) -> str:
#         return str(self.date)
