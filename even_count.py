def count_even():
    numbers=([1,2,3,4,6,8,10])
    count = 0
    for number in numbers:
        if number %2 ==0:
           count +=1
    print(count)
count_even()
