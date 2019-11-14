TAKEN = True
OPEN = False

class DataHandler:
	def __init__(self, d=0, m=0):
		#number of time in a row a person was detected in frame
		#updated ever 10 seconds 
		self.detects_in_a_row = d
		self.misses_in_a_row = m
	
	def updateHandler(self, personWasFound):
		if (personWasFound):
			self.detects_in_a_row += 1
		else: 
			self.misses_in_a_row += 1 
		
		if (self.detects_in_a_row >= 6):
			self.updateServer(TAKEN)
			self.detects_in_a_row = 0 
			self.misses_in_a_row = 0 
		elif (self.misses_in_a_row >= 6):
			self.updateServer(OPEN)
			self.detects_in_a_row = 0
			self.misses_in_a_row = 0 

	def updateServer(self, taken):
		if (taken):
			print("taken")
		else:
			print("open")


# #Testing main
# if __name__ == "__main__":
# 	d = DataHandler(6, 0)
# 	d.updateHandler(True)
# 	d2 = DataHandler()

		

	


