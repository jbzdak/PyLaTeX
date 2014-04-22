# -*- coding: utf-8 -*-
from pylatex.base_classes import BaseLaTeXContainer, TemplatedLatexMixin



class Float(TBaseLaTeXContainer):

    def __init__(self, data=None, packages=None):
        super(Float, self).__init__(data, packages)

    def dumps(self):
        pass

    def append(self, item):
        super(Float, self).append(item)

