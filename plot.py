import math
import matplotlib.pyplot as plt
def txy(G,nu,b,x,y):
    D=G*b/(2*math.pi*(1-nu))
    return  D*x*((x*x-y*y)/(x*x+y*y)**2)
x=[]
f=[]    
G=200
nu=0.33
b=0.1
y=10
for xx in range(-10,11):
    x.append(xx)
    f.append(b*txy(G,nu,b,xx,5))
#print(txy(G,nu,b,x,5))
for i in range(len(x)):
    print(str(x[i])+ ""+str(f[i]))
plt.plot(x,f)
plt.show().animate
