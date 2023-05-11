#!/usr/bin/python3

"""
File_name: 102-magic_calculation.py
Created: 11th of May, 2023
Auth: Bassey John
Size: undefined
Project: 0x02-python-import_modules
Status: submitted.
"""

def magic_calculation(a, b):
	from magic_calculation_102 import add, sub
	if a < b:
	c = add(a, b)
	for i in range(4, 6):
	c = add(c, i)
	return c
	else:
	return sub(a, b)
