num = input()
# k=len(num)
count = 0
for i in range(0, len(num)):
    if int(num[i]) % 2 == 0:
        count = count + 1
print(count, end=" ")
for j in range(0, len(num) - 1):
    if int(num[j]) % 2 == 0:
        count = count - 1
    print(count, end=" ")
