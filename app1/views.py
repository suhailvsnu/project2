from django.shortcuts import render

# Create your views here.
def html(request):
    return render(request,'sample.html')

def book1(request):
    return render(request,'sample2.html')

def data(request):
    return render(request,'sample3.html')
