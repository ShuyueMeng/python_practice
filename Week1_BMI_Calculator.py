def main(height,weight):
    return weight / height ** 2


if __name__ == "__main__":
    height=float(input("Please enter your height(m):"))
    weight = float(input("Please enter your weight(kg):"))
    print(f'Your BMI is: {main(height,weight)}')