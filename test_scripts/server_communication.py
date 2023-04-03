import requests
import time
from async_functions import run_async, run_thread
from camera import take_photo
from video import Camera

FRAME_RATE = 12

url = 'https://kian-weimer-reimagined-couscous-pwgr5j75456fr66g-8000.preview.app.github.dev/upload'
# url = 'http://192.168.0.147:8005/upload'

def send_image(image, filename="image.jpg"):
    start = time.time()   
    # print("SENDING IMAGE")   
    files = {"media": (filename, image)}
    response = requests.post(url, files=files)
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
