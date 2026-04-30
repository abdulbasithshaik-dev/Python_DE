class myclass:

    var=100

    #dunder method or magic method
    def __init__(self):
        print("this is a constructor")

    #dunder method for string representation of the object
    def __str__(self):
        return "this is a string representation of the object"
    
    @classmethod
    def _change_value(cls,new_value):
        cls.var=new_value
    @staticmethod
    def dummy():
        print("this is a dummy method")

obj=myclass()
print(obj.var)

obj1=myclass()
obj1._change_value(200)
print(myclass.var)

obj2=myclass()
print(obj2.var)

obj3=myclass()
print(obj3.dummy())


obj4=myclass()
print(obj4.__str__())
print(obj4)