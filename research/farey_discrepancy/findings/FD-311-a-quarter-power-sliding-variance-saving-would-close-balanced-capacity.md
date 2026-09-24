# FD-311 — A quarter-power sliding-variance saving would close balanced capacity

- **Date:** 2026-09-24
- **Status:** proved an exact theorem-design threshold for source-selected short-interval variance and isolated the balanced-depth target
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** block-Mertens source / sliding short intervals / second moment / theorem-design barrier / balanced depth / prior-art boundary
- **Depends on:** FD-300, FD-303, FD-304, FD-307, FD-310
- **Classification:** `EXACT-DERIVED + CONDITIONAL-THEOREM-TEMPLATE + VARIANCE-THRESHOLD + RH-ASPECT-RATIO-LOCALIZATION + PRIOR-ART-AUDIT + FRONTIER-REFINEMENT`

## Claim

Let

\[
c:=1-\log_2(3/2)=0.4150374992\ldots
\tag{1}
\]

and retain the near-capacity premise

\[
L_N(x)\ge N^{1/2}x^{1+c-o(1)},
\qquad
x=N^{\lambda+o(1)}.
\tag{2}
\]

FD-300 supplies a dyadic shell `Q<q<=2Q`; put

\[
X:=NQ
\tag{3}
\]

and define the complete sliding length-`N` Möbius second moment on the corresponding fixed dyadic start interval by

\[
J_\mu(X,N)
:=
\sum_{X\le y<2X}
\left|M(y+N)-M(y)\right|^2.
\tag{4}
\]

FD-303 gives the deterministic lower bound

\[
\boxed{
\frac{J_\mu(X,N)}{XN}
\ge
N^{3c\lambda-1/2-o(1)}.
}
\tag{5}
\]

Equivalently,

\[
\boxed{
J_\mu(X,N)
\ge
X N^{1/2+3c\lambda-o(1)}.
}
\tag{6}
\]

The trivial second-moment ceiling is `J_mu(X,N)<=XN^2`. Consider a theorem template on the **same source-selected dyadic window**:

\[
\boxed{
J_\mu(X,N)
\le
X N^{2-\eta+o(1)}
}
\tag{7}
\]

for some fixed power saving `eta>0`. Comparing (6) and (7), the near-capacity premise is impossible whenever

\[
\boxed{
\eta>
\eta_{\rm var}(\lambda)
:=
\frac32-3c\lambda.
}
\tag{8}
\]

This is an exact theorem-design threshold within the FD-303 variance reduction. Equality is only tangency because both sides carry `o(1)` losses.

At balanced depth `lambda=1`,

\[
\boxed{
\eta_{\rm var}(1)
=
\frac32-3c
=
0.2548875021\ldots .
}
\tag{9}
\]

Therefore **any fixed improvement beyond a `0.254888` power of `N` from the trivial sliding second moment closes the balanced near-capacity route**. Concretely, for any fixed `epsilon>0`, an estimate

\[
\boxed{
J_\mu(X,N)
\ll
X N^{1.7451124978-\varepsilon}
}
\tag{10}
\]

uniformly on the source-selected windows is enough.

The same threshold has an RMS formulation. From (6), near-capacity forces

\[
\boxed{
\left(
\frac1X J_\mu(X,N)
\right)^{1/2}
\ge
N^{\sigma_{\rm var}(\lambda)-o(1)},
\qquad
\sigma_{\rm var}(\lambda)
:=
\frac14+\frac{3c}{2}\lambda.
}
\tag{11}
\]

Hence a uniform short-sum theorem of the stronger pointwise form

\[
|M(y+N)-M(y)|
\le
N^{\sigma+o(1)}
\qquad (X\le y<2X)
\tag{12}
\]

would kill near-capacity whenever

\[
\boxed{
\sigma<\sigma_{\rm var}(\lambda).
}
\tag{13}
\]

At balanced depth this critical RMS exponent is

\[
\boxed{
\sigma_{\rm var}(1)
=
\frac14+\frac{3c}{2}
=
0.8725562489\ldots .
}
\tag{14}
\]

