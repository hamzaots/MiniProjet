# from celery import shared_task , Task
# from django.shortcuts import render , redirect
# from django.http import HttpResponse
# import subprocess
# import xml.etree.ElementTree as ET
# from django.contrib import messages
# import subprocess
# import datetime 
# import time
# from datetime import timedelta


# @shared_task         
# def scheduled_periodic_scan(target, scan_datetime):
#     current_datetime = datetime.datetime.now(datetime.timezone.utc)
    

#     if scan_datetime > current_datetime:
#         time_diff = (scan_datetime - current_datetime).total_seconds()
#         print("Waiting for initial scheduled scan at:", scan_datetime.strftime("%Y-%m-%d %H:%M:%S"))
#         print("Time left:", datetime.timedelta(seconds=time_diff))
#         print("current:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
#         scan_command = ["nmap", "-oX", "output2.xml", target]
#         subprocess.run(scan_command)
#         # Wait until the initial scan time arrives
#         time.sleep(time_diff)
#         print("Initial scheduled scan started at:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#         subprocess.run(scan_command)
#     else:
#         print("Waiting for initial scheduled scan at:", scan_datetime.strftime("%Y-%m-%d %H:%M:%S"))
#         print("current:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
#         print("Scheduled time has already passed.")

# # @shared_task          
# # def scheduled_scan(target):
# #     scan_command = ["nmap", "-oX", "output2.xml", target]
# #     subprocess.run(scan_command)

# # def dynamic_schedule(request):
# #     data = dateasynForm(request.POST)
# #     if data.is_valid():
        
# #             d=0

# #             duration = data['duration']
# #             if duration == "daily":
# #                 d = 1
# #             elif duration == "weekly":
# #                 d = 7
# #             elif duration == "yearly":
# #                 d = 365
# #             elif duration == "monthly":
# #                 d = 30
# #             return timedelta(days=d)
# #     return timedelta(days=1)

