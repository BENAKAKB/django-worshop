from django.urls import path
from app5.views import doctor1,doctor2,doctor3,welcome
urlpatterns=[
    path('welcome/',welcome,name='welcome'),
    path('welcome/doctor1.html',doctor1,name='doctor1'),
    path('welcome/doctor2.html',doctor2,name='doctor2'),
    path('welcome/doctor3.html',doctor3,name='doctor3'),
    
]