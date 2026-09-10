# PF-260 — intrinsic Davies–Gaffney locality closes the full fixed-axis upper fractional window

**Status:** `LITERATURE+DERIVED + EXACT-SHORT-TIME-OFFDIAGONAL + FULL-FIXED-AXIS-UPPER-WINDOW + POSITIVE/ROUTE-STRENGTHENING`.

PF-259 proves the predicted `R<3/2+\sigma` Hilbert--Schmidt window only for the large-time/low-energy part of the Balakrishnan formula for the intrinsic-six thin-seam tangent. Its explicit remaining question is whether the unbounded jump rates can destroy the same window at short time.

They do not. The intrinsic path metric already constructed in PF-258 is exactly the structure needed by the sharp Davies--Gaffney--Grigor'yan theorem for weighted graphs with **unbounded** Laplacian. Applied to normalized singleton vectors after the PF-258 ground-state transform, that theorem gives an all-time `\ell^2` off-diagonal semigroup estimate with no vertex-volume prefactor. At fixed short time, the Davies rate is superalgebraically small across the separated cone because the intrinsic distance there is `\gtrsim\sqrt j`.

Consequently the entire short-time fractional contribution has arbitrary polynomial separated smoothing. Combining it with PF-259 yields, for every `0<\sigma<1`,

\[
\boxed{
|\langle e_i,H_\varepsilon^\sigma e_j\rangle|
\lesssim
(i+1)(j+1)^{-2-\sigma},
\qquad j\ge2i+2,
}
\tag{1}
\]

and hence

\[
\boxed{
E_dH_\varepsilon^\sigma N^R\in\mathcal S_2
\qquad
(0\le R<\tfrac32+\sigma).
}
\tag{2}
\]

At `\sigma=1/2`, every strict `1<R<2` therefore survives for the **full fixed-axis tangent**. This closes the short-time/high-energy obstruction identified by PF-259. It does **not** prove that `R=3/2+\sigma` is sharp, and it does not transfer the estimate uniformly to the finite-`s` relative seam or the actual corridor.

## Claim

Fix a parity `\varepsilon\in\{0,1\}` and let

\[
H_\varepsilon=A^{1/4}J_\varepsilon A^{1/4}
\]

be the positive linearly weighted Jacobi tangent from PF-258. Let `\mu_j>0` be its exact zero-mode ground state and

\[
m_j=\mu_j^2,
\qquad
c_j=-\widetilde a_j\mu_j\mu_{j+1}>0.
\tag{3}
\]

Multiplication by `\mu` is a unitary

\[
U:\ell^2(\mathbb N_0,m)\to\ell^2(\mathbb N_0),
\qquad
(Uf)_j=\mu_jf_j,
\tag{4}
\]

under which `H_\varepsilon` is the weighted path Laplacian

\[
(\widetilde Hf)_j
=
\frac{c_j}{m_j}(f_j-f_{j+1})
+
\frac{c_{j-1}}{m_j}(f_j-f_{j-1}),
\qquad c_{-1}=0.
\tag{5}
\]

PF-258/PF-259 give globally, after absorbing the finite initial segment,

\[
m_j\asymp(j+1)^2,
\qquad
c_j\asymp(j+1)^3,
\tag{6}
\]

and the intrinsic path metric with edge lengths

\[
\ell_j
=
\min\!\left\{
\sqrt{\frac{m_j}{2c_j}},
\sqrt{\frac{m_{j+1}}{2c_j}}
\right\}
\asymp(j+1)^{-1/2}.
\tag{7}
\]

Write `\rho` for the associated path distance and

\[
S:=\sup_j\ell_j<\infty
\tag{8}
\]

for its jump size. Then for every fixed `t_0>0`, every `0<\sigma<1`, and every `M>0`, the short-time multiplier

\[
T_{\sigma,<t_0}
:=C_\sigma\int_0^{t_0}
(I-e^{-tH_\varepsilon})\frac{dt}{t^{1+\sigma}}
\tag{9}
\]

