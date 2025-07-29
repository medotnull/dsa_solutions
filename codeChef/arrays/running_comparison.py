t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Your code goes here
    #on ith day A ran a meter and B ran b meter
    count = 0
    for x,y in zip(a,b):
        if 2*x < y or 2*y < x:
            continue
        else:
            count+=1
    print(count)
    t -= 1