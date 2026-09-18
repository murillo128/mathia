# AF-411 — every fixed Euler confluent order is positive in the right tail

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FINITE-ORDER-POSITIVE-GATE`, `CONFLUENT-TOTAL-POSITIVITY`, `RIGHT-TAIL-RIGIDITY`, `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f(t):=-\log(1-e^{-e^t}),
\qquad
H_m(f;t):=(-1)^{\binom m2}
\det\!\left[f^{(i+j)}(t)\right]_{i,j=0}^{m-1}.
\tag{1}
\]

For every fixed integer `m>=1` there exists a finite threshold `T_m` such that

\[
\boxed{
H_m(f;t)>0
\qquad\text{for every }t\ge T_m.
}
\tag{2}
\]

Equivalently, for every fixed finite order `r` there is `T_r^*` such that the complete confluent flag

\[
H_1(f;t),\ldots,H_r(f;t)
\tag{3}
\]

is strictly positive for every `t>=T_r^*`.

The mechanism is simple but structurally useful. Writing `x=e^t`, the full Euler logarithm has the exact harmonic expansion

\[
f(t)=\sum_{n\ge1}\frac{e^{-nx}}n
=e^{-x}+\sum_{n\ge2}\frac{e^{-nx}}n.
\tag{4}
\]

At any **fixed** confluent order, the first harmonic `e^{-x}` has an explicit strictly positive Hankel--Toda determinant, while every term containing at least one higher harmonic gains an extra factor `e^{-x}`. Polynomial losses from differentiation cannot defeat that exponential gap as `x\to\infty`.

Consequently, the all-order obstruction of AF-217 cannot be witnessed at one fixed finite confluent order arbitrarily far into the positive logarithmic tail. If there are points `t_j\to+\infty` and orders `m_j` with

\[
H_{m_j}(f;t_j)\le0,
\tag{5}
\]

then necessarily

\[
\boxed{m_j\to\infty.}
\tag{6}
\]

Thus the right-tail failure mode, if it persists through the unbounded hierarchy, is **order drift** rather than failure of any one fixed local certificate.

## Derivation

### 1. Higher Euler harmonics are exponentially smaller under every fixed derivative budget

Put

\[
g(t):=e^{-x},
\qquad
r(t):=f(t)-g(t)=\sum_{n\ge2}\frac{e^{-nx}}n,
\qquad x=e^t.
\tag{7}
\]

Let `D=d/dt=x d/dx`. For every fixed `k>=0`,

\[
D^k e^{-nx}=P_k(nx)e^{-nx},
\tag{8}
\]

where `P_k` is a polynomial of degree `k` whose coefficients depend only on `k`. Hence, for `x>=1`,

\[
|D^k g(t)|\le C_k x^k e^{-x}.
\tag{9}
\]

Using `(8)` termwise in the absolutely convergent tail,

\[
\begin{aligned}
|D^k r(t)|
&\le C_k x^k\sum_{n\ge2}n^{k-1}e^{-nx}\\
&\le C_k' x^k e^{-2x}.
\end{aligned}
\tag{10}
\]

Thus every fixed derivative of the higher-harmonic tail is smaller than the corresponding natural first-harmonic scale by one full exponential factor.

### 2. The first harmonic has an exact positive confluent hierarchy

Use the normalized determinants from AF-404,

\[
R_m(g;t):=\frac{H_m(g;t)}{g(t)^m}.
\tag{11}
\]

For `g=e^{-x}`,

\[
-(\log g)''=x.
\tag{12}
\]

AF-404's Hankel--Toda recurrence therefore gives

\[
R_{m+1}R_{m-1}
=R_m^2\left(mx-(\log R_m)''\right),
\qquad
R_1=1,\quad R_2=x.
\tag{13}
\]

Induction now stays inside monomials. Define

\[
a_m=\binom m2,
\qquad
C_m=\prod_{j=1}^{m-1}j!
\quad(C_1=1).
\tag{14}
\]

If `R_m=C_m x^{a_m}`, then `\log R_m` is affine in `t=\log x`, so `(\log R_m)''=0`. Equation `(13)` gives exactly

\[
R_{m+1}=m\frac{C_m^2}{C_{m-1}}
 x^{2a_m-a_{m-1}+1}
=C_{m+1}x^{a_{m+1}}.
\tag{15}
\]

Therefore

\[
\boxed{
H_m(g;t)
=C_m e^{-mx}x^{\binom m2}>0
\qquad(m\ge1,\ x>0).
}
\tag{16}
\]

This is the exact positive reference certificate that the full Euler profile approaches in the right tail.

### 3. Determinant multilinearity makes the first harmonic dominant at each fixed order

For fixed `m`, the matrix defining `H_m` uses derivatives only through order `2m-2`. From `(9)` and `(10)`, every first-harmonic matrix entry is

\[
O_m\!\left(x^{2m-2}e^{-x}\right),
\tag{17}
\]

while every tail entry is

\[
O_m\!\left(x^{2m-2}e^{-2x}\right).
\tag{18}
\]

Expand the determinant for `f=g+r` by multilinearity in its columns. The pure-`g` term is `H_m(g;t)`. Every other term contains at least one tail column, so for `x>=1`,

