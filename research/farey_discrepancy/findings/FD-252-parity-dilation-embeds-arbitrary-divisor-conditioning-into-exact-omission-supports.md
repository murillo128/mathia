# FD-252 — Parity dilation embeds arbitrary divisor conditioning into exact omission supports

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / support embedding / weighted incidence inversion / parity dilation / coefficient-pairing frontier
- **Depends on:** FD-225, FD-248, FD-251
- **Classification:** `EXACT-DERIVED + SUPPORT-EMBEDDING + NEGATIVE/OBSTRUCTION + COEFFICIENT-PAIRING-FRONTIER`

## Claim

Let `D` be any finite nonempty subset of `{1,...,N}` and let

\[
\kappa(D)
=
\max_{d\in D}
\sum_{\substack{q\in D\\q\mid d}}
|\mu_D(q,d)|\frac qd
\]

be the weighted incidence-Möbius inverse norm from FD-248, where `mu_D` is the Möbius function of the induced divisibility poset on `D`.

There is an **actual exact-omission response** `Y` on `{0,...,2N+1}` whose omission set is

\[
E=2D:=\{2d:d\in D\},
\]

such that, with `Y(0)=0`, `Y(2d)=1` for `d in D`, and `Y(m)=0` otherwise,

\[
\boxed{
\operatorname{supp}(\Delta Y)
=
2D\cup(2D+1)
=:D'.
}
\tag{1}
\]

Moreover the original induced divisibility intervals survive unchanged inside `D'`:

