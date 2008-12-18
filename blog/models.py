# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime

class BlogPost(models.Model):
    title   = models.CharField(max_length=128)
    pub_date = models.DateField(editable=False)
    author  = models.ForeignKey(User)
    text    = models.TextField(max_length=2048)
    
    def save(self):
        if not self.id:
            self.pub_date = datetime.date.today()
        super(BlogPost, self).save()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/"
