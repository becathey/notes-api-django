from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.title