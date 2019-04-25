from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse


class ArticleFeed(Feed):
    title = '文章'
    link = '/'

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse('myblog:single', args=(item.id,))