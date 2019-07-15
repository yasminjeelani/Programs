
def _sum(arr,n):
    return sum(arr)

n = int(input("Enter number of array elements: "))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

if __name__ == '__main__':
   y =  _sum(arr,n)
   print("sum of array element: " ,y)



