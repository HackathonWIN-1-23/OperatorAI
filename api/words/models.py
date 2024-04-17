from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.text