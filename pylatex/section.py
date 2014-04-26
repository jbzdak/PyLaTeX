# -*- coding: utf-8 -*-
u"""
    pylatex.section
    ~~~~~~~

    This module implements the class that deals with sections.

    :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from .utils import dumps_list
from .base_classes import BaseLaTeXContainer


class SectionBase(BaseLaTeXContainer):

    u"""A class that is the base for all section type classes"""

    def __init__(self, title, numbering=True, data=None):
        self.title = title
        self.numbering = numbering

        super(SectionBase, self).__init__(data)

    def dumps(self):
        u"""Represents the section as a string in LaTeX syntax."""

        if not self.numbering:
            num = u'*'
        else:
            num = u''

        base = u'\\' + self.__class__.__name__.lower() + num
        string = base + u'{' + self.title + u'}\n' + dumps_list(self)

        super(SectionBase, self).dumps()
        return string


class Section(SectionBase):

    u"""A class that represents a section."""

    def __init__(self, title, numbering=True, data=None):
        super(Section, self).__init__(title, numbering, data)


class Subsection(SectionBase):

    u"""A class that represents a subsection."""

    def __init__(self, title, numbering=True, data=None):
        super(Subsection, self).__init__(title, numbering, data)



class Subsubsection(SectionBase):

    u"""A class that represents a subsubsection."""

    def __init__(self, title, numbering=True, data=None):
        super(Subsubsection, self).__init__(title, numbering, data)
