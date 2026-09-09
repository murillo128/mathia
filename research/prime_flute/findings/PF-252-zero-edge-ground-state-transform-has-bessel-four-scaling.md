# PF-252 — zero-edge ground-state transform has Bessel-four scaling

**Status:** `EXACT-DERIVED + GROUND-STATE-REPRESENTATION + BESSEL-FOUR-SCALING + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-251-exact-zero-edge-solutions-select-growing-inverse-square-jacobi-branch|PF-251]] identifies, in each parity sector of the fixed-axis relative Jacobi operator
\[
J=A^{-1/2}LA^{-1/2},
\]
the unique zero-energy solution satisfying the actual half-line boundary condition. It is strictly positive and grows as
\[
\nu_j^{(\varepsilon)}=C_\varepsilon j^{3/2}(1+O(j^{-1})).
\]
That exact boundary solution can be used as a ground-state/Doob transform. The resulting weighted nearest-neighbor operator has mass and conductance both growing like \(j^3\), and its diffusive scaling limit is
\[
-\frac14\left(\partial_x^2+\frac3x\partial_x\right),
\]
the radial Laplacian in four Euclidean dimensions, scaled by \(1/4\).

This gives a sharper interpretation of PF-248/PF-251's inverse-square threshold. The free Dirichlet chain used in PF-248--PF-250 has boundary zero mode \(j+1\) and the analogous ground-state transform has three-dimensional radial scaling. The actual [[research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes|PF-247]] inverse-square tail therefore changes the threshold model from Bessel dimension three to Bessel dimension four. It does **not** merely add an arbitrary trace-class defect to the free edge.

The result does not yet prove the low-energy spectral density, fractional-power matrix decay, or the \(R>1\) separated Robin-Poisson estimate. It does, however, replace the generic perturbative picture by an exact positive weighted-chain model whose endpoint geometry can be attacked with Bessel/heat-kernel methods.

## Claim

Fix one parity \(\varepsilon\in\{0,1\}\), and write the PF-247 Jacobi block as
\[
(J_\varepsilon u)_j
=a_j u_{j+1}+b_j u_j+a_{j-1}u_{j-1},
\qquad j\ge0,
\]
with the origin-row convention \(a_{-1}=0\). PF-247's exact formulas give \(a_j<0\). Let \(\nu=\nu^{(\varepsilon)}\) be PF-251's positive full half-line zero solution:
\[
J_\varepsilon\nu=0,
\qquad
\nu_j=C_\varepsilon j^{3/2}(1+O(j^{-1})).
\]

Define
\[
m_j:=\nu_j^2,
\qquad
c_j:=-a_j\nu_j\nu_{j+1}>0.
\]
Then:

1. multiplication by \(\nu\),
   \[
   (U_\varepsilon f)_j=\nu_j f_j,
   \]
   is unitary from \(\ell^2(\mathbb N_0,m)\) to ordinary \(\ell^2(\mathbb N_0)\);

2. the conjugated operator \(H_\varepsilon=U_\varepsilon^{-1}J_\varepsilon U_\varepsilon\) is exactly the weighted nearest-neighbor Laplacian
   \[
   \boxed{
   (H_\varepsilon f)_j
   =\frac{c_j}{m_j}(f_j-f_{j+1})
   +\frac{c_{j-1}}{m_j}(f_j-f_{j-1}),
   }
   \tag{1}
   \]
   with the second term absent at \(j=0\);

3. its quadratic form is exactly
   \[
   \boxed{
   \langle f,H_\varepsilon f\rangle_{\ell^2(m)}
   =\sum_{j\ge0}c_j|f_{j+1}-f_j|^2;
   }
   \tag{2}
   \]

4. the PF-248 coefficient asymptotics and the exact PF-251 gamma-ratio formulas imply
   \[
   \boxed{
   m_j=C_\varepsilon^2j^3(1+O(j^{-1})),
   \qquad
   c_j=\frac{C_\varepsilon^2}{4}j^3(1+O(j^{-1})),
   }
   \tag{3}
   \]
   and, more sharply,
   \[
   \boxed{
   \frac{c_j}{m_j}
   =\frac14+\frac{3}{8j}+O(j^{-2}),
   \qquad
   \frac{c_{j-1}}{m_j}
   =\frac14-\frac{3}{8j}+O(j^{-2});
   }
   \tag{4}
   \]

5. for every \(F\in C_c^3((0,\infty))\), if \(f_j^{(N)}=F(j/N)\), then uniformly for \(j/N\) in compact subsets of \((0,\infty)\),
   \[
   \boxed{
   N^2(H_\varepsilon f^{(N)})_j
   \longrightarrow
   -\frac14\left(F''(x)+\frac3xF'(x)\right),
   \qquad x=\frac jN;
   }
   \tag{5}
   \]

6. the transformed chain has
   \[
   \boxed{
   \sum_{j\le N}m_j
   =\frac{C_\varepsilon^2}{4}N^4(1+O(N^{-1})),
   }
   \tag{6}
   \]
   while its tail resistance satisfies
   \[
   \boxed{
   \sum_{j\ge N}\frac1{c_j}
   =\frac{2}{C_\varepsilon^2}N^{-2}(1+O(N^{-1})).
   }
   \tag{7}
   \]

Equations (5)--(7) are the radial four-dimensional/Bessel scaling statement. They are an asymptotic classification of the exact transformed Jacobi chain, not a claim that the chain is literally the continuum Bessel operator.

## 1. PF-251's positive zero solution gives an exact ground-state transform

For \(u=\nu f\), the zero equation
\[
a_j\nu_{j+1}+b_j\nu_j+a_{j-1}\nu_{j-1}=0
\tag{8}
\]
gives
\[
\begin{aligned}
\nu_j^{-1}(J_\varepsilon(\nu f))_j
&=
-a_j\frac{\nu_{j+1}}{\nu_j}(f_j-f_{j+1})
-a_{j-1}\frac{\nu_{j-1}}{\nu_j}(f_j-f_{j-1})\\
&=
\frac{c_j}{m_j}(f_j-f_{j+1})
+\frac{c_{j-1}}{m_j}(f_j-f_{j-1}),
\end{aligned}
\]
which proves (1). The origin row is included because PF-251 proves that \(\nu\) satisfies the actual first Jacobi row, not merely the tail recurrence.

Multiplying (1) by \(m_j\overline{f_j}\), summing, and pairing each edge once gives (2). No asymptotic theorem or probabilistic interpretation is needed for this identity. It is the one-dimensional linear ground-state representation specialized to the exact PF-247 chain.

## 2. The transformed coefficients have cubic mass and conductance

PF-251's exact Gegenbauer-moment formulas are finite products and gamma ratios. Stirling expansion of those exact formulas gives, for either parity,
\[
\frac{\nu_{j+1}}{\nu_j}
=1+\frac{3}{2j}+O(j^{-2}),
\qquad
\frac{\nu_{j-1}}{\nu_j}
=1-\frac{3}{2j}+O(j^{-2}).
\tag{9}
\]
This is stronger than using only the compressed statement
\(\nu_j=C_\varepsilon j^{3/2}(1+O(j^{-1}))\): the exact gamma-ratio representation supplies the full smooth asymptotic expansion needed for the ratio.

PF-248 gives
\[
a_j=-\frac14+\frac{1}{64j^2}+O(j^{-3}).
\tag{10}
\]
There is no \(j^{-1}\) term. Combining (9) and (10) yields (3)--(4).

Two coarse invariants are immediate. Summing \(m_j\sim C_\varepsilon^2j^3\) gives the quartic volume law (6), while summing
\[
c_j^{-1}
=\frac{4}{C_\varepsilon^2}j^{-3}(1+O(j^{-1}))
\]
gives (7). In electrical-network language the transformed half-line has finite resistance to infinity, the expected transient side of a Bessel model of dimension greater than two. Only the explicit resistance asymptotic is used here.

## 3. Diffusive scaling is radial dimension four

Let \(x=j/N\) stay in a fixed compact subset of \((0,\infty)\). Taylor expansion gives
\[
f_{j\pm1}^{(N)}
=
F(x)\pm N^{-1}F'(x)
+\frac12N^{-2}F''(x)
+O(N^{-3}).
\tag{11}
\]
Insert (4) and (11) into (1). The symmetric part contributes
\[
-\frac{1}{4N^2}F''(x),
\]
while the first-order asymmetry contributes
\[
-\frac{3}{4jN}F'(x)
=
-\frac{3}{4N^2x}F'(x).
\]
This proves (5).

The operator
\[
-\partial_x^2-\frac3x\partial_x
\tag{12}
\]
is the radial nonnegative Laplacian on \(\mathbb R^4\), acting in the radial measure \(x^3dx\). Conjugating (12) by the radial ground-state weight \(x^{3/2}\) gives the inverse-square Schrödinger expression
\[
-\partial_x^2+\frac{3}{4x^2}.
\tag{13}
\]
After the common factor \(1/4\), (13) is exactly the continuum Bessel model suggested independently by PF-251's discrete indicial equation
\[
2u_j-u_{j+1}-u_{j-1}+\frac{3}{4j^2}u_j\sim0.
\]
Thus the exponent pair \(-1/2,3/2\), the cubic ground-state mass, and the four-dimensional radial drift are three equivalent views of the same threshold geometry.

## 4. The free calibration is Bessel dimension three, not four

For the constant Dirichlet chain \(J_0\) of PF-248--PF-250,
\[
(J_0u)_j=-\frac14u_{j-1}+\frac12u_j-\frac14u_{j+1},
\qquad u_{-1}=0,
\]
the positive boundary zero solution is exactly
\[
\nu_j^{(0)}=j+1.
\tag{14}
\]
Its ground-state transform therefore has
\[
m_j^{(0)}=(j+1)^2,
\qquad
c_j^{(0)}=\frac14(j+1)(j+2),
\]
and
\[
\frac{c_j^{(0)}}{m_j^{(0)}}
=\frac14+\frac{1}{4j}+O(j^{-2}),
\qquad
\frac{c_{j-1}^{(0)}}{m_j^{(0)}}
=\frac14-\frac{1}{4j}+O(j^{-2}).
\]
The corresponding scaling limit is
\[
-\frac14\left(\partial_x^2+\frac2x\partial_x\right),
\tag{15}
\]
the radial Laplacian in three dimensions.

This comparison matters for the PF-243 smoothing route. PF-250's half-line image cancellation was derived in the free Bessel-three calibration. PF-251/PF-252 show that the actual inverse-square Jacobi tail changes the zero-edge ground-state geometry to Bessel four. Hence the first-moment-critical perturbation is not merely an uncontrolled mechanism that can only worsen the free endpoint. Its exact zero mode points toward a higher-dimensional threshold model, which in the continuous Bessel theory has stronger low-energy suppression.

That observation is **not** a transfer theorem for fractional powers. The next step must prove the relevant discrete low-energy heat/resolvent kernel or weighted functional calculus for the actual coefficients rather than infer it from dimension counting.

## 5. Consequence for the accepted critical-Jacobi clue

PF-251 ruled out importing PF-250 through generic trace-class perturbation theory. PF-252 supplies a replacement structure: after an exact positive ground-state transform, the variable chain is a cubic-volume/cubic-conductance birth-death operator with a four-dimensional radial scaling limit.

This changes the best next test. Instead of asking only whether the free Dirichlet image cancellation survives an arbitrary \(O(j^{-2})\) perturbation, one should exploit the exact transformed coefficients and ask whether Bessel-four heat-kernel/resolvent estimates persist with enough uniformity to control the actual spectral factor. A continuum dimensional calibration predicts *better*, not worse, fixed-row endpoint decay than the free Bessel-three model; however that prediction remains below the evidence threshold until proved for this discrete chain.

A decisive local theorem would establish one of the following directly for \(J_\varepsilon\):

- a low-energy spectral-density/Green-kernel asymptotic with the Bessel-four exponent;
- two-sided heat-kernel bounds for \(H_\varepsilon\) at the cubic-volume scale, strong enough to subordinate to \(J_\varepsilon^\sigma\);
- or the weighted separated estimate needed by PF-243 without first identifying the full spectral density.

Any of those would turn the exact zero-edge geometry into the \(R>1\) mode-locality statement the Robin-Poisson route needs.

## 6. Prior-art and novelty audit

Ground-state/Doob transforms of positive discrete Schrödinger operators and weighted-graph energies are standard. A modern general reference is Florian Fischer, *A non-local quasi-linear ground state representation and criticality theory*, Calculus of Variations and Partial Differential Equations 62 (2023), article 163, DOI `10.1007/s00526-023-02496-5`, arXiv:2204.05391. Equation (2) is derived directly here in the linear nearest-neighbor case; no general theorem is needed to establish it.

Continuous half-line inverse-square operators and their Bessel spectral behavior are also classical. Hynek Kovařík and Françoise Truc, *Schrödinger Operators on a Half-Line with Inverse Square Potentials*, Mathematical Modelling of Natural Phenomena 9 (2014), 170--176, DOI `10.1051/mmnp/20149511`, arXiv:1403.3624, study the low-energy spectral density of these operators and show enhanced threshold vanishing for positive inverse-square coupling. Jan Dereziński and Serge Richard, *On Schrödinger Operators with Inverse Square Potentials on the Half-Line*, Annales Henri Poincaré 18 (2017), 869--928, DOI `10.1007/s00023-016-0520-7`, give explicit Bessel/Hankel diagonalizations for the homogeneous continuum family.

PF-251 already records representative prior art for discrete inverse-square Jacobi/Schrödinger tails through Damanik--Teschl. A targeted audit did not locate the particular PF-238 compactification/PF-247 parity chain or the cubic ground-state transform above.

No novelty is claimed for ground-state representations, Doob transforms, electrical resistance, radial Laplacians, Bessel operators, or inverse-square spectral theory. The project-specific result is the exact identification of the PF-247 zero-edge chain, using PF-251's boundary-selected solution, with a weighted discrete model whose mass/conductance asymptotics and diffusive scaling are those of radial dimension four.

## 7. Falsification and boundary checks

1. **Sign.** PF-247's exact upper off-diagonal formula has \(d_n^+<0\), and all normalization factors are positive, so \(a_j<0\) and \(c_j>0\).
2. **Boundary row.** Equation (2) has no extra origin term only because PF-251 proves that \(\nu\) solves the actual first row. A tail-only subordinate solution cannot be substituted.
3. **Ratio expansion.** Expanding PF-251's exact gamma ratios must give (9). A surviving \(j^{-1}\) term in \(a_j+1/4\) would alter (4), but PF-248 proves that term cancels exactly.
4. **Dimension check.** The drift coefficient in (5) is \(3/x\), while the free Dirichlet transform gives \(2/x\). Confusing the two would erase the inverse-square threshold deformation PF-251 established.
5. **No spectral-density theorem yet.** Bessel-four scaling does not by itself prove that the discrete spectral measure is asymptotic to a constant times \(\lambda\,d\lambda\), nor does it prove any fractional-power row exponent. Those are the next tests.
6. **No Robin estimate yet.** The actual normalized Robin factor, \(T_a\), hypercycle reparameterization, Hardy ends, physical \(P/H\) recoupling, finite-pant completion, neighboring-module extension, global weak-\(S_1\) reassembly, and every RH-level bridge remain open.
7. **No arithmetic conclusion.** The result concerns the fixed-axis operator forced by the prime-flute geometry. It does not establish a new relation between prime gaps and zeta zeros by itself.
