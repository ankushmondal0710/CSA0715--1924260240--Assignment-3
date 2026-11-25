import socket,threading,hashlib,time,random
payload=b"Synthetic X-ray data "*5000
chat=b"Doctor: appointment confirmed"
server=socket.socket(); server.bind(("127.0.0.1",0)); server.listen(2)
def receive():
    for label,expected in (("file",payload),("chat",chat)):
        c,_=server.accept()
        with c:
            chunks=[]
            while True:
                b=c.recv(4096)
                if not b: break
                chunks.append(b)
            data=b"".join(chunks)
            print(label,len(data),"SHA256 match",hashlib.sha256(data).digest()==hashlib.sha256(expected).digest())
    server.close()
th=threading.Thread(target=receive); th.start(); start=time.perf_counter()
for data in (payload,chat):
    with socket.create_connection(server.getsockname()) as c: c.sendall(data)
th.join(); print("Local elapsed seconds",round(time.perf_counter()-start,6))
for rtt in (.1,.3):
    for loss in (0,.05):
        rng=random.Random(7); attempts=0
        for _ in range((len(payload)+1459)//1460):
            attempts+=1
            while rng.random()<loss: attempts+=1
        print("Stop-and-wait model",rtt,loss,"attempts",attempts,"seconds",round(attempts*rtt,2),"delivered bytes",len(payload))