satisfies

\[
\boxed{
|\langle e_i,T_{\sigma,<t_0}e_j\rangle|
\le C_{M,\sigma,t_0}(j+1)^{-M},
\qquad j\ge2i+2.
}
\tag{10}
\]

Moreover, for every `d>0` and every `R\ge0`,

\[
\boxed{
E_dT_{\sigma,<t_0}N^R\in\mathcal S_2,
\qquad
E_de_j=e^{-d(j+1)}e_j,
\quad
Ne_j=(j+1)e_j.
}
\tag{11}
\]

Combining (10)--(11) with PF-259's large-time estimate proves (1)--(2). Equation (2) is a sufficient window only.

## 1. The PF-258 metric is intrinsic in exactly the DGG sense

From (7), at an interior vertex `j`,

\[
c_{j-1}\ell_{j-1}^2+c_j\ell_j^2\le m_j.
\tag{12}
\]

Thus `\rho` is an intrinsic metric for the weighted graph `(\mathbb N_0,c,m)`. Its jump size is finite because `\ell_j\asymp(j+1)^{-1/2}` and only finitely many initial edges remain. PF-259 also records

\[
\rho(i,j)
\asymp
\left|\sqrt{i+1}-\sqrt{j+1}\right|.
\tag{13}
\]

No bounded weighted-degree hypothesis is available: indeed

\[
\operatorname{Deg}(j)
=
\frac{c_j+c_{j-1}}{m_j}
\asymp j+1.
\tag{14}
\]

This is precisely why PF-253's bounded-rate discrete-time argument cannot be copied. It is **not**, however, an obstruction to the intrinsic Davies--Gaffney estimate used below.

## 2. Sharp DGG gives an all-time singleton semigroup bound

Frank Bauer, Bobo Hua, and Shing-Tung Yau, *Sharp Davies--Gaffney--Grigor'yan Lemma on Graphs*, Mathematische Annalen **368** (2017), 1429--1437, DOI `10.1007/s00208-017-1529-z`, prove the functional DGG estimate for weighted graphs equipped with an intrinsic metric of finite jump size, including the unbounded-Laplacian setting. In their notation the rate is

\[
\zeta_S(t,r)
=
\frac1{S^2}
\left[
 rS\,\operatorname{arsinh}\!\left(\frac{rS}{t}\right)
 +t-\sqrt{t^2+r^2S^2}
\right].
\tag{15}
\]

For functions supported in sets at intrinsic distance `r`, their theorem bounds the heat-semigroup pairing by the product of the `\ell^2(m)` norms times `e^{-\lambda_0t-\zeta_S(t,r)}`, where `\lambda_0` is the spectral bottom.

Apply this to the closed weighted Dirichlet form unitarily equivalent to `H_\varepsilon`. Since `m_i=\mu_i^2`, the normalized singleton

\[
f_i=m_i^{-1/2}\mathbf1_{\{i\}}
\]

satisfies `Uf_i=e_i`. Positivity gives `\lambda_0\ge0`, so dropping the favorable spectral-bottom factor yields the exact counting-basis estimate

\[
\boxed{
|\langle e_i,e^{-tH_\varepsilon}e_j\rangle|
\le
\exp[-\zeta_S(t,\rho(i,j))]
\qquad(t>0).
}
\tag{16}
\]

There is no mass or volume prefactor in (16): normalization of the singleton vectors cancels it before conjugating back to counting measure.

## 3. At short time the DGG rate is superalgebraic in the separated cone

Let `r=\rho(i,j)`. Two elementary inequalities are enough:

\[
\sqrt{t^2+r^2S^2}-t\le rS,
\qquad
\operatorname{arsinh}x\ge\log(2x)
\quad(x>0).
\tag{17}
\]

Substituting them into (15) gives

\[
\zeta_S(t,r)
\ge
\frac rS
\left[
\log\!\left(\frac{2rS}{t}\right)-1
\right].
\tag{18}
\]

