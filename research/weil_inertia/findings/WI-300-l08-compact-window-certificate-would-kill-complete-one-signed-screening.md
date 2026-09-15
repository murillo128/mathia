# WI-300 — independently replayed L=0.8 compact-window positivity kills complete one-signed first-crossing screening

**Status:** `PRIOR-ART-REDIRECT + RECENT-PREPRINT + COMPUTATIONAL-INTERVAL + INDEPENDENT-REPLAY + EXACT-DERIVED`.

The verification gate recorded in the original version of this finding is now discharged. Xuefeng Zhu's pinned v2 preprint, *Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law*, arXiv:2608.24827v2 (revised 2 September 2026), states the unconditional compact-window bound

\[
\boxed{
Q_W(f)\ge 8.9\times10^{-18}\,\|f\|_2^2
\qquad
\text{for every complex }f\text{ supported in }[-0.8,0.8].
}
\tag{1}
\]

Mathia issue [#152](https://github.com/murillo128/mathia/issues/152) independently reconstructed and interval-certified the v2 lower-bound pipeline from the geometric side, without using zeta zeros, RH, or an author-supplied matrix. The replay therefore upgrades (1) from fresh author-certified prior art to independently checked computer-assisted evidence at the level used by this line.

Through the normalization dictionary already audited against Suzuki's localized Weil form, (1) gives

\[
\boxed{
\lambda_{0.8}\ge 8.9\times10^{-18}>0.
}
\tag{2}
\]

WI-238 makes the localized ground-state profile nonincreasing in the aperture and, under RH failure, defines the first crossing

\[
a_*:=\inf\{a>0:\lambda_a\le0\}.
\]

Hence (2) forces

\[
\boxed{a_*>0.8.}
\tag{3}
\]

WI-298 independently proves that a hypothetical first-crossing null mode which is both one-signed and completely prime-power screened would instead force

\[
\boxed{
a_*\le r_2:=\frac{\log2}{2}=0.346573590\ldots .
}
\tag{4}
\]

Since `r_2<0.8`, the two inequalities are incompatible. Thus the **one-signed completely screened first-crossing branch is unconditionally excluded**, subject only to the ordinary computer-assisted-evidence boundary of the replayed finite certificate. WI-301 strengthens this conclusion further: the first-crossing and null-mode hypotheses can be removed entirely for the completely screened one-signed class.

## 1. What was independently replayed

The replay was pinned to the exact v2 source archive rather than to mutable unversioned metadata. Its source and matrix provenance, software versions, analytic error bounds, complete reconstruction code, and independent checker are preserved in the [issue evidence comment](https://github.com/murillo128/mathia/issues/152#issuecomment-5678076696).

For `L=0.8`, the prime comb has only `n=2,3,4` active. The replay independently checked

\[
A_L
=\sqrt2\log2+\frac{2}{\sqrt3}\log3+\log2
=2.9419735252236204555\ldots
\]

and the pointwise Binet tail floors

\[
\beta_{200}=0.5134667749150707383\ldots,
\qquad
\beta_{150}=0.2241180357966231442\ldots .
\]

The even sector used `N=200` normalized Legendre modes, cutoff `T=200`, and outward Arb arithmetic at 100 decimal digits. The odd sector used `N=200`, `T=150`, and 140 digits. Head entries were enclosed with Gauss--Legendre quadrature plus a rigorous Bernstein-ellipse remainder; the discarded diagonal and head--tail coupling were bounded analytically. A separate 150-digit checker converted the matrix intervals to exact dyadic endpoint bounds, formed an exact-dyadic Gram factor from the midpoint Cholesky data, and enclosed the residual independently rather than reusing the primary recurrence or factorization logic.

At shifts `9e-18` and `8.3e-15`, the residual operator bounds were below `7.367e-32` and `1.328e-88`, respectively. After the explicit quadrature and tail deductions, the certified sector floors are

\[
\lambda_{\rm even}\ge8.9\times10^{-18},
\qquad
\lambda_{\rm odd}\ge8.2065\times10^{-15}.
\]

Parity and real/imaginary decomposition therefore yield (1) for the full complex window. This is a computer-assisted interval certificate, not a Lean theorem.

## 2. Dictionary to Suzuki's localized form

Suzuki's localized operator uses the same Bombieri/Weil quadratic functional, closed on functions supported in `(-a,a)`. In the Fourier normalization of WI-238 its diagonal zeros-side form is

\[
Q_W(v,v)
=\sum_\gamma m_\gamma
\widehat v(\gamma)
\overline{\widehat v(\bar\gamma)},
\]

while Zhu's geometric-side form is the corresponding explicit-formula representation of the same autocorrelation functional. Issue #152 rechecked the apparent archimedean normalization mismatch directly: the conversion factor is exactly one, because the residual constant is canceled by the elementary integral equal to `log 2`. Thus no scalar or parity loss occurs between the certified `L=0.8` theorem and Suzuki's `lambda_0.8`.

Primary sources:

- Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096 (2026): https://arxiv.org/abs/2606.09096.
- Xuefeng Zhu, **Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau--Widom decay law**, pinned arXiv:2608.24827v2, revised 2 September 2026: https://arxiv.org/abs/2608.24827v2.
- Mathia issue **#152**, independent certified replay: https://github.com/murillo128/mathia/issues/152.

## 3. Exact branch consequence

The logical use of the certificate is much weaker than any attempt to extend compact-window positivity toward arbitrary aperture. Positivity at the single scale `0.8` already implies, by monotonicity,

\[
a_*>0.8.
\]

The exact support-packing and rearrangement theorem WI-298 says complete one-signed prime-power screening at a first crossing would compress the mode to a nonpositive test at the first-prime aperture `r_2=(log2)/2`, hence `a_*<=r_2`. The contradiction is therefore finite and has no asymptotic step.

This closes the verification target that originally motivated WI-300 and supersedes the narrower `lambda_{r_2}>0` certificate as the shortest route for this branch. It does not invalidate the endpoint analysis of WI-299; that work remains an independent description of the first-prime transition.

## 4. Prior-art and evidence boundary

The compact-window reduction, the `8.9e-18` constant, the parity extension, and the pointwise-envelope barrier are Zhu's v2 claims. Mathia's contribution in WI-300 is the source dictionary, independent replay, and the exact integration with the branch structure already proved in WI-238 and WI-298. No priority claim is made.

A targeted prior-art check found the fixed-window theorem in Zhu and the localized form in Suzuki, but no source turning this particular verified window into the line-local screened first-crossing contradiction. The stronger arbitrary-support screened-class consequence is recorded separately in WI-301 so that its different mathematical claim identity is explicit.

The result does **not** establish unrestricted Weil positivity beyond `L=0.8`, does not control sign-changing screened functions, and does not prove RH. Zhu's own pointwise-envelope architecture has a doubly exponential large-window cost: its threshold is `T_1(L)=2\pi e^{A_L}`, with `A_L=(4+o(1))e^L`. The present branch closure avoids that barrier because it needs only one verified finite window above `(log2)/2`.