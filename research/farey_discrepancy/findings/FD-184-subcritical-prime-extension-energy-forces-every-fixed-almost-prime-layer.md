# FD-184 — Subcritical prime-extension energy forces every fixed almost-prime layer

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** relational source rigidity / all-fixed-rank prime-fan bootstrap / exceptional-prefix convolution / fixed-prime signed perturbations
- **Depends on:** FD-181, FD-183
- **Classification:** `EXACT-DERIVED + RELATIONAL-RIGIDITY + ALL-FIXED-RANK-BOOTSTRAP + FIXED-PRIME-SIGNED-PERTURBATIONS`

## Claim

`FD-183` shows that on the fixed-prime fibre, suppressing prime-extension energy below the prime-fan scale forces a non-Möbius perturbation through the squarefree semiprime layer. The two-generation argument can in fact be iterated through **every fixed multiplicative rank**, provided the exceptional edges are counted through their canonical prime-factor prefixes rather than by naively repeating the one-parent fan estimate.

Let `a` be a real-valued arithmetic source satisfying

\[
a(1)=1,
\qquad
a(n)=0\quad\text{whenever }\mu(n)=0,
\qquad
a(p)=-1\quad(p\text{ prime}).
\tag{1}
\]

Put

\[
\delta(n):=a(n)-\mu(n),
\qquad
S:=\{n:\delta(n)\ne0\},
\tag{2}
\]

and suppose `a!=mu`. Let

\[
n_0:=\min S,
\qquad
\Delta:=|\delta(n_0)|>0.
\tag{3}
\]

For fixed `1<=q<infinity`, use the prime-extension energy

\[
\mathcal M_{a,q}(x)
:=
\sum_{(n,pn)\in E_x}
|a(pn)-a(p)a(n)|^q,
\tag{4}
\]

with the same squarefree prime-extension edge set as `FD-181` and `FD-183`.

Assume

\[
\boxed{
\mathcal M_{a,q}(x)=o(x/\log x).
}
\tag{5}
\]

Then for **every fixed integer `r>=1`**,

\[
\boxed{
S(x)
\ge
\left(
\frac{1}{n_0(r-1)!}+o(1)
\right)
\frac{x(\log\log x)^{r-1}}{\log x}.
}
\tag{6}
\]

Thus the `r=1` case recovers the prime-fan support scale, while `r=2` recovers the semiprime-scale conclusion of `FD-183`. More importantly, no fixed almost-prime rank is terminal: subcritical relation energy propagates a fixed seed error through asymptotically almost all squarefree descendants of every fixed added rank.

A useful equivalent consequence is that for every fixed real `A>=0`,

\[
\boxed{
\frac{S(x)\log x}
{x(\log\log x)^A}
\longrightarrow\infty.
}
\tag{7}
\]

So a non-Möbius fixed-prime source with subcritical prime-extension energy cannot have support

\[
S(x)=O\!\left(
\frac{x(\log\log x)^A}{\log x}
\right)
\tag{8}
\]

for any fixed `A`. The support tariff above one prime fan must beat **every fixed power of `log log x`**.

## 1. Fixed primes turn every canonical edge into an additive error recurrence

As in `FD-183`, for every prime `p` with `p\nmid n`,

\[
a(pn)-a(p)a(n)
=
\delta(pn)+\delta(n).
\tag{9}
\]

Fix an integer `r>=1` for the rest of the proof and set

\[
\eta:=\frac{\Delta}{2r}.
\tag{10}
\]

Let

\[
m=p_1p_2\cdots p_r,
\qquad
p_1<\cdots<p_r,
\qquad
(m,n_0)=1,
\tag{11}
\]

be squarefree, and define canonical prefixes

\[
m_j:=p_1\cdots p_j,
\qquad m_0:=1.
\tag{12}
\]

Along the canonical path

\[
n_0,\ n_0m_1,\ldots,n_0m_r
\tag{13}
\]

define edge defects

\[
e_j(m)
:=
\delta(n_0m_j)+\delta(n_0m_{j-1}).
\tag{14}
\]

If every edge on this path is `eta`-good, meaning `|e_j(m)|<=eta`, then iteration of (14) gives

\[
\delta(n_0m_r)
=
(-1)^r\delta(n_0)
+
\sum_{j=1}^r(-1)^{r-j}e_j(m).
\tag{15}
\]

Consequently

\[
|\delta(n_0m_r)|
\ge
\Delta-r\eta
=
\Delta/2.
\tag{16}
\]

Hence

\[
\boxed{
\text{an unchanged rank-`r` descendant must contain a bad canonical edge.}
}
\tag{17}
\]

This path identity is the finite-depth stability mechanism that was implicit in the two-generation proof of `FD-183`.

