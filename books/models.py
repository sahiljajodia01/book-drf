from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=40)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication = models.DateField()

    def __str__(self):
        return self.title
