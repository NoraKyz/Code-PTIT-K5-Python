class Employee:
    cnt = 1

    def __init__(self, name, salary, department_id, department_name) -> None:
        self.name = name
        self.salary = salary
        self.department_id = department_id
        self.department_name = department_name

    def setId(self, id = None) -> None:
        if id == None:
            self.id = "NV" + format(Employee.cnt, "03d")
            Employee.cnt += 1
        else:
            self.id = id

    def __str__(self) -> str:
        return self.id + " | " + self.name + " " * (25 - len(self.name)) + " | " + str(self.salary) + " " * (6 - len(str(self.salary))) + " | " + self.department_id + " " * (6 - len(self.department_id)) + " | " + self.department_name + " " * (20 - len(self.department_name))
    
    