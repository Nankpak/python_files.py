students_scores = {
    "Aisha": 95,
    "David": 82,
    "Mary": 99,
    "John": 78,
    "Sarah": 65,
    "Paul": 88,
    "Grace": 100,
    "James": 73,
    "Ruth": 84,
    "Daniel": 90,
    "Michael": 67,
    "Esther": 59,
    "Tunde": 48,
    "Ngozi": 34,
    "Chinedu": 27,
    "Hauwa": 72,
    "Ibrahim": 41,
    "Femi": 53,
    "Victoria": 68,
    "Samuel": 38
}
isrunning = True
while isrunning:
    grade ={
        'first_class':[],
        'second_upper':[],
        'second_lower':[],
        'third_class':[],
        'pass_degree':[]
    }
    for student,score in students_scores.items():
        if 70 <= score <= 100:
           grade['first_class'].append((student,score))
        elif 60 <= score <= 69:
           grade['second_upper'].append((student,score))
          
        elif 50  <= score <= 59:
           grade['second_lower'].append((student,score))
          
        elif 40 <= score <= 49:
           grade['third_class'].append((student,score))
          
        elif 30 <= score <= 39:
           grade['third_class'].append((student,score))
          
        elif 0 <= score <= 29:
           grade['pass_degree'].append((student,score))
           print(grade)
        isrunning = False
