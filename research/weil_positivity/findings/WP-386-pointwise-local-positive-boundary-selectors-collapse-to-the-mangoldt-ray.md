---
id: WP-386
title: Pointwise-local positive boundary selectors collapse to the Mangoldt ray
branch: weil_positivity
status: supported
kind: pointed-boundary-local-positive-measure-classification
claim_strength: exact RH-independent classification showing that any positive multiplication-form geometry on the WP-384 boundary coordinate which annihilates every mixed-prime boundary profile must be supported entirely on the canonical interval (0,1); on that interval every arithmetic profile equals Lambda(m)/sqrt(m), so the complete shell Gram and every local-anchor cross term collapse to one Mangoldt ray, leaving no independent archimedean or test-function channel
created: 2026-09-20
related: [WP-168, WP-381, WP-382, WP-383, WP-384, WP-385]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical Nyman--Beurling L2(0,1) geometry and its Mellin/Hardy reformulations
  - classical identity mu * log = Lambda
  - WP-384 fresh-prime boundary profile h_m
---

# WP-386 — Pointwise-local positive boundary selectors collapse to the Mangoldt ray

## Claim

`WP-385` rules out every closed positive boundary form that is stationary under the canonical dilation action. The most immediate escape is therefore to break scale stationarity while retaining the strongest possible notion of local positivity: multiply pointwise by an arbitrary positive measure in the canonical boundary coordinate.

For the `WP-384` boundary profiles

\[
h_m(x)=\frac1{\sqrt m}\sum_{d\mid m}\mu(m/d)
 a(x/d),
\qquad
a(x)=H_{\lfloor x\rfloor}-\log x-\gamma,
\tag{1}
\]

let `nu` be a positive Borel measure on `(0,infinity)` such that every arithmetic profile `h_m`, `m>1`, lies in `L^2(nu)`. Define the pointwise-local positive form

\[
Q_\nu(f,g)=\int_0^\infty f(x)\overline{g(x)}\,d\nu(x).
\tag{2}
\]

Then the following are equivalent:

\[
Q_\nu(h_m)=0
\quad\text{for every }m>1\text{ having at least two distinct prime divisors},
\tag{3}
\]

and

\[
\boxed{\nu([1,\infty))=0.}
\tag{4}
\]

Thus exact mixed-shell nullity does not merely constrain an arbitrary nonstationary local weight: it forces all of its mass into the single canonical interval `(0,1)`.

On that interval there is a second exact identity. For every `m>1`,

\[
\boxed{
h_m(x)=\frac{\Lambda(m)}{\sqrt m}
\qquad(0<x<1).}
\tag{5}
\]

Consequently, writing

\[
M_\nu:=\nu((0,1))<\infty,
\tag{6}
\]

one obtains for all `m,n>1`

\[
\boxed{
Q_\nu(h_m,h_n)
=M_\nu\frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}.
}
\tag{7}
\]

The whole arithmetic shell Gram therefore has rank at most one. More generally, for every admissible local anchor `g`,

\[
\boxed{
Q_\nu(h_m,g)
=\frac{\Lambda(m)}{\sqrt m}
\int_{(0,1)}\overline{g(x)}\,d\nu(x),
}
\tag{8}
\]

whenever the integral is defined. Any pointwise-local finite--global incidence has exactly the same one-dimensional shell dependence.

