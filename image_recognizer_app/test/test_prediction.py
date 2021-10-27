#
# @test_prediction.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from unittest import TestCase
from pathlib import Path
from ..exceptions.file_exception import FileException
from ..model.prediction import Prediction


class TestPrediction(TestCase):
    """Unitary tests for Prediction class"""
    # Test positive case
    def test_prediction(self):
        BASE_DIR1 = Path(__file__).resolve().parent.parent.parent
        filepath = str(BASE_DIR1) + '/workspace/ml_fc-jenkins@2/resources_test/ml_image_test/positive'
        d = Prediction(filepath, 'pug', '50')
        result = d.predict('nasnet')
        expected = 1

        self.assertEqual(expected, len(result))
    # Test negative case when image name is not a number
    def test_prediction_ErrorName(self):
        with self.assertRaises(FileException):

            BASE_DIR2 = Path(__file__).resolve().parent.parent.parent
            filepath = str(BASE_DIR2) + '/resources_test/ml_image_test/negative/'
            d = Prediction(filepath, 'pug', '50')
            d.predict('vgg16')
    # Test positive case when no word is passed to Prediction
    def test_prediction_NoWord(self):
        BASE_DIR1 = Path(__file__).resolve().parent.parent.parent
        filepath = str(BASE_DIR1) + '/resources_test/ml_image_test/positive'
        d = Prediction(filepath, '', '50')
        result = d.predict('nasnet')
        expected = 2

        self.assertEqual(expected, len(result))


