def sint(a,q):
    b=a.split()
    x=""
    if b[0]=='MIX':
        x='MX'
        for i in b:
            if i !=b[0]:
                if i.isnumeric():
                    x+=q[int(i)-1]
                else:
                    x+=i
        x+='XM'
    if b[0]=='WATER':
        x='WT'
        for i in b:
            if i !=b[0]:
                if i.isnumeric():
                    i = int(i)
                    x=x+q[i-1]
                else:
                    x+=i
        x+='TW'
    if b[0]=='DUST':
        x='DT'
        for i in b:
            if i !=b[0]:
                if i.isnumeric():
                    x+=q[int(i)-1]
                else:
                    x+=i
        x+='TD'
    if b[0]=='FIRE':
        x='FR'
        for i in b:
            if i !=b[0]:
                if i.isnumeric():
                    x+=q[int(i)-1]
                else:
                    x+=i
        x+='RF'
    return x
for n in range(1,11):
    otv=open('output'+str(n)+'.txt').read()
    f=open('input'+str(n)+'.txt')
    t=f.read().split('\n')
    q=[0 for i in range(len(t))]
    for j in range(len(t)):
        q[j]=sint(t[j],q)
    print(otv==q[-1])
