# PF-333 — positivity alone does not remove logarithmic relative square-root sensitivity

**Status:** `LITERATURE+DERIVED + GRADED-POLAR-IDENTIFICATION + LOGARITHMIC-GENERIC-OBSTRUCTION + ROUTE-NARROWING`.

PF-332 reduces the remaining completed-packet locality question to the relative square-root defect

\[
G=(A_0^{1/2}-Q^{1/2})Q^{-1/2},
\qquad
A_0=Q+\Lambda_{LL},
\qquad
Q>0,
\quad \Lambda_{LL}\ge0.
\]

There are two useful facts about this object that sharpen the endpoint gate.

First, `G` is exactly a **scaled positive-polar-factor perturbation** of the type studied in classical graded-matrix perturbation theory. Put

\[
K:=Q^{-1/2}\Lambda_{LL}Q^{-1/2}\ge0,
\qquad
P:=I+K,
\qquad
S:=Q^{1/2},
\]

and define

\[
B:=P^{1/2}S.
\]

Then

\[
B^*B=SPS=A_0,
\]

so the positive polar factor of `B` is

\[
H=(B^*B)^{1/2}=A_0^{1/2}.
\]

For the unperturbed graded matrix `B_0=S`, the positive polar factor is `H_0=S`. Therefore

\[
\boxed{
G=(H-H_0)S^{-1}.
}
\tag{1}
\]

Ren-Cang Li's 2005 graded positive-polar perturbation paper studies precisely scaled differences of the form `(\widetilde H-H)S^{-1}` and explicitly extends that framework to square roots of graded positive-definite matrices. Thus the generic matrix-analysis shape of PF-332 is classical prior art; the Prime-Flute difficulty is not the invention of a new relative square-root variable.

Second, **positivity of the pant insertion is not, by itself, enough to make the relative square-root map uniformly Lipschitz in operator norm as the retained dimension grows**. Roy Mathias proved that the sharp first-order constant for the normalized matrix square root under arbitrary Hermitian relative perturbations grows like `log r` in dimension `r`. A short cone-decomposition argument shows that the same logarithmic order is already unavoidable when the normalized perturbation is restricted to be positive semidefinite.

Consequently a proof of the PF-332 locality gate cannot come from a dimension-free theorem using only

\[
Q>0,
\qquad
\Lambda_{LL}\ge0,
\qquad
K=Q^{-1/2}\Lambda_{LL}Q^{-1/2},
\]

and the size of `K`. It must exploit additional structure of the **actual pant/core DtN insertion**: its translation defect, spatial locality/quasilocality, resolvent propagation, physical band geometry, or another property absent from unrestricted positive matrix perturbations.

This is a route-narrowing result, not a negative theorem about the Prime-Flute operator family. The positive-semidefinite matrices witnessing generic logarithmic sensitivity need not be realizable as the one-cusp-pant/core DtN blocks occurring here.

## 1. Exact identification with the graded positive-polar variable

On one finite physical-low section, introduce the one-parameter positive insertion

\[
A_\eta:=Q+\eta\Lambda_{LL}
=Q^{1/2}(I+\eta K)Q^{1/2},
\qquad \eta\ge0,
\tag{2}
\]

and the relative defect

\[
G_\eta:=A_\eta^{1/2}Q^{-1/2}-I.
\tag{3}
\]

Let

\[
P_\eta=I+\eta K,
\qquad
B_\eta=P_\eta^{1/2}S,
\qquad S=Q^{1/2}.
\tag{4}
\]

The positive polar factor of `B_\eta` is

\[
H_\eta=(B_\eta^*B_\eta)^{1/2}
=(SP_\eta S)^{1/2}
=A_\eta^{1/2}.
\tag{5}
\]

Since `H_0=S`, equations (3)--(5) give the exact identity

\[
\boxed{
G_\eta=(H_\eta-H_0)S^{-1}.
}
\tag{6}
\]

This is the same scaling used in Li's graded positive-polar framework. The identification is exact and does not use an asymptotic expansion, commutativity, or a condition-number bound on `Q`.

It does **not** imply that Li's quantitative hypotheses are automatically uniform in the Prime-Flute degeneration. In the representation `B_\eta=P_\eta^{1/2}S`, the grading `S` may vary wildly, while the relevant control of the prefactor `P_\eta^{1/2}` depends on the actual normalized pant insertion. Equation (6) identifies the correct classical perturbation class; it does not close PF-332.

## 2. The logarithmic generic obstruction persists on the positive cone

For an `r x r` positive-definite matrix `Q`, define the first relative square-root derivative

\[
\mathcal D_Q(E)
:=
\left.\frac{d}{d\eta}\right|_{\eta=0}
\left(Q+\eta Q^{1/2}EQ^{1/2}\right)^{1/2}Q^{-1/2}.
\tag{7}
\]

The map `E \mapsto \mathcal D_Q(E)` is linear. Mathias's 1997 result says that the least worst-case first-order constant

\[
c_r^{\rm all}
:=
\sup_{Q>0}
\sup_{\substack{E=E^*\\ \|E\|\le1}}
\|\mathcal D_Q(E)\|
\tag{8}
\]

grows like `log r`.

Now restrict the perturbation to the positive cone:

\[
c_r^+
:=
\sup_{Q>0}
\sup_{\substack{0\le E\le I}}
\|\mathcal D_Q(E)\|.
\tag{9}
\]

For every Hermitian contraction `E`, write its spectral positive/negative decomposition

