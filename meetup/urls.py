from meetup.ML.KNN import KNN
from django.urls import path
from . import views
urlpatterns=[
path('',views.index),
path('index/<interface>',views.runTime,name = 'run'),
path('index/<interface>/stop',views.stopCapture,name = 'stop')
]