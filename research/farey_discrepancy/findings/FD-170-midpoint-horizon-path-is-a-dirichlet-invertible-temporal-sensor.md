# FD-170 — Midpoint horizon path is a Dirichlet-invertible temporal sensor

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** restricted spatial acquisition / cross-horizon inversion / stability / information-boundary
- **Depends on:** FD-009, FD-116, FD-117, FD-167, FD-169
- **Classification:** `EXACT-DERIVED + TEMPORAL-ACQUISITION + DIRICHLET-INVERSION + SUBPOWER-STABILITY + NEGATIVE/ROUTE-RESTRICTION`

## Claim

The restricted-acquisition frontier left by `FD-169` behaves very differently when spatial scarcity is traded for **consecutive-horizon observation**. A single fixed spatial sample, at the apparently degenerate Farey midpoint `x=1/2`, is already an invertible temporal sensor for the whole source prefix.

Let

\[
a:\mathbb N\to\mathbb R,
\qquad
A(t):=\sum_{n\le t}a(n),
\tag{1}
\]

and let `\mathcal D_{H,a}` denote the source-controlled Farey field of `FD-117`/`FD-167`,

\[
\mathcal D_{H,a}(x)
=
x-\lfloor x\rfloor
+
\sum_{m\le H}
\bigl(\lfloor mx\rfloor-mx\bigr)
A\!\left(\left\lfloor\frac Hm\right\rfloor\right).
\tag{2}
\]

Put

\[
P_a(H):=\mathcal D_{H,a}(1/2),
\qquad H\ge1,
\tag{3}
\]

and use the algebraic baseline `P_a(0):=1/2`. If

\[
g_a(H):=P_a(H)-P_a(H-1),
\tag{4}
\]

then, with `u(n)=1` for odd `n` and `u(n)=0` for even `n`,

\[
\boxed{
 g_a=-\frac12\,(u*a)
}
\tag{5}
\]

under ordinary Dirichlet convolution. The Dirichlet inverse of `u` is

\[
\boxed{
 u^{-1}(n)=
 \begin{cases}
 \mu(n),&n\text{ odd},\\
 0,&n\text{ even},
 \end{cases}
}
\tag{6}
\]

so every coefficient is recovered explicitly from the consecutive midpoint path:

\[
\boxed{
 a(n)
 =-2
 \sum_{\substack{d\mid n\\ d\text{ odd}}}
 \mu(d)\,
 g_a(n/d).
}
\tag{7}
\]

Consequently the finite map

\[
(a(1),\ldots,a(K))
\longmapsto
(P_a(1),\ldots,P_a(K))
\tag{8}
\]

is invertible for every `K`; equivalently its lower-triangular determinant is `(-1/2)^K` after taking first differences. In particular,

\[
\boxed{
P_a(H)=P_\mu(H)\quad(1\le H\le K)
\Longrightarrow
 a(n)=\mu(n)\quad(1\le n\le K).
}
\tag{9}
\]

If the natural normalization `a(1)=1` is imposed, the same conclusion through index `K` follows from midpoint agreement only for `2<=H<=K`.

The physical path itself looks maximally uninformative:

\[
P_\mu(1)=0,
\qquad
P_\mu(H)=\frac12\quad(H\ge2).
\tag{10}
\]

Thus the information is not carried by variation of the physical midpoint value. It is carried by the **changing horizon operator**: requiring a synthetic source to reproduce the same stationary midpoint value at every consecutive horizon imposes a triangular family of distinct constraints whose Dirichlet inverse is the source itself.

## 1. Midpoint sampling turns the source-controlled field into an odd-divisor convolution

At `x=1/2`, the sawtooth from `FD-117` is exactly

\[
s_m(1/2)
:=\left\lfloor\frac m2\right\rfloor-\frac m2
=
\begin{cases}
-1/2,&m\text{ odd},\\
0,&m\text{ even}.
\end{cases}
\tag{11}
\]

Subtracting the horizon-`H-1` instance of (2) from the horizon-`H` instance is easiest after expanding the cumulative source:

\[
A\!\left(\left\lfloor\frac Hm\right\rfloor\right)
=\sum_{n\le H/m}a(n).
\tag{12}
\]

The non-affine part of (2) is therefore

\[
\sum_{mn\le H}s_m(1/2)a(n)
=
\sum_{q\le H}\sum_{mn=q}s_m(1/2)a(n).
\tag{13}
\]

Taking the first difference in `H` isolates the new diagonal `mn=H`:

\[
\begin{aligned}
g_a(H)
&=\sum_{mn=H}s_m(1/2)a(n)\\
&=-\frac12
\sum_{\substack{m\mid H\\m\text{ odd}}}
 a(H/m),
\end{aligned}
\tag{14}
\]