## 2. At every fixed prefix depth, bad canonical edges have prime-scale counting density

For `1<=j<=r`, let `B_j(T)` be the number of squarefree integers

\[
t=q_1\cdots q_j\le T,
\qquad
q_1<\cdots<q_j,
\qquad
(t,n_0)=1,
\tag{18}
\]

whose canonical final edge

\[
(n_0q_1\cdots q_{j-1},\ n_0t)
\tag{19}
\]

has defect larger than `eta`.

Every such edge belongs to the energy at scale `n_0T` and contributes more than `eta^q`. Therefore (5) gives

\[
\eta^q B_j(T)
\le
\mathcal M_{a,q}(n_0T)
=
o(T/\log T),
\tag{20}
\]

so, for every fixed `j`,

\[
\boxed{
B_j(T)=o(T/\log T).
}
\tag{21}
\]

The key point is that (21) is available separately at every fixed prefix depth without spending the energy budget once per parent. What remains is to show that a set this sparse cannot contaminate a main-order proportion of a higher fixed almost-prime layer through its many possible completions.

## 3. Exceptional-prefix convolution lemma

We use the following elementary consequence of the prime number theorem.

**Lemma.** Let `B` be any set of positive integers with

\[
B(T)=o(T/\log T).
\tag{22}
\]

For fixed `s>=0`, let `C_s(X)` count tuples

\[
(b,p_1,\ldots,p_s),
\qquad
b\in B,
\qquad
bp_1\cdots p_s\le X,
\tag{23}
\]

where the `p_i` are primes; repetitions and order are allowed. Then

\[
\boxed{
C_s(X)
=
o\!\left(
\frac{X(\log\log X)^s}{\log X}
\right).
}
\tag{24}
\]

For `s=0` this is (22). For the induction step,

\[
C_{s+1}(X)=\sum_{p\le X}C_s(X/p).
\tag{25}
\]

Given `epsilon>0`, choose a fixed `Y_0` so that beyond `Y_0`,

\[
C_s(Y)
\le
\epsilon
\frac{Y(1+\log\log Y)^s}{\log Y}.
\tag{26}
\]

The primes with `X/p<Y_0` contribute only `O_{Y_0}(X/log X)`. For the rest, (26), the PNT and partial summation reduce the required bound to

\[
\sum_{p\le X/Y_0}
\frac{(1+\log\log(X/p))^s}
{p\log(X/p)}
\ll_s
\frac{(\log\log X)^{s+1}}{\log X}.
\tag{27}
\]

Indeed the corresponding PNT integral is

\[
\int
\frac{(1+\log(\log X-u))^s}
{u(\log X-u)}\,du,
\tag{28}
\]

and

\[
\frac1{u(\log X-u)}
=
\frac1{\log X}
\left(
\frac1u+\frac1{\log X-u}
\right),
\tag{29}
\]

which gives (27). Since `epsilon` is arbitrary, (24) follows.

This is the weighted exceptional-prefix control missing from a formal repetition of `FD-183`: a prime-scale exceptional set remains negligible after convolution with any **fixed** number of additional prime factors.

## 4. Almost every fixed-rank descendant has a completely good canonical path

Put

\[
X:=x/n_0.
\tag{30}
\]

For a fixed level `j`, any rank-`r` integer `m` whose canonical `j`-prefix belongs to `B_j` can be written as

\[
m=t u,
\qquad
t\in B_j,
\tag{31}
\]

where `u` is a product of `r-j` primes. Dropping the ordering, distinctness and coprimality restrictions can only enlarge the count. Applying the lemma with `s=r-j` therefore shows that the number of rank-`r` descendants contaminated at level `j` is

\[
o\!\left(
\frac{X(\log\log X)^{r-j}}{\log X}
\right).
\tag{32}
\]

Because `r` is fixed, summing (32) over `j=1,...,r` gives

\[
o\!\left(
\frac{X(\log\log X)^{r-1}}{\log X}
\right).
\tag{33}
\]

Landau's fixed-rank theorem gives

\[
\#\{m\le X:\mu^2(m)=1,\ \omega(m)=r\}
\sim
\frac{X(\log\log X)^{r-1}}
{(r-1)!\log X}.
\tag{34}
\]

Requiring `(m,n_0)=1` does not change the main term: excluding any of the finitely many prime divisors of `n_0` lowers the multiplicative rank by one and therefore costs only a lower-order fixed-rank layer.

Combining (33) and (34), asymptotically all eligible rank-`r` integers have no bad canonical edge. Equation (16) then shows that all those terminal coordinates `n_0m` belong to `S`. Since `m -> n_0m` is injective and `n_0m<=x`, we obtain

