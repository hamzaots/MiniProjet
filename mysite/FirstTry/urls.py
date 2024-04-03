
from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("Hamza",views.Hamza , name = 'Hamza'),
    path("run_scan_view",views.run_scan_view , name='run_scan_view'),
    path("viewhtml",views.form , name='form'),
    path("results",views.your_view, name ="results"),
    path("run_scan", views.run_scan_view, name='run_scan')
]