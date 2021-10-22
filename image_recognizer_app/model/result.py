#
# @result.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

class Result:
    """ Stores the information of the object detection results"""

    def __init__(self, image, model, percentage, time, word):
        self.image = image
        self.model = model
        self.confidence = percentage
        self.time = time
        self.word = word

    # Return the object 'Result' as dictionary
    def as_dict(self):
        return {'image': self.image, 'model': self.model, 'confidence': str(self.confidence),
                'time': self.time, 'object': self.word}
