#
# @prediction.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import os
import datetime
from .nasnet import NasNet
from .resnet import ResNet
from .result import Result
from .vgg16 import Vgg16
# from .yolo import Yolo
from ..exceptions.file_exception import FileException


class Prediction:
    """Performs object detection on all images in a directory"""

    def __init__(self, folder, word, percentage):
        self.models = {'nasnet': NasNet(), 'resnet': ResNet(), 'vgg16': Vgg16()}
        self.folder = folder
        self.word = word
        self.confidence = float(percentage)
        self.images = os.listdir(folder)

    # This function predicts the object according to the given percentage and word and return a list of objects
    def predict(self, model):
        model = self.models[model]
        model.start()
        list_obj = []
        for image in self.images:
            pre = model.predict('/'.join((self.folder, image)))

            for element in pre:
                if self.word.lower() in element[0].lower() and float(element[1] * 100) > self.confidence:
                    result = Result(image, model.name, round(element[1]*100, 2), self.__convert_time(image), element[0])
                    list_obj.append(result)
                    break

        return list_obj

    # This function converts the name of the file into a time format
    def __convert_time(self, name_img):
        index = name_img.find('.')
        try:
            name_img = int(name_img[:index])
        except ValueError as error:
            raise FileException(error, "The name of the files should be number only to be converted into time format.")

        return str(datetime.timedelta(seconds=name_img))
