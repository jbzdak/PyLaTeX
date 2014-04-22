# -*- coding: utf-8 -*-
u"""
    pylatex.base_classes
    ~~~~~~~~~~~~~~~~~~~~

    This module implements base classes with inheritable functions for other
    LaTeX classes.

    :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

from ordered_set import OrderedSet
from pylatex.utils import dumps_list

from six import StringIO

from jinja2 import Template, Environment


class BaseLaTeXClass(object):

    u"""A class that has some basic functions for LaTeX functions."""

    def __init__(self, packages=None):
        if packages is None:
            packages = []

        self.packages = OrderedSet(packages)

    def dumps(self):
        u"""Represents the class as a string in LaTeX syntax."""

    def dump(self, file_):
        u"""Writes the LaTeX representation of the class to a file."""
        dump = self.dumps()
        file_.write(dump)

    def dumps_packages(self):
        u"""Represents the packages needed as a string in LaTeX syntax."""
        return dumps_list(self.packages)

    def dump_packages(self, file_):
        u"""Writes the LaTeX representation of the packages to a file."""
        file_.write(self.dumps_packages())


class TemplatedLatexMixin(object):

    TEMPLATE = None

    ENV = Environment(
        '%{%', '%}%',
        '%{{'
    )

    def dumps(self):
        u"""Represents the class as a string in LaTeX syntax."""
        file = StringIO.StringIO()
        self.dump(file)

    def dump(self, file_):
        u"""Writes the LaTeX representation of the class to a file."""

        template = Template(self.TEMPLATE)
        for token in template.generate(s=self):
            file_.write(token)

class BaseLaTeXContainer(BaseLaTeXClass):

    u"""A base class that can cointain other LaTeX content."""

    def __init__(self, data=None, packages=None):
        if data is None:
            data = []

        self.data = data

        super(BaseLaTeXContainer, self).__init__(packages=packages)

    def append(self, item):
        self.data.append(item)

    def __iter__(self):
        """
        Iterates over appened items
        """
        return iter(self.data)

    def dumps(self):
        u"""Represents the container as a string in LaTeX syntax."""
        self.propegate_packages()

    def propegate_packages(self):
        u"""Makes sure packages get propegated."""
        for item in self.data:
            if isinstance(item, BaseLaTeXClass):
                for p in item.packages:
                    self.packages.add(p)

    def dumps_packages(self):
        u"""Represents the packages needed as a string in LaTeX syntax."""
        self.propegate_packages()
        return dumps_list(self.packages)


class BaseLaTeXNamedContainer(BaseLaTeXContainer):

    u"""A base class for containers with one of a basic begin end syntax"""

    def __init__(self, name, data=None, packages=None, options=None):
        self.name = name
        self.options = options

        super(BaseLaTeXNamedContainer, self).__init__(data=data, packages=packages)

    def dumps(self):
        u"""Represents the named container as a string in LaTeX syntax."""
        string = ur'\begin{' + self.name + u'}\n'

        if self.options is not None:
            string += u'[' + self.options + u']'

        string += dumps_list(self)

        string += ur'\end{' + self.name + u'}\n'

        super(BaseLaTeXNamedContainer, self).dumps()

        return string

class BaseTemplatedLaTeXNamedContainer(TemplatedLatexMixin, BaseLaTeXNamedContainer):

    TEMPLATE = u"""
    \
    """.strip()