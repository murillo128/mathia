# PC-451 — Cotangent-tower boundedness is exactly orbit A2

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + CLASSICAL-STRUCTURE + CONTROL-BLIND. For every probability equivalent to Haar on the singleton-base complete cotangent tower, either unchanged cylinder action is bounded exactly when the density satisfies the classical uniform orbit `A_2` condition. The two actions are therefore bounded simultaneously; reciprocal integrability follows automatically. In this entire bounded class both spectra are `[-1,1]`. This closes PC-450's nonmaximal-boundedness boundary by a finite-cylinder necessity proof and an established ergodic Hilbert-transform sufficiency theorem. It is not a new prime discriminator or an RH implication.

## 1. Object and classification

Take the complete power-map preimages of `P_2^*={-1}`, with coherent lift coordinate
\[
X=\widehat{\mathbb Z},\qquad \mu=\text{Haar probability},\qquad Sx=x+1.
\]
Let `nu=w mu`, where `0<w<infinity` almost everywhere and `integral w dmu=1`, and put `H_w=L^2(nu)`. Retain the exact cylinder matrices
\[
(B_m)_{ts}=\begin{cases}
\dfrac{i}{m}\cot\dfrac{\pi(t-s)}m,&t\ne s,\\
0,&t=s,
\end{cases}
\qquad B_m^+=B_m+J_m/m,
\tag{1}
\]
where `J_m` is the all-ones matrix. Their compatibility under refinement is the tower prescription used in [[research/prime_circle/findings/PC-449-equivalent-power-weights-give-cotangent-towers-empty-resolvent]] and [[research/prime_circle/findings/PC-450-bounded-weighted-cotangent-towers-retain-the-haar-band]]. For `q=j/m in [0,1)`, define `chi_q(x)=exp(2 pi i j(x mod m)/m)`. On these rational characters,
\[
B\chi_q=b(q)\chi_q,\qquad
b(0)=0,\quad b(q)=1-2q\ (0<q<1),\qquad
B^+\chi_q=(1-2q)\chi_q.
\tag{2}
\]
The cylinder algebra is dense in `H_w`.

Define the orbit weight characteristic
\[
[w]_{A_2(S)}=
\operatorname*{ess\,sup}_{x\in X}\ \sup_{n\ge1}
\left(\frac1n\sum_{j=0}^{n-1}w(x+j)\right)
\left(\frac1n\sum_{j=0}^{n-1}\frac1{w(x+j)}\right).
\tag{3}
\]
The essential supremum is with respect to `mu`. After removing countably many translates of an exceptional null set, the same bound holds for all finite integer intervals along each remaining orbit.

**Theorem.** The following are equivalent:

1. The unchanged unaugmented cylinder action `B` extends boundedly to `H_w`.
2. The unchanged augmented cylinder action `B^+` extends boundedly to `H_w`.
3. `K=[w]_{A_2(S)}<infinity`.

If either bounded operator has norm `L`, a nonsharp necessity bound is
\[
K\le (6\pi)^4 L^4.
\tag{4}
\]
Whenever these conditions hold,
\[
\int_X w^{-1}\,d\mu\le K,
\qquad
\sigma(B_w)=\sigma(B_w^+)=[-1,1].
\tag{5}
\]
No essential upper or lower bound on the density is assumed. Boundedness concerns the full cylinder algebra, not a restriction to mean-zero functions or a changed half-density-conjugated action.

## 2. Necessity from two finite blocks

Let `mathcal F_m` be the partition into residue cylinders modulo `m`, and write
\[
w_m(t)=m\int_{x\equiv t\pmod m}w(x)\,d\mu(x).
\tag{6}
\]
Each `w_m(t)` is positive and finite. The weighted norm of a level-`m` cylinder is exactly
\[
\|f\|_{H_w}^2=\frac1m\sum_{t=0}^{m-1}|f(t)|^2w_m(t).
\tag{7}
\]
Thus a bound `L` for either full action bounds every corresponding finite matrix in (7), uniformly in `m`.

Fix `n>=1`, `m>=12n` and any starting residue `a`. Use the disjoint cyclic blocks
\[
I=\{a,\ldots,a+n-1\},\qquad
J=\{a+2n,\ldots,a+3n-1\}\pmod m.
\]
For `s in I,t in J`, choose their indicated integer lifts. Then
`n+1<=t-s<=3n-1` and `0<pi(t-s)/m<=pi/4`. Since
`sin theta<=theta` and `cos theta>=1/2` on this range,
\[
\frac1m\cot\frac{\pi(t-s)}m
\ge\frac1{2\pi(t-s)}\ge\frac{\kappa}{n},
\qquad \kappa=\frac1{6\pi}.
\tag{8}
\]
The cotangent is periodic under changes of residue lifts. Consequently the sign and bound survive when the blocks cross residue zero. In the reverse direction the kernel has the opposite, still constant, imaginary sign.

