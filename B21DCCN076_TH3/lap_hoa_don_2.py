import datetime

class Customer:
    cnt = 0
    def __init__(self, name, room, start, end, service):
        Customer.cnt += 1
        self.id = 'KH' + format(Customer.cnt, '02d')
        self.name = name
        self.room = room
        self.start = start
        self.end = end
        self.service = service
        self.total = self.get_total()

    def get_gia_phong(self):
        if self.room[0] == '1':
            return 25
        elif self.room[0] == '2':
            return 34
        elif self.room[0] == '3':
            return 50
        else:
            return 80
    
    def get_total(self):
        return ((self.end - self.start).days + 1) * self.get_gia_phong() + self.service
    
    def __str__(self):
        return f'{self.id} {self.name} {self.room} {(self.end - self.start).days + 1} {self.total}'
    
if __name__ == '__main__':
    n = int(input())
    list_customer = []
    for i in range(n):
        name = input().strip()
        room = input().strip()
        start = datetime.datetime.strptime(input().strip(), '%d/%m/%Y')
        end = datetime.datetime.strptime(input().strip(), '%d/%m/%Y')
        service = int(input())
        list_customer.append(Customer(name, room, start, end, service))
    list_customer.sort(key= lambda x: x.total, reverse=True)
    for customer in list_customer:
        print(customer)