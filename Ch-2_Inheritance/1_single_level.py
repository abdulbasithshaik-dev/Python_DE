class company:

    title:str ="consultancy"

    def __init__(self,company_name:str):
        self.company_name:str=company_name

    def info(self):
        print(f"company name:{self.company_name}")
        return self.company_name

class employee(company):

    def __init__(self, employee_name,company_name):
        self.employee_name=employee_name
        self.company_name=company_name

    def employee_info(self):
        response=company.info(self)
        print(f"employee name:{self.employee_name} works at {response}")

obj1=employee("john","abc")
obj1.employee_info()