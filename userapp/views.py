from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass1"]
        confirm_password = request.POST["pass2"]
        if password != confirm_password:
            messages.warning(request, "Password not Matching")
            return render(request, "auth/signup.html")

        try:
            if User.objects.get(username=email):
                messages.warning(request, "Emaail already taken")
        except Exception as identifier:
            pass

        user = User.objects.create_user(email, email, password)
        user.save()
        messages.info(request, "Sign up Successfull ! Please login")
        return redirect("userapp:login")
    return render(request, "auth/signup.html")


def handlelogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        userpassword = request.POST["pass1"]
        user = authenticate(username=email, password=userpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect("mainapp:index")
        else:
            messages.error(request, "Someting went wrong ")
            return redirect("userapp:login")

    return render(request, "auth/login.html")


def handlelogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect("userapp:login")
