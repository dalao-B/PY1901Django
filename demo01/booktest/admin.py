from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
