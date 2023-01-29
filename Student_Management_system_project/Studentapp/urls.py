from django.urls import path

from Studentapp import views

urlpatterns=[
    path('',views.log_fun,name='log'),# it will display login.html page
    path('logdata',views.logdata_fun), # it will read data and verify user is superuser and redirect to home .html

    path('reg',views.reg_fun,name='reg'), # it will return to register.html page
    path('regdata',views.regdata_fun),#it will create superuseer account

    path('home',views.home_fun,name='home'),#it will redirect to home.html

    path('add_students',views.addstudent_fun,name='add'), # it will add student details
    path('readdata',views.readdata_fun),#itwill insert record into student table

    path('display',views.display_fun,name='display'),# it will display student table data in display.html file

    path('update/<int:id>',views.update_fun,name='up'), # it will update student data
    path('delete/<int:id>',views.delete_fun,name='del'),# it will delete record from student table

    path('logout',views.logout_fun,name='logoutt')
]