# FD-182 — Exact dyadic midpoint null data do not control prime-extension multiplicativity

- **Date:** 2026-09-17
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** observation-kernel obstruction / dyadic midpoint sensing / prime-extension multiplicativity / rate-sharp non-observability
- **Depends on:** FD-179, FD-181
- **Classification:** `EXACT-DERIVED + PERMANENT-SOURCE + DYADIC-NULL + RELATIONAL-NONOBSERVABILITY + PRIME-FAN-CRITICAL-RATE`

## Claim

`FD-181` gives a quantitative source-faithfulness separator: for squarefree-supported perturbations of Möbius with support `o(x/log x)`, prime-extension multiplicativity defect below the critical scale forces the source to be exactly Möbius. The missing question was whether the Farey midpoint observations themselves could control that relation defect strongly enough to make the separator source-native.

They cannot, even with the entire exact dyadic ladder.

Fix `1<=q<infinity` and any finite cutoff `X`. There exists one permanent deletion-only source `a not equal mu` supplied by the `FD-179` construction such that

\[
a(n)\in\{0,\mu(n)\},
\qquad
a(n)=\mu(n)\quad(n\le X),
\tag{1}
\]

and

\[
\boxed{
P_a(2^m)=P_\mu(2^m)
\qquad(m\ge1).
}
\tag{2}
\]

Let

\[
S:=\{n:a(n)\ne\mu(n)\},
\qquad
C_S:=\sum_{n\in S}\frac1n.
\tag{3}
\]

The same construction has

\[
S(x)=x^{o(1)},
\tag{4}
\]

so `0<C_S<infinity`. Its deleted coordinates can be chosen composite, hence all prime coordinates remain physical. Therefore the exact fixed-prime asymptotic of `FD-181` applies:

\[
\boxed{
\mathcal M_{a,q}(x)
=
(C_S+o(1))\frac{x}{\log x},
}
\tag{5}
\]

where

\[
\mathcal M_{a,q}(x)
=
\sum_{(n,pn)\in E_x}
|a(pn)-a(p)a(n)|^q.
\tag{6}
\]

Equivalently, since `FD-181` uses

\[
|E_x|
=
\frac{x}{\zeta(2)}\log\log x+O(x),
\tag{7}
\]

we have

\[
\boxed{
(\log x\,\log\log x)^{1/q}
\left(
\frac{\mathcal M_{a,q}(x)}{|E_x|}
\right)^{1/q}
\longrightarrow
(\zeta(2)C_S)^{1/q}>0.
}
\tag{8}
\]

Thus exact zero dyadic midpoint error is compatible with prime-extension defect sitting exactly at the critical `FD-181` rate. In particular, no estimate derived only from the dyadic midpoint data can uniformly force

\[
\mathcal M_{a,q}(x)=o(x/\log x)
\tag{9}
\]

on this source class. The dyadic midpoint ladder is therefore **provably insufficient as the source-native bridge needed by `FD-180`--`FD-181`**. Any successful bridge must use a richer Farey observation family or a stricter source class.

## 1. The `FD-179` null source lies well inside the `FD-181` sparse regime

`FD-179` constructs, after any prescribed finite prefix, a nontrivial permanent deletion set `S` satisfying

\[
\log(2+S(x))
=
O_X\!\left(
(\log x)^{2/3}(\log\log x)^{2/3}
\right).
\tag{10}
\]

Hence

\[
S(x)=x^{o(1)}=o(x/\log x).
\tag{11}
\]

This is much smaller than the support threshold required by the coercive part of `FD-181`. Because the source is deletion-only,

\[
\delta(n):=a(n)-\mu(n)
=
-\mu(n)\mathbf 1_S(n),
\tag{12}
\]

so `|delta(n)|=1` on `S`.

The reciprocal mass in `FD-181` is therefore exactly `C_S`. It is positive because the source is nontrivial. It is finite because (10) implies, for every fixed `epsilon>0`, `S(t)<=t^epsilon` for all sufficiently large `t`; partial summation with any `epsilon<1` gives

\[
\sum_{n\in S}\frac1n<\infty.
\tag{13}
\]

The `FD-179` repair coordinates are the high-rank composites used by its dyadic block construction, so the prime coordinates remain `a(p)=-1`. Consequently all hypotheses of the exact asymptotic branch of `FD-181` are satisfied, and (5) follows immediately.

Even without using the fixed-prime refinement, the general `FD-181` lower bound already gives

\[
\liminf_{x\to\infty}
\frac{\log x}{x}\mathcal M_{a,q}(x)
\ge C_S>0,
\tag{14}
\]

