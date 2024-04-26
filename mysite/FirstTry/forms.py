from django.forms import ModelForm
from .models import Scan , dateasyn
from .models import Result


class ScanForm(ModelForm):
  class Meta:
    model = Scan
    fields = ('ip_address', 'scan_type',)
    
class ResultatForm(ModelForm):
  class Meta:
    model = Result
    fields = ('vulnerability', 'severity','host_ip','host_name','time',)

class dateasynForm(ModelForm) :
  class Meta:
    model = dateasyn  
    fields = ('ip_address','scan_type','start_time', 'end_time','duration','recurrence',)  
