from django.shortcuts import render
from django.http import HttpResponse


def index(reuqest):
    return HttpResponse('<h1>Привет Мир!</h1>')
