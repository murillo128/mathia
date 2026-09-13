# NB-083 — boundary zeros force reciprocal-depth screening

**Status:** `EXACT-DERIVED + ANCHORED-POLYNOMIAL-PREDICTION + STATIONARY-BRANCH-CALIBRATION + SHARP-PREDICTION-RATE + HORIZON-DICHOTOMY + METHOD-BOUNDARY`.

`NB-082` identifies the normalized finite-prediction excess

\[
a_{\psi,L}
=
\frac{1}{|\psi(0)|^2}
\inf_{\substack{p\in\mathbb C[z]\\ \deg p\le L,\ p(0)=1}}
\|\psi p\|_{H^2}^2-1
\tag{1}
\]

as the exact scalar controlling the depth-`L` prediction-volume charge of every stationary branch filter `D_j^(psi)=psi(V_m)e_j`. It leaves the rate of `a_(psi,L)` as an abstract input. For outer **polynomial** filters this rate has a sharp geometric classification.

Let `psi` be a nonzero polynomial with `c_0:=psi(0) != 0` and no zero in the open unit disk, so `psi` is outer in `H^2`. Put

\[
f(z):=\frac{\psi(z)}{c_0},\qquad f(0)=1.
\tag{2}
\]

If `f` has boundary zeros `zeta_1,...,zeta_s in T` with multiplicities `k_1,...,k_s`, define

\[
\kappa(f):=\sum_{r=1}^s k_r^2.
\tag{3}
\]

Then, as `L->infinity`,

\[
\boxed{
a_{\psi,L}=\frac{\kappa(f)}{L}+o(L^{-1})
}
\qquad\text{whenever }\kappa(f)>0.
\tag{4}
\]

Zeros strictly outside the unit circle do not change the leading constant. By contrast, if `f` has no zero on the closed unit disk, then for every

\[
1<r<\min_{f(\lambda)=0}|\lambda|
\]

one has

\[
\boxed{
a_{\psi,L}=O_{f,r}(r^{-2L}).}
\tag{5}
\]

Combining (4)--(5) with the exact two-sided charge estimate of `NB-082` gives a genuine future-cost dichotomy. For

\[
N_{R,L}=m^L R-1,
\]

an outer polynomial with at least one boundary zero satisfies

\[
\boxed{
\mathfrak J_{R,N_{R,L}}
\asymp_{m,f}\frac{R}{L}
}
\tag{6}
\]

for `L->infinity`; hence bounded charge requires `L=Omega(R)` and vanishing charge requires `L/R->infinity`. In physical horizon size, bounded screening already costs

\[
N_{R,L}\ge R\,m^{cR}
\tag{7}
\]

for some positive `c`, while vanishing screening requires `log N/R -> infinity`.

If all zeros lie strictly outside the closed disk, logarithmic descendant depth is sufficient: choosing `L=C log R` with `C` large enough gives `mathfrak J -> 0`, and then

\[
N_{R,L}=R^{O(1)}.
\tag{8}
\]

Thus, inside the polynomial matched-control class, **polynomial-size future screening is separated from exponential-size screening exactly by contact of a zero with the unit circle**. Qualitative outerness does not see this distinction. The rate is controlled by the boundary singularity of the inverse, and finite boundary multiplicity changes only the leading constant, not the reciprocal-depth law.

This is a calibration theorem, not an arithmetic Nyman estimate. Its relevance is that an affordable source-facing theorem cannot be obtained by replacing the missing prediction-rate estimate with qualitative cyclicity or smoothness of the forward filter. Even an entire polynomial outer filter can require `L` of order `R` when its inverse is singular on the boundary. For the actual nonstationary Nyman innovations, one therefore needs either a quantitative inverse/prediction statement strong enough to beat this boundary mechanism, or a certificate that does not pay the finite-prediction layer.

## 1. The prediction excess is an anchored polynomial inverse problem

Normalize by (2). Since every admissible `p` satisfies `p(0)=1`, the polynomial

\[
e=fp-1
\tag{9}
\]

has zero constant term. Constants are orthogonal to `zH^2`, so

\[
\|fp\|_{H^2}^2=1+\|fp-1\|_{H^2}^2.
\tag{10}
\]

Therefore (1) is exactly

