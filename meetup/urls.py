from meetup.ML.BGTs import BGTs
from django.urls import path
from . import views
urlpatterns=[
path('',views.index),
path('getData',views.getData,name='getData'),
path('<interface>',views.runTime,name = 'run'),
path('<interface>/stop',views.stopCapture,name = 'stop')
]