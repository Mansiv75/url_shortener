from django.db import models

# Create your models here.
class URL(models.Model):
    original_url=models.URLField()
    shortened_url=models.CharField(max_length=10,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} -> {self.shortened_url}"