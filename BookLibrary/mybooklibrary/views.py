from django.shortcuts import render

# Create your views here.
from django.shortcuts import reverse,redirect,render
from django.http import HttpResponseRedirect, HttpResponse, request
from . models import Users, Books, Historys, HotImages
import datetime,time
from hashlib import sha1


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
        password = sha1(password.encode('utf8')).hexdigest()
        user = Users.objects.all().filter(username=username)
        if user.__len__() == 0:
            error = 'Invalid username'
        elif not user[0].pwd == password:
            error = 'Invalid password'
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
            return redirect(reverse('mybooklibrary:reader_login'))
    return render(request, 'mybooklibrary/register.html', {"error": error})


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


