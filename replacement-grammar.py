import string

class Rule:
	inString = ""
	outString = ""
	def __init__(self, inString, outString):
		self.inString = inString;
		self.outString = outString;


def replaceWithRule(input, rule):
	return string.replace(input, rule.inString, rule.outString)

def parseRule(input):
	splitInput = string.split("|")
	return Rule(splitInput[0], splitInput[1])

def main():
	#


if __name__ == "__main__":
	main()
