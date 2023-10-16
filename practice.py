class Person:
  def __init__(self, name, age):
    self.name = name
    self._age = age
    self.x=10

  def myfunc(self):
    print("Hello my name is " + self.name)

class student(Person):
  def __init__(self,name,age,section):
    super().__init__(name,age)
  def run(self):
    print(self.x)

x = student('raja',23,'ttt')
x.myfunc()0
