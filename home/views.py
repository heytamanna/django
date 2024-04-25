from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#THIS IS A FUNCTION
def home(request):
    
    peoples = [
        
        {'name':'Tamanna','age':21},
        {'name':'Rajat','age':26},
        {'name':'Ayansh','age':4},
        {'name':'Anju','age':45},
        {'name':'Ishita','age':11},
        {'name':'Kaka Ram','age':55}
    ]
    
    for people in peoples:
        if people['age']:
            print('YES')
    
    fruits = ['Mango🥭','Kiwi🥝','Apple🍎','Cherry🍒']
    
    return render(request,"index.html",context = {'peoples':peoples,'fruits' : fruits})

def about(request):
    context = {"page":'about'}
    return render(request,"about.html",context={'page': 'Django 2024 ' 'peoples'})


def contact(request):
   context = {"page":'contact'}
   return render(request,"contact.html",context)


def success_page(request):
    print("*" * 10)
    
    return HttpResponse("<h6>Hey this is a success page.</h6>")