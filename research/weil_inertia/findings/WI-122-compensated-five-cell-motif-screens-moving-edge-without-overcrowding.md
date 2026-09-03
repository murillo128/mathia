# WI-122 — a compensated five-cell motif screens the moving-edge signal without number overcrowding

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. WI-121 rules out positive-density *long double-density* critical-screening islands using Fujii's unconditional mesoscopic number moments. The exact construction below shows that this does **not** by itself supply the extraction lemma left open by WI-120/WI-121. A mean-density periodic motif can contain a positive density of off-line mirror pairs, have uniformly bounded ordinate-count discrepancy, and nevertheless cancel the `Theta(M^2)` moving-edge response of those pairs down to a signed `Theta(M)` term by interference with ordinary simple critical-line zeros.

The consequence is deliberately narrow but decisive: **ordinate-count information alone cannot force cancellation of the WI-120 edge signal to manifest as mesoscopic overcrowding.** Any defect-to-zero continuation must control an additional signed pair/spectral statistic (or another zeta-specific observable) that sees the compensating ordinary-zero phase reservoir. This finding does not change Mathia's current unconditional simple-critical proportion and does not give a point process satisfying the full unconditional Montgomery form factor.

## 1. Frozen-scale zero-side motif

Keep the WI-120 normalization

\[
L=\log T,
\qquad
x=\gamma\frac{L}{2\pi},
\]

so mean zeta spacing is one in the unfolded ordinate `x`. Fix

\[
\boxed{y=\operatorname{arcosh}2},
\qquad \cosh y=2,
\qquad \sinh y=\sqrt3.
\tag{1}
\]

For each integer cell `n`, place one functional-equation mirror pair at ordinate

\[
x=5n,
\qquad
\beta=\frac12\pm\frac{y}{L},
\tag{2}
\]

and three simple critical-line zeros at ordinates

\[
x=5n+\frac12,
\qquad
x=5n+\frac32,
\qquad
x=5n+\frac52.
\tag{3}
\]

Thus every cell of unfolded length `5` carries exactly five zeros counted with multiplicity: two off line and three simple/on line. The off-line fraction in the motif is therefore exactly

\[
\boxed{\frac25}.
\tag{4}
\]

For comparison, replace each mirror pair in (2) by two critical-line labels at the same ordinate `x=5n`, leaving (3) unchanged. The two configurations then have **exactly the same ordinate multiset**. Reflecting the construction to negative ordinates supplies the usual conjugation symmetry, so the local labels respect the functional-equation/conjugation pattern relevant to the line.

This is an adversarial frozen-scale model, not a claim about the actual zeta zeros.

## 2. Every ordinate-count statistic is blind to the replacement

Let `mu` be the counting measure of either configuration in unfolded coordinates. It is periodic with period `5` and mass `5` per period. Hence every half-open interval of length `5` contains exactly five labels (away from irrelevant endpoint conventions). Writing `X=5q+r`, `0<=r<5`, gives uniformly in the starting point `u`

\[
\boxed{
\mu([u,u+X))=X+O(1),
}
\tag{5}
\]

with an absolute error independent of `X`.

In particular, on a mesoscopic window of `K -> infinity` mean spacings,

\[
\mu([u,u+K))=K+O(1),
\tag{6}
\]

rather than the `(1+eta)K` overcrowding used in WI-121. More strongly, because the mirror-pair and double configurations have identical ordinates, **all statistics formed only from `N(t+Delta)-N(t)` are exactly identical for the two configurations**, not merely their second or higher moments.

Thus Fujii's number-variance/moment input can rule out the long double-density island of WI-005/WI-121, but no amount of strengthening of an ordinate-only count statistic can distinguish the horizontal replacement (2) inside this compensated density-one environment.

## 3. Exact moving-edge algebra before the Montgomery weight

Take `N` complete cells and put

\[
M:=5N.
\tag{7}
\]

For real frequency `alpha`, define

\[
E_N(\alpha)
:=\sum_{n=0}^{N-1}e^{2\pi i(5n)\alpha}
\tag{8}
\]

and the three-simple-zero cell factor

\[
P(\alpha)
:=e^{\pi i\alpha}+e^{3\pi i\alpha}+e^{5\pi i\alpha}.
\tag{9}
\]

The critical-line simple zeros contribute `P(alpha)E_N(alpha)`. Because the off-line labels occur in a symmetric mirror pair, their horizontal factors sum to `2 cosh(y alpha)`. Therefore, with the Montgomery factor `w` temporarily replaced by `1`, the all-pairs Fourier amplitude of the mirror configuration is

