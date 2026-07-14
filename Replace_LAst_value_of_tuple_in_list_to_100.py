l=[(10,20,30),(40,50,60),(70,80,90)]
res=[]
for t in l:
    t=t[:-1]+(100,)
    res.append(t)
print(res)