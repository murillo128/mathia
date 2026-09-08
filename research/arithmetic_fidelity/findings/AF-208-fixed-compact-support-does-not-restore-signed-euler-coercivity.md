# AF-208 — Fixed compact support does not restore signed Euler coercivity

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-BRIDGE`, `QUANTITATIVE-FIDELITY`, `SOURCE-REALIZABILITY`, `SOURCE-COMPLEXITY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-207 shows that a signed Peano carrier can hide an order-one weighted-variation defect from every observable in a fixed Euler band by sending a zero-mass dipole to infinity. Tail escape is not the essential obstruction. Even after imposing one common compact support and a uniform total-variation bound, arbitrarily fine signed oscillation can defeat every fixed compact Euler observation family.

Fix

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad T<\infty,
\]

and retain

\[
g_{m,\tau}(t)
:=(-1)^mF_{\sigma+i\tau}^{(m)}(t),
\qquad |\tau|\le T,
\]

and

\[
h(t):=g_{m,0}(x)-g_{m,0}(t)>0\qquad(t>x).
\]

For a finite signed Borel measure `beta` of mass one define, as in AF-207,

\[
V_h(\beta):=\int h\,d|\beta|,
\]

and

\[
D_T(\beta):=
\sup_{|\tau|\le T}
\left|
\int\bigl(g_{m,\tau}(t)-g_{m,\tau}(x)\bigr)\,d\beta(t)
\right|.
\]

Then for every prescribed `A>0` there exist a finite `L>x`, a constant `B<\infty`, and smooth compactly supported signed densities `b_n` contained in the single interval `(x,L)` such that

\[
\int b_n(t)\,dt=1,
\qquad
\|b_n(t)dt\|_{TV}\le B,
\]

while

\[
\boxed{
D_T(b_n(t)dt)\longrightarrow0,
\qquad
V_h(b_n(t)dt)\longrightarrow A>0.
}
\]

Thus neither tightness, common compact support, nor a uniform total-variation budget restores a lower coercive estimate

\[
D_T(\beta)\ge cV_h(\beta)
\]

on a sufficiently rich signed carrier class.

The mechanism is structural. If `K` and `Theta` are compact spaces and `phi in C(Theta times K)`, the observation operator

\[
\mathcal A:M(K)\to C(\Theta),
\qquad
(\mathcal A\mu)(\theta)=\int_K\phi(\theta,t)\,d\mu(t),
\]

is compact from total variation to the uniform norm. Consequently its restriction to any infinite-dimensional closed subspace cannot be bounded below. A compact continuum of smooth observations can be exactly injective on an infinite-dimensional signed source class, but it cannot provide uniform total-variation stability there.

The Euler band is one instance with

\[
K\subset(x,\infty),
\qquad
\Theta=[-T,T],
\qquad
\phi(\tau,t)=g_{m,\tau}(t)-g_{m,\tau}(x).
\]

Hence AF-030's exact closed-span criterion and the present stability obstruction are compatible: an observation family may in principle have no exact annihilator while still possessing arbitrarily small singular directions.

Finally, the explicit compactly supported carriers below are again genuine normalized Peano carriers of moment-matched probability source pairs supported in one common compact interval. The failure is therefore not introduced by allowing unrealizable signed carrier profiles.

## Derivation

### 1. Continuous compact observation families define compact measure operators

Let `K` and `Theta` be compact metric spaces and let

\[
\phi:\Theta\times K\to\mathbb C
\]

be continuous. For the unit ball of `M(K)` in total variation,

\[
\|\mu\|_{TV}\le1,
\]

one has

\[
|\mathcal A\mu(\theta)|
\le \|\phi\|_\infty.
\]

Moreover,

