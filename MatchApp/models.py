from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
       is_company = models.BooleanField(default=False)

       def __str__(self):
              return self.username


class RegularUser(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
       age = models.IntegerField()
       name = models.CharField(max_length=50)
       email = models.EmailField(max_length=50)
       phone = models.CharField(max_length=50)
       address = models.CharField(max_length=50)
       desired_salary = models.IntegerField()
       desired_position = models.CharField(max_length=50)

       def __str__(self):
              return self.name