x = ["Ala","Olek","Michał","Konstanty","Mikołaj"]
y = (len(x)%2)
if y != 0:
    z = len(x)/2 - 0.5 - 0.0

else:
    z = len(x)/2 - 1



j = x[::int(z)]
d = x[int(z+1)::]
print(j)
print(d)