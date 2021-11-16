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
		print("%s Party has %d counted members, %d calculated\nHouse seats, and %d calculauted Popularity points.\n" % (partyObjects[i].getName(),partyObjects[i].getMembers(),partyObjects[i].getHouse(),partyObjects[i].getPoints()))

def main():
	createObjects()
	while True:
		print("-------------------------------------------\nUNITED PARTIES OF DISCORD ELECTORAL MANAGER\n-------------------------------------------\n1. Display party member counts\n2. Input party member counts ")
		choice = int(input("Input choice (1-2): "))
		print()
		if choice == 1:
			outputInfo()
		elif choice == 2:
			print()
		else:
			print("\n\nError - Invalid input.\n\n")

main()