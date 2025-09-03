def counter():
    if not hasattr(counter,'count'):
       counter.count=0
    counter.count += 1
    return counter.count
print(counter())
print(counter())
