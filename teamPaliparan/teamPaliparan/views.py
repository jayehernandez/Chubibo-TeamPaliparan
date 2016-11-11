from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def hello(request):
    t = get_template('hello.html')
    html = t.render()
    return HttpResponse(html)