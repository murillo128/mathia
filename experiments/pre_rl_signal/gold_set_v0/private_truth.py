from __future__ import annotations

import math


def _mul(a: int, n: int) -> list[int]: return [(a*x) % n for x in range(n)]
def _aff(a: int, b: int, n: int) -> list[int]: return [(a*x+b) % n for x in range(n)]
def _perm(v: list[object], n: int) -> bool: return len(v) == n and len(set(v)) == n
def _collision(v: list[object]) -> list[int] | None:
    seen: dict[object,int] = {}
    for x,y in enumerate(v):
        if y in seen: return [seen[y],x]
        seen[y] = x
    return None

def _sols(a: int, b: int, n: int) -> list[int]: return [x for x in range(n) if (a*x-b) % n == 0]
def _all_cycles(v: list[int]) -> bool:
    for start in range(len(v)):
        path=[]; pos={}; x=start
        while x not in pos:
            pos[x]=len(path); path.append(x); x=v[x]
        if start not in path[pos[x]:]: return False
    return True

def _crt_solutions(rm: int, rn: int, m: int, n: int) -> list[int]: return [x for x in range(m*n) if x%m==rm and x%n==rn]


def build_private() -> dict[str, object]:
    answers: dict[str, dict[str, object]] = {}

    for i,n,a in [(1,15,4),(2,15,5),(3,16,3),(4,16,6),(5,21,8),(6,21,7),(7,35,12),(8,35,10)]:
        b=(i*3+1)%n; target=(i*5+2)%n; vals=_mul(a,n); unit=math.gcd(a,n)==1
        answers[f"R{i:02d}"]={"T1":_perm(vals,n),"T2":_perm(_aff(a,b,n),n),"T3":len(_sols(a,target,n)),"T4":_all_cycles(vals) if unit else _collision(vals)}

    for i,a,b,q in [(9,107,35,3),(10,91,26,-2),(11,84,30,4),(12,221,52,5)]:
        q2=q+2; c2,d2=b,a-q2*b; q3=-3; e,f=d2,c2-q3*d2
        answers[f"G{i:02d}"]={"T1":math.gcd(a,b)==math.gcd(c2,d2),"T2":math.gcd(c2,d2),"T3":math.gcd(e,f),"T4":False}

    for i,m,n in [(13,3,5),(14,4,9),(15,5,8),(16,4,6)]:
        cop=math.gcd(m,n)==1; x0=(7*i+3)%(m*n); rm=x0%m; rn=x0%n
        vals=[(x%m,x%n) for x in range(m*n)]; compatible=_crt_solutions(rm,rn,m,n)
        if cop:
            answers[f"C{i:02d}"]={"T1":len(set(vals))==m*n,"T2":len(compatible),"T3":compatible[0],"T4":False}
        else:
            answers[f"C{i:02d}"]={"T1":len(set(vals))==m*n,"T2":len(compatible),"T3":_collision(vals),"T4":len(_crt_solutions(0,1,m,n))}

    for i,n,a,b,c,d in [(17,12,5,2,7,0),(18,15,6,5,4,1),(19,20,3,0,7,0),(20,18,5,1,6,4)]:
        fv=_aff(a,b,n); gv=_aff(c,d,n); comp=[gv[fv[x]] for x in range(n)]
        answers[f"M{i:02d}"]={"T1":_perm(fv,n),"T2":_perm(gv,n),"T3":_perm(comp,n),"T4":False}

    return {"version":"gold-set-v0","answers":answers}
