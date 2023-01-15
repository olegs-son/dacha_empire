from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.TextField()
    password = models.TextField()

    def __str__(self) -> str:
        return f"{self.fname} {self.lname}({self.id})"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_by = models.ForeignKey("User", on_delete=models.CASCADE)
    date_published = models.DateField()
    date_start = models.DateField()
    date_end = models.DateField()