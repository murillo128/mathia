# PF-258 — the thin-seam relative edge is a linearly weighted Jacobi tangent with intrinsic dimension six

**Status:** `EXACT-DERIVED + THIN-SEAM-TANGENT + GROUND-STATE-TRANSFORM + INTRINSIC-VOLUME-SIX + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes|PF-247]] identifies the fixed-axis compactification through the bounded relative operator

\[
J=A^{-1/2}LA^{-1/2},
\qquad
A=-\partial_\theta^2+\csc^2\theta,
\]

and [[research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window|PF-253]] proves the sharp fractional kernel of `J^\sigma`. [[research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform|PF-257]] then shows that the physical normalized Robin injection should be studied as the combined transform `X(I+X^*X)^{-1}`, not by estimating a naked polar partial isometry.

There is an important scale correction between these statements. The operator entering the Robin relative seam is normalized by the **first-order corridor operator** `K`, not by `A` itself. In the exact fixed-axis symmetric seam control from [[research/prime_flute/findings/PF-235-hypercycle-boundary-compactification-has-only-quadratic-prime-dependent-defect|PF-235]],

\[
Q_w^0=L^{1/2}\tanh(wL^{1/2}),
\]

while the reference corridor scale is `K_s^0=sA^{1/2}`. If `w=rs` with fixed `r>0`, the corresponding dimensionless relative seam has the thin-seam tangent

\[
\boxed{
\mathcal R_{s,r}^0
=(K_s^0)^{-1/2}Q_{rs}^0(K_s^0)^{-1/2}
\longrightarrow
rH,
\qquad
H:=A^{-1/4}LA^{-1/4}=A^{1/4}JA^{1/4}.
}
\]

Thus the positive Robin edge is **not literally governed by `J`**. The quarter-order `A` sandwich is load-bearing. It converts each bounded PF-247 parity Jacobi chain into an unbounded, linearly weighted Jacobi chain. Using PF-251's exact positive zero solution, the ground-state transform of `H` has

\[
\boxed{
m_j\asymp (j+1)^2,
\qquad
c_j\asymp (j+1)^3,}
\]

where `m_j` is the reversible vertex mass and `c_j` the nearest-neighbor conductance. A canonical intrinsic edge length is therefore `\asymp(j+1)^{-1/2}`. The intrinsic distance from the origin grows like `\sqrt j`, while the mass of an origin-centered intrinsic ball grows like the sixth power of its radius:

\[
\boxed{
\rho(0,j)\asymp \sqrt{j+1},
\qquad
m(B_\rho(0,R))\asymp R^6.
}
\]

This is an exact structural calibration of the thin-seam relative edge. It does **not** yet prove a heat-kernel or fractional-power estimate for `H`, and it does not close the actual Robin smoothing gate. What it does prove is that PF-253's Bessel-four `J^\sigma` theorem cannot simply be inserted into PF-257 by identifying the relative seam edge with `J`. The correct tangent has different reversible geometry and unbounded jump rates. A new fractional-calculus theorem for this `H`-edge is required before its smoothing budget is spent on the actual `K_a`, hypercycle transport, reflection cycles, or PF-243 reassembly.

## Claim

Let `A,L,J` be the exact PF-247 operators, let

\[
f_w(\lambda)=\sqrt\lambda\tanh(w\sqrt\lambda),
\]

and define the fixed-axis symmetric seam control

\[
Q_w^0=f_w(L).
\tag{1}
\]

For `s>0` and a fixed ratio `r>0`, put

\[
K_s^0=sA^{1/2},
\qquad
\mathcal R_{s,r}^0
:=(K_s^0)^{-1/2}Q_{rs}^0(K_s^0)^{-1/2}.
\tag{2}
\]

Then:

1. in quadratic-form sense,
   \[
   \boxed{
   \mathcal R_{s,r}^0
   =s^{-1}A^{-1/4}f_{rs}(L)A^{-1/4};
   }
   \tag{3}
   \]
2. as `s\downarrow0`, the forms in (3) increase to the closed form of
   \[
   \boxed{
   rH,
   \qquad
   H=A^{-1/4}LA^{-1/4}=A^{1/4}JA^{1/4};
   }
   \tag{4}
   \]
   in particular the associated positive operators converge in strong resolvent sense;
3. on every fixed finite Gegenbauer/Galerkin regularization the convergence is in operator norm with error `O_{r,N}(s^2)`;
4. each parity block `H_\varepsilon` is again Jacobi. If `a_j^{(\varepsilon)},b_j^{(\varepsilon)}` are PF-247/PF-248's coefficients for `J_\varepsilon`, `n_j=2j+\varepsilon`, and `\kappa_n=n+\alpha`, then
   \[
   \boxed{
   \widetilde a_j^{(\varepsilon)}
   =\sqrt{\kappa_{n_j}\kappa_{n_{j+1}}}\,a_j^{(\varepsilon)},
   \qquad
   \widetilde b_j^{(\varepsilon)}
   =\kappa_{n_j}b_j^{(\varepsilon)};
   }
   \tag{5}
   \]
5. using PF-248's coefficient asymptotics,
   \[
   \boxed{
   \widetilde a_j^{(\varepsilon)}
   =-\frac j2-\frac{\alpha+\varepsilon+1}{4}+O(j^{-1}),
   \qquad
   \widetilde b_j^{(\varepsilon)}
   =j+\frac{\alpha+\varepsilon}{2}+O(j^{-1});
   }
   \tag{6}
   \]
6. if `\nu^{(\varepsilon)}` is PF-251's positive exact zero solution of `J_\varepsilon`, then
   \[
   \boxed{
   \mu_j^{(\varepsilon)}
   :=\kappa_{n_j}^{-1/2}\nu_j^{(\varepsilon)}
   }
   \tag{7}
   \]
   is an exact positive rowwise zero solution of `H_\varepsilon` and
   \[
   \boxed{
   \mu_j^{(\varepsilon)}
   =\widetilde C_\varepsilon(j+1)(1+O(j^{-1}));
   }
   \tag{8}
   \]
7. the ground-state transform defined by
   \[
   m_j=(\mu_j^{(\varepsilon)})^2,
   \qquad
   c_j=-\widetilde a_j^{(\varepsilon)}
   \mu_j^{(\varepsilon)}\mu_{j+1}^{(\varepsilon)}
   \tag{9}
   \]
   satisfies
   \[
   \boxed{
m_j\asymp(j+1)^2,
   \qquad
   c_j\asymp(j+1)^3,
   \qquad
   \frac{c_j}{m_j}\asymp j+1;
   }
   \tag{10}
   \]
8. with the intrinsic edge length
   \[
   \ell_j:=
   \min\left\{
   \sqrt{\frac{m_j}{2c_j}},
   \sqrt{\frac{m_{j+1}}{2c_j}}
   \right\},
   \tag{11}
   \]
   the induced path metric `\rho` is intrinsic for the weighted graph and obeys
   \[
   \boxed{
   \ell_j\asymp(j+1)^{-1/2},
   \quad
   \rho(0,j)\asymp\sqrt{j+1},
   \quad
   \sum_{\rho(0,j)\le R}m_j\asymp R^6.
   }
   \tag{12}
   \]

Equations (4)--(12) are properties of the **fixed-axis thin-seam relative tangent**. They are not asserted for the full actual complete-lift Robin operator without the remaining transfer arguments.

## 1. The thin seam differentiates to `L`, but Robin normalization inserts only a quarter power of `A`

PF-235's fixed compactification is unitary from the complete-axis coordinate, so its flat symmetric seam control is exactly (1). For `\lambda\ge0`,

\[
\frac1s f_{rs}(\lambda)
=r\lambda\,
\frac{\tanh(rs\sqrt\lambda)}{rs\sqrt\lambda}.
\tag{13}
\]

The scalar factor `tanh x/x` increases to `1` as `x\downarrow0`. Hence, as `s\downarrow0`, spectral calculus gives monotone form convergence

\[
\frac1s f_{rs}(L)\uparrow rL.
\tag{14}
\]

Sandwiching by the bounded positive operator `A^{-1/4}` gives (3)--(4). The limiting form is

\[
r\|L^{1/2}A^{-1/4}u\|^2,
\tag{15}
\]

on its natural domain. Standard monotone convergence of closed positive forms gives strong-resolvent convergence of the associated operators.

The finite-dimensional statement is even more elementary. For `x\ge0`,

\[
0\le x-\tanh x\le \frac{x^3}{3}.
\tag{16}
\]

Therefore on a fixed bounded Galerkin realization `L_N`,

\[
\left\|
\frac1s f_{rs}(L_N)-rL_N
\right\|
\le
\frac{r^3s^2}{3}\|L_N\|^2.
\tag{17}
\]

After the fixed `A_N^{-1/4}` sandwich this gives the claimed `O_{r,N}(s^2)` operator-norm error. This is exactly the bounded-regularization regime in which PF-254/PF-257's Robin algebra is already rigorous.

The normalization is the important point. Since

\[
J=A^{-1/2}LA^{-1/2},
\]

one has

\[
A^{-1/4}LA^{-1/4}
=A^{1/4}JA^{1/4},
\tag{18}
\]

not `J`. The first-order corridor normalizer therefore spends one half of the two `A^{-1/2}` factors used in PF-247's bounded relative operator. That missing half-order changes the threshold geometry.

## 2. The tangent remains parity-local but its Jacobi coefficients grow linearly

PF-247 proves that `J` preserves even and odd Gegenbauer modes and is tridiagonal in each parity chain. Since `A^{1/4}` is diagonal in the same basis, (18) preserves the exact tridiagonal pattern. Equation (5) follows immediately.

PF-248 gives, in parity-chain index `j`,

\[
a_j^{(\varepsilon)}
=-\frac14+\frac{1}{64j^2}+O(j^{-3}),
\qquad
b_j^{(\varepsilon)}
=\frac12+\frac{5}{32j^2}+O(j^{-3}).
\tag{19}
\]

Writing `c_\varepsilon=\alpha+\varepsilon`,

\[
\kappa_{n_j}=2j+c_\varepsilon,
\]

and

\[
\sqrt{\kappa_{n_j}\kappa_{n_{j+1}}}
=2j+c_\varepsilon+1+O(j^{-1}).
\tag{20}
\]

Substitution in (5) gives (6). Thus the critical bounded Jacobi chain has become an unbounded Jacobi operator with linear coefficients. It is still maximally local in chain distance; the new issue is its **rate geometry**, not long-range matrix entries at generator level.

## 3. PF-251's exact zero mode turns the tangent into a weighted birth-death form

PF-251 constructs an exact positive solution of the full half-line recurrence

\[
J_\varepsilon\nu^{(\varepsilon)}=0,
\qquad
\nu_j^{(\varepsilon)}
=C_\varepsilon j^{3/2}(1+O(j^{-1})).
\tag{21}
\]

Let `D_\varepsilon` be multiplication by `\kappa_{n_j}^{1/2}`. Since

\[
H_\varepsilon=D_\varepsilon J_\varepsilon D_\varepsilon,
\]

setting `\mu=D_\varepsilon^{-1}\nu` gives exactly

\[
H_\varepsilon\mu
=D_\varepsilon J_\varepsilon\nu=0
\tag{22}
\]

row by row, including the origin row. Equation (8) follows from `\kappa_{n_j}^{1/2}\asymp j^{1/2}`.

The off-diagonal coefficients are negative, so (9) defines positive conductances. Multiplication by `\mu` is an isometry from `\ell^2(m)` to ordinary `\ell^2`, and the transformed difference expression is

\[
\boxed{
(\widetilde Hf)_j
=\frac{c_j}{m_j}(f_j-f_{j+1})
+\frac{c_{j-1}}{m_j}(f_j-f_{j-1}).
}
\tag{23}
\]

Equations (6) and (8) give (10). This should be contrasted with PF-252's transform of `J`, where both mass and conductance are cubic. Here the mass loses one power while the conductance retains cubic growth, so the continuous-time jump rate grows linearly.

## 4. The natural intrinsic metric has sixth-power root volume

For a weighted graph with masses `m_j` and edge conductances `c_j`, a path metric is intrinsic when the squared edge lengths weighted by conductance sum to at most the vertex mass. The choice (11) gives at every vertex

\[
c_{j-1}\ell_{j-1}^2+c_j\ell_j^2\le m_j.
\tag{24}
\]

Hence it is intrinsic. Equation (10) gives

\[
\ell_j\asymp(j+1)^{-1/2}.
\tag{25}
\]

Summing along the half-line,

\[
\rho(0,j)
=\sum_{k<j}\ell_k
\asymp\sqrt{j+1}.
\tag{26}
\]

The reversible mass enclosed up to chain index `j` is

\[
\sum_{k\le j}m_k\asymp(j+1)^3.
\tag{27}
\]

Combining (26)--(27) gives the final statement in (12). In this precise intrinsic-volume sense the thin-seam relative tangent has a **dimension-six** growth law.

No Gaussian estimate is inferred from volume growth alone. In particular the unbounded rates in (10) mean that PF-253's discrete-time lazy-chain proof cannot be copied verbatim. Uniform Poincare/Sobolev control in the intrinsic metric, lower heat-kernel control, and the effect of the exact lower-order coefficients still have to be checked.

## 5. Consequence for the combined Robin gate

PF-257 writes the regularized normalized injection as

\[
B_X=X(I+X^*X)^{-1}=(I+XX^*)^{-1}X,
\tag{28}
\]

with positive left Gram variable `XX^*=\mathcal R`. Equations (3)--(4) therefore identify the positive thin-seam edge seen by the combined Robin transform: on bounded regularizations it is a regular function of an operator converging to `rH`, not to `rJ`.

This does **not** reintroduce PF-254's discarded requirement to control the polar factor separately. It says something narrower and necessary: any argument that spends PF-253's `J^{1/2}` kernel as though `\mathcal R^{1/2}` were literally `J^{1/2}` has skipped the `A^{1/4}` sandwich. The combined transform may still preserve favorable correlations that a polar split would lose, but those correlations must now be proved against the `H` tangent or directly in `X`, not inferred from PF-253 alone.

The new calibration remains encouraging rather than fatal. Dimension-six intrinsic growth is compatible with a supercritical smoothing window, and the exact generator remains nearest-neighbor in parity index. But the available theorem is no longer PF-253. The next fixed-axis step is a fractional/off-diagonal theorem for `H` (or directly for the thin-seam combined `B_X`) that is robust under the finite-to-form limit and then under the actual `K_a` and hypercycle transports.

## 6. Prior-art and novelty audit

Ground-state transforms of positive discrete Schrödinger/Jacobi operators into weighted graph Dirichlet forms are standard. A broad modern reference is M. Keller, Y. Pinchover, and F. Pogorzelski, *Criticality theory for Schrödinger operators on graphs*, Journal of Spectral Theory 10 (2020), 73--114, DOI `10.4171/JST/286`.

Linearly growing Jacobi matrices and their Markovian weighted transforms also have close classical models. A. Kostenko, *Heat kernels of the discrete Laguerre operators*, Letters in Mathematical Physics 111 (2021), Article 32, DOI `10.1007/s11005-021-01372-7`, gives explicit heat kernels for discrete Laguerre Jacobi operators and exhibits the corresponding weighted birth-death transform. It is useful prior art for the **kind** of unbounded-rate chain appearing here, but PF-258 does not identify `H_\varepsilon` with a discrete Laguerre operator and does not import Kostenko's kernel formulas.

For genuinely unbounded weighted graph Laplacians, intrinsic metrics are the appropriate heat-kernel geometry. M. Keller and C. Rose, *Gaussian upper bounds for heat kernels on graphs with unbounded geometry*, Journal of Spectral Theory 16 (2026), 709--750, DOI `10.4171/JST/604`, is a current reference for that framework. Its general upper-bound theorem is not used to claim a fractional kernel here; the lower/sharp estimates needed by the Prime-Flute smoothing problem remain to be verified for the exact chain.

A targeted structural search did not locate the PF-specific operator

\[
A^{-1/4}LA^{-1/4}
\]

arising as the thin-seam tangent of this compactified Robin relative seam, nor the resulting `(m_j,c_j)\asymp(j^2,j^3)` specialization. No novelty is claimed for monotone functional calculus, Jacobi ground-state transforms, intrinsic metrics, discrete Laguerre theory, or volume-growth arguments. The project-specific contribution is the exact correction of the live bridge: the relative seam tangent forced by the Prime-Flute scales is `H`, not PF-247's bounded `J`, and its reversible geometry is correspondingly different.

## 7. Falsification and boundary checks

1. **Reference fixed-axis stage only.** `Q_w^0` is PF-235's fixed-axis symmetric seam control. Hypercycle coordinate/density transport, the intrinsic hyperbolic seam correction, and the actual complete-lift realization remain outside (1)--(12).
2. **Reference corridor scale only.** `K_s^0=sA^{1/2}` is the fixed-axis calibration. PF-256 gives a two-derivative graph equivalence between `A` and the actual `T_a`, but it does not automatically transfer fractional kernels of `H`.
3. **Thin-seam ratio fixed.** The tangent takes `w=rs` with fixed `r`. It does not control arbitrary `w/s` or the entire high-frequency crossover where `rs\sqrt L` is order one or larger.
4. **Strong-resolvent is not weighted-kernel convergence.** Equation (4) does not imply the uniform high-to-low estimates required by PF-243.
5. **Intrinsic dimension is not yet a heat-kernel theorem.** Equation (12) is a metric-volume calculation from exact asymptotic masses/conductances. Gaussian bounds and fractional-power asymptotics require additional hypotheses.
6. **Combined transform still matters.** PF-257's warning remains in force: do not estimate a naked polar partial isometry unless a proof genuinely needs it. The new `H` tangent identifies the positive relative edge but does not separate away orientation from the physical `B_X`.
7. **No global conclusion.** Nothing here proves the PF-243 separated Robin-Poisson estimate, high-high trace class, weak-trace reassembly, finite-pant completion, scattering/determinant statements, a zeta-zero statement, or RH.

## Decisive next test

Prove or refute a sharp separated fractional-power estimate for the exact parity blocks of `H`. The ground-state data (10)--(12) suggest treating the problem as an unbounded-rate weighted birth-death diffusion in its intrinsic metric, with the discrete Laguerre heat kernel as a calibration rather than an identity. Only after a fixed-axis `H^{1/2}` or direct `B_X` theorem leaves some strict `R>1` margin should that margin be transferred through PF-256 and spent in PF-243's actual separated Robin-Poisson factorization.