---
id: WP-321
title: Atomwise smoothing matches every Mangoldt gap law and the full bounded-gap Julia family
branch: weil_positivity
status: supported
kind: nonsparse-all-gap-atomless-matched-control-obstruction
claim_strength: exact matched-control construction for the reflected Mangoldt Herglotz source; one positive non-atomic locally absolutely continuous measure, obtained by sufficiently small atomwise smoothing, preserves every prime-power gap midpoint as a regular node and asymptotically matches the derivative normalization and derivative-biased law at every consecutive support gap in bounded-Lipschitz distance; consequently, on the entire unthinned fixed-additive-gap family of WP-319, where those laws are uniformly tight, the normalized scalar Julia profiles also converge locally uniformly, so nonsparse same-source scalar coherence in the natural weak/Julia topology is still not arithmetic-selective
created: 2026-09-15
related: [WP-304, WP-315, WP-318, WP-319, WP-320]
prior_art:
  - Jim Agler and N. J. Young, Boundary Nevanlinna-Pick interpolation via reduction and augmentation, Mathematische Zeitschrift 268 (2011), 791-817, DOI 10.1007/s00209-010-0696-3, arXiv:0905.4759, for the classical Julia-Nevanlinna reduction underlying WP-318
  - Roland Speicher and Reza Woroudi, Boolean convolution, Fields Institute Communications 12 (1997), 267-279, DOI 10.1090/fic/012/13, for the Boolean self-energy transform used in WP-318
  - Toby O'Neil, A measure with a large set of tangent measures, Proceedings of the American Mathematical Society 123 (1995), no. 7, 2217-2220, DOI 10.2307/2160960, as prior-art warning that one measure can support highly flexible tangent behavior
  - Tuomas Sahlsten, Tangent measures of typical measures, Real Analysis Exchange 40 (2015), no. 1, 53-80, DOI 10.14321/realanalexch.40.1.0053, for a stronger generic tangent-flexibility comparison already audited in WP-320
---

# WP-321 — Atomwise smoothing matches every Mangoldt gap law and the full bounded-gap Julia family

## Claim

`WP-320` left a deliberately sharp loophole. Its one-source matched control required aggressive thinning so that independently engineered blocks could be placed at physically separated gap nodes. The remaining scalar hope was therefore that a **non-sparse or all-gap family** might force cross-gap coherence that one non-arithmetic positive Herglotz source cannot reproduce.

For every scalar criterion that sees the source only through the derivative-biased gap laws in the bounded-Lipschitz topology, that loophole also closes.

Enumerate the prime powers increasingly as

\[
2\le q_1<q_2<\cdots,
\qquad \Lambda(q_k)>0,
\tag{1}
\]

and put

\[
x_k=-\log q_k,
\qquad
a_k=\frac{\Lambda(q_k)}{q_k+1}.
\tag{2}
\]

Thus the reflected Mangoldt Herglotz measure of `WP-318` is

\[
\mu=\sum_{k\ge1}a_k\delta_{x_k}.
\tag{3}
\]

For **every** consecutive support gap define

\[
t_j=\frac{x_j+x_{j+1}}2,
\qquad
g_j=x_j-x_{j+1}
     =\log\frac{q_{j+1}}{q_j}>0,
\tag{4}
\]

and let

\[
D_j=\sum_{k\ge1}\frac{a_k}{(x_k-t_j)^2}.
\tag{5}
\]

Let `rho_j` be the derivative-biased probability law of `mu` at `t_j`, pushed to the same physical gap coordinate

\[
u=\frac{x-t_j}{g_j}.
\tag{6}
\]

Then there exists a **single positive non-atomic, locally absolutely continuous Herglotz measure** `mu_ctrl` such that every `t_j` remains a regular support-free point, and if `Dhat_j` and `rhohat_j` denote its derivative and derivative-biased law at the **same** node and scale, then

