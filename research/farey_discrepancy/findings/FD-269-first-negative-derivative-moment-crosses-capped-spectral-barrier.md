# FD-269 — The first negative derivative moment crosses the capped spectral barrier

- **Date:** 2026-09-22
- **Status:** proved bridge + conditional literature calibration
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** Mertens zero packet / negative moments of zeta derivative / frequency-capped Mellin complexity / square-root barrier / phase-sensitive frontier
- **Depends on:** FD-260, FD-261, FD-267, FD-268
- **Classification:** `EXACT-DERIVED + NEGATIVE-MOMENT-BRIDGE + CRITICAL-LINE-CALIBRATION + SQUARE-ROOT-COMPLEXITY + PHASE-CANCELLATION-FRONTIER`

## Claim

FD-268 reduced the Mellin-packet route to a concrete band-dependent complexity. At critical-line exponent `theta=1/2`, a simple zeta-zero residue

\[
\frac{t^\rho}{\rho\zeta'(\rho)},
\qquad \rho=\frac12+i\gamma,
\]

contributes to the capped complexity at depth `D` the weight

\[
\frac{(1+\min\{|\rho|,D\})^{1/2}}
{|\rho\zeta'(\rho)|}.
\tag{1}
\]

For the finite packet containing all positive critical-line zeros with `0<gamma<=D`, write

\[
\mathcal W_D
:=
\sum_{0<\gamma\le D}
\frac{(1+|\rho|)^{1/2}}
{|\rho\zeta'(\rho)|},
\tag{2}
\]

and define the first negative derivative moment

\[
J_{-1/2}(D)
:=
\sum_{0<\gamma\le D}\frac1{|\zeta'(\rho)|}.
\tag{3}
\]

Then, whenever the zeros in the packet are simple and lie on the critical line,

\[
\boxed{
\mathcal W_D
\gg
D^{-1/2}J_{-1/2}(D).
}
\tag{4}
\]

This converts the FD-268 spectral-complexity threshold into a standard negative-moment target. Since FD-261/268 require capped complexity larger than

\[
D^{1-\beta+o(1)},
\qquad
\beta=\log_2\frac32,
\tag{5}
\]

the first negative moment already supplies enough absolute spectral budget whenever

\[
\boxed{
J_{-1/2}(D)
\gg
D^{3/2-\beta+o(1)}
=
D^{0.9150374992\ldots+o(1)}.
}
\tag{6}
\]

Thus the threshold left by FD-268 is not asking for an exotic high-frequency tail. It can already be crossed by the ordinary critical zeros below the physical depth if their reciprocal-derivative first moment has essentially linear power growth.

There is a strong literature calibration. Heap--Li--Zhao prove, assuming RH and simple zeros, that for every fractional `k>=0`,

\[
J_{-k}(T)\gg T(\log T)^{(k-1)^2}.
\]

At `k=1/2` this gives

\[
J_{-1/2}(D)
\gg
D(\log D)^{1/4},
\tag{7}
\]

hence through the exact bridge (4)

\[
\boxed{
\mathcal W_D
\gg
D^{1/2}(\log D)^{1/4}.
}
\tag{8}
\]

The power `1/2` exceeds the FD-268 threshold

\[
1-\beta
=0.4150374992\ldots
\]

by

\[
\boxed{
\beta-\frac12
=0.0849625007\ldots .
}
\tag{9}
\]

Equation (4) is the new deterministic bridge. Equation (8) is a conditional prior-art calibration of that bridge, not an ingredient in its proof.

## 1. The capped norm contains the negative first moment

Under the critical-line specialization `rho=1/2+i gamma`,

\[
|\rho|=\sqrt{\gamma^2+\frac14}.
\]

For `0<gamma<=D` and `D>=2`, monotonicity of

\[
r\longmapsto\frac{\sqrt{1+r}}r
\]

for positive `r` gives

\[
\frac{(1+|\rho|)^{1/2}}{|\rho|}
\gg D^{-1/2}.
\tag{10}
\]

Multiplying by `1/|zeta'(rho)|` and summing immediately yields (4). No cancellation, zero-density estimate, explicit-formula truncation, or asymptotic for `J_{-1/2}` is used.

The same argument is unchanged if the real packet also contains conjugate zeros: the capped norm merely doubles. It is likewise insensitive to the first finitely many zeros. What matters is that frequencies up to the divisor depth `D` are in the unsaturated part of the FD-268 cap, where each zero residue is charged at scale `gamma^{-1/2}/|zeta'(rho)|`.

The exponent conversion is now immediate. If

\[
J_{-1/2}(D)=D^{\lambda+o(1)},
\]

then

\[
\mathcal W_D\ge D^{\lambda-1/2+o(1)}.
\tag{11}
\]

To clear the spectral threshold `1-beta`, it is enough that

\[
\lambda-\frac12>1-\beta,
\]

which is exactly `lambda>3/2-beta`, proving (6).

## 2. Natural inverse-derivative moments hit a square-root wall

There is a complementary upper-bound calculation explaining why standard magnitude moments naturally stop at the same `D^(1/2)` scale.

Fix `p>1`. On a dyadic zero block `X<gamma<=2X` with `X<=D`, suppose

\[
Z(X):=\#\{\rho:X<\gamma\le2X\}
\le X^{1+o(1)}
\tag{12}
\]

and

\[
A_p(X)
:=
\sum_{X<\gamma\le2X}|\zeta'(\rho)|^{-p}
\le X^{\sigma+o(1)}.
\tag{13}
\]

Hölder gives

\[
\sum_{X<\gamma\le2X}|\zeta'(\rho)|^{-1}
\le
Z(X)^{1-1/p}A_p(X)^{1/p}.
\tag{14}
\]

Since the FD-268 weight in this block is `asymp X^(-1/2)/|zeta'(rho)|`, its contribution to the capped norm is at most

\[
\boxed{
X^{1/2+(\sigma-1)/p+o(1)}.
}
\tag{15}
\]

In particular, a natural-scale inverse moment `A_p(X)<=X^{1+o(1)}` yields only

\[
\mathcal W_D\ll D^{1/2+o(1)}
\tag{16}
\]

after summing dyadic blocks. The power `1/2` is independent of `p`: taking higher fixed moments does not push the absolute capped norm below the FD-268 boundary.

More generally, for this Hölder route to certify an exponent strictly below `1-beta`, (15) would require

\[
\frac12+\frac{\sigma-1}{p}<1-\beta,
\]

or

\[
\boxed{
\sigma<1-p\left(\beta-\frac12\right).
}
\tag{17}
\]

For `p=2`, this means

\[
\sigma<0.8300749986\ldots .
\tag{18}
\]

So even an inverse-square moment upper bound of essentially linear size does not come close to pruning the route by absolute values. One would need a genuinely sublinear power estimate, not just sharper logarithms.

This section is a method barrier rather than a theorem about the true value of every negative moment. It says exactly what any magnitude-only moment estimate would have to achieve before it can force the FD-268 packet below threshold.

## 3. Why this changes the surviving spectral question

FD-268 left open whether the real zeta-zero packet can accumulate `D^(0.415...)` capped complexity. The bridge above shows that this is no longer the most informative question at the level of absolute residue magnitudes. Under the standard critical-line calibration, the first negative derivative moment alone naturally lives at a stronger `D^(1/2)` scale, and published conditional lower bounds already realize that power under RH plus simplicity.

But a large `mathcal W_D` is only a large **budget** in the triangle-inequality estimate of FD-268. It does not prove that the canonical repair field

\[
G_{F,N}(d)
=
\sum_{q\mid d}
\bigl(F(Nq)-F(N(q-1))\bigr)
\tag{19}
\]

actually has comparable one-sided mass. The modes carry phases from `N^rho`, from `q^rho-(q-1)^rho`, and from `1/(rho zeta'(rho))`. Those phases can cancel before or after divisor replication.

This relocates the useful frontier. Further attempts to make the absolute packet norm subpolynomial, or even merely `D^(0.415...)`, are pointed in the wrong direction for a full critical-zero packet: the known negative-moment scale is already larger. The next decisive object must be phase-sensitive, for example a signed or quadratic estimate for the actual replicated field, a correlation statement tying residue phases to the consecutive-difference kernel, or a truncation/remainder theorem showing that the large absolute packet budget cannot enter the relevant one-sided repair demand coherently.

Equivalently, FD-268 should now be read as an **upper envelope with enough raw capacity**, not as a likely route-pruning estimate. The obstruction has moved from spectral magnitude to spectral coherence.

## 4. Prior-art boundary and validation

Negative discrete moments of `zeta'(rho)` are classical. A targeted search identified Winston Heap, Junxian Li and Jing Zhao, *Lower bounds for discrete negative moments of the Riemann zeta function*, Algebra & Number Theory **16**(7) (2022), 1589--1625, DOI `10.2140/ant.2022.16.1589`, whose Theorem 1 proves under RH and simple zeros

\[
J_{-k}(T)\gg T(\log T)^{(k-1)^2}
\]

for fractional `k>=0`. Bui--Florea--Milinovich, *Negative discrete moments of the derivative of the Riemann zeta-function*, Bulletin of the London Mathematical Society **56** (2024), 2680--2703, DOI `10.1112/blms.13092`, records the same Gonek--Hejhal moment scale and the modern upper-bound landscape. Those results concern the zero moments themselves, not the consecutive-difference/divisor-replicated norm introduced in FD-268. The new content here is the exact exponent bridge (4)--(6) and its consequence for which kind of estimate can still matter in this line.

The bridge was independently checked numerically on the first 20 critical zeros. At `D=80`, using direct numerical differentiation of `zeta` at those zeros gives

\[
J_{-1/2}(80)\approx12.63297,
\qquad
\mathcal W_{80}\approx2.07877,
\]

while

\[
80^{-1/2}J_{-1/2}(80)\approx1.41235.
\]

The ratio is about `1.47`, consistent with the deterministic lower comparison. This computation is only a normalization audit; the proof of (4) is the one-line monotonicity argument above.

## Boundary

FD-269 does **not** prove that a truncated zero packet approximates `M(x)` with a sufficiently small remainder, and it does not turn the lower bound for `mathcal W_D` into a lower bound for the negative part of the actual repair coefficients. It also uses RH and simplicity only in the literature calibration (7)--(8); the deterministic bridge (4) is a statement about any finite simple critical-line zero packet.

The result does rule out a misleading next step: trying to close the spectral route merely by sharpening absolute residue-magnitude estimates until the FD-268 capped norm falls below `D^(1-beta)`. At the critical-line moment scale, that norm is already naturally of square-root size. The missing ingredient is cancellation or coherence of the **actual packet field**, not a smaller `l^1` residue ledger.

**Verdict.** The first negative derivative moment converts directly into capped Mellin complexity. Its critical-line scale is `D^(1/2+o(1))`, which sits above the `D^(0.415037...)` threshold left by FD-268. The spectral route therefore survives every magnitude-only test performed so far; the next useful test must be phase-sensitive.