For a residue set `E`, put
\[
W_E=\sum_{t\in E}w_m(t),\qquad
V_E=\sum_{t\in E}w_m(t)^{-1}.
\]
Test the finite action on the real nonnegative vector `f=1_I/w_m`. On `J`, (8) gives
\[
|(B_m f)(t)|\ge\frac{\kappa}{n}V_I.
\tag{9}
\]
The same lower bound holds for `|B_m^+ f|`: its added component is real, while `B_m f` is purely imaginary, so augmentation cannot cancel it. Weighted boundedness, with the common factor `1/m` canceled from both sides, now gives
\[
\frac{\kappa^2}{n^2}W_J V_I^2
\le L^2 V_I,
\qquad
W_JV_I\le L^2n^2/\kappa^2.
\tag{10}
\]
Interchanging the blocks gives `W_I V_J<=L^2 n^2/kappa^2`. Multiply the two bounds and use `W_JV_J>=n^2` by Cauchy--Schwarz to obtain
\[
\boxed{\frac{W_I V_I}{n^2}\le L^4/\kappa^4.}
\tag{11}
\]
This argument does not assume boundedness of maximal truncations, translations, Haar averaging, or `w^{-1}` integrability.

To pass to the actual density, take the cofinal increasing partitions `m=k!`. The functions `w_{k!}` are precisely `E_mu(w|mathcal F_{k!})`. The martingale convergence theorem gives `w_{k!}->w` almost everywhere, because these partitions generate the Borel sigma-algebra of `X`. Remove also all integer translates of the exceptional null set. For each remaining `x`, every finite list `w_{k!}(x+j)` converges to its positive finite limit `w(x+j)`, and so do their reciprocals. Apply (11) to `a=x mod k!`, with `k!>=12n`, and pass to the limit. This proves (3)--(4) for every `n`, and establishes necessity for either raw action.

It is essential here that the reciprocal in (11) is `1/E(w|mathcal F_m)`. No unproved interchange with `E(1/w|mathcal F_m)` is being made.

## 3. Reciprocal integrability and sufficiency

The transformation `S` is invertible and Haar preserving. It is ergodic: its action on `chi_q` is multiplication by `exp(2 pi i q)`, whose value is one only for the constant character. Haar probability on `X` is nonatomic.

Assume `K<infinity`. For every positive integer `R`, the function
`v_R=min(w^{-1},R)` is integrable. The defining orbit inequality implies
\[
\left(\frac1n\sum_{j=0}^{n-1}w(S^jx)\right)
\left(\frac1n\sum_{j=0}^{n-1}v_R(S^jx)\right)\le K.
\tag{12}
\]
By the ergodic theorem the two factors converge almost everywhere to
`integral w=1` and `integral v_R`. Taking the countable intersection over `R`, then using monotone convergence, proves the first part of (5). In particular Haar averaging
\[
Af=\left(\int_X f\,d\mu\right)\mathbf1
\tag{13}
\]
is bounded on `H_w`, by Cauchy--Schwarz, with norm at most `sqrt K`.

For the unaugmented action use the maximal weighted ergodic Hilbert-transform theorem of Atencia--Martín-Reyes, Theorem 1.2. Its assumptions are an invertible ergodic measure-preserving transformation on a nonatomic probability space, a positive integrable density, and exactly the orbit condition (3). All have been checked. It bounds in `H_w` the maximal absolute value of the symmetrically truncated sums
\[
\sum_{s<|j|<t}\frac{f(S^jx)}j,
\qquad s,t\in\mathbb Z_{\ge0}.
\tag{14}
\]
The theorem is for a maximal operator; we use only its sufficient direction, after deriving necessity for the nonmaximal cylinder action independently.

The Bernoulli sawtooth series gives, for `0<q<1`,
\[
\lim_{N\to\infty}\sum_{0<|j|\le N}\frac{e^{2\pi i jq}}j
=\pi i(1-2q),
\tag{15}
\]
while for `q=0` every symmetric sum is zero. Hence on every cylinder function
\[
Bf=\frac1{\pi i}\lim_{N\to\infty}
\sum_{0<|j|\le N}\frac{f(S^jx)}j.
\tag{16}
\]
The maximal estimate and Fatou's lemma bound this limit uniformly in `H_w`; density then gives the bounded extension of `B`. Finally `B^+=B+A` on cylinders, and (13) gives the bounded augmented extension. This proves all three equivalences, including equivalence of the two raw actions without an extra reciprocal-integrability assumption.

