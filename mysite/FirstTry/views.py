from django.shortcuts import render , redirect
from django.http import HttpResponse
import subprocess
from .forms import ScanForm # Assurez-vous d'importer les formulaires
import xml.etree.ElementTree as ET
from django.contrib import messages
# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

def Hamza(request):
    return HttpResponse("hallllllll")

def run_scan_view(request) :
    command = "nmap -oX output.xml 192.168.56.101 "
    try:
        subprocess.run(command, shell=True, check=True)
        return HttpResponse("La commande s'est exécutée avec succès.")
    except subprocess.CalledProcessError as e:
        return HttpResponse("Erreur lors de l'exécution de la commande:", e)

def viewhtml (request) :
    return render(request,"hello/index.html")


def form(request):
    if request.method == 'POST':
        scan_form = ScanForm(request.POST)
        
        if scan_form.is_valid():
            # Sauvegarder les données du formulaire
            scan = scan_form.save(commit=False)

    else:
        scan_form = ScanForm()
   
    return render(request, "hello/index.html", {'scan_form': scan_form})
    


def your_view(request):
    
    run_scan_view(request)
    # Chemin vers le fichier XML généré par Nmap
    xml_file_path = 'output.xml'
    ScanForm = ScanForm(request.POST)
    if ScanForm.scan_type == "tcp_ping":
        # Exécutez le scan Nmap et extrayez les informations du fichier XML
        ports_info = parse_nmap_xml(request,xml_file_path)
        # Passez les informations extraites au template
        return render(request, 'hello/ind.html', {'ports_info': ports_info})


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
