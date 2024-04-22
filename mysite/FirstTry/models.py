from django.db import models
from django.utils import timezone

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


class dateasyn(models.Model):

    ip_address = models.CharField(max_length=15)
    scan_type = models.CharField(max_length = 20)

    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    time_zone = models.CharField(max_length=32, default="UTC")

    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)

    DURATION_CHOICES = (
        ("entire", "Opération entière"),
    )
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES, default="entire")

    RECURRENCE_CHOICES = (
        ("monthly", "Mensuelle"),
        ("daily", "Quotidienne"),
        ("weekly", "Hebdomadaire"),
        ("yearly", "Annuelle"),
        ("none", "Une seule fois"),
    )
    recurrence = models.CharField(max_length=10, choices=RECURRENCE_CHOICES, default="monthly")

    def __str__(self):
        return self.name

