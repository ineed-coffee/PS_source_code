N = int(input().strip())

def Fib(N):
    if N==0:
        return 0
    elif N==1:
        return 1
    else:
        a=[0,1]+[0]*(N-1)
        for i in range(2,N+1):
            a[i]=a[i-1]+a[i-2]
        return a[-1]

print(Fib(N))
