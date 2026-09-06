# WP-178 — Hilbert–Carleman `det_2` leaves the Schur modulus but preserves passive boundary-phase monotonicity

**Status:** `LITERATURE+DERIVED + HILBERT-CARLEMAN-NO-GO + LOSSLESS-PASSIVE-BOUNDARY + PHASE-MONOTONICITY + GAMMA-OBSTRUCTION + DECISIVE-NARROWING + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-177` identifies the first determinant category in which ordinary scalar Schur boundedness genuinely fails: for a Hilbert--Schmidt defect one may form the second modified Fredholm (Hilbert--Carleman) determinant `det_2`, and even a one-dimensional unitary contraction can have `|det_2|>1`. That observation leaves open the natural hope that regularization might retain Hilbert-space passivity while supplying the missing archimedean Gamma phase.

For the **regular lossless Hilbert--Schmidt boundary category**, that hope still fails. If an operator-valued Schur response has a unitary boundary path `U(t)` with `U(t)-I` Hilbert--Schmidt and the path is differentiable in Hilbert--Schmidt norm, then the raw `det_2 U(t)` has modulus

\[
\boxed{
|\det_2 U(t)|
=\exp\!\left(\frac12\|U(t)-I\|_2^2\right),
}
\tag{1}
\]

so it is unimodular only at the trivial response `U=I`. More importantly, after discarding that positive modulus and keeping only the regularized determinant phase, passivity still forces

\[
\boxed{
\frac{d}{dt}\arg\det_2 U(t)
=\operatorname{Tr}\!\left((I-\operatorname{Re}U(t))Q_U(t)\right)
=\frac12\|(I-U(t))Q_U(t)^{1/2}\|_2^2
\ge0,
}
\tag{2}
\]

where

\[
Q_U(t):=-iU(t)^*U'(t)\succeq0
\tag{3}
\]

is the passive boundary-delay operator. Thus `det_2` escapes the **Schur modulus** but not the **one-sided phase orientation** of a regular conservative passive system.

The exact real-place phase isolated in `WP-169`--`WP-170` has the opposite global behavior: if

\[
R_\infty(t)=e^{i\phi_\infty(t)},
\]

then `phi_infty'(t)>0` near the origin and `phi_infty'(t)<0` for all sufficiently large positive `t`. Hence neither the passive orientation in (2) nor its reversed orientation can reproduce the whole Gamma phase. The raw `det_2` already fails by modulus; its canonical boundary phase fails by monotonicity.

This is not a no-go for arbitrary regularized determinants. It closes the most direct `det_2` escape only when the operator response remains an ordinary regular lossless Hilbert-space passive system. A genuinely analytic counterterm, a dissipative/non-lossless operator lift whose regularized scalar happens to be unimodular, higher modified determinants, zeta/heat regularization, singular ideal/domain limits, indefinite geometry, or nonseparable finite--archimedean assembly remain outside the claim and must supply their own coercivity/sign theorem.

## 1. Exact modulus of `det_2` on the Hilbert--Schmidt unitary group

Let `H` be a Hilbert space and let

\[
U\in\mathcal B(H),
\qquad U^*U=UU^*=I,
\qquad U-I\in\mathcal S_2(H).
\tag{4}
\]

Because `U-I` is compact and normal, the nontrivial spectrum of `U` consists of eigenvalues

\[
e^{i\theta_j},
\tag{5}
\]

counted with multiplicity and accumulating, if at all, only at `1`. The Hilbert--Schmidt condition is exactly

\[
\sum_j|e^{i\theta_j}-1|^2<\infty.
\tag{6}
\]

For `K=U-I`, the standard Hilbert--Carleman product formula gives

\[
\det_2(I+K)
=\prod_j(1+\lambda_j(K))e^{-\lambda_j(K)}.
\tag{7}
\]

Using `lambda_j(K)=e^{i theta_j}-1`, this becomes

\[
\det_2 U
=\prod_j e^{i\theta_j}\exp\!\left(1-e^{i\theta_j}\right).
\tag{8}
\]

Taking absolute values,

