import json as filereader

class Party():
	def __init__(self,name,members,extrapoints):
		self.name = name
		self.points = (members*5) + extrapoints

	def listAttributes(self):
		return [self.name, self.points]

with open("parties.json","r") as partyFile:
	partyDict = filereader.load(partyFile)
#partyDict is a two-dimensional dictionary
#partyDict[i] has keys "name","members","extrapoints"

partyRefs = list(partyDict.keys())
partyNames = []
print(partyRefs)
print(partyNames)