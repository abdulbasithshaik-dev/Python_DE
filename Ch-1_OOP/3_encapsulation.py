class myclass():

    #class variables
    var1="shaik"
    var2="abdul"
#instance variables constructors
    def __init__(self,dyna1,dyna2,dyna3):
        self.dyna1=dyna1 #public variable
        self.__dyna2=dyna2 #private variable
        self._dyna3=dyna3  #protected variable

    def func1(self):
        print(f"hello world,{self.dyna1}")

    def func2(self):
        print(f"welcome to python,{self.__dyna2}")
        
    def func3(self):
        print(f"welcome to python,{self._dyna3}")

dev1=myclass("shaik","doop","noob")
dev1.dyna1="pqr"
print(dev1.dyna1)


dev1.dyna2="stuv"
print(dev1.dyna2)
dev1.func2()


print(dev1._dyna3)
changed=dev1.__dyna2="dfg"
dev1.func3()

