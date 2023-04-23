from Home import *
import threading
import subprocess
from getmac import get_mac_address as gma

MAC_ADDRESS = gma()
print(MAC_ADDRESS)
doc_ref = db.collection("Home").document(MAC_ADDRESS)
processes = {}

import requests
url = 'http://192.168.1.143:8000'
response = requests.post(url+'/register_device', data={"mac_address": MAC_ADDRESS})


# Define the callback function that will be triggered when the document changes
def on_snapshot(doc_snapshot, changes, read_time):
    house: House = House.get(MAC_ADDRESS)
    for doc in doc_snapshot:
        print(f'Received document snapshot: {doc.id}')
        events = doc.to_dict()["events"]
        for change in changes:
            if change.type.name == 'ADDED':
                print(f'New House: {change.document.id}')
            elif change.type.name == 'MODIFIED':
                if(events["laser_changed"] == True):
                    print(f'Modified House: {change.document.id} and Turned on the laser with mode {events["laser_state"]}')
                    house.events.laser_changed = False
                    house.events.laser_state = events["laser_state"]
                    house.create()
                    
                    if ("Laser" in processes.keys()):
                        if(events["laser_state"] == "OFF"):
                            #Kill process and procede
                            processes["Laser"].terminate()
                            subprocess.run(["python","kill_laser.py"])
                        else:
                            processes["Laser"].terminate() # Kill old process and
                            command = ['python', 'servo4.py', '-m', str(events["laser_state"])]
                            processes["Laser"] = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    else:
                        # Run the command asynchronously and capture the output
                        command = ['python', 'servo4.py', '-m', str(events["laser_state"])]
                        processes["Laser"]= subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        # Do other things while the command runs asynchronously
                        print("Running command in the background...")
                elif(events["dispense_changed"] == True):
                    house.events.dispense_changed = False
                    house.events.dispense_amount = events["dispense_amount"]
                    house.create()
                    print(f'Modified House: {change.document.id}, Dispensing: {events["dispense_amount"]} units of food')
                    command=['python', 'motor.py', '-t', str(events["dispense_amount"])]
                    processes["Motor"] = subprocess.run(command)
                    
                else:
                    print(f'Modified House: {change.document.id} somehow?')
            elif change.type.name == 'REMOVED':
                print(f'Removed House: {change.document.id}')

doc_watch = doc_ref.on_snapshot(on_snapshot)

if __name__ == "__main__":
    command = ['python', 'server_communication.py', '-u', url]
    processes["Video"]= subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Starting Video in the background")
    while(1):
        pass
