import csv
import os
def bonus(salary, rate=0.1, *extras, **options):
    total = salary * rate + sum(extras)
    if "cap" in options:
        total = min(total, options["cap"])
    return total
class InvalidSalaryError(Exception):
    pass
class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary
    def annual_salary(self):
        return self.salary * 12
    def get_details(self):
        return self.name, self.salary
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    def get_details(self):
        return self.name, self.salary, self.team_size
csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "employees.csv")
with open(csv_path, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    if not reader.fieldnames:
        raise ValueError("The CSV file is empty or has no header.")
    reader.fieldnames = [
        name.strip().lower() for name in reader.fieldnames
    ]
    print("CSV file:", csv_path)
    print("CSV columns:", reader.fieldnames)
    if "salary" not in reader.fieldnames:
        raise ValueError(
            "Missing 'salary' column. Check the CSV header printed above."
        )
    employees = list(reader)
for emp in employees:
    emp["salary"] = int(emp["salary"])
names = [emp["name"] for emp in employees if emp["salary"] > 50000]
print("Above 50000:", names)
salaries = list(map(lambda x: x * 1.1,
                    [emp["salary"] for emp in employees]))
print("After 10% raise:", salaries)
chennai = list(filter(
    lambda emp: emp["city"].strip().lower() == "chennai",
    employees
))
print("Chennai:", [emp["name"] for emp in chennai])
for emp in employees:
    if emp["salary"] == 0:
        continue
    if emp["salary"] > 85000:
        break
    print("Processing:", emp["name"])
print("Bonus:", bonus(30000, 0.1, 500, cap=3000))
e = Employee("Arun", 30000)
print("Annual salary:", e.annual_salary())
m = Manager("Priya", 60000, 5)
print("Manager:", m.get_details())
try:
    e = Employee("Test", -500)
except InvalidSalaryError as error:
    print("Error:", error)
finally:
    print("Transaction finished")
