from django.http import HttpResponse
from django.shortcuts import render
from HW_2.models import User


def user(request):
    res = User.objects.all()
    print(res)
    res1 = ['<br>' + str(i) for i in res]
    return HttpResponse(f'{res1}')
