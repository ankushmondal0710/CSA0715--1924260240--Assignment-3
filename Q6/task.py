for rtt in (100,150,300):
    print("RTT",rtt,"ms")
    for name,n in (("TCP TLS1.2",3),("TCP TLS1.3",2),("QUIC first",1),("QUIC resumed",0)):
        print(name,n*rtt,"ms before request")