\[
\begin{aligned}
\log|\det_2 U|
&=\sum_j(1-\cos\theta_j)\\
&=\frac12\sum_j|e^{i\theta_j}-1|^2\\
&=\frac12\|U-I\|_2^2.
\end{aligned}
\tag{9}
\]

This proves (1). In particular,

\[
\boxed{
|\det_2 U|=1
\iff U=I.
}
\tag{10}
\]

The one-dimensional calculation in `WP-177`, `|det_2(e^{i theta})|=exp(1-cos theta)`, is therefore not an accident. It is the exact infinite-dimensional unitary Hilbert--Schmidt law.

Since the Gamma scattering factor satisfies `|R_infty(t)|=1` for every real `t`, a nontrivial lossless response can never satisfy

\[
\det_2 U(t)=R_\infty(t)
\tag{11}
\]

even pointwise on an interval. A boundary normalization can remove the excess positive modulus, but then the phase itself becomes the decisive datum.

## 2. Ordinary Schur passivity still makes the operator boundary delay positive

Let

\[
S:\mathbb C_+\to\mathcal B(H)
\tag{12}
\]

be holomorphic and contractive,

\[
\|S(z)\|\le1.
\tag{13}
\]

Suppose `t` is a regular lossless boundary point with

\[
U(t):=S(t),
\qquad U(t)^*U(t)=I,
\tag{14}
\]

and enough norm regularity for the boundary derivative `U'(t)` to exist. The operator-valued de Branges--Rovnyak/Pick kernel

\[
K_S(z,w)
=\frac{I-S(z)S(w)^*}{-i(z-\overline w)}
\tag{15}
\]

is positive. Taking `z=t+iy` and using the boundary expansion

\[
S(t+iy)=U(t)+iyU'(t)+o(y),
\tag{16}
\]

together with the tangential derivative of `UU^*=I`, gives

\[
\lim_{y\downarrow0}K_S(t+iy,t+iy)
=-iU'(t)U(t)^*\succeq0.
\tag{17}
\]

After unitary conjugation,

\[
\boxed{
Q_U(t):=-iU(t)^*U'(t)\succeq0.
}
\tag{18}
\]

This is the infinite-dimensional regular-boundary version of the matrix calculation in `WP-171`. No determinant has been used: (18) is inherited directly from Hilbert-space Schur passivity.

## 3. The `det_2` anomaly weights the positive delay but does not reverse it

Now assume on an interval `I` that

\[
U(t)-I\in\mathcal S_2(H)
\tag{19}
\]

and that `t -> U(t)-I` is `C^1` in Hilbert--Schmidt norm. Since `U(t)` is unitary, `det_2 U(t)` never vanishes. The standard derivative identity for the modified determinant is

\[
\frac{d}{dt}\log\det_2 U(t)
=\operatorname{Tr}\!\left(U(t)^{-1}U'(t)-U'(t)\right).
\tag{20}
\]

The trace is legitimate because `(U^*-I)` and `U'` are Hilbert--Schmidt, hence their product is trace class. Using

\[
U^{-1}=U^*,
\qquad
U'=iUQ_U,
\tag{21}
\]

we obtain

