"""
URL configuration for Quora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registeration/', registeration, name='registeration'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', user_logout, name='user_logout'),
    path('register_done/',register_done, name='register_done'),
    path('register_notdone/',register_notdone, name='register_notdone'),
    
    path('QuestionList/',QuestionList.as_view(),name='QuestionList'),
    path('QuestionDetail/',QuestionDetail.as_view(),name='QuestionDetail'),
    path('ask_question/',ask_question,name='ask_question'),
    path('answer_question/',answer_question,name='answer_question'),
    
    
    re_path('(?P<pk>\d+)/',QuestionDetail.as_view(),name='detail'),
]
