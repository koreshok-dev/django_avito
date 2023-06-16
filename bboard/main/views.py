from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def other_page(request, page):
    try:
        t=get_template(f'main/{page}.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(t.render(request=request))