\[
\boxed{
a_{\psi,L}
=
\inf_{\substack{p\in\mathbb C[z]\\ \deg p\le L,\ p(0)=1}}
\|fp-1\|_{H^2}^2.
}
\tag{11}
\]

The anchor `p(0)=1` is essential. Equation (11) is closely related to the standard optimal-polynomial-approximant problem for `1/f`, but it is **not** the same minimization: an unconstrained OPA need not have constant coefficient one. The anchored form is the quantity selected by the branch-prediction normalization in `NB-082` and is treated directly below.

Let `d=deg f` and `M=L+d`. Writing

\[
e(z)=\sum_{n=1}^{M}u_nz^n
\tag{12}
\]

turns the problem into a finite minimum-norm Hermite interpolation problem. If `lambda` is a zero of `f` of multiplicity `k`, divisibility of `1+e` by `f` is equivalent to

\[
e(\lambda)=-1,
\qquad
e^{(q)}(\lambda)=0\quad(1\le q<k).
\tag{13}
\]

Conversely, imposing (13) at every zero makes `(1+e)/f` a polynomial of degree at most `L` with value one at zero. Hence

\[
\boxed{
a_{\psi,L}
=
\min\left\{
\sum_{n=1}^{M}|u_n|^2:
(12)\text{ satisfies all constraints }(13)
\right\}.
}
\tag{14}
\]

This exact interpolation representation, rather than unconstrained OPA normalization, is what drives the rate below.

## 2. Boundary Hermite constraints contribute `k^2/M`

First consider one boundary zero `zeta in T` of multiplicity `k`. The derivative row of order `q` in (13) is

\[
\bigl(n^{\underline q}\,\zeta^{\,n-q}\bigr)_{1\le n\le M},
\tag{15}
\]

where `n^(underline q)` is the falling factorial. After dividing row `q` by `M^(q+1/2)`, its Gram matrix converges, up to harmless unit-modulus phase conjugations, to the `k x k` Hilbert moment matrix

\[
H_k=\left(\frac1{q+r+1}\right)_{0\le q,r<k}.
\tag{16}
\]

Indeed,

\[
M^{-(q+r+1)}
\sum_{n=1}^{M}n^{\underline q}n^{\underline r}
\longrightarrow
\int_0^1x^{q+r}\,dx.
\tag{17}
\]

The scaled interpolation datum is `(-M^(-1/2),0,...,0)`. Since the classical inverse Hilbert matrix satisfies

\[
(H_k^{-1})_{00}=k^2,
\tag{18}
\]

the minimum squared coefficient norm forced by this one multiplicity-`k` boundary zero is

\[
\frac{k^2}{M}+o(M^{-1}).
\tag{19}
\]

For distinct boundary points, mixed Gram entries are oscillatory sums

\[
\sum_{n\le M}n^{q+r}(\zeta_i\overline{\zeta_j})^n,
\qquad i\ne j,
\tag{20}
\]

which are one power of `M` smaller than the corresponding diagonal sums. After the scaling used in (17), the different boundary blocks therefore decouple. Their energies add, giving

\[
\frac{1}{M}\sum_{r=1}^s k_r^2+o(M^{-1})
\tag{21}
\]

before the constraints from exterior zeros are imposed.

Exterior zeros do not alter this leading term. Their evaluation/derivative Gram blocks grow geometrically in `M`; boundary--exterior cross blocks carry the same geometric endpoint factor but one fewer power of `M` than the boundary diagonal after the exterior block is eliminated. The fixed-dimensional Schur complement therefore perturbs each scaled boundary block by `O(M^{-1})`. Thus the leading matrix in (16) and the energy in (21) are unchanged. Since `M=L+d`, this proves (4).

The asymptotic passes two sharp calibrations already present in the line. For `f=1-z`, `kappa=1` and `NB-082` gives the exact value `a_(psi,L)=1/(L+1)`. For `f=(1-z)^k`, the same confluent-Hilbert calculation gives

\[
L\,a_{\psi,L}\longrightarrow k^2,
\tag{22}
\]

so higher boundary multiplicity changes the constant quadratically but does not improve the exponent.

## 3. Strictly exterior zeros give geometric prediction

Suppose now that every zero of `f` has modulus greater than one. Then `1/f` is analytic in a disk of radius `rho>1`, where `rho` may be taken below the modulus of the closest zero. Let

