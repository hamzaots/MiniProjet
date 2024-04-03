from django.db import models

# Create your models here.
class Result(models.Model):
    vulnerability = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    host_ip = models.CharField(max_length=15)
    host_name = models.CharField(max_length=100)
    time = models.DateTimeField()

class Scan(models.Model):
    ip_address = models.CharField(max_length=15)
    scan_type = models.CharField(max_length = 20)
