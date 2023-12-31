from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render 
from .forms import usersForm

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

def login(request):
  
    title = 'login'
    context = {'title':title}
    return render(request,'login.html',context)

def contact(request):
    fm = usersForm();
    try:
        if(request.method =="POST"):
            name = request.POST['name']
            address = request.POST['address']
            email = request.POST['email']
            phone= request.POST.get('phone')#this is using get() method call
            url = "/login/?name={}& address={}".format(name,address)
            return HttpResponseRedirect(url)
            #return redirect(url) # for this import redirect from django.shortcut
    except:
        pass
    title = 'contact'

    

    context = {'title':title,
               'form':fm,
               }
    return render(request,'contact.html',context)

def thankyou(request):
    try:
        if(request.method =="POST"):
            name = request.POST['name']
            address = request.POST['address']
            email = request.POST['email']
            phone= request.POST.get('phone')#this is using get() method call
            context={'name':name, 
                     'address':address,
                     'title':"thankyou",
                     'email':email,
                     'phone':phone,
                     }
            return render(request,'thankyou.html',context)
           
    except:
        pass

def calculator(request):
    c = ''
    try:
        if(request.method == "POST"):
            c = 'in'
            num1 = eval(request.POST['num1'])
            num2 = eval(request.POST['num2'])
            opr = request.POST['opr']
            if(opr == "+"):
                 c = num1+num2
            elif(opr == "-"):
                 c = num1-num2
            elif(opr == "*"):
                 c = num1*num2  
            elif(opr == "/"):
                 c = num1/num2   
                 
    except:
        c = "invalid expression"
    print(c)    
    data = {'result':c}
    return render(request,'calculator.html',data)