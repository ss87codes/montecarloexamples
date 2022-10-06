# One of the most influential figures in the history of probability theory was Blaise Pascal. His interest in the field began when a friend asked him the following question:
# "Would it be profitable given 24 rolls of a pair of fair dice to bet against there being at least one double six?"
# Write a function that uses Monte Carlo to simulate the probability of getting a pair of 6's within twenty-four rolls of a pair of dice.



import random

def rolldie():
	return random.choice([1,2,3,4,5,6])

def montecarloprob(numtrials):
	count = 0.0
	for j in range(numtrials):
		for i in range(24):
			first = rolldie()
			second = rolldie()
			if first==6 and second==6:
				count +=1
				break
	return count/numtrials

print(montecarloprob(24))
print(montecarloprob(50))
print(montecarloprob(5000))
print(montecarloprob(500000))
print(montecarloprob(5000000))
