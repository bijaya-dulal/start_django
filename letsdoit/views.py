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

def library(request):
      title = 'library'
      context = {'title':title}
      return render(request, 'library.html',context)
def Course(request):
    return HttpResponse("<h4>Following Course are available</h4>")

def courseId(request, cid):
    return HttpResponse(cid)
def login(request):
    title = 'login'
    context = {'title':title}
    return render(request,'login.html',context)

def contact(request):
    try:
        name = request.GET['name']
        address = request.GET['address']
        email = request.GET['email']
        phone= request.GET['phone']
    except:
        pass
    title = 'contact'
    context = {'title':title}
    return render(request,'contact.html',context)