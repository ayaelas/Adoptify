from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path
from django.template.loader import render_to_string
# Create your views here.


def about(request):
    html_content = render_to_string('adoptify/about.html')
    return HttpResponse(html_content)


def index(request):
    html_content = render_to_string('adoptify/index.html')
    return HttpResponse(html_content)

def blog(request):
    html_content = render_to_string('adoptify/blog.html')
    return HttpResponse(html_content)

def contacter(request):
    html_content = render_to_string('adoptify/contacter.html')
    return HttpResponse(html_content)