\[
|\mathcal A\mu(\theta)-\mathcal A\mu(\theta')|
\le
\sup_{t\in K}|\phi(\theta,t)-\phi(\theta',t)|.
\]

Uniform continuity of `phi` on the compact product makes the image of the unit ball uniformly bounded and equicontinuous. Arzela--Ascoli therefore makes that image relatively compact in `C(Theta)`. Thus `mathcal A` is compact.

Suppose now that `E subset M(K)` is a closed infinite-dimensional subspace and that for some `c>0`

\[
\|\mathcal A\mu\|_\infty\ge c\|\mu\|_{TV}
\qquad(\mu\in E).
\]

Then `mathcal A|_E` is injective, has closed range, and its inverse on that range is bounded. Relative compactness of the image of the unit ball would then imply relative compactness of the unit ball of `E`, impossible in an infinite-dimensional normed space. Therefore

\[
\boxed{
\inf_{\mu\in E,\ \|\mu\|_{TV}=1}
\|\mathcal A\mu\|_\infty=0.
}
\]

This is the abstract source-complexity obstruction. Compactness of the source *domain* `K` does not make the total-variation unit ball compact; an infinite-dimensional signed source class still contains oscillatory directions that a compact observation operator can flatten.

### 2. Explicit fixed-support Euler null sequence

Choose numbers

\[
x<a<b<L
\]

and a nonnegative nonzero bump

\[
q\in C_c^\infty((a,b)).
\]

Since `h>0` on `(x,\infty)`, put

\[
H_q:=\int_a^b h(t)q(t)\,dt>0
\]

and choose

\[
c:=\frac{A\pi}{2H_q}.
\]

Define the zero-mass oscillatory density

\[
r_n(t)
:=\frac{c}{n}\frac{d}{dt}\bigl(q(t)\sin(nt)\bigr)
=cq(t)\cos(nt)+\frac{c}{n}q'(t)\sin(nt).
\]

Because `q` vanishes at the endpoints of its support,

\[
\int r_n(t)\,dt=0.
\]

Independently choose a nonnegative unit-mass bump `a_n` supported in `(x,x+1/n)` for all sufficiently large `n`, and set

\[
b_n:=a_n+r_n.
\]

The two supports are disjoint for large `n`; every `b_n` is smooth, supported in `(x,L)`, and has total mass one.

Put

\[
\Phi_\tau(t):=g_{m,\tau}(t)-g_{m,\tau}(x).
\]

The anchor part satisfies, uniformly in the fixed band,

\[
\sup_{|\tau|\le T}
\left|\int\Phi_\tau(t)a_n(t)dt\right|
=O(n^{-1}),
\]

because `Phi_tau(x)=0` and `partial_t Phi_tau` is uniformly bounded near `x`.

For the oscillatory part, integration by parts gives

\[
\int\Phi_\tau(t)r_n(t)dt
=-\frac{c}{n}\int_a^b
\partial_t\Phi_\tau(t)q(t)\sin(nt)dt.
\]

Continuity of the Euler derivative family on the compact set `[-T,T] times [a,b]` therefore gives

\[
\sup_{|\tau|\le T}
\left|\int\Phi_\tau r_n\right|
\le
\frac{c\|q\|_1}{n}
\sup_{|\tau|\le T,\ t\in[a,b]}
|g'_{m,\tau}(t)|
=O(n^{-1}).
\]

Hence

\[
D_T(b_n(t)dt)=O(n^{-1})\to0.
\]

No mass escapes and no large support scale is used. The invisible direction is purely oscillatory.

### 3. Weighted variation stays nonzero

Because the anchor and oscillatory supports are disjoint,

\[
V_h(b_n(t)dt)
=
\int h(t)a_n(t)dt
+
\int h(t)|r_n(t)|dt.
\]

The first term tends to zero by continuity of `h` and `h(x)=0`.

For the second term,

\[
\left|
|r_n(t)|-c q(t)|\cos(nt)|
\right|
\le \frac{c}{n}|q'(t)|,
\]

so

\[
\int h|r_n|
-c\int hq|\cos(nt)|
\longrightarrow0.
\]

The elementary periodic averaging formula

\[
\int_a^b w(t)|\cos(nt)|dt
\longrightarrow
\frac2\pi\int_a^b w(t)dt
\]

for continuous `w` gives

\[
\int h|r_n|
\longrightarrow
c\frac2\pi H_q=A.
\]

Therefore `V_h(b_n dt)->A` as claimed.

The same estimates give a uniform total-variation bound:

\[
\|b_n(t)dt\|_{TV}
\le
1+c\|q\|_1+\frac{c}{n}\|q'\|_1.
\]

Thus the counterexample survives all three naive repairs suggested by the far-tail construction: tightness, fixed support, and bounded total variation.

### 4. The compact-support profiles are source-realizable Peano carriers

For each `b_n`, define

\[
d\lambda_n(t):=(-1)^m b_n^{(m)}(t)dt.
\]

Exactly as in AF-207, compact support and repeated integration by parts give

\[
\int t^j\,d\lambda_n(t)=0
\qquad(j=0,\ldots,m-1),
\]

and

\[
\int t^m\,d\lambda_n(t)=m!\int b_n(t)dt=m!.
\]

The order-`m` Peano kernel of `lambda_n` is exactly `b_n`. Since `lambda_n` has zero total mass, its positive and negative Jordan parts have the same finite mass `alpha_n>0`. Therefore

\[
\mu_{+,n}:=\alpha_n^{-1}\lambda_n^+,
\qquad
\mu_{-,n}:=\alpha_n^{-1}\lambda_n^-
\]

are probability measures, supported in the same compact interval `(x,L)`, whose difference `nu_n` cancels moments through order `m-1` and has normalized Peano carrier exactly

\[
\beta_{\nu_n}(dt)=b_n(t)dt.
\]

The source realization does become increasingly oscillatory: derivatives of `r_n` grow with frequency and the Jordan normalization changes the surviving moment amplitude. This is not a defect in the statement; it identifies the missing resource. Compact support controls location, but not source complexity.

## Arithmetic Fidelity consequence

AF-207's provisional escape routes can now be separated sharply. **Tightness by itself is not an anti-cancellation principle.** A fixed band of continuous Euler observables is a compact measurement operator on a compactly supported signed carrier class, so an infinite-dimensional source can hide in increasingly fine oscillations even when no mass moves outward.

The viable repairs must therefore constrain a different resource. Examples include sign coherence as in AF-206, a genuinely precompact source class in the norm relevant to the desired lower bound, a finite-dimensional or bounded-complexity parametrization with a uniform conditioning theorem, a variation/Sobolev/oscillation budget strong enough to compactify the normalized carrier class, or an observation family whose bandwidth/resolution grows with source complexity.

This is the same exact-versus-stable distinction already visible elsewhere in Arithmetic Fidelity. AF-030 classifies when a linear test family has an exact annihilator; the present result says that exact injectivity is not enough for stable inversion under total variation. A compact observation map may separate every pair and still have inverse condition number diverging along high-complexity directions.

For eventual prime applications, this sharpens the audit question. A claim that rational-prime information survives an analytic compression cannot be justified only by saying that the relevant arithmetic source remains localized in a bounded norm/scale window. One must also identify which source-complexity directions are admissible and whether the analytic observation family resolves them with a uniform modulus.

## Prior art and novelty assessment

The functional-analytic mechanism is classical.

- The Arzela--Ascoli theorem gives relative compactness of uniformly bounded equicontinuous families in `C(K)`; this is the compactness step for the measure-to-observation operator above. Standard references include K. Yosida, *Functional Analysis*, and the classical Ascoli theorem.
- Compact-operator theory says that a compact linear operator cannot have a bounded inverse on an infinite-dimensional range in the manner required by a uniform lower norm estimate. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Springer, gives standard Banach-space and compact-operator background. The Encyclopedia of Mathematics entry **“Compact operator”** records the same no-continuous-inverse boundary.
- Rainer Kress, *Linear Integral Equations*, 3rd ed., Springer (2014 printing of the 2013 edition), is standard background for compact integral operators and the resulting ill-posedness of first-kind inversion.
- The averaging of `|cos(nt)|` against a continuous weight is a classical periodic/Fourier averaging fact; it may also be obtained directly from the Fourier series of `|cos|` and the Riemann--Lebesgue theorem.
- The Peano realization step is the same classical Peano-kernel machinery already audited in AF-206 and AF-207.

No novelty is claimed for compact operators, Arzela--Ascoli, oscillatory weak cancellation, periodic averaging, or Peano kernels. The durable result is the Mathia-specific boundary they impose on the current Euler transfer program: AF-207's tail obstruction persists on one fixed compact support, so localization alone cannot replace positivity; a source-complexity or observation-resolution gate is mathematically necessary for stable signed recovery.

## Boundaries and failure modes

1. The result concerns **uniform quantitative recovery in total-variation-type carrier size**. It does not imply failure of exact injectivity for the complete fixed-band observation function `tau -> integral g_{m,tau} d beta`.
2. The counterexample exploits unbounded oscillatory complexity inside a fixed compact interval. A finite-dimensional, norm-precompact, bounded-variation, analytic, spline-complexity-bounded, or otherwise compactified source class may admit a positive lower modulus after injectivity is established.
3. The observation parameter set is compact. Allowing bandwidth or derivative order to grow with the source complexity can break the compact-family obstruction and must be analyzed separately.
4. Source realizability preserves the normalized Peano carrier exactly, but the surviving moment amplitude depends on the Jordan normalization, as in AF-207. Absolute unnormalized source statements must still carry the `Delta_m`/profile factor from AF-206.
5. The theorem is a control/stability result, not a rational-prime discriminator, a zeta-zero mechanism, or an RH implication.

## Consequence for the next research step

The signed-source problem should no longer ask whether mere tightness or bounded support repairs AF-207. The next exact question is to classify which **source-complexity compactness condition**, paired with which observation bandwidth, turns injectivity into a uniform lower recovery modulus. For Euler/Peano carriers this means identifying a natural arithmetic source class whose normalized signed profiles form a sufficiently compact set after the intended quotient, or proving that the arithmetic class still contains oscillatory null sequences of the type constructed here.