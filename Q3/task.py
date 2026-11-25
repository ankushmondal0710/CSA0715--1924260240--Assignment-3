import math
for added in (0,50,200):
    r=(50+added)/1000
    for n in (80,8):
        print(added,n,"objects", "sequential",2*(n+1)*r,"persistent",(n+2)*r,"pipeline",3*r,"parallel",(2+2*math.ceil(n/6))*r)
