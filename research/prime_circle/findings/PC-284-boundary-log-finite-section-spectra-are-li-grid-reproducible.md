# PC-284 — boundary-log finite-section spectra are Li-grid reproducible

**Status:** `DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the source-placement branch left open by PC-283 in the classical PNT transport regime.

PC-283 completely identifies the selector-subtracted boundary logarithmic symbol on `Z/qZ`, but deliberately leaves open whether the source-dependent two-sided finite-section placement

\[
E_{pH_B}C_qE_{rH_B}^*
\]

can retain an order-one prime-specific singular-spectrum law. The obstacle to applying PC-281 directly is real: the exact boundary profile is logarithmically singular at the anchor and has no `q`-uniform Lipschitz realization.

That obstruction can nevertheless be removed without changing the exact operator except on a rare microscopic phase set. Let

\[
k_q(0):=-\log q,
\qquad
k_q(t):=\log\left(2\sin\frac{\pi |t|_q}{q}\right),\quad t\ne0,
\tag{1}
\]

where `|t|_q=min(t,q-t)`. This is exactly the PC-283 boundary-renormalized cyclic profile. For source points `x=p/q,y=r/q` and

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

define

\[
K_{q,B}(x,y)(h,k):=k_q(hp+kr\bmod q),
\qquad h,k\in H_B,
\tag{2}
\]

and let `Sigma_{q,B}(x,y)` be the ordered singular-value vector of `K_{q,B}(x,y)/N`.

Let `nu_q` be the normalized prime source of PC-277 and `\widetilde\lambda_q` its denominator-`q` Li-grid control. If `rho^{prime,log}_{q,B}` is the law of `Sigma_{q,B}` on distinct prime pairs and `rho^{Li,log}_{q,B}` is the corresponding product law under `\widetilde\lambda_q`, then there is an absolute `c>0` such that, for every `1/q<=epsilon<=1/4`,

\[
\boxed{
\begin{aligned}
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll{}&
\sqrt\varepsilon\,(\log q)^{3/2}\\
&+\frac{B\log q}{\varepsilon}
\left((\log q)e^{-c\sqrt{\log q}}+\frac{\log q}{q}\right)
+\frac{(\log q)^2}{q}.
\end{aligned}
}
\tag{3}
\]

Consequently, for every bandwidth sequence satisfying

\[
\boxed{\log B(q)=o(\sqrt{\log q}),}
\tag{4}
\]

one can choose `epsilon=exp(-c_0 sqrt(log q))` with a fixed sufficiently small `c_0>0` and obtain

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B(q)},
\rho^{Li,log}_{q,B(q)}
\right)\longrightarrow0.
}
\tag{5}
\]

Thus the exact selector-subtracted logarithmic boundary kernel does **not** rescue the PC-280 finite-section spectrum throughout the same sub-`exp(sqrt(log q))` source-transport regime. The singularity is too sparse to defeat a microscopic clipping argument, while the clipped operator is regular enough for the classical PC-277 prime-to-Li transport to control its entire normalized singular spectrum.

## 1. A Lipschitz surrogate that keeps the anchor value exact

Write `d(x)=||x||_{R/Z}`. For `1/q<=epsilon<=1/4`, define an even periodic profile `F_{q,epsilon}` by

\[
F_{q,\varepsilon}(x)=
\begin{cases}
-\log q+
\displaystyle\frac{d(x)}{\varepsilon}
\left[
\log(2\sin\pi\varepsilon)+\log q
\right],&0\le d(x)\le\varepsilon,\\[2ex]
\log(2\sin\pi d(x)),&\varepsilon\le d(x)\le1/2.
\end{cases}
\tag{6}
\]

This interpolation is chosen only to regularize the microscopic singular arc; importantly,

\[
F_{q,\varepsilon}(0)=-\log q=k_q(0).
\tag{7}
\]

Hence exact collisions are not replaced by an artificial finite value. Elementary differentiation gives

\[
\boxed{
\|F_{q,\varepsilon}\|_\infty\ll\log q,
\qquad
\operatorname{Lip}(F_{q,\varepsilon})\ll\frac{\log q}{\varepsilon}.
}
\tag{8}
\]

Indeed the inner slope is at most `O(log q/epsilon)`, while outside the clipped arc

\[
\left|\frac d{dx}\log(2\sin\pi d(x))\right|
=\pi|\cot(\pi d(x))|
\ll\varepsilon^{-1}.
\]

Let

\[
K^{(\varepsilon)}_{q,B}(x,y)(h,k)
:=F_{q,\varepsilon}(hx+ky).
\tag{9}
\]

The PC-281 perturbation argument applies verbatim to this `q`-dependent regular profile. Its normalized ordered singular spectrum `Sigma^{(epsilon)}_{q,B}` satisfies

\[
\boxed{
\|\Sigma^{(\varepsilon)}_{q,B}(x,y)
-\Sigma^{(\varepsilon)}_{q,B}(x',y')\|_\infty
\ll
\frac{B\log q}{\varepsilon}
\bigl(d(x,x')+d(y,y')\bigr).
}
\tag{10}
\]

No spectral asymptotic is used here: (10) follows directly from the entrywise Lipschitz bound, Frobenius domination of operator norm, and the coordinatewise singular-value perturbation inequality.

## 2. The clipping error is supported on a rare microscopic phase set

At denominator-`q` rational sources, equations (1) and (6) agree at residue `0` and at every residue whose circular distance is at least `epsilon q`. Therefore their difference can occur only for

\[
S_{q,\varepsilon}
:=\{t\in\mathbb Z/q\mathbb Z:
0<|t|_q<\varepsilon q\},
\qquad
|S_{q,\varepsilon}|\le2\varepsilon q.
\tag{11}
\]

On this set the crude but sufficient bound is

\[
|k_q(t)-F_{q,\varepsilon}(t/q)|\ll\log q.
\tag{12}
\]

Both source measures used here have maximal grid atom

\[
\boxed{
\max_a\nu_q(a/q)+
\max_a\widetilde\lambda_q(a/q)
\ll\frac{\log q}{q}.
}
\tag{13}
\]

For `nu_q` this is `1/|P_q|\asymp log q/q`; for the Li-grid control it follows directly from projecting the normalized logarithmic-integral density onto intervals of length `O(1/q)`, including the bounded number of endpoint cells.

Fix `(h,k)\ne(0,0)` in `H_B^2`. Since `N<=q`, at least one nonzero coefficient is invertible modulo the prime `q`. Conditioning on the other source variable and using (13),

\[
\boxed{
\Pr(hp+kr\bmod q\in S_{q,\varepsilon})
\ll\varepsilon\log q
}
\tag{14}
\]

under either independent source product law. The central coefficient pair `(h,k)=(0,0)` contributes no clipping error because of (7).

Let `Delta=K_{q,B}-K^{(epsilon)}_{q,B}`. From (11)--(14),

\[
\begin{aligned}
\mathbb E\left\|\frac{\Delta}{N}\right\|_F^2
&=\frac1{N^2}
\sum_{h,k\in H_B}
\mathbb E|\Delta(h,k)|^2\\
&\ll\varepsilon(\log q)^3.
\end{aligned}
\tag{15}
\]

Therefore Jensen, `||A||_op<=||A||_F`, and singular-value perturbation give

\[
\boxed{
\mathbb E
\|\Sigma_{q,B}-\Sigma^{(\varepsilon)}_{q,B}\|_\infty
\ll
\sqrt\varepsilon\,(\log q)^{3/2}
}
\tag{16}
\]

for both the prime product law and the Li-grid product law.

The important point is that no uniform Lipschitz constant for the exact logarithm is needed. Its bad derivative is confined to a set whose source probability is `O(epsilon log q)`, and the normalized matrix perturbation averages that microscopic defect before the singular-value comparison.

## 3. Transport the clipped whole spectrum and remove prime diagonals

PC-277 gives

\[
W_1(\nu_q,\widetilde\lambda_q)
\ll
(\log q)e^{-c\sqrt{\log q}}+
\frac{\log q}{q}.
\tag{17}
\]

Coupling two independent copies and applying (10) yields

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
(\Sigma^{(\varepsilon)}_{q,B})_*(\nu_q^{\otimes2}),
(\Sigma^{(\varepsilon)}_{q,B})_*(\widetilde\lambda_q^{\otimes2})
\right)
\ll
\frac{B\log q}{\varepsilon}
\left((\log q)e^{-c\sqrt{\log q}}+
\frac{\log q}{q}\right).
}
\tag{18}
\]

The exact and clipped matrices have entries of size `O(log q)`, hence every singular value after the `1/N` normalization is `O(log q)`. Passing from the prime product law to distinct prime pairs therefore costs at most

\[
O\!\left(
\frac{\log q}{q}\cdot\log q
\right)
=O\!\left(\frac{(\log q)^2}{q}\right),
\tag{19}
\]

because the diagonal source mass is `1/|P_q|=O(log q/q)`. Combining (16), (18), and (19) proves (3).

Now choose

\[
\varepsilon_q=e^{-c_0\sqrt{\log q}}
\tag{20}
\]

with any fixed `0<c_0<c`, after reducing `c_0` if necessary to absorb harmless constants in the PNT exponent. The first term of (3) is exponentially small up to powers of `log q`; the PNT term in the second is

\[
B(\log q)^2
\exp\!(-(c-c_0)\sqrt{\log q}),
\]

and the mesh term is even smaller. Condition (4) makes all terms tend to zero, proving (5).

## 4. What this closes relative to PC-281--PC-283

PC-281 proves whole-spectrum Li-grid reproducibility for regular profiles but explicitly excludes the unsmoothed logarithmic singularity. PC-282 shows that the unrenormalized boundary-first singularity is dominated by the exact modular collision selector. PC-283 subtracts that forced selector divergence and identifies the remaining full-domain symbol as the classical digamma/logarithmic Green kernel, while leaving its source-dependent finite-section placement open.

Equation (5) closes that placement escape throughout the classical source-transport regime (4). The boundary profile itself can be singular and its exact finite-section matrix can retain source dependence for each fixed source pair; nevertheless, **the law of its complete normalized singular spectrum on the prime source is reproduced asymptotically by the non-prime Li-weighted denominator-`q` control**.

This is stronger than replacing the logarithm by a fixed smoothing. The smoothing scale in (20) tends to zero, the exact anchor value `-log q` is retained, and the discrepancy between the smoothed and exact matrices is controlled in the spectral law rather than assumed negligible pointwise.

It also identifies why the singularity does not help here. The same denominator-`q` discreteness that creates the logarithmic spike makes the set of residues affected by a shrinking regularization explicitly countable. Against sources with `O(log q/q)` maximal atoms, that exceptional set is too sparse to overcome the classical prime-to-Li transport before the intermediate rational-microscopic regime.

## 5. Prior-art and novelty audit

Every analytic ingredient is classical or already isolated in the line. The logarithmic circle kernel and its finite Fourier/digamma symbol were classicalized in PC-283. Coordinatewise singular-value perturbation and finite-section spectra are standard matrix/operator theory and already audited in PC-280/281. The prime-to-Li-grid estimate (17) is exactly the classical quantitative-PNT transport input of PC-277.

A targeted literature search against logarithmic/singular Toeplitz and finite-section kernels, singular values of Toeplitz finite sections, partial Fourier concentration, and clipped logarithmic kernels found the expected surrounding operator theory. In particular, the finite-section/singular-value architecture belongs to classical Toeplitz and Fourier-section theory; singular symbols require care, but no independent mechanism was found that turns this Prime-Circle prime/Li source comparison into a new zeta criterion. No novelty is claimed for clipping a logarithmic singularity, matrix perturbation, or the PNT estimate.

The project-local delta is the quantitative synthesis (3): it removes the exact-log regularity gap left between PC-281 and PC-283 and proves that the **entire normalized singular-spectrum law** remains classically reproducible for `log B=o(sqrt(log q))`. Because all load-bearing external ingredients are already sourced by PC-277/280/281/283 and the new exceptional-set estimate is elementary, no new `SOURCES.md` dependency is required.

## 6. Surviving boundary and falsification tests

The result is deliberately not a global no-go for the finite-section program. It does not cover bandwidths in the intermediate rational-microscopic regime where `log B` is comparable to `sqrt(log q)` or larger, nor does it cover an additional magnification of the prime-minus-Li residual, cross-level/non-single-phase operators, or statistics that deliberately retain information beyond the ordered singular-value vector.

It also does not settle simultaneous `(q,B,rho)` scaling for the pre-boundary radial kernel when the PC-282 selector and its remainder remain comparable. Equation (5) concerns the canonical PC-283 boundary-renormalized profile itself.

The proof has direct finite falsification points. The interpolation (6) must satisfy (8); any denominator-`q` phase outside `S_{q,epsilon}` must agree exactly with (1); (14) can be checked by direct source counting; and the coordinatewise difference of exact and clipped normalized singular spectra must be bounded by `||Delta/N||_F`. A positive order-one lower bound in (5) along a sequence satisfying (4) would contradict at least one of these deterministic/counting estimates or the PC-277 source transport input.

The live finite-section frontier is therefore narrower than after PC-283: within sub-`exp(sqrt(log q))` windows, neither a regular profile nor the exact selector-subtracted boundary logarithm supplies a prime-specific positive spectral law beyond the Li-weighted rational control. The unresolved source-placement question begins only after this classical transport regime, or after enriching the observable so that it no longer factors through one two-sided finite section and its singular spectrum.
