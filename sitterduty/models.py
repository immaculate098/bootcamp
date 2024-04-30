from django.db import models


class Sitter(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    on_duty = models.BooleanField(default=False)
    off_duty = models.BooleanField(default=False)

    def __str__(self):
        return self.name