\[
\boxed{
\mu_{D'}(2q,2d)=\mu_D(q,d)
\qquad(q,d\in D,\ q\mid d).
}
\tag{2}
\]

Consequently

\[
\boxed{
\kappa(D')\ge \kappa(D).
}
\tag{3}
\]

Thus the special support geometry forced by exact omissions does **not**, by itself, lower the worst-case weighted divisibility conditioning. Every arbitrary finite divisor support embeds, after only a factor-two dilation of the ambient scale, into the bad-increment support of a genuine exact-omission response while preserving all original weighted Möbius rows as subrows.

The conclusion is specifically support-level. The constructed exact omission has the paired increment amplitudes

\[
\Delta Y(2d)=+1,
\qquad
\Delta Y(2d+1)=-1,
\tag{4}
\]

so an actual omission response does not have free coefficients on `D'`. Equation (3) concerns the support-only norm `kappa(D')`, whose inverse norm allows arbitrary input signs and amplitudes on that support. Therefore this finding does **not** prove that paired exact-omission data attain the same amplification as arbitrary support data. It proves that any improvement over FD-251 must use the coefficient pairing in (4), adjacent cancellation for more general omission patterns, or stronger source-side structure; support combinatorics alone cannot supply it.

## Exact omission support by parity dilation

Fix finite nonempty `D subset {1,...,N}`. Define

\[
Y(m)=
\begin{cases}
1,&m=2d\text{ for some }d\in D,\\
0,&\text{otherwise},
\end{cases}
\qquad 0\le m\le2N+1.
\tag{5}
\]

All omission points are even, hence no two are consecutive. Therefore for each `d in D`,

\[
\Delta Y(2d)=Y(2d)-Y(2d-1)=1,
\]

and

\[
\Delta Y(2d+1)=Y(2d+1)-Y(2d)=-1.
\]

Every other increment vanishes. The sets `2D` and `2D+1` are disjoint, so (1) follows exactly, not merely as the usual inclusion

\[
\operatorname{supp}(\Delta Y)\subset E\cup(E+1).
\]

This also gives a legitimate response-side coefficient sequence under the envelope used in FD-248. By the exact inversion from FD-225,

\[
g=\Delta Y,
\qquad
b=\mathbf 1*g,
\qquad
(\mathscr A b)(m)=Y(m).
\tag{6}
\]

Since every nonzero `g(r)` equals `+1` or `-1`,

\[
|b_n|
=
\left|\sum_{r\mid n}g(r)\right|
\le \tau(n)
\le n.
\tag{7}
\]

Thus no amplitude rescaling is needed: the construction already satisfies the normalized finite-horizon envelope `|b_n|<=n`.

## Why the original Möbius intervals survive

Take `q,d in D` with `q|d`. Consider the interval from `2q` to `2d` inside the induced divisibility poset on

\[
D'=2D\cup(2D+1).
\]

If `x in D'` belongs to that interval, then

\[
2q\mid x\mid2d.
\tag{8}
\]

The first divisibility in (8) forces `x` to be even. Hence **no odd companion `2s+1` can lie in an interval whose lower endpoint is one of the embedded even nodes**. The even elements of the interval are exactly

\[
\{2r:r\in D,\ q\mid r\mid d\}.
\tag{9}
\]

The map `r -> 2r` is therefore an isomorphism from the induced interval `[q,d]_D` onto `[2q,2d]_{D'}`. The Möbius function of a finite poset interval depends only on that interval, so (2) follows.

A useful stress-test is that `D'` is **not** generally a disjoint union of the even core and isolated odd companions. Odd companions can divide larger even core elements; for example `3|6`. The proof does not require global isolation. It uses only the stronger local fact relevant to the preserved rows: an odd node cannot occur above an even lower endpoint because divisibility by that even endpoint forces even parity.

## Weighted conditioning is inherited

Fix `d in D`. The row of the weighted inverse defining `kappa(D')` at upper node `2d` contains, among any additional terms, all embedded even divisors `2q` with `q in D` and `q|d`. For those terms, (2) gives the same Möbius coefficient and the weight is unchanged:

\[
\frac{2q}{2d}=\frac qd.
\tag{10}
\]

Hence

\[
\begin{aligned}
\sum_{\substack{x\in D'\\x\mid2d}}
|\mu_{D'}(x,2d)|\frac{x}{2d}
&\ge
\sum_{\substack{q\in D\\q\mid d}}
|\mu_{D'}(2q,2d)|\frac{2q}{2d}\\
&=
\sum_{\substack{q\in D\\q\mid d}}
|\mu_D(q,d)|\frac qd.
\end{aligned}
\tag{11}
\]

Taking the maximum over `d` proves (3). Any cross-edges contributed by odd companions can only add nonnegative absolute-value terms to the selected rows; they cannot erase the embedded conditioning.

## Extremal consequence

Define the unrestricted support extremal

\[
\mathfrak K(N)
:=
\sup_{\varnothing\ne D\subset[1,N]}\kappa(D),
\tag{12}
\]

and define the exact-omission support extremal `mathfrak K_om(H)` by taking the supremum of `kappa(supp(Delta Y))` over finite responses on `{0,...,H}` that vanish outside an arbitrary omission set. Every exact-omission bad-increment support is an ordinary subset of `[1,H]`, so

\[
\mathfrak K_{\rm om}(H)\le\mathfrak K(H).
\tag{13}
\]

Conversely, the parity-dilation construction applied to any `D subset[1,N]` gives

\[
\boxed{
\mathfrak K_{\rm om}(2N+1)
\ge
\mathfrak K(N).
}
\tag{14}
\]

Therefore the two support classes have the same power-law upper growth exponent:

\[
\boxed{
\limsup_{N\to\infty}
\frac{\log\mathfrak K_{\rm om}(N)}{\log N}
=
\limsup_{N\to\infty}
\frac{\log\mathfrak K(N)}{\log N}.
}
\tag{15}
\]

The statement also preserves an omission-count budget. If

\[
\mathfrak K(N,M)
:=
\sup_{\substack{D\subset[1,N]\\1\le|D|\le M}}
\kappa(D),
\]

then the construction uses exactly `|D|` omitted samples and gives

\[
\boxed{
\mathfrak K_{\rm om}(2N+1,M)
\ge
\mathfrak K(N,M),
}
\tag{16}
\]

where the left side restricts to responses with at most `M` omissions. Thus even in the polynomial-`K` window left by FD-251, the bare support constraint cannot improve the worst-case conditioning relative to arbitrary divisor supports of the same cardinality, up to constant dilation of the ambient horizon.

## Finite audit

Take

\[
D=\{1,3\}.
\]

The induced poset has `1|3`, hence

\[
\mu_D(1,3)=-1
\]

and the upper row at `3` has weighted absolute sum

\[
1+\frac13=\frac43.
\]

Parity dilation gives

\[
E=\{2,6\},
\qquad
D'=\{2,3,6,7\}.
\]

Although the odd companion `3` divides the even endpoint `6`, it cannot lie in the interval from `2` to `6` because `2` does not divide `3`. Hence

\[
\mu_{D'}(2,6)=-1= \mu_D(1,3),
\]

and the preserved even contribution to the row at `6` is again

\[
1+\frac26=\frac43.
\]

The additional node `3` may increase the full row norm; it cannot reduce the embedded contribution. This is the smallest example displaying the only subtlety in the proof: global odd-to-even divisibility is allowed, while the even-lower-endpoint intervals remain protected.

## Relation to FD-251

FD-251 proves the universal support bound

\[
\kappa(D)
\le N^{\rho_*-1+o(1)},
\qquad
\zeta(\rho_*)=2,
\qquad
\rho_*-1=0.7286472389\ldots .
\tag{17}
\]

It left open whether the genuine exact-omission support condition could lower that exponent. Equations (14)-(16) answer that question negatively at the level of `kappa`: **the class of exact-omission bad-increment supports is already universal enough to contain a conditioning-preserving copy of every finite induced divisibility support**.

This does not show that the exponent in (17) is sharp. It instead says that any sharper bound obtained solely by replacing an arbitrary support with `supp(Delta Y)` cannot improve the extremal exponent: arbitrary support complexity can be hidden inside an exact omission pattern by parity dilation.

The remaining exact-response problem is coefficient-level. For isolated omissions the increment vector is constrained to adjacent opposite pairs as in (4). With neighboring omissions, these pairs overlap and telescope rather than becoming free coordinates. A useful next object is therefore a **paired inverse norm** that keeps the map from omission amplitudes `Y(e)` to increments `Delta Y`, instead of replacing it by a free vector on `supp(Delta Y)`. A polynomial improvement there would be genuine new coercivity not contradicted by the support embedding above.

## Prior-art audit

The only general poset fact used is the standard interval-locality of the Möbius function: isomorphic finite intervals have the same Möbius coefficient. The parity-dilation construction and its application to exact-omission supports are elementary and are proved completely above.

A targeted search around incidence algebras, induced subposets, interval-preserving embeddings and divisibility-poset Möbius functions found the standard incidence-algebra framework but no result specific to the exact-omission adjacent-pair support generated here. No external theorem is load-bearing, so this finding adds no new source dependency to `SOURCES.md`.

## Boundaries and non-claims

The construction is response-side. Equation (7) gives the coefficient envelope used by the exact-omission analysis, but it does not make `b` a nonnegative prime-reservoir occupancy, enforce finite reservoir capacity, impose squarefree physical realization, or recover full arithmetic coherence.

More importantly, `kappa(D')` is an operator norm over **free** coordinates indexed by `D'`; the concrete response in (5) supplies the paired coordinates `(+1,-1)`. The large row realizing `kappa(D')` need not align with that paired subspace. Hence (3) must not be read as a lower bound on the actual coefficient mass generated by (5), nor as a countermodel to FD-251's coercivity conclusion.

The result instead removes one proposed source of improvement: exact-omission **support geometry alone** cannot reduce the universal conditioning exponent. Any further gain must survive the parity embedding by using information that the embedding does not preserve as free data—most naturally the adjacent amplitude pairing, or the independent source-admissibility constraints.

## Research consequence

FD-251 narrowed the live response-side frontier to the polynomial omission window and asked whether `D subset E union (E+1)` itself could force a smaller conditioning exponent. This finding closes that support-only branch.

The next response-side test should retain the actual linear map from omission amplitudes to paired increments and ask for its weighted inverse norm after composition with the induced divisibility inverse. Either that paired norm admits a stronger polynomial upper bound than `N^(rho_*-1+o(1))`, extending the coercive range, or a structured exact-omission family realizes polynomial amplification even under the pairing constraint. Support-only refinements of `kappa(D)` cannot decide between those alternatives.