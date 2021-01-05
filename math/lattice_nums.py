#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:32:19 2020

@author: vdixit
"""


for x in range(-80, -26):
    y = (-8*x + 791)/27
    if y.is_integer():
        print(x, y)
        