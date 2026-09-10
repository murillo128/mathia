# FD-030 — sublinear prime-prefix ancestry still allows GCD-duality saturation

**Status:** `EXACT-DERIVED + CLASSICAL-DAVENPORT-MOBIUS-CANCELLATION + POSITIVE-MERTENS-CONE + PRIME-SHELL-REALIZATION + SCALE-DEPENDENT-SOURCE + SUBLINEAR-PRIME-BREADTH + GCD-DUALITY-SATURATION + NEGATIVE/OBSTRUCTION`.

`FD-029` classifies the exact residual freedom after enforcing every Möbius prime direction through a cutoff `Y`. At `Y>=sqrt(H)` that freedom is already prime-only, while an unbounded complete prime prefix imposed on one common source eventually recovers `mu` pointwise. The remaining finite-horizon question is whether a growing cutoff can force a uniform gap from the sharp `FD-003` GCD-duality constant before common-source recovery becomes complete.

For horizon-dependent sources, **every unbounded sublinear prime prefix is still insufficient**. Let `Y_H` be any integer-valued cutoff with

\[
Y_H\to\infty,
\qquad
Y_H/H\to0.
\tag{1}
\]

Then there are horizons `H_j->infinity` and, for every `j`, squarefree-supported ternary coefficients `a^(j)` through `H_j` satisfying

\[
a^{(j)}_1=1,
\qquad
a^{(j)}_n=0\quad(n\text{ nonsquarefree}),
\qquad
a^{(j)}_n\in\{-1,+1\}\quad(n\text{ squarefree}),
\tag{2}
\]

and the complete prefix ancestry law

\[
\boxed{
a^{(j)}_{pn}=-a^{(j)}_n
\quad
(p\le Y_{H_j}\text{ prime},\ p\nmid n,\ pn\le H_j),
}
\tag{3}
\]

such that, for `A_j(x)=sum_(n<=x) a_n^(j)`, the horizon vector

\[
m^{(H_j)}_d=A_j\!\left(\left\lfloor\frac{H_j}{d}\right\rfloor\right)
\]

satisfies

\[
\boxed{
R_{H_j}:=
\frac{(m^{(H_j)}_1)^2}
{(m^{(H_j)})^TK_{H_j}m^{(H_j)}}
\longrightarrow\zeta(2),
\qquad
K_H(d,e)=\frac{\gcd(d,e)^2}{de}.
}
\tag{4}
\]

Since `FD-003` proves `R_H<=C_H<zeta(2)` for every real horizon vector and `C_H->zeta(2)`, equation (4) is saturation of the sharp unrestricted constant. Thus exact ancestry through `Y_H=o(H)` cannot by itself yield any nonvanishing finite-horizon GCD gap, even when `Y_H` grows almost linearly.

The mechanism is precise. Positive combinations of lower-horizon physical Mertens staircase vectors approximate the GCD equality rays. A free prime `p` with `floor(H/p)=L` contributes exactly one such lower-horizon vector when its rough-core sign is flipped. The two limits in (1) leave arbitrarily many fixed quotient shells available, and the prime number theorem supplies enough primes in each shell to realize the required nonnegative coefficients.

## 1. A positive Mertens cone approaches the GCD equality rays

Write

\[
M(x)=\sum_{n\le x}\mu(n)
\]

and define, for every `L>=1`, the finitely supported vector

\[
\boxed{
b^{(L)}_d=M\!\left(\left\lfloor\frac Ld\right\rfloor\right),
\qquad d\ge1.
}
\tag{5}
\]

It vanishes for `d>L` and has `b_L^(L)=M(1)=1`. Hence `b^(1),...,b^(r)`, restricted to their first `r` coordinates, form an upper-triangular basis with diagonal one.

Consider the positive weighted combination

\[
s^{(D)}:=\sum_{L=1}^{D}\frac{b^{(L)}}{L(L+1)}.
\tag{6}
\]

For `d<=D`, put `Q=floor(D/d)`. Grouping the `L`-sum by `floor(L/d)` and telescoping `1/[L(L+1)]` gives the exact finite identity