Put `q=r/S`. Whenever `q>\sigma`, equations (16)--(18) imply

\[
\begin{aligned}
\int_0^{t_0}
 e^{-\zeta_S(t,r)}\frac{dt}{t^{1+\sigma}}
&\le
\frac{e^q}{(2rS)^q}
\int_0^{t_0}t^{q-1-\sigma}\,dt\\
&=
\frac{t_0^{-\sigma}}{q-\sigma}
\left(\frac{e t_0}{2rS}\right)^q.
\end{aligned}
\tag{19}
\]

The right side decays faster than every negative power of `r` as `r\to\infty`.

In the separated cone `j\ge2i+2`, equation (13) gives

\[
\rho(i,j)
\ge c_0\sqrt{j+1}
\tag{20}
\]

for a fixed `c_0>0`, after changing constants on the finite initial segment. Hence for every `M>0`,

\[
\int_0^{t_0}
 e^{-\zeta_S(t,\rho(i,j))}
 \frac{dt}{t^{1+\sigma}}
\le C_{M,\sigma,t_0}(j+1)^{-M}.
\tag{21}
\]

For `i\ne j` the identity term in (9) vanishes. Equations (16) and (21) therefore prove (10). The finitely many separated pairs for which `\rho(i,j)/S\le\sigma` are absorbed into the constant using the fact that finitely supported basis vectors lie in the domain of every `H_\varepsilon^\sigma`, `0<\sigma<1`.

The important point is qualitative as well as quantitative: unbounded jump **rates** do not imply long short-time propagation when the correct intrinsic edge lengths are used. The decreasing edge scale in (7) is exactly what the DGG large-deviation rate sees.

## 4. The entire short-time weighted block is Hilbert--Schmidt for every polynomial weight

Equation (10) controls the only dangerous high-to-low region. It remains to check the complementary region without pretending that the short-time multiplier is bounded.

The Jacobi coefficients of `H_\varepsilon` are `O(i+1)` by PF-258, so

\[
\|H_\varepsilon e_i\|\le C(i+1).
\tag{22}
\]

For `0<\sigma<1`, spectral interpolation gives

\[
\|H_\varepsilon^\sigma e_i\|
\le
\|H_\varepsilon e_i\|^\sigma
\lesssim(i+1)^\sigma.
\tag{23}
\]

The scalar multiplier in (9) is pointwise bounded by `\lambda^\sigma`, hence

\[
\|T_{\sigma,<t_0}e_i\|
\le
\|H_\varepsilon^\sigma e_i\|
\lesssim(i+1)^\sigma.
\tag{24}
\]

On `j<2i+2`, `(j+1)^R\lesssim(i+1)^R`. Therefore

\[
\begin{aligned}
&\sum_i\sum_{j<2i+2}
 e^{-2d(i+1)}(j+1)^{2R}
 |\langle e_i,T_{\sigma,<t_0}e_j\rangle|^2\\
&\qquad\lesssim
\sum_i e^{-2d(i+1)}(i+1)^{2R}
 \|T_{\sigma,<t_0}e_i\|^2\\
&\qquad\lesssim
\sum_i e^{-2d(i+1)}(i+1)^{2R+2\sigma}
<\infty.
\end{aligned}
\tag{25}
\]

On `j\ge2i+2`, choose `M>R+1`; equation (10) makes the double square sum converge immediately. This proves (11) for every finite `R\ge0`.

Thus **short time imposes no polynomial separated-weight ceiling at all** in this fixed-axis problem.

## 5. PF-259 now yields the full fractional upper window

Write

\[
H_\varepsilon^\sigma
=T_{\sigma,<t_0}+T_{\sigma,\ge t_0}
\tag{26}
\]

using the same split as PF-259. That finding proves, in the separated cone,

\[
|\langle e_i,T_{\sigma,\ge t_0}e_j\rangle|
\lesssim
(i+1)(j+1)^{-2-\sigma}
\tag{27}
\]

