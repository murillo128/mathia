# PF-259 — the intrinsic-six seam tangent has anchored Gaussian large-time control

**Status:** `EXACT-DERIVED + SPEED-MEASURE-TIME-CHANGE + BESSEL-SIX-SCALING + INTRINSIC-POINCARE + SOBOLEV-12 + LITERATURE+DERIVED-GAUSSIAN-UPPER + LARGE-TIME-FRACTIONAL-WINDOW + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-258-thin-seam-relative-edge-is-a-linearly-weighted-jacobi-tangent-with-intrinsic-dimension-six|PF-258]] identifies the correct fixed-axis thin-seam relative tangent

\[
H=A^{-1/4}LA^{-1/4}=A^{1/4}JA^{1/4}
\]

and proves that its positive ground-state transform has mass `m_j\asymp(j+1)^2`, conductance `c_j\asymp(j+1)^3`, intrinsic edge length `\ell_j\asymp(j+1)^{-1/2}`, and root-volume growth `V_\rho(R)\asymp R^6`. It deliberately stops before a heat-kernel theorem because the jump rates grow linearly and [[research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window|PF-253]]'s bounded-rate lazy-chain argument is unavailable.

There is nevertheless considerably more exact structure. The PF-258 weighted chain is an **exact speed-measure time change** of the PF-252 Bessel-four chain: its conductances are unchanged and only the reversible mass is divided by the corridor eigenvalue `\kappa_{2j+\varepsilon}`. This gives a squared-Bessel-six scaling law, but more importantly it makes the intrinsic functional geometry elementary enough to verify directly. The chain satisfies scale-invariant Poincare on intrinsic balls, sixth-order root volume doubling, and a uniform dimension-12 intrinsic isoperimetric/Sobolev inequality. Keller--Rose's anchored heat-kernel theorem for graphs with unbounded geometry then gives a Gaussian/Davies upper bound for all sufficiently large times.

Consequently, the **large-time/low-energy part** of the Balakrishnan representation already has exactly the supercritical separated decay suggested by the current intrinsic-six clue:

\[
\boxed{
|\langle e_i,T_{\sigma,\ge t_0}e_j\rangle|
\lesssim
(i+1)(j+1)^{-2-\sigma},
\qquad j\ge 2i+2,
}
\]

for every `0<\sigma<1`, where `T_{\sigma,\ge t_0}` is the bounded large-time Balakrishnan piece defined below. In PF-253's weighted notation this piece is Hilbert--Schmidt for every `R<3/2+\sigma`; at `\sigma=1/2` it therefore has the desired strict window `1<R<2`.

This is **not yet a theorem for the full fractional power `H^\sigma`**. Keller--Rose's anchored estimate starts at a fixed positive time `t_0`. The remaining `0<t<t_0` Balakrishnan contribution is a high-energy/off-diagonal problem for the unbounded-rate chain and is not controlled below. Thus the exact fixed-axis bottleneck has sharpened substantially: large-time diffusion does not kill the proposed window; the remaining obstruction is short-time/high-energy locality, followed by PF-258's non-uniform finite-`s` crossover and the actual-corridor/hypercycle transfers.

## Claim

Fix a parity `\varepsilon\in\{0,1\}`. Let `J_\varepsilon` be the PF-247 Jacobi block, write

\[
\kappa_j:=\kappa_{2j+\varepsilon}=2j+\alpha+\varepsilon,
\qquad
D e_j=\kappa_j^{1/2}e_j,
\]

so that the PF-258 tangent block is

\[
H_\varepsilon=DJ_\varepsilon D.
\tag{1}
\]

Let `\nu` be PF-251's positive full half-line zero solution for `J_\varepsilon`, let `\mu=D^{-1}\nu`, and denote PF-252's Bessel-four ground-state data by

\[
m_j^{(4)}=\nu_j^2,
\qquad
c_j^{(4)}=-a_j\nu_j\nu_{j+1}.
\tag{2}
\]

If `\widetilde a_j=\sqrt{\kappa_j\kappa_{j+1}}a_j` is the off-diagonal coefficient of `H_\varepsilon`, define its ground-state data by

\[
m_j^{(6)}=\mu_j^2,
\qquad
c_j^{(6)}=-\widetilde a_j\mu_j\mu_{j+1}.
\tag{3}
\]

Then:

1. the two weighted chains satisfy the exact identities
   \[
   \boxed{
   m_j^{(6)}=\frac{m_j^{(4)}}{\kappa_j},
   \qquad
   c_j^{(6)}=c_j^{(4)};
   }
   \tag{4}
   \]
2. if `\widetilde H_\varepsilon` is the weighted Laplacian associated with (3), then its jump rates satisfy
   \[
   \boxed{
   \frac{c_j^{(6)}}{m_j^{(6)}}
   =\frac j2+\frac{\alpha+\varepsilon}{4}+\frac34+O(j^{-1}),
   }
   \tag{5}
   \]
   \[
   \boxed{
   \frac{c_{j-1}^{(6)}}{m_j^{(6)}}
   =\frac j2+\frac{\alpha+\varepsilon}{4}-\frac34+O(j^{-1});
   }
   \tag{6}
   \]
3. for `F\in C_c^3((0,\infty))` and `f_j^{(N)}=F(j/N)`, uniformly for `j/N` in compact subsets of `(0,\infty)`,
   \[
   \boxed{
   N(\widetilde H_\varepsilon f^{(N)})_j
   \longrightarrow
   -\frac12\left(xF''(x)+3F'(x)\right),
   \qquad x=\frac jN;
   }
   \tag{7}
   \]
   after `x=r^2`, the right side is `-\frac18(g''+5r^{-1}g')`, the radial six-dimensional Laplacian up to scale;
4. for PF-258's intrinsic path metric `\rho`, after changing finitely many constants if necessary,
   \[
   \rho(i,j)\asymp
   \left|\sqrt{i+1}-\sqrt{j+1}\right|,
   \tag{8}
   \]
   and root balls satisfy
   \[
   \boxed{m(B_0(R))\asymp R^6}
   \tag{9}
   \]
   for all sufficiently large `R`, hence anchored volume doubling holds with dimension `d=6`;
5. every intrinsic ball `B=B_\rho(i,R)` with sufficiently large `R` satisfies the scale-invariant Poincare inequality
   \[
   \boxed{
   \sum_{j\in B}m_j^{(6)}|f_j-f_B|^2
   \le CR^2
   \sum_{\{j,j+1\}\subset B}c_j^{(6)}|f_{j+1}-f_j|^2;
   }
   \tag{10}
   \]
6. root balls satisfy a uniform Keller--Rose isoperimetric inequality of dimension `n=12`, and therefore the Sobolev property `S(12,R_1,\infty)` for some fixed `R_1`; together with (9), this gives `SV(R_1,\infty,6,12)`;
7. the geometry-error factor in Keller--Rose's anchored theorem is uniformly bounded for this chain, so there are `t_0,C>0` such that its heat-kernel density `p_t(i,j)` with respect to `m^{(6)}` satisfies, for all `t\ge t_0`,
   \[
   \boxed{
   p_t(i,j)
   \le
   \frac{C}{m(B_0(\sqrt t))}
   \left(1+\frac{\rho(0,i)^2+\rho(0,j)^2}{t}\right)^6
   \left(1+\frac{\rho(i,j)^2}{t}\right)^6
   e^{-\zeta_S(\rho(i,j),t)};
   }
   \tag{11}
   \]
   here `S<\infty` is the intrinsic jump size and `\zeta_S` is Davies' graph rate function;
8. for `0<\sigma<1`, define the bounded large-time Balakrishnan operator
   \[
   T_{\sigma,\ge t_0}
   :=C_\sigma\int_{t_0}^{\infty}
   (I-e^{-tH_\varepsilon})\frac{dt}{t^{1+\sigma}}.
   \tag{12}
   \]
   For distinct indices in the separated cone `j\ge2i+2`,
   \[
   \boxed{
   |\langle e_i,T_{\sigma,\ge t_0}e_j\rangle|
   \lesssim
   (i+1)(j+1)^{-2-\sigma}.
   }
   \tag{13}
   \]
   Hence, with PF-253's `Ne_j=(j+1)e_j` and `E_d=e^{-dN}`, the whole large-time operator satisfies
   \[
   \boxed{
   E_dT_{\sigma,\ge t_0}N^R\in\mathcal S_2
   \qquad\text{for every }R<\frac32+\sigma.
   }
   \tag{14}
   \]

No lower bound or sharpness is asserted in (11)--(14), and (14) is not asserted for the missing short-time contribution to `H_\varepsilon^\sigma`.

## 1. The intrinsic-six chain is an exact speed-measure time change of Bessel four

Equation (4) is algebraic. Since `\mu_j=\kappa_j^{-1/2}\nu_j`,

\[
m_j^{(6)}=\mu_j^2=\kappa_j^{-1}\nu_j^2
=\frac{m_j^{(4)}}{\kappa_j}.
\]

For the conductance, the quarter-order sandwich cancels exactly against the transformed zero mode:

\[
\begin{aligned}
c_j^{(6)}
&=-\sqrt{\kappa_j\kappa_{j+1}}a_j
  \frac{\nu_j}{\sqrt{\kappa_j}}
  \frac{\nu_{j+1}}{\sqrt{\kappa_{j+1}}}\\
&=-a_j\nu_j\nu_{j+1}
=c_j^{(4)}.
\end{aligned}
\tag{15}
\]

Thus PF-258 does not create a new edge-energy profile: it changes the **clock** of the PF-252 chain by replacing `m^{(4)}` with `m^{(4)}/\kappa`. In particular,

\[
\frac{c_j^{(6)}}{m_j^{(6)}}
=\kappa_j\frac{c_j^{(4)}}{m_j^{(4)}},
\qquad
\frac{c_{j-1}^{(6)}}{m_j^{(6)}}
=\kappa_j\frac{c_{j-1}^{(4)}}{m_j^{(4)}}.
\tag{16}
\]

PF-252 proves

\[
\frac{c_j^{(4)}}{m_j^{(4)}}
=\frac14+\frac{3}{8j}+O(j^{-2}),
\qquad
\frac{c_{j-1}^{(4)}}{m_j^{(4)}}
=\frac14-\frac{3}{8j}+O(j^{-2}).
\tag{17}
\]

Multiplying by `\kappa_j=2j+\alpha+\varepsilon` gives (5)--(6). This exact time-change relation is stronger than merely observing the coarse PF-258 asymptotics `m_j\asymp j^2`, `c_j\asymp j^3`.

## 2. The continuum calibration is squared Bessel of dimension six

Insert

\[
f_{j\pm1}^{(N)}
=F(x)\pm N^{-1}F'(x)
+\frac12N^{-2}F''(x)+O(N^{-3})
\]

into the weighted difference expression from PF-258. Equations (5)--(6) give

\[
\frac{c_{j-1}}{m_j}-\frac{c_j}{m_j}
=-\frac32+O(j^{-1}),
\qquad
\frac{c_{j-1}+c_j}{m_j}
=j+O(1).
\]

Therefore

\[
(\widetilde H_\varepsilon f^{(N)})_j
=-\frac{1}{2N}\left(xF''(x)+3F'(x)\right)+O(N^{-2})
\]

on compact `x`-ranges, proving (7). With `x=r^2` this becomes

\[
-\frac18\left(g''(r)+\frac5r g'(r)\right).
\]

Linear birth--death/squared-Bessel correspondences are classical, so the phrase “Bessel six” is a calibration rather than a novelty claim. The useful project-specific fact is that the exact PF chain reaches this calibration through (4), not by matching only leading matrix coefficients.

## 3. Intrinsic balls satisfy volume doubling and Poincare

PF-258's intrinsic edge length satisfies

\[
\ell_j\asymp(j+1)^{-1/2}.
\tag{18}
\]

Summing (18) between two indices gives (8). Since `m_j^{(6)}\asymp(j+1)^2`, a root ball of radius `R` reaches index `\asymp R^2`, and summing the quadratic masses proves (9). In particular root volume doubling is sixth-order.

The same one-dimensional structure gives (10) directly. Write an intrinsic ball as the integer interval `B=[L,U]`. The weighted mean `f_B` minimizes weighted squared error, so it is enough to compare with `f_U`. By Cauchy--Schwarz along the unique path,

\[
|f_j-f_U|^2
\le
\left(\sum_{k=j}^{U-1}\frac1{c_k}\right)
\left(\sum_{k=j}^{U-1}c_k|f_{k+1}-f_k|^2\right).
\tag{19}
\]

After multiplying by `m_j` and summing,

\[
\sum_{j=L}^Um_j|f_j-f_U|^2
\le
\mathcal E_B(f)
\sum_{j=L}^Um_j\sum_{k=j}^{U-1}\frac1{c_k},
\tag{20}
\]

where `\mathcal E_B(f)` is the edge energy on `B`.

If `L\ge U/2`, all indices in the ball are comparable. Writing `q=U-L+1`, the last factor in (20) is `O(q^2/(L+1))`; (8) gives `q\lesssim R\sqrt{L+1}`, hence it is `O(R^2)`. If `L<U/2`, then (8) forces `U+1\lesssim R^2`. Since

\[
\sum_{k=j}^{\infty}c_k^{-1}\lesssim(j+1)^{-2}
\]

and `m_j\lesssim(j+1)^2`, every summand in the last factor of (20) is bounded, and there are `O(R^2)` of them. This proves (10), with the finite initial region absorbed into the constant.

## 4. Root isoperimetry gives a dimension-12 Sobolev inequality

For the same intrinsic metric,

\[
c_j\ell_j\asymp(j+1)^{5/2}.
\tag{21}
\]

Let `W` be any nonempty finite subset of a root ball and decompose it into disjoint integer intervals `I_r=[a_r,b_r]`. The right boundary edge of each component alone contributes

\[
b\rho(\partial I_r)
\gtrsim (b_r+1)^{5/2}.
\tag{22}
\]

On the other hand,

\[
m(I_r)=\sum_{j=a_r}^{b_r}m_j
\lesssim(b_r+1)^3,
\]

so (22) gives

\[
b\rho(\partial I_r)\gtrsim m(I_r)^{5/6}.
\tag{23}
\]

Because `x\mapsto x^{5/6}` is concave,

\[
\sum_r m(I_r)^{5/6}
\ge
\left(\sum_r m(I_r)\right)^{5/6},
\]

and therefore Keller--Rose's intrinsic isoperimetric constant obeys

\[
\boxed{h_{B_0(R),12}\ge c>0}
\tag{24}
\]

uniformly in sufficiently large `R`.

Theorem 3.4 of Matthias Keller and Christian Rose, *Anchored heat kernel upper bounds on graphs with unbounded geometry and anti-trees*, Calc. Var. PDE **63** (2024), article 20, DOI `10.1007/s00526-023-02622-3`, turns (24) into Sobolev control. Taking their parameter `C=R`, and using

\[
\frac{m(B_0(R))^{2/12}}{R^2}\asymp\frac1R,
\]

shows exactly that `S(12,R_1,\infty)` holds after increasing a fixed `R_1`. Together with root volume doubling, this is `SV(R_1,\infty,6,12)` in their notation.

## 5. The unbounded geometry correction remains harmless

Keller--Rose's Theorem 2.1 allows unbounded weighted vertex degree through an explicit factor `\Gamma`. Choose an admissible finite `p>1` with Holder conjugate `q>6=n/2`. Since

\[
\operatorname{Deg}(j)
=\frac{c_j+c_{j-1}}{m_j}
\asymp j+1,
\]

and a root ball of radius `R` contains only `j\lesssim R^2`, their averaged degree obeys

\[
D_p(R)\lesssim R^2.
\tag{25}
\]

Also `m_j` has a positive global lower bound, so their averaged inverse-measure quantity satisfies `M_p(R)\le C`. Finally `m(B_0(R))\asymp R^6`. In the Keller--Rose error factor the bracket containing `D_p`, `M_p`, and root volume therefore grows only polynomially, while its exponent `\theta(R)` decays exponentially in `\sqrt R` for the admissible choice `q>n/2`. Consequently

\[
\sup_{R\ge R_1}\Gamma(R)<\infty.
\tag{26}
\]

All other geometric hypotheses of Theorem 2.1 are already explicit: (18) has finite jump size and its balls are finite. Increasing `R_1` once more to meet the theorem's fixed scale condition, then taking the outer radius to infinity, yields (11). The displayed version uses the elementary estimate on Keller--Rose's second polynomial correction

\[
1\vee S^{-2}\bigl(\sqrt{t^2+S^2r^2}-t\bigr)
\lesssim 1+\frac{r^2}{t},
\]

and drops the favorable nonnegative spectral-bottom factor.

The later Keller--Rose paper *Gaussian upper bounds for heat kernels on graphs with unbounded geometry*, J. Spectr. Theory **16** (2026), 709--750, DOI `10.4171/JST/604`, develops the same large-time unbounded-geometry framework further; no additional 2026 theorem is needed for (11).

## 6. Large-time Balakrishnan mass already has the predicted separated exponent

Let `p_t` be the weighted heat-kernel density in (11). Because multiplication by `\mu` is the ground-state unitary,

\[
\langle e_i,e^{-tH_\varepsilon}e_j\rangle
=\mu_i\mu_j p_t(i,j).
\tag{27}
\]

In the separated cone `j\ge2i+2`, put `J=j+1`. Equations (8)--(9) give

\[
\rho(i,j)^2\asymp J,
\qquad
\rho(0,i)^2+\rho(0,j)^2\lesssim J,
\qquad
m(B_0(\sqrt t))\asymp t^3
\]

for the large scales relevant below. Thus (11) implies

\[
p_t(i,j)
\lesssim
t^{-3}\left(1+\frac Jt\right)^{12}
\exp[-\zeta_S(c\sqrt J,t)]
\tag{28}
\]

for `t\ge t_0`, after enlarging constants to cover bounded indices.

Davies' function has two elementary regimes. For `t\ge S\sqrt J`, compactness of the bounded ratio range in its defining formula gives

\[
\zeta_S(c\sqrt J,t)\gtrsim J/t,
\]

while for `t_0\le t\le S\sqrt J` it is at least `c'\sqrt J` up to constants depending only on the fixed jump size. The latter range therefore contributes faster than any negative power of `J`. On the first range, `u=J/t` gives

\[
\int_{S\sqrt J}^{\infty}
 t^{-4-\sigma}
 \left(1+\frac Jt\right)^{12}
 e^{-cJ/t}\,dt
\lesssim J^{-3-\sigma}.
\tag{29}
\]

PF-258 gives `\mu_k\asymp k+1`. For `i\ne j`, the identity term in (12) vanishes, so multiplying (29) by `\mu_i\mu_j` in (27) proves (13).

It remains to justify that the complementary matrix region does not affect (14). The operator `T_{\sigma,\ge t_0}` is bounded by spectral calculus because the integral in (12) starts at `t_0>0`. When `j<2i+2`, one has `(j+1)^R\lesssim(i+1)^R` for `R\ge0`. Hence the squared `\ell^2` norm of the `i`-th weighted row over this complementary region is bounded by

\[
C e^{-2d(i+1)}(i+1)^{2R}\|T_{\sigma,\ge t_0}\|^2,
\]

which is summable in `i`. On the separated region, squaring (13) and multiplying by `(j+1)^{2R}` gives a convergent `j`-sum whenever

\[
2R-4-2\sigma<-1,
\]

namely `R<3/2+\sigma`; the remaining `i`-sum is again killed by `E_d`. This proves the **sufficient** Hilbert--Schmidt window (14). No converse follows from the one-sided heat-kernel estimate.

## 7. Prior art, evidence boundary, and next test

Keller--Rose supply the imported heat-kernel theorem and the isoperimetry-to-Sobolev implication; the verification of their hypotheses above is specific to the PF-258 chain. Aleksey Kostenko, *Heat kernels of the discrete Laguerre operators*, Lett. Math. Phys. **111** (2021), article 32, DOI `10.1007/s11005-021-01372-7`, gives exact heat kernels for a classical family of linearly growing Laguerre Jacobi matrices and their weighted Markovian realizations. Laurent Miclo and Pierre Patie, *On a gateway between continuous and discrete Bessel and Laguerre processes*, Annales Henri Lebesgue **2** (2019), 59--98, DOI `10.5802/ahl.13`, establish a classical two-way relation between squared-Bessel processes and linear birth--death processes. These sources make clear that neither linearly growing Jacobi matrices nor Bessel/Laguerre birth--death scaling is new in itself.

No identity with a discrete Laguerre operator is used here. In particular, the exact lower-order PF coefficients are not discarded, and no Laguerre heat kernel is transplanted to `H_\varepsilon`. The project-specific contribution is (4), the direct intrinsic Poincare/isoperimetric verification for that exact chain, and the resulting application of Keller--Rose to obtain (11)--(14).

The strongest remaining boundary is **short time**. The full Balakrishnan formula for `H_\varepsilon^\sigma` also contains

\[
T_{\sigma,<t_0}
=C_\sigma\int_0^{t_0}
(I-e^{-tH_\varepsilon})\frac{dt}{t^{1+\sigma}},
\tag{30}
\]

and (11) does not estimate its off-diagonal matrix elements. Unbounded rates mean that bounded-generator power-series arguments from PF-253 cannot simply replace the missing estimate. A uniform intrinsic Davies/high-energy locality theorem strong enough for (30), or a direct resolvent/functional-calculus argument for the exact linearly weighted Jacobi matrix, would complete the fixed-axis **upper** estimate suggested by the clue. Sharpness would still require a matching lower bound or another obstruction argument.

Even a full fixed-axis `H^{1/2}` estimate would not finish the Prime-Flute route. PF-258's finite-dimensional `O(s^2)` tangent error is not uniform in the crossover `rs\sqrt L\sim1`; the actual `K_a` replacement, PF-255/PF-256 hypercycle transport, reflection factors, PF-243 separated Robin-Poisson factorization, trace-class reassembly, finite-pant completion, scattering/determinant bridge, any zeta-zero statement, and RH all remain outside this finding.

**Decisive next test.** Prove or refute a short-time off-diagonal estimate for the exact `H_\varepsilon` semigroup that makes (30) obey the same separated bound as (13). If it succeeds, the full fixed-axis upper fractional window `R<3/2+\sigma` follows; at `\sigma=1/2` this leaves `1<R<2`. If it fails, identify an escaping high-frequency packet showing that the large-time Bessel-six gain is destroyed by the high-energy part rather than by the diffusive threshold geometry.