which is (5). The artificial value `P_a(0)=1/2` merely extends the same finite algebra to `H=1`; for every `H>=2`, (14) is the ordinary difference of two actual source-controlled Farey observations.

The matrix from `(a(1),...,a(K))` to `(g_a(1),...,g_a(K))` is lower triangular in the divisibility ordering and has diagonal entry `-1/2`, because the divisor `m=1` occurs in every row. Hence exact invertibility is already visible without any analytic input.

## 2. The inverse is an odd Möbius filter

The arithmetic function `u=1_{2\nmid n}` has Dirichlet series

\[
\sum_{n\ge1}\frac{u(n)}{n^s}
=(1-2^{-s})\zeta(s)
\tag{15}
\]

in the half-plane of absolute convergence. Multiplying by the Dirichlet series of the function

\[
\mu_{\rm odd}(n):=\mu(n)1_{2\nmid n}
\tag{16}
\]

gives identically one. Equivalently, directly at the coefficient level,

\[
\sum_{d\mid n}u(d)\mu_{\rm odd}(n/d)
=\mathbf 1_{n=1}.
\tag{17}
\]

Thus `u^{-1}=\mu_{\rm odd}`. Applying this inverse to (5) proves (7).

For the physical source `a=\mu`,

\[
u*\mu=\varepsilon-\mathbf 1_{n=2},
\tag{18}
\]

because `(1-2^{-s})\zeta(s)/\zeta(s)=1-2^{-s}`. Hence

\[
g_\mu(1)=-\frac12,
\qquad
g_\mu(2)=\frac12,
\qquad
g_\mu(H)=0\quad(H\ge3),
\tag{19}
\]

which yields (10) from the baseline `P_\mu(0)=1/2`. This is exactly the midpoint degeneracy already visible geometrically from Farey reflection and recorded in `FD-116`.

The important point is that the degeneracy is only a property of the **physical trajectory**. The observation operator on an arbitrary formal source is not rank one or stationary: its consecutive first differences are the invertible convolution (5).

## 3. Approximate midpoint matching has only subpower inverse loss

The exact classification also has a simple stability statement. Let

\[
E_H:=P_a(H)-P_\mu(H),
\qquad E_0:=0,
\tag{20}
\]

and write `\delta a=a-\mu`. Subtracting the physical and source-controlled versions of (5) gives

\[
E_H-E_{H-1}
=-\frac12(u*\delta a)(H),
\tag{21}
\]

so

\[
\boxed{
\delta a(n)
=-2
\sum_{\substack{d\mid n\\d\text{ odd}}}
\mu(d)
\bigl(E_{n/d}-E_{n/d-1}\bigr).
}
\tag{22}
\]

If

\[
\max_{0\le H\le K}|E_H|\le\epsilon,
\tag{23}
\]

then for every `n<=K`,

\[
\boxed{
|a(n)-\mu(n)|
\le
4\epsilon\,2^{\omega(n_{\rm odd})},
}
\tag{24}
\]

where `n_odd` is the odd part of `n`. The constant is deliberately coarse: each first difference costs at most `2 epsilon`, and the number of squarefree odd divisors is `2^{omega(n_odd)}`.

The same elementary maximal-prime-factor count used in `FD-168` gives, uniformly for `n<=K`,

\[
2^{\omega(n_{\rm odd})}
\le
\exp\!\left(O\!\left(\frac{\log K}{\log\log K}\right)\right)
=K^{o(1)}.
\tag{25}
\]

Therefore the temporal inverse is not uniformly conditioned as in the complete-field `L^2` theorem `FD-167`, but its worst finite-prefix amplification is only subpower. For an integer-valued source, any midpoint error satisfying

\[
4\epsilon
\max_{n\le K}2^{\omega(n_{\rm odd})}<1
\tag{26}
\]

forces exact equality `a(n)=\mu(n)` throughout the prefix.

This stability statement is in the `l^\infty` norm of the **horizon path**. It should not be confused with same-horizon field conditioning: temporal differencing is part of the inverse, and sparse or irregular horizon sampling does not inherit (22).

## 4. What this says about restricted acquisition

`FD-168` and `FD-169` study how much same-horizon Fourier information is needed to recover a source prefix. The present result shows that a different resource accounting gives a radically different answer. If consecutive horizons are available, spatial acquisition can collapse to one fixed point: `K` midpoint samples across `K` horizons contain the full `K`-coefficient formal source prefix.

