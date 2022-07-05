from django.http import HttpResponse


def index(request):
    if request.user.is_authenticated:
        return HttpResponse('<p>Вы вошли как <strong>%s</strong>.</p><p><a href="/cas/logout">Выйти</a></p>' % request.user)
    else:
        return HttpResponse('<a href="https://proxy.bmstu.ru:8443/cas/login?service=http%3A%2F%2Fguimc-dev.eu.bmstu.ru%2Fapi%2Fregistration%2F">Войти</a>')