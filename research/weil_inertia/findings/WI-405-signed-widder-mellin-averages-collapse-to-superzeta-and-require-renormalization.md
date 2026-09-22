# WI-405 — signed Widder Mellin averages collapse to superzeta and require renormalization

**Status:** `CLASSICAL-IDENTITY + LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT + BOOTSTRAP-INTERFACE`.

**Parent findings:** [WI-399](./WI-399-widder-root-growth-gives-effective-shift-bootstrap.md), [WI-403](./WI-403-scalar-widder-envelope-feedback-is-a-closure-operator.md), [WI-404](./WI-404-finite-p-scalar-widder-averages-have-a-critical-height-weight.md).

## Claim

WI-404 leaves signed/phase-sensitive cross-height observables open after showing that finite-`p` nonnegative scalar Widder averages lose a fixed off-critical defect unless their height weight grows at the corresponding critical rate. For the simplest signed pure-power Mellin family there is now an exact answer.

For a zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad
w_\rho=(\gamma-i\delta)^2,
\]

use the **complex signed** one-zero Widder mode

\[
z_w(T):=\frac{4T^2w}{(T^2+w)^2}.
\tag{1}
\]

This is not the modulus/excess response of WI-404. For every integer `m>=1` and real `a` with

\[
-2m-1<a<2m-1,
\tag{2}
\]

one has the exact one-zero Mellin identity

\[
\boxed{
\int_0^\infty T^a z_w(T)^m\,dT
=
2^{2m-1}
B\!\left(m+\frac{a+1}{2},m-\frac{a+1}{2}\right)
 w^{(a+1)/2}.
}
\tag{3}
\]

Writing

\[
\sigma:=-\frac{a+1}{2},
\tag{4}
\]

the full zero sum is absolutely interchangeable with the height integral in the natural range

\[
\boxed{\frac12<\sigma<m.}
\tag{5}
\]

There the signed cross-height average is exactly

\[
\boxed{
\int_0^\infty T^{-2\sigma-1}
\sum_{\rho\in\mathcal Z_+}z_{w_\rho}(T)^m\,dT
=
2^{2m-1}B(m-\sigma,m+\sigma)\,\mathcal Z(\sigma,0),
}
\tag{6}
\]

where

\[
\mathcal Z(\sigma,0)=\sum_{\rho\in\mathcal Z_+}w_\rho^{-\sigma}
\tag{7}
\]

is precisely the `v=0` second-kind superzeta studied classically by Voros. Thus the absolutely convergent pure-power signed Mellin average does **not** produce a new scalar invariant: it is a beta multiple of a classical superzeta.

Moreover, that absolutely convergent regime still loses high fixed-depth horizontal defects. For the functional-equation pair

\[
w_\pm=(\gamma\mp id)^2,
\qquad d>0,
\]

one has, for fixed `sigma`,

\[
\boxed{
w_+^{-\sigma}+w_-^{-\sigma}-2\gamma^{-2\sigma}
=
-2\sigma(2\sigma+1)d^2\gamma^{-2\sigma-2}
+O_{\sigma,d}(\gamma^{-2\sigma-4}).}
\tag{8}
\]

Since absolute zero-set convergence requires `sigma>1/2`, this defect signal decays strictly faster than `gamma^-3`. Therefore the raw absolutely convergent signed Mellin family cannot by itself supply a height-uniform additive charge for a fixed off-critical defect.

There is nevertheless an exact critical signed observable. For every integer `m>=2`, the weight `a=1` gives

\[
\boxed{
\int_0^\infty T\,z_w(T)^m\,dT=C_m w,
\qquad
C_m:=2^{2m-1}B(m+1,m-1).
}
\tag{9}
\]

Hence an off-line functional-equation pair pays the **exact height-independent horizontal charge**

\[
\boxed{
\int_0^\infty T
\left[
2z_{\gamma^2}(T)^m-z_{w_+}(T)^m-z_{w_-}(T)^m
\right]dT
=2C_m d^2.
}
\tag{10}
\]

But `a=1` corresponds to `sigma=-1`, far outside the domain of absolute zero-sum convergence. The raw sums of `w_rho` and of the critical baseline `gamma_rho^2` diverge. Voros's meromorphic continuation does not by itself turn (10) into a nonnegative additive global defect budget. A valid global use of (10) therefore requires a **new truncation, cancellation, or renormalized prime-side identity** that cancels the divergent same-ordinate baseline while preserving the finite-pair `d^2` charge.

This closes the naive signed-Mellin escape from WI-404 but identifies a sharper bootstrap interface: the obstruction is no longer lack of one-zero sensitivity, but the three powers of height separating absolute zero-set convergence (`a<-2`) from the height-uniform signed defect tariff (`a=1`). No improved simple-critical-zero proportion, no global `sum d^2` bound, and no proof of RH is claimed.

## 1. Exact one-zero Mellin transform

From (1),

