class myclass():

    #class variables
    var1="shaik"
    var2="abdul"
#instance variables constructors
    def __init__(self,dyna1,dyna2,dyna3):
        self.dyna1=dyna1
        self.dyna2=dyna2
        self.dyna3=dyna3

    def func1(self):
        print(f"hello world,{self.dyna1}")

    def func2(self):
        print(f"welcome to python,{self.dyna2}")
        
    def func3(self):
        print(f"welcome to python,{self.dyna3}")

obj=myclass("shaik","abdul","doop")
obj.func3()

#another way of writing function
myclass.func1(obj)
