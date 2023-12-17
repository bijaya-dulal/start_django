from django.http import HttpResponse
from django.shortcuts import render 

# def homePage(request):
#     return render(request,"index.html")


def homePage(request):
    data = {
        'title':'home Page',
        'bdata':'bijaya dulal',
        'clists':['php','java','django'],
        'numbers':[10,20,30,40,50],
        'student_details':[{'name':'bijaya','phone':98446349199},
                          {'name':'bijaya','phone':98446349199},
                          ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("<h3>Welcome to letsdoit</h3>")

def Course(request):
    return HttpResponse("<h4>Following Course are available</h4>")

def courseId(request, cid):
    return HttpResponse(cid)