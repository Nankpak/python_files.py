try:
   add = lambda a,b: a+b
   sub = lambda a,b: a-b
   mult = lambda a,b:a*b
   div = lambda a,b: a/b
   print(div(2/0))
   def sum(*nums):
       v= 0
       for num in nums:
           v +=1
       return v
   print(sum(1,2,3,4,6,78)) 
   sum2 = lambda **nums: nums.items()
   print(sum2(num2=2,num=4,num22=3,num32=6,num42=7))
except ZeroDivisionError:
   print('math error')
