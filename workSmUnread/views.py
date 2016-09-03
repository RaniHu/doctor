from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def unread(request):
     return render(request,'workSmUnread/unread.html')