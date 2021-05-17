from django.shortcuts import render

# Create your views here.

def coworker(request):
    return render(request,'coworker.html')

def workspace(request):
    return render(request,'workspace.html')
    
def meetingrooms(request):
    return render(request,'meetingrooms.html')
    
def globalpass(request):
    return render(request,'globalpass.html')