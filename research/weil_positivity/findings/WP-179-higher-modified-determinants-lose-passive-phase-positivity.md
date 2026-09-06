# WP-179 — `det_2` is the last modified determinant whose lossless passive phase inherits a universal sign

**Status:** `EXACT-DERIVED + SCHATTEN-DETERMINANT-CLASSIFICATION + PASSIVE-PHASE-SIGN-BOUNDARY + MATCHED-INNER-CONTROLS + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION`.

`WP-178` closes the Hilbert--Carleman escape at order two. For a regular lossless Hilbert--Schmidt boundary path `U(t)` with passive delay

\[
Q_U(t):=-iU(t)^*U'(t)\succeq0,
\tag{1}
\]

it proves

\[
\frac{d}{dt}\arg\det_2 U(t)
=
\operatorname{Tr}\bigl((I-\operatorname{Re}U(t))Q_U(t)\bigr)
\ge0.
\tag{2}
\]

The finding explicitly leaves higher modified Fredholm determinants `det_m`, `m>=3`, open. That boundary can be classified exactly.

Let `m>=1` be an integer and let `U(t)` be a `C^1` unitary path with `U(t)-I in S_m` and `U'(t) in S_m`. Assume the same upper-half-plane passive orientation as `WP-171`--`WP-178`, so (1) holds. Then, on every continuous logarithmic branch of the nonvanishing modified determinant,

\[
\boxed{
\frac{d}{dt}\arg\det_m U(t)
=
\operatorname{Tr}\bigl(H_m(U(t))Q_U(t)\bigr),
}
\tag{3}
\]

where

\[
\boxed{
H_m(U)
:=
\operatorname{Re}\!\left[(-1)^{m-1}(U-I)^{m-1}\right].
}
\tag{4}
\]

For the ordinary determinant, `m=1`, `H_1=I`. For `m=2`,

\[
H_2(U)=I-\operatorname{Re}U
=\frac12(U-I)^*(U-I)\succeq0,
\tag{5}
\]

recovering `WP-178`. But for **every** `m>=3`, the scalar symbol of `H_m` changes sign on the unit circle. If `z=e^{i\theta}` and `0<\theta<2\pi`,

\[
\boxed{
h_m(\theta)
:=
\operatorname{Re}\!\left[(-1)^{m-1}(e^{i\theta}-1)^{m-1}\right]
=
\bigl(2\sin(\theta/2)\bigr)^{m-1}
\cos\!\left(\frac{(m-1)(\theta-\pi)}2\right).
}
\tag{6}
\]

Hence `H_m` is not universally positive or negative once `m>=3`. This failure already occurs on the elementary scalar inner/passive pure delay

\[
U_a(z)=e^{iaz},\qquad a>0,
\tag{7}
\]

for which `Q=a>0` on the real boundary, yet

\[
\frac{d}{dt}\arg\det_m U_a(t)
=a\,h_m(at)
\tag{8}
\]

changes sign for every `m>=3`.

Therefore

\[
\boxed{
\det\text{ and }\det_2
\text{ are exactly the modified determinant orders whose lossless boundary-phase sign is forced by }Q\succeq0.
}
\tag{9}
\]

This does **not** prove that a higher modified determinant cannot reproduce the Gamma phase. It proves the more relevant point for the branch mandate: if `det_m`, `m>=3`, produces the required signed archimedean phase, that sign is no longer inherited from passive geometric positivity. The regularization polynomial itself can manufacture both signs on an arithmetic-free one-channel control. A useful higher-determinant construction therefore needs a new independent spectral/coercive theorem; matching the Gamma sign pattern is not by itself a positivity mechanism.

## 1. Exact modified-determinant derivative

For `K in S_m`, the standard `m`th modified Fredholm determinant is

\[
\det_m(I+K)
=
\det\!\left(
(I+K)
\exp\!\left[
\sum_{j=1}^{m-1}\frac{(-1)^j}{j}K^j
\right]
\right).
\tag{10}
\]

The standard logarithmic derivative identity along a `C^1` invertible path is

\[
\boxed{
\frac{d}{dt}\log\det_m(I+K(t))
=
(-1)^{m-1}
\operatorname{Tr}\!\left(
K^{m-1}(I+K)^{-1}K'
\right).
}
\tag{11}
\]

