
def selection_sort(myList):
  n = len(myList)
  for i in range(n-1):
    minIndex = i
    for j in range(i+1, n):
      if myList[j] < myList[minIndex]:
        minIndex = j
    if minIndex != i:
      myList[i], myList[minIndex] = myList[minIndex], myList[i]

  return myList

# Example:
arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))  # [11, 12, 22, 25, 64]