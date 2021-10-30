#
# @machine_learning_exception.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#


class MachineLearningException(Exception):
    """This is the main class from the exceptions, all the other exceptions will inherit from this class."""
    def __init__(self, error_title, error_class, error_message, error_description, error_code, error_status):
        self.error_title = error_title
        self.error_class = error_class
        self.error_message = error_message
        self.error_description = error_description
        self.error_code = error_code
        self.error_status = error_status
        super().__init__(self.error_message)
