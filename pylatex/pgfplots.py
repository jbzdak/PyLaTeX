# -*- coding: utf-8 -*-
u"""
    pylatex.pgfplots
    ~~~~~~~~~~~~~~~~

    This module implements the classes used to show plots.

    :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""
import six

from pylatex.base_classes import BaseLaTeXClass, BaseLaTeXNamedContainer, \
    Options
from pylatex.package import Package


class TikZ(BaseLaTeXNamedContainer):

    u"""Basic TikZ container class."""

    def __init__(self, data=None):
        packages = [Package(u'tikz')]
        super(TikZ, self).__init__(u'tikzpicture', data=data, packages=packages)


class Axis(BaseLaTeXNamedContainer):

    u"""PGFPlots axis container class, this contains plots."""

    def __init__(self, data=None, options=None):
        packages = [Package(u'pgfplots'), Package(u'compat=newest',
                                                 base=u'pgfplotsset')]

        super(Axis, self).__init__(u'axis', data=data, options=options, packages=packages)


class Plot(BaseLaTeXClass):

    u"""PGFPlot normal plot."""

    def __init__(self, name=None, func=None, coordinates=None, options=None):
        self.name = name
        self.func = func
        self.coordinates = coordinates
        self.options = Options.create(options)

        packages = [Package(u'pgfplots'), Package(u'compat=newest',
                                                 base=u'pgfplotsset')]

        super(Plot, self).__init__(packages=packages)

    def dumps(self):
        u"""Represents the plot as a string in LaTeX syntax."""
        string = six.text_type()

        string+= r'\addplot'

        string += self.options.dumps()

        if self.coordinates is not None:
            string += u' coordinates {\n'

            for c in self.coordinates:
                string += u'(' + six.text_type(c[0]) + u',' + six.text_type(c[1]) + u')\n'
            string += u'};\n\n'

        elif self.func is not None:
            string += u'{' + self.func + u'};\n\n'

        if self.name is not None:
            string += r'\addlegendentry{' + self.name + u'}\n'

        super(Plot, self).dumps()

        return string
