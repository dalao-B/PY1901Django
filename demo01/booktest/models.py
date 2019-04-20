from django.db import models

# Create your models here.

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return "%d %s" % (self.pk, self.btitle)

    def name(self):
        return self.btitle
    name.short_description = "书名"


    def date(self):
        return self.bpub_date
    date.short_description = "日期"



class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=50)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    def __str__(self):
        return "%d %s" % (self.pk, self.hname)

    def skill(self):
        return self.hcontent
    skill.short_description = "英雄技能"


    def sxingbie(self):
        return self.hgender
    sxingbie.short_description = "性别"


    def sname(self):
        return self.hname
    sname.short_description = "姓名"


class Goods(models.Model):
    name = models.CharField(max_length=20)
    @classmethod
    def creatr(cls, name):
        return cls(name=name)


class GoodsManage(models.Manager):
    def create_book(self, name):
        goods =  self.model()
        goods.name = name
        return goods


class Goods1(models.Model):
    name = models.CharField(max_length=20)
    gdmanager = GoodsManage()


class GoodsManage2(models.Manager):
    def create_book(self, name):
        return self.create(name = name)


class Goods2(models.Model):
    name = models.CharField(max_length=20)
    gdmanager = GoodsManage2()