PC-450 proves that every bounded augmented realization has spectrum exactly `[-1,1]`, by character-modulation interval projections and an explicit bounded inverse outside the band. Its unaugmented conclusion requires `integral w^{-1}<infinity`, now supplied by (12). Applying those exact results gives the spectral statement (5); it does not follow merely from density of the character eigenvalues.

## 4. Consequences, controls and prior art

PC-449 and PC-450's contrasting examples are now separated by a necessary and sufficient condition, rather than by density size. For example, (3) at `n=2` implies
\[
\frac{w(x)}{w(x+1)}+\frac{w(x+1)}{w(x)}+2\le4K
\quad\text{almost everywhere}.
\tag{17}
\]
The PC-449 density `w_alpha(x)=c_alpha p^{alpha v_p(x_p)}` violates this already on the positive-measure cylinders where `v_p(x_p)` is large and `v_p(x_p+1)=0`. Its unbounded raw action is consistent with its independently proved empty-resolvent phenomenon. PC-450's iterated-maximal densities satisfy orbit `A_1`, hence (3), despite their unbounded size. Neither boundedness nor the common spectral band forces Haar measure or a Riesz character basis.

For an arbitrary singleton base `exp(2 pi i theta)`, the lifted angles are `(theta+t)/m`. Every angle difference in (1) is still `(t-s)/m`. In particular an irrational-angle singleton yields precisely the same criterion, proof and spectral band. The classification does not recover prime birth, select a critical line, or supply arithmetic coercivity.

**Prior-art boundary.** The general mechanism is classical weighted singular-integral theory. E. Atencia and F. J. Martín-Reyes, *The maximal ergodic Hilbert transform with weights*, Pacific J. Math. **108** (1983), 257--263, [Theorem 1.2 and the separated-block necessity argument on pp. 258--260](https://msp.org/pjm/1983/108-2/pjm-v108-n2-p01-s.pdf), provide the direct literature bridge. Their theorem concerns maximal truncations. Section 2 here specializes the classical two-block test to the exact finite cotangent matrices and uses conditional expectations to derive necessity from boundedness of the full nonmaximal action alone. No novelty is claimed for the testing method, orbit weight class, ergodic theorem or martingale convergence.

The source's historical reference is Hunt--Muckenhoupt--Wheeden, *Weighted norm inequalities for the conjugate function and Hilbert transform*, Trans. Amer. Math. Soc. **176** (1973), 227--251. The proof here needs no additional theorem from that reference. The normalization in (15) is the `n=0` specialization of [DLMF 24.8.2](https://dlmf.nist.gov/24.8.E2), with the constant-character endpoint treated separately.

The line-local delta is the complete boundedness classification for arbitrary equivalent singleton-tower densities, closing the explicit necessity question in PC-450 and removing its separate reciprocal-integrability assumption when comparing the two actions. This is a classicalization of that entire bounded measure-only branch, not a new spectral mechanism.

## 5. Validation and limits

The analytic proof checks the kernel sign on separated cyclic blocks, the real/imaginary separation for augmentation, positivity of every finite marginal, a uniform bound before the factorial-partition limit, and the source theorem's full hypotheses. The reciprocal-integrability proof truncates `1/w` before applying ergodicity, so it does not assume its conclusion.

Standard-library Python checks evaluated (8) in **30,040** cases with `12<=m<=240`, `1<=n<=floor(m/12)` and `n+1<=d<=3n-1`; the smallest ratio to the asserted lower bound was greater than `1.61`. A further **186,840** two-block tests used `12<=m<=72`, every starting residue, both propagation directions, both raw actions, and five explicitly chosen profiles: Haar; `exp(2 cos(2 pi t/m))`; a spike `w(0)=m^0.6` with other weights one; its dip counterpart `w(0)=m^-0.6`; and `exp((((37t+11) mod 101)-50)/10)`. They verified the lower weighted output norm in (10), including wrap-around and augmentation; the smallest ratio of squared norms to that lower bound exceeded `3.27`. These are floating-point finite diagnostics, not proof of the infinite theorem or numerical estimates of an infinite operator norm.

This result does not classify singular measures, unbounded closed realizations, multi-point base towers, growing-base regimes or changed kernels. Failure of (3) rules out boundedness of the specified raw action; it does not imply nonclosability or empty resolvent. Equation (4) is deliberately nonsharp. A bounded raw realization with infinite orbit characteristic, or an orbit-`A_2` equivalent probability with an unbounded raw action, would falsify the classification. A bounded example with nonintegrable reciprocal would falsify (12)'s consequence. No computation, formal proof or RH claim beyond the stated evidence boundary is asserted.
