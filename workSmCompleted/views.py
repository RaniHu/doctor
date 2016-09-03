from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def completed(request):
     return render(request,'workSmCompleted/completed.html')