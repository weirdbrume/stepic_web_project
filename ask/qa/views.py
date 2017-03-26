from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request, *args, **kwargs):
    return HttpResponse('NEW')
