from .import views
from django.urls import path,include


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('trainers/',views.trainers,name='trainers'),
    path('admission/',views.admission,name='admission'),
    path('payment/',views.payment,name='payment'),
    path('otp/', views.otp, name='otp'),
    path('otp/confirmation.html',views.confirmation,name='confirmation'),
    
              ] 