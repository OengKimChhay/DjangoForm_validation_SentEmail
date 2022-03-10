from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    contact = models.TextField(max_length=225)
    created = models.DateTimeField(auto_now_add=True)
    views = models.BigIntegerField(default=0)

    class Meta:
        db_table = "employee"
