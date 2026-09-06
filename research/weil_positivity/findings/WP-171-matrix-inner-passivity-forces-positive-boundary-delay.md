# WP-171 — Regular matrix-inner passivity forces a PSD boundary-delay matrix, so it cannot carry the signed Gamma phase velocity

**Status:** `EXACT-DERIVED + MATRIX-SCHUR-NO-GO + DE-BRANGES-ROVNYAK-KERNEL + POSITIVE-BOUNDARY-DELAY + ARCHIMEDEAN-GAMMA + DECISIVE-NARROWING + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION`.

`WP-169` identifies the exact real-place phase retained by the pointed critical shell before positive scalarization,

\[
R_\infty(\tau)
=\pi^{i\tau}
\frac{\Gamma(\tfrac14-\tfrac{i\tau}{2})}
     {\Gamma(\tfrac14+\tfrac{i\tau}{2})},
\qquad |R_\infty(\tau)|=1,
\tag{1}
\]

with logarithmic phase velocity

\[
i\frac{d}{d\tau}\log R_\infty(\tau)
=A_\infty(\tau)
:=\operatorname{Re}\psi\!\left(\frac14+\frac{i\tau}{2}\right)-\log\pi.
\tag{2}
\]

`WP-170` proves that the scalar phase itself is not a Schur/inner passive response: its upper-half-plane zeros violate the Blaschke condition, and its boundary phase velocity changes sign. That finding deliberately leaves open a genuinely matrix/operator-valued passive response with a new coercivity theorem.

The most direct matrix escape is also impossible. Let

\[
S:\mathbb C_+\longrightarrow M_d(\mathbb C)
\tag{3}
\]

be an analytic matrix Schur function, `||S(z)||<=1`, and suppose that on a real interval `I` it has regular lossless boundary values,

\[
S(t)^*S(t)=I,
\qquad t\in I,
\tag{4}
\]

with enough boundary regularity to differentiate. Then the associated boundary-delay matrix

\[
\boxed{
Q_S(t):=-iS(t)^*S'(t)
}
\tag{5}
\]

is Hermitian positive semidefinite at every such boundary point:

\[
\boxed{Q_S(t)\succeq0.}
\tag{6}
\]

This is not a physical heuristic. It follows directly from the positive de Branges--Rovnyak/Pick kernel of the matrix Schur class. Consequently every positive scalar readout of the delay matrix -- a channel state, positive matrix weight, or trace -- is nonnegative. The exact Weil Gamma symbol `A_infty`, however, is negative near the origin and positive for sufficiently large `|tau|`. Therefore

\[
\boxed{
A_\infty(t)\neq \omega_t(Q_S(t))
}
\tag{7}
\]

for any family of positive linear functionals `omega_t` on `M_d(C)` throughout the real line. Reversing the causal orientation only reverses the semidefinite sign and fails on the opposite side of the unique zero of `A_infty`.

Thus **finite channel mixing does not rescue ordinary passive positivity**. To recover the signed Gamma contribution from a matrix boundary object one must use a signed/indefinite scalarization, leave the Schur-inner/passive category, or couple the finite and archimedean sectors before the response is reduced to a positive boundary-delay observable. No global Weil positivity or RH statement is obtained here.

## 1. The matrix Schur kernel forces a positive delay matrix

For a matrix Schur function on the upper half-plane, the Pick/de Branges--Rovnyak kernel

\[
\boxed{
K_S(z,w)
:=
\frac{I-S(z)S(w)^*}{-i(z-\overline w)}
}
\tag{8}
\]

is positive definite. In particular, for `z=t+iy`, `y>0`,

\[
K_S(t+iy,t+iy)
=
\frac{I-S(t+iy)S(t+iy)^*}{2y}
\succeq0.
\tag{9}
\]

At a regular unitary boundary point write `S=S(t)` and `S'=S'(t)`. Holomorphy gives

\[
S(t+iy)=S+i yS'+O(y^2).
\tag{10}
\]

Differentiating `SS^*=I` tangentially gives

\[
S'S^*+SS'^*=0.
\tag{11}
\]

Hence

\[
\begin{aligned}
S(t+iy)S(t+iy)^*
&=I+i y(S'S^*-SS'^*)+O(y^2)\\
&=I+2iyS'S^*+O(y^2),
\end{aligned}
\tag{12}
\]

so the boundary limit of (9) is

\[
\boxed{
\lim_{y\downarrow0}K_S(t+iy,t+iy)
=-iS'S^*
=S\,Q_S(t)\,S^*
\succeq0.
}
\tag{13}
\]

Unitary conjugation preserves the positive cone, proving (6). This is the matrix form of the scalar fact used in `WP-170`: an inner boundary phase has nonnegative angular velocity in the Schur orientation.

The theorem is local in the spectral parameter. It does not require `S` to be rational or finite-state; finite matrix size and a regular unitary boundary point suffice. Rational lossless passive systems are a particularly transparent subclass.