\[
\left|H_m(f;t)-H_m(g;t)\right|
\le
C_m' x^{2m(m-1)}e^{-(m+1)x}.
\tag{19}
\]

Dividing by the exact positive baseline `(16)` yields

\[
\frac{|H_m(f;t)-H_m(g;t)|}{H_m(g;t)}
\le
C_m'' x^{\frac32m(m-1)}e^{-x}
\longrightarrow0
\qquad(x\to\infty).
\tag{20}
\]

Hence there is `X_m<\infty` for which the ratio in `(20)` is smaller than `1` whenever `x>=X_m`. Taking `T_m=\log X_m` proves `(2)`. For a finite flag through order `r`, take

\[
T_r^*=\max_{1\le m\le r}T_m.
\tag{21}
\]

### 4. Fixed-order failure cannot escape to the right

Suppose `t_j\to+\infty` and `H_{m_j}(f;t_j)<=0`. If the orders `m_j` had a bounded subsequence, some fixed `m` would occur infinitely often. Equation `(2)` would then force `H_m(f;t_j)>0` for all sufficiently large `j`, a contradiction. Thus `(6)` follows.

This is the exact non-uniformity left compatible with AF-217: each finite order eventually inherits the positive first-harmonic certificate, while the threshold is allowed to deteriorate with order.

## Relation to AF-217, AF-337, and AF-408--AF-410

AF-217 proves that the full Euler-log translation kernel is not totally nonnegative of all orders. AF-411 does not weaken that obstruction. It shows instead that its right-tail realization cannot remain at a bounded confluent order: the all-order failure must either occur at bounded logarithmic scale or move to higher and higher order as the observation point moves right.

AF-337 proves a different finite-order recovery theorem: sufficiently deep real sampling, together with an escaping **integer source window**, lets the first-harmonic Vandermonde margin dominate all higher Euler harmonics in ordinary discrete sampling matrices. AF-411 has no integer-window or source-separation hypothesis. It is a local/confluent statement about the continuous Euler-log profile itself. The common mechanism is harmonic-tail suppression; the certificate and source class are different.

AF-408--AF-410 identify the concrete order-five gate and certify explicit left/right tails, reducing possible order-five failure to a compact interval. AF-411 is non-effective but works at **every fixed order** on the right. It does not resolve the compact order-five monotonicity question currently isolated by those findings.

## Exact controls and boundaries

### The threshold is order-dependent

No uniform `T` is asserted such that every `H_m(f;t)` is positive for all `m` once `t>=T`. Such a statement would require control of the constants and derivative degrees in `(19)` uniformly in `m` and would run directly into the all-order obstruction of AF-217.

### This is a confluent certificate, not an unrestricted tail-strip total-positivity theorem

Equation `(2)` controls derivative-Hankel minors at one translation coordinate. AF-403 globalizes a **globally** positive complete confluent hierarchy to arbitrary translation minors. AF-411 does not by itself justify applying that globalization to arbitrary row/column placements whose pairwise differences wander outside the certified tail. No broader restricted-strip `STP_r` claim is made here.

### The theorem is source-agnostic

The right-tail inheritance comes from the Euler harmonic expansion and exponential scale separation. It does not distinguish rational primes from matched generalized-prime or non-arithmetic sources and therefore supplies no prime discriminator by itself.

### There is no RH consequence

No location of a zeta zero is used. The only connection to the zero problem is structural: AF-217 shows that the full hierarchy must eventually fail somewhere, while AF-411 constrains how such failure can behave at large positive logarithmic scale.

## Prior-art and novelty audit

The determinant technology is classical. AF-404 records the Jacobi/Desnanot--Jacobi and Hankel--Toda literature, including Kajiwara--Masuda--Noumi--Ohta--Yamada (2001) and Kajiwara--Mazzocco--Ohta (2007). The pure first-harmonic profile is also consistent with Schoenberg's classical Pólya-frequency theory: after a positive exponential tilt, its bilateral Laplace transform is a shifted Gamma function, whose reciprocal has the real-zero entire-product structure appearing in Schoenberg's characterization. AF-217 records the primary Schoenberg references and the modern Gröchenig connection to zeta.

A targeted literature search for the exact full-Euler profile `-log(1-e^{-e^t})`, its derivative-Hankel determinants, and finite-order right-tail total-positivity inheritance did not locate a directly matching theorem. That absence is not evidence of novelty. The durable claim here is therefore conservative: the exact first-harmonic Toda formula plus elementary control of the higher Euler harmonics yields the order-by-order tail statement `(2)`.

## Consequence for the Arithmetic Fidelity frontier

AF-411 separates two notions that an all-order compression statement can conflate. **Every fixed finite structural certificate can become asymptotically faithful to a simpler reference model while the unbounded hierarchy remains globally unfaithful.** In the Euler case the hidden resource is order: the higher-harmonic correction is exponentially negligible against any fixed derivative budget, but no one fixed budget represents `PF_infinity`.

For the current Euler frontier this removes one possible failure mode. A bounded-order confluent defect cannot drift arbitrarily far to the right. The remaining useful questions are therefore compact-scale finite-order gates, explicit growth of `T_m` with `m`, and the distinct left-tail problem where logarithmic factors interact nontrivially with harmonic suppression.