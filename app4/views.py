from django.shortcuts import render
from app4.forms import inputform1

def home(request):
    if request.method == 'POST':
        form1 = inputform1(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            limit1 = data.get('limit1')
            result = factorial2(limit1)
            print(result)
            return render(request, 'app4/index.html', {'param1': result, 'form': form1})
        else:
           
            print('Form is invalid')
            return render(request, 'app4/index.html', {'form': form1})
    else:
        print('Show empty form')
        form1 = inputform1()
        return render(request, 'app4/index.html', {'form': form1})

def factorial1(n1):
    factorial = 1
    for i in range(1, n1 + 1, 1):
        factorial *= i
    return factorial

def factorial2(limit1):
    list1 = []
    list2 = []

    for i in range(2, limit1 + 1, 1):
        list1.append(factorial1(i))
        list2.append(i)
    final = zip(list1, list2)

    return final
