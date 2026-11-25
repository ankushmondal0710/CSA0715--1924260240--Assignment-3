import random,heapq
from collections import deque
def mm1(lam,mu):
    if lam>=mu: return None
    rho=lam/mu
    return rho,rho/(1-rho),1/(mu-lam)
for lam in (500,800,900,950,990,1000,1100):
    r=mm1(lam,1000)
    print(lam, "unstable" if r is None else (round(r[0],2),round(r[1],1),round(r[2]*1000,1)))
def queue(priority,backup):
    rng=random.Random(7); arrivals=[]
    for rate,kind in ((200,0),(backup,1)):
        t=0
        while True:
            t+=rng.expovariate(rate)
            if t>10: break
            arrivals.append((t,kind))
    arrivals.sort(); waiting=[]; i=0; now=0; delays=[]
    while i<len(arrivals) or waiting:
        if not waiting: now=max(now,arrivals[i][0])
        while i<len(arrivals) and arrivals[i][0]<=now:
            t,k=arrivals[i]; heapq.heappush(waiting,(k if priority else 0,t,k)); i+=1
        _,t,k=heapq.heappop(waiting); now+=rng.expovariate(1000)
        if k==0: delays.append(now-t)
    return sum(delays)/len(delays)*1000
for b in (750,1000,250):
    print("Backup",b,"FIFO video ms",round(queue(False,b),2),"Priority video ms",round(queue(True,b),2))
try:
    import matplotlib.pyplot as plt
    x=list(range(0,1000,10)); plt.plot(x,[1000/(1000-i) for i in x]); plt.xlabel("Load pkt/s"); plt.ylabel("Delay ms"); plt.savefig("delay.png")
except ImportError: pass
