n=0
for x in range (245690,245756+1):
    m = []
    n += 1
    for i in range(2,x//2+1):
        if x%i==0:
            m.append(i)
        if len(m)>0:
            break
    if len(m)==0:
        print(n,x)
