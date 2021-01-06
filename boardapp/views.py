from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupfunc(request):
    object = User.objects.get(username='tak')
    print(object.email)
    if request.method == "POST":
        print('post')
    else:
        print(request.method)

    return render(request, 'signup.html',{})