\[
T^a z_w(T)^m
=
4^m w^m\frac{T^{a+2m}}{(T^2+w)^{2m}}.
\]

Put `x=T^2`. Then

\[
\int_0^\infty T^a z_w(T)^m\,dT
=
2^{2m-1}w^m
\int_0^\infty
\frac{x^{m+(a+1)/2-1}}{(x+w)^{2m}}\,dx.
\tag{11}
\]

The ordinary beta integral gives

\[
\int_0^\infty\frac{x^{u-1}}{(x+w)^{2m}}\,dx
=w^{u-2m}B(u,2m-u),
\tag{12}
\]

for `0<u<2m`, initially for positive `w` and then throughout the right half-plane by holomorphy with the principal branch. Here

\[
u=m+\frac{a+1}{2},
\]

so `0<u<2m` is exactly (2), and (11)--(12) prove (3).

For nontrivial zeta zeros in the upper half-plane, `|delta|<1/2` while `gamma` is bounded away from zero, hence

\[
\Re w_\rho=\gamma^2-\delta^2>0.
\]

Thus no branch crossing is involved in the application to the zeta zero set.

At `a=1`, condition (2) requires `m>=2`; `m=1` is the logarithmically divergent endpoint. Substituting `a=1` into (3) gives (9) exactly.

## 2. Absolute zero-sum regime and the Voros identification

Set `a=-2sigma-1`. Then (3) becomes

\[
\int_0^\infty T^{-2\sigma-1}z_w(T)^m\,dT
=
2^{2m-1}B(m-\sigma,m+\sigma)w^{-\sigma}.
\tag{13}
\]

The zeta parameters `w_rho` lie in a fixed sector strictly inside the right half-plane. Scaling `T=|w|^{1/2}u` therefore bounds the absolute one-zero integral by

\[
\int_0^\infty
T^{-2\sigma-1}|z_w(T)|^m\,dT
\ll_{m,\sigma}|w|^{-\sigma}
\tag{14}
\]

whenever `-m<sigma<m`. The Riemann--von Mangoldt estimate `N(U)=O(U log U)` and `|w_rho| asymp gamma_rho^2` give

\[
\sum_{\rho\in\mathcal Z_+}|w_\rho|^{-\sigma}<\infty
\qquad(\sigma>1/2).
\tag{15}
\]

Hence Tonelli/Fubini is valid for `1/2<sigma<m`, and summing (13) proves (6).

The right side is classical prior art. André Voros defines a second-kind superzeta over the Riemann zeros of the form

\[
\mathcal Z(\sigma,v)=\sum_k(\tau_k^2+v)^{-\sigma},
\tag{16}
\]

where a zero is parametrized as `rho_k=1/2+i tau_k`. In the present notation `tau_k=gamma-i delta`, so `tau_k^2=w_rho`; therefore `v=0` is exactly (7). Voros also develops the meromorphic continuation of this family beyond its defining half-plane. That continuation is relevant to regularization, but it is not an absolutely convergent zero sum there.

## 3. Absolute convergence still loses horizontal defect

Let

\[
\nu:=\frac{a+1}{2}=-\sigma.
\]

For a symmetric off-line pair, write

\[
w_\pm
=
\gamma^2-d^2\mp2i\gamma d
=
\gamma^2
\left(1-\frac{d^2}{\gamma^2}\mp2i\frac d\gamma\right).
\]

Taylor expansion at fixed `d` and `gamma -> infinity` gives

\[
\boxed{
w_+^\nu+w_-^\nu-2\gamma^{2\nu}
=
2\nu(1-2\nu)d^2\gamma^{2\nu-2}
+O_{\nu,d}(\gamma^{2\nu-4}).}
\tag{17}
\]

Substituting `nu=-sigma` yields (8). In the only range where the raw zero sum and height integral can be interchanged absolutely, `sigma>1/2`, the pairwise horizontal signal is therefore `o(gamma^-3)`.

This is a genuine barrier for this particular scalar family. It does **not** say that signed information is useless. It says that demanding absolute summability of the raw pure-power Mellin transform forces the weight so far toward small heights that the desired fixed-depth defect charge disappears at high ordinate.

## 4. The critical signed weight has an exact pairwise `d^2` charge

For `a=1` and `m>=2`, (9) is linear in `w`. The two upper-half-plane members of a functional-equation pair satisfy

\[
w_++w_-=2(\gamma^2-d^2).
\tag{18}
\]

The corresponding pair projected onto the critical line at the same ordinate has total parameter `2gamma^2`. Therefore

\[
\begin{aligned}
&\int_0^\infty T
\left[
2z_{\gamma^2}(T)^m-z_{w_+}(T)^m-z_{w_-}(T)^m
\right]dT\\
&\qquad=C_m\left(2\gamma^2-w_+-w_-\right)
=2C_m d^2,
\end{aligned}
\]

which is (10). This identity is exact for each finite pair and has no residual dependence on `gamma`.

