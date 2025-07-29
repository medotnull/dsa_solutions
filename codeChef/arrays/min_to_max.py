t = int(input())

while t > 0:
    n = int(input()) #len of array
    a = list(map(int, input().split())) #array
    # Your code goes here
    t -= 1
    minimum = a[0]
    for i in a:
        if i <= 1:
            print(0)
        minimum = min(minimum, i)
        i+=1
    print(minimum)