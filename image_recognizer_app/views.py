#
# @views.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from django.db.models import base
from django.views import View
from django.http import JsonResponse
from pathlib import Path
from .model.prediction import Prediction
from .utils.checker import Checker
from .utils.unzip import Unzip
from django.http import HttpResponse
from .utils.imageRecognizer import ImageRecognizer
import json
from .exceptions.machine_learning_exception import MachineLearningException
from .exceptions.error_response import ErrorResponse


class Recognizer(View):
    """ Machine Learning Endpoint, call machine learning modules with
        received parameters and recognize objects from a zipped image folder"""

    def post(self, request):

        try:
            BASE_DIR = Path(__file__).resolve().parent.parent
            verified = Checker.check(BASE_DIR, request.FILES['file'], request.POST['md5'])
            images_path = Unzip.extract(verified['path'], verified['filename'])
            testing = ImageRecognizer.recognize(images_path, request)
            return JsonResponse(testing, safe=False)

        except MachineLearningException as error:
            error = ErrorResponse(error)
            return HttpResponse(json.dumps(error.get_dictionary_machine_learning()), 'application/json', status=error.get_status())

        except Exception as error:
            error = ErrorResponse(error)
            return HttpResponse(json.dumps(error.get_dictionary_general()), 'application/json', status=500)