Thus the balanced problem does **not** require square-root cancellation in every length-`N` interval. On the variance route, it is enough to beat RMS size `N^(0.872556...)` by any fixed power.

## 1. The variance barrier follows directly from FD-303

FD-303 starts from the shell energy forced by FD-300 and thickens each large aligned block into nearby sliding starts using only the Lipschitz property of a length-`N` sum with coefficients bounded by one. Its conclusion, in the fixed polynomial regime (2), is exactly (5).

Multiplying (5) by `XN` gives

\[
J_\mu(X,N)
\ge
X N^{1/2+3c\lambda-o(1)},
\tag{15}
\]

while (7) supplies

\[
J_\mu(X,N)
\le
X N^{2-\eta+o(1)}.
\tag{16}
\]

A fixed-power contradiction occurs precisely when

\[
\frac12+3c\lambda
>
2-\eta,
\tag{17}
\]

which rearranges to (8).

Several checkpoints are useful. At the first depth where FD-303 already forces superdiagonal variance,

\[
\lambda=\frac1{6c}=0.4015701399\ldots,
\tag{18}
\]

one has `eta_var=1`. Thus the natural diagonal-scale estimate `J_mu<<XN^(1+o(1))` is exactly tangent there. At the common-window threshold used by FD-304 and FD-307,

\[
\lambda_{\rm cw}
=
\frac3{10c}
=
0.7228262519\ldots,
\tag{19}
\]

one has

\[
\eta_{\rm var}(\lambda_{\rm cw})=0.6.
\tag{20}
\]

At the unconditional source ceiling of FD-300,

\[
\lambda_{\rm src}
=
\frac1{2c}
=
1.2047104198\ldots,
\tag{21}
\]

one has `eta_var=0`: any fixed power saving from the trivial second moment would already enter below the source ceiling. The threshold therefore decreases linearly from the diagonal requirement at shallow depth to an arbitrarily small fixed power saving at the source boundary.

This also clarifies what FD-303 has already bought. The unresolved theorem is not a full square-root cancellation statement. It is a quantitative exclusion of an **inflated second moment** whose permitted exponent is explicitly known.

## 2. Balanced depth lives at a very specific polynomial short-interval geometry

To compare this target with short-interval literature, now assume RH only for the shell localization of FD-304. Write

\[
Q=x^{\rho+o(1)},
\qquad
2c\le\rho\le1.
\tag{22}
\]

Since `X=NQ` and `x=N^(lambda+o(1))`, the interval length `N` relative to its ambient position `X` is

\[
N=X^{\beta+o(1)},
\qquad
\boxed{
\beta=
\frac1{1+\lambda\rho}.
}
\tag{23}
\]

At balanced depth `lambda=1`, the full RH-allowed shell range becomes

\[
\boxed{
\frac12
\le
\beta
\le
\frac1{1+2c}
=
0.5464256934\ldots .
}
\tag{24}
\]

So the theorem requested by (10) is not an unspecified short-interval estimate: it is a mean-square estimate for Möbius sums of length approximately `X^beta` with `beta` between `0.5` and `0.54643`, on the exact dyadic window selected by the Farey source.

The currently anchored short-interval results do not supply the fixed-power variance saving (9). Matomäki--Teräväinen gives all-interval Möbius cancellation for fixed interval exponent `theta>0.55`, which is already just above the entire balanced band (24), and its saving is logarithmic rather than a fixed power of the interval length. Matomäki--Radziwiłł II gives quantitative almost-all short-interval control with power-saving exceptional-set information, but the amplitude saving available from that theorem is again not a fixed power sufficient to imply (10). The 2026 higher-uniformity theorem gives arbitrary fixed log-power Möbius cancellation outside a log-power exceptional set for `H>=X^(1/3+epsilon)`; after the exceptional set is bounded trivially, this still yields only log-power savings from the `XN^2` second-moment scale.

Thus none of those anchored results is being used as a hidden proof of (10). They instead locate the literature boundary: the missing input is a **fixed-power `L^2` saving** in a polynomial interval-length regime near the square-root scale.

