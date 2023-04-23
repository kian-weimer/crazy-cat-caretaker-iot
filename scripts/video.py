import os
import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 0
    cam = None # cv2.VideoCapture(-1)
    old_image = None
    def __init__(self):
        print("init complete")
        Camera.cam = cv2.VideoCapture(-1)
        if os.environ.get('OPENCV_CAMERA_SOURCE'):
            Camera.set_video_source(int(os.environ['OPENCV_CAMERA_SOURCE']))
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        print(Camera.video_source)
        camera = Camera.cam # cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            # img.resize(img, (64, 64))
            # img = cv2.resize(img, (0,0), fx = 0.15, fy = 0.15)
            # encode as a jpeg image and return it
            try:
                image = cv2.imencode('.jpg', img)[1].tobytes()
                Camera.old_image = image
                yield image
            except:
                yield Camera.old_image


