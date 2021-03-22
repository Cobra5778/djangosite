#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=250,blank=True)
    art_data = models.TextField(default=None)
    state = models.DecimalField(max_digits=1, decimal_places=0, default=None)

class Articles_tree(models.Model):
    parent = models.IntegerField(default=None)
    id_articles = models.IntegerField(default=None)
    possision = models.DecimalField(max_digits=4, decimal_places=0, default=None)
    url = models.SlugField(max_length=100, blank=True)
    title = models.CharField(max_length=50,blank=True)
    type = models.DecimalField(max_digits=1, decimal_places=0, default=None)
