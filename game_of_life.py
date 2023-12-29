# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:13:47 2023

@author: laurin
"""

import board

# my screen size = 1280, 720
# this ensures nothing gets cut off
b1 = board.board(height = 72, width = 128)
b1.__draw__()