\[
A_y(\alpha)
=\bigl(P(\alpha)+2\cosh(y\alpha)\bigr)E_N(\alpha),
\tag{10}
\]

whereas the double comparison is

\[
A_0(\alpha)
=\bigl(P(\alpha)+2\bigr)E_N(\alpha).
\tag{11}
\]

Consequently the pointwise mirror-minus-double difference is exactly

\[
\begin{aligned}
D_N(\alpha)
&:=|A_y(\alpha)|^2-|A_0(\alpha)|^2\\
&=4\bigl(\cosh(y\alpha)-1\bigr)
\Bigl(
\cosh(y\alpha)+1+\operatorname{Re}P(\alpha)
\Bigr)
|E_N(\alpha)|^2.
\end{aligned}
\tag{12}
\]

At the first support-one alias,

\[
P(1)=P(-1)=-3,
\qquad
\cosh y=2,
\]

so

\[
\boxed{D_N(1)=D_N(-1)=0.}
\tag{13}
\]

This is an exact unit-cell structure-factor cancellation. It is qualitatively different from the canonical WI-120 block, where a full lattice of mirror pairs with no compensating ordinary zeros has a positive `Theta(M^2)` response near the same alias.

## 4. The WI-120 edge profile leaves only a signed linear term

Use exactly the moving profile of WI-120. Fix nonzero

\[
\phi\in C_c^\infty((1/4,1/2)),
\qquad \phi\ge0,
\tag{14}
\]

and set

\[
r_M(\alpha)
=M\phi\bigl(M(1-|\alpha|)\bigr).
\tag{15}
\]

Its support lies in the two layers `|alpha|=1-Theta(1/M)` and its `L^1` norm is independent of `M`.

Write

\[
Q(\alpha)
:=\cosh(y\alpha)+1+\operatorname{Re}P(\alpha).
\tag{16}
\]

By (1), (9),

\[
Q(1)=Q(-1)=0,
\qquad
Q'(1)=y\sqrt3,
\qquad
Q'(-1)=-y\sqrt3.
\tag{17}
\]

For `s in [1/4,1/2]`, uniformly on that compact interval,

\[
Q\left(1-\frac{s}{M}\right)
=-\frac{y\sqrt3\,s}{M}+O(M^{-2}),
\tag{18}
\]

and the same first-order value holds at `-1+s/M`. Also

\[
\frac{|E_N(1-s/M)|^2}{N^2}
\longrightarrow
\left(\frac{\sin \pi s}{\pi s}\right)^2,
\tag{19}
\]

with the identical limit at the negative edge. Since `N=M/5`, substituting (18)--(19) into (12) and then (15) gives the exact asymptotic

\[
\boxed{
\frac1M
\int_{-1}^{1}r_M(\alpha)D_N(\alpha)\,d\alpha
\longrightarrow
-\frac{8y\sqrt3}{25}
\int_{1/4}^{1/2}
 s\phi(s)
\left(\frac{\sin\pi s}{\pi s}\right)^2ds
<0.
}
\tag{20}
\]

Thus the compensated motif does not merely reduce the canonical positive edge signal: it changes the mirror-minus-double response from `Theta(M^2)` to a **negative `Theta(M)` term**. The coefficient in (20) is strictly negative for every nonzero nonnegative `phi` in (14).

This is the decisive calculation. A positive density of off-line zeros is present, the ordinate process has no mesoscopic excess, and the moving-edge form supplies no positive superlinear charge that could be extracted from count regularity alone.

## 5. The exact Montgomery weight preserves the obstruction

WI-120 uses

\[
w(u)=\frac4{4-u^2}.
\tag{21}
\]

In a block of unfolded diameter `M`, actual vertical differences are `O(M/L)` and the horizontal differences in (2) are `O_y(1/L)`. Hence, for `M=o(L)`,

