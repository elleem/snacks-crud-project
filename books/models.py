from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    image_url = models.URLField(default='none')

    def __str__(self):
        return self.name

#return user to the detail page of their new entry
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])