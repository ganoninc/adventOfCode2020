#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A simple script to solve https://adventofcode.com/2020/day/6
"""

__author__ = "Romain Giovanetti"
__license__ = "GPL"

import pprint

pp = pprint.PrettyPrinter(indent=4)

def build_populate_groups(formatedText):
	groups = []
	formatedGroups = formatedText.split('\n\n')
	for fromatedGroup in formatedGroups:
		tmp_answers_list = fromatedGroup.split('\n')
		groups.append({
			'answers_by_people': tmp_answers_list,
			'yes_count': 0,
			})
	#pp.pprint(groups)
	return groups


def get_total_of_yes(populated_groups):
	total_of_yes = 0
	for group in populated_groups:
		yes_count_of_current_group = 0
		encounted_yes = []
		for people_answers in group['answers_by_people']:
			for answer in people_answers:
				if answer not in encounted_yes:
					yes_count_of_current_group += 1
					encounted_yes.append(answer)
		#group['yes_count'] = yes_count_of_current_group
		total_of_yes += yes_count_of_current_group
	#pp.pprint(populated_groups)
	return total_of_yes


def main():
	# Open a file: file
	# file = open('sample.txt',mode='r')
	file = open('input.txt',mode='r')
	 
	# read all lines at once
	formatedText = file.read()
	populated_groups = build_populate_groups(formatedText)
	total_of_yes = get_total_of_yes(populated_groups)

	print('The answer is ' + str(total_of_yes))
	 
	# close the file
	file.close()

if __name__ == "__main__":
	main()