## 2. The exact Gamma phase velocity has the forbidden sign pattern

From `WP-170`,

\[
A_\infty(0)
=\psi\!\left(\frac14\right)-\log\pi
=-\gamma-\frac\pi2-3\log2-\log\pi<0,
\tag{14}
\]

while for `tau>0`

\[
A_\infty'(\tau)
=
\sum_{m=0}^{\infty}
\frac{(m+\tfrac14)(\tau/2)}
     {\bigl((m+\tfrac14)^2+(\tau/2)^2\bigr)^2}
>0
\tag{15}
\]

and

\[
A_\infty(\tau)
=
\log\frac{\tau}{2\pi}+O(\tau^{-2})
\longrightarrow +\infty.
\tag{16}
\]

Therefore `A_infty` has a unique positive zero `tau_0` (`tau_0≈6.2898359888`) and

\[
A_\infty(\tau)<0\quad(0\le\tau<\tau_0),
\qquad
A_\infty(\tau)>0\quad(\tau>\tau_0).
\tag{17}
\]

Let `omega_t` be any positive linear functional on matrices. From (6),

\[
\omega_t(Q_S(t))\ge0.
\tag{18}
\]

Thus (7) already fails on `(0,tau_0)`. If the opposite half-plane/scattering convention is chosen, the same derivation gives the negative semidefinite orientation, which fails for `tau>tau_0`. The sign change cannot be repaired by choosing an orientation once and for all.

This rules out more than the scalar characteristic-function interpretation of `WP-170`. A matrix response cannot hide the negative part in channel mixing and then recover the exact Gamma term by a **positive** channel measurement. Positive compression preserves the cone.

## 3. Determinant and total time delay collapse back to scalar inner theory

There is a second exact check on the natural gauge-invariant scalarization. For finite `d`,

\[
D(z):=\det S(z)
\tag{19}
\]

is a scalar Schur function because all singular values of `S(z)` are at most one, so `|D(z)|<=1`. On the lossless boundary, `|D(t)|=1`; hence `D` is scalar inner.

At a regular unitary boundary point,

