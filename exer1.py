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
new = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[]}
db = list(students_scores.items())
a,b = db[0]
j = 0
while j < len(db):
    a,b = db[j]
    if 70 <= b <=100:
       new['A'].append((a,b))
    if 60 <= b <= 69:
       new['B'].append((a,b))
    if 50 <= b <=59:
       new['C'].append((a,b))
    if 40 <= b <= 49:
       new['D'].append((a,b))
    if 30 <= b <= 39:
       new['E'].append((a,b))
    if 0 <= b <= 29:
       new['E'].append((a,b))
       print(new)
    j += 1
    break
