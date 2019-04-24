from django.contrib import admin
from  .models import Article, Category, Tags, Comment

# Register your models here.



class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title ', 'content', 'article_time', 'article_username', 'article_views',
                    'article_comment_num']
    list_filter = ['title']
    list_per_page = 2


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_content ']
    list_filter = ['category_content']
    list_per_page = 2


class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'tags_content ']
    list_filter = ['tags_content']
    list_per_page = 2


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment_username ', 'comment_email', 'comment_addr', 'comment_time', 'comment_content']
    list_filter = ['comment_username']
    list_per_page = 2


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Comment)