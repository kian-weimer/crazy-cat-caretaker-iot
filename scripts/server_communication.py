import requests
import time
from async_functions import run_async, run_thread
# from camera import take_photo
from video import Camera
from getmac import get_mac_address as gma
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description='Running Video Code')

# Add arguments
parser.add_argument('-u', '--url', type=str, required=False,default ='http://192.168.1.143:8000',help='urlto communicate to ')

# Parse the arguments
args = parser.parse_args()

# Access the values of the arguments

url = args.url+'/upload'
print(url)
FRAME_RATE = 24

#url = 'https://kian-weimer-reimagined-couscous-pwgr5j75456fr66g-8000.preview.app.github.dev/upload' # deploy url
# url = 'http://192.168.0.33:8001/upload'  #kians house
#url = 'http://192.168.1.143:8000/upload'

def send_image(image, filename="image.jpg"):
    start = time.time()   
    # print("SENDING IMAGE")   
    files = {"media": (filename, image)}
    response = requests.post(url, files=files, data={"mac_address": gma()})
    # response = requests.post(url, files=files)
    print(response)
    # print(f"DONE in {time.time() - start}s response: {response}")

def send_photo():
    image = take_photo()
    send_image(image)

def test():
    camera = Camera()
    print("Camera initialized.")

    for image in Camera.frames():
        start = time.time()
        run_thread(send_image, image)
        delay = 1/FRAME_RATE - (time.time()-start)
        print(f"time to loop: {time.time() - start}s Sleeping for {delay}s")
        time.sleep(max(delay, 0))

if __name__ == "__main__":
    test()
