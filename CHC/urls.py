from django.contrib import admin
from django.urls import path
from CHC.views import home
from CHC.views import HospitalDetailView


urlpatterns = [
    path('',home,name='homepage'),
    path('hospital/<int:pk>',HospitalDetailView.as_view()),
    ]
