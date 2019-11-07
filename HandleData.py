class DataHandler:
	TAKEN = True
	OPEN = False

	def __init__(self):
		#number of time in a row a person was detected in frame
		#updated ever 10 seconds 
		self.detects_in_a_row = 0
		self.misses_in_a_row = 0
	
	def updateHandler(personWasFound):
		if (personWasFound):
			detects_in_a_row += 1
		else: 
			misses_in_a_row += 1 
		
		if (detects_in_a_row >= 6):
			# updateServer(TAKEN)
			detects_in_a_row, misses_in_a_row = 0 
		elif (misses_in_a_row >= 6):
			# updateServer(OPEN)
			detects_in_a_row, misses_in_a_row = 0 

	def updateServer(taken):
		

	


