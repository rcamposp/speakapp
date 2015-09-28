from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render

def index(request):
    current_user = request.user
    
    if not (current_user.is_anonymous()):
        return redirect('/list')
    else:
        return render(request, 'speakapp/index.html')

def list(request):
    current_user = request.user
    if not (current_user.is_anonymous()):
        return render(request, 'speakapp/list.html') 
    else:
        return redirect('/')
    

def add(request):
    current_user = request.user
    return render(request, 'speakapp/add.html') 