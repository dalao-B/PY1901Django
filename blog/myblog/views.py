from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,request
from django.shortcuts import reverse,redirect,render
from  .models import Article, Category, Tags, Comment
import datetime


# Create your views here.


def index(request):
    articlelist = Article.objects.all()
    categorylist = Category.objects.all()
    tagslist = Tags.objects.all()
    now_time = datetime.datetime.now()
    # content = articlelist[0].content
    # small_text = content[:50]
    # if small_text == content:
    #     return render(request, 'myblog/index.html', {"articlelist":articlelist, "small_text":content})
    # else:
    #     return render(request, 'myblog/index.html', {"articlelist": articlelist, "small_text": small_text+"..."})
    return render(request, 'myblog/index.html', {"articlelist": articlelist,
                                                 "categorylist":categorylist, "tagslist":tagslist, "now_time":now_time})


def single(request, id):
    now_time = datetime.datetime.now()
    articlelist = Article.objects.all()
    categorylist = Category.objects.all()
    tagslist = Tags.objects.all()
    cur_article = Article.objects.get(pk=id)
    cur_article.article_views += 1
    cur_article.save()
    return render(request, 'myblog/single.html', {"cur_article":cur_article, "articlelist": articlelist,
                                                 "categorylist":categorylist, "tagslist":tagslist, "now_time":now_time})


def category(request, id):
    now_time = datetime.datetime.now()
    articlelist = Article.objects.all()
    categorylist = Category.objects.all()
    tagslist = Tags.objects.all()
    cur_category = Category.objects.get(pk=id)
    cur_articlelist = cur_category.article_set.all()
    now_time = datetime.datetime.now()
    return render(request, 'myblog/category.html', {"cur_articlelist": cur_articlelist,"articlelist": articlelist,
                                                 "categorylist":categorylist, "tagslist":tagslist, "now_time":now_time})


def tags(request, id):
    now_time = datetime.datetime.now()
    articlelist = Article.objects.all()
    categorylist = Category.objects.all()
    tagslist = Tags.objects.all()
    cur_tags = Tags.objects.get(pk=id)
    cur_articlelist = cur_tags.article_set.all()
    return render(request, 'myblog/category.html', {"cur_articlelist": cur_articlelist,"articlelist": articlelist,
                                                 "categorylist":categorylist, "tagslist":tagslist, "now_time":now_time})


def filetime(request, y ,m):
    now_time = datetime.datetime.now()
    articlelist = Article.objects.all()
    categorylist = Category.objects.all()
    tagslist = Tags.objects.all()
    cur_articlelist = Article.objects.all().filter(article_time__year=y).filter(article_time__month=m)
    return render(request, 'myblog/filetime.html', {"cur_articlelist": cur_articlelist, "articlelist": articlelist,
                                                    "categorylist": categorylist, "tagslist": tagslist, "now_time":now_time})


def comment(request, id):
    print("aaaaaaaaaaaaaa")
    name = request.POST["name"]
    email = request.POST["email"]
    url = request.POST["url"]
    comment = request.POST["comment"]

    print(name,email,url,comment)
    article = Article.objects.get(pk=id)
    cur_comment = Comment()
    cur_comment.comment_username = name
    cur_comment.comment_email = email
    cur_comment.comment_addr = url
    cur_comment.comment_time = datetime.datetime.now()
    cur_comment.comment_content = comment
    cur_comment.comment_article = article
    cur_comment.save()

    return HttpResponseRedirect("/single/"+str(id)+"/")
