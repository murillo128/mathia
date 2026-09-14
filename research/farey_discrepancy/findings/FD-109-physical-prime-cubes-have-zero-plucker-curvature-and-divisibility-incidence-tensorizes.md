# FD-109 — physical prime cubes have zero Plücker curvature and divisibility incidence tensorizes

**Status:** `EXACT-DERIVED + PHYSICAL-COEFFICIENT-LAW + MULTI-PRIME-INCIDENCE + RANK-ONE-PRIME-CUBE + VANISHING-LOCAL-PLUCKER-MINORS + COMMUTING-DILATION-RESOLVENT + SOURCE-RICH-PRODUCT-BUDGET + NEGATIVE/ROUTE-RESTRICTION`.

`FD-108` shows that the first-order prime-divisibility consequence of the physical source law is power-critical at the terminal harmonic fan. Its live escape clause is to use genuinely higher-order prime incidence, multiplicative sign coherence, or a nonlinear coupling before the one-prime information is collapsed into an additive `L^2` budget. The first higher-order object to test is therefore the prime-direction cube of the physical increments themselves.

That raw local cube is completely flat. If

\[
a(n):=\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n,
\tag{1}
\]

then for every finite set `S` of distinct primes and every `m>=1`,

\[
\boxed{
a\!\left(m\prod_{p\in T}p\right)
=a(m)\prod_{p\in T}\tau_p(m)
\qquad(T\subseteq S),}
\tag{2}
\]

where

\[
\tau_p(m)
:=\mathbf 1_{p\mid m}-(1-p^{-1})
=
\begin{cases}
-(1-p^{-1}),&p\nmid m,\\[1mm]
p^{-1},&p\mid m.
\end{cases}
\tag{3}
\]

Consequently every flattening of the `2^{|S|}` prime cube has tensor rank one. In particular, for distinct primes `p,q`,

\[
\boxed{
a(m)a(pqm)-a(pm)a(qm)=0.}
\tag{4}
\]

Thus the most direct coefficient-level two-prime Plücker determinant vanishes identically; increasing the number of raw prime directions produces no local exterior defect to exploit.

The nontriviality introduced by summation can also be classified exactly. For squarefree

\[
q=\prod_{p\in S}p
\]

put

\[
D_S(X)
:=\sum_{\substack{n\le X\\p\mid n\ \forall p\in S}}a(n),
\qquad
(T_rF)(X):=F\!\left(\left\lfloor\frac Xr\right\rfloor\right).
\tag{5}
\]

Then, for `p notin S`,

\[
\boxed{
D_{S\cup\{p\}}(X)
=D_{S\cup\{p\}}\!\left(\left\lfloor\frac Xp\right\rfloor\right)
-(1-p^{-1})D_S\!\left(\left\lfloor\frac Xp\right\rfloor\right),}
\tag{6}
\]

and hence

\[
\boxed{
D_S
=a(q)\prod_{p\mid q}T_p(I-T_p)^{-1}\mathcal H.}
\tag{7}
\]

The inverse is only a finite geometric sum at each fixed `X`. The dilation operators commute exactly, including the floors. Expanding (7) gives

\[
\boxed{
D_S(X)
=a(q)
\sum_{\substack{r\ge1\\\operatorname{rad}r=q}}
\mathcal H\!\left(\left\lfloor\frac Xr\right\rfloor\right),}
\tag{8}
\]

while applying the finite differences back gives

\[
\boxed{
\left(\prod_{p\mid q}(I-T_p)\right)D_S
=a(q)T_q\mathcal H.}
\tag{9}
\]

Therefore every fixed squarefree higher-order divisibility projection is an exact commuting tensor product of the one-prime resolvent from `FD-108`. After the appropriate prime-direction finite differences it recovers one source value at the **product scale** `X/q`; it does not manufacture a same-scale cross-prime observable such as a product or antisymmetric coupling of the terminal values `mathcal H(X/p)` and `mathcal H(X/r)`.

This sharply restricts what “higher-order prime incidence” can mean at the current frontier. Merely replacing the one-prime projection of `FD-108` by simultaneous divisibility by `pr`, `prs`, and so on is a depth refinement, not yet the missing terminal-fan coherence theorem. A successful higher-order route must use something lost by (7)--(9): nonlinear products before summation, least-prime-factor order, correlations between different horizons, or a refinement/Plücker construction whose vectors are not the raw local coefficient cube.

## 1. The physical prime cube is exactly rank one

`FD-108` derived the one-prime covariance

\[
a(pm)=
\begin{cases}
-(1-p^{-1})a(m),&p\nmid m,\\[1mm]
p^{-1}a(m),&p\mid m.
\end{cases}
\tag{10}
\]

