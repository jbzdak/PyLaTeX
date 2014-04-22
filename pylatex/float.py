# -*- coding: utf-8 -*-

from pylatex.base_classes import *
import re

FLOAT_PLACEMENT = r'[Hhtpb]\!?'

class Float(BaseTemplatedLaTeXNamedContainer):
    """

    """
    FLOAT_NAME = None
    TEMPLATE_NAME = "float.tex"
    def __init__(self, name=None, placement=None, data=None, packages=None, label=None, caption=None):
        if name is None:
            name = self.FLOAT_NAME
        super(Float, self).__init__(name, data, packages)
        if not re.match(FLOAT_PLACEMENT, placement):
            raise ValueError(u"Invalid float placement.")
        self.options.append(placement)
        self.label = label
        self.caption = caption

class Graphics(BaseLaTeXClass):
    """
    >>> print(Graphics("foo.png").dumps())
    \\includegraphics{foo.png}
    >>> print(Graphics("foo.png", width=Dimension(0.5, "textwidth")).dumps())
    \\includegraphics[width=0.5\\textwidth]{foo.png}
    """
    def __init__(self, file, width=None, height=None):
        super(Graphics, self).__init__()
        self.file = file
        self.width = width
        self.height = height

    def dumps(self):
        options = Options()
        if self.width is not None:
            options['width'] = self.width
        if self.height is not None:
            options.height = self.height

        return "\includegraphics{opts}{{{file}}}".format(opts=options.dumps(), file=self.file)


class Figure(Float):

    """
    >>> f = Figure(placement='h')
    >>> print(f.dumps()) #doctest: +NORMALIZE_WHITESPACE
    \\begin{ figure }[h]
    <BLANKLINE>
    \\end{ figure }
    >>> f = Figure(placement='h', label="Foo", caption="The Foo figure")
    >>> print(f.dumps()) #doctest: +NORMALIZE_WHITESPACE
    \\begin{ figure }[h]
    <BLANKLINE>
    \\caption{ The Foo figure \\label{ Foo }}
    \\end{ figure }

    """
    FLOAT_NAME = "figure"