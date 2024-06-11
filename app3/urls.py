
from django.urls import path
from .views import customer_create_view, success_view

urlpatterns = [
    path('customer/', customer_create_view, name='customer-create'),
    path('success/<int:customer_id>/', success_view, name='customer-success'),
]