which is precisely `a(pm)=tau_p(m)a(m)`. If `p` and `r` are distinct primes, multiplying `m` by `r` does not change whether `p` divides it. Hence

\[
\tau_p(rm)=\tau_p(m)
\qquad(p\ne r).
\tag{11}
\]

Applying (10) one prime at a time therefore proves (2), independently of the order of the primes. The two-dimensional face is

\[
\begin{pmatrix}
a(m)&a(qm)\\
a(pm)&a(pqm)
\end{pmatrix}
=
a(m)
\begin{pmatrix}1\\\tau_p(m)\end{pmatrix}
\begin{pmatrix}1&\tau_q(m)\end{pmatrix},
\tag{12}
\]

so its determinant is zero, proving (4). More generally the full cube is the decomposable tensor

\[
a(m)\bigotimes_{p\in S}(1,\tau_p(m)).
\tag{13}
\]

This is not an asymptotic independence statement. It is an exact pointwise algebraic identity, valid whether or not some of the primes in `S` already divide `m`. Repeated powers in one prime direction are not being declared independent directions; they are handled by the `p^{-1}` branch of (10).

There is also an elementary multiplicative description behind this flatness. At prime powers,

\[
a(p^e)=-\frac{p-1}{p^e}\qquad(e\ge1),
\tag{14}
\]

and (1) is multiplicative on coprime arguments. Thus vanishing of the raw prime-cube minors is the expected local Euler-product geometry, not a new arithmetic theorem by itself. The Mathia-relevant result is the route classification obtained after carrying this exact flatness through the cumulative divisibility hierarchy.

## 2. Summation creates only commuting product-depth resolvents

Let `p notin S` and put `Y=floor(X/p)`. Writing every integer counted by `D_(S union {p})(X)` as `pm`, the other prime divisibility conditions are exactly `r|m` for all `r in S`. Splitting at `p|m` and using (10),

\[
\begin{aligned}
D_{S\cup\{p\}}(X)
&=-(1-p^{-1})
 \bigl(D_S(Y)-D_{S\cup\{p\}}(Y)\bigr)
 +p^{-1}D_{S\cup\{p\}}(Y)\\
&=D_{S\cup\{p\}}(Y)-(1-p^{-1})D_S(Y),
\end{aligned}
\tag{15}
\]

which is (6). Iterating until the argument is zero yields

\[
D_{S\cup\{p\}}
=-(1-p^{-1})T_p(I-T_p)^{-1}D_S.
\tag{16}
\]

The floor dilations satisfy

\[
T_rT_s=T_{rs}=T_sT_r
\tag{17}
\]

for positive integers `r,s`. Starting from `D_emptyset=mathcal H` and iterating (16) over the distinct prime factors of `q` gives

\[
D_S
=(-1)^{\omega(q)}
\prod_{p\mid q}(1-p^{-1})
\prod_{p\mid q}T_p(I-T_p)^{-1}\mathcal H.
\tag{18}
\]

Because `q` is squarefree,

\[
(-1)^{\omega(q)}\prod_{p\mid q}(1-p^{-1})
=\frac{\mu(q)\varphi(q)}q
=a(q),
\tag{19}
\]

which proves (7). Expanding all geometric series gives (8), since the resulting dilation denominators are exactly

\[
r=\prod_{p\mid q}p^{j_p},
\qquad j_p\ge1,
\]

that is, `rad(r)=q`. Multiplying (7) by `prod_(p|q)(I-T_p)` proves (9) with no remainder.

A useful quantitative form separates the leading product-depth sample from repeated-prime tails. Since `|a(n)|<=1`,

\[
|\mathcal H(Y)|\le Y.
\tag{20}
\]

The terms in (8) other than `r=q` therefore satisfy

\[
\begin{aligned}
\left|
D_S(X)-a(q)\mathcal H\!\left(\left\lfloor\frac Xq\right\rfloor\right)
\right|
&\le |a(q)|X
\left(
\prod_{p\mid q}\frac1{p-1}-\frac1q
\right)\\
&=
\boxed{
\frac Xq\left(1-\frac{\varphi(q)}q\right).}
\end{aligned}
\tag{21}
\]

For a product of large primes the simultaneous divisibility projection is therefore close to `a(q) mathcal H(X/q)`, but it is still a deeper scalar source sample rather than a coupling of the first-layer samples.

## 3. The adaptive source cutoff becomes a product budget, not a Cartesian prime fan

The distinction matters at the exact terminal scale isolated by `FD-105`--`FD-108`. Write the sharp parent horizon as `H=4X` and retain the adaptive low-source cutoff

