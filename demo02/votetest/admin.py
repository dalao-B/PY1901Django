from django.contrib import admin
from .models import QuestionInfo, VoteInfo

# Register your models here.

class VoteInfoInline(admin.StackedInline):
    model = VoteInfo
    extra = 1


class QuestionInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'qtitle', 'qpub_date']
    list_filter = ['qtitle']
    search_fields = ['qtitle']
    list_per_page = 2

    inlines = [VoteInfoInline]


class VoteInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'vcontent', 'vnum']
    list_filter = ['vcontent']
    search_fields = ['vcontent']
    list_per_page = 2


admin.site.register(QuestionInfo)
admin.site.register(VoteInfo)