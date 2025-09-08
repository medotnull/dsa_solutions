n = int(input())
myList = [int(_) for _ in input().split()]

for i in range(n-1):
  for j in range(n-i-1):
    if myList[j] > myList[j+1]:
      myList[j], myList[j+1] = myList[j+1], myList[j]
print(myList)