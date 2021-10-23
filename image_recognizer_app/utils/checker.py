#
# @checker.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from django.core.files.storage import FileSystemStorage
from ..models import MlAssets
from .checksum import Checksum


class Checker:
    """ Determines if an uploaded file was stored previously by checking MD5 checksum"""

    @staticmethod
    def check(base_path, file, md5):
        # Calculate uploaded file MD5 checksum and compares it with received MD5
        calculated_md5 = Checksum.md5(file)
        if calculated_md5 != md5.lower():
            raise Exception("MD5 sent DO NOT correspond to uploaded file's MD5")

        filepath1 = "/media"
        output = {}
        # Chek if the sent zip-file already exists
        if MlAssets.objects.filter(checksum=md5):
            previous_file = MlAssets.objects.get(checksum=md5)
            output['path'] = str(base_path) + previous_file.path
            output['filename'] = previous_file.name
            return output
        # If not, then save file's information into the DB and store the file
        else:
            fs = FileSystemStorage()
            fs.save(file.name, file)
            asset = MlAssets(name=file.name, path=filepath1, checksum=md5)
            asset.save()
            output['path'] = str(base_path) + filepath1
            output['filename'] = file.name
            return output
