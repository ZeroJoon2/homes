from django.shortcuts import render, redirect
from users.models import tbUsers
# Create your views here.

def demand_view(request):
    user_email = request.session.get('user_email')
    if user_email:
        user = tbUsers.objects.get(email = user_email)
        print('hello~')
        return render(request, 'demand_view.html', {'user':user})
    else:
        print('?')        
        return render(request,'login.html')