\[
w(\rho-\rho')=1+O_y\left(\frac{M^2}{L^2}\right).
\tag{22}
\]

The transform of `r_M` is uniformly bounded on the fixed horizontal strip relevant to (2), because `||r_M||_1` is fixed. There are `O(M^2)` ordered pairs, so replacing `w` by `1` changes either complete block form by at most

\[
O_{\phi,y}\left(\frac{M^4}{L^2}\right).
\tag{23}
\]

Choose any admissible mesoscopic scale satisfying

\[
M\to\infty,
\qquad
M=o(L^{2/3});
\tag{24}
\]

for example `M=L^{1/2}`. Then (23) is `o(M)`, so the exact weighted mirror-minus-double response obeys the same limit as (20):

\[
\boxed{
\frac{\Delta_M^{(w)}}{M}
\longrightarrow
-\frac{8y\sqrt3}{25}
\int_{1/4}^{1/2}
 s\phi(s)
\left(\frac{\sin\pi s}{\pi s}\right)^2ds.
}
\tag{25}
\]

Therefore the obstruction is not an artifact of dropping the Montgomery factor.

## 6. What this closes — and what it does not

WI-121 remains correct: a long exact critical lattice carrying two zeros at essentially every mean-spacing site forces a macroscopic local count excess and therefore cannot occur at positive density by Fujii's theorem. The present motif occupies a different extremal class. It keeps the **total** ordinate density equal to one by interleaving the mirror pairs with ordinary simple critical zeros, and those ordinary zeros simultaneously provide the phase needed to cancel the first edge alias.

Accordingly, the following hoped-for implication is false as an information principle:

\[
\boxed{
\text{cancellation of the WI-120 moving-edge mirror signal}
\;\Longrightarrow\;
\text{mesoscopic ordinate overcrowding}.
}
\tag{26}
\]

It is false even for a configuration with bounded count discrepancy and with functional-equation/conjugation-compatible mirror pairs. A successful extraction theorem must have a second branch that detects the **signed phase reservoir** supplied here by the ordinary critical zeros.

This is not a counterexample to a theorem using all established zeta information. The period-five motif has nontrivial reciprocal-lattice structure at fixed rational frequencies and is not claimed to satisfy the unconditional Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh form factor, let alone the full collection of known zeta statistics. Thus the live route after this finding is sharper rather than closed: combine the moving-edge observable with a fixed subcritical pair/spectral statistic capable of ruling out precisely this kind of compensation.

Nor does this model identify the actual uncertified complement. It only proves that `multiple/off-line + ordinary-simple` mixtures can defeat a count-only bootstrap even when the canonical long double-density screening background is unavailable.

## 7. Prior-art and novelty audit

The ingredients outside the Mathia-specific setup are classical. Periodic one-dimensional point patterns with strongly suppressed number fluctuations are standard examples in the hyperuniformity literature; see S. Torquato and F. H. Stillinger, **Local density fluctuations, hyperuniformity, and order metrics**, *Phys. Rev. E* 68 (2003), 041113, DOI `10.1103/PhysRevE.68.041113`. Cancellation of a reciprocal-lattice reflection by the Fourier transform of a multi-point unit cell is the classical structure-factor/systematic-extinction mechanism of diffraction theory.

Lagarias--Rodgers, **Higher Correlations and the Alternative Hypothesis**, *Q. J. Math.* 71 (2020), 257--280, DOI `10.1093/qmathj/haz043`, is nearby zeta-zero prior art showing that lattice-supported vertical configurations can survive all currently known fixed bandlimited higher-correlation tests. Their construction is not the present one: it does not model the off-line-mirror versus on-line-double ambiguity or the `T`-dependent edge profile of WI-120.

No novelty is claimed for periodic bounded discrepancy, structure-factor cancellation, Dirichlet-kernel asymptotics, or these prior-art observations. The durable line-specific deduction is the exact five-cell motif (2)--(3), the tuning `cosh y=2`, and the asymptotic (20)/(25), which together falsify a **count-only** extraction of the WI-120 horizontal signal after WI-121. A bounded targeted search did not locate this specific zeta-symmetry/moving-edge formulation; absence from the search is not a priority claim.

## 8. Research implication and decisive next test

The canonical long-lattice screen of WI-005 is no longer the only adversarial geometry that matters. After WI-121, the relevant exceptional configuration is a **compensated screen**: off-line mirror mass can coexist with ordinary simple critical mass at the correct total density, and the latter can destructively interfere with the moving support-edge observable.

The next useful bootstrap target is therefore a two-observable dichotomy. Starting from the exact WI-120 form, prove that if a positive density of mirror-pair blocks loses its `Theta(M^2)` edge response while all mesoscopic counts remain regular, then the compensating population must create a quantitatively detectable fixed-frequency pair/spectral defect (or another already-controlled zeta statistic). The five-cell motif supplies a sharp falsifier: any proposed lemma must classify it into that second branch rather than incorrectly forcing number overcrowding.

Conversely, a stronger adversarial construction that is simultaneously count-regular, screens the moving edge as in (25), **and** matches the established fixed support-one form factor would materially close the present escape. Until one of those two directions succeeds, WI-120 + WI-121 is not yet a defect-to-zero bootstrap.