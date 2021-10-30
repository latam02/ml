#
# @nasnet.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import shutil

from .model import Model
from keras.applications.nasnet import NASNetLarge
from keras.applications.nasnet import preprocess_input
from keras.applications.nasnet import decode_predictions
from keras.preprocessing import image
import numpy as np


class NasNet(Model):
    """Model NasNetLarge"""
    def __init__(self):
        pass

    # This function initialize the model
    def start(self):
        self.name = 'NasNet'
        self.model = NASNetLarge(weights='imagenet', include_top=True)

    # This function tries to predict the objects
    def predict(self, img_path):
        # Preprocessing
        original = image.load_img(img_path, target_size=(331, 331))
        numpy_image = image.img_to_array(original)
        image_batch = np.expand_dims(numpy_image, axis=0)
        processed_image = preprocess_input(image_batch)

        preds = self.model.predict(processed_image)
        # Select the first two predictions
        pred_class = decode_predictions(preds, top=2)[0][0]

        return [(pred_class[1], round(float(pred_class[2]), 2))]
