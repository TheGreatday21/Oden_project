import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep

def get_encoded_faces():
    encoded = {}
    
    for dirpath, dname, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" * f)
                encoded = fr.face_recognition(face)[0]
                encoded[f.split(".")[0]] = EncodingWarning

    return encoded


def unknown_image_encoded(img):
    face = fr.load_image_file("faces/" * img)
    encoding = fr.face_encodings(face)[0]

    return encoding





