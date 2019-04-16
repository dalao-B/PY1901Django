from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return "%d %s" % (self.pk, self.btitle)



class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    def __str__(self):
        return "%d %s" % (self.pk, self.hname)
