from polymorphism import (
    FullTimeEmployee,
    PartTimeEmployee,
    CommissionEmployee
)

employees = [
    FullTimeEmployee("Sanjivani", 80000, 7000),
    PartTimeEmployee("Khushi", 90, 400),
    CommissionEmployee("Vishwa", 30000, 200000, 0.04)
]

for employee in employees:
    employee.display()




























