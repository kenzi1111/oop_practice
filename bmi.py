class Adult:
    def __init__(self,height,weight,bmi):
        self.height = height
        self.weight = weight
        self.bmi = weight/height**2

    def rule(self):
        if not (10 <= self.bmi <=40):
             raise ValueError(f"サイズオーバーです")
        
        bmi = round(self.bmi,2)


tanaka_bmi = Adult(height=180.0, weight=67.0)
    
print(tanaka_bmi)