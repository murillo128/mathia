# WI-434 — Hardy transport regularizes crossed-zero edge poles

Status: `CLASSICAL-HARDY-IDENTITY + EXACT-DERIVED + STRUCTURAL-REDIRECTION + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`

Parents: `WI-426`, `WI-432`, `WI-433`

## Claim

`WI-433` leaves one precise live term after horizontal continuation of the localized positive Hardy component,

\[
-i\int_\sigma^{\sigma_0}e^{-(u-\sigma)\xi}K_u(\xi)\,du,
\qquad
K_u(\xi)=1_{\xi>0}\widehat{\chi'F(u+i\,\cdot)}(\xi),
\tag{1}
\]

where

\[
F(s)=\frac{\zeta'(s)}{\zeta(s)}+\frac1{s-1},
\qquad \frac12<\sigma<1<\sigma_0,
\tag{2}
\]

and `chi` is a real smooth compactly supported height window. A first concern is that the raw strip energy of `K_u` is singular whenever the transition region crosses an off-critical zero: `WI-426` already records the local planar `L^2` divergence of a logarithmic derivative through a pole.

For the actual transport in (1), that concern is too crude. The integrating semigroup in `WI-433` cancels the horizontal pole singularity exactly. More precisely, if

\[
\rho=\beta+i\gamma,
\qquad \sigma<\beta<1,
\qquad m=m_\rho,
\qquad \delta=\beta-\sigma,
\tag{3}
\]

is a right-half zero, then the principal part of `chi' F` at `rho` has coefficient

\[
c_\rho:=m_\rho\chi'(\gamma).
\tag{4}
\]

Under the Fourier convention of `WI-433`, its positive-frequency contribution is

\[
K^{\rm pp}_{\rho,u}(\xi)
=
-2\pi c_\rho e^{-(\beta-u)\xi}e^{-i\gamma\xi}
1_{\{u<\beta\}},
\qquad \xi>0.
\tag{5}
\]

Thus the raw line norm has the familiar pole blow-up. With the Plancherel-normalized positive-frequency norm

\[
\|G\|_{\mathcal H}^2
:=\frac1{2\pi}\int_0^\infty|G(\xi)|^2\,d\xi,
\tag{6}
\]

one has

\[
\|K^{\rm pp}_{\rho,u}\|_{\mathcal H}^2
=
\frac{\pi |c_\rho|^2}{\beta-u},
\qquad u<\beta,
\tag{7}
\]

so `int ||K_u||^2 du` diverges logarithmically at the crossing whenever `chi'(gamma) != 0`.

But the transported principal part is

\[
\boxed{
W^{\rm pp}_{\rho,u}(\xi)
:=e^{-(u-\sigma)\xi}K^{\rm pp}_{\rho,u}(\xi)
=
-2\pi c_\rho e^{-\delta\xi}e^{-i\gamma\xi}
1_{\{u<\beta\}}.
}
\tag{8}
\]

The singular factor has disappeared completely: before the crossing, the transported vector is independent of `u`; after the crossing it is zero. Consequently

\[
\boxed{
\int_\sigma^\beta
\|W^{\rm pp}_{\rho,u}\|_{\mathcal H}^2\,du
=
\pi |c_\rho|^2,
}
\tag{9}
\]

independent of the horizontal depth `delta`. The correct semigroup-weighted quadratic edge energy is therefore locally finite even though the unweighted strip `L^2` energy is infinite.

There is a stronger finite-height consequence. For an adiabatic family

\[
\chi_T(t)=\chi(t/T),
\tag{10}
\]

the **entire principal-pole part** of the transported edge forcing coming from crossed zeros whose ordinates lie in the transition region has quadratic energy

\[
\boxed{
\mathcal Q_T^{\rm pp}
\ll_\chi \frac{\log^2(2+T)}{T},
}
\tag{11}
\]

uniformly in every probe line `1/2 < sigma < 1` which is not itself a zero real part. Hence its contribution to the integrated edge term in (1) satisfies

\[
\boxed{
\left\|
-i\int_\sigma^{\sigma_0}
W_u^{\rm pp}\,du
\right\|_{\mathcal H}
\ll_{\chi,\sigma_0}
\frac{\log(2+T)}{\sqrt T}
=o(1).
}
\tag{12}
\]

This uses only the classical Riemann--von Mangoldt local zero count, with multiplicity. Thus the pole singularities of transition-zone zeros are **not** an asymptotic obstruction to a quadratic estimate of the actual `WI-433` transport. The remaining live object is the regular edge remainder after these principal parts are removed. No bound for that remainder is proved here.

## 1. Exact local normal form

For one zero `rho`, write locally

\[
F(s)=\frac{m}{s-\rho}+H(s),
\tag{13}
\]

with `H` holomorphic. Freeze the window derivative at the pole:

\[
\chi'(t)\frac{m}{u-\beta+i(t-\gamma)}
=
\frac{m\chi'(\gamma)}{u-\beta+i(t-\gamma)}
+
\frac{m(\chi'(t)-\chi'(\gamma))}
     {u-\beta+i(t-\gamma)}.
\tag{14}
\]

The second quotient is uniformly locally `L^2(dt)` as `u -> beta`, because its numerator vanishes linearly at `t=gamma`. Away from the pole it is ordinary smooth data. Since `chi'` has compact support, only finitely many poles occur in the relevant compact rectangle. Subtracting the frozen principal part (14) at each of them leaves a remainder whose `L^2(dt)` norm is locally bounded through every crossing. The full Cauchy tails introduced by the subtraction are also `L^2`.

For the first term in (14), the one-pole Fourier calculation already checked in `WI-433` gives, for `u<beta`,

\[
\widehat{\frac1{u-\beta+i(t-\gamma)}}(\xi)
=-2\pi e^{-(\beta-u)\xi}e^{-i\gamma\xi},
\qquad \xi>0,
\tag{15}
\]

while its positive-frequency transform is zero for `u>beta`. This proves (5). Equation (7) follows from

\[
\int_0^\infty e^{-2(\beta-u)\xi}\,d\xi
=\frac1{2(\beta-u)}.
\tag{16}
\]

Multiplying (5) by the exact integrating factor from `WI-433` gives

\[
e^{-(u-\sigma)\xi}e^{-(\beta-u)\xi}
=e^{-(\beta-\sigma)\xi},
\tag{17}
\]

which proves (8)--(9). The cancellation is not an estimate; it is the semigroup law.

In particular, for every fixed compactly supported window the quantity

\[
\int_\sigma^{\sigma_0}
\left\|
 e^{-(u-\sigma)\xi}K_u(\xi)
\right\|_{\mathcal H}^2du
\tag{18}
\]

is locally finite across the finitely many pole crossings after the harmless regular remainder from (14) is included. This is exactly the quadratic object for which horizontal Cauchy--Schwarz is legitimate. Applying Cauchy--Schwarz **before** the semigroup, to `int ||K_u||_H^2 du`, destroys the cancellation (17) and produces the false infinite barrier (7).

## 2. The crossed-zero principal parts form an exact positive Gram kernel

Let `Z` be the finite set of crossed zeros with `chi'(gamma_rho) != 0`, put

\[
\delta_\rho=\beta_\rho-\sigma,
\qquad
c_\rho=m_\rho\chi'(\gamma_\rho),
\tag{19}
\]

and sum (8):

\[
W_u^{\rm pp}(\xi)
=-2\pi
\sum_{\rho\in Z:\,u<\beta_\rho}
 c_\rho e^{-\delta_\rho\xi}e^{-i\gamma_\rho\xi}.
\tag{20}
\]

Expanding its norm and integrating first in `u` and then in `xi` gives the exact quadratic form

\[
\boxed{
\begin{aligned}
\mathcal Q^{\rm pp}
&:=
\int_\sigma^{\sigma_0}
\|W_u^{\rm pp}\|_{\mathcal H}^2\,du\\
&=
2\pi\sum_{\rho,\rho'\in Z}
 c_\rho c_{\rho'}
 \min(\delta_\rho,\delta_{\rho'})
 \frac{\delta_\rho+\delta_{\rho'}}
 {(\delta_\rho+\delta_{\rho'})^2
  +(\gamma_\rho-\gamma_{\rho'})^2}.
\end{aligned}
}
\tag{21}
\]

The kernel is positive semidefinite because (21) is literally a Gram norm. Equivalently it is the Schur product of the Brownian covariance kernel `min(delta_rho,delta_rho')` with the positive exponential/Cauchy Gram kernel from `WI-429`--`WI-430`.

For one zero, the diagonal entry of (21) is exactly

\[
\boxed{\pi m_\rho^2|\chi'(\gamma_\rho)|^2,}
\tag{22}
\]

with no factor `1/delta_rho`. This must not be misread as a lower bound for the multi-zero energy: the coefficients `chi'(gamma_rho)` have signs and cross terms can cancel. What is rigid is the disappearance of the reciprocal-depth singularity from the transported principal-part kernel.

The integrated principal edge atom itself is also explicit:

\[
\boxed{
-i\int_\sigma^{\sigma_0}
W^{\rm pp}_{\rho,u}(\xi)\,du
=
2\pi i\,m_\rho\chi'(\gamma_\rho)\delta_\rho
 e^{-\delta_\rho\xi}e^{-i\gamma_\rho\xi}.
}
\tag{23}
\]

The residue atom in `WI-433` for the same zero is

\[
-2\pi m_\rho\chi(\gamma_\rho)
 e^{-\delta_\rho\xi}e^{-i\gamma_\rho\xi}.
\tag{24}
\]

For a real window, the two scalar coefficients in (23)--(24) are in quadrature. Therefore the **local principal part of a zero cannot screen its own residue**:

\[
\boxed{
\left\|
(23)+(24)
\right\|_{\mathcal H}^2
=
\pi m_\rho^2
\left(
\frac{\chi(\gamma_\rho)^2}{\delta_\rho}
+
\delta_\rho\chi'(\gamma_\rho)^2
\right).
}
\tag{25}
\]

This statement is deliberately local to the frozen principal part. The regular remainder in (14), other zeros, and the holomorphic part of `F` can still interfere with the same frequency profile. Equation (25) says only that cancellation cannot come from the singular self-term that initially looked dangerous. For a plateau zero with `chi'(gamma_rho)=0`, that singular self-edge term vanishes identically.

## 3. Adiabatic windows make the principal crossed-zero edge energy vanish

Now set `chi_T(t)=chi(t/T)`. Then

\[
c_{\rho,T}
=
\frac{m_\rho}{T}\chi'(\gamma_\rho/T).
\tag{26}
\]

Only zeros with `gamma_rho/T` in the fixed compact support of `chi'` occur. For every nontrivial zero crossed from `sigma>1/2`,

\[
0<\delta_\rho<\frac12.
\tag{27}
\]

Hence the scalar kernel in (21) obeys the uniform elementary bound

\[
0\le
\min(\delta,\delta')
\frac{\delta+\delta'}
     {(\delta+\delta')^2+(\gamma-\gamma')^2}
\le
\frac1{1+(\gamma-\gamma')^2}.
\tag{28}
\]

Indeed, for `|gamma-gamma'| <= 1` the left side is at most `min(delta,delta')/(delta+delta') <= 1/2`, while for `|gamma-gamma'| >= 1` its numerator is less than `1/2` and the denominator is at least `(gamma-gamma')^2`.

Let `n_k` denote the number of nontrivial zeros, with multiplicity, whose ordinates lie in `[k,k+1]`. The classical Riemann--von Mangoldt formula gives

\[
n_k\ll \log(2+|k|).
\tag{29}
\]

If `supp chi'` is contained in `[-C,C]`, only `O(T)` unit intervals occur, each with `O(log(2+T))` zeros. Since

\[
\sum_{r\in\mathbb Z}\frac1{1+r^2}<\infty,
\tag{30}
\]

binning the double sum by unit ordinate intervals gives

\[
\sum_{|\gamma_\rho|,|\gamma_{\rho'}|\le CT}
\frac{m_\rho m_{\rho'}}
     {1+(\gamma_\rho-\gamma_{\rho'})^2}
\ll_\chi T\log^2(2+T).
\tag{31}
\]

Combining (21), (26), (28), and (31) proves (11):

\[
\mathcal Q_T^{\rm pp}
\ll_\chi
\frac1{T^2}
\,T\log^2(2+T)
=
O_\chi\!\left(\frac{\log^2(2+T)}T\right).
\tag{32}
\]

Finally, horizontal Cauchy--Schwarz is now applied to the **already transported** field:

\[
\left\|
\int_\sigma^{\sigma_0}W_u^{\rm pp}\,du
\right\|_{\mathcal H}^2
\le
(\sigma_0-\sigma)\mathcal Q_T^{\rm pp},
\tag{33}
\]

which proves (12). The estimate is uniform as the predetermined probe line approaches `1/2`; no lower bound on the crossed-zero depths is used.

## 4. What remains after the singular pole part is removed

For each fixed `T`, equations (14) and (20) give an exact decomposition

\[
K_u=K_u^{\rm pp}+K_u^{\rm reg},
\tag{34}
\]

where the second term is ordinary `L^2` through every pole crossing. The finding proves that the first term is both semigroup-regularized and asymptotically negligible in the adiabatic family. It does **not** prove that

\[
-i\int_\sigma^{\sigma_0}
 e^{-(u-\sigma)\xi}K_u^{\rm reg}(\xi)\,du
\tag{35}
\]

is small or prime-side controlled.

That distinction is the mathematical delta. A raw strip-area estimate such as

\[
\int_\sigma^{\sigma_0}\|K_u\|_{\mathcal H}^2du
\tag{36}
\]

is unusable because of (7), reproducing the pole singularity already seen in `WI-426`. But the actual transport never asks for (36). Its integrating factor yields the finite functional

\[
\boxed{
\int_\sigma^{\sigma_0}
\|e^{-(u-\sigma)D}K_u\|_{\mathcal H}^2du,
\qquad D:\ G(\xi)\mapsto \xi G(\xi),
}
\tag{37}
\]

and the only part of (37) forced by the pole principal parts is quantified by (21)--(32).

Thus the next circularity audit after `WI-433` should not ask whether a positive raw `L^2` strip norm crosses unknown zeros; `WI-426` already says that is singular. It should ask whether the **regular remainder** in (35)/(37) can be bounded from data fixed independently of the right-half zero divisor. If an order-one compensation survives for adiabatic windows, (12) says it cannot be blamed on the local pole singularities themselves.

## Prior art and novelty audit

No novelty or priority claim is made for any analytic ingredient.

- Matthias Kunik, *Logarithmic Fourier integrals for the Riemann Zeta Function*, arXiv:0804.4829, supplies the half-plane Poisson--Schwarz/Blaschke framework in which right-half zeta zeros appear as the inner-factor divisor. `WI-429`--`WI-433` already use that factorization as the zeta-specific background.
- The Fourier support of half-plane Cauchy kernels, the Paley--Wiener identification of one-sided Fourier support with Hardy space, and the exponential translation/Laplace semigroup are classical. Equation (17) is simply their semigroup law applied before taking a quadratic norm.
- The local `L^2(dA)` divergence of a logarithmic derivative through a zero is classical and was already made explicit for this research line in `WI-426`. The point here is not to rediscover that divergence but to show that it is absent from the semigroup-conjugated object which actually occurs in `WI-433`.
- The local count `N(t+1)-N(t)=O(log t)` used in (29)--(32) is the standard consequence of the Riemann--von Mangoldt formula.
- Neighboring Hardy/Blaschke derivative literature includes P. R. Ahern and D. N. Clark, *On inner functions with H^p derivative*, Michigan Math. J. 21 (1974), 115--127, and later work on Hardy/Bergman regularity of Blaschke derivatives. Those results concern function-space regularity rather than the zeta-specific horizontally transported edge functional above.

A targeted literature search around Kunik/Blaschke logarithmic derivatives, half-plane Hardy projections, Cauchy-kernel semigroups, and zeta logarithmic-derivative localization did not locate a source packaging the exact principal-pole Gram kernel (21) or its adiabatic consequence (11). Absence from that search is not evidence of priority. The durable repository delta is the exact correction to the live proof interface: **the pole singularity is an artefact of taking the quadratic norm before the `WI-433` semigroup transport, and its correctly transported principal part is quantitatively negligible for broad windows.**

## Stress tests, boundaries, and falsification

1. **The full edge term is not bounded.** `K_u^{reg}` in (34) contains the holomorphic/outer part of `F`, regularized pieces of the same zero divisor, and nonlocal contributions from zeros whose ordinates do not lie at the transition point. No uniform-in-`T` estimate for that term is asserted.

2. **No RH implication is claimed.** Equations (11)--(12) remove only the singular principal-pole contamination from the edge-forcing problem. An unconditional subquantum bound for the complete interior Hardy detector remains exactly the hard step identified in `WI-430`--`WI-433`.

3. **The diagonal tariff is not additive.** Although one pole pays the exact amount (22) in the transported strip energy, signed values of `chi'` allow cross-term cancellation in (21). The proof of (11) deliberately uses an upper bound, not a false diagonal lower bound.

4. **The quadrature statement is local.** Equation (25) excludes cancellation between one residue atom and the frozen singular edge principal part of the same zero. It does not exclude cancellation by the regular remainder, by other zeros, or by the safe-line/localization terms.

5. **The semigroup must be retained before squaring.** Removing `e^{-(u-sigma)xi}` recovers (7) and the logarithmic divergence. Any proposed quadratic estimate which first majorizes `K_u` in an unweighted strip norm throws away the exact cancellation (17).

6. **Endpoint lines are avoided.** As in `WI-433`, `sigma` is taken not to equal the real part of a zero. The formula extends distributionally across interior crossings; the value at the single horizontal parameter `u=beta` is irrelevant to the integrated norm.

The result would be falsified by a one-pole calculation in the conventions of `WI-433` for which the transported factor retained any dependence on `u` before the crossing, or by a counterexample to the positive Gram identity (21). Both reduce directly to the Cauchy transform (15), the semigroup identity (17), and elementary integration.

## Consequence for the research line

The live `WI-433` edge problem has a narrower and better-conditioned target. The obvious raw strip `L^2` norm is indeed singular, but that singularity does **not** survive the actual horizontal propagator. After the correct conjugation, every crossed-zero principal part becomes a bounded step in the horizontal variable, its individual quadratic tariff loses the reciprocal-depth blow-up, and the aggregate principal-pole forcing of an adiabatic window is `o(1)` by classical zero counting.

Therefore future work should estimate the semigroup-weighted **regular edge remainder** in (35)/(37), not `int ||K_u||^2 du`. A successful source-side estimate must explain that remainder from prime/boundary data or expose a new circularity obstruction there. The dangerous local pole singularity itself is no longer a viable explanation for failure of the `WI-433` transport route.