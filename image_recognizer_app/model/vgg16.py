#
# @vgg16.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


from .model import Model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16


class Vgg16(Model):
    """Model VGG16"""
    def __init__(self):
        pass

    # This function initialize the model
    def start(self):
        self.name = 'Vgg16'
        self.model = VGG16(weights='imagenet', include_top=True)

    # This function tries to predict the objects
    def predict(self, img_path):
        original = load_img(img_path, target_size=(224, 224))
        numpy_image = img_to_array(original)
        image_batch = numpy_image.reshape((1, numpy_image.shape[0], numpy_image.shape[1], numpy_image.shape[2]))
        processed_image = preprocess_input(image_batch)
        preds = self.model.predict(processed_image)
        pred_class = decode_predictions(preds)[0][0]
        return [(pred_class[1], round(float(pred_class[2]), 2))]
