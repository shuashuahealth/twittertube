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
    file  = forms.FileField()

def handlefile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #return HttpResponse(request.FILES['file'].read())
        if form.is_valid():
            return HttpResponse(request.FILES['file'].content-type)
            default_storage.save('minikey.txt', request.FILES['file'])
            return HttpResponse("upload succeed.")
        else:
            return HttpResponse("upload forminvalid")
    else:
        form = UploadFileForm()
        return HttpResponse("upload else")
    return HttpResponse("upload failed.")