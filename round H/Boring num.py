def digit(n):
    l=[]
    count=0
    while(n>0):
        l.append(n%10)
        n=n//10
        count+=1
    l.append(count)
    l.reverse()
    return l
def f(x):
    if(x==0):
        return 0
    l=digit(x)
    count=l[0]
    l.pop(0)
    if(count==1):
        re=0
    else:
        re=pow(5,count)
        re-=1
        re=re//4
        re-=1
    z=len(l)
    idx=1
    for i in range(z):
        if(i%2==0):
            if(l[i]%2):
                ok=(l[i])//2
                re+=(ok)*(pow(5,z-i-1))
            else:
                ok=l[i]//2
                re+=(ok)*(pow(5,z-i-1))
                idx=0
                break
        else:
            if(l[i]%2==0):
                ok=(l[i]+1)//2
                re+=(ok)*(pow(5,z-i-1))
            else:
                ok=(l[i]+1)//2
                re+=(ok)*(pow(5,z-i-1))
                idx=0
                break
    re+=idx
    return re
t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    print("Case #"+str(i+1)+': '+str(f(r)-f(l-1)))