There is a small trace-ideal subtlety worth making explicit. In finite rank, Jacobi's formula plus cyclicity differentiates the determinant and the regularizing polynomial; the resulting operator bracket

\[
(I+K)^{-1}-I+K-\cdots+(-1)^{m-1}K^{m-2}
\tag{12}
\]

collapses algebraically to

\[
(-1)^{m-1}K^{m-1}(I+K)^{-1}
\tag{13}
\]

**before** taking the final trace. In the general Schatten setting the lower-order summands in (12) need not be separately trace class, so they are not assigned separate traces. Equation (11) is obtained by the standard `S_m` differentiability/finite-rank approximation of the modified determinant, and its final product is trace class: for `m>=2`,

\[
K^{m-1}\in S_{m/(m-1)},
\qquad
(I+K)^{-1}K'\in S_m,
\tag{14}
\]

so Schatten Holder gives an `S_1` product. The `m=1` case is the ordinary trace-class determinant formula.

Now set `K=U-I`. Since `U` is unitary,

\[
U^{-1}U'=U^*U'=iQ_U.
\tag{15}
\]

Substituting into (11) gives

\[
\boxed{
\frac{d}{dt}\log\det_m U
=
i(-1)^{m-1}
\operatorname{Tr}\bigl((U-I)^{m-1}Q_U\bigr).
}
\tag{16}
\]

Taking the imaginary part yields (3). No commutation between `U` and `Q_U` is needed: for the trace-class product,

\[
\operatorname{Re}\operatorname{Tr}(AQ_U)
=
\operatorname{Tr}((\operatorname{Re}A)Q_U).
\tag{17}
\]

Thus the positivity question is exactly whether the functional-calculus factor `H_m(U)` has a universal semidefinite orientation.

## 2. Only orders one and two retain the passive cone

For `m=1`, (3) gives the ordinary determinant phase law

\[
\frac{d}{dt}\arg\det U
=
\operatorname{Tr}Q_U\ge0.
\tag{18}
\]

For `m=2`, unitarity gives

\[
H_2(U)
=I-\operatorname{Re}U
=\frac12(U-I)^*(U-I)\succeq0,
\tag{19}
\]

which is exactly the order-two positivity behind `WP-178`.

For `m>=3`, write `n=m-1>=2`. The elementary identity

\[
e^{i\theta}-1
=2i\,e^{i\theta/2}\sin(\theta/2)
\tag{20}
\]

gives

\[
(-1)^n(e^{i\theta}-1)^n
=
\bigl(2\sin(\theta/2)\bigr)^n
\exp\!\left(\frac{in(\theta-\pi)}2\right),
\tag{21}
\]

which proves (6).

At `theta=pi`,

\[
h_m(\pi)=2^{m-1}>0.
\tag{22}
\]

For `m=3`,

\[
h_3(\theta)
=-2\cos\theta(1-\cos\theta),
\qquad
h_3(\pi/3)=-\frac12<0.
\tag{23}
\]

For `m>=4`, set `n=m-1>=3` and choose

\[
\theta_n=\pi-\frac{2\pi}{n}.
\tag{24}
\]

Then the cosine in (6) equals `-1`, while the sine factor is positive, hence

\[
h_m(\theta_n)
=-\bigl(2\cos(\pi/n)\bigr)^n<0.
\tag{25}
\]

So the scalar symbol changes sign for every `m>=3`. Since scalar unitaries are a subclass of the operator problem, no universal theorem of the form

\[
Q_U\succeq0
\Longrightarrow
\frac{d}{dt}\arg\det_m U\ge0
\quad\text{or}\quad
\frac{d}{dt}\arg\det_m U\le0
\tag{26}
\]

can hold at those orders. This proves (9).

## 3. Matched passive controls show that the regularizer creates the sign

The sign-indefiniteness is not an artifact of allowing arbitrary unitary paths. The pure delay (7) is a scalar Schur-inner function in the upper half-plane because, for `z=x+iy` with `y>0`,

\[
|U_a(z)|=e^{-ay}\le1,
\tag{27}
\]

while on the real axis

