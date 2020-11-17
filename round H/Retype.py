t=int(input())
for i in range(t):
    n,k,s=map(int,input().split())
    re=min(n+k,(k-s)+(n-s)+k)
    print('Case #'+str(i+1)+': '+str(re))
