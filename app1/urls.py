from django.urls import path
from app1.views import squarenum,factorial
urlpatterns = [path('', squarenum),
               path('factorial',factorial)]