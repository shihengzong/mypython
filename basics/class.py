class Person:
    # __xx__ 表示私有属性
    def __init__(self,name):
        self.name = name
    def printPerson(self):
        print("这是%s的printPerson方法." % self.name)

p = Person("张三")
p.printPerson()

class Parents:
    def __init__(self,name):
        self.name = name
    def say(self):
        print("i am your father !")
    def getName(self):
        return self.name


# 继承
class Child(Person,Parents):
    pass
    # def __init__(self):
    # super().__init__()
    # def say():
    # print("i am your father !")

class Child2(Parents):
    pass
  

c = Child("child")
c.printPerson()

c2 = Child2("child")
c2.say()
print(c2.getName())


class Abstract:
    def setName(self,x,y):
        return x+y,x*y

class Child3(Abstract):
    pass

child3 = Child3()
print(child3.setName(1,2))

# 
seq = ('Google', 'Runoob', 'Taobao')
 
dict = dict.fromkeys(seq)
print(dict)

dict = dict.fromkeys(seq, 10)
print(dict)