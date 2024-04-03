from django.forms import ModelForm
from . import models
from .models import Scan
from .models import Result
from django import forms


class ScanForm(ModelForm):
  class Meta:
    model = Scan
    fields = ('ip_address', 'scan_type',)
    
class ResultatForm(ModelForm):
  class Meta:
    model = Result
    fields = ('vulnerability', 'severity','host_ip','host_name','time',)