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
new = {}
for i,k in students_scores.items():
    if 70 <= k <= 100:
       new.update({i:k})
       print(i,k)
    elif 60<=k<=69:
       new.update({i:k})
       print('60-69')
       print(i,k)
    elif 50<=k<=59:
       new.update({i:k})
       print('50-59')
       print(i,k)
    elif 40 <=k<=49:
       new.update({i:k})
       print('40-49')
       print(i,k)
    elif 30 <=k<=39:
       new.update({i:k})
       print('30-39')
       print(i,k)
    elif 0<=k<=29:
       new.update({i:k})
       print('0-29')
       print(i,k)
