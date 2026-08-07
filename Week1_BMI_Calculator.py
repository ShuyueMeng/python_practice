def bmi_cal(height,weight):
    return weight / height ** 2

def main():
    height = float(input("Please enter your height(m):"))
    weight = float(input("Please enter your weight(kg):"))
    print(f'Your BMI is: {bmi_cal(height, weight)}')



if __name__ == "__main__":
    main()