This result closes a genuine loophole left by `WP-385`: **dropping dilation covariance is not enough if positivity remains pointwise local in the source boundary coordinate**. The nonstationary local form can recover exact prime-power support, but only by collapsing onto the same Mangoldt ray already isolated by `WP-381`--`WP-383`; it does not produce the independent test-function family, Gamma term, polar term, or global counterterm required for a Weil positivity mechanism.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + FRESH-PRIME-BOUNDARY + POSITIVE-MEASURE-FORM + NONSTATIONARY-ALLOWED + EXACT-MIXED-NULLITY-CLASSIFICATION + CANONICAL-(0,1)-SUPPORT + MANGOLDT-RANK-ONE-COLLAPSE + MATCHED-CONTROL + DECISIVE-NEGATIVE + NOT-A-WEIL-BRIDGE`.

## 1. The interval `(0,1)` carries exactly the Mangoldt coefficient

If `0<x<1`, then `x/d<1` for every positive divisor `d`. Since `H_0=0`,

\[
a(x/d)
=-\log(x/d)-\gamma
=-\log x+\log d-\gamma.
\tag{9}
\]

Substitute this into (1). For `m>1`,

\[
\sum_{d\mid m}\mu(m/d)=0,
\tag{10}
\]

so the common `-log x-gamma` term cancels and

\[
\begin{aligned}
h_m(x)
&=\frac1{\sqrt m}
\sum_{d\mid m}\mu(m/d)\log d\\
&=\frac{(\mu*\log)(m)}{\sqrt m}
=\frac{\Lambda(m)}{\sqrt m}.
\end{aligned}
\tag{11}
\]

This proves (5). In particular, every mixed-prime profile vanishes identically on `(0,1)`, whereas a prime-power profile `m=p^k` is the nonzero constant

\[
h_{p^k}(x)=\frac{\log p}{p^{k/2}}.
\tag{12}
\]

The support interval is therefore not fitted after seeing prime labels. It is the first interval of the same floor/harmonic boundary coordinate already forced by the `WP-384` scaling limit.

## 2. Every positive local selector is forced onto `(0,1)`

The converse is the substantive rigidity statement. Fix `X>=1` and choose two distinct primes `p,q>X`. For every `x` in `[1,X]`, the three numbers `x/p`, `x/q`, and `x/(pq)` lie in `(0,1)`. The squarefree profile is

\[
h_{pq}(x)
=\frac1{\sqrt{pq}}
\bigl(a(x)-a(x/p)-a(x/q)+a(x/(pq))\bigr).
\tag{13}
\]

Using (9) for the three scaled arguments gives the exact cancellation

\[
\boxed{
h_{pq}(x)=\frac{H_{\lfloor x\rfloor}}{\sqrt{pq}}
\qquad(1\le x\le X).}
\tag{14}
\]

Since `H_floor(x)>=1` on `[1,X]`, this profile is strictly positive throughout that whole interval. But `pq` is a mixed-prime shell, so (3) and positivity imply

\[
0=Q_\nu(h_{pq})
\ge \int_{[1,X]}
\frac{H_{\lfloor x\rfloor}^2}{pq}\,d\nu(x).
\tag{15}
\]

Hence

\[
\nu([1,X])=0.
\tag{16}
\]

Because `X` was arbitrary, monotone exhaustion gives (4).

The reverse implication is immediate from (5): if `nu` is supported on `(0,1)`, every mixed-prime `m` has `Lambda(m)=0`, hence `h_m=0` `nu`-almost everywhere and (3) holds.

This proof is stronger than a countable common-zero-set argument. On every compact interval `[1,X]`, **one** mixed shell `pq`, with both primes larger than `X`, is already strictly positive everywhere and removes all positive measure there. No Mellin diagonalization, closure theorem, continuity assumption, or asymptotic prime-distribution estimate is used.

## 3. Positivity then forces a rank-one arithmetic Gram

Under the standing domain assumption, any prime profile belongs to `L^2(nu)`. Equation (12) then forces `M_nu<infinity`, establishing (6). With (4)--(5), polarization of (2) gives (7) directly.

Thus all prime powers survive, but they survive on one ray. If `M_nu>0`,

\[
Q_\nu(h_{p^k})
=M_\nu\frac{(\log p)^2}{p^k}>0,
\tag{17}
\]

while every mixed shell has zero energy. If `M_nu=0`, the entire arithmetic family is null. There is no intermediate pointwise-local positive measure capable of retaining a second independent arithmetic coordinate while preserving exact mixed-shell nullity.

The same collapse applies to cross terms. Let `g` be any function for which the local pairing is defined. Because each `h_m`, `m>1`, is constant on the support of `nu`, equation (8) follows. In particular, taking the universal base profile

\[
h_1(x)=a(x)=-\log x-\gamma
\qquad(0<x<1)
\tag{18}
\]

gives

\[
Q_\nu(h_m,h_1)
=\frac{\Lambda(m)}{\sqrt m}
\int_{(0,1)}(-\log x-\gamma)\,d\nu(x).
\tag{19}
\]

Changing the local measure can alter the scalar moment multiplying the Mangoldt coefficient and the self-energy of the anchor, but it cannot create a new shell-dependent archimedean response. This is the same structural bottleneck found from a very different representation in `WP-381`--`WP-383`.

## 4. Matched controls and falsification

The smallest familiar mixed control `m=6` illustrates why one fixed shell is not enough. Its profile vanishes on `(0,1)` but can have additional zeros for `x>=1`; therefore `Q_nu(h_6)=0` alone does not classify the support. The theorem needs the full exact mixed-shell requirement, and equation (14) shows precisely how fresh large primes eliminate the apparent loophole compact interval by compact interval.

Prime powers provide the positive control. Once the support has been forced into `(0,1)`, `p^k` has exactly the critical coefficient `log(p)/p^{k/2}` rather than a generic positive value. The theorem therefore does not incorrectly kill the desired arithmetic sector; it classifies the only way a positive local measure can retain it.

The result also survives singular and highly nonstationary choices of `nu`. Atoms, Cantor-type measures, discontinuous densities, and arbitrary scale-dependent weights are all allowed. This is why the theorem genuinely extends the search boundary beyond `WP-385`, which required a closed dilation-invariant form.

Several stronger conclusions are deliberately excluded. A positive nonlocal kernel

\[
Q_K(f)=\iint f(x)\overline{f(y)}\,dK(x,y)
\tag{20}
\]

can use off-diagonal cancellation and is not covered. Nor are derivative/interface energies, an indefinite finite--archimedean coupling before the final sign theorem, or a finite-`q` prelimit construction. Those are structurally different routes rather than technical gaps in (4).

## 5. Representation audit

**Intrinsic/source lens.** The profiles `h_m` and the coordinate `x` are not introduced for this theorem; they are the exact continuum boundary layer derived from the critically normalized primitive cyclotomic shells in `WP-384`. The threshold `x=1` is the first floor discontinuity of that source profile.

**Local-positive lens (primary).** A positive measure form is the most general zeroth-order pointwise-local positive geometry in this coordinate. No scale symmetry is imposed. Exact mixed-shell nullity says that every mixed source profile lies in the radical of this positive form, and positivity turns that into an almost-everywhere support statement.

**Log-scale lens.** Under `t=log x`, arbitrary positive measures are merely pushed forward and the forced support becomes the half-line `t<0`. The classification is unchanged; it is not an artifact of choosing multiplicative rather than logarithmic notation.

**Mellin lens.** Mellin transform converts multiplication in `x` into an off-diagonal convolution-type operation in frequency. Therefore this theorem is intentionally complementary to `WP-385`: it covers arbitrary local nonstationarity in the native boundary coordinate, while `WP-385` covers arbitrary diagonal spectral reweighting. Neither theorem licenses the claim that every positive form is excluded.

The representation-invariant consequence within the stated class is the rank-one shell response (7)--(8). What remains architecture-sensitive is locality itself. A surviving candidate must justify why a genuinely nonlocal/off-diagonal boundary coupling is source-forced and why its positivity is independent of the desired Weil conclusion.

## 6. Prior-art and novelty audit

The ingredients are classical. The convolution identity `mu*log=Lambda` is elementary multiplicative number theory. The distinguished interval `(0,1)` is central to the classical Nyman--Beurling formulation and its Hardy/Mellin variants; `SOURCES.md` already records Bagchi's account of the Nyman--Beurling--Baez-Duarte Hilbert-space criterion and Burnol's description of the corresponding Hardy/Mellin subspace. `WP-168` and `WP-384` already treat the Nyman carrier itself as prior art rather than a Mathia novelty.

A targeted literature check of Nyman--Beurling/Baez-Duarte formulations and the harmonic-floor/Mellin carrier did not locate the route-specific classification proved here: for the exact `WP-384` primitive-cyclotomic boundary profiles, arbitrary positive multiplication measures satisfying mixed-shell nullity are forced to `(0,1)` by the large-fresh-prime identity (14), after which the shell Gram collapses to the Mangoldt ray. No broad theorem-level novelty is claimed. The durable contribution is an exact Mathia search-boundary result.

The appearance of `(0,1)` should in fact lower, not raise, novelty claims. It shows that the only pointwise-local positive selector is driven into the classical Nyman region, where the finite arithmetic response becomes the already-known Mangoldt coefficient. This is not a new geometric proof of Weil positivity and it does not supply an independent sign theorem for RH.

## Consequence for the research line

`WP-385` left nonstationary boundary geometry as a live escape. The present classification splits that escape cleanly. **Nonstationary but pointwise-local positivity is exhausted:** exact mixed-shell nullity forces support to `(0,1)`, and there the arithmetic family is one-dimensional with coefficient `Lambda(m)/sqrt(m)`.

This is useful because it both recovers the desired finite support and explains why that recovery is insufficient. The same local geometry cannot independently manufacture the archimedean Gamma/polar structure or a nontrivial test-function family; every local anchor couples to the arithmetic shells through the same Mangoldt ray.

The next viable boundary experiment must therefore use structure that is genuinely nonlocal/off-diagonal in the native boundary coordinate, retain a finite-`q` term discarded by the continuum limit, or postpone exact mixed-shell selection until after a source-derived finite--archimedean interaction. Any such proposal should first be tested against the compact control behind (14): on every `[1,X]`, a single sufficiently large mixed squarefree shell is strictly positive everywhere, so pointwise-local positive cancellation is impossible there.

## Conclusion

The `WP-384` boundary layer admits an exact nonstationary positive selector, but it is completely rigid. A positive local measure annihilates every mixed-prime profile **if and only if** it is supported on `(0,1)`. On that interval every arithmetic profile is the constant `Lambda(m)/sqrt(m)`, so the entire shell Gram and every local-anchor incidence collapse to one Mangoldt ray.

This closes the simplest non-dilation-invariant escape from `WP-385` without assuming RH and without inserting zero data. It also sharpens the remaining target: any genuine Weil bridge carried by this boundary layer must obtain its missing degrees of freedom from a nonlocal/global coupling, not from another positive pointwise reweighting of the same continuum profile.
