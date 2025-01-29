f=open('perepis.txt','r')
g=0
a=(int(input("1 or 2")))
if a==1:
    for i in f:
        L=i.split('.')
        v=int(L[2])
        if v<1978:
            print(i)
            g+=1
    print(g)
elif a==2:
    k=int(input("diapozon ot"))
    k0=int(input("diapozon do"))
    for i in f:
        L=i.split('.')
        v=int(L[2])
        if v>=k and v<=k0:
            print(i)
