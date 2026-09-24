# PL-440 — The mod-5 orientation probes split into reflection anisotropy and a quadratic lag character

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CALIBRATED`; substantive reduction.

**Parent findings:** `PL-425`, `PL-438`, `PL-439`.

## Claim

`PL-439` expresses the two unresolved oriented coordinates of the mod-5 Schur gate through four real signed-residue energies. In the established reduced-residue order `(1,2,4,3)`, write

\[
A=(1,-1,1,1),\qquad
B=(1,1,1,-1),
\tag{1}
\]

and

\[
C=(1,1,-1,-1),\qquad
D=(1,-1,-1,1).
\tag{2}
\]

Then

\[
\Delta_s=J(A)-J(B)=8s,
\qquad
\Delta_f=J(C)-J(D)=8f.
\tag{3}
\]

Extend each probe to a function on `Z/5Z` by setting its value at residue `0` equal to zero, and define its circular lag autocorrelation by

\[
\mathcal C_w(h):=\sum_{a\bmod 5}w(a)w(a+h).
\tag{4}
\]

The two PL-439 differences have sharply different symmetry content:

\[
\boxed{\mathcal C_A(h)-\mathcal C_B(h)=0\quad\text{for every }h,}
\tag{5}
\]

whereas

\[
\boxed{\mathcal C_C(h)-\mathcal C_D(h)=4\chi_5(h),}
\tag{6}
\]

with `chi_5` the quadratic character modulo `5`, extended by `chi_5(0)=0`.

Consequently, for any centered quadratic source model whose pair kernel is **translation-stationary in the residue variable** and depends only on the additive lag `h`, the entire stationary contribution to `Delta_s` cancels identically, while the stationary contribution to `Delta_f` is exactly the quadratic-character lag twist of that kernel.

Thus the two load-bearing oriented coordinates of `PL-438` are not merely two arbitrary covariance directions. In source-adapted symmetry language:

- `s` measures a reflection/start-residue anisotropy channel invisible to every translation-stationary lag kernel;
- `f` contains the mod-5 quadratic lag-character channel, plus whatever nonstationary/start-residue anisotropy survives in the actual prime source.

This is an exact finite residue-space reduction. It is not an asymptotic estimate and does not establish the Schur gate or RH.

## 1. Exact residue-symmetry computation

In the ordinary residue order `0,1,2,3,4`, the four probes are

\[
A=(0,1,-1,1,1),\qquad
B=(0,1,1,-1,1),
\tag{7}
\]

and

\[
C=(0,1,1,-1,-1),\qquad
D=(0,1,-1,1,-1).
\tag{8}
\]

The first pair is related by reflection:

\[
B(a)=A(-a).
\tag{9}
\]

Circular autocorrelation is invariant under reflection, so

\[
\mathcal C_B(h)
=\sum_a A(-a)A(-a-h)
=\mathcal C_A(h),
\tag{10}
\]

which proves (5). Directly,

\[
\mathcal C_A=\mathcal C_B=(4,-1,1,1,-1)
\tag{11}
\]

for lags `h=0,1,2,3,4`.

For the second pair,

\[
D(a)=C(2a),
\tag{12}
\]

and therefore

\[
\mathcal C_D(h)=\mathcal C_C(2h).
\tag{13}
\]

A direct computation gives

\[
\mathcal C_C=(4,1,-3,-3,1),
\qquad
\mathcal C_D=(4,-3,1,1,-3).
\tag{14}
\]

Their difference is

\[
(0,4,-4,-4,4)
=4(0,1,-1,-1,1)
=4\chi_5,
\tag{15}
\]

which proves (6).

No analytic continuation, Euler product, positivity, or RH assumption enters (5)--(15).

## 2. Projection of a stationary pair kernel

Suppose a centered quadratic form on residue probes has the translation-stationary shape

\[
Q_{\rm stat}(w)
=\sum_{h\bmod5}\kappa(h)\mathcal C_w(h)
\tag{16}
\]

for some real lag kernel `kappa`. Then (5) implies

\[
Q_{\rm stat}(A)-Q_{\rm stat}(B)=0,
\tag{17}
\]

while (6) gives

\[
Q_{\rm stat}(C)-Q_{\rm stat}(D)
=4\sum_{h\bmod5}\chi_5(h)\kappa(h).
\tag{18}
\]

Thus the stationary projection of the PL-439 oriented pair is exactly

\[
(\Delta_s^{\rm stat},\Delta_f^{\rm stat})
=\left(0,\,4\sum_h\chi_5(h)\kappa(h)\right).
\tag{19}
\]

Combining with `PL-439`,

\[
s=\frac{\Delta_s}{8},
\qquad
f=\frac{\Delta_f}{8},
\tag{20}
\]

so a nonzero `s` cannot arise from the translation-stationary residue-lag component at all. It must come from the part of the actual covariance that remembers the starting residue, from a centering/boundary asymmetry, or from another explicitly nonstationary source term.

Likewise, the stationary part of `f` is not an arbitrary lag average: it is precisely its `chi_5` Fourier/character projection.

## 3. Relation to the current arithmetic target

`PL-438` reduces local-factor positivity to the Schur ellipse

\[
(g-\mu)^TE^{-1}(g-\mu)\le\alpha,
\tag{21}
\]

with

\[
g=\frac1{\sqrt2}(s-f,s+f)^T.
\tag{22}
\]

`PL-439` then realizes `s,f` through four real signed-residue energies. The present decomposition identifies the **symmetry type** of the two paired differences before any number-theoretic estimate is attempted.

For the prime source, it is therefore useful to decompose the centered pair covariance into a residue-translation-stationary part plus an anisotropic remainder. Under that decomposition:

\[
\Delta_s=\Delta_s^{\rm aniso},
\tag{23}
\]

while

\[
\Delta_f
=4\sum_h\chi_5(h)\kappa(h)
+\Delta_f^{\rm aniso}.
\tag{24}
\]

Equations (23)--(24) do not by themselves prove either term small. They replace a generic two-dimensional covariance target by two source-specific questions: control of reflection/start-residue anisotropy and control of one explicit quadratic-character lag twist.

This is potentially useful because those two modes are arithmetically different. The first is killed by exact translation-stationary symmetry; the second survives that symmetry but lies in a single nonprincipal mod-5 character channel.

## 4. Literature calibration and novelty audit

The algebra in (5)--(18) is elementary finite Fourier/correlation theory and carries no standalone novelty claim. The durable line-specific content is the identification of the exact `PL-439` probes with these two symmetry modes at the current `PL-438` Schur gate.

`PL-425` already records the relevant prior-art warning from Kuperberg-type singular-series analysis: nonprincipal fixed-modulus character contributions can be strongly suppressed in averaged prime-pattern models. The present calculation is consistent with that picture, but it does **not** strengthen the existing asymptotic theorem. In particular, it does not convert model-level square-root suppression into the variance-scale fixed-source estimate needed by (21).

The current line audit in `PL-434`--`PL-439` also remains binding: available almost-all short-interval and Hardy--Littlewood technology does not yet supply the required second-order estimate for the exact centered fixed-mod-5 source. The present finding narrows the analytic object to be estimated; it does not close that gap.

No novelty claim is made for reflection invariance of autocorrelation, character projection of a circulant kernel, or the identity `chi_5=(0,1,-1,-1,1)`. The substantive delta is only the source-adapted decomposition of the line's already-accepted oriented Schur defect.

## 5. Adversarial audit and boundaries

1. **The actual prime covariance need not be residue-stationary.** Equation (17) is exact only for the component represented by a lag-only kernel. A pair kernel `K(a,b)` that depends on the starting residue `a`, not merely `b-a`, can contribute to `Delta_s` and alter `Delta_f`.

2. **The zero-at-residue-0 extension is a bookkeeping device for reduced residues.** It does not assert that the prime source has no contribution from the residue `0 mod 5`; the established centered source and its treatment of the local prime `5` must be inherited from the parent findings.

3. **Centering and interval boundaries remain load-bearing.** Moving-window subtraction or endpoint terms can break the ideal translation-stationary form and therefore enter the anisotropic remainder.

4. **A character projection is not automatically small.** Equation (18) identifies the mode exactly, but cancellation at the variance scale still requires an arithmetic theorem. A generic bound on `kappa`, a total variance estimate, or first-order equidistribution does not suffice.

5. **Kuperberg calibration is not a proof for this source.** Square-root suppression in an averaged singular-series model cannot be substituted for the fixed-modulus moving-prime covariance estimate required by the Schur ellipse.

6. **No RH implication follows from the symmetry split alone.** Even perfect control of the stationary projection would leave the nonstationary remainder to be bounded strongly enough to satisfy (21).

## Consequence for the line

The next arithmetic search need not target a generic complex covariance matrix. It can ask two narrower and falsifiable questions on the canonical centered mod-5 source:

\[
\boxed{\text{How large is the reflection/start-residue anisotropic component measured by }\Delta_s?}
\tag{25}
\]

and

\[
\boxed{\text{How large is the quadratic lag-character component }\sum_h\chi_5(h)\kappa(h)\text{, together with its anisotropic remainder?}}
\tag{26}
\]

Any theorem or obstruction at the true variance scale for these two modes feeds directly into the exact source vector `g` of `PL-438`; results only for total scalar variance or residue-diagonal balance still do not resolve the gate.