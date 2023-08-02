from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {'page' : 'home'}



    peopels =[
        {"name":"John","age":25,"gender" : "Male"},
        {"name":"Jane","age":30,  "gender" :"Female"},
        {"name":"Jane","age":30,  "gender" :"Female"},
        {"name":"Jane","age":30,  "gender" :"Female"},
        {"name":"Jane","age":30,  "gender" :"Female"},
    ]
    veg = ["pi","to","pt"]
    return render (request ,"index.html",context={'page' :'home index', 'peopels':peopels ,'veg':veg})

   

def about(request):
    context = {'page' : 'About'}
    return render(request ,"about.html",context)

def contact(request):
    context = {'page' : 'Contact'}

    return render(request,"contact.html",context)