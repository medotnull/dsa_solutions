t = int(input())

while t > 0:
    n = int(input()) #len of array
    a = list(map(int, input().split())) #array
    # Your code goes here
    minimum = min(a) #got min value
    count = 0
    for i in a:
        if i > minimum:
            count+=1
    print(count)
    t -= 1