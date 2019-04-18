from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .models import QuestionInfo, VoteInfo
# Create your views here.


def index(request):

    questionlist = QuestionInfo.objects.all()
    return render(request, 'votetest/index.html', {"questionlist": questionlist})


def detail(request, id):
    question = QuestionInfo.objects.get(pk=id)
    vote = question.voteinfo_set.all()
    # print(question.qtitle)
    return render(request, 'votetest/detail.html', {"vote":vote,"question":question})


def vote(request, id):

    voteid = request.POST["choice"]
    vote = VoteInfo.objects.get(pk=int(voteid))
    vote.vnum += 1
    vote.save()
    question = QuestionInfo.objects.get(pk=id)
    vote = question.voteinfo_set.all()
    # vnum = vote.vnum + 1
    # return HttpResponse("aaaaaaaaaaaaaaa")
    return render(request, 'votetest/vote.html', {"vote": vote, "question":question})