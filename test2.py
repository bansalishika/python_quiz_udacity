from variables import *


def choose_level():

	print introduction

	level = raw_input()
	print game_data[level]['quiz']

	start_quiz(level)



def start_quiz(level):

	print "this is an ", level, " quiz"

	data = game_data[level]
	dictionary = data['ques_ans']

	for i in question:

		q = i['ques']
		a = i ['answer']


		result = ask_question(q, a)
	print congrats 


def ask_question(ques, ans):

	print ques
	answer = raw_input()
	
	correct = 0 

	while (correct == 0):
		if answer.lower() == ans.lower():
			correct = 1 
		else:
			print 'Wrong answer. Try again. '
			print ques 
			answer = raw_input()


choose_level()

