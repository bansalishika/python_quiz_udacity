from variables import *
'''imports everything from another file. '''





"""
  Args:
      level : This argument has 3 options: easy, medium, hard chosen using above function. 
  Behavior:
      This helps to choose one level.
  Returns:
      nothing 
  """

def choose_level():

	print introduction

	#ask level from user
	level = raw_input()
	level = level.lower() 

	#print main question of that level
	print game_data[level]['quiz']

	#this will start the question and answers
	start_quiz(level)



"""
  Args:
      level : This argument has 3 options: easy, medium, hard chosen using above function. 
  Behavior:
      this function will start the quiz and connects it to the other function.
  Returns:
      nothing 

  """


def start_quiz(level):

	print "\n\n", "This is ", level, " quiz"

	data = game_data[level]

	questions = data['ques_ans']

	# the below loop will seperate the questions and answers. Seperate variables will have both the things seperately. 
	for dictionary in questions:

		quest = dictionary['ques']
		answ = dictionary['answer']
		full = dictionary['full']


		#this connects us to the other function. 
		result = ask_question(quest,answ,full)



	# when all the questions are answered. The concluding line will be printed. 
	print congrats 






"""
  Args:
      ques: this is the question in dictionary (game_data)
      ans: this is the answer in dictionary (game_data)
  Behavior:
      this function will check whether the answer is correct or not, if correct moves on to the other questions. 
  Returns:
     after the answer is correct, returns correct as 1 which breaks the loop and the next question is printed. 

  """

def ask_question(ques, ans, full):

	# the question will be printed. 
	print ques

	# asks for user input
	user_answer = raw_input()

	correct = 0


	'''this loop will keep on working until the person answers the question correctly. Once it is done, the same will apply to other blanks. '''
	while (correct==0):
		if user_answer.lower() == ans.lower():
			correct = 1
			print 'correct answer \n\n'
			print full ,'\n\n'
			return correct

		else:
			print "Wrong answer. Try again \n\n"
			print ques
			user_answer = raw_input()





# this makes the whole code run. 
choose_level()