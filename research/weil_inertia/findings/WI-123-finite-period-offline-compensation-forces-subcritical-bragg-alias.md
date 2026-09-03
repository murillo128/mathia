# WI-123 — finite-period off-line compensation forces a strictly subcritical Bragg alias

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. WI-122 gives a density-one period-five motif in which ordinary critical zeros cancel the moving support-edge horizontal signal without any ordinate overcrowding. The exact argument below proves a complementary rigidity statement: **no finite-period density-one motif containing any off-critical horizontal displacement can cancel all of its reciprocal-lattice harmonics below the support-one edge.** Functional-equation balance plus the Newton--Girard identities force at least one nonzero structure factor at a fixed frequency `alpha=m/P<1`. For the specific WI-122 motif the first harmonic `alpha=1/5` is already nonzero.

This does not improve Mathia's current simple-critical proportion. It does, however, resolve the sharp finite-period falsifier left by WI-122 into the proposed second branch: exact compensated screening at mean ordinate density can evade every count statistic, but if it is genuinely periodic and contains off-line mass then it necessarily creates a fixed **strictly subcritical** pair/spectral alias. What remains open is extraction from an embedded positive-density family of such blocks in the actual zeta zero set, because the complete form-factor square can still contain destructive interference from zeros outside a selected block.

## 1. General density-one periodic cell

Use the unfolded ordinate coordinate

\[
x=\gamma\frac{L}{2\pi},\qquad L=\log T,
\]

and the normalized horizontal coordinate

\[
b=(\beta-\tfrac12)L.
\]

Fix an integer period `P>=2`. A density-one cell contains exactly `P` zero labels, counted with multiplicity, at data

\[
(a_j,b_j),\qquad 1\le j\le P,
\]

with `a_j` understood modulo `P`. Assume the labels respect the horizontal functional-equation balance inside the cell: off-line labels occur in mirror pairs `+b,-b`, while critical-line labels have `b=0`. Hence

\[
\boxed{\sum_{j=1}^P b_j=0.}
\tag{1}
\]

For the unweighted Montgomery exponential sum of one cell define

\[
C(\alpha)
:=\sum_{j=1}^P
\exp\!\left(b_j\alpha+2\pi i a_j\alpha\right).
\tag{2}
\]

At reciprocal-lattice frequencies `alpha=m/P`, put

\[
z_j:=\exp\!\left(\frac{b_j+2\pi i a_j}{P}\right).
\tag{3}
\]

Then

\[
\boxed{C(m/P)=p_m:=\sum_{j=1}^P z_j^m.}
\tag{4}
\]

Moreover (1) gives

\[
\boxed{\left|\prod_{j=1}^P z_j\right|
=\exp\!\left(\frac1P\sum_j b_j\right)=1.}
\tag{5}
\]

Thus the horizontal zeta symmetry becomes an exact product constraint on the reciprocal-cell variables.

## 2. Newton rigidity: vanishing all subcritical harmonics forces every zero onto the line

Assume, toward contradiction, that every strictly subcritical reciprocal harmonic vanishes:

\[
p_1=p_2=\cdots=p_{P-1}=0.
\tag{6}
\]

Let `e_k` be the elementary symmetric functions of `z_1,...,z_P`. Newton--Girard gives for `1<=k<=P-1`

\[
k e_k
=\sum_{m=1}^k(-1)^{m-1}e_{k-m}p_m.
\tag{7}
\]

Equation (6) therefore implies recursively

\[
e_1=e_2=\cdots=e_{P-1}=0.
\tag{8}
\]

Consequently the monic polynomial with roots `z_j` has only its leading and constant terms:

\[
\prod_{j=1}^P(z-z_j)
=z^P+(-1)^P e_P.
\tag{9}
\]

Every root hence has the same modulus

\[
|z_j|=|e_P|^{1/P}.
\tag{10}
\]

But by (5), `|e_P|=|prod z_j|=1`, so (10) gives

\[
|z_j|=1\qquad(1\le j\le P).
\tag{11}
\]

From (3), `|z_j|=e^{b_j/P}`. Hence

