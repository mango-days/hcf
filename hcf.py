def hcf(a,b):
    if (a==0) and (b==0): return 0
    if (a==0): return b
    if (b==0): return a
    if (a<0) and (b<0): print("error")
    if (a==b): return a
    if (a>b): return hcf(a-b,b)
    if (a<b): return hcf(a,b-a)
    
a=12
b=15
print(hcf(a,b))