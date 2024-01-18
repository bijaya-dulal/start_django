from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

import re

# def homePage(request):
#     return render(request,"index.html")

@login_required(login_url='login')
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
@login_required(login_url='login')
def library(request):
      title = 'library'
      context = {'title':title}
      return render(request, 'library.html',context)

def login_user(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        if request.method == 'POST':
            # Get the username and password from the POST request
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Use Django's authenticate function to check the credentials
            user = authenticate(request, username=username, password=password)

            # If the user is authenticated, log them in
            if user is not None:
                login(request,user)
                # Redirect to a success page or homepage
                return render(request,'index.html')
            else:
                # If authentication fails, you can handle it accordingly
                return render(request, 'login.html', {'error': 'Invalid credentials'})

    # If it's a GET request, render the login form
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request,'login.html')

@login_required(login_url='login')
def contact(request):
   # fm = usersForm();
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
              # 'form':fm,
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