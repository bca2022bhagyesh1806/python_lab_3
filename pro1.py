class Employee:
    def __init__(self,empnm,doj,desig,sal):
        self.empnm = empnm
        self.doj = doj
        self.desig = desig
        self.sal = sal
data = Employee("Bhagyesh Patel","20-2-2024","Manager",180000)
print(f"Employee Name :- {data.empnm}\nDate Of Join :- {data.doj}\nDesignation :- {data.desig}\nSalary :- {data.sal}") 
