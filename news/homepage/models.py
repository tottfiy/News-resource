from django.db import models


class News(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=60)
    date = models.DateTimeField(max_length=40)
    text = models.TextField(max_length=5000)

    def __str__(self):
        return (f'{self.name}, '
                f'{self.author}, '
                f'{self.date}, '
                f'({self.text})')


class Authors(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    short_text = models.TextField(max_length=300)

    def __str__(self):
        return (f'{self.name}, '
                f'{self.surname}, '
                f'{self.short_text}')