The important restriction is global. At `a=1`, `sigma=-1`; the formal right side of (6) would involve

\[
\sum_\rho w_\rho,
\]

which diverges, as does the comparison baseline `sum gamma_rho^2`. Consequently one may **not** sum (10) over all off-critical pairs by Fubini, nor subtract the two divergent baselines termwise without a separately justified truncation/cancellation theorem.

The meromorphically continued value `mathcal Z(-1,0)` is a regularized spectral quantity. Nothing in the classical continuation identifies it with a positive sum of the pairwise quantities `d^2`, and no such identification is used here. In particular, analytic continuation alone cannot promote (10) to a global defect-to-zero theorem.

## 5. Prior-art audit and novelty boundary

The Widder mode and fixed-height framework come from Zeraoulia Rafik, *Uniform Beta Smoothing of Widder Sums for the Riemann xi-Function and a Schur--Triple Application to Simple Critical Zeros*, Preprints.org manuscript `202609.1018`, version 2, posted 17 September 2026:

<https://www.preprints.org/manuscript/202609.1018>

The manuscript is explicitly non-peer-reviewed. WI-399 independently reconstructed the load-bearing zero-side Widder normalization and prime/zero root-rate interface used here.

The direct classical prior art for (7) is:

- André Voros, *Zeta functions for the Riemann zeros*, Annales de l'Institut Fourier **53** (2003), 665--699, DOI `10.5802/aif.1955`: <https://www.numdam.org/articles/10.5802/aif.1955/>.
- André Voros, *Erratum - Zeta functions for the Riemann zeros*, Annales de l'Institut Fourier **54** (2004), 1139, DOI `10.5802/aif.2046`: <https://www.numdam.org/articles/10.5802/aif.2046/>.

Voros's paper explicitly studies Dirichlet-series zeta functions built from the nontrivial Riemann zeros and their meromorphic continuation. Equation (6) should therefore be viewed as an exact bridge from the signed Widder Mellin observable to an existing classical object, not as a new zeta function.

A targeted audit around the Rafik preprint, Voros superzetas, Mellin transforms over Riemann zeros, and Widder/secondary-zeta constructions did not locate this exact signed cross-height bridge or the finite-pair identity (10). That negative search is **not** used as a priority claim. The durable mathematical contribution of this finding is the exact reduction/barrier and the resulting specification of what additional theorem would actually be needed.

## 6. Consequence and next falsifiable target

The simplest signed cross-height proposal now splits sharply into two regimes:

1. In the absolutely convergent regime `a<-2`, equivalently `sigma>1/2`, the observable collapses to the classical Voros superzeta and its fixed-depth horizontal defect signal vanishes rapidly with height.
2. At the height-uniform defect weight `a=1`, each finite off-line pair carries the exact charge `2 C_m d^2`, but the raw global zero sum is divergent.

Thus the next useful target is **not** another absolutely convergent pure-power Mellin weight. It is a zeta-specific identity that legitimizes the critical signed weight by cancellation before summation. Concretely, one would need a truncation or renormalization theorem in which the critical projection/same-ordinate baseline is cancelled on the zero side and the corresponding prime/gamma terms are controlled, while the residual off-line contribution retains a one-sided lower bound comparable to

\[
\sum_{\rho\in\mathcal Z_+(H)} d_\rho^2
\]

on finite truncations. If such a theorem survived the limit with a finite prime-side budget, (10) would supply the missing height-uniform defect tariff directly. If every admissible regularization necessarily introduces an uncontrolled signed counterterm of the same size, this route closes.

The gap in polynomial height weight is exact:

\[
\boxed{
\text{absolute zero-set convergence: }a<-2
\qquad\text{versus}\qquad
\text{height-uniform pair defect: }a=1.
}
\tag{19}
\]

This is a three-power mismatch. It is the current barrier and the current bootstrap interface for the raw signed Widder--Mellin route.

## Evidence classification and limitations

- `CLASSICAL-IDENTITY`: the beta/Mellin transform and Voros second-kind superzeta are classical objects.
- `LITERATURE+DERIVED`: the Widder mode is inherited from the recent Rafik framework; the superzeta identification is anchored to Voros.
- `EXACT-DERIVED`: equations (3), (6), (9), and (10) follow by exact beta integration and functional-equation pairing.
- `DECISIVE-NEGATIVE`: absolutely convergent pure-power signed Mellin averages cannot yield a height-uniform fixed-depth defect tariff.
- `PRIOR-ART-REDIRECT`: the convergent signed family is already a classical superzeta rather than a new independent invariant.
- `BOOTSTRAP-INTERFACE`: the critical `a=1` finite-pair identity isolates the missing theorem as a cancellation/renormalization problem.

No assertion is made that meromorphic continuation preserves positivity, that `mathcal Z(-1,0)` equals a sum of horizontal defects, that the pairwise identity may be summed over all zeros without further work, or that this finding improves the established proportion of simple critical zeros.