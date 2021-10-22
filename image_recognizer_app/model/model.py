#
# @model.py Copyright (c) 2021 Jalasoft.
# Cl 26 Sur #48-41, Ayurá Center Edificio Union № 1376, Medellín, Colombia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from abc import ABC, abstractmethod


class Model(ABC):
    "The objective of this abstract class is that all the subclasses that inherit this class, implement these methods"
    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def start(self):
        pass
