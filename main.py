import json as filereader
import os
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

class Party():
	def __init__(self,name,members,extrapoints):
		self.name = name
		self.members = members
		self.extrapoints = extrapoints
		self.points = (members*5) + extrapoints
		self.house = self.points//30 + 1

	def getName(self):
		return self.name
	def getMembers(self):
		return self.members
	def getPoints(self):
		return self.points
	def getHouse(self):
		return self.house
	def getExtras(self):
		return self.extrapoints

	def setExtras(self,newExtra):
		self.extrapoints = newExtra
		self.__init__(self.name,self.members,self.extrapoints)

	def setMembers(self,newMembers):
		self.members = newMembers
		self.__init__(self.name,self.members,self.extrapoints)

	def createDict(self):
		return {"name":self.name,"members":self.members,"extrapoints":self.extrapoints}

def saveObjects():
	newDict = {}
	for i in partyRefs:
		newDict[i] = partyObjects[i].createDict()
	with open("parties.json","w",encoding="utf-8") as file:
		filereader.dump(newDict,file,ensure_ascii=False,indent=4) 	

def createObjects():
	global partyObjects
	global partyRefs
	with open("parties.json","r") as partyFile:
		partyDict = filereader.load(partyFile)
	#partyDict is a two-dimensional dictionary
	partyRefs = list(partyDict.keys())
	partyObjects = {}
	for i,j in zip(range(len(partyRefs)),partyRefs):
		temp = partyDict[partyRefs[i]].values()
		valueArray = list(temp)
		partyObjects[j] = Party(*valueArray) #partyObjects["mp"] for example is the name of the Minarchy Party object and can be called as such

def outputInfo():
	for i in partyRefs:
		print("%s Party has %d counted members, %d calculated\nHouse seats, and %d calculauted Popularity points, %d are bonus.\n" % (partyObjects[i].getName(),partyObjects[i].getMembers(),partyObjects[i].getHouse(),partyObjects[i].getPoints(),partyObjects[i].getExtras() ) )

def inputMembers(reference):
	newMembers = input("\nInput member count for %s Party: " % partyObjects[reference].getName())
	if newMembers.isdigit():
		partyObjects[reference].setMembers(int(newMembers))
	else:
		print("\n\nerror invalid data type\n\n")
		inputMembers(reference)
	saveObjects()

def inputExtras(reference):
	newExtras = input("\nInput bonus points for %s Party: " % partyObjects[reference].getName())
	if newExtras.isdigit():
		partyObjects[reference].setExtras(int(newExtras))
	else:
		print("\n\nerror invalid data type\n\n")
		inputExtras(reference)
	saveObjects()

def inputData():
	validChoices = ["members","points"]
	print("\nINPUT TARGET PARTY REFERENCE: ")
	reference = input()
	if reference in partyRefs:
		valid = False
		while not valid:
			print("\nInput members or points?")
			choice = input()
			if choice in validChoices:
				valid = True
				if choice == "members":
					inputMembers(reference)
				elif choice == "points":
					inputExtras(reference)
			else:
				print("\nInvalid input\n")
	else:
		print("\nInvalid reference\n")
		inputData()

def main():
	createObjects()
	while True:
		print("-------------------------------------------\nUNITED PARTIES OF DISCORD ELECTORAL MANAGER\n-------------------------------------------\n1. Display party member counts\n2. Input data")
		choice = int(input("Input choice (1-2): "))
		print()
		if choice == 1:
			outputInfo()
		elif choice == 2:
			inputData()
		else:
			print("\n\nError - Invalid input.\n\n")

main()