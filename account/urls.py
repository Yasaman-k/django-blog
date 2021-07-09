from  django.urls import  path
from .views import  signupView,loginView,logoutView

app_name='account'

urlpatterns=[
    path('signup/',signupView,name='signup'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout')

]