which is enough for the non-observability conclusion.

## 2. Exact observational equality coexists with a critical relation defect

Define the finite dyadic observation vector at scale `x` by

\[
Y_x(a)
:=
\bigl(P_a(2^m)-P_\mu(2^m)\bigr)_{2^m\le x}.
\tag{15}
\]

Equation (2) says

\[
Y_x(a)=0
\qquad\text{for every }x,
\tag{16}
\]

not merely asymptotically or up to noise. Yet (5) says that the same permanent source satisfies

\[
\mathcal M_{a,q}(x)\asymp\frac{x}{\log x}.
\tag{17}
\]

This gives a direct nullspace obstruction. Suppose a proposed dyadic-to-relation estimate had the form

\[
\mathcal M_{b,q}(x)
\le
\Phi_x\bigl(Y_x(b)\bigr)
\tag{18}
\]

uniformly over any source class containing both Möbius and the `FD-179` source. Then necessarily

\[
\Phi_x(0)
\ge
(C_S+o(1))\frac{x}{\log x}.
\tag{19}
\]

Therefore no such estimate can have

\[
\Phi_x(0)=o(x/\log x).
\tag{20}
\]

The statement is independent of how nonlinear, adaptive, or discontinuous the reconstruction rule is: the two sources supply exactly the same complete dyadic midpoint data. A different norm on that same data does not help because the observation difference is literally zero.

The normalized version is rate-sharp relative to `FD-181`. Although

\[
\left(
\frac{\mathcal M_{a,q}(x)}{|E_x|}
\right)^{1/q}
\longrightarrow0,
\tag{21}
\]

it decays only at

\[
(\log x\,\log\log x)^{-1/q}
\tag{22}
\]

with a positive limiting constant after rescaling. This is exactly the boundary below which `FD-181` becomes rigid. The midpoint kernel therefore reaches the coercive threshold but cannot cross it.

## 3. What this rules out, and what remains open

The conclusion is narrower than saying that Farey observations cannot control multiplicativity. Complete Farey fields are source-invertible on much broader classes, so sufficiently rich spatial data can in principle recover the coefficients and then evaluate any source relation. The obstruction concerns the **sparse dyadic midpoint ladder** and every observation family whose kernel still contains the permanent `FD-179` source.

It also does not contradict the target-rigidity of `FD-172`--`FD-174`. Those results impose multiplicativity in the source class before interpreting the sparse midpoint data. `FD-182` instead shows that the midpoint data cannot manufacture that missing cross-coordinate law when the source class permits the `FD-179` null direction.

The live bridge question therefore becomes more concrete. One must either identify additional Farey spatial coordinates that destroy the `FD-179` kernel while quantitatively exposing enough prime-extension relations, or impose an independent source restriction strong enough to exclude that kernel. Merely sharpening an inequality involving the same dyadic midpoint samples cannot yield the `o(x/log x)` relation-energy estimate required by `FD-181`.

The separate cardinal question from `FD-181` remains open: support of size comparable to `x/log x` might or might not be sufficient to screen prime fans and drive relation energy below the critical rate. `FD-182` does not address that threshold; it shows instead that even a far sparser dyadic-null source already prevents the midpoint observations from proving subcritical relation energy.

## Representation audit

No representation is inverted or enriched in this pass. The observation side is exactly the physical dyadic midpoint sequence already used in `FD-179`; the destination side is exactly the prime-extension defect energy introduced in `FD-180` and generalized in `FD-181`. The result is a kernel-separation statement between two persisted objects.

The generic inverse-problem principle is simple: a functional cannot be uniformly controlled below a scale by measurements if one exact measurement-null source has functional value at that scale. The Farey/Möbius-specific content is that `FD-179` supplies such a permanent arithmetic null source and `FD-181` computes its prime-fan multiplicativity cost at the precise critical rate.

The deliberately discarded information is all non-midpoint Farey spatial data. Therefore the finding must not be read as a no-go theorem for complete Farey observations, consecutive midpoint histories, or stronger source classes.

## Prior-art audit

A targeted search was run for Farey midpoint/Möbius reconstruction, approximate multiplicativity of arithmetic functions, and nullspace obstructions in inverse problems. The search recovered generic nullspace principles from inverse-problem/compressed-sensing literature and standard work on multiplicative functions, but no direct analogue of the dyadic Farey midpoint kernel paired with prime-extension multiplicativity energy.

No external theorem is load-bearing here: the result is the exact composition of the already-persisted `FD-179` null-source construction with the already-persisted `FD-181` prime-fan asymptotic. `SOURCES.md` therefore needs no update.
