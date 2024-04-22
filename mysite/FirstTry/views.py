from django.shortcuts import render , redirect
from django.http import HttpResponse
import subprocess
from django import forms
from .forms import ScanForm ,dateasynForm# Assurez-vous d'importer les formulaires
import xml.etree.ElementTree as ET
from django.contrib import messages
# Create your views here.
import subprocess
import datetime 
import time
from asgiref.sync import sync_to_async
from celery import shared_task
import asyncio


class new(forms.Form):
    task= forms.CharField(label="new task")
    ana= forms.DecimalField(label="num")
    pr=forms.IntegerField(label="Pr",min_value=1,max_value=10)



def index(request):
    return HttpResponse("Hello world!")

def Hamza(request):
    return HttpResponse("hallllllll")

def run_scan_view(request) :
    command = "nmap -oX output2.xml 192.168.56.101 "
    try:
        subprocess.run(command, shell=True, check=True)
        return HttpResponse("La commande s'est exécutée avec succès.")
    except subprocess.CalledProcessError as e:
        return HttpResponse("Erreur lors de l'exécution de la commande:", e)

def viewhtml (request) :
    return render(request,"hello/NewSchedule.html")


def form(request):
    if request.method == 'POST':
        scan_form = ScanForm(request.POST)
        
        if scan_form.is_valid():
            # Sauvegarder les données du formulaire
            scan = scan_form.save(commit=False)

    else:
        scan_form = ScanForm()
   
    return render(request, "hello/index.html", {'scan_form': scan_form})
    

@shared_task
def your_view(request):
    
    data = dateasynForm(request.POST)
    if data.is_valid():
        
            d=0

            duration = data['duration']
            if duration == "daily":
                d = 1
            elif duration == "weekly":
                d = 7
            elif duration == "yearly":
                d = 365
            elif duration == "monthly":
                d = 30

    #run_scan_view(request)
            scan_datetime=datetime.datetime.now()
            scan_datetime = data.cleaned_data['start_time']
    
    
            

    # Chemin vers le fichier XML généré par Nmap
            xml_file_path = 'output2.xml'

#             Scan_Form = ScanForm(request.POST)


            if data["scan_type"].value() == "tcp_ping":
                scheduled_periodic_scan(data['ip_address'].value(), scan_datetime , d)
        # Exécutez le scan Nmap et extrayez les informations du fichier XML
                ports_info = parse_nmap_xml(request,xml_file_path)
        # Passez les informations extraites au template
                return render(request, 'hello/ind.html', {'ports_info': ports_info})
            else :
                return HttpResponse("Hello world!")



def parse_nmap_xml(request,xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        ports = []
        for port in root.findall('.//port'):
            port_number = port.get('portid')
            state = port.find('.//state').get('state')
            service_element = port.find('.//service')

            if service_element is not None:
               service = service_element.get('name')
            else:
                service = "N/A"
            ports.append({'port': port_number,
                         'state': state,
                          'service': service,
                          })

        
        messages.success(request, 'Your message here')

        return ports
    
    except Exception as e:

        messages.error(request,"Une erreur s'est produite lors de l'analyse du fichier XML : {e}")
        return []
    
#faire un scan périodique
    
@shared_task
def scheduled_periodic_scan(target, scan_datetime, period_days):
    current_datetime = datetime.datetime.now(datetime.timezone.utc)
    

    if scan_datetime > current_datetime:
        time_diff = (scan_datetime - current_datetime).total_seconds()
        print("Waiting for initial scheduled scan at:", scan_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        print("Time left:", datetime.timedelta(seconds=time_diff))
        print("current:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        # Wait until the initial scan time arrives
        time.sleep(time_diff)
        print("Initial scheduled scan started at:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        while True:
            # Run the scan command
            scan_command = ["nmap", "-oX", "output2.xml", target]
            # subprocess.run(scan_command)
            print("Scan completed at:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            # Calculate next scan datetime
            scan_datetime += datetime.timedelta(days=period_days)
            # Calculate time difference until next scan
            time_diff = (scan_datetime - datetime.datetime.now(datetime.timezone.utc)).total_seconds()
            if time_diff > 0:
                print("Next scheduled scan at:", scan_datetime.strftime("%Y-%m-%d %H:%M:%S"))
                print("Time left until next scan:", datetime.timedelta(seconds=time_diff))
                # Wait until the next scan time arrives
                asyncio.sleep(time_diff)
            else:
                print("Error: Next scheduled scan time has already passed.")
                break
    else:
        print("Waiting for initial scheduled scan at:", scan_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        print("current:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        print("Scheduled time has already passed.")


