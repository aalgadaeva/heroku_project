import os
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files import File

class HomePageView(TemplateView):
    template_name = 'home.html'

def about(request):
    f = open('templates/about.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
        
def contacts(request):
    f = open('templates/contacts.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

class GalleryPageView(TemplateView):
    template_name = 'gallery.html'