\[
\boxed{
\frac{\widehat D_j}{D_j}\longrightarrow1,
\qquad
 d_{\rm BL}(\widehat\rho_j,\rho_j)\longrightarrow0
\quad (j\to\infty).
}
\tag{7}
\]

No thinning of the gap sequence is used.

This becomes stronger on the unavoidable fixed-additive-gap family of `WP-319`. Along that entire family the arithmetic laws `rho_j` are uniformly tight. Hence (7) implies, for every compact `K` in the upper half-plane,

\[
\boxed{
\sup_{\zeta\in K}
\left|
K_{\widehat\rho_j}(\zeta)-K_{\rho_j}(\zeta)
\right|\longrightarrow0.
}
\tag{8}
\]

By `WP-318`, the canonically normalized scalar Julia responses therefore converge locally uniformly as well. This holds on the **full unthinned fixed-gap family**, not merely on the sparse subsequence used by `WP-320`.

Thus nonsparse same-source provenance plus asymptotic coherence of all local derivative-biased gap laws is still not an arithmetic-selective scalar positivity mechanism. A surviving scalar route must use an invariant that is discontinuous in this natural weak/Julia topology, detects exact atomic/support arithmetic, or couples the finite source to genuinely global/archimedean data before scalar Julia reduction.

The result does **not** construct the Weil form and does not claim that every exact cross-gap identity can be smoothed away. It is a matched-control obstruction to a specific family-level escape from `WP-318`--`WP-320`.

