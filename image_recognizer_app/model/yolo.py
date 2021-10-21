#
# @yolo.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import cv2
from PIL import Image
import numpy as np
from .model import Model
from pathlib import Path
from ..exceptions.yolo_exception import YoloException


class Yolo(Model):
    """This class belong to the Yolo model and all the necessary functions to work"""
    def __init__(self):
        pass

    # This function initialize the model
    def start(self):
        self.name = 'Yolo'

        # Constants
        self.wH = 320
        self.confThreshold = 0.1
        self.nmsThreshold = 0.3

        self.classNames = [
            'person', 'bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
            'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
            'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
            'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
            'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
            'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'sofa',
            'pottedplant', 'bed', 'diningtable', 'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard',
            'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
            'teddy bear', 'hair drier', 'toothbrush']

        BASE_DIR = Path(__file__).resolve().parent
        modelConfiguration = str(BASE_DIR) + "\\yolov3.cfg"
        modelWeigths = str(BASE_DIR) + "\\yolov3.weights"

        try:
            self.net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeigths)
        except cv2.error as error:
            raise YoloException(error, "Please check the weight and cfg files for Yolo.")
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    # This function tries to predict the objects
    def predict(self, img_path):
        image = Image.open(img_path)
        img = np.array(image)

        blob = cv2.dnn.blobFromImage(img, 1 / 255, (self.wH, self.wH), [0, 0, 0], 1, crop=False)
        self.net.setInput(blob)

        layerNames = self.net.getLayerNames()
        outputNames = [layerNames[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        outputs = self.net.forward(outputNames)

        return self.__findObjects(outputs, img)

    # This function finds the objects and try to reduce the duplicate objects
    def __findObjects(self, outputs, img):
        hT, wT, cT = img.shape
        bbox = []
        classIds = []
        confs = []
        for output in outputs:
            for det in output:
                scores = det[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > self.confThreshold:
                    w, h = int(det[2] * wT), int(det[3] * hT)
                    x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                    bbox.append([x, y, w, h])
                    classIds.append(classId)
                    confs.append(float(confidence))

        indices = cv2.dnn.NMSBoxes(bbox, confs, self.confThreshold, self.nmsThreshold)
        predictions_list = []

        for i in indices:
            i = i[0]
            predictions_list.append((self.classNames[classIds[i]].capitalize(), confs[i]))

        return predictions_list
