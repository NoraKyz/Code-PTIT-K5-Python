from employee import Employee

DB_FILE = 'NV.txt'

class Manager:
    def __init__(self) -> None:
        pass

    def load_NV(self):
        try:
            with open('NV.txt', 'r', encoding='utf-8') as file:
                dataNV = []
                for line in file:
                    id, name, salary, department_id, department_name = line.strip().split(', ')
                    employee = Employee(name, salary, department_id, department_name)
                    employee.setId(id)
                    dataNV.append(employee)
                return dataNV
        except FileNotFoundError:
            return []

    def save_users(self, dataNV: list[Employee]):
        with open(DB_FILE, 'w', newline='', encoding='utf-8') as file:
            for employee in dataNV:
                NV_data = f"{employee.id}, {employee.name}, {employee.salary}, {employee.department_id}, {employee.department_name}\n"
                file.write(NV_data)

    def add_NV(self, employee: Employee):
        if employee == None:
            return
        
        employee.setId()
        dataNV = self.load_NV()
        dataNV.append(employee)
        self.save_users(dataNV)

    def delete_NV(self, id: str):
        dataNV = self.load_NV()
        for employee in dataNV:
            if employee.id == id:
                dataNV.remove(employee)
        self.save_users(dataNV)

    def update_salary_NV(self, id: str, salary: int):
        dataNV = self.load_NV()
        for employee in dataNV:
            if employee.id == id:
                employee.salary = salary
        self.save_users(dataNV)

    def find_NV(self, id: str) -> Employee:
        dataNV = self.load_NV()
        for employee in dataNV:
            if employee.id == id:
                return employee
            
        return None
            
    def display_all_NV(self):
        dataNV = self.load_NV()
        