from sys import stdin, setrecursionlimit, maxsize
from math import ceil,floor,gcd


setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)] + [0]

s = [0] * (n*4)

def q(i,node,nL,nR):
    if nL==nR:
        return nL
    m = (nL+nR)//2
    if i>s[node*2]:
        i-=s[node*2]
        return q(i,node*2+1,m+1,nR)
    return q(i,node*2,nL,m)

def u(i,v,node,nL,nR):
    if i<nL or i>nR:
        return s[node]
    if nL==nR:
        s[node] += v
        return s[node]
    m = (nL+nR)//2
    s[node] = u(i,v,node*2,nL,m)+u(i,v,node*2+1,m+1,nR)
    return s[node]

for i in range(1,n+1):
    u(i,1,1,1,n)

res = [0]*(n+1)
for i in range(1,n+1):
    ret = q(a[i-1]+1,1,1,n)
    res[ret]=i
    u(ret,-1,1,1,n)

for i in range(n):
    print(res[i+1])