\[
\boxed{
s^{(D)}_d
=
\frac1d\sum_{n\le Q}\frac{\mu(n)}n
-
\frac{M(Q)}{D+1}.
}
\tag{7}
\]

The incomplete final block is exactly the displayed boundary term, so no infinite rearrangement is hidden here. Davenport's classical Möbius estimate gives, for every fixed `A>0`,

\[
M(x)\ll_A\frac{x}{\log^A(2x)}.
\tag{8}
\]

Together with the classical identity `sum_(n>=1) mu(n)/n=0` and partial summation, this yields

\[
\sum_{n\le x}\frac{\mu(n)}n
\ll_A\frac1{\log^A(2x)}.
\tag{9}
\]

The exact GCD geometry also has the elementary tail bound

\[
\boxed{
\sum_{d,e>R}\frac{\gcd(d,e)^2}{d^2e^2}\ll\frac1R.
}
\tag{10}
\]

To see this, use `gcd(d,e)^2=sum_(r|d,e) J_2(r)`. Then

\[
\sum_{d,e>R}\frac{\gcd(d,e)^2}{d^2e^2}
=
\sum_{r\ge1}J_2(r)
\left(
\sum_{\substack{s\ge1\\rs>R}}\frac1{r^2s^2}
\right)^2.
\tag{11}
\]

For `r<=R` the inner sum is `O(1/(rR))`; for `r>R` it is `O(1/r^2)`. Since `J_2(r)<=r^2`, the two ranges total `O(1/R)`. Likewise

\[
\sum_{d,e\ge1}\frac{\gcd(d,e)^2}{d^2e^2}
=
\zeta(2)^2\sum_{r\ge1}\frac{J_2(r)}{r^4}<\infty.
\tag{12}
\]

For `d<=sqrt(D)`, equations (7)--(9) give `|s_d^(D)|<<_A 1/[d log^A D]`; for `d>sqrt(D)`, trivial estimates give `|s_d^(D)|<<log(D)/d`. Equations (10)--(12), with Cauchy--Schwarz for the cross term in the positive-definite `K` inner product, therefore imply

\[
\boxed{
\|s^{(D)}\|_K^2
\ll_A
\frac1{\log^{2A}D}
+
\frac{\log^2D}{\sqrt D}
\longrightarrow0.
}
\tag{13}
\]

Thus the strictly positive weights in (6) form an asymptotically zero direction in exactly the norm used by `FD-003`.

Fix `r`, let

\[
v^{(r)}:=K_r^{-1}e_1,
\qquad
C_r:=v^{(r)}_1=(K_r^{-1})_{11},
\tag{14}
\]

and pad `v^(r)` by zeros above coordinate `r`. The triangular basis gives unique real coefficients `c_1,...,c_r` with

\[
v^{(r)}=\sum_{L=1}^{r}c_Lb^{(L)}.
\tag{15}
\]

Choose finite `T_r` so that

\[
c_L+\frac{T_r}{L(L+1)}\ge0
\qquad(1\le L\le r).
\tag{16}
\]

For `D>=r`, define

\[
\alpha_L^{(r,D)}=
\begin{cases}
c_L+T_r/[L(L+1)],&L\le r,\\
T_r/[L(L+1)],&r<L\le D.
\end{cases}
\tag{17}
\]

All `alpha_L^(r,D)` are nonnegative, and

\[
\boxed{
g^{(r,D)}
:=\sum_{L=1}^{D}\alpha_L^{(r,D)}b^{(L)}
=v^{(r)}+T_rs^{(D)}.
}
\tag{18}
\]

By (13), `g^(r,D)->v^(r)` in `K` norm as `D->infinity`. Since

\[
\frac{(v^{(r)}_1)^2}{(v^{(r)})^TK_rv^{(r)}}=C_r
\tag{19}
\]

and `C_r->zeta(2)` by `FD-003`, a diagonal choice of `r,D` yields finite **nonnegative** combinations of the columns (5) whose coordinate quotient tends to `zeta(2)`.

