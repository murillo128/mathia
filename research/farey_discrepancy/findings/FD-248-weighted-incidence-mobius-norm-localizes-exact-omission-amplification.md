# FD-248 — Weighted incidence Möbius norm localizes exact-omission amplification

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / divisibility posets / incidence inversion / growing defect / quantitative inverse
- **Depends on:** FD-225, FD-245, FD-246, FD-247
- **Classification:** `EXACT-DERIVED + WEIGHTED-INCIDENCE-INVERSE + FOREST-STABILITY + CONDITIONING-THRESHOLD`

## Claim

FD-247 shows that divisibility-antichain support makes the exact omission inverse diagonal. The next question is whether cross-scale divisibility chains can already create the large inverse amplification left open there. They cannot. More generally, the exact response-side amplification is controlled by a concrete weighted Möbius norm of the **induced divisibility poset on the actual increment support**.

Let

\[
Y(m)=(\mathscr A b)(m),\qquad Y(0)=0,
\]

with

\[
|b_n|\le Cn\qquad(n\ge1).
\tag{1}
\]

Fix `N>=1`, and suppose

\[
Y(m)=0\qquad(1\le m\le N,\ m\notin E_N)
\tag{2}
\]

for an exact omission set `E_N subseteq {1,...,N}` of cardinality `K`. Put

\[
g=\mu*b,
\qquad
D_N:=\{d\le N:g(d)\ne0\}.
\tag{3}
\]

As in FD-225 and FD-247,

\[
b=\mathbf1*g,
\qquad
g(d)=Y(d)-Y(d-1),
\tag{4}
\]

and therefore

\[
D_N\subseteq E_N\cup\bigl((E_N+1)\cap[1,N]\bigr),
\qquad |D_N|\le2K.
\tag{5}
\]

Order `D_N` by divisibility and let `mu_D(q,d)` denote the Möbius function of this **finite induced poset**, not the arithmetic Möbius function in (3). Define

\[
\boxed{
\kappa(D_N)
:=
\max_{d\in D_N}
\sum_{\substack{q\in D_N\\q\mid d}}
|\mu_D(q,d)|\frac qd.
}
\tag{6}
\]

Then

\[
\boxed{
\sum_{n\le N}|b_n|
\le
C N
\sum_{d\in D_N}
\sum_{\substack{q\in D_N\\q\mid d}}
|\mu_D(q,d)|\frac qd
\le
C N|D_N|\kappa(D_N)
\le
2CNK\kappa(D_N).
}
\tag{7}
\]

Thus `kappa(D_N)` is the weighted active-support inverse norm relevant to the exact-omission problem. In particular, if `kappa(D_N)=O(1)`, every `K=o(N)` exact-omission family is signed-coercive at macroscopic coefficient scale.

There is a large cross-scale class with a uniform bound. Suppose every nonminimal `d in D_N` has at most one maximal proper active divisor; equivalently, the Hasse diagram of the induced divisibility order has no downward merges. Then

\[
\boxed{\kappa(D_N)\le\frac32}
\tag{8}
\]

and hence

\[
\boxed{
\sum_{n\le N}|b_n|
\le\frac32 CN|D_N|
\le3CNK.
}
\tag{9}
\]

This class includes arbitrarily long divisibility chains. Consequently, **cross-scale chains alone do not amplify exact omissions beyond the linear `NK` scale**. Any family that hides macroscopic coefficient mass with `K=o(N)` exact omissions must develop an unbounded weighted incidence-Möbius norm, which requires more than primitive support or forest-like chains.

Quantitatively, if for some fixed `eta>0`

\[
\sum_{N/2<n\le N}|b_n|
\ge
\eta\sum_{N/2<n\le N}n,
\tag{10}
\]

then (7) forces

\[
\boxed{
\kappa(D_N)\gg \frac{\eta}{C}\frac NK.
}
\tag{11}
\]