and

\[
E_dT_{\sigma,\ge t_0}N^R\in\mathcal S_2
\qquad
(R<\tfrac32+\sigma).
\tag{28}
\]

The superalgebraic bound (10) is stronger than (27) at large separated indices, with the finite remainder absorbed into the constant. Therefore (26)--(28) give the full kernel bound (1). Combining (11) and (28) proves (2).

Equivalently, the currently proved upper-window ceiling comes entirely from the **large-time/low-energy** estimate. Short-time/high-energy propagation is not the mechanism that can kill the supercritical square-root margin.

At the physically relevant square root,

\[
\sigma=\frac12
\quad\Longrightarrow\quad
E_dH_\varepsilon^{1/2}N^R\in\mathcal S_2
\quad\text{for every }R<2.
\tag{29}
\]

Hence the strict interval `1<R<2` required as a fixed-axis source-smoothing margin is nonempty.

## 6. Prior art and novelty boundary

The DGG theorem is classical imported analysis, not a Mathia discovery. Bauer--Hua--Yau explicitly designed their sharp estimate to include unbounded graph Laplacians equipped with intrinsic metrics, so applying it here does not create a new general heat-kernel theorem. The Balakrishnan semigroup formula and the general principle that Davies--Gaffney estimates feed off-diagonal functional calculus are likewise standard.

The project-specific content is narrower:

1. PF-258 identifies the **actual** thin-seam tangent and its exact ground-state weighted graph rather than a bounded-rate surrogate;
2. PF-258/PF-259 verify the intrinsic metric geometry `m_j\asymp j^2`, `c_j\asymp j^3`, `\rho(0,j)\asymp\sqrt j` for that chain;
3. equations (18)--(21) show that the published DGG rate makes the previously unproved `0<t<t_0` Balakrishnan contribution superalgebraically local in the exact separated cone;
4. equations (22)--(25) upgrade that separated estimate to the complete weighted Hilbert--Schmidt short-time statement; and
5. combining this with PF-259 closes the full **upper** fixed-axis window.

No novelty is claimed for DGG, intrinsic metrics, fractional powers, or general functional-calculus locality. No exact discrete-Laguerre identification is needed.

## 7. Evidence boundary and next test

Equation (2) is one-sided. PF-259 supplies only an upper large-time heat-kernel estimate for the intrinsic-six chain, so this finding does **not** prove a matching lower fractional-kernel asymptotic or show that `R=3/2+\sigma` is the true threshold. The Bessel-six dimensional prediction remains a calibration, not a sharpness theorem.

More importantly, `H_\varepsilon` is only the `s\to0` fixed-axis tangent. PF-258 gives finite-dimensional `O(s^2)` convergence for

\[
\mathcal R_{s,r}^0
=s^{-1}A^{-1/4}f_{rs}(L)A^{-1/4},
\qquad
f_w(\lambda)=\sqrt\lambda\tanh(w\sqrt\lambda),
\tag{30}
\]

but that expansion is not uniform in the crossover `rs\sqrt L\sim1`. Therefore (29) cannot be promoted to a uniform finite-`s` weighted estimate by strong-resolvent or finite-dimensional convergence.

The next route-level test is now unambiguous: control the finite-`s` crossover of the **combined normalized relative-seam/Robin transform** while retaining some strict exponent `R>1`, then transport only that surviving margin through PF-256's actual corridor basis, PF-255's hypercycle ceiling, reflection factors, and PF-243's separated Robin--Poisson factorization.

Failure at that stage must exhibit a genuinely finite-`s` or corridor effect. It can no longer be attributed to uncontrolled short-time propagation of the intrinsic-six tangent.

Nothing here proves PF-243's actual separated Robin--Poisson estimate, uniform finite-`s` source locality, physical `P/H` recoupling, trace-class reassembly, finite-pant completion, a scattering/determinant theorem, any zeta-zero statement, or RH.