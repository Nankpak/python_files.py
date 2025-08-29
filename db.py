scores = {'Alice':[80,90],'Bob':[70,85],'Charlie':95}
isrunning = True
while isrunning:
    stu_name = input('enter student name ').capitalize()
    if stu_name == 'Exit':
       quit()
    elif stu_name in scores:
       stu_score = int(input('enter your score '))
       scores[stu_name].append(stu_score)
       print(scores)
    else:
       stu_score = int(input('enter your score '))
       scores.update({stu_name:stu_score})
       print(scores)
   
    