\[
\frac{d}{dt}\log\det_2 U
=\operatorname{Tr}((U^*-I)U')
=i\operatorname{Tr}((I-U)Q_U).
\tag{22}
\]

Let `vartheta_2(t)` be any local continuous branch of `arg det_2 U(t)`. Taking the imaginary part of (22),

\[
\begin{aligned}
\vartheta_2'(t)
&=\operatorname{Re}\operatorname{Tr}((I-U)Q_U)\\
&=\operatorname{Tr}((I-\operatorname{Re}U)Q_U).
\end{aligned}
\tag{23}
\]

For a unitary operator,

\[
I-\operatorname{Re}U
=\frac12(I-U)^*(I-U)
\succeq0.
\tag{24}
\]

Moreover `(I-U)^*(I-U)` is trace class by (19). Since `Q_U` is bounded and positive,

\[
\begin{aligned}
\vartheta_2'(t)
&=\frac12\operatorname{Tr}\!\left((I-U)^*(I-U)Q_U\right)\\
&=\frac12\operatorname{Tr}\!\left(Q_U^{1/2}(I-U)^*(I-U)Q_U^{1/2}\right)\\
&=\frac12\|(I-U)Q_U^{1/2}\|_2^2\\
&\ge0.
\end{aligned}
\tag{25}
\]

This proves (2). The regularization anomaly has not destroyed the passive orientation; it has inserted the positive weight `I-Re U` in front of the ordinary delay.

Equality in (25) can occur for nontrivial `U` only when the active delay lies in the `1`-eigenspace of `U` in the precise sense `(I-U)Q_U^{1/2}=0`. It cannot generate negative phase velocity.

## 4. Exact conflict with the Riemann Gamma phase

The phase isolated in `WP-169` is

\[
R_\infty(t)
=\pi^{it}
\frac{\Gamma(\tfrac14-\tfrac{it}{2})}
     {\Gamma(\tfrac14+\tfrac{it}{2})}
=e^{i\phi_\infty(t)}.
\tag{26}
\]

`WP-170` gives

\[
\phi_\infty'(t)
=\log\pi-
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
=-A_\infty(t),
\tag{27}
\]

where `A_infty` is strictly increasing on the positive axis, negative at the origin, and positive for all sufficiently large `t`. Its unique positive zero is

\[
t_0\approx6.2898359888.
\tag{28}
\]

Consequently

\[
\phi_\infty'(t)>0
\quad(0<t<t_0),
\qquad
\phi_\infty'(t)<0
\quad(t>t_0).
\tag{29}
\]

Equation (25) therefore excludes

\[
\arg\det_2 U(t)
=\phi_\infty(t)+\text{constant}
\tag{30}
\]

on the whole positive axis for any regular lossless Hilbert--Schmidt boundary response in the upper-half-plane passive orientation. Reversing the causal/scattering orientation reverses the one-sided inequality and then fails on `(0,t_0)` instead. There is no fixed passive orientation that produces both signs.

Combining (10) and (29) yields the sharper two-stage conclusion:

\[
\boxed{
\begin{array}{l}
\text{raw lossless }\det_2:\quad |\det_2 U|>1\text{ unless }U=I,\\[2mm]
\text{phase-normalized lossless }\det_2:\quad
\dfrac{d}{dt}\arg\det_2 U\ge0.
\end{array}
}
\tag{31}
\]

Thus neither the raw Hilbert--Carleman determinant nor the scalar phase left after stripping its positive boundary modulus can be the exact global Gamma scattering factor.

## 5. Matched controls and aggressive falsification

**Scalar Blaschke control.** Let `b_a` be an ordinary upper-half-plane Blaschke factor. On the real line its passive phase velocity is

\[
q_a(t)=-i\overline{b_a(t)}b_a'(t)>0.
\tag{32}
\]

In one dimension,

\[
\det_2 b_a=b_a\exp(1-b_a).
\tag{33}
\]

Equations (1) and (25) reduce exactly to

\[
|\det_2 b_a|=\exp(1-\operatorname{Re}b_a),
\qquad
\frac{d}{dt}\arg\det_2 b_a
=(1-\operatorname{Re}b_a)q_a(t)\ge0.
\tag{34}
\]

So the theorem reproduces the elementary scalar control and is not an artifact of noncommutative trace manipulations.

**Fixed unitary references do not help.** If `V` is a fixed unitary and `T(t)=U(t)V^*` satisfies `T-I in S_2`, then right multiplication by `V^*` preserves Schur contractivity and losslessness. Its delay is a unitary conjugate of `Q_U`, so the same argument applies to `det_2 T`. A parameter-dependent reference `V(t)` can inject an arbitrary extra phase and is therefore new mechanism, not an innocent change of origin.

**Removing the positive modulus does not help.** The boundary scalar

\[
\frac{\det_2 U(t)}{|\det_2 U(t)|}
\tag{35}
\]

is unimodular but has exactly the same phase derivative (25). This normalization is only a boundary operation and need not be analytic, but even granting it for free does not recover the Gamma sign pattern.

**An analytic outer/counterterm normalization remains open.** Multiplying `det_2 U(z)` by a nontrivial analytic scalar chosen to repair its modulus can also alter its boundary phase. That operation is no longer controlled by (25) as a pure `det_2` readout. Under the branch mandate it must be generated intrinsically by the Mathia geometry, not selected to fit `R_infty`, and its contribution must come with an independent positive/coercive theorem.

**Dissipative boundary lifts remain open.** The proof uses a unitary operator boundary response because it audits the conservative/lossless route suggested by an exact scattering phase. A contractive but nonunitary operator can have regularized determinant modulus one through cancellation between dissipative and phase contributions. This finding does not classify such lifts. If they are used, the reason their scalarization becomes the exact lossless Gamma phase is additional structure and must itself be derived.

**Higher modified determinants are not covered.** For `det_p`, `p>=3`, the regularizing polynomial contains higher powers of `U-I`; the analogue of (25) is not asserted to have a fixed sign. Zeta/heat determinants, non-Schatten determinant notions, and dimension-dependent counterterms remain separate categories.

**Singular/domain-changing and indefinite geometries remain open.** The argument assumes a regular bounded unitary boundary value, a bounded passive delay, and `C^1` Hilbert--Schmidt variation. Unbounded boundary operators, singular relations, changing domains, infinite negative index, or a final positive quotient formed only after finite--archimedean coupling require new analysis.

**Nonseparable finite--archimedean assembly remains open.** As in `WP-170`--`WP-177`, the no-go applies when the real-place phase is scalarized from an archimedean passive response before the final global positivity theorem. It does not exclude a larger Mathia object in which finite-prime incidence and the real-place sector interact first and the signed Gamma observable appears only after an independently positive global construction.

## 6. Prior-art and novelty audit

The operator-determinant facts used here are classical. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), especially Chapter 9, is a standard reference for modified Fredholm determinants on Schatten ideals, including the `det_2` product and differentiation formulas. Israel Gohberg, Seymour Goldberg, and Nahum Krupnik, *Traces and Determinants of Linear Operators*, Operator Theory: Advances and Applications 116, Birkhäuser (2000), DOI `10.1007/978-3-0348-8401-3`, gives the same trace-ideal and regularized-determinant framework.