\[
|U_a(t)|=1,
\qquad
-i\overline{U_a(t)}U_a'(t)=a>0.
\tag{28}
\]

It is therefore a regular lossless passive response with a **constant positive** geometric delay. In one dimension all Schatten hypotheses hold automatically. Nevertheless, its `det_m` phase derivative is (8), and for every `m>=3` it alternates sign as `at` moves around the circle.

For `m=3`, the scalar regularized phase is especially transparent:

\[
\arg\det_3(e^{i\theta})
=
\theta-2\sin\theta+\frac12\sin2\theta
\quad\text{modulo a branch constant},
\tag{29}
\]

so

\[
\frac{d}{d\theta}\arg\det_3(e^{i\theta})
=-2\cos\theta(1-\cos\theta).
\tag{30}
\]

Thus the third-order counterterm turns a constant positive delay into a signed phase velocity. Nothing arithmetic, archimedean, or zero-dependent is involved.

A one-pole Blaschke factor gives the same control in the rational-inner class. Its boundary phase winds once around the unit circle with positive delay, so it traverses both sign regions of `h_m` for every `m>=3`. The escape from `WP-178` is therefore real, but it is a generic regularization effect rather than a new source-specific positive geometry.

## 4. The raw modulus also stops carrying a stable orientation

For a scalar unitary `z=e^{i\theta}`, (10) gives

\[
\log|\det_m z|
=
\operatorname{Re}\sum_{j=1}^{m-1}
\frac{(-1)^j}{j}(z-1)^j.
\tag{31}
\]

At order three,

\[
\log|\det_3(e^{i\theta})|
=(1-\cos\theta)^2\ge0,
\tag{32}
\]

so the raw `det_3` is still non-unimodular except at the identity. Already at order four,

\[
\boxed{
\log|\det_4(e^{i\theta})|
=-\frac{(1-\cos\theta)^2(4\cos\theta-1)}{3},
}
\tag{33}
\]

which takes both signs and vanishes nontrivially at `cos(theta)=1/4`. Hence even the direction of the raw modulus anomaly found for `det_2` is not stable under higher regularization order.

This is another falsification of the idea that simply moving to a higher determinant retains passive positivity while gaining the desired signed phase. The higher counterterm polynomial is itself changing the order structure.

## 5. Consequence for the exact Gamma phase

The source-derived real-place factor from `WP-169` is

\[
R_\infty(t)
=\pi^{it}
\frac{\Gamma(\tfrac14-\tfrac{it}{2})}
     {\Gamma(\tfrac14+\tfrac{it}{2})}
=e^{i\phi_\infty(t)},
\tag{34}
\]

with

\[
\phi_\infty'(t)
=\log\pi-
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right).
\tag{35}
\]

`WP-170`--`WP-178` show that this derivative is positive near the origin and negative for sufficiently large positive `t`, while ordinary Schur delay and the `det_2` phase have a fixed passive orientation.

For `m>=3`, equation (6) means that the simple sign-change contradiction disappears. It would therefore be **wrong** to extend `WP-178` by claiming that every higher modified determinant remains monotone.

But the branch target is not merely an analytic representation of (34). It asks for a sign forced independently by geometry. Equations (6)--(8) show that higher modified determinants lose exactly that inheritance: the same cone `Q_U>=0` can be scalarized to either sign solely by changing the passive boundary phase. Consequently an identity

\[
\arg\det_m U(t)=\phi_\infty(t)+C,
\qquad m\ge3,
\tag{36}
\]

would not by itself explain Weil positivity. It would show only that the regularized determinant is flexible enough to encode the target phase.

A higher-determinant route becomes relevant only if Mathia supplies an additional **independent** theorem forcing the admissible spectrum/coupling so that the factor `H_m(U)` in (3) acquires a canonical sign or coercivity property after the finite-prime and archimedean sectors are assembled. Choosing spectral sectors or counterterms because they reproduce (35) is precisely the hand-picked regularization failure mode excluded by the line contract.

## 6. Aggressive falsification and exact scope

This result is deliberately narrower than a realization no-go. A specially constrained `det_m`, a dissipative lift, an analytic counterterm, a singular determinant, or a nonseparable finite--archimedean construction could still reproduce the exact Gamma factor. What is closed is the claim that **ordinary lossless passivity itself** supplies the sign after a higher modified determinant scalarization.

