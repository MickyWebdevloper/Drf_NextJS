from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

User = get_user_model()


class Posts(models.Model):
    slug = models.SlugField(max_length=25)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ['date_created']
        verbose_name_plural = ("Posts")

    # def __str__(self):
    #     return self.author.username

    # def get_absolute_url(self):
    #         return reverse("_detail", kwargs={"pk": self.pk})
