from django.urls import path

from userapp.views import handlelogin, handlelogout, signup

app_name = "userapp"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", handlelogin, name="login"),
    path("logout/", handlelogout, name="logout"),
]