\[
\boxed{b_1=\cdots=b_P=0.}
\tag{12}
\]

We have proved the contrapositive:

\[
\boxed{
\text{if some }b_j\ne0,
\text{ then }C(m/P)\ne0
\text{ for at least one }1\le m\le P-1.
}
\tag{13}
\]

The location of the forced alias is therefore **strictly inside** the unconditional Montgomery support range; the endpoint `alpha=1` is not needed. This strengthening uses the functional-equation balance (1). Without (1), (6) would only force all `|z_j|` to be equal, not equal to one.

This is also the exact equality classification. A density-one `P`-periodic cell can annihilate all reciprocal harmonics `m/P`, `1<=m<P`, only if every label lies on the critical line and the complex numbers `z_j` form, up to a common rotation, the complete set of `P`-th roots of a unimodular constant. In particular, horizontal off-line displacement is incompatible with complete subcritical extinction.

## 3. Repeating the cell turns the forced alias into quadratic local spectral mass

Repeat the same cell over `N` periods, at unfolded translations `Pn`, `0<=n<N`. At `alpha=m/P`, the translation phase is exactly one:

\[
e^{2\pi i(Pn)m/P}=1.
\]

Therefore the complete unweighted exponential amplitude of the `PN` labels is

\[
A_N(m/P)=N C(m/P),
\tag{14}
\]

and the corresponding all-pairs form is

\[
\boxed{|A_N(m/P)|^2=N^2|C(m/P)|^2.}
\tag{15}
\]

Whenever the cell contains off-line mass, (13) supplies at least one fixed `m<P` for which the right side is a positive constant times `N^2`. This is the standard Bragg amplification of a periodic unit-cell structure factor, but here the Newton argument shows that zeta's horizontal mirror balance prevents all **subcritical** Bragg lines from being systematically extinguished.

The exact Montgomery weight

\[
w(u)=\frac4{4-u^2}
\tag{16}
\]

does not remove this local signal on a slowly growing periodic block. Keep `P` and the cell data fixed, let

\[
M:=PN\to\infty,\qquad M=o(L).
\tag{17}
\]

All differences inside the block satisfy `|rho-rho'|=O(M/L)`, while the horizontal exponential factors at the fixed `alpha=m/P` remain bounded by constants depending only on the cell. Hence

