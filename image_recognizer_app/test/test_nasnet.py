#
# @test_nasnet.py Copyright (c) 2021 Jalasoft.
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
from ..model.nasnet import NasNet


class TestNasnet(TestCase):
    """" Unitary Test for Nasnet class"""
    # Positive case
    def test_nas_net(self):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
        filepath = str(BASE_DIR) + 'workspace/ml_fc-jenkins@2/resources_test/ml_image_test/positive/001.jpg'
        d = NasNet()
        d.start()
        result = d.predict(filepath)
        expected = [('Eskimo_dog', float(0.57))]

        self.assertListEqual(expected, result)
