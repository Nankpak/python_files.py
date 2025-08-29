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
grade ={'A':[],'B':[],'C':[],'D':[],'E':[],'F':[]}
for student,score in students_scores.items():
          if 70 <= score <= 100:
             grade['A'].append((student,score))
          elif 60 <= score <= 69:
             grade['B'].append((student,score))
  
          elif 50  <= score <= 59:
             grade['C'].append((student,score))
  
          elif 40 <= score <= 49:
             grade['D'].append((student,score))
  
          elif 30 <= score <= 39:
             grade['E'].append((student,score))
  
          elif 0 <= score <= 29:
             grade['F'].append((student,score))
             print(grade)

