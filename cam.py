#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import picamera
import time
import sys

FILEPATH = '/data/'
MOVIE_INTERVAL = 600

def main(now):
    filename = FILEPATH + now + ".h264"
    with picamera.PiCamera() as camera:

        camera.resolution = (1024,768)
        camera.brightness = 70
        camera.start_recording(filename)
        time.sleep(MOVIE_INTERVAL)
        camera.stop_recording()

if __name__ == '__main__':
    if len(sys.argv[1:]) != 1:
        print("Invalid argument.")
        sys.exit(1)
    main(sys.argv[1])