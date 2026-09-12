# FD-060 — subpower CRT packets force diverging nonsquarefree energy at the zero frontier

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + ZERO-FRONTIER-SPIKE + SUBPOWER-HOST-FACTOR + CRT-NONSQUAREFREE-PACKET + DIVERGING-LOCAL-OCCUPATION + ROUTE-REFINEMENT`.

`FD-059` shows that a shell spike of height

\[
A_X:=|\mathcal H(X)|,
\qquad
Q_X:=\frac{X}{A_X},
\]

can be transferred deterministically to one nonsquarefree Jordan row at the natural host scale `q\asymp Q_X`. A fixed positive fraction of the spike is enough for a comparable quadratic contribution, while multiplying the host scale by any subpower factor tending to infinity gives first-order transfer without changing the zero-frontier row exponent.

The same subpower slack can do something stronger than improve the accuracy of one twin: it can manufacture a **growing packet of distinct nonsquarefree rows**, all of which retain a fixed fraction of the same physical spike. The packet length can tend to infinity while the host stays at the same power exponent.

Assume along an unbounded sequence that

\[
A_X\to\infty,
\qquad
Q_X\to\infty.
\tag{1}
\]

Then there exist integers

\[
K_X\to\infty
\]

with

\[
K_X\le \log\log Q_X,
\tag{2}
\]

and squarefree hosts `q=q_X` satisfying

\[
\boxed{
2K_XQ_X\le q\le(2K_X+1)Q_X
}
\tag{3}
\]

such that every one of

\[
q+1,q+2,\ldots,q+K_X
\]

is nonsquarefree.

Put

\[
T=qX.
\]

For every fixed Schur-head dimension `D`, all packet rows exceed `D` for sufficiently large `X`, and the exact one-Lipschitz law for the physical shell source gives

\[
\boxed{
U_{T,D}
\ge
\frac{K_X}{\zeta(2)}
\left(\frac{A_X}{2}-1\right)^2.
}
\tag{4}
\]

If

\[
J_q(T):=w(q)A_X^2,
\qquad
w(r):=\frac{J_2(r)}{r^2},
\]

is the squarefree host-row energy, then `w(q)<=1` and therefore

\[
\boxed{
\frac{U_{T,D}}{J_q(T)}
\ge
\frac{K_X}{4\zeta(2)}(1-o(1))
\longrightarrow\infty.
}
\tag{5}
\]

Thus deterministic transfer at the zero-frontier power scale is not limited to producing one comparable nonsquarefree twin. A sufficiently slow subpower displacement of the host scale supports a nonsquarefree packet whose **total quadratic occupation exceeds the host-row energy by an unbounded factor**.

## 1. CRT creates an arbitrarily long nonsquarefree forward packet

Fix an integer `K>=1`. Choose distinct primes

\[
p_1,\ldots,p_K>K
\]

and put

\[
M_K:=\prod_{d=1}^K p_d^2.
\tag{6}
\]

By the Chinese remainder theorem there is a residue class `a_K mod M_K` satisfying

\[
a_K\equiv-d\pmod{p_d^2}
\qquad(1\le d\le K).
\tag{7}
\]

Because `p_d>K>=d`, no `p_d` divides `d`. Hence

\[
\gcd(a_K,M_K)=1.
\tag{8}
\]

Every integer `q\equiv a_K mod M_K` then satisfies

\[
p_d^2\mid q+d
\qquad(1\le d\le K),
\tag{9}
\]

so the whole forward packet `q+1,...,q+K` is nonsquarefree.

The only extra requirement is that the host `q` itself be squarefree. This can be obtained with an elementary fixed-progression count. If `gcd(a,M)=1` and `Y<Z`, then

\[
N_{a,M}(Y,Z)
:=
\#\{Y<n\le Z:n\equiv a\pmod M,\ \mu(n)^2=1\}
\]

satisfies

\[
\boxed{
N_{a,M}(Y,Z)
=
\frac{Z-Y}{M}C_M+O(\sqrt Z),
}
\tag{10}
\]

where

\[
C_M
:=
\sum_{\substack{d\ge1\\(d,M)=1}}
\frac{\mu(d)}{d^2}
=
\frac1{\zeta(2)}
\prod_{p\mid M}(1-p^{-2})^{-1}
\ge
\frac1{\zeta(2)}.
\tag{11}
\]

Indeed, insert `mu(n)^2=sum_(d^2|n) mu(d)`. Condition `(a,M)=1` removes every `d` sharing a prime with `M`; otherwise `d^2` is invertible modulo `M`, and the simultaneous conditions `n=0 mod d^2`, `n=a mod M` specify one class modulo `Md^2`. Summing the resulting interval count gives the main term in (10), an `O(sqrt Z)` accumulation of endpoint errors, and a smaller tail from extending the absolutely convergent `d^{-2}` sum.

This is deliberately stronger than needed as a literature input: the progression modulus will grow only by a diagonal choice below, so no uniform squarefree-distribution theorem is required.

## 2. A diagonal choice lets the packet grow while keeping the host subpower

For the fixed CRT systems above, choose `K_X` to be any maximal integer `K` satisfying

\[
K\le\log\log Q_X,
\qquad
M_K^2K\le Q_X^{1/2}.
\tag{12}
\]

For each fixed `K`, both inequalities eventually hold as `Q_X\to\infty`; consequently

\[
K_X\to\infty.
\tag{13}
\]

Now apply (10) to `a=a_{K_X}`, `M=M_{K_X}` and

\[
Y=2K_XQ_X,
\qquad
Z=(2K_X+1)Q_X.
\tag{14}
\]

The interval has length `Q_X`. By (10)--(12), its squarefree-host count is bounded below by

\[
\frac{Q_X}{M_{K_X}\zeta(2)}
-O(\sqrt{K_XQ_X}).
\tag{15}
\]

The ratio of the main scale to the error scale is

\[
\frac{\sqrt{Q_X}}{M_{K_X}\sqrt{K_X}}
\ge Q_X^{1/4}\to\infty.
\tag{16}
\]

Hence (15) is positive for all sufficiently large members of the sequence. This supplies a squarefree `q` satisfying (3) and the CRT packet conditions (9).

The diagonal condition is intentionally crude. Its role is only to prove coexistence of three properties: `K_X\to\infty`, a squarefree host in the prescribed CRT class, and `K_X=Q_X^{o(1)}`. Optimizing the packet growth rate would not improve the power-exponent conclusion below.

## 3. Every packet row keeps at least half of the physical spike

For `1<=d<=K_X`, let

\[
r_d:=q+d,
\qquad
x_d:=\left\lfloor\frac{T}{r_d}\right\rfloor
=
\left\lfloor\frac{qX}{q+d}\right\rfloor.
\tag{17}
\]

Since `X` is an integer,

\[
X-x_d
=
\left\lceil\frac{dX}{q+d}\right\rceil
\le
\frac{dX}{q}+1.
\tag{18}
\]

Using `d<=K_X` and `q>=2K_XQ_X`, we obtain

\[
X-x_d
\le
\frac{K_XX}{2K_XQ_X}+1
=
\frac{A_X}{2}+1.
\tag{19}
\]

The exact physical coefficient identity from `FD-033` gives

\[
|\Delta\mathcal H(n)|\le1.
\tag{20}
\]

Therefore

\[
|\mathcal H(x_d)|
\ge
|\mathcal H(X)|-|X-x_d|
\ge
\frac{A_X}{2}-1.
\tag{21}
\]

Every `r_d` is nonsquarefree by (9), and every Jordan weight obeys

\[
w(r)\ge\frac1{\zeta(2)}.
\tag{22}
\]

Summing the `K_X` distinct packet rows in the definition of `U_{T,D}` proves (4), and comparison with `J_q(T)<=A_X^2` proves (5).

More generally, replacing `2K_XQ_X` in (14) by `cK_XQ_X` with any fixed `c>1` retains the fraction `1-1/c+o(1)` of the spike across the full packet. The factor `2` merely makes the displayed constants transparent.

## 4. The packet amplification costs no zero-frontier power exponent

Along the false-RH zero-frontier spike sequence used in `FD-054`--`FD-059`, suppose

\[
A_X=X^{\Theta+o(1)},
\qquad
\frac12<\Theta<1.
\tag{23}
\]

Then

\[
Q_X=X^{1-\Theta+o(1)}.
\tag{24}
\]

Equation (2) gives `K_X=X^{o(1)}`, so (3) implies

\[
q=X^{1-\Theta+o(1)}.
\tag{25}
\]

Since `T=qX`, exactly as in `FD-059`,

\[
\boxed{
q=T^{\alpha_\Theta+o(1)},
\qquad
\alpha_\Theta:=\frac{1-\Theta}{2-\Theta}.
}
\tag{26}
\]

Thus the packet length can diverge while the row coordinate remains at the same power exponent as the single critical-scale twin. The distinction is subpower: here

\[
\frac{qA_X}{X}\asymp K_X\to\infty,
\tag{27}
\]

so the construction lies on the deterministic supercritical side of the exact host-scale threshold even though it is invisible at the exponent level.

This gives a sharper interpretation of the subpower first-order variant in `FD-059`. Subpower slack above `X/A_X` can be spent either on making one endpoint asymptotically identical to the spike or on creating **more and more nonsquarefree endpoints that each retain a fixed fraction**. The latter yields the unbounded local occupation factor (5).

## 5. What this does and does not buy globally

The packet does not prove a fixed lower bound for

\[
\frac{U_{T,D}}{E_{T,D}}.
\]

Equation (5) compares the nonsquarefree packet with the energy of the selected squarefree host row, not with all remaining Jordan rows. Unrelated low rows may still contribute much more to `E_{T,D}`. The global occupation gate isolated in `FD-037`--`FD-053` therefore remains open.

There is also a deterministic reason why this argument does not penetrate the below-critical regime. If one asks the one-Lipschitz law alone to preserve a fixed fraction `rho` of a spike simultaneously over offsets `1<=d<=K`, the worst packet displacement is of order

\[
\frac{KX}{q}.
\]

To make this at most `(1-rho)A_X` requires, at the level of this deterministic mechanism,

\[
K\lesssim (1-\rho)\frac{qA_X}{X}.
\tag{28}
\]

At a genuinely constant critical ratio `qA_X/X=O(1)`, bounded increments can therefore guarantee only a bounded packet length; a growing packet necessarily consumes a growing supercritical factor unless additional cancellation in the actual source is used. This is consistent with `FD-059`: the source-regularity bill starts when one tries to cross below `X/A_X`, not when one refines what can be obtained above it.

The number-theoretic ingredients themselves are classical. Chinese-remainder constructions of long runs of nonsquarefree integers and squarefree counting in arithmetic progressions are not claimed as new. A targeted prior-art audit found the expected squarefree-progression literature, but no result matching the present coupling of a growing CRT packet to the reciprocal-floor shell transfer and Jordan occupation at the zero-frontier exponent. Since (10) is proved directly at the weak strength needed here, no new external theorem is load-bearing and `SOURCES.md` remains unchanged.