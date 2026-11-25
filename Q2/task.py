def simulate(losses, ssthresh=16, reno=True):
    cwnd, trace = 1, []
    for rtt in range(1,21):
        trace.append(cwnd)
        if rtt in losses:
            ssthresh=max(cwnd//2,2)
            cwnd=ssthresh if reno else 1
        elif cwnd<ssthresh:
            cwnd=min(2*cwnd,ssthresh)
        else:
            cwnd+=1
    return trace
for label, reno in (("Reno",True),("Tahoe",False)):
    tr=simulate({8,14},reno=reno)
    print(label, tr, "segments sent",sum(tr),"delivered model",sum(tr)-2)
print("Extra Reno",sum(simulate({8,14}))-sum(simulate({8,14},reno=False)))
try:
    import matplotlib.pyplot as plt
    for label,r in (("Reno",True),("Tahoe",False)):
        plt.plot(range(1,21),simulate({8,14},reno=r),marker="o",label=label)
    plt.xlabel("RTT"); plt.ylabel("Window (segments)"); plt.legend(); plt.savefig("window.png")
except ImportError: print("Install matplotlib for graph")