\[
w(\rho-\rho')=1+O(M^2/L^2),
\]

and summing over `O(M^2)` ordered pairs changes the block form by

\[
O(M^4/L^2)=o(M^2)=o(N^2).
\tag{18}
\]

Thus the weighted block still has a coherent `Theta(N^2)` reciprocal-harmonic signal.

## 4. The WI-122 five-cell motif is detected already at alpha=1/5

For WI-122, `P=5`, the mirror pair is at `a=0` with

\[
y=\operatorname{arcosh}2,
\]

and the three simple critical zeros are at `a=1/2,3/2,5/2`. Its cell amplitude is

\[
C(\alpha)
=2\cosh(y\alpha)
+e^{\pi i\alpha}
+e^{3\pi i\alpha}
+e^{5\pi i\alpha}.
\tag{19}
\]

At the first reciprocal harmonic,

\[
\operatorname{Im}C(1/5)
=\sin(\pi/5)+\sin(3\pi/5)
=\sin(\pi/5)+\sin(2\pi/5)>0.
\tag{20}
\]

Therefore

\[
\boxed{C(1/5)\ne0.}
\tag{21}
\]

No numerical approximation is involved. The same motif that exactly cancels the moving-edge mirror-minus-double structure factor at `alpha=1` in WI-122 necessarily emits a coherent Bragg line at the fixed, safely subcritical frequency `alpha=1/5`.

This is precisely the second branch that WI-122 asked a successful two-observable argument to identify: the compensating ordinary-zero phase reservoir leaves a fixed-frequency spectral footprint even though the ordinate counting measure has bounded discrepancy.

## 5. Relation to the unconditional zeta form factor

Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh prove unconditionally that

\[
F_T(\alpha)
=T^{-2\alpha}(\log T+O(1))
+\alpha+O((\log T)^{-1/2})
\tag{22}
\]

uniformly for `0<=alpha<=1`, with the complete complex-zero sum and exact weight (16). Thus at every fixed `alpha in (0,1]` the normalized complete zeta form factor is `O(1)`. In particular the arithmetic theorem already evaluates every rational frequency `m/P` forced by (13); no wider Fourier support, higher correlation, RH, or new prime theorem is required merely to **see** the alias.

This immediately rules out the WI-122 motif, or any other fixed finite-period off-line density-one motif, as a **standalone global model** for the zeta zero set: a repeated periodic cell has coherent reciprocal-lattice mass while the actual complete form factor stays bounded after normalization.

There is, however, an important extraction boundary. Equations (15)--(18) concern a selected periodic block. The BGSTB theorem controls the complete zero sum. Their Lemma 3 represents that complete quantity as an integral of a squared modulus, but a large selected-block amplitude can in principle be canceled by the complementary zero amplitude before the square is taken. Therefore (22) does **not** by itself imply that a positive density of embedded finite periodic blocks is impossible. Proving that requires a localization/coercivity statement controlling this external cancellation reservoir.

The durable conclusion is narrower and exact:

\[
\boxed{
\text{finite-period mean-density compensation}
+\text{off-line mass}
\Longrightarrow
\text{a nonzero fixed subcritical reciprocal alias}.
}
\tag{23}
\]

Thus the count-only obstruction of WI-122 is not spectrally featureless. Any stronger adversarial countermodel must either destroy finite periodic coherence (for example by growing periods/aperiodicity), or arrange external cancellation of the forced subcritical aliases as well as the moving-edge alias.

## 6. Prior-art audit and evidence boundary

The arithmetic input is the published unconditional form-factor theorem of Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh, *Acta Arithmetica* 214 (2024), 357--376, arXiv:2306.04799. Their Theorem 1 gives the uniform range through `alpha=1`; their Lemma 3 gives the positive squared-modulus representation of the complete form factor. These are already canonical sources for this research line.

The algebraic input (7) is the classical Newton--Girard identity. Periodic diffraction and reciprocal-lattice Bragg peaks are also classical; for nearby general weighted-lattice prior art see Michael Baake, **Diffraction of weighted lattice subsets**, arXiv:math/0106111 (2001), and the later weighted-Dirac-comb literature. No novelty is claimed for Newton identities, structure factors, systematic extinctions, or Bragg diffraction.

A targeted audit also checked Lagarias--Rodgers' bandlimited Alternative-Hypothesis construction. It does not contradict (13): their fixed-correlation mimicry is not a finite density-one cell carrying nonzero horizontal radii `|z_j|!=1` and required to extinguish every reciprocal harmonic below one. The line-specific deduction here is the combination of zeta functional-equation balance with Newton power sums, which turns any off-line finite-period compensation into a strictly subcritical alias.

No claim of priority is made for that combination. The finding does **not** prove that actual off-line zeros occur periodically, that all count-regular compensation is periodic, that a selected block contribution is lower-bounded by the complete form factor, or that a larger simple-critical proportion follows. The remaining load-bearing problem is exactly the external-cancellation/localization step.

## 7. Research implication

WI-121 killed dense long *overcrowded* screening islands; WI-122 then showed that bounded-discrepancy finite-period compensation evades every ordinate-count statistic and can cancel the moving edge. The present finding supplies the missing deterministic second observable for the whole finite-period class: if the compensated cell has any off-line mass, it cannot simultaneously erase all fixed subcritical reciprocal harmonics.

The next useful test is therefore no longer to search for another finite periodic unit cell. It is to ask whether a positive density of long compensated blocks whose local subcritical aliases are forced by (13) can have those aliases canceled by the rest of the actual zero set while the complete BGSTB form factor remains `O(N(T))`. A coercive localization theorem would combine WI-121's count branch with (23)'s spectral branch and would be a genuine defect-to-zero bootstrap. Conversely, an aperiodic or growing-period model that keeps counts regular, screens the WI-120 edge, and also neutralizes every fixed subcritical alias would materially close this route.