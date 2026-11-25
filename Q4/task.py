import time
SERVERS={"root":{"in.":"tld-in","com.":"tld-com"},"tld-in":{"ac.in.":"ns-ac"},"tld-com":{"example.com.":"ns-example"},"ns-ac":{"simats.ac.in.":"ns-simats"},"ns-simats":{"results.simats.ac.in.":"10.20.30.40"},"ns-example":{"www.example.com.":"93.184.216.34"}}
cache={}
def resolve(name):
    if name in cache:
        return cache[name],0
    server,queries="root",0
    while True:
        queries+=1
        matches=[k for k in SERVERS[server] if name.endswith(k)]
        if not matches: return "NXDOMAIN",queries
        value=SERVERS[server][max(matches,key=len)]
        if any(c.isdigit() for c in value):
            cache[name]=value
            return value,queries
        server=value
for n in ("results.simats.ac.in.","www.example.com.","results.simats.ac.in."):
    ip,q=resolve(n)
    print(f"{n:<24} {ip:<15} queries sent: {q}")
expiry={}
def resolve_ttl(name,ttl=300):
    if time.monotonic()>=expiry.get(name,0):
        cache.pop(name,None)
    ip,q=resolve(name)
    if q and ip!="NXDOMAIN": expiry[name]=time.monotonic()+ttl
    return ip,q
print("TTL demo",resolve_ttl("results.simats.ac.in."),resolve_ttl("results.simats.ac.in."))
