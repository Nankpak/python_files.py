class Animal:
   def __init__(self,name,alive,gender):
       self.name=name
       self.alive=alive
       self.gender=gender
   def eat(self):
       print(f'the animal is a {self.name} and its eating')
   def walk(self):
       print(f'the {self.name} is walking')
   def alive(self):
       print(f'it is {self.alive} the {self.name} is alive')
   def gender(self):
       print(f'the {self.name} is a {self.gender}')
animal_1 = Animal('monkey',True,'female')
animal_1.eat()
animal_1.walk()
print(animal_1.alive)
