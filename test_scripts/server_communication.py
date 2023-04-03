import requests
import time
from async_functions import run_async
from camera import take_photo
from video import Camera

FRAME_RATE = 5

# url = 'https://kian-weimer-reimagined-couscous-pwgr5j75456fr66g-8000.preview.app.github.dev/upload'
url = 'http://192.168.0.147:8005/upload'

def send_image(image, filename="image.jpg"):
    start = time.time()   
    # print("SENDING IMAGE")   
    files = {"media": (filename, image)}
    response = requests.post(url, files=files)
    # print(f"DONE in {time.time() - start}s response: {response}")

def send_photo():
    image = take_photo()
    send_image(image)

def test():
    camera = Camera()
    print("Camera initialized.")
    for image in Camera.frames():
        start = time.time()
        # image = take_photo()
        run_async(send_image, image)
        delay = 1/FRAME_RATE - (time.time()-start)
        print(f"time to loop: {time.time() - start}s Sleeping for {delay}s")
        # image = take_photo()
        time.sleep(max(delay, 0))
        # send_image(image)

if __name__ == "__main__":
    test()
