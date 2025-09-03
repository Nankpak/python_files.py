class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count +=1
        return self.count
counter = Counter()
print(counter.increment())
print(counter.increment())
