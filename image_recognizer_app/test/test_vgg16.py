#
# @test_vgg16.py Copyright (c) 2021 Jalasoft.
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
from ..model.vgg16 import Vgg16


class TestVgg16(TestCase):
    """Unitary Tests for Vgg16 class"""
    # Positive case
    def test_vgg16(self):
        BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent
        filepath = str(BASE_DIR) + '/workspace/ml_fc-jenkins@2/resources_test/ml_image_test/2.jpg'
        d = Vgg16()
        d.start()
        result = d.predict(filepath)
        expected = [('Egyptian_cat', float(0.72))]

        self.assertListEqual(expected, result)
