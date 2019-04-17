from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    # 关联个数
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    # list_display：显示字段，可以点击列头进行排序
    list_display = ['id', 'name', 'date']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['btitle']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['btitle']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 2
    # 再添加书的时候可以额外添加英雄
    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'sname', 'sxingbie','skill']
    # list_filter：过滤字段，过滤框会出现在右侧
    list_filter = ['hname']
    # search_fields：搜索字段，搜索框会出现在上侧
    search_fields = ['hname']
    # list_per_page：分页，分页框会出现在下侧
    list_per_page = 2



admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)

