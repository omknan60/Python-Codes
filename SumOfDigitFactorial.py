num = int(input())

arr = []

for _ in range(num):
    n, m = [int(x) for x in input().split()]
    arr.append([n,m])

def digits(n):
    dig = []
    while n!=0:
        dig.append(n%10)
        n = n//10
    return dig
    
def fact(n, m):
    if ((n-m) == 0):
        return(1)
    elif (n - m) == 1:
        return n
    elif (n - m) == 2:
        return n*(n-1)
    elif (n - m) == 3:
        return n*(n-1)*(n-2)
    else:
        return fact(n, (n+m)//2)*fact((n+m)//2, m)

data = {}
datas = set()

for i in range(10):
    a = digits(i)
    ar = []
    for x in a:
        ar.append(fact(x))
    s1 = sum(ar)
    s2 = digits(s1)
    s3 = sum(s1)
    s4 = digits(s3)
    s = sum(s4)
    if s in datas:
        pass
    else:
        datas.add(s)
        data[s] = i

def sumf(n):
    s = 0
    for x in range(n):
        s += data[x]

for i in arr:
    print(sumf(i[0]))
