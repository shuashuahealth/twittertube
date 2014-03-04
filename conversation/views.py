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

def index(request, sponsor_id):
    s = Sponsor.objects.get(pk=sponsor_id)
    all_participants = Participant.objects.filter(sponsor=s)
    return render(request, 'conversation/index.html', {'s':s, 'all_p':all_participants})
    #return HttpResponse("Hello, world. You're at the index.")


class UploadFileForm(forms.Form):
    file  = forms.FileField()

def handlefile(request, sponsor_id):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #return HttpResponse(request.FILES['file'].read())
        if form.is_valid():
            s = Sponsor.objects.get(pk=sponsor_id)
            p = Participant()
            #uploaded file must be mp4
            filename = str(s.id)+'_'+str(s.next_int_num)+'.mp4'
            p.sponsor = s
            p.internal_num = s.next_int_num
            p.filename = filename
            p.save()
            s.next_int_num += 1
            s.save()
            
            default_storage.save(filename, request.FILES['file'])
            return HttpResponseRedirect('/%s/' %sponsor_id)
        else:
            return HttpResponse("upload forminvalid")
    else:
        form = UploadFileForm()
        return HttpResponse("upload else")
    return HttpResponse("upload failed.")
