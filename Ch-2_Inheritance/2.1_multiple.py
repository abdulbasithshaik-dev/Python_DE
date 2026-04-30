class company:

    title:str ="consultancy"

    def __init__(self,company_name:str):
        self.company_name:str=company_name

    def info(self):
        print(f"company name:{self.company_name}")
        return self.company_name

class client_company(company):

    def __init__(self, client_company_name,company_name):
        self.client_company_name=client_company_name
        super().__init__(company_name)

    def info(self):
        response=super().info()
        
        print(f"client company name:{self.client_company_name} works with {response}")
        return f"{response} with client {self.client_company_name}"


class employee(client_company):

    def __init__(self, employee_name,client_company_name,company_name):
        self.employee_name=employee_name
        super().__init__(client_company_name,company_name)


    def info(self):
        response=super().info()
        print(f"employee name:{self.employee_name} works at {response}")


class contractor(client_company,company):
    
    def __init__(self, contractor_name,client_company_name,company_name):
        self.contractor_name=contractor_name
        super().__init__(client_company_name,company_name)

    def info(self):
        response=super().info()
        print(f"contractor name:{self.contractor_name} works at {response}")

        bj=employee("john","tecg","kyndryl")

obj=contractor("shaik","tecg","kyndryl")
obj.info()