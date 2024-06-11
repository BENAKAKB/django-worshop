

from django.shortcuts import render, redirect
from .forms import CustomerForm

def customer_create_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('customer-success', customer_id=customer.customer_id)
    else:
        form = CustomerForm()
    
    return render(request, 'app3/index.html', {'form': form})

def success_view(request, customer_id):
    return render(request, 'app3/index.html', {'customer_id': customer_id})
