def largest(arr,n):
    max = arr[0]
    for i in range(1,n):
        if arr[i] > max:
            max = arr[i]
    return max
if __name__ == "__main__":
    n = int(input("number of array elements: "))
    arr = []
    for i in range(n):
        x = int(input())
        arr.append(x)
    print("max :", largest(arr,n))