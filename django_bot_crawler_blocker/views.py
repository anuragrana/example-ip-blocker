from django.http import HttpResponse


def index(request):
    print("I am in view")
    return HttpResponse("Hello")