\[
\frac1{f(z)}=\sum_{n\ge0}b_nz^n,
\qquad b_0=1.
\tag{23}
\]

For every fixed `1<r<rho`, Cauchy's estimate gives `|b_n|=O_(f,r)(r^(-n))`. Take the Taylor truncation

\[
p_L(z)=\sum_{n=0}^{L}b_nz^n.
\tag{24}
\]

It is admissible in (11), and multiplication by the fixed polynomial `f` preserves the geometric tail rate. Hence

\[
\|fp_L-1\|_{H^2}^2
=O_{f,r}(r^{-2L}),
\tag{25}
\]

which proves (5). No lower geometric rate is needed for the horizon classification.

This regime contains the `NB-081/082` filter `psi(z)=1-rho_0 z` with `0<rho_0<1`: its unique zero `1/rho_0` is strictly exterior and the exact error is geometric. The endpoint `rho_0=1` moves that zero onto the boundary and immediately changes the screening law to `1/L`.

## 4. Branching converts the scalar singularity into a sharp horizon barrier

`NB-082` proves, for `L->infinity`,

\[
K_{m,R,L}\log(1+a_{\psi,L})
\le
\mathfrak J_{R,m^LR-1}
\le
(R-1)\log(1+a_{\psi,L}),
\tag{26}
\]

with `K_(m,R,L)/R -> 1-1/m` uniformly in `L`. If a boundary zero is present, (4) and `log(1+x)~x` give (6). Therefore

\[
\mathfrak J=O(1)
\iff
\frac RL=O(1),
\qquad
\mathfrak J\to0
\iff
\frac RL\to0.
\tag{27}
\]

Because the physical future size is `m^L R`, those two conditions are exactly the exponential and super-fixed-exponential costs stated in (7).

If the inverse is analytic through the unit circle, (5) allows `L=C log R`. Taking `C` so that `R r^(-2L)->0` forces `mathfrak J->0`, while `m^L R` remains polynomial in `R`. Thus the branch geometry amplifies a scalar analytic distinction into a qualitative distinction in the amount of future required by the certificate.

## 5. Prior-art boundary, falsification tests, and consequence

The unconstrained neighboring approximation problem is classical optimal-polynomial-approximant theory. Bénéteau, Manolaki and Seco, *Boundary Behavior of Optimal Polynomial Approximants*, Constructive Approximation 54 (2021), 157--183, DOI `10.1007/s00365-020-09508-z`, gives finite zero-Gram formulas for polynomial `f`, the Hardy `1/L` boundary-zero rate in the ordinary OPA setting, and a confluent/Hilbert-matrix analysis for a higher-multiplicity boundary zero. No novelty is claimed for those OPA mechanisms or for the general phenomenon that boundary zeros slow cyclic approximation.

The exact scalar in `NB-082` carries the additional anchor `p(0)=1`, so the literature result is a prior-art boundary rather than a substituted theorem. Equations (9)--(21) derive the anchored rate directly. The line-local consequence is then the insertion of that rate into the branch-screening theorem, which identifies a complete polynomial calibration of future cost: zero-free continuation across the circle admits polynomial-size horizons, while any finite-order boundary zero forces exponential-size horizons despite outerness and despite the filter being a polynomial.

The falsification checks agree. The flat filter has `a=0`; `1-rho z`, `rho<1`, has geometric decay; `1-z` has exactly reciprocal decay; repeated boundary zeros retain reciprocal decay with the predicted multiplicity-squared constant. Interior zeros are deliberately excluded: they create a nonconstant inner factor, so `NB-082` already gives a positive limiting excess and a linear-in-`R` charge at every depth.

No specialized external estimate is load-bearing in the derivation above, and the OPA paper is used only to delimit prior art, so `SOURCES.md` is unchanged.

The research consequence is negative but concrete. The actual Nyman innovations are nonstationary, so (4) cannot simply be transferred to them. But any attempt to obtain the required `1/R` finite-prediction accuracy from outerness or forward regularity alone is calibrated against an analytic polynomial control where those qualitative properties coexist with the `1/L` boundary law. An affordable arithmetic horizon must exploit stronger source information: quantitative inverse stability away from a boundary singularity, genuinely nonstationary arithmetic cancellation, or a stable-mode certificate that avoids finite prediction altogether.
