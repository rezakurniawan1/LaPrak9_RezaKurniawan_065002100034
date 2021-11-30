# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:03:51 2021

@author: Reza Kurniawan
"""
a = ["abc", "bab", "gui", "51825"]
print("List string: ", a)

count = 0
for x in a:
	if x[:1] == x[-1:]:
		print("- ", x)
		count += 1

print(f"Terdapat {count} string yang memenuhi kriteria")