This is not compression below target dimension. There are still `K` real observations for `K` real source coefficients. The result instead identifies a **space-time tradeoff**: one must count independent horizon constraints, not merely the number of spatial samples used at each horizon. A statement such as “one fixed Farey point is almost information-free” is false once the complete consecutive horizon history is admitted.

The midpoint is useful precisely because it is the strongest hostile control. For the physical Farey sequence its value is stationary after `H=2`; no visible fluctuation is being smuggled into the sensor. Yet matched controls cannot exploit that stationarity, because the synthetic midpoint equations change triangularly with `H`.

This also clarifies why the theorem does not contradict `FD-164`--`FD-166`. Finite-cutoff controls can move their freedom outward, and a sparse unbounded set of complete fields rigidifies a permanent source by exposing ever larger square-root prefixes. Here the spatial field has been reduced to one scalar, but the price is the **dense consecutive horizon hierarchy** needed to take the exact temporal differences in (14). For a sparse horizon set the triangular inversion is unavailable, and no rigidity claim is made.

Nor does the result create a new route to RH. It reconstructs the Möbius source; it does not prove new cancellation of that source or a stronger Franel--Landau destination bound. In fact it is partly a negative information-boundary result: a proposed argument that assumes exact or extremely accurate midpoint agreement at every consecutive horizon is already feeding in enough information to recover the target arithmetic coefficients.

## 5. Representation audit, prior art, and boundary

The algebraic engine is generic. Dirichlet convolution by any arithmetic function with nonzero first coefficient is triangularly invertible on every finite prefix. No novelty is claimed for that fact, for Möbius inversion, or for the inverse (6) of the odd-indicator function.

The Farey-specific splice is the `FD-117` source-controlled field and the midpoint identity (11). Together they turn one fixed **spatial** Farey sample across changing horizons into the explicit odd-divisor convolution (5). The strongest line-local point is therefore not a new abstract inversion theorem but the observation-model classification: the symmetry-degenerate midpoint, despite carrying a constant physical value for all `H>=2`, is source-complete when observed over consecutive horizons.

A fresh prior-art search around Farey midpoint ranks, local discrepancy at `1/2`, Möbius inversion and odd-divisor convolutions recovered the standard facts that `1/2` is the middle Farey term and the fixed-rational local-discrepancy/Mertens formulas represented by Rogelio Tomás García, *New Analytical Formulas for the Rank of Farey Fractions and Estimates of the Local Discrepancy*, Mathematics **13** (2025), 140. That paper is already anchored in `SOURCES.md` and is also the prior-art boundary used by `FD-116`. No external theorem beyond those existing anchors is load-bearing here, and no claim is made that the generic convolution inversion is novel.

The result has several sharp boundaries. It uses consecutive horizons; arbitrary sparse horizons are not covered. It is exact on the formal source-controlled model of `FD-117`; a different synthetic field model need not have the same triangular diagonal. The subpower stability estimate (24) is an upper bound, not asserted optimal. Finally, source recovery is not destination coercivity: even perfect knowledge of `a=mu` merely returns the original arithmetic problem.

Clue transition check: no accepted clue changes status. The result addresses the restricted/horizon-uniform acquisition branch exposed by `FD-169` rather than resolving the surviving gap-order or nonsquarefree-occupation clue programs.

## Research consequence

The observation frontier should now distinguish **same-horizon scarcity** from **cross-horizon temporal accumulation**. Same-horizon raw Fourier sampling has the nontrivial support geometry of `FD-168`, and unrestricted same-horizon mixing collapses to target rank by `FD-169`. In contrast, one fixed midpoint sample per consecutive horizon already realizes an explicit full-rank temporal transform.

A genuinely nontrivial compressed observation model must therefore restrict both axes: it cannot merely demand few spatial samples per horizon while silently allowing a consecutive horizon history whose length matches the target prefix. The remaining useful questions are sparse/nonconsecutive temporal acquisition, local/coarsened sensors with an explicit total space-time budget and noise geometry, source-specific compression on a smaller arithmetic admissible class, and—separately—the unresolved bridge from recovered source information to RH-critical Farey discrepancy coercivity.

## Related findings

- `FD-009` — consecutive floor/divisor compatibility is itself a triangular encoding of the Möbius prefix.
- `FD-116` — fixed rational anchor histories are periodic Möbius transforms; the physical midpoint is stationary after order two.
- `FD-117` — the complete source-controlled Farey field is an affine transform of the quotient cumulative source.
- `FD-167` — complete-field `L^2` inversion has uniform square-root-prefix conditioning.
- `FD-168` — same-horizon raw Fourier selectors have an exact coordinate-minimal prefix sampler.
- `FD-169` — unrestricted same-horizon mixed measurements collapse exact recovery to target rank.
