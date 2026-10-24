class Employee:
    def calculate_salary(self):
        return 70000

class Manager:
    def calculate_salary(self):
        return 80000

class Developer:
    def calculate_salary(self):
        return 90000

employees = [Employee(), Manager(), Developer()]

for employee in employees:
    print(
        employee.__class__.__name__,
        employee.calculate_salary()
    )


class PDFReport:
    def generate(self):
        print("Generating PDF report")


class ExcelReport:
    def generate(self):
        print("Generating Excel report")


class HTMLReport:
    def generate(self):
        print("Generating HTML report")


def create_report(report):
    report.generate()


reports = [
    PDFReport(),
    ExcelReport(),
    HTMLReport()
]

for report in reports:
    create_report(report)


from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(Payment):
    def pay(self, amount):
        return f"UPI payment: Rs. {amount}"


class CardPayment(Payment):
    def pay(self, amount):
        return f"Card payment: Rs. {amount}"


class CashPayment(Payment):
    def pay(self, amount):
        return f"Cash payment: Rs. {amount}"


def checkout(payment_method, amount):
    print(payment_method.pay(amount))


checkout(UpiPayment(), 700)
checkout(CardPayment(), 2000)
checkout(CashPayment(), 300)
      

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(20, 40)
v2 = Vector(7, 14)

print(v1 + v2)


from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def display(self):
        print(
            f"{self.name}: Rs. {self.calculate_salary():,.2f}"
        )


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus=0):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours * self.hourly_rate


class CommissionEmployee(Employee):
    def __init__(self, name, base_salary, sales, rate):
        super().__init__(name)
        self.base_salary = base_salary
        self.sales = sales
        self.rate = rate

    def calculate_salary(self):
        return self.base_salary + self.sales * self.rate


employees = [
    FullTimeEmployee("Sanjivani", 80000, 7000),
    PartTimeEmployee("Khushi", 90, 400),
    CommissionEmployee("Vishwa", 30000, 200000, 0.04)
]

for employee in employees:
    employee.display()


























