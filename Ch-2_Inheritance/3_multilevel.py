class company:

    title:str ="consultancy"

    def __init__(self,company_name:str):
        self.company_name:str=company_name

    def info(self):
        print(f"company name:{self.company_name}")
        return self.company_name

class manager(company):

    def __init__(self, manager_name,company_name):
        super().__init__(company_name)
        self.manager_name=manager_name

    def info(self):
        response=super().info()
        print(f"manager name:{self.manager_name} works at {response}")
        return f"{response} under manager {self.manager_name}"

class employee(manager):

    def __init__(self, employee_name,manager_name, company_name):
        super().__init__(manager_name, company_name)
        self.employee_name=employee_name

    def info(self):
        response=super().info()
        print(f"employee name:{self.employee_name} works at {response}")


obj=employee("john","shaik","abc")
obj.info()