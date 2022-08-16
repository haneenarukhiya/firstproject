from django.shortcuts import render

# Create your views here.

def homeview(request):
    return render(request,"homepage.html")
def second(request):
    return render(request,"second.html")
def extention (request):
     return render(request,"extention.html")
def secondpage(request):
    return render(request,"secondpage.html")
def second2(request):
    return render(request,"secondpage2.html")