\[
E=E_+-E_-,
\qquad
0\le E_\pm\le I.
\tag{10}
\]

Linearity gives

\[
\|\mathcal D_Q(E)\|
\le
\|\mathcal D_Q(E_+)\|
+
\|\mathcal D_Q(E_-)\|
\le 2c_r^+.
\tag{11}
\]

Taking the two suprema in (8) yields

\[
\boxed{
c_r^{\rm all}\le2c_r^+.}
\tag{12}
\]

The reverse inequality `c_r^+\le c_r^{\rm all}` is immediate. Hence Mathias's asymptotic implies

\[
\boxed{
c_r^+\asymp\log r.}
\tag{13}
\]

Thus the generic logarithmic relative-square-root sensitivity cannot be blamed solely on sign-indefinite perturbations. Even the abstract class

\[
Q>0,
\qquad
\Lambda\ge0,
\qquad
\|Q^{-1/2}\Lambda Q^{-1/2}\|\le1
\tag{14}
\]

has no dimension-independent first-order operator-norm Lipschitz constant.

Equivalently, there cannot be a universal constant `C`, independent of `r`, such that every positive pair in (14) satisfies

\[
\|(Q+\eta\Lambda)^{1/2}Q^{-1/2}-I\|
\le C\eta+o(\eta)
\tag{15}
\]

uniformly over the class as `\eta\downarrow0`.

## 3. Consequence for the completed packet locality gate

PF-332 already shows that the translation defect has the much more structured form

\[
[F,\tau_t]
=\frac1\pi\int_0^\infty
\mu^{1/2}(A_0+\mu)^{-1}
[\Lambda_{LL},\tau_t]
(A_0+\mu)^{-1}Q^{-1/2}
\,d\mu,
\tag{16}
\]

because the seam block `Q` commutes with the physical translations. PF-333 explains why that structure is not optional bookkeeping. A generic estimate that forgets the commutator source and remembers only positivity plus relative form size is allowed a logarithmically worsening operator-norm constant as the finite-section dimension grows.

Therefore the live obstruction branch should preserve the **pant insertion and its physical localization** all the way through the estimate. Useful targets include uniform bounds on the resolvent-dressed commutator in (16), off-diagonal versions of PF-332's relative defect formula, or a Prime-Flute-specific theorem showing that the admissible DtN insertions occupy a much smaller class than the positive matrices responsible for (13).

Conversely, failure to prove a dimension-free bound from `K\ge0` alone is not evidence of delocalization of the actual completed packets. The generic obstruction says only that positivity and relative size are insufficient hypotheses.

## Prior-art and novelty audit

The two load-bearing literature anchors are:

- **Roy Mathias**, *A Bound for the Matrix Square Root with Application to Eigenvector Perturbation*, SIAM Journal on Matrix Analysis and Applications 18(4) (1997), 861--867, DOI `10.1137/S5089547989529577`. Its abstract states the `c_r\asymp\log r` first-order relative-square-root sensitivity used in (8).
- **Ren-Cang Li**, *Relative Perturbation Bounds for Positive Polar Factors of Graded Matrices*, SIAM Journal on Matrix Analysis and Applications 27(2) (2005), 424--433, DOI `10.1137/S0895479803437153`. Its abstract explicitly introduces bounds for the scaled positive-polar difference `(\widetilde H-H)S^{-1}` and says the results extend to square roots of graded positive-definite matrices.

Mathias's logarithmic first-order bound is classical matrix perturbation theory. Li's scaled positive-polar framework is also classical and already targets graded matrices whose scaling can vary strongly. No new general theorem about matrix square roots or polar decompositions is claimed here.

The project-specific content is the exact identification (6) of PF-332's completed relative defect with Li's scaled positive-polar variable, together with the positive-cone consequence (12)--(13) applied to the live Prime-Flute proof strategy. The latter is an elementary deduction from Mathias's all-Hermitian lower bound, not a claim that Mathias constructed Prime-Flute DtN examples.

The quantitative theorems inside Li's paper have not been imported as a proof dependency here. Before using a specific Li bound to close the endpoint, its exact conditioning hypotheses and constants must be audited against the degenerating `P_\eta^{1/2}S` family.

## Boundaries and adversarial checks

1. **No Prime-Flute counterexample is constructed.** The positive matrices forcing (13) need not arise from a hyperbolic one-cusp pant/core DtN operator.
2. **The result is first-order and generic.** It rules out a uniform proof based only on positivity and relative perturbation size; it does not determine the nonlinear size of the actual `G` at `\eta=1`.
3. **No locality estimate is proved or disproved.** Translation/cutoff commutators may be much better behaved than unrestricted operator-norm perturbations because `Q`, `\Lambda_{LL}`, and the physical translations have geometric structure.
4. **Li's framework is identified, not invoked as a black-box endpoint theorem.** Its exact quantitative hypotheses remain to be checked before any stronger consequence is claimed.
5. **No completed-angle endpoint is closed.** PF-318's Hilbert--Schmidt budget and PF-328's positive-measure packet obstruction remain open.
6. **No scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication is established.**

## Consequence for the research line

The generic matrix route has now been separated from the genuinely geometric one. PF-332's relative defect is already a classical graded positive-polar perturbation variable, and positivity alone cannot provide a dimension-free operator-norm bound even infinitesimally. The next useful theorem must exploit structure specific to the pant/core DtN insertion—most directly the resolvent-dressed translation/cutoff defects isolated by PF-332—or prove that those structured defects genuinely remain large on almost all PF-328 critical packets.