class Calculator:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def add(self):
        return self.first_num + self.second_num

    def subtract(self):
        return self.first_num - self.second_num

    def multiply(self):
        return self.first_num * self.second_num

    def divide(self):
        return self.first_num / self.second_num

    def choice(self, operator):
        if operator == 1:
            return f" {first_num} + {second_num} = {self.add()}"
        elif operator == 2:
            return f" {first_num} - {second_num} = {self.subtract()}"
        elif operator == 3:
            return f" {first_num} * {second_num} = {self.multiply()}"
        elif operator == 4:
            return f" {first_num} / {second_num} = {self.divide()}"
        else:
            return "Invalid Choice!"


while True:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))
    operator = int(input("Choose operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n>> "))
    calc = Calculator(first_num, second_num)
    result = calc.choice(operator)
    print(result)
    another_operation = input("Do you want another operation? ")
    if another_operation.lower() == "yes":
        continue
    else:
        break
