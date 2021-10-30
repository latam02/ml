#
# @models.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from django.db import models


class MlAssets(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    checksum = models.CharField(max_length=100)

    class Meta:
        managed = True

    def __str__(self):
        return '{} File: {}, stored in {} with MD5: {}'.format(self.id, self.name, self.path, self.checksum)
