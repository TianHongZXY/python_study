# -*- coding: utf-8 -*-
"""
Created on Sat May 26 16:31:34 2018

@author: hp
"""
bri = set(['brazil','russia','india'])
print('china' in bri)
print('india' in bri)
bric = bri.copy()
bric.add('usa')
print(bri.issuperset(bric))
print(bric.issuperset(bri))
print(bri&bric)
print(bri|bric)