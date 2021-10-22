#
# @imageRecognizer.py Copyright (c) 2021 Jalasoft.
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
import shutil

from ..model.prediction import Prediction


class ImageRecognizer:
    """Calls a machine learning model to recognize objects in an image"""

    @staticmethod
    def recognize(path, request):
        #ImageRecognizer.validate(path)
        result = Prediction(path, request.POST['word'], request.POST['percentage']
                            ).predict(request.POST['model'])
        testing = [pred.as_dict() for pred in result]
        shutil.rmtree(path)
        return testing

    # check if folder path is valid
    @staticmethod
    def validate(path):
        if not os.path.isdir(path):
            raise Exception("Invalid folder path")
