from django.db import models

# Create your models here.


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    article_time = models.DateTimeField(auto_now_add=True)
    article_username = models.CharField(max_length=20)
    article_views = models.IntegerField(default=0)
    article_category = models.ForeignKey("Category", on_delete=models.CASCADE)
    article_tags = models.ManyToManyField(to="Tags")

    def __str__(self):
        return "%d %s " % (self.pk, self.title)


class Category(models.Model):
    """文章分类"""
    category_content = models.CharField(max_length=100)
    def __str__(self):
        return "%s " % (self.category_content)


class Tags(models.Model):
    """文章标签"""
    tags_content = models.CharField(max_length=100)
    def __str__(self):
        return "%s " % (self.tags_content)


class Comment(models.Model):
    """文章评论"""
    comment_username = models.CharField(max_length=100)
    comment_email = models.CharField(max_length=100)
    comment_addr = models.CharField(max_length=100)
    comment_time = models.DateTimeField()
    comment_content = models.CharField(max_length=100)
    comment_article = models.ForeignKey("Article", on_delete=models.CASCADE)
    def __str__(self):
        return "%s " % (self.comment_username)