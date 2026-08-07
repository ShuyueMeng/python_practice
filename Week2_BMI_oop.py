class bmi:

    def __init__(self,height,weight):
        self.height=height
        self.weight=weight
        self.bmi=weight / height ** 2
    def display(self):
        print(f'your BMI number is:{self.bmi}')

def main():
    height = float(input("Please enter your height(m):"))
    weight = float(input("Please enter your weight(kg):"))
    user_bmi=bmi(height,weight)
    user_bmi.display()

if __name__ == "__main__":
    main()