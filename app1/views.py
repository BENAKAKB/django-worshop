from django.shortcuts import render

# Create your views here.
def squarenum(request):
    n1=5
    square=n1*n1
    return render(request,'app1/index.html',{'parum1': square})
def factorial(request):
   
    factorial_results = {}

   
    for i in range(1, 8):
        fact = 1
        num = i
       
        while i > 0:
            fact *= i
            i -= 1
       
        factorial_results[num] = fact

   
    return render(request, 'app1/index.html', {'factorial_results': factorial_results,'num':num})