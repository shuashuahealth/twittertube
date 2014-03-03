# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django import forms
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def index(request):
    return render(request, 'homepage/index.html', {})
    #return HttpResponse("Hello, world. You're at the poll index.")


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()

def handle_uploaded_file(f):
    destination = default_storage.open('name.txt', 'wb+')
    for chunk in f.chunks():
            destination.write(chunk)
    destination.close()

def handlefile(request):
    return HttpResponse("upload succeed.")
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("upload succeed.")
    else:
        form = UploadFileForm()
    return HttpResponse("upload failed.")