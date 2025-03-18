from django.contrib import admin
from django.urls import path

from configapp.views import login_view, admin_panel, staff_panel, add_teachers, add_students, index

urlpatterns = [
    path('',login_view),
    path('admin_panel/', admin_panel,name='admin_panel'),
    path('staff_panel/', staff_panel,name='staff_panel'),
    path('add_teachers', add_teachers, name='add_teachers'),
    path('add_students', add_students, name='add_students'),
    path('index/', index,name='home'),

]
