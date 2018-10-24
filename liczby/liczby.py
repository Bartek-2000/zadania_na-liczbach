x = [1,2,3,4,5]
y=x[0]
for i in range (len(x)-1):
    y=y*x[i+1]
print(y)


z = [4,7,-9,2,-6,10]#17 not 2
q = 0
if z[0] > 0:
    q = z[0]
for i in range (len(z)-1):
    if z[i+1]> 0:
        q= q+z[i+1]
print(q)
    
        