A source-forced spectral-sector theorem could restore a sign: if an intrinsic construction kept the spectrum of `U(t)` inside an arc on which `h_m` has one orientation, then (3) would again become one-sided. But that arc restriction is new geometry. It must be derived without fitting the Gamma target and must survive the full finite--archimedean assembly.

The result does not weaken `WP-171`. Passivity still gives `Q_U>=0`; the sign is discarded only by the higher regularizing polynomial. Nor does it classify zeta determinants, heat-kernel determinants, non-Schatten notions, dimension-dependent subtractions, singular/domain-changing limits, or indefinite geometries. Each of those requires its own coercivity and prior-art audit.

Most importantly, nonseparable finite--archimedean coupling remains open. A larger Mathia object could alter the admissible operator cone before any determinant is taken and prove positivity only after a final quotient/compression. The present classification applies to determinant scalarization of a regular lossless passive boundary object.

## 7. Prior-art and novelty audit

The determinant technology is classical. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society (2005), especially Chapter 9, and Israel Gohberg, Seymour Goldberg, and Nahum Krupnik, *Traces and Determinants of Linear Operators*, Operator Theory: Advances and Applications 116, Birkhauser (2000), are standard references for Schatten ideals and modified Fredholm determinants. `WP-178` already uses these as the order-two prior-art boundary.

For the higher-order definition and correction-polynomial structure, a direct modern source is Thomas Britz, Alan Carey, Fritz Gesztesy, Roger Nichols, Fedor Sukochev, and Dmitriy Zanin, *The product formula for regularized Fredholm determinants*, Proceedings of the American Mathematical Society, Series B 8 (2021), 42--51; arXiv: `2007.12834`. Their standard `det_k` definition is (10). Nikolaos Koutsonikos-Kouloumpis and Matthias Lesch, *The product formula for regularized Fredholm determinants: two new proofs*, arXiv: `2202.12923`, gives a later treatment of the same higher-order algebra.

Higher-order spectral-shift theory is also established prior art rather than a new Mathia mechanism; see Ken Dykema and Anna Skripka, *Higher order spectral shift*, Journal of Functional Analysis 257 (2009), 1092--1132, DOI `10.1016/j.jfa.2009.02.019`, and subsequent higher-order trace-formula work. The passive boundary input is classical as well: `WP-171` records Potapov and Arov--Dym as the anchors for Schur/inner functions, passive systems, and `Q_U>=0`.

A bounded literature audit across modified Fredholm determinants, regularized perturbation determinants, and higher-order spectral-shift theory found the expected regularization and higher-order trace machinery. No historical novelty is claimed for (10)--(17), Schatten Holder, scalar unitary functional calculus, or the fact that higher counterterms need not preserve an order structure.

The Mathia-specific delta is the exact passivity-sign classification obtained by combining that classical determinant calculus with the source-derived boundary problem of `WP-169`--`WP-178`:

\[
\boxed{
Q_U\succeq0
\quad\Longrightarrow\quad
\begin{cases}
\dfrac{d}{dt}\arg\det_m U\ge0, & m=1,2,\\[2mm]
\text{no universal sign}, & m\ge3.
\end{cases}
}
\tag{37}
\]

The pure-delay and Blaschke controls show that the lost sign is not a subtle arithmetic effect. This is a branch-specific decisive narrowing and prior-art classicalization, not a new theorem in determinant theory and not a proof of Weil positivity.

## 8. Research consequence

The determinant frontier after `WP-178` now has a sharp boundary. Going from `det_2` to `det_m`, `m>=3`, **does** evade the monotonicity obstruction, so higher modified determinants cannot be dismissed by repeating the Hilbert--Carleman argument. But they evade it by giving up the very positivity inheritance the branch is trying to explain.

The next determinant-based route is therefore not to try higher regularizations until the Gamma phase fits. It must identify an intrinsic reason, absent from the pure-delay and Blaschke controls, why the assembled Mathia operator lies in a spectral/cohomological sector on which the signed higher-determinant readout is controlled by a new positive theorem. Without that theorem, the construction is another regularized representation of already-known archimedean data and fails the substantive target even if the scalar identity is exact.
