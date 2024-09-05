from django.shortcuts import render
from .models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def users(request):
    new_user = User()
    new_user.name = request.POST.get('name')
    new_user.phone = request.POST.get('phone')
    new_user.save()
    users = {
        'users': User.objects.all()
    }
    return render(request, 'users.html', users)
