import cv2
import time


def take_photo():
    cam = cv2.VideoCapture(0)
    ret, image = cam.read()
    cam.release()

    # convert image to format suitable for internet transfer
    image = cv2.imencode('.jpg', image)[1].tobytes()

    return image

def save_photo(filename, image):
    with open(filename, 'wb') as f:
        f.write(image)

def test():
    image = take_photo()
    save_photo("test_image.jpg", image)

if __name__ == "__main__":
    test()