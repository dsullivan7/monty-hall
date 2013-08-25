import random
class MontyHall:

	"""
	play1 represents the case where the contestent never switches
	"""
	def play1(self, ndoors):
		correct_choice = random.randint(0, ndoors - 1)
		contestent_choice = random.randint(0, ndoors - 1)
		"""
		since neither the contest nor the correct door change
		we can return the comparison now
		"""
		return correct_choice == contestent_choice
	
	"""
	play2 represents the case where the contestent swithces every time
	"""
	def play2(self,ndoors):
		doors = self.get_door_array(ndoors)
	    	correct_door = random.randint(0, ndoors - 1)

	    	while len(doors) > 2:
			contestent_choice = self.choose_door(doors)
			if contestent_choice != correct_door:
				doors.remove(correct_door)
			monty_choice = self.choose_door(doors)
			if contestent_choice != correct_door:
				doors.append(correct_door)
			temp_choice = self.choose_door(doors)
			doors.append(contestent_choice)
			contestent_choice = temp_choice
			doors.append(contestent_choice)

	    	return correct_door == contestent_choice 

	"""
	play3 represents the case where the contestent keeps his choice until 
	Monty leaves one door unopened and then switches to that door
	"""
	def play3(self,ndoors):
		doors = self.get_door_array(ndoors)
		correct_door = random.randint(0, ndoors - 1)
		contestent_choice = random.randint(0, ndoors - 1)

		doors.remove(contestent_choice)
		if contestent_choice != correct_door:
			doors.remove(correct_door)
		"""
		Monty selects all doors that aren't the correct door or the door 
		the contestent selected
		"""
		while len(doors) > 1:
			doors.pop()
		"""
		if the door the contestent selected was not the correct door
		the only door left is the correct door
		"""
		if contestent_choice != correct_door:
			doors.pop()
			doors.append(correct_door)
		"""
		otherwise the contestent originally choose correctly and switches
		doors in his last choice
		"""
		contestent_choice = doors.pop()
		return contestent_choice == correct_door
    	
	def play_games(self,ngames,ndoors):
	    	num_correct1 = 0
	    	num_correct2 = 0
	    	num_correct3 = 0
		for i in xrange(ngames):
			if self.play1(ndoors):
				num_correct1 += 1
			if self.play2(ndoors):
				num_correct2 += 1
			if self.play3(ndoors):
				num_correct3 += 1
		print ("The number of games guessed correctly by the contestent"
		"who did not switch at all is "+ str(num_correct1) +" out of "+str(ngames))
	
		print ("The number of games guessed correctly by the contestent"
		"who switched at every opportunity is "+ str(num_correct2) +" out of "+str(ngames))
	
		print ("The number of games guessed correctly by the contestent"
		"who waited until the last door to switch is "+ str(num_correct3) +" out of "+str(ngames))
	def get_door_array(self, ndoors):
		d = []
		for i in xrange(ndoors):
			d.append(i)
		return d

	def choose_door(self, d):
		return d.pop(random.randint(0, len(d) - 1))
