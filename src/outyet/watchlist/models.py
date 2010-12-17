from django.db import models
import datetime
#from django.core.management.validation import max_length

class Watchlist(models.Model):
    title = models.CharField(max_length=30)
    priority = models.IntegerField()
    
    def __unicode__(self):
        return self.title

class Title(models.Model):    
    type = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    release_date = models.DateField()
    
    def days_left(self):
        return self.release_date - datetime.date.today()
    
    def __unicode__(self):
        return self.title

class Entry(models.Model):
    watchlist = models.ForeignKey(Watchlist)
    title = models.ForeignKey(Title)