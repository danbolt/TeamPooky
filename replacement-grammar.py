#!/usr/bin/python

import string
import sys

class Rule:
	inString = ""
	outString = ""
	def __init__(self, inString, outString):
		self.inString = inString;
		self.outString = outString;


def replaceWithRule(input, rule):
	return string.replace(input, rule.inString, rule.outString)

def makeRule(input):
	splitInput = string.split(input, "|")
	return Rule(splitInput[0], splitInput[1])

def translateWithRules(rules, input):
	if (len(rules) == 0):
		return input
	else:
		outp = replaceWithRule(input, rules[0])
		rules.pop(0)
		return translateWithRules(rules, outp)



def main():
	rules = []
	readingRules = True

	while (readingRules == True):
		s = sys.stdin.readline().rstrip('\r\n')
		if (len(s) == 0):
			readingRules = False
		else:
			rules.append(makeRule(s))

	# keep reading newlines until we get the message
	s = ""
	while (len(s) == 0):
		s = sys.stdin.readline().rstrip('\r\n')

	print translateWithRules(rules, s)
	#


if __name__ == "__main__":
	main()
