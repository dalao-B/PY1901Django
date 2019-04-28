from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=20)
    pwd = models.CharField(max_length=100)
    college = models.CharField(max_length=50)
    num = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return "%d %s" % (self.pk, self.username)


class Books(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    publish_com = models.CharField(max_length=50)
    publish_date = models.DateField()

    def __str__(self):
        return "%d %s" % (self.pk, self.title)


class Historys(models.Model):
    date_borrow = models.DateField()
    date_return = models.DateField()
    status = models.BooleanField()
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    book = models.ForeignKey('Books', on_delete=models.CASCADE)

    def __str__(self):
        return "%d %s %s" % (self.pk, self.user, self.book)
