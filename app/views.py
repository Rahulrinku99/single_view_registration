from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def Twa(request):
    tfo=TopicForm()
    wfo=WebpageForm()
    afo=AccessRecordForm()
    d={'tfo':tfo,'wfo':wfo,'afo':afo}
    if request.method=='POST':
        tfd=TopicForm(request.POST)
        wfd=WebpageForm(request.POST)
        afd=AccessRecordForm(request.POST)
        if tfd.is_valid() and wfd.is_valid() and afd.is_valid():
            STFD=tfd.save()

            NSWO=wfd.save(commit=False)
            NSWO.topic_name=STFD
            NSWO.save()

            NSAO=afd.save(commit=False)
            NSAO.name=NSWO
            NSAO.save()

            return HttpResponse('data saved successfully')
        else:
            return HttpResponse('not valid')
        
    return render(request,'Twa.html',d)