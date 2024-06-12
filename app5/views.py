from django.shortcuts import render

def doctor1(request):
    return render(request,'app5/doctor1.html')
def doctor2(request):
    return render(request,'app5/doctor2.html')
def doctor3(request):
    return render(request,'app5/doctor3.html')
def welcome(request):
    return render(request,'app5/welcome.html')
