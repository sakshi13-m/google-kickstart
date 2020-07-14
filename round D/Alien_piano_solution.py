t=int(input())
for j in range(1,t+1):
    k=int(input())
    a=list(map(int,input().split()))
    p=0
    n=0
    r=0
    for i in range(k-1):
        if(a[i+1]-a[i]>0):
            p+=1
            n=0
        if(a[i+1]-a[i]<0):
            n+=1
            p=0
        if(p>3 or n>3):
            r+=1
            p=0
            n=0
        
    print('Case #'+str(j)+': '+str(r))
