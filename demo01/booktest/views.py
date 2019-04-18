from django.shortcuts import render
from django.template import loader, RequestContext
from .models import BookInfo, HeroInfo

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


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


def delete(request, id):
    try:
        BookInfo.objects.get(pk=id).delete()
        booklist = BookInfo.objects.all()
        # return render(request, 'booktest/list.html',{"booklist": booklist})
        return HttpResponseRedirect('/list',{"booklist": booklist})
    except:
        return HttpResponse("删除失败！！！")


def addhero(request, bookid):
    return render(request, 'booktest/addhero.html', {"bookid":bookid})


def addherohandler(request):
    bookid = request.POST["bookid"]
    hname = request.POST["heroname"]
    hgender = request.POST["sex"]
    hcontent = request.POST["herocontent"]
    print(hname)

    book = BookInfo.objects.get(pk=bookid)
    hero = HeroInfo()
    hero.hname = hname
    hero.hgender = hgender
    hero.hcontent = hcontent
    hero.hbook = book
    hero.save()

    return HttpResponseRedirect("/detail/"+str(bookid)+"/",{"book":book})