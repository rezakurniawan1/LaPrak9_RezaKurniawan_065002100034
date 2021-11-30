# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:03:51 2021

@author: Reza Kurniawan
"""
a = ((1, 2, 3), (2, 3, 4, 5), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8, 9))

rata_rata = []
for x in a:
	rata_rata.append(sum(x) / len(x))
		
print("Tuple: ", a)
print("Rata-rata tiap tuple: ", rata_rata)

