# ANF-101 — linear-span near-extremizers have exponentially tight vertical mass

**Status:** `EXACT-DERIVED + ALL-COMPLEX-MULTISETS + VERTICAL-MOMENT-COERCIVITY + LINEAR-SPAN-TIGHTNESS + NOTCH-EXPOSURE-NARROWING`. `ANF-100` shows that any growing Montgomery--Taylor near-extremizer must escape across a horizontal interval of length at least a fixed positive multiple of its cardinality. Retaining the `cosh` growth that `ANF-100` discarded gives a complementary constraint: on the same phase-coherent central interval, conjugation turns vertical height into a positive exponential moment. Consequently, whenever the horizontal diameter is only linear in cardinality, a near-extremizer has uniformly exponentially tight **vertical mass after scaling by cardinality**. Large imaginary heights can survive only on a sparse tail or together with superlinear horizontal escape.

Let

\[
J_0:=J_{\rm MT},\qquad
S_W(\alpha):=\sum_{z\in W}e^{-2\pi i\alpha z},
\qquad
N:=|W|,
\]

for a nonempty finite conjugation-invariant multiset `W`, and write

\[
L(W):=2N-\sigma(W),
\qquad
r(W):=\frac{\int_{-1}^{1}J_0(\alpha)|S_W(\alpha)|^2\,d\alpha}{L(W)}.
\tag{1}
\]

Let

\[
D:=D_x(W)
=\max_{z\in W}\Re z-\min_{z\in W}\Re z.
\tag{2}
\]

Fix `0<a_0<1` and `0<\vartheta<\pi/2`, put

\[
j(a_0):=\min_{|\alpha|\le a_0}J_0(\alpha)>0,
\tag{3}
\]

and define

\[
a(W):=
\min\!\left\{
 a_0,\frac{\vartheta}{\pi D}
\right\},
\tag{4}
\]

with `\vartheta/(\pi D)=+\infty` when `D=0`.

Then every configuration with

\[
r(W)\le1+\varepsilon
\tag{5}
\]

satisfies the exact exponential-height moment bound

\[
\boxed{
\sum_{z\in W}
\exp\!\bigl(\pi a(W)|\Im z|\bigr)
\le
2\sqrt2
\left(
\frac{N(1+\varepsilon)}
     {a(W)j(a_0)\cos^2\!\vartheta}
\right)^{1/2}.
}
\tag{6}
\]

In the linear-escape branch

\[
D\ge\frac{\vartheta}{\pi a_0},
\tag{7}
\]

so that `a(W)=\vartheta/(\pi D)`, this becomes

\[
\boxed{
\frac1N\sum_{z\in W}
\exp\!\left(\frac{\vartheta|\Im z|}{D}\right)
\le
C_{a_0,\vartheta,\varepsilon}
\sqrt{\frac DN},
}
\tag{8}
\]

where

\[
C_{a_0,\vartheta,\varepsilon}
:=
2\sqrt2
\left(
\frac{\pi(1+\varepsilon)}
     {\vartheta j(a_0)\cos^2\!\vartheta}
\right)^{1/2}.
\tag{9}
\]

Therefore, for every `\lambda\ge0`,

\[
\boxed{
\frac1N
\#\left\{z\in W:|\Im z|\ge\lambda D\right\}
\le
C_{a_0,\vartheta,\varepsilon}
\sqrt{\frac DN}\,e^{-\vartheta\lambda}.
}
\tag{10}
\]

The consequence relevant to `ANF-099`--`ANF-100` is immediate. If `W_n` is a growing Montgomery--Taylor near-extremizer,

\[
N_n\to\infty,
\qquad
r(W_n)\to1,
\tag{11}
\]

and its horizontal escape is at most linear,

\[
D_n\le A N_n
\tag{12}
\]

for some fixed `A`, then, after discarding finitely many indices,

\[
\boxed{
\sup_n\frac1{N_n}
\sum_{z\in W_n}
\exp\!\left(
\frac{\vartheta}{A}\frac{|\Im z|}{N_n}
\right)
<\infty.
}
\tag{13}
\]

After translating each configuration horizontally to the midpoint of its real-part span, (12)--(13) imply a concrete empirical tightness statement: for every `\delta>0` there is `R=R(\delta,A,a_0,\vartheta)` such that, for all sufficiently large `n`, at least `(1-\delta)N_n` points lie in

\[
\left\{z:
\frac{|\Re z|}{N_n}\le\frac A2,
\quad
\frac{|\Im z|}{N_n}\le R
\right\}.
\tag{14}
\]

