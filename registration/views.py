from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> Witamy na stronie rejestracji</h1>")
