from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=30)
    birth = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return f"[{self.pk} / {self.name} / {self.email}]"

    def get_url(self):
        return f'/member/{self.pk}/'