\[
\frac{D'(t)}{D(t)}
=\operatorname{Tr}(S(t)^{-1}S'(t))
=\operatorname{Tr}(S(t)^*S'(t))
=i\operatorname{Tr}Q_S(t).
\tag{20}
\]

Writing `D(t)=e^{i\theta(t)}` gives

\[
\boxed{
\theta'(t)=\operatorname{Tr}Q_S(t)\ge0.
}
\tag{21}
\]

Therefore neither the determinant phase nor the total Wigner--Smith/characteristic delay can reproduce `A_infty`, whose sign changes. Likewise one cannot arrange

\[
\det S(t)=c\,R_\infty(t)^{\pm1}
\tag{22}
\]

with `|c|=1`: the left side is scalar inner, whereas `WP-170` proves that neither orientation of the exact `R_infty` is an admissible scalar inner response.

This also closes the obvious strategy of adding finitely many passive auxiliary channels and hoping that the unwanted scalar non-inner behavior disappears in a determinant. A finite-dimensional matrix lift does not change the analytic class of its determinant.

## 4. Blaschke--Potapov controls make the sign mechanism explicit

The scalar control is a single upper-half-plane Blaschke factor with zero `a=x+iy`, `y>0`,

\[
b_a(z)=\frac{z-a}{z-\overline a}.
\tag{23}
\]

On the real line its delay is

\[
-i\overline{b_a(t)}b_a'(t)
=
\frac{2y}{(t-x)^2+y^2}>0.
\tag{24}
\]

A rank-`r` Blaschke--Potapov factor

\[
B_{a,P}(z)=I+(b_a(z)-1)P,
\tag{25}
\]

with an orthogonal projection `P`, has

\[
Q_{B_{a,P}}(t)
=
\frac{2y}{(t-x)^2+y^2}P
\succeq0.
\tag{26}
\]

For a product `S=S_1S_2`, direct differentiation gives

\[
\boxed{
Q_S
=S_2^*Q_{S_1}S_2+Q_{S_2}.
}
\tag{27}
\]

Thus every finite Blaschke--Potapov cascade builds the boundary delay by adding unitary conjugates of PSD channel contributions. Matrix mixing changes directions but not the cone. This is the finite rational matched control behind the general kernel proof (13).

A pure passive delay `e^{iat}I`, `a>=0`, merely adds `aI` to `Q_S`. It can shift a scalar delay upward but cannot reproduce the **exact** signed symbol without subsequently subtracting a constant. At the level of the exact phase, `WP-170` gives the stronger zero-set statement: multiplying by an ordinary delay or finite passive factor cannot cure the non-Blaschke Gamma zero sequence.

## 5. Aggressive falsification and exact boundary of the no-go

**A signed matrix readout can change sign, but then positivity has not been inherited.** If one evaluates `Q_S` with an indefinite matrix weight or a difference/supertrace of channels, the result may certainly have both signs. That is outside (18). Any useful construction of this kind must derive the grading or indefinite scalarization intrinsically and then prove that the **assembled** global form is positive. Merely choosing the signs to fit `A_infty` would reproduce the failure mode excluded by the branch mandate. Burnol's nonarchimedean supertrace mechanism is the obvious classical warning.

**A `J`-inner or generalized-Schur system can evade the PSD kernel, but it changes category.** Potapov/Krein--Langer theory allows indefinite metrics and kernels with negative squares. Such a response is not an ordinary Hilbert-passive positivity theorem. If this is the correct Mathia route, the missing work is precisely to show how a source-forced indefinite finite--archimedean object acquires a final positive quotient/compression without importing Weil positivity.

**Nonseparable finite--archimedean coupling remains open.** The argument treats `A_infty` as a scalar readout of an archimedean Schur-inner boundary delay. It does not exclude a larger object in which finite-prime data and the real-place phase interact before the positive cone is formed, so that neither sector separately equals the final scalar response.

**Domain-changing or singular operator realizations remain open.** The proof assumes a regular unitary boundary point of an ordinary matrix Schur function. Infinite-dimensional operator-valued responses with singular boundary domains, unbounded boundary operators, or no trace/determinant require separate analysis. At every regular Schur-inner boundary point the same Pick-kernel argument still points toward a positive operator delay, but no unrestricted infinite-dimensional theorem is claimed here.

**The positive Gamma Markov symbol is a different object.** `WP-117` shows that the normalized digamma variation has an independent positive jump-Dirichlet realization, while `WP-115` and the later Gamma sequence obstruct its direct critical finite-prime gluing. The present result concerns the raw phase `R_infty` and its signed logarithmic velocity from `WP-169`; it does not contradict that separate Markov positivity.

These controls make the surviving escape precise: the matrix/operator category can help only if Mathia uses **more than ordinary Schur passivity plus a positive scalar channel readout**.

## 6. Prior-art and novelty audit

No theorem-level novelty is claimed for matrix Schur kernels, inner matrix functions, Blaschke--Potapov factorization, or passive realizations. The classical source is V. P. Potapov, *The multiplicative structure of J-contractive matrix functions*, Trudy Moskov. Mat. Obshch. 4 (1955), 125--236; English translation, American Mathematical Society Translations, Series 2, vol. 15 (1960), 131--243, DOI `10.1090/trans2/015/07`. A modern systematic reference for upper-half-plane `J`-contractive/`J`-inner matrix functions and passive systems is Damir Z. Arov and Harry Dym, *J-Contractive Matrix Valued Functions and Related Topics*, Cambridge University Press (2008), DOI `10.1017/CBO9780511721427`, especially the chapters on `J`-contractive/`J`-inner functions and operator nodes/passive systems.

The positivity of (8) is the defining Pick/de Branges--Rovnyak structure of the Schur class, and (13) is its elementary regular-boundary limit. In the rational inner subclass, Potapov factorization reduces the same statement to (26)--(27). Hence the matrix positivity mechanism is classical.

The Mathia-specific result is the **application of that classical matrix positivity theorem to the exact source-derived real-place phase and Weil digamma symbol isolated by `WP-169`/`WP-170`**. `WP-170` left matrix/operator response as a live escape from scalar inner failure. Equations (6)--(21) now remove the ordinary finite-channel version of that escape whenever the Weil scalar is supposed to arise as a positive channel delay, a positive compression, or the total/determinant phase.

A bounded literature audit across matrix Schur/inner, Potapov factorization, passive-system, and operator-valued inner-function sources found the general machinery above, as expected. No historical novelty is claimed for it; the substantive delta is the branch-specific exclusion it produces.

## 7. Consequence for the Weil-positivity search

The live frontier asked whether passing from the scalar phase of `WP-170` to a matrix/operator boundary response could preserve a genuine passive positivity theorem while recovering the signed archimedean Weil term. For the regular finite-channel Schur-inner class, the answer is now no:

\[
\boxed{
\text{matrix Schur-inner passivity}
\Longrightarrow
Q_S(t)\succeq0
\Longrightarrow
\text{every positive scalar delay readout has one sign},
}
\tag{28}
\]

whereas

\[
\boxed{A_\infty(t)\text{ changes sign}.}
\tag{29}
\]

The remaining matrix/operator direction must therefore be genuinely structural rather than dimensional. It must introduce a source-forced grading/indefinite intermediate form with a later independent positivity theorem, a nonseparable finite--archimedean coupling before scalarization, or a singular/domain-changing operator geometry not described by regular Schur-inner boundary delay. Simply adding passive channels, mixing them unitarily, taking a positive compression, or taking a determinant/trace does not evade the scalar obstruction.