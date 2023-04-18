from django.shortcuts import render

from app.models import *
from django.http import HttpResponse

def Insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic Inserted Successfully')
    return render (request,'Insert_topic.html')

def Insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,mail=em)[0]
        WO.save()

        return HttpResponse('Webpage Inserted Successfully')
    return render (request,'Insert_webpage.html',context=d)

def insert_access(request):
    LWO=Webpage.objects.all()
    d={'webpage':LWO}

    if request.method=='POST':
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        WO=Webpage.objects.get_or_create(name=na)[0]
        WO.save()
        AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()

        return HttpResponse('Access records inserted successfully ')
    return render(request,'insert_access.html',d)

def retrieve(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}

    if request.method=='POST':
        tn=request.POST.getlist('tn')
        print(tn)

        webquery=Webpage.objects.none()

        for i in tn:
            webquery = webquery | Webpage.objects.filter(topic_name=i)

        d1={'webpage':webquery}

        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve.html',d)


def checkbox(request):
    LTO=Topic.objects.all()
    d={'webpage':LTO}
    return render(request ,'checkbox.html',d)

def radio(request):
    LTO=Topic.objects.all()
    d={'topic': LTO}
    return render(request,'radio.html',d)

def retrieve_access(request):
    LWO=Webpage.objects.all()
    d={'webpage':LWO}

    if request.method=='POST':
        na=request.POST.getlist('na')
        print(na)
        accessquery=AccessRecord.objects.none()

        for i in na:
            accessquery = accessquery | AccessRecord.objects.filter(name=i)
            

        d1={'access':accessquery}

        return render(request,'display_access.html',d1)
    return render(request,'retrieve_access.html',d)
    

def update_webpage(request):
    LWO=Webpage.objects.all()
    d={'webpage':LWO}
    if request.method=="POST":
        #tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        #TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get(name=na)

        Webpage.objects.filter(name=WO).update(url=ur,mail=em)
        LOW=Webpage.objects.all()
        d1={'webpage':LOW}
        return render(request,'display_webpage.html',d1)
    return render(request,'update_webpage.html',d)