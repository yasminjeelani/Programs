def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("factorial of a number " , num , "is : " , factorial(num))