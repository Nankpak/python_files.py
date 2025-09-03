class Animal:
    def __init__(self,name,age,size):
        self.name = name
        self._age = age
        self.__size = size
    def eat(self):
        print(f'the dog name is {self.name}')
    def get_age(self):
        return self._age
    def getsize(self):
        return self__size
dog = Animal('popi',2,'large')
print(dog.name)
print(dog._age)
print(dog.getsize)
