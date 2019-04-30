from django.shortcuts import render

# Create your views here.
from django.shortcuts import reverse,redirect,render
from django.http import HttpResponseRedirect, HttpResponse, request
from . models import Users, Books, Historys, HotImages
import datetime,time
from hashlib import sha1
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired
from PIL import Image,ImageDraw,ImageFont
import random, io

def index(request):
    imglist = HotImages.objects.all().order_by("index")
    return render(request, 'mybooklibrary/index.html', {"imglist": imglist})


def reader(request):
    username = request.session.get("username")
    user = Users.objects.get(username=username)
    return render(request, 'mybooklibrary/reader.html',{"username":request.session.get("username"),"user":user})


def reader_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        verifycode = request.POST["verifycode"]
        password = sha1(password.encode('utf8')).hexdigest()
        user = Users.objects.all().filter(username=username)
        if user.__len__() == 0:
            error = 'Invalid username'
        elif not user[0].pwd == password:
            error = 'Invalid password'
        elif not verifycode == request.session.get("verifycode"):
            error = 'Invalid verifycode'
        elif not user[0].is_active:
            error = 'Not active'
        else:
            request.session['username'] = username
            return redirect(reverse('mybooklibrary:reader'))
    return render(request, 'mybooklibrary/reader_login.html', {"error": error})


def logout(request):
    request.session.pop("username")
    return redirect(reverse('mybooklibrary:index'))


def register(request):
    error = None
    if request.method == 'POST':
        if not request.POST['username']:
            error = 'You have to enter a username'
        elif not request.POST['password']:
            error = 'You have to enter a password'
        elif request.POST['password'] != request.POST['password2']:
            error = 'The two passwords do not match'
        elif Users.objects.all().filter(username=request.POST['username']).__len__() != 0:
            error = 'The username is already taken'
        else:
            username = request.POST['username']
            pwd = request.POST['password']
            pwd = sha1(pwd.encode('utf8')).hexdigest()
            college = request.POST['college']
            num = request.POST['number']
            email = request.POST['email']
            pic = request.FILES['header_img']
            user_content = request.POST["user_content"]
            user = Users()
            user.username = username
            user.pwd = pwd
            user.college = college
            user.num = num
            user.email = email
            user.header = pic
            user.user_content = user_content
            user.save()
            id = user.pk
            serutil = Serializer(settings.SECRET_KEY,50)
            resultid = serutil.dumps({"userid":id}).decode("utf8")

            send_mail("点击激活账户", "<a href = 'http://127.0.0.1:8000/active/%s'>点击：</a>"%(resultid),
                      settings.DEFAULT_FROM_EMAIL, [email,"zhibin61@163.com"])
            return redirect(reverse('mybooklibrary:reader_login'))
    return render(request, 'mybooklibrary/register.html', {"error": error})


def active(request, idstr):
    deser = Serializer(settings.SECRET_KEY, 50)
    try:
        obj = deser.loads(idstr)
        user = Users.objects.get(pk=obj["userid"])
        user.is_active = True
        user.save()
        return redirect(reverse('mybooklibrary:reader_login'))
    except SignatureExpired as e:
        return render(request, 'mybooklibrary/active.html')



def reader_info(request):
    username = request.session.get("username")
    user = Users.objects.get(username=username)
    return render(request, 'mybooklibrary/reader_info.html', {"user": user})


def reader_modify(request):
    error = None
    username = request.session.get("username")
    user = Users.objects.get(username=username)
    if request.method == 'POST':
        if not request.POST['username']:
            error = 'You have to input your name'
        elif not request.POST['password']:
            username = request.POST['username']
            college = request.POST['college']
            num = request.POST['number']
            email = request.POST['email']
            pic = request.FILES['header_img']
            user_content = request.POST["user_content"]
            user.username = username
            user.college = college
            user.num = num
            user.email = email
            user.header = pic
            user.user_content = user_content
            user.save()
            request.session['username'] = username
            return redirect(reverse('mybooklibrary:reader_info'))
        else:
            username = request.POST['username']
            pwd = request.POST['password']
            college = request.POST['college']
            num = request.POST['number']
            email = request.POST['email']
            pic = request.FILES['header_img']
            user_content = request.POST["user_content"]
            user.username = username
            user.pwd = pwd
            user.college = college
            user.num = num
            user.email = email
            user.header = pic
            user.user_content = user_content
            user.save()
            request.session['username'] = username
            return redirect(reverse('mybooklibrary:reader_info'))
    return render(request, 'mybooklibrary/reader_modify.html', {"user": user, "error": error})


def reader_query(request):
    error = None
    books = None
    if request.method == 'POST':
        if request.POST['item'] == 'name':
            if not request.POST['query']:
                error = 'You have to input the book name'
            else:
                books = Books.objects.all().filter(title__icontains=request.POST['query'])
                if not books:
                    error = 'Invalid book name'
        else:
            if not request.POST['query']:
                error = 'You have to input the book author'
            else:
                books = Books.objects.all().filter(author__icontains=request.POST['query'])
                if not books:
                    error = 'Invalid book author'
    return render(request, 'mybooklibrary/reader_query.html', {'books':books, "error":error})


def reader_book(request, bookid):
    error = None
    username = request.session.get("username")
    user = Users.objects.get(username=username)
    book = Books.objects.get(pk=bookid)
    historys = book.historys_set.all()

    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return_time = time.strftime('%Y-%m-%d', time.localtime(time.time() + 2600000))

    if request.method == 'POST':
        for history in historys:
            if history.status is True:
                error = 'The book has already borrowed.'
                break
        else:
            history = Historys()
            history.book = book
            history.user = user
            history.date_borrow = current_time
            history.date_return = return_time
            history.status = True
            history.save()
            return redirect(reverse('mybooklibrary:reader_book', args=(bookid,)))
    return render(request, 'mybooklibrary/reader_book.html', {'book': book, 'historys': historys, "error": error})


def reader_histroy(request):
    username = request.session.get("username")
    user = Users.objects.get(username=username)
    historys = user.historys_set.all()
    return render(request, 'mybooklibrary/reader_histroy.html', {"historys": historys})


def mail(request):
    send_mail("Django","hello,everybody!",
              settings.DEFAULT_FROM_EMAIL,["zhibin61@163.com","zhibin61@163.com"]
              )
    return HttpResponse("发送成功！")


def verifycode(request):
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    print(rand_str,"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # 构造字体对象
    font = ImageFont.truetype('LCALLIG.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')