This positivity is load-bearing. Mere linear span would not suffice below, because prime-core flips can add copies of a defect direction but cannot request a negative number of primes. Equation (18) is the mechanism that repairs the mixed signs of the triangular equality-ray expansion without paying asymptotic GCD energy.

## 2. One free rough-prime shell is exactly one lower-horizon Mertens direction

Fix `H,Y` and use the exact `FD-029` parametrization. Every squarefree `n<=H` has a unique factorization `n=qr`, where `q` uses only primes `<=Y`, `r` is `Y`-rough, and every source satisfying the prefix ancestry law is

\[
a_{qr}=\mu(q)b_r.
\tag{20}
\]

Start from the physical rough-core choice `b_r=mu(r)`. Let `p>Y` be a rough prime and flip only `b_p` from `-1` to `+1`. Put

\[
L=\left\lfloor\frac Hp\right\rfloor
\tag{21}
\]

and assume `L<=Y`. At horizon coordinate `d`, `FD-029` gives the cumulative defect

\[
2M_Y\!\left(
\left\lfloor\frac{\lfloor H/d\rfloor}{p}\right\rfloor
\right),
\tag{22}
\]

where `M_Y` is the Möbius sum over the `Y`-smooth squarefree semigroup. Nested floors give

\[
\left\lfloor\frac{\lfloor H/d\rfloor}{p}\right\rfloor
=
\left\lfloor\frac{H}{dp}\right\rfloor
=
\left\lfloor\frac Ld\right\rfloor.
\tag{23}
\]

The last quotient is at most `Y`, so every squarefree integer contributing to `M_Y` is automatically `Y`-smooth. Thus `M_Y=M` there and one flipped prime contributes exactly

\[
\boxed{2b^{(L)}}
\tag{24}
\]

to the full horizon vector. If `k_L` primes are flipped in

\[
\frac{H}{L+1}<p\le\frac HL,
\tag{25}
\]

the contribution is exactly `2k_L b^(L)`.

## 3. Every `o(H)` growing prefix leaves enough shell capacity

Choose `r_j->infinity`. From Section 1 choose, for every `j`, finite `D_j>=r_j` and nonnegative coefficients `alpha_(j,L)` such that the quotient of

\[
g_j:=\sum_{L\le D_j}\alpha_{j,L}b^{(L)}
\tag{26}
\]

is within `1/j` of `C_(r_j)`.

The two assumptions in (1) let us choose `H_j` arbitrarily large with

\[
D_j\le Y_{H_j},
\qquad
(D_j+1)Y_{H_j}<H_j.
\tag{27}
\]

Hence every shell (25) used by `g_j` lies entirely above the enforced prime prefix. For fixed `L`, the prime number theorem gives

\[
\#\left\{p:\frac{H}{L+1}<p\le\frac HL\right\}
\sim
\frac{H}{L(L+1)\log H}.
\tag{28}
\]

Take

\[
t_H:=\frac{H}{\log^4H},
\qquad
k_L:=\left\lfloor\frac{t_H\alpha_{j,L}}2\right\rceil.
\tag{29}
\]

At fixed stage `j`, equation (28) exceeds every requested `k_L` by three powers of `log H`, so `H_j` can be chosen large enough to realize all counts with distinct primes. Define the source by (20), flipping exactly those prime rough cores and leaving every other rough-core sign physical. Equations (24)--(29) give the exact decomposition

\[
\boxed{
m^{(H)}
=m_\mu^{(H)}+2\sum_{L\le D_j}k_Lb^{(L)},
\qquad
m_{\mu,d}^{(H)}=M\!\left(\left\lfloor\frac Hd\right\rfloor\right).
}
\tag{30}
\]

The physical background in (30) is negligible at scale `t_H`. Split it at `d=sqrt(H)`. For the low block, Davenport gives `|m_(mu,d)^(H)|<<_A H/[d log^A H]`; for the high block use `|m_(mu,d)^(H)|<=H/d`. Applying (10)--(12) once more yields

\[
\boxed{
\|m_\mu^{(H)}\|_{K_H}
\ll_A
\frac{H}{\log^AH}+H^{3/4}.
}
\tag{31}
\]