\[
L_H=\left\lfloor\frac{U_H}{H\log H}\right\rfloor.
\tag{22}
\]

A one-prime terminal sample `mathcal H(floor(X/p))` is source-rich only while

\[
\frac Xp\gtrsim L_H,
\]

which is the origin of the terminal cutoff

\[
P_*(X)\asymp\frac X{L_H}
\ll \frac{X^2\log X}{U_H}
\tag{23}
\]

up to harmless constants and the endpoint convention used in `FD-108`.

For the `k`-prime projection (8), the leading new sample is at `X/q`, where `q` is the **product** of the distinct prime labels. It remains in the same source-rich region only if

\[
\boxed{q\lesssim P_*(X).}
\tag{24}
\]

Thus going to order `k` does not replace the one-prime range by a Cartesian box `p_1,...,p_k<=P_*`. It gives the logarithmic simplex

\[
\boxed{
\sum_{j=1}^k\log p_j\lesssim\log P_*(X).}
\tag{25}
\]

On a sharp false-RH state with

\[
U_H=H^{2\Theta+o(1)},
\qquad \frac12<\Theta<1,
\tag{26}
\]

this common product budget is

\[
q\le X^{2-2\Theta+o(1)}.
\tag{27}
\]

The higher-order hierarchy therefore descends into smaller source arguments as soon as several prime labels are combined. It can certainly contain useful information there, and highly unbalanced products such as `2p` still reach almost to the one-prime edge. What (24)--(27) rule out is a simpler hope: that fixed-order simultaneous divisibility automatically supplies independent source-rich constraints for arbitrary tuples drawn from the full terminal prime fan. The adaptive cutoff is on their product.

This also identifies the missing bridge for the tempting `q=2p` use of (9). That identity controls `mathcal H(X/(2p))`, while the terminal packet of `FD-106` is measured by `mathcal H(X/p)`. Passing from one to the other requires genuine cross-scale information about the physical source; the commuting incidence algebra alone provides none. The common-source and one-Lipschitz controls were already shown insufficient for the harmonic endpoint in `FD-107`, so this step cannot be silently supplied by generic regularity.

## 4. Stress tests, prior art, and the surviving higher-order target

The first adversarial control is the local Plücker test itself. For every choice of divisibility pattern of `m` by `p` and `q`, direct substitution in (10) gives (4); there is no exceptional face on which a coefficient-level determinant survives. A finite exact check over small `X` and several one-, two-, and three-prime sets also reproduces (8), but the proof above is algebraic and does not depend on computation.

The second control is information-theoretic. Equations (7)--(9) do **not** say that simultaneous divisibility is useless. The family of product-depth samples may still constrain a physical false-RH profile when combined nonlinearly, across horizons, or with the least-prime-factor partition. The conclusion is narrower: the linear divisibility hierarchy itself is a commuting tensor of the one-prime transfer, and its raw local Plücker minors vanish. Any claimed two-prime gain that uses only these projections must identify where it departs from this flat resolvent algebra.

The third control is analytic. There is a substantial literature on large sieves for sparse sets of moduli, from Baier's work on sparse moduli to later bounds using additive energy. Therefore this finding does **not** claim that the all-moduli large-sieve constant used in `FD-108` is optimal for squarefree products of primes, nor that every sparse-modulus `L^2` refinement is power-critical. No such theorem is needed here. The exact statements (2), (4), and (6)--(9) precede any large-sieve estimate and survive any improvement of that analytic layer.

The local flatness is also distinct from two earlier Mathia controls. `FD-011` shows that raw Plücker minors of homogeneous Farey increment vectors collapse to classical Farey-index algebra; the present finding concerns the prime-direction cube of the **physical harmonic source coefficients**. `FD-029` gives an exact rough-core factorization for a squarefree sign-source model under a growing prime-prefix ancestry law; here the coefficients are the fixed physical source, prime powers are retained, and the cumulative statement is the resolvent identity (7)--(9).

No novelty is claimed for multiplicativity, Euler-factor tensorization, or the elementary vanishing determinant (4) in isolation. The durable line-specific content is the boundary they impose on the post-`FD-108` program: **raw higher-order coefficient incidence has zero local exterior curvature, while cumulative higher-order divisibility merely exposes deeper product-scale samples under the same source-rich product budget.** The next useful higher-order object must therefore break at least one of those reductions—for example by preserving least-prime-factor order, forming nonlinear cross-horizon energy before summation, or using controlled refinement vectors whose Plücker minors are not the raw coefficient cube.

No external theorem is load-bearing in the derivation, so `SOURCES.md` requires no change.