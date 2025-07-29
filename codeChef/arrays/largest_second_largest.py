t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    
    if n < 2:
        print(a)
    else:
        maxi = a[0] + a[1]
        for i in range(1, n-1):
            next = a[i] + a[i+1]
            if next > maxi:
                maxi = next
        print(maxi)