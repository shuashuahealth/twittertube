# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django import forms
from .forms import ModelFormWithFileField

def index(request):
    return render(request, 'homepage/index.html', {})
    #return HttpResponse("Hello, world. You're at the poll index.")


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()

def handle_uploaded_file(f):
    with open('test.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handlefile(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render(request, 'homepage/index.html', {})
    else:
        form = UploadFileForm()
    return render(request, 'homepage/index.html', {})