Therefore a sublinear omission set can sustain macroscopic signed mass only if its active divisibility inverse becomes correspondingly ill-conditioned.

## The active-support inverse is a weighted incidence-zeta inverse

For every `d in D_N`, evaluate `b=1*g` at the active coordinate `d`:

\[
b_d
=
\sum_{\substack{q\in D_N\\q\mid d}}g(q).
\tag{12}
\]

Normalize the two vectors by their indices,

\[
\beta_d:=\frac{b_d}{d},
\qquad
x_d:=\frac{g(d)}d.
\tag{13}
\]

Then (12) becomes

\[
\beta_d
=
\sum_{\substack{q\in D_N\\q\mid d}}
\frac qd\,x_q.
\tag{14}
\]

Let `Z_D` be the ordinary zeta matrix of the induced divisibility poset and let `R=diag(d:d in D_N)`. The matrix in (14) is

\[
W_D=R^{-1}Z_D R.
\tag{15}
\]

Since `Z_D^{-1}` is the incidence Möbius matrix,

\[
\boxed{
W_D^{-1}(d,q)
=
\mathbf1_{q\mid d}\,\mu_D(q,d)\frac qd.
}
\tag{16}
\]

Hence (6) is exactly the induced `ell^infty` norm of this weighted inverse:

\[
\kappa(D_N)=\|W_D^{-1}\|_{\infty}.
\tag{17}
\]

The coefficient envelope (1) gives `|beta_d|<=C` on every active coordinate, so (16)--(17) imply

\[
\frac{|g(d)|}{d}=|x_d|
\le
C
\sum_{\substack{q\in D_N\\q\mid d}}
|\mu_D(q,d)|\frac qd.
\tag{18}
\]

This already identifies the conditioning object requested by the FD-247 frontier. It depends on the full incidence geometry, not only on the cardinality of `D_N`, its smallest element, or its harmonic footprint.

## Weighted incidence mass controls all coefficients below the horizon

For every `n<=N`,

\[
b_n
=
\sum_{\substack{d\in D_N\\d\mid n}}g(d).
\tag{19}
\]

Therefore

\[
\begin{aligned}
\sum_{n\le N}|b_n|
&\le
\sum_{d\in D_N}|g(d)|
\left\lfloor\frac Nd\right\rfloor\\
&\le
N\sum_{d\in D_N}\frac{|g(d)|}{d}.
\end{aligned}
\tag{20}
\]

Substituting (18) gives the first bound in (7), and taking the maximum weighted Möbius row sum gives the second. Equation (5) then gives the final `2CNK kappa(D_N)` estimate.

This sharpens the hierarchy from FD-245--FD-247. The finite omission-column bound of FD-245 controls amplitudes without inspecting divisibility geometry; FD-246 controls the reachable coefficient footprint from omission locations; FD-247 treats the zero-incidence case. Equation (7) keeps the entire active divisibility inverse instead of relaxing it to any of those coarser summaries.

## Divisibility forests have uniform inverse norm

Assume that each nonminimal `d in D_N` has a unique maximal proper active divisor, denoted `p(d)`. More generally, allow some elements to have no such predecessor. Because the poset is finite, every active divisor `q<d` must lie below a maximal active proper divisor of `d`; uniqueness therefore forces every interval below `d` to follow one predecessor chain.

Consequently, for the induced-poset Möbius function,

\[
\mu_D(q,d)
=
\begin{cases}
1,&q=d,\\
-1,&q=p(d),\\
0,&q<d\text{ and }q\ne p(d).
\end{cases}
\tag{21}
\]

The same formula follows directly from the finite Möbius recurrence: an interval of chain length at least two has zero endpoint Möbius value. Thus no external rooted-forest theorem is needed here.

Equation (16) now gives

\[
\sum_{q\mid d}|\mu_D(q,d)|\frac qd
=
\begin{cases}
1,&d\text{ minimal},\\
1+\dfrac{p(d)}d,&\text{otherwise}.
\end{cases}
\tag{22}
\]

