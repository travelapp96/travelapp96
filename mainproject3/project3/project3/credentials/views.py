from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        email_id = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():  # for checking the username
                messages.info(request, "username Taken")
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request, "email_id Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,
                                                first_name=f_name, last_name=l_name, email=email_id)
                user.save();
                print("user registered")
        else:
            messages.info(request, 'password not matched')
            return redirect('register')
        return redirect('login')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")

            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')