Thus the minimal horizontal escape scale forced by `ANF-100` does not leave an independent macroscopic vertical-escape degree of freedom. A fatal near-extremizer in the linear-span chamber must obtain its large central-notch exposure from a genuinely nonconvex arrangement of a tight bulk, or from a sparse high-height tail whose source contribution is cancelled outside the phase-coherent window. If neither is possible, the only remaining geometric escape is `D_n/N_n\to\infty`.

## 1. Conjugation converts height into a positive exponential moment

As in `ANF-100`, group `W` by horizontal center. For real `\alpha`, a real point at `x` contributes a positive amplitude times `e^{-2\pi i\alpha x}`. A nonreal conjugate pair `x\pm iy`, with multiplicity `m` on each side, contributes

\[
2m\cosh(2\pi\alpha y)e^{-2\pi i\alpha x}.
\tag{15}
\]

Hence

\[
S_W(\alpha)
=\sum_xA_x(\alpha)e^{-2\pi i\alpha x},
\qquad
A_x(\alpha)>0.
\tag{16}
\]

This time retain the height dependence. Since

\[
2\cosh t=e^t+e^{-t}\ge e^{|t|},
\tag{17}
\]

every nonreal conjugate pair contributes at least one half of the corresponding pointwise exponential moment, while real points satisfy the same inequality trivially. Therefore

\[
\boxed{
\sum_xA_x(\alpha)
\ge
\frac12
\sum_{z\in W}
\exp\!\bigl(2\pi|\alpha|\,|\Im z|\bigr).
}
\tag{18}
\]

This is the only new ingredient beyond the phase-cone argument of `ANF-100`. It is physical: arbitrary signed exponential sums do not satisfy (18), and no Gram conditioning or frequency separation is being assumed.

## 2. The coherent central annulus pays for the vertical moment

Let `c` be the midpoint of the smallest interval containing the real parts of `W`. By the definition of `a(W)`, every `|\alpha|\le a(W)` satisfies

\[
|2\pi\alpha(\Re z-c)|\le\vartheta.
\tag{19}
\]

All horizontal phase vectors in (16) therefore lie in one cone of half-angle `\vartheta`. Taking the real part along its axis gives

\[
|S_W(\alpha)|
\ge
\cos\vartheta\sum_xA_x(\alpha).
\tag{20}
\]

Now restrict to the two intervals

\[
\frac{a(W)}2\le|\alpha|\le a(W).
\tag{21}
\]

Using (18), monotonicity of the exponential, and (20),

\[
\boxed{
|S_W(\alpha)|
\ge
\frac{\cos\vartheta}{2}
\sum_{z\in W}
\exp\!\bigl(\pi a(W)|\Im z|\bigr).
}
\tag{22}
\]

The union in (21) has total length `a(W)`, lies inside `[-a_0,a_0]`, and `J_0\ge j(a_0)` there. Consequently

\[
\int_{-1}^{1}J_0|S_W|^2
\ge
\frac{a(W)j(a_0)\cos^2\vartheta}{4}
\left(
\sum_{z\in W}
 e^{\pi a(W)|\Im z|}
\right)^2.
\tag{23}
\]

On the other hand, (5) and `L(W)\le2N` give

\[
\int_{-1}^{1}J_0|S_W|^2
=r(W)L(W)
\le2N(1+\varepsilon).
\tag{24}
\]

Combining (23)--(24) proves (6). Substitution of `a(W)=\vartheta/(\pi D)` gives (8)--(9), and Markov's elementary exponential-moment estimate gives (10).

No limiting argument enters the finite statement. Repeated real sites, repeated nonreal pairs, collisions in horizontal center, unbounded heights, and arbitrary cardinality are all included.

## 3. Linear horizontal escape forces empirical vertical tightness

Assume (11)--(12). `ANF-100` already implies

\[
\liminf_n\frac{D_n}{N_n}>0,
\tag{25}
\]

so in particular `D_n\to\infty`; hence (7) holds eventually for every fixed `a_0,\vartheta`. Also `1+\varepsilon_n` is eventually bounded, where `\varepsilon_n=r(W_n)-1`. From (8) and `D_n/N_n\le A`,

\[
\frac1{N_n}\sum_{z\in W_n}
\exp\!\left(\frac{\vartheta|\Im z|}{D_n}\right)
\le C\sqrt A
\tag{26}
\]

with `C` independent of `n`. Since `D_n\le AN_n`,

