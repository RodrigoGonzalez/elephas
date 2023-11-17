from __future__ import absolute_import

import numpy as np


def add_params(p1, p2):
    '''
    Add two lists of parameters
    '''
    return [x+y for x, y in zip(p1, p2)]


def subtract_params(p1, p2):
    '''
    Subtract two lists of parameters
    '''
    return [x-y for x, y in zip(p1, p2)]


def get_neutral(array):
    '''
    Get list of zero-valued numpy arrays for
    specified list of numpy arrays
    '''
    return [np.zeros_like(x) for x in array]


def divide_by(array_list, num_workers):
    '''
    Divide a list of parameters by an integer num_workers.
    '''
    for i, x in enumerate(array_list):
        array_list[i] /= num_workers
    return array_list
