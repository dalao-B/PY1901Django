from django.shortcuts import render
from django.template import loader, RequestContext
from .models import BookInfo, HeroInfo

# Create your views here.
from django.http import HttpResponse


def index(request):
    # template = loader.get_template('booktest/index.html')
    context = {"username":"aaa"}
    return render(request, 'booktest/index.html', context)
    # result = template.render(context=context)
    # return HttpResponse(result)
    # return HttpResponse("index")


def detail(request, id):
    # template = loader.get_template('booktest/detail.html')
    book = BookInfo.objects.get(pk=id)
    context = {"book": book}
    return render(request, 'booktest/detail.html', context)
    # result = template.render(context=context)
    # return HttpResponse("详情页 %s" %id)
    # return HttpResponse("detail %s" %id)


def list(request):
    # template = loader.get_template('booktest/detail.html')
    booklist = BookInfo.objects.all()
    context = {"booklist":booklist}
    return render(request, 'booktest/list.html', context)
    # result = template.render(context=context)
    # return HttpResponse(result)
    # return HttpResponse("liebiaoye")
