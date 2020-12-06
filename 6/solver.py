#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A simple script to solve https://adventofcode.com/2020/day/6
"""

groups = []

def populate_groups(formatedText):
	formatedGroups = formatedText.split('\n\n')
	for fromatedGroup in formatedGroups:
		tmp_answers_list = fromatedGroup.split('\n')
		groups.append(tmp_answers_list)
	print(groups)

def main():
	# Open a file: file
	file = open('input.txt',mode='r')
	 
	# read all lines at once
	formatedText = file.read()
	populate_groups(formatedText)
	 
	# close the file
	file.close()

if __name__ == "__main__":
	main()