word = 'foods'
dic = {}
for i in word:	
    if i in dic:
       dic[i] += 1
    else:
       dic[i] = 1
for keys in dic:
    if dic[keys] == 1:
       print(keys, end="")
print()
print('********************')
string = 'dogging'
unique = []
for i in range(len(string)):
    count = 0
    for j in range(len(string)):
       if string[i] == string[j]:
          count +=1
    if count == 1:
       unique.append(string[i])
if len(unique) >= 2:
   for k in unique:
       print(k, end='')
