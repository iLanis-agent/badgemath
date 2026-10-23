import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def packs(n, b):
    k = -(-n//b)
    return f"The {pl(n,' attendee',' attendees')} at {pl(b,' badge',' badges')} a pack {v(n,'takes','take')} {pl(k,' pack',' packs')}, the last pack holding {pl(n-(k-1)*b,' badge',' badges')}."
def lanyard(n, b):
    k = -(-n//b)
    return f"The {pl(n,' attendee',' attendees')} at {pl(b,' lanyard',' lanyards')} a bag {v(n,'takes','take')} {pl(k,' bag',' bags')}, leaving {pl(k*b-n,' lanyard',' lanyards')} spare."
def cost(b, pc, n):
    cc = b*pc
    pa = (2*cc + n)//(2*n)
    return f"The {pl(b,' pack',' packs')} at ${m(pc)} a pack {v(b,'comes','come')} to ${m(cc)}, ${m(pa)} an attendee."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' badge',' badges')} at {pl(pm,' badge',' badges')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(779)
R = random.randint
cases = [
 dict(fn="packs", args=["240","25"], expect=packs(240,25)),
 dict(fn="lanyard", args=["240","50"], expect=lanyard(240,50)),
 dict(fn="cost", args=["10","12.75","240"], expect=cost(10,1275,240)),
 dict(fn="time", args=["240","8"], expect=time_(240,8)),
 dict(fn="packs", args=["1","1"], expect=packs(1,1)),
 dict(fn="packs", args=["250","25"], expect=packs(250,25)),
 dict(fn="packs", args=["1000000","1000"], expect=packs(1000000,1000)),
 dict(fn="lanyard", args=["1","1"], expect=lanyard(1,1)),
 dict(fn="lanyard", args=["200","50"], expect=lanyard(200,50)),
 dict(fn="lanyard", args=["1000000","1000"], expect=lanyard(1000000,1000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="packs", args=[str(n),str(b)], expect=packs(n,b)))
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="lanyard", args=[str(n),str(b)], expect=lanyard(n,b)))
for _ in range(24):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["packs",["0","25"]],["packs",["1000001","25"]],["packs",["2.5","25"]],["packs",["240","0"]],["packs",["240","1001"]],
 ["lanyard",["0","50"]],["lanyard",["240","0"]],["lanyard",["240","1001"]],["lanyard",["240","1.5"]],["lanyard",["1000001","50"]],
 ["cost",["0","12.75","240"]],["cost",["100001","12.75","240"]],["cost",["10","0","240"]],["cost",["10","12.755","240"]],["cost",["10","12.75","0"]],
 ["time",["0","8"]],["time",["240","0"]],["time",["240","101"]],["time",["240","6.5"]],["time",["1000001","8"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
