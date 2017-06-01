from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import imutils
import time
import cv2

camera = PiCamera()
camera.resolution = (320,240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320,240))
stream = camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)

fps = FPS().start()

for (i, f) in enumerate(stream):
    frame = f.array
    frame = imutils.resize(frame, width=400)

    rawCapture.truncate(0)
    fps.update()

    if i == 100:
        break

fps.stop()
print("Elapsed time: {:.2f}".format(fps.elapsed()))
print("Approx. FPS: {:.2f}".format(fps.fps()))

stream.close()
rawCapture.close()
camera.close()

vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()
while fps._numFrames < 100:
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    fps.update()

fps.stop()
print("Elapsed time: {:.2f}".format(fps.elapsed()))
print("Approx. FPS: {:.2f}".format(fps.fps()))

vs.stop()

try:
    sys.stdout.close()
except:
    pass
try:
    sys.stderr.close()
except:
    pass
