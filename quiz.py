#quiz program
questions = ('who is the first president of Nigeria?',
           'who is the first man on earth?',
           'who is the strongest man in the bible?',
           'which animal is the largest on earth?',
           'who is the head of the family?',
           'how may days do we have in  week?')

options = (('A. Dr Nnamdi Azikiwe','B. Olusegun Obanjo','C. Alhaji Shehu Shagari','D. Gen Murtala Muhamed'),
          ('A. Adam','B. Moses','C. Adama','D. God'),
          ('A. David','B. Cain','C. Jesus','D. Samson'),
          ('A. Elephan','B. Cow','C. Fish','D. Fat animal'),
          ('A. First son','B. Father','C. Mother','D. Uncle'),
	  ('A. 7','B. 6','C. 77','D. 8'))
answers = ('C','A','D','C','B','A')
score = 0
guesses= []
question_num = 0
for question in questions:
	print('---------------')
	print(question)
	for option in options[question_num]:
		print(option)
	guess= input('Enter (A,B,C,D): ').upper()

	guesses.append(guess)
	if guess == answers[question_num]:
		score += 1
		print('CORRECT')
	else:
		print('INCORRECT')
		print(f'{answers[question_num]} is the correct answer')
	question_num += 1
print('answer: ', end ="")
for answer in answers:
	print(answer)
print()
print('guesses: ', end="")
for guess in guesses:
	print(guess)
print()
score = score /len(question)*100
print(f'your score is {score}')