\[
S(x)
\ge
\left(
\frac1{(r-1)!}+o(1)
\right)
\frac{X(\log\log X)^{r-1}}{\log X},
\tag{35}
\]

which is (6).

Finally, for any fixed real `A>=0`, choose a fixed integer `r` with `r-1>A`. Dividing (6) by `x(log log x)^A/log x` proves (7).

## 5. Stress tests and boundaries

**No growing-rank conclusion is claimed.** The theorem is uniform in `x` only after `r` is fixed. The edge threshold `eta=Delta/(2r)`, the exceptional-prefix estimates and Landau asymptotics all have constants depending on `r`. It is therefore invalid to choose `r=r(x)` from (6), and the result does not prove that `S(x)=o(x)` plus subcritical energy forces `a=mu`.

**Moving prime coordinates remain outside the theorem.** The exact recurrence (9) depends on `a(p)=-1` for every prime. If prime labels move, one changed prime can affect a whole edge family and the canonical additive recurrence no longer holds. `FD-181` remains the robust statement for that larger fibre.

**Signed and tiny later amplitudes are allowed.** No sign or lower bound is imposed on `delta(n)` away from `n_0`. The fixed seed amplitude `Delta` supplies the path threshold. If many later amplitudes become tiny, some edge on the canonical path must absorb a fixed defect and is charged to the global energy.

**The hierarchy is a support theorem, not an observation theorem.** No Farey spatial data are used. `FD-182` still rules out obtaining the needed subcritical relation-energy control from the exact dyadic midpoint ladder alone on the broad nonmultiplicative fibre.

**No RH consequence follows.** Even a source-side condition that forces Möbius would still need a quantitatively stable route into the Franel--Landau discrepancy norm at the critical scale.

## Representation audit

The proof stays in the original arithmetic coefficient coordinates and uses exactly the prime-extension graph of `FD-181`--`FD-183`. No cumulative inversion, source-dependent transform, spectral reweighting or Farey-field reconstruction is introduced.

The generic mechanism is a finite-depth path-stability statement plus a sparse-exception convolution lemma: a fixed endpoint can differ substantially from the alternating seed only if one edge on its canonical path carries a fixed defect, while a set of such bad prefixes of size `o(T/log T)` cannot cover a main-order proportion of a fixed almost-prime layer after finitely many prime extensions. The arithmetic splice is the physical prime identity (9) and Landau's fixed-rank count.

The deliberately discarded information remains all Farey spatial structure. The result strengthens only the source-side relation tariff available to a future observation-to-relation bridge.

## Prior-art audit

The load-bearing external inputs are classical and already anchored in `SOURCES.md`: the prime number theorem (Newman) and Landau's fixed-rank almost-prime asymptotic (Wright). No new theorem is imported.

A targeted search was also made for stability of multiplicative functions, property testing of multiplicativity, expansion on divisibility graphs, and fixed-rank almost-prime propagation. The closest structural neighbor found was Helfgott--Radziwiłł, *Expansion, divisibility and parity* (arXiv:2103.06853), which proves strong local spectral expansion for a different graph: vertices in a short interval are connected additively by `n -> n +/- p` when `p|n`. That work is highly relevant as a warning that prime-divisibility graphs can carry genuine expansion, but it does not state the present deterministic theorem on the multiplicative extension graph `n -> pn`, sparse support of a perturbation of Möbius, or propagation through every fixed almost-prime rank.

No direct prior-art match was found for the exceptional-prefix convolution bootstrap above. This is not a claim that no such formulation exists elsewhere; the novelty claim is restricted to the Mathia-specific splice of the fixed-prime defect recurrence, subcritical global edge energy and fixed-rank Landau layers.

Because Helfgott--Radziwiłł is a neighboring prior-art boundary rather than a load-bearing dependency, and the proof itself uses only already-anchored PNT/Landau inputs, `SOURCES.md` requires no change in this pass.

## Research consequence

`FD-183` left open whether the two-generation semiprime tariff was a terminal phenomenon. It is not. On the fixed-prime fibre, subcritical prime-extension energy forces support through every fixed squarefree almost-prime generation and therefore makes the excess support above `x/log x` super-polynomial in `log log x`.

The remaining source-side question is now genuinely a **growing-rank** question: can the exceptional-prefix convolution be made quantitative uniformly for `r=r(x)` far enough to force a near-linear support tariff, or is there a construction that exploits deterioration of the path threshold and fixed-rank counting constants? That question is distinct from the moving-prime `x/log x` frontier of `FD-181`.

The observation-side question from `FD-182` is unchanged and becomes more valuable: any intermediate Farey spatial sensor that can force `M_(a,q)(x)=o(x/log x)` on this fixed-prime fibre would inherit an all-fixed-rank support rigidity theorem rather than merely the semiprime bound of `FD-183`.