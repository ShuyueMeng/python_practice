def fib(num):
    a = 0
    b = 1
    list_1=[a,b]
    for i in range(num-2):
        new=a+b
        list_1.append(new)
        a=b
        b=new
    print(list)

if __name__ == "__main__":
    num=int(input("Please Enter a Number:"))
    fib(num)
