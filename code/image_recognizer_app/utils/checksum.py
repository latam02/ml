#
# @checksum.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
import hashlib


class Checksum:
    """"Calculate Checksum hash from a received file"""

    # Calculate MD5 checksum to a received file.
    @staticmethod
    def md5(file):
        size = 1024*1024  # 1MB
        checksum = hashlib.md5()
        # Check is file size is greater than 2.5 MB
        if file.multiple_chunks():
            for data in file.chunks(size):
                checksum.update(data)
        else:
            checksum.update(file.read())

        return checksum.hexdigest()
