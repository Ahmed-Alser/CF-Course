class Calculator:
    def __init__(self, num_1, num_2):
        self.a = num_1
        self.b = num_2

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def choice(self, operator):
        if operator == 1:
            return f" {self.a} + {self.b} = {Calculator.add(self)}"
        elif operator == 2:
            return f" {self.a} - {self.b} = {Calculator.subtract(self)}"
        elif operator == 3:
            return f" {self.a} * {self.b} = {Calculator.multiply(self)}"
        elif operator == 4:
            return f" {self.a} / {self.b} = {Calculator.divide(self)}"
        else:
            print("Invalid Choice!")


while True:
    num_one = int(input("Enter first number: "))
    num_two = int(input("Enter second number: "))
    operator = int(input("Choose operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n>> "))
    calc = Calculator(num_one, num_two)
    result = calc.choice(operator)
    print(result)
    another_operation = input("Do you want another operation? ")
    if another_operation.lower() == "yes":
        continue
    else:
        break
