from django.shortcuts import render
from .models import Job, Practice

def homePage(request):
    return render(request, "home.html")

def allJobsPage(request):
    jobs = Job.objects.all().order_by('-postDate')
    return render(request, "all-jobs.html", {
        'jobs': jobs
    })

def allPracticePage(request):
    practices = Practice.objects.all().order_by('-postDate')
    return render(request, "all-practice.html", {
        'practices': practices
    })