## 3. This is a different target from the pointwise Fourier barrier in FD-310

FD-310 considered a principal-frequency pointwise theorem

\[
|F_X(\alpha)|
\le
X^{1/2+o(1)}
(1+X\|\alpha\|)^\theta
\tag{25}
\]

and found that balanced depth requires `theta<0.2739244180...` to eliminate every carrying shell. The variance threshold (9) is not numerically comparable to that `theta`: the exponents measure different theorem classes.

The structural distinction is more important. FD-310 asks for a uniform pointwise estimate on an additive Fourier transform throughout a shrinking principal-frequency neighborhood. FD-311 asks only for the **average square** of physical length-`N` Möbius sums across one dyadic start interval. The latter may exploit cancellation in `y` and does not need to control every frequency or every individual short interval.

Conversely, (7) must hold on the same source-selected window `[X,2X)` supplied by the Farey reduction. An averaged theorem over unrelated scales, or a statement that permits a sparse exceptional family carrying second-moment mass of order `XN^2`, does not suffice. The reduction has removed much freedom, but it has not removed the need for uniformity over the possible source-selected shell.

There is also an exact numerical echo of the Fejér reduction. At balanced depth, the forced RMS exponent in (14), `0.8725562489...`, equals

\[
\frac14+\frac{3c}{2},
\tag{26}
\]

which is the exponent appearing in the FD-307 frequency localization

\[
\|\alpha_*\|_{\mathbb T}
\le
N^{-1/4-(3c/2)+o(1)}.
\tag{27}
\]

This is not an independent coincidence: both come from the same inflated sliding moment. The physical-space and low-pass Fourier certificates are two projections of the same variance anomaly.

## 4. Adversarial checks and remaining frontier

The threshold (8) uses no RH. RH enters only in Section 2, where FD-304 converts the source-selected shell into the explicit aspect-ratio band (24). The conclusion must therefore not be stated as an RH proof of a variance estimate; it is an exact conditional reduction plus an RH localization of where such an estimate is needed.

The strict inequalities matter. At `eta=eta_var(lambda)` or `sigma=sigma_var(lambda)`, the `o(1)` losses on the two sides leave only tangency, not a contradiction. Likewise, a logarithmic saving such as `XN^2/log^A N` corresponds to `eta=0` at exponent level and does not close balanced depth.

The theorem template is also genuinely second-moment. An almost-all pointwise bound with an exceptional set can imply (7) only if the exceptional contribution, after the trivial `N^2` bound, is itself at most `XN^(2-eta+o(1))`. A log-power exceptional measure is therefore insufficient for any fixed positive `eta` without extra control on the exceptional amplitudes.

Finally, no lower bound stronger than FD-303 is claimed here, and no new Möbius cancellation theorem is asserted. The progress is the conversion of the vague request for “better short-interval cancellation” into a precise quantitative target. At balanced depth the target is only

\[
\boxed{
J_\mu(X,N)
\ll
X N^{1.7451124978-\varepsilon}
}
\tag{28}
\]

on source-selected windows with `N=X^(0.5...0.54643+o(1))`. Proving such a fixed-power mean-square saving, or showing that the Farey-selected windows possess additional structure that makes it accessible, is now a distinct alternative to improving the generic principal-frequency pointwise exponent of FD-310.

## Conclusion

The live balanced-depth obstruction can be attacked before the Fejér/Fourier stage. Near-capacity already forces the physical sliding Möbius RMS to reach `N^(0.872556...-o(1))`. Therefore any theorem that pushes the corresponding second moment below `XN^(1.745112...-epsilon)` on the source-selected dyadic windows rules out balanced near-capacity.

The relevant intervals have polynomial length `N=X^beta` with `1/2<=beta<=0.5464257...` under RH. Existing anchored short-interval theorems provide strong logarithmic or almost-all cancellation but do not give the fixed-power second-moment saving required here. The next useful target is consequently a source-window `L^2` estimate, not another generic major-arc decomposition.