\[
\exp\!\left(
\frac{\vartheta}{A}\frac{|\Im z|}{N_n}
\right)
\le
\exp\!\left(
\frac{\vartheta|\Im z|}{D_n}
\right),
\tag{27}
\]

which proves (13).

The horizontal coordinates need no additional estimate: after centering, (12) places every real part in `[-AN_n/2,AN_n/2]`. Applying (13) to the complement of `|\Im z|\le RN_n` gives an exponentially decaying upper bound in `R`, proving (14).

This is deliberately an **empirical-mass** statement rather than a bound on the largest height. Equation (6) permits a bounded number of points as high as order `D\log(ND)`; a sparse high-height tail is not excluded. What is excluded is a positive proportion of the configuration escaping to arbitrarily large multiples of `D` when `D=O(N)`.

## 4. Consequence for the fixed-notch envelope

`ANF-099` reduces improvement along one frozen central-notch ray to the strict inequality

\[
\beta_\eta<B_\eta,
\tag{28}
\]

where `\beta_\eta` is the limiting notch exposure over all Montgomery--Taylor near-extremizers. `ANF-100` then shows that any growing sequence contributing to this envelope has `D_n\gg N_n`. The present result splits the remaining physical search into two genuinely different regimes.

If `D_n=O(N_n)`, the normalized bulk cannot escape vertically: after horizontal recentering and scaling by `N_n`, all but an arbitrarily small proportion lies in one fixed compact rectangle. Therefore any failure of (28) in this chamber must be generated by the arrangement of that tight bulk or by a sparse vertically amplified component together with enough horizontal phase cancellation to keep the full Montgomery--Taylor source norm near equality.

If instead `D_n/N_n\to\infty`, the bound (8) weakens by the explicit factor `\sqrt{D_n/N_n}`. This is a real boundary of the argument, not a missing constant. Superlinear horizontal dilution is now a separate escape regime that must be controlled by a different mechanism.

The result does **not** itself upper-bound notch exposure, produce a separable comparator, fix the anti-alignment sign from `ANF-097`, or prove (28). In particular, empirical tightness cannot discard a vanishing fraction of very high points: because the target source and notch norms contain exponential `cosh` amplification, a sparse tail may still be analytically important. Any later compactness argument must either control that tail in the target norm or keep it explicitly.

## 5. Prior art and adversarial audit

A targeted prior-art search was made against nonharmonic Fourier inequalities and Remez/Turán--Nazarov bounds for exponential polynomials. Those theories control general exponential sums through frequency separation, term count, spectral diameter, measurable-set geometry, or related complexity parameters. They do not supply the present estimate from the special conjugation-positive orbit amplitudes, and no such external theorem is needed in the derivation. The mathematical input is only the already-canonical Montgomery--Taylor spectrum and the physical conjugation symmetry of `W`, so `SOURCES.md` is unchanged.

The main failure modes are explicit. Horizontal translation changes `S_W` only by a common unimodular phase and cannot affect the argument. Large imaginary parts cannot reverse an orbit coefficient on the real `\alpha` axis because they enter through `cosh`. The phase-cone interval is chosen using the full horizontal diameter, so no hidden gap or local-density assumption is present. The use of both signs of `\alpha` is legitimate because (18)--(22) depend only on `|\alpha|`; no unproved positivity of a spatial transform at complex arguments is invoked.

The constant in (6) is audit-sensitive but elementary: the two intervals in (21) have total length `a(W)`, the orbit-to-exponential-moment comparison costs `1/2` in amplitude and hence `1/4` in energy, and `L(W)\le2N` contributes the remaining factor. A direct falsification test is therefore to find a finite conjugation-invariant multiset violating (23); such a violation would have to break either the phase-cone estimate (20) or the positive orbit bound (18).

## 6. Research boundary

Together, `ANF-100` and (13) identify a normalized geometry chamber that can no longer be dismissed as noncompact merely because complex heights are unrestricted. For growing near-extremizers with `D_n\asymp N_n`, the macroscopic mass is tight in both horizontal and vertical directions after the natural `N_n` scaling. The surviving obstruction to the `ANF-099` envelope is therefore sharper than generic lack of compactness: it must come from **nonconvex microscopic organization, a source-relevant sparse height tail, or superlinear horizontal escape**.

A decisive positive continuation would show that none of those three mechanisms can keep the source-generated notch exposure at `B_\eta` while the Montgomery--Taylor excess tends to zero. A decisive negative continuation would construct an actual physical near-extremizer in one of those regimes with exposure tending to `B_\eta` or above. The present finding supplies the exact vertical-mass constraint that any such construction must satisfy.