Choosing `A>4` makes this `o(t_H)`. The integer rounding in (29) costs only `O_j(1)` in `K` norm because `D_j` is fixed during the choice of `H_j`. Therefore `H_j` can be chosen so that

\[
\left\|
\frac{m^{(H_j)}}{t_{H_j}}-g_j
\right\|_{K_{H_j}}<\frac1j,
\qquad
\left|
\frac{m^{(H_j)}_1}{t_{H_j}}-g_{j,1}
\right|<\frac1j.
\tag{32}
\]

The support of `g_j` is at most `D_j`, so its `K_(H_j)` norm is its `K_(D_j)` norm. Quotient continuity, `C_(r_j)->zeta(2)`, and the universal `FD-003` upper bound now prove (4).

## 4. Consequence for the prime-breadth program

`FD-027` rules out fixed finite prime breadth, `FD-028` rules out even infinitely many sufficiently sparse prime directions for a common source, and `FD-029` shows that a complete growing prime prefix eventually determines any one common source. The present theorem separates that pointwise recovery phenomenon from finite-scale coercivity.

Even exact ancestry through **all primes up to `H^0.99`, `H/log H`, `H/log log H`, or any other unbounded `o(H)` cutoff** still permits horizon-dependent saturation. The primes near `H/L` in finitely many quotient shells synthesize the positive Mertens cone, and sublinearity leaves the number of available fixed shells unbounded along the diagonal construction.

Accordingly, simply accelerating a sublinear prime cutoff cannot close the current finite-horizon relaxation. The next breadth transition is genuinely **linear-scale exposure**: `Y_H/H` must fail to tend to zero before this shell-synthesis obstruction loses its arbitrarily deep quotient reservoir. This is a boundary of the present theorem, not a proof that every fixed positive linear fraction forces a gap.

The construction also does not preserve the `1/2+epsilon` source envelopes from `FD-026` and `FD-028`. Its selected endpoint scale is deliberately comparable to `H/log^4 H` up to the fixed-stage factor, consistent with the super-square-root endpoint requirement in `FD-025`. Thus the remaining stronger intersection is quantitative: can sufficiently broad ancestry **together with** an RH-scale source envelope coerce non-saturation?

## 5. Prior-art and falsification boundary

The analytic inputs are classical. H. Davenport, *On Some Infinite Series Involving Arithmetical Functions (II)*, Quarterly Journal of Mathematics **os-8** (1937), 313--320, proves the log-power Möbius exponential-sum saving whose zero-frequency case gives (8). The prime-shell asymptotic (28) is the ordinary prime number theorem. Möbius inversion and completeness of Lambert-type systems also have classical literature, including Hille--Szász, *On the Completeness of Lambert Functions II*, Annals of Mathematics **37** (1936), 801--815. That work is a neighboring completeness boundary, not a load-bearing theorem here.

No novelty is claimed for PNT cancellation, positive cones, Lambert completeness, or fixed-relative-width prime intervals in isolation. The line-specific result is their exact splice with `FD-029`: **free rough-prime shells realize positive lower-horizon Mertens directions one-for-one, and those directions recover the sharp `FD-003` dual constant despite an arbitrarily deep sublinear complete prime prefix.**

Several stress tests are essential. Equation (24) needs both `L<=Y` and `p>Y`; (27) enforces both. The equality vector does not generally have nonnegative coefficients in the finite triangular basis; the positive zero direction (6) is what repairs those signs. The decay proof uses the finite identity (7), so no conditionally convergent series is rearranged. Davenport's input is unconditional and far weaker than RH. Finally, the sources depend on `H`; imposing growing complete prefixes on one fixed infinite source returns to the `FD-029` recovery theorem and the construction disappears.

If `Y_H/H` is bounded below by a positive constant, only finitely many quotient shells `floor(H/p)` remain above the prefix, so the diagonal `D_j->infinity` construction is unavailable. No non-saturation theorem is asserted in that linear regime. A falsification of (4) would require failure of the exact shell identity (24), the positive-cone approximation (18), the PNT shell capacity (28), or the physical-background estimate (31).