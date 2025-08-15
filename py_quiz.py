questions = ('Q1. bool + bool is =?',
             'Q2. bool + int is =?',
	     'Q3. bool + float is =?',
	     'Q4. bool + str is =?',
	     'Q5. str + str is =?',
	     'Q6. str + int is =?',
	     'Q7. str + float is =?',
	     'Q8. str + bool is =?',
	     'Q9. int + int is =?',
	     'Q10. int + float is =?',
	     'Q11. int + str is =?',
	     'Q12. int + bool is =?',
	     'Q13. float + bool',
	     'Q14. float + float is =?',
	     'Q15. float + str is =?',
	     'Q16. float + int is =?')
options = (('A. bool','B. syntaxError','C. TypeError','D. string'),
           ('A. float','B. bool','C. int','D. TypeError'),
	   ('A. TypeError','B.SyntaxError ','C. float','D. bool'),
	   ('A. str','B. int','C. TypeError','D. bool'),
	   ('A. float','B. int','C. TypeError','D. str'),
	   ('A. int','B. str','C. TypeError','D. bool'),
	   ('A. TypeError','B. float','C. str','D. int'),
	   ('A. str','B. int','C. TypeError','D. bool'),
	   ('A. int','B. float','C. TypeError','D. NameError'),
	   ('A. syntaxError','B. float','C. str','D. int'),
	   ('A. str','B. ValueError','C. TypeError','D. int'),
	   ('A. str','B. float','C. int','D. TypeError'),
	   ('A. float','B. ValueError','C. bool','D. int'),
	   ('A. TypeError', 'B. int','C. str','D. float'),
	   ('A. TypeError','B. float','C. ValueError','D. str'),
	   ('A. invalidSyntax','B. int','C. TypeError','D. float'))
answers =('A','C','C','C','D','C','A','C','A','B','C','C','A','D','A','D')
guesses = []
option_index = 0
score = 0
for question in questions:
	print('----------------------------------')
	print(question)
	for option in options[option_index]:
		print(option)
	guess = input('selection option (A,B,C,D) ').upper()
	guesses.append(guess)
	if guess == answers[option_index]:
		score += 1
		print("CORRECT")
	else:
		print("INCORRECT")
		print(f'{answers[option_index]} is the correct answer')
	option_index +=1
print('Answer: ')
for answer in answers:
	print(answer, end=" ")
print()
print('Guesses')
for guess in guesses:
	print(guess, end=" ")
print()
score = score / len(questions)*100
print(f'score {score:.0f}percentage')
