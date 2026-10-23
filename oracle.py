import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def boxes(n, b):
    k = -(-n//b)
    return f"The {pl(n,' shirt',' shirts')} at {pl(b,' shirt',' shirts')} a box {v(n,'takes','take')} {pl(k,' box',' boxes')}, the last box holding {pl(n-(k-1)*b,' shirt',' shirts')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' shirt',' shirts')} at {pl(w,' shirt',' shirts')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' shirt',' shirts')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pb = (2*cc + n)//(2*n)
    return f"The {pl(b,' box',' boxes')} at ${m(pc)} a box {v(b,'comes','come')} to ${m(cc)}, ${m(pb)} a shirt."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' shirt',' shirts')} at {pl(pm,' shirt',' shirts')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(783)
R = random.randint
cases = [
 dict(fn="boxes", args=["345","25"], expect=boxes(345,25)),
 dict(fn="weeks", args=["345","45"], expect=weeks(345,45)),
 dict(fn="cost", args=["14","118.75","345"], expect=cost(14,11875,345)),
 dict(fn="time", args=["345","6"], expect=time_(345,6)),
 dict(fn="boxes", args=["1","1"], expect=boxes(1,1)),
 dict(fn="boxes", args=["325","25"], expect=boxes(325,25)),
 dict(fn="boxes", args=["1000000","1000"], expect=boxes(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["315","45"], expect=weeks(315,45)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="boxes", args=[str(n),str(b)], expect=boxes(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["boxes",["0","25"]],["boxes",["1000001","12"]],["boxes",["2.5","12"]],["boxes",["345","0"]],["boxes",["345","1001"]],
 ["weeks",["0","30"]],["weeks",["345","0"]],["weeks",["345","100001"]],["weeks",["345","1.5"]],["weeks",["1000001","30"]],
 ["cost",["0","118.75","345"]],["cost",["100001","118.75","345"]],["cost",["14","0","345"]],["cost",["14","118.755","345"]],["cost",["14","118.75","0"]],
 ["time",["0","6"]],["time",["345","0"]],["time",["345","101"]],["time",["345","6.5"]],["time",["1000001","5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