The positivity of the de Branges--Rovnyak/Pick kernel and the resulting nonnegative boundary delay for regular lossless Schur responses are also classical; `WP-171` already records the finite-channel Potapov/de Branges--Rovnyak prior-art boundary. No novelty is claimed for any of those theorems, for the Hilbert--Carleman determinant itself, or for the algebraic identities (7), (20), and (24).

The Mathia-specific content is their exact combination with the source-derived Gamma phase of `WP-169`--`WP-170`. `WP-177` showed only that `det_2` leaves the scalar Schur ball and therefore constitutes a real regularization boundary. The present calculation shows that, in the canonical conservative Hilbert-passive regime, that category change is still too weak:

\[
\boxed{
\text{lossless Schur passivity}
+\text{Hilbert--Schmidt }\det_2
\Longrightarrow
\text{nondecreasing regularized phase}
\neq
\text{global Gamma phase}.
}
\tag{36}
\]

This is a decisive narrowing and prior-art classicalization, not a proof of Weil positivity and not a new theorem in determinant theory.

## 7. Research consequence

The determinant frontier is now narrower than `WP-177` alone suggested. Passing from the ordinary Fredholm determinant to the Hilbert--Carleman `det_2` genuinely escapes scalar Schur **modulus**, but a regular conservative passive realization still carries a hidden positive theorem: its regularized boundary phase is the integral of the nonnegative density (25). The exact Gamma phase needs both orientations on the positive frequency axis and therefore cannot arise this way.

A determinant-based continuation must consequently exploit something beyond the standard lossless `det_2` anomaly: a source-forced analytic counterterm, a genuinely dissipative lift whose regularized scalar becomes lossless for structural reasons, a higher/singular determinant category, or nonseparable finite--archimedean assembly before scalarization. In every case the burden identified by the branch mandate remains unchanged: the extra mechanism must be intrinsic, must produce the finite-prime and archimedean/global terms rather than fit them afterward, and must come with its own independent coercivity/positivity theorem.