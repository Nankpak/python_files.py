class Human:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
    def description(self):
        print(f'my name is {self.name} i am {self.age} years old')
    def work(self):
        print(f'i am now working at {self.job}')
class boy(Human):
    def bio(self,schoolname):
        print(f'i study in {schoolname}')
b = boy('Nankpak',25,'self_employed')
b.description()
b.work()
b.bio('plasu')
        
