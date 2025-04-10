
#A beginner-friendly Python project demonstrating object-oriented programming (OOP) by modeling utility bills. Includes water, natural gas, and electricity bills, each with its own calculation method based on specific units.

class BaseBill:
    def __init__(self, value_add_task: int, amount: float):
        self.value_add_task = value_add_task
        self.amount = amount

    def calculate_bill(self):
        print('The calculation function has been executed.')

class WaterBill(BaseBill):
    def __init__(self, value_add_task: int, amount: float, mill: int):
        super().__init__(value_add_task, amount)
        self.mill = mill

    def calculate_bill(self):
        return self.value_add_task * self.amount * self.mill

class NaturalGasBill(BaseBill):
    def __init__(self, value_add_task: int, amount: float, m3: int):
        super().__init__(value_add_task, amount)
        self.m3 = m3

    def calculate_bill(self):
        return self.value_add_task * self.amount * self.m3

class ElectricityBill(BaseBill):
    def __init__(self, value_add_task: int, amount: float, kw: int):
        super().__init__(value_add_task, amount)
        self.kw = kw

    def calculate_bill(self):
        return self.value_add_task * self.amount * self.kw

water = WaterBill(value_add_task=10, amount=1.5, mill=100)
gas = NaturalGasBill(value_add_task=8, amount=2.0, m3=50)
electric = ElectricityBill(value_add_task=12, amount=0.75, kw=120)

print(f'Water bill:', water.calculate_bill()),
print(f'Natural gas bill:', gas.calculate_bill()),
print(f'Electricity bill:', electric.calculate_bill())