**Classification:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + ALL-GAP-MATCHED-CONTROL + NONATOMIC-SMOOTHING + NONSPARSE-FAMILY-COHERENCE + BOUNDED-LIPSCHITZ + FULL-BOUNDED-GAP-JULIA-CONTROL + NOT-WEIL-POSITIVITY`.

## 1. The Mangoldt source has finite boundary derivatives and a uniform derivative floor

The Herglotz integrability condition holds because

\[
\sum_{k\ge1}\frac{a_k}{1+x_k^2}
=
\sum_{n\ge2}
\frac{\Lambda(n)/(n+1)}{1+(\log n)^2}
<\infty.
\tag{9}
\]

For example, on the exponential shell `e^m<=n<e^{m+1}`, Chebyshev's bound `psi(x)=O(x)` gives

\[
\sum_{e^m\le n<e^{m+1}}\frac{\Lambda(n)}n=O(1),
\tag{10}
\]

and the extra factor `(1+m^2)^{-1}` is summable. The same shell argument, using that `t_j` lies a positive distance from the support, shows that every `D_j` in (5) is finite.

A second elementary fact is decisive for the diagonal construction below: no fixed finite collection of atoms carries asymptotically nonzero derivative-biased mass.

Write

\[
L_j=-t_j=\frac{\log q_j+\log q_{j+1}}2\longrightarrow\infty.
\tag{11}
\]

The prime number theorem and partial summation give

\[
\sum_{e^{L+1}<n\le e^{L+2}}
\frac{\Lambda(n)}{n+1}
=1+o(1)
\qquad(L\to\infty).
\tag{12}
\]

For such `n`, `1<=log n-L<=2`. Therefore

\[
D_j
\ge
\frac14
\sum_{e^{L_j+1}<n\le e^{L_j+2}}
\frac{\Lambda(n)}{n+1}
\ge c>0
\tag{13}
\]

for all sufficiently large `j`.

For each fixed support index `k`, its derivative-biased weight is

\[
w_{j,k}
:=
\rho_j(\{(x_k-t_j)/g_j\})
=
\frac{a_k/(x_k-t_j)^2}{D_j}.
\tag{14}
\]

Equations (11)--(13) imply

\[
w_{j,k}\longrightarrow0
\qquad(j\to\infty)
\tag{15}
\]

for every fixed `k`. Hence, for every fixed `K`,

\[
\sum_{k\le K}w_{j,k}\longrightarrow0.
\tag{16}
\]

This is the only arithmetic input needed by the smoothing argument beyond positivity and local discreteness.

## 2. Choose finite derivative cores whose indices themselves escape

Equation (16) permits a diagonal choice of integers `m_j -> infinity` and errors `eps_j -> 0` such that

\[
\rho_j(\{k<m_j\})\le\varepsilon_j.
\tag{17}
\]

One explicit construction is to choose increasing thresholds `J_r` so that

\[
j\ge J_r
\quad\Longrightarrow\quad
\rho_j(\{k\le r\})<1/r,
\tag{18}
\]

and then let `r(j)` be the largest `r` with `J_r<=j`, taking `m_j=r(j)+1` and `eps_j=1/r(j)` once `r(j)>=1`.

Because `rho_j` is a probability measure on a countable support, choose `N_j>=m_j` so that

\[
\rho_j(\{k>N_j\})\le\varepsilon_j.
\tag{19}
\]

Set

\[
F_j:=\{m_j,m_j+1,\ldots,N_j\}.
\tag{20}
\]

Then

\[
\rho_j(F_j^c)\le2\varepsilon_j\to0.
\tag{21}
\]

The crucial direction of the diagonalization is that **every fixed atom index `k` belongs to only finitely many sets `F_j`**, because `m_j->infinity`. This makes it possible to impose arbitrarily fine gap-scale accuracy on every local core while still giving each original atom a strictly positive smoothing radius.

## 3. Smooth every atom once, with finitely many strong constraints per atom

For each support point `x_k`, let

\[
\delta_k:=\inf_j|x_k-t_j|>0.
\tag{22}
\]

Since the `t_j` are consecutive-support midpoints, the infimum is attained at one of the two adjacent gaps. Start with a radius

\[
0<r_k<\min\{1,\delta_k/4\}.
\tag{23}
\]

For every pair `(j,k)` with `k in F_j`, impose in addition

\[
a_k
\sup_{|y-x_k|\le r_k}
\left|
\frac1{(y-t_j)^2}-\frac1{(x_k-t_j)^2}
\right|
\le
\frac{\varepsilon_jD_j}{2|F_j|},
\tag{24}
\]

and

\[
a_k\frac1{(x_k-t_j)^2}\frac{r_k}{g_j}
\le
\frac{\varepsilon_jD_j}{2|F_j|}.
\tag{25}
\]

For fixed `k` there are only finitely many relevant `j`, by the final sentence of Section 2. The left sides of (24)--(25) tend to zero with `r_k`. Therefore a strictly positive radius satisfying all constraints exists.

Let `sigma_k` be normalized Lebesgue measure on

\[
I_k=[x_k-r_k,x_k+r_k]
\tag{26}
\]

and define

\[
\boxed{
\mu_{\rm ctrl}:=\sum_{k\ge1}a_k\sigma_k.
}
\tag{27}
\]

This measure is positive and non-atomic. It is in fact locally absolutely continuous. Equation (23) leaves an open neighborhood of every midpoint `t_j` outside all intervals `I_k`, so every original gap node remains regular.

The Herglotz growth condition is also preserved. Since `r_k<=1`, the weights `(1+y^2)^{-1}` on `I_k` are uniformly comparable, outside finitely many initial indices, with `(1+x_k^2)^{-1}`. Thus (9) implies

\[
\int_{\mathbb R}\frac{d\mu_{\rm ctrl}(y)}{1+y^2}<\infty.
\tag{28}
\]

No prime-power atom remains in the control source.

## 4. Kernel comparability controls the tails while the finite cores are arbitrarily accurate

Put

\[
f_j(x):=\frac1{(x-t_j)^2}.
\tag{29}
\]

Because `r_k<=delta_k/4` and `delta_k<=|x_k-t_j|`, every `y in I_k` satisfies

\[
|y-t_j|\ge\frac34|x_k-t_j|,
\tag{30}
\]

hence

\[
f_j(y)\le\frac{16}{9}f_j(x_k).
\tag{31}
\]

Let `lambda_j` be the unnormalized derivative-biased measure in gap coordinates,

\[
\lambda_j
=
\sum_k a_kf_j(x_k)
\delta_{(x_k-t_j)/g_j},
\qquad
\lambda_j(\mathbb R)=D_j,
\tag{32}
\]

and let `lambdahat_j` be the analogous measure for `mu_ctrl`.

Take any bounded-Lipschitz test function `phi` with

\[
\|\phi\|_\infty\le1,
\qquad
\operatorname{Lip}(\phi)\le1.
\tag{33}
\]

On a core atom `k in F_j`, equations (24)--(25) give

\[
\left|
 a_k\int_{I_k}
f_j(y)\phi\!\left(\frac{y-t_j}{g_j}\right)d\sigma_k(y)
-
a_kf_j(x_k)\phi\!\left(\frac{x_k-t_j}{g_j}\right)
\right|
\le
\frac{\varepsilon_jD_j}{|F_j|}
\tag{34}
\]

after shrinking the radii once more if necessary to replace `f_j(x_k)` by the uniformly close `f_j(y)` in the Lipschitz term. Summing over `F_j` costs at most `eps_j D_j`.

Outside `F_j`, (21) and (31) give

\[
\lambda_j(F_j^c)\le2\varepsilon_jD_j,
\qquad
\widehat\lambda_j(F_j^c)
\le\frac{32}{9}\varepsilon_jD_j.
\tag{35}
\]

Therefore there is an absolute constant `C` such that

\[
\boxed{
\|\widehat\lambda_j-\lambda_j\|_{\rm BL}
\le C\varepsilon_jD_j.
}
\tag{36}
\]

Using `phi=1` in the same estimate gives

\[
|\widehat D_j-D_j|
\le C\varepsilon_jD_j,
\tag{37}
\]

so

\[
\frac{\widehat D_j}{D_j}\to1.
\tag{38}
\]

After dividing (36) by the respective total masses and using (38),

\[
d_{\rm BL}(\widehat\rho_j,\rho_j)
\le C'\varepsilon_j
\longrightarrow0.
\tag{39}
\]

This proves (7) for the **entire sequence of consecutive prime-power support gaps**.

## 5. WP-319's full fixed-gap family therefore has one atomless Julia matched control

The bounded-Lipschitz conclusion alone is already enough to rule out any family invariant that is continuous in that topology. To reach the actual scalar Julia observable, one additionally needs reciprocal Cauchy-transform stability.

`WP-319` supplies exactly that missing compactness on its fixed-additive-gap family. Along that entire family, without further thinning,

\[
\limsup_j\rho_j(\{|u|>R\})\ll_d R^{-1}.
\tag{40}
\]

Hence the arithmetic laws are uniformly tight. Equation (39) makes the control laws uniformly tight as well.

Fix a compact `K subset C^+`. Tightness gives an `R` and `eta>0` such that every sufficiently late arithmetic and control law puts at least one half of its mass in `[-R,R]`, while `Im zeta>=eta` on `K`. Therefore

\[
-\operatorname{Im}G_{\rho_j}(\zeta)
=
\operatorname{Im}(\zeta)
\int\frac{d\rho_j(u)}{|\zeta-u|^2}
\ge c_K>0,
\tag{41}
\]

uniformly in `j` and `zeta in K`; the same holds for `rhohat_j`.

The kernels `u -> (zeta-u)^{-1}` are uniformly bounded and uniformly Lipschitz for `zeta in K`. Thus (39) gives

\[
\sup_{\zeta\in K}
|G_{\widehat\rho_j}(\zeta)-G_{\rho_j}(\zeta)|
\to0.
\tag{42}
\]

The lower bound (41) makes inversion uniformly continuous, yielding (8). By the exact normal form of `WP-318`,

\[
\frac{\mathcal J_{t_j}[f](t_j+g_j\zeta)-\beta_j}
{D_jg_j}
=-K_{\rho_j}(\zeta)
\tag{43}
\]

up to the harmless choice of affine origin used there, and the control has the analogous formula with hats. Together with (38) and (8), the normalized scalar Julia fields of the arithmetic source and the single atomless control are asymptotically indistinguishable on compact spectral sets over the **whole WP-319 fixed-gap family**.

This strictly strengthens `WP-320`: physical separation and summable block grafting are unnecessary once the control is allowed to smooth the original source atom by atom.

## 6. Aggressive falsification and boundaries

The construction should not be read more strongly than it proves.

First, `mu_ctrl` is deliberately target-engineered. Its small intervals remain centered at the prime-power logarithms. The result therefore does **not** say that prime locations can be forgotten. It says that scalar Julia observables with the continuity used in `WP-318`--`WP-320` cannot distinguish exact atomic Mangoldt support from a single non-atomic positive source that shadows it at every gap.

Second, (39) is asymptotic. An invariant that detects exact atoms, exact support endpoints, exact cross-gap equalities, or a topology stronger than bounded-Lipschitz may separate the two sources. Such an invariant would need its own independent sign theorem and matched-control audit; merely asserting exactness does not supply Weil positivity.

Third, local uniform convergence of the Boolean self-energies is asserted in Section 5 only on subfamilies with the uniform tightness needed to control reciprocal Cauchy transforms. `WP-319` provides that hypothesis for the complete fixed-additive-gap family. The present argument does not claim uniform Julia-profile convergence over every possible large prime-power gap.

Fourth, the control contains no archimedean Gamma term, pole term, trivial-zero divisor, or global finite--infinite coupling. Even a scalar invariant surviving the smoothing obstruction would still have to generate those pieces from the same independently positive geometry.

Finally, the construction changes category from an atomic arithmetic source to a locally absolutely continuous one. If a proposed mechanism explicitly requires atomicity as an intrinsic geometric axiom, this control is inadmissible; but then the sign must be shown to follow from that atomic geometric axiom rather than from the universal Herglotz/Julia positivity already classified in `WP-318`.

## Prior-art and novelty audit

The positivity and reduction machinery is not new. Agler--Young supplies the classical boundary Julia-Nevanlinna framework, and Speicher--Woroudi supplies the Boolean self-energy language already used in `WP-318`. Replacing a point mass by a narrow absolutely continuous bump is standard weak-approximation technology, not a Mathia novelty claim.

O'Neil and Sahlsten show a much broader qualitative warning: one Radon measure can exhibit an extremely flexible family of tangent measures. `WP-320` used that literature only as a comparison for sparse block grafting. The present argument is different and more elementary: it constructs one Herglotz control by atomwise smoothing and proves simultaneous quantitative approximation at the **prescribed arithmetic midpoint nodes and their prescribed individual gap scales**, with no thinning.

The derived contribution is therefore the matched-control consequence for Mathia's exact scalar observable: finite derivative cores can be chosen to escape every fixed atom, allowing each atom to satisfy only finitely many strong scale constraints. That diagonal fact removes the physical-separation hypothesis of `WP-320` and closes the natural nonsparse bounded-gap scalar escape left open there.

This is a negative result about source selectivity, not a new positive-function theorem and not a claim of literature novelty for mollification itself.

## Consequence for the research line

The scalar pure-measure Julia program has now crossed a stronger boundary:

\[
\text{one tangent}
\;\to\;
\text{sparse same-source family}
\;\to\;
\boxed{\text{all gap laws / full bounded-gap Julia family}}
\tag{44}
\]

all admit a single positive non-atomic matched control in the natural asymptotic topology relevant to the scalar reduction.

A future candidate cannot obtain arithmetic selectivity merely by asking for more scalar gap charts from the same Herglotz source. It must exploit exact non-smoothable arithmetic structure, move to a matrix/operator-valued or genuinely nonlocal response, or introduce the finite--archimedean/global coupling **before** the universal scalar Julia sign has erased the source distinction.
