from django.conf.urls import url

from register.registercontroller import registercontroller
from login.logincontroller import logincontroller

from adduser.addusercontroller import addusercontroller

urlpatterns = [

    url('^api/register/$', registercontroller.registerUser),
    url('^api/login/$', logincontroller.login),
    url('^api/user/$', addusercontroller.userData),
    url('^api/listuser/$', logincontroller.getUserDetails),

]