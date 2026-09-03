# XF-004 — absolute-gap backward bootstraps cannot yield a fixed upper-bound gain

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for one-slice arguments that try to continue real-rootedness backward by proving a uniform positive lower bound for every absolute adjacent gap. The zero-counting input is classical; the collision-clock input is XF-003. The durable result is the exact incompatibility between those two ingredients.

## 1. Claim

Fix a time `t_0` for which `H_{t_0}` is real-rooted, and enumerate its positive real zeros in increasing order as

\[
0<x_1(t_0)\le x_2(t_0)\le\cdots .
\]

Let

\[
g_j(t_0)=x_{j+1}(t_0)-x_j(t_0).
\]

The classical zero-counting asymptotic for the de Bruijn--Newman deformation implies

\[
\boxed{
\inf_j g_j(t_0)=0.
}
\]

More quantitatively, every sufficiently large dyadic interval `[T,2T]` contains an adjacent gap

\[
\boxed{
g_j(t_0)=O_{t_0}\!\left(\frac1{\log T}\right).}
\]

On the other hand, XF-003 shows that if an adjacent pair is born in a simple double collision at time `t_*<t_0` and remains in the same real-simple adjacent regime up to `t_0`, then its squared gap satisfies

\[
g_j(t_0)^2<8(t_0-t_*).
\]

Hence a sufficient one-slice criterion of the form

\[
\forall j,\qquad g_j(t_0)^2\ge 8\varepsilon
\]

would indeed exclude every such simple collision in `(t_0-\varepsilon,t_0]`, but **it can never hold for any fixed `\varepsilon>0` for the Xi flow**. Therefore no method whose only global continuation input is a uniform positive absolute gap floor on one real-rooted slice can improve an upper bound for `\Lambda` by a fixed positive amount.

This is a method obstruction, not evidence that a collision actually occurs in every backward interval. It says that the obvious collision-age bootstrap suggested by XF-003 has zero global reach when compressed to the minimum absolute gap.

## 2. Zero density forces the absolute gap floor to vanish

For fixed `t`, the de Bruijn--Newman zero-counting function satisfies the classical asymptotic

\[
N_t(T)
=
\frac{T}{4\pi}\log\frac{T}{4\pi}
-\frac{T}{4\pi}
+\frac{t}{16}\log\frac{T}{4\pi}
+O_t(1),
\]

in the normalization used by the Polymath15 analysis. In particular,

\[
N_t(2T)-N_t(T)\asymp T\log T.
\]

If `M` zeros lie in an interval of length `T`, at least one of the `M-1` internal adjacent gaps is at most `T/(M-1)`. Therefore

\[
\min_{x_j,x_{j+1}\in[T,2T]} g_j(t)
\ll_t \frac1{\log T},
\]

and the global infimum of the absolute gaps is zero. This conclusion needs no pair-correlation conjecture and no RH assumption once the chosen slice is already known to be real-rooted.

Multiplicity only strengthens the obstruction: a multiple zero gives an absolute gap of zero immediately.

## 3. Why the XF-003 collision clock cannot be globalized by minimum gap

For a simple collision at `t_*`, XF-003 gives on the real-rooted forward side

\[
q'=8-4qS<8,
\qquad
q(t_*)=0,
\]

where `q=g^2` and `S>0` is the exterior inverse-square field. Thus

\[
q(t_0)<8(t_0-t_*).
\]

Consequently, if a pair had collided at some

\[
t_*\in(t_0-\varepsilon,t_0],
\]

then its descendant gap at `t_0` would satisfy

\[
g(t_0)<\sqrt{8\varepsilon}.
\]

So a uniform gap floor `g\ge\sqrt{8\varepsilon}` would be a legitimate finite-system non-collision certificate. The failure is not in this local implication; it is that the Xi zero set has increasing density, which makes every fixed absolute floor impossible.

This also shows the characteristic degeneration scale of the naive bootstrap. The smallest gaps forced merely by zero density are already of order `1/log T`, so the corresponding gap-squared collision clock is at most of order

\[
\frac1{(\log T)^2}.
\]

As `T\to\infty`, that time scale vanishes and cannot certify a fixed backward interval.

