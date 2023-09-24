class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight / (self.height**2)


tanaka_bmi = BMI(height=1.80, weight=67.0)

result = round(tanaka_bmi.calculate_bmi(),2)

print(result)
