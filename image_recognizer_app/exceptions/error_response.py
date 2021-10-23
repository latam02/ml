#
# @error_response.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from typing import Dict


class ErrorResponse():
    """This class returns a dictionary depending on the type of error."""
    def __init__(self, error):
        self.error = error

    # Return a dictionary for Machine Learning exceptions
    def get_dictionary_machine_learning(self) -> Dict:
        dictionary = {}
        dictionary['error_title'] = self.error.error_title
        dictionary['error_class'] = self.error.error_class
        dictionary['error_message'] = self.error.error_message
        dictionary['error_description'] = self.error.error_description
        dictionary['error_code'] = self.error.error_code
        dictionary['error_status'] = self.error.error_status

        return dictionary

    # Return a dictionary for general exceptions
    def get_dictionary_general(self) -> Dict:
        dictionary = {}
        dictionary['error_title'] = 'Unexpected error'
        dictionary['error_class'] = str(self.error.__class__)
        dictionary['error_context'] = str(self.error.__context__)
        dictionary['error_message'] = str(self.error)

        return dictionary

    # Return the status of error
    def get_status(self) -> str:
        return self.error.error_status
