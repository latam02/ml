#
# @zip_exception.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from ..exceptions.machine_learning_exception import MachineLearningException


class ZipException(MachineLearningException):
    """This class exception inherits from 'MachineLearningException' and is used for more easy tracking errors."""
    def __init__(self, error, error_description):
        self.error_title = "Zip Exception"
        self.error_class = str(error.__class__)
        self.error_message = str(error)
        self.error_description = error_description
        self.error_code = 'LATAM-02: 4321'
        self.error_status = '500'
        super().__init__(
            self.error_title, self.error_class, self.error_message,
            self.error_description, self.error_code, self.error_status
            )
