f"""
URL configuration for letsdoit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from letsdoit import views

urlpatterns = [
    path('admin/',admin.site.urls),
    #there is empty because home page should display at 8000(any port) direclty
    
    path('',views.homePage,name= "home"),
    path('library/',views.library, name= "library"),
    path('login/',views.login, name= "login"),
    path('contact/',views.contact, name= "contact"),
    path('thankyou/',views.thankyou, name= "submit_contact"),
    path('calculator/',views.calculator, name= "calculator"),
    # dynamic routes/urls
    # urls type : int, str and slug ->like(bijay-dulal-sudal)
    #path('course/<int:cid>',views.courseId),
    #path('course/<str:cid>',views.courseId),
    #path('course/<slug:cid>',views.courseId),
    #this is for all typed dynamic
]
