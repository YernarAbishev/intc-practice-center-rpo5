from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('jobs/all/', views.allJobsPage, name='allJobsPage'),
    path('practice/all/', views.allPracticePage, name='allPracticePage'),
]