Since a proper integer divisor satisfies `p(d)<=d/2`, every row is at most `3/2`. This proves (8). Equivalently, inversion on such support is simply

\[
g(d)=
\begin{cases}
b_d,&d\text{ minimal},\\
b_d-b_{p(d)},&\text{otherwise},
\end{cases}
\tag{23}
\]

so arbitrarily many multiplicative scales do not accumulate an inverse penalty along a chain.

This strictly extends the antichain case of FD-247. There `p(d)` never exists and the inverse norm is exactly one. Here long chains and arbitrary upward branching are allowed, provided two incomparable active divisor branches never merge into the same active multiple.

## Macroscopic hidden mass forces large incidence conditioning

The denominator in (10) satisfies

\[
\sum_{N/2<n\le N}n\asymp N^2.
\tag{24}
\]

Combining (10), (24), and (7),

\[
\eta N^2
\ll
CNK\kappa(D_N),
\]

which proves (11). Thus the growing-defect problem has a quantitative target: for `K=o(N)`, a bad exact-omission family must realize

\[
\kappa(D_N)\gtrsim N/K.
\tag{25}
\]

A mere divisibility relation, or even an arbitrarily deep chain, is far too weak. The active support must accumulate substantial incidence-Möbius mass. Nodes with several incomparable active predecessor branches are the first place where the forest formula (21) can fail, but one such merge is not by itself claimed to be sufficient; what matters is growth of the weighted inverse norm in (6).

The top-half construction of FD-246/FD-247 remains the sharpness control for the bounded-norm regime. Its active support is primitive, `kappa(D_N)=1`, and its coefficient mass is of order `NK`. Hence the linear dependence in (7) cannot be improved uniformly when the incidence norm stays bounded.

## Prior-art / novelty audit

Finite-poset Möbius inversion and the interpretation of the Möbius matrix as the inverse of the zeta matrix are classical incidence-algebra facts, going back at least to Rota's foundational treatment. Möbius functions on rooted-forest posets have also been studied explicitly. A targeted search around incidence algebras, rooted forests, divisibility posets and matrix conditioning did not reveal the weighted inverse norm (6) used as a finite-horizon exact-omission coefficient bound, nor the Farey/Mertens consequence (9)--(11).

No external theorem is load-bearing. Equations (12)--(23) are derived directly from the exact divisor inverse already established inside this line. Accordingly no new dependency is added to `SOURCES.md`, and no novelty is claimed for incidence algebras, poset Möbius inversion, or rooted-forest Möbius functions themselves. The line-specific contribution is the identification of the weighted induced-poset inverse as the exact conditioning statistic for the active omission increments, plus the uniform forest/chain consequence and the necessary `N/K` conditioning threshold.

## Boundary and next audit

This remains an exact-zero, signed response-space theorem. It does not improve the approximate-residual term of FD-242, and it does not impose positivity, finite prime-reservoir capacity, squarefree source realization, or full Möbius arithmetic coherence.

The statistic `kappa(D_N)` is computed from the **actual support of `g=Delta Y`**, not merely from the declared omission set. The next response-side audit is therefore concrete: determine how large `kappa(D_N)` can become for supports constrained by

\[
D_N\subseteq E_N\cup(E_N+1)
\]

with `|E_N|=K`, and identify which repeated merge patterns can make it grow. A proof that `kappa(D_N)=o(N/K)` throughout a sublinear-defect regime would give coercivity there; a construction with `kappa(D_N)\gtrsim N/K` would identify the incidence geometry needed to escape it.

## Status

**Proved.** The weighted incidence inverse formula, the coefficient-mass bound, the `3/2` forest norm, and the `N/K` necessary conditioning scale are exact finite statements. The result materially sharpens the FD-247 frontier by showing that long divisibility chains are harmless and that only growth of the weighted incidence-Möbius inverse can support superlinear exact-omission amplification. It does not by itself improve a physical Mertens bound or imply RH.