## 4. The obstruction is specifically infinite-dimensional

A finite real-rooted heat-flow polynomial with simple zeros has a positive minimum gap on any fixed collision-free slice. For such a finite system, XF-003's inequality can genuinely certify a small backward interval from that minimum gap.

The Xi obstruction comes from the unbounded zero count: the local length scale shrinks indefinitely with height. Thus finite particle simulations can systematically overstate the power of an absolute-gap continuation argument unless their limiting procedure tracks the shrinking microscopic spacing.

This is a line-specific warning for any truncation approach. A theorem proved at fixed particle number with a continuation time proportional to the square of the minimum unnormalized gap will generally lose all fixed-time content as the truncation height tends to infinity.

## 5. The scale-invariant exterior coupling survives the dimensional test

The exact XF-003 equation already identifies what does not automatically disappear under local rescaling. Under a dilation of local zero coordinates by a factor `a`,

\[
q\mapsto a^2q,
\qquad
S\mapsto a^{-2}S,
\]

so

\[
\boxed{qS\ \text{is scale invariant}.}
\]

By contrast, `q` alone carries the shrinking square-gap scale. This does not prove that `qS` is Xi-specific or sufficient to control `\Lambda`; XF-003 already shows that the sign of `S` is universal in real-rooted controls. It does identify the correct type of quantity for the next step: a fixed-time upper-bound mechanism must retain density-normalized exterior information, an integrated field, or another nonlocal observable instead of collapsing to the smallest absolute gap.

## 6. Prior art and current upper-bound context

The zero-counting asymptotic and the effective high-height analysis of `H_t` are part of the Polymath15 upper-bound program, D. H. J. Polymath, **Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn--Newman constant**, *Research in the Mathematical Sciences* 6 (2019), article 31. Platt--Trudgian's peer-reviewed verification of RH through height `3\cdot10^{12}` supplies the published numerical input that improved the established upper-bound benchmark to `\Lambda\le0.2` through that framework.

A 2026 crowdsourced optimization-constants record currently also lists a certificate-backed candidate `\Lambda\le3/16=0.1875`, merged as `teorth/optimizationproblems#126`, but the repository itself marks this bound with an asterisk for minimal external verification. The present finding does **not** use that candidate as established evidence; the absolute-gap obstruction applies at any real-rooted starting time and therefore is unchanged whether the starting benchmark is `0.2`, `0.1875`, or another positive value.

No novelty is claimed for the zero-counting formula, shrinking high-zero spacing, or classical zero-motion law. The Mathia-specific contribution is the exact method classification obtained by combining the counting asymptotic with XF-003: the local squared-gap clock is valid but cannot be promoted to a fixed global backward continuation by taking a minimum gap over the full Xi zero set.

## 7. Boundaries and falsification

The result rules out only **absolute-gap-floor** bootstraps. It does not rule out a height-dependent argument that couples each gap to its local density, to the exterior field `S`, or to a nonlocal barrier. It also does not address higher-multiplicity collisions directly, nor transitions realized only as a limiting phenomenon at heights tending to infinity; those possibilities make a minimum-gap-only proof no stronger.

A counterexample to this finding would require either a failure of the stated zero-counting asymptotic on a fixed real-rooted Xi slice or a fixed `\varepsilon>0` continuation theorem whose only global hypothesis is the one-slice absolute bound `g_j(t_0)^2\ge8\varepsilon` for every adjacent pair despite `\inf_j g_j(t_0)=0`. Neither is compatible with the established inputs above.

## 8. Consequence for `xi_flow`

XF-001 removed singular root labelling as a safe collision coordinate; XF-002 replaced it by an analytic discriminant; XF-003 showed that the exterior field gives a finite one-sided damping term. The present result closes the simplest global use of that local clock: **the minimum absolute gap cannot transport real-rootedness backward by any fixed time because the Xi microscopic spacing shrinks to zero with height**.

The live route is therefore scale-aware. The next useful target is a theorem controlling a density-normalized exterior quantity such as `qS`, or an integrated/collective version of it, strongly enough to distinguish the actual Xi field from matched real-entire controls with positive transition time.