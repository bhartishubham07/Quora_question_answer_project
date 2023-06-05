from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from django.http import HttpResponse
from django.core.mail import send_mail
from app.forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView,DetailView


def registeration(request):
    UFO=UserForm()
    d={'UFO':UFO}
    if request.method=='POST':
        UFD=UserForm(request.POST)
        if UFD.is_valid():
            NSUO=UFD.save(commit=False)
            password=UFD.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            

            return render(request,'app/register_done.html')
        else:
            return render(request,'app/register_notdone.html')
    return render(request,'app/registeration.html',d)

def register_done(request):
    return render(request, 'app/register_done.html')

def register_notdone(request):
    return render(request, 'app/register_notdone.html')


def user_login(request):
    LFO = LoginForm()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('QuestionList'))
        else:
            return render(request,'app/register_notdone.html')
        
    return render(request,'app/user_login.html',{'LFO':LFO})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('QuestionList'))


class QuestionList(ListView):
    model = Question
    context_object_name='questions'

class QuestionDetail(DetailView):
    model =Question
    context_object_name='Qcl'





@login_required
def ask_question(request):
    QFO= QuestionForm()
    d={'QFO':QFO}
    if request.method == 'POST':
        QFD = QuestionForm(request.POST)
        if QFD.is_valid():
            username=request.session['username']
            UO=User.objects.get(username=username)

            NSAQO = QFD.save(commit=False)
            NSAQO.user = UO
            NSAQO.save()
            return HttpResponseRedirect(reverse('QuestionList'))
        else:
            return HttpResponse('Question not asked successfully')
        
    return render(request, 'app/ask_question.html',d)

    
@login_required
def answer_question(request):
    AQO = AnswerForm()
    d={'AQO':AQO}
    question = Question.objects.all()
    if request.method == 'POST':
        AQD= AnswerForm(request.POST)
        if AQD.is_valid():
            username=request.session['username']
            UO=User.objects.get(username=username)
            NSAQO = AQD.save(commit=False)
            NSAQO.user = UO
            NSAQO.save()
            Q=NSAQO.question
            AO=Answer.objects.filter(question=Q)
            d1={'AO':AO}
            return HttpResponseRedirect(reverse('QuestionList'))
        else:
            return HttpResponse('Question not asked successfully')
        
    return render(request, 'app/answer_question.html',d)

