from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    privileges = models.CharField(max_length=3)

    def __str__(self):
        return self.username


class Archive(models.Model):
    name = models.CharField(max_length=250)
    format_type = models.CharField(max_length=10)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.name

class Nodes(models.Model):
    name = models.CharField(max_length=50)
    ip_addres = models.CharField(max_length=15)
    neighbor = models.CharField(max_length=50)

    def __str__(self):
        return self.name, self.ip_addres


