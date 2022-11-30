from django.urls import path
from .views import (UserRegistrationView, UserLoginView)


app_name = 'authapi'
'''
    I do not think so that i need here name section, because it is an API not and full stack project.
'''
urlpatterns = [
    path("registration/", UserRegistrationView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
]
