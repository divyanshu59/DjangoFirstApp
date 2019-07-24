from django.urls import path
from home.views import home
from login.views import login,signup

urlpatterns = [
    path('', home),
    path('login/', login),
    path('signup/', signup),
]