from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def hello(request):
    t = get_template('hello.html')
    html = t.render()
    return HttpResponse(html)

def login(request):
    t = get_template('login.html')
    html = t.render()
    return HttpResponse(html)

def adminpage(request):
    t = get_template('adminpage.html')
    html = t.render()
    return HttpResponse(html)

def submit(request):
    t = get_template('submit.html')
    html = t.render()
    return HttpResponse(html)

def guests(request):
    t = get_template('guests.html')
    html = t.render()
    return HttpResponse(html)

def logo(request):
    t = get_template('logo.html')
    html = t.render()
    return HttpResponse(html)