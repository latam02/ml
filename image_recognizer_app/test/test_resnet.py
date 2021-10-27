#
# @test_resnet.py Copyright (c) 2021 Jalasoft.
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
from ..model.resnet import ResNet


class TestResnet(TestCase):
    """ Unitary test for Resnet class"""
    # Positive case
    def test_resnet(self):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
        filepath = str(BASE_DIR) + '/workspace/ml_lc-jenkins@2/resources_test/ml_image_test/0843.jpg'
        d = ResNet()
        d.start()
        result = d.predict(filepath)
        expected = [('pug', float(0.71))]

        self.assertListEqual(expected, result)
