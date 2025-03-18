"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from http.client import responses

from django.contrib import admin
from django.http import HttpResponse, Http404
from django.urls import path
from django.shortcuts import render, redirect
from bookmark import views



football_ranking=[
    {'Team':'리버풀', 'ranking':'1'},
    {'Team':'아스날', 'ranking':'2'},
    {'Team':'노팅엄', 'ranking':'3'},
    {'Team':'첼시', 'ranking':'4'},
    {'Team':'맨시티', 'ranking':'5'}
]


def index(request):
    return HttpResponse("Hello")

def book_list(request):
    # book_text = ''
    #
    # for i in range(0, 10):
    #     book_text += f'book {i}<br>'

    return render(request, template_name='book_list.html', context={'range':range(0, 10)})

def book(request, num):

    return render(request, template_name='book_detail.html', context={'num':num})

def language(request, lang):
    return HttpResponse(f'<h1>{lang}언어 페이지 입니다.')

def footballs(request):
    # football_teams = [football['Team'] for football in football_ranking]
    #
    #
    #     # football_teams = []
    #     # for football in football_ranking:
    #     #   football_teams.append(football['team'])
    # responses_text = ''
    # for index, Team in enumerate(football_teams):
    #     responses_text += f'<a href="/football/{index}">{Team}</a><br>'
    # return HttpResponse(responses_text)

    return render(request, template_name='football.html', context={'football_ranking': football_ranking})
def football_detail(request, index):
    if index > len(football_ranking) -1 :
        raise Http404

    football = football_ranking[index]

    # responses_text = f'<h1>{football["Team"]}</h1> <p>순위 :{football["ranking"]}</p>'
    context = {'football':football}
    return render(request, template_name='footballs.html', context=context)

def gugu(request, num):
    if num < 2 :
        return redirect('/gugu/2')
    # table = []
    # for i in range(2, 10):
    #     row = []
    #     for j in range(1, 10):
    #         row.append(f'{i}x{j} = {i * j}')
    #     table.append(row)
    # context = {'table':table}
    context = {
        'num':num,
        'results':[num * i for i in range(1, 10)]
    }
    return render(request, 'gugu.html', context)







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),

    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', language),
    path('football/', footballs),
    path('football/<int:index>/', football_detail),
    path('gugu/<int:num>/', gugu),
    path('bookmark/', views.bookmark_list),
    path('bookmark/<int:pk>/', views.bookmark_detail),
]
