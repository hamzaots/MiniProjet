
from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("Hamza",views.Hamza , name = 'Hamza'),
    path("run_scan_view",views.run_scan_view , name='run_scan_view'),
    path("viewhtml",views.viewhtml, name='form'),
    path("your_view",views.your_view, name ="your_view"),
    path("run_scan", views.run_scan_view, name='run_scan'),
    path("check",views.check , name = "task_status"),

]