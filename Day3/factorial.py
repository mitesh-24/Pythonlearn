def fact(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def fact2(n):
    if n==0 or n<0:
        return 1
    return n * fact(n-1)

print(fact2(int(input("Enter : "))))