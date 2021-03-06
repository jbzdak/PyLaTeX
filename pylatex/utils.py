# -*- coding: utf-8 -*-
u"""
    pylatex.utils
    ~~~~~~~

    This module implements some simple functions with all kinds of
    functionality.

    :copyright: (c) 2014 by Jelte Fennema.
    :license: MIT, see License for more details.
"""

_latex_special_chars = {
    u'&':  ur'\&',
    u'%':  ur'\%',
    u'$':  ur'\$',
    u'#':  ur'\#',
    u'_':  ur'\_',
    u'{':  ur'\{',
    u'}':  ur'\}',
    u'~':  ur'\lettertilde{}',
    u'^':  ur'\letterhat{}',
    u'\\': ur'\letterbackslash{}',
    u'\n': ur'\\\\',
}


def escape_latex(s):
    u"""Escape characters that are special in latex.

    Sources:
        * http://tex.stackexchange.com/a/34586/43228
        * http://stackoverflow.com/a/16264094/2570866
    """
    return u''.join(_latex_special_chars.get(c, c) for c in s)


def dumps_list(l, escape=False, token=u'\n'):
    u"""Dumps a list that can contain anything"""
    return token.join(_latex_item_to_string(i, escape) for i in l)


def _latex_item_to_string(i, escape=False):
    u"""Use the render method when possible, otherwise use str."""
    if hasattr(i, u'dumps'):
        return i.dumps()
    elif escape:
        return unicode(escape_latex(i))
    return unicode(i)


def bold(s):
    u"""Returns the string bold.

    Source: http://stackoverflow.com/a/16264094/2570866
    """
    return ur'\textbf{' + s + u'}'


def italic(s):
    u"""Returns the string italicized.

    Source: http://stackoverflow.com/a/16264094/2570866
    """
    return ur'\textit{' + s + u'}'
