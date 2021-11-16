import json as filereader

class Party():
	def __init__(self,name,members,extrapoints):
		self.name = name
		self.points = (members*5) + extrapoints
		self.house = self.points//30 + 1

	def listAttributes(self):
		return [self.name, self.points, self.house]

def createObjects():
	global partyObjects
	with open("parties.json","r") as partyFile:
		partyDict = filereader.load(partyFile)
	#partyDict is a two-dimensional dictionary
	partyRefs = list(partyDict.keys())
	partyObjects = {}
	for i,j in zip(range(len(partyRefs)),partyRefs):
		temp = partyDict[partyRefs[i]].values()
		valueArray = list(temp)
		partyObjects[j] = Party(*valueArray) #partyObjects["mp"] for example is the name of the Minarchy Party object and can be called as such

def main():
	createObjects()
	print("UNITED PARTIES OF DISCORD ELECTORAL MANAGER\n1. Display party member counts\n2. Input party member counts\n3. ") #unf

main()