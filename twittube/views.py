# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django import forms
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

import sys
sys.path.append( '..' )
from twittube.models import Sponsor
from conversation.models import Participant

def index(request):
    all_sponsors = Sponsor.objects.all()
    return render(request, 'twittube/index.html', {'all_s':all_sponsors})
    #return HttpResponse("Hello, world. You're at the index.")


class UploadFileForm(forms.Form):
    file  = forms.FileField()

def handlefile(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #return HttpResponse(request.FILES['file'].read())
        if form.is_valid():
            s = Sponsor()
            s.save()
            filename = str(s.id)+'_0.mp4'
            s.filename = filename
            s.save()
            default_storage.save(filename, request.FILES['file'])
            return HttpResponseRedirect(reverse('twittube.views.index'))
        else:
            return HttpResponse("upload form invalid")
    else:
        form = UploadFileForm()
    return HttpResponse("upload failed.")

