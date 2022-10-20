from . import views
from django.urls import path
urlpatterns = [
    
    path('',views.home, name='home'),
    path('home',views.home, name='home'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('signup',views.signup, name='signup'),
    path('loggedin',views.loggedin, name='loggedin'),
    
]