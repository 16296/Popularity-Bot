import json as filereader

class Party():
	def __init__(self,name,members,extrapoints):
		self.name = name
		self.points = (members*5) + extrapoints

	def listAttributes(self):
		return [self.name, self.points]


partyList = filereader.load(file open)