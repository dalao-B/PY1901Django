from django.db import models

# Create your models here.

class QuestionInfo(models.Model):
    '''问题模型类'''
    qtitle = models.CharField(max_length=100)
    qpub_date = models.DateTimeField()

    def __str__(self):
        return "%d %s" % (self.pk, self.qtitle)


class VoteInfo(models.Model):
    vcontent = models.CharField(max_length=20)
    vnum = models.IntegerField()
    vquestion = models.ForeignKey('QuestionInfo', on_delete=models.CASCADE)
    def __str__(self):
        return "%d %s" % (self.pk, self.vcontent)

