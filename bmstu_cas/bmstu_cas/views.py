from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    if request.user.is_authenticated:
         redirect('http://guimc-dev.eu.bmstu.ru/api/registration/?ticket=ST-85631-zsP2W3qqmc1gAvhsGze6-proxy')
        #return HttpResponse('<p>Вы вошли как <strong>%s</strong>.</p><p><a href="/cas/logout">Выйти</a></p>' % request.user)
    else:
        return HttpResponse('<a href="https://proxy.bmstu.ru:8443/cas/login">Войти</a>')
