import requests
import time
from camera import take_photo

url = 'https://kian-weimer-reimagined-couscous-pwgr5j75456fr66g-5000.preview.app.github.dev/upload'
url = 'http://192.168.0.147:8000/upload'

def send_image(image, filename="image.jpg"):
    start = time.time()   
    print("SENDING IMAGE")   
    files = {"media": (filename, image)}
    response = requests.post(url, files=files)
    print(f"DONE in {time.time() - start}s")

def test():
    image = take_photo()
    send_image(image)

if __name__ == "__main__":
    test()