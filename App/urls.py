from django.conf.urls import url

from App import views

urlpatterns = [

    url(r'^addstudent/', views.add_student),
    url(r'^getstudents/', views.get_students),

]