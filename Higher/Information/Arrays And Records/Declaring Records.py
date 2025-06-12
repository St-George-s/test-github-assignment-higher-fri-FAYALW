#Declaring Records
#In SQA Reference Language (Pseudocode), we declare a record as follows:
    #RECORD player IS {
		#STRING uniqueID, 
		#INTEGER score, 
		#REAL minutes, 
		#INTEGER speed, 
		#INTEGER Strength, 
		#INTEGER agility
	#}
	
#In Python (when asked in the exam), we declare a record as follows:

# To create a record called Player with default values 
	#class Player:
	    #uniqueID: str = ""
	    #score: int = 0
	    #minutes: float = 0.0
	    #speed: int = 0
	    #strength: int = 0
	    #agility: int = 0
	
#In Python (when implementing our code), we declare a record as follows:

	# To create a record called Player with default values 
	#class Player:
	  #def __init__(self, uniqueID, score, minutes, speed, strength, agility):
	    #self.uniqueID: str = uniqueID
	    #self.score: int = score
	    #self.minutes: float = minutes
	    #self.speed: int = speed
	    #self.strength: int = strength
    #self.agility: int = agility