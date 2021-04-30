from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quantity_pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_inclusion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
