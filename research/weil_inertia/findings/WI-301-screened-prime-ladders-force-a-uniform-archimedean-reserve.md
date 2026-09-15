# WI-301 — dyadic screening forces a uniform archimedean reserve

**Status:** `EXACT-DERIVED + COMPUTATIONAL-INTERVAL + INDEPENDENT-REPLAY + CLASSICAL-REARRANGEMENT + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

Let

\[
c_0:=8.9\times10^{-18}.
\]

The independently replayed compact-window certificate of WI-300, combined with the source-side rearrangement inequalities of WI-298, gives an aperture-independent coercivity statement on a nonlinear screened class that is stronger than WI-300's first-crossing consequence.

Let `f` be a nonzero real compactly supported vector in the Weil form domain and suppose `f` has one global sign. Replace `f` by `-f` if necessary, so `f>=0`. Write

\[
C_f(h):=\int_{\mathbb R}f(x+h)f(x)\,dx
\]

and split the geometric Weil form as

\[
Q_W(f)=q_{\rm arch}(f)-\mathcal P(f),
\qquad
\mathcal P(f)
:=2\sum_{\Lambda(n)>0}\frac{\Lambda(n)}{\sqrt n}\,C_f(\log n).
\tag{1}
\]

Only finitely many terms in (1) are active for compactly supported `f`, and `\mathcal P(f)>=0` because `f>=0`.

Assume only that the powers-of-two ladder is screened:

\[
\boxed{
C_f(k\log2)=0\qquad(k\ge1).
}
\tag{2}
\]

Then

\[
\boxed{
q_{\rm arch}(f)\ge c_0\|f\|_2^2.
}
\tag{3}
\]

Consequently every one-signed `f` satisfying (2) and `Q_W(f)<=0` must carry a quantitative unscreened prime source:

\[
\boxed{
\mathcal P(f)\ge c_0\|f\|_2^2.
}
\tag{4}
\]

In particular, if **all** active prime-power autocorrelations are screened, then `\mathcal P(f)=0` and

\[
\boxed{
Q_W(f)\ge c_0\|f\|_2^2>0.
}
\tag{5}
\]

Thus no nonzero real one-signed compactly supported Weil test with `Q_W(f)<=0` can be completely prime-power screened. This removes the null-mode and first-crossing hypotheses from the branch exclusion of WI-300: complete one-signed screening is incompatible with nonpositivity at **any** aperture, not merely at the first Suzuki crossing.

## 1. Dyadic screening is a measurable packing constraint

Put

\[
L:=\log2.
\]

If `kL` is smaller than the essential span of `f`, (2) and nonnegativity give

\[
0=C_f(kL)=\int f(x+kL)f(x)\,dx,
\]

so

\[
f(x+kL)f(x)=0
\quad\text{for a.e. }x.
\tag{6}
\]

If `kL` is at least the span, (6) is automatic from compact support. Hence it holds for every nonzero integer `k`. For

\[
E:=\{x:f(x)>0\},
\]

this says that the translates `E+kL` are pairwise disjoint modulo null sets. Decomposing Lebesgue measure over a fundamental interval of `L\mathbb Z` gives

\[
\boxed{|E|\le L.}
\tag{7}
\]

This is the same elementary selector argument used in WI-281, but no null equation, eigenvector condition, or first-crossing hypothesis enters it.

Let `f^*` be the symmetric decreasing rearrangement. Equimeasurability preserves the `L^2` norm and the measure of the nonzero set, so

\[
\boxed{
\operatorname{supp}f^*\subseteq[-L/2,L/2],
\qquad
\|f^*\|_2=\|f\|_2.
}
\tag{8}
\]

Since

\[
\frac{L}{2}=\frac{\log2}{2}=0.346573590\ldots<0.8,
\tag{9}
\]

`f^*` lies inside the independently certified `L=0.8` window of WI-300.

The same packing argument with powers of three gives support length at most `log 3`, but that fact alone does **not** imply (3): after triadic rearrangement the smaller `log 2` prime shift can still overlap. The dyadic ladder is special here because `log 2` is the first prime-power lag.

## 2. The prime-deleted form decreases under rearrangement

The load-bearing point in WI-298 is stronger than its first-crossing headline. Its Sections 2--3 prove, for **every** nonnegative vector in the relevant form domain,

\[
G(f^*)\le G(f),
\qquad
P(f^*)\le P(f),
\]

where `G` is the gamma contribution and `P` the pole contribution. Therefore

\[
\boxed{
q_{\rm arch}(f^*)\le q_{\rm arch}(f).
}
\tag{10}
\]

No null-mode hypothesis is used in this step. The gamma inequality follows by applying Riesz rearrangement to bounded symmetric-decreasing truncations of the positive translation-difference kernel and then using monotone convergence; the same argument proves that `f^*` remains in the form domain. The pole inequality follows from the layer-cake representation of the increasing distance kernel `cosh(|x-y|/2)` and the Riesz inequality for close-pair mass.

The support in (8) has diameter at most `log 2`. Thus the `n=2` shift has at most a null endpoint overlap and every larger prime-power lag is outside the support. Hence all prime terms of `f^*` vanish:

\[
\boxed{Q_W(f^*)=q_{\rm arch}(f^*).}
\tag{11}
\]

Combining (10), (11), and WI-300's independently replayed compact-window certificate gives

\[
q_{\rm arch}(f)
\ge q_{\rm arch}(f^*)
=Q_W(f^*)
\ge c_0\|f^*\|_2^2
=c_0\|f\|_2^2,
\]

which proves (3).

## 3. Complete screening gives uniform coercivity at arbitrary aperture

If all active prime-power autocorrelations of `f` vanish, then in particular (2) holds, so (3) holds. Complete screening also makes the prime source in (1) vanish exactly. Therefore

\[
Q_W(f)=q_{\rm arch}(f)
\ge c_0\|f\|_2^2,
\]

which is (5). There is no Suzuki first-crossing parameter, no null equation, and no restriction on the original support radius. The fixed-window certificate is used only **after** rearrangement compresses the screened one-signed function into the first-prime window.

A useful contrapositive is quantitative. If `f>=0` satisfies dyadic screening and `Q_W(f)<=0`, then from (1) and (3)

\[
\boxed{
2\sum_{\Lambda(n)>0}
\frac{\Lambda(n)}{\sqrt n}
C_f(\log n)
\ge c_0\|f\|_2^2.
}
\tag{12}
\]

All powers-of-two terms vanish by (2), so the reserve must be paid by other prime-power lags. Equation (12) is an exact arithmetic-unscreening charge, although the present constant is tiny and the inequality does not identify which odd-prime lag carries it.

## 4. Certificate evidence and normalization

The numerical input is exactly WI-300's independently replayed theorem, not a new floating-point experiment. Mathia issue [#152](https://github.com/murillo128/mathia/issues/152) reconstructed Zhu's pinned arXiv:2608.24827v2 certificate from the geometric-side formulas using outward Arb arithmetic. The even `N=200,T=200` matrix plus analytic quadrature/tail controls and an independent exact-dyadic residual checker certify the floor `8.9e-18`; a separate odd `N=200,T=150` replay certifies `8.2065e-15`. The normalization audit against Suzuki gives scalar conversion exactly one. The full reproducible evidence is preserved in [issue comment 5678076696](https://github.com/murillo128/mathia/issues/152#issuecomment-5678076696).

An independent consistency calculation reproduces the replayed analytic constants

\[
A_{0.8}
=\sqrt2\log2+\frac{2}{\sqrt3}\log3+\log2
=2.9419735252236204555\ldots,
\]

\[
\beta_{200}
=\log\!\frac{200}{2\pi}-\frac1{200}-A_{0.8}
=0.5134667749150707383\ldots,
\qquad
\beta_{150}
=0.2241180357966231442\ldots .
\]

## 5. Prior art, novelty boundary, and limits

The compact-window coercivity constant is Zhu's v2 result; the localized Weil form is Suzuki's; the selector packing and Riesz rearrangement ingredients are classical and were already assembled line-locally in WI-281/WI-298. A targeted prior-art search around compact-window Weil positivity, Riesz rearrangement, and prime-power screening found the fixed-window theorem and the classical narrow-support literature, but not the aperture-independent screened-class consequence above. This is not a priority claim: the durable Mathia content is the exact implication obtained by combining independently validated inputs.

The one-sign hypothesis is essential. It is used twice: zero autocorrelation becomes pointwise disjointness because the integrand is nonnegative, and Riesz rearrangement orders the archimedean terms only for nonnegative functions. Sign-changing functions can screen by cancellation and are not constrained by this argument. Likewise, if the dyadic ladder is not screened, the selector bound need not hold. The result therefore does not establish unrestricted Weil positivity at large aperture and does not prove RH.

The structural message is narrower but rigid: **a one-signed nonpositive Weil test cannot hide all arithmetic interaction through screening.** If its powers-of-two overlaps vanish, a fixed positive archimedean reserve survives; nonpositivity then forces at least that reserve back into the remaining prime-power source. This is an exact defect-to-unscreening mechanism that no longer depends on first-crossing minimality.