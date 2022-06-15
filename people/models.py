from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)


    class Meta:
        verbose_name_plural = "People"
        
    def __str__(self):
        return self.name
