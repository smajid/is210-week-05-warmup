#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Declares two parameters, besides that I have no clue what's happening.

    Args:
        wink(mixed): First parameter.
        numwink(int): Second parameter, with a default value of 2.

    Returns:
        str: A string because of .format()

    Examples:

        >>>couldn't run this code, didn't know exactly what to type.
        Tried many know_what_i_mean options ad combinations.
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
