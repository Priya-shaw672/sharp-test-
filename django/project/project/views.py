from django . http import HttpResponse
from django . shortcuts import render
from project import views
from app.models import Exam
from app.models import Gk
from app.models import Django


# Create your views here.
def webpage1(request):
    return render(request,'index.html')

def webpage2(request):
    return render(request,'login.html')

def webpage3(request):
    return render(request,'all-quiz.html')

def webpage4(request):
       django=Django.objects.all()
       return render(request,"computer.html",{"django":django})


def webpage5(request):
    return render(request,'leaderboard.html')


def webpage6(request):
       gk=Gk.objects.all()
       return render(request,"gk.html",{"gk":gk})


def webpage7(request):
    return render(request,'life.html')


def webpage8(request):
    return render(request,'math.html')


def webpage9(request):
    return render(request,'physics.html')

def webpage10(request):
    return render(request,'register.html')

def webpage11(request):
    return render(request,'blogs.html')

def webpage12(request):
    return render(request,'confirm.html')

def webpage13(request):
    return render(request,'contact-us.html')

def webpage14(request):
    return render(request,'dashboard.html')

def webpage15(request):
    return render(request,'downloads.html')

def webpage16(request):
    return render(request,'message.html')

def webpage17(request):
    return render(request,'profile-edit.html')

def webpage18(request):
    return render(request,'terms and condition.html')


def webpage19(request):
    return render(request,'profile.html')


def home(request):
    exam=Exam.objects.all()
    return render(request,"question.html",{"exam":exam})

