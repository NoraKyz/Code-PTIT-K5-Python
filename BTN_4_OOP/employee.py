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
        return "ID: " + self.id + "\nName: " + self.name + "\nLương: " + str(self.salary) +'\n' + "ID phòng ban: " + self.department_id +'\n'+ "Tên phòng ban: " + self.department_name
    