# AF-508 — Sublevel-distance profile is the exact no-contact rate carrier

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `CONVEX-GEOMETRY`, `RATE-TRANSFER`, `MINIMAL-LIFT`, `ORDER-OF-OPERATIONS`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-507 reduced the one-sided convex no-contact problem to the divergence of the admission height near the missing nearest quotient point. That qualitative statement can be made exact.

Keep the AF-507 setup. Let `Q` be a finite-dimensional real Hilbert space, let `u in Q` be a unit vector, write

\[
H=u^\perp,
\qquad
Q=H\oplus\mathbb Ru,
\]

and let `F subset Q` be nonempty, closed, convex, with

\[
u\in\operatorname{rec}(F),
\qquad
-u\notin\operatorname{rec}(F).
\]

Let `a=a_F:H\to\mathbb R\cup\{+\infty\}` be the proper closed convex admission height from AF-507, so

\[
F=\{z+su:s\ge a(z)\}.
\]

Set

\[
f(t):=\operatorname{dist}(tu,F),
\qquad
\lambda:=\operatorname{dist}(0,\operatorname{dom}a),
\]

and let

\[
z_*:=P_{\overline{\operatorname{dom}a}}(0).
\]

Assume the **no-contact branch**

\[
a(z_*)=+\infty.
\]

For every real admission budget `r`, define the closed convex sublevel set

\[
C_r:=\{z\in H:a(z)\le r\}
\]

and the **transverse accessibility profile**

\[
\rho(r):=\operatorname{dist}(0,C_r)^2-\lambda^2,
\]

with `dist(0,emptyset)=+infinity`. Then `rho` is nonincreasing, is strictly positive at every finite budget for which it is finite, and

\[
\rho(r)\downarrow0
\qquad(r\to+\infty).
\]

The full finite-time excess above the quotient threshold is recovered exactly from this one-dimensional profile:

\[
\boxed{
E(t):=f(t)^2-\lambda^2
=
\inf_{r\in\mathbb R}
\bigl(\rho(r)+(r-t)_+^2\bigr).
}
\]

For every sufficiently large `t` with `rho(t)<infinity`, monotonicity localizes the formula further to

\[
\boxed{
E(t)
=
\inf_{0\le h\le\sqrt{\rho(t)}}
\bigl(\rho(t+h)+h^2\bigr).
}
\]

Thus `rho` is an exact rate carrier for this observation channel. The distance observable does not see the admission-height geometry directly; it sees the sublevel accessibility profile through a one-sided quadratic infimal envelope.

There is also an exact inverse description of admission-height divergence. Define, for `eta>=0`,

\[
A(\eta)
:=
\min_{\|z\|^2-\lambda^2\le\eta} a(z).
\]

In the no-contact branch,

\[
A(0)=+\infty,
\qquad
A(\eta)<+\infty\quad(\eta>0),
\qquad
A(\eta)\to+\infty\quad(\eta\downarrow0),
\]

and the two profiles satisfy the exact generalized-inverse relation

\[
\boxed{
A(\eta)\le r
\iff
\rho(r)\le\eta.
}
\]

Consequently the divergence law of AF-507 and the accessibility profile are not two independent lifts: for this target they encode the same information in inverse coordinates.

Finally, the quadratic envelope preserves the leading rate whenever `rho` does not undergo a macroscopic relative drop inside its own square-root window. If

\[
\omega(t)
:=
\inf_{0\le h\le\sqrt{\rho(t)}}
\frac{\rho(t+h)}{\rho(t)},
\]

then

\[
\boxed{
\omega(t)\rho(t)
\le E(t)\le\rho(t).
}
\]

Hence

\[
\omega(t)\to1
\quad\Longrightarrow\quad
E(t)\sim\rho(t).
\]

In particular, a power-law boundary divergence

\[
A(\eta)\sim c\,\eta^{-\beta}
\qquad(\eta\downarrow0),
\qquad c,\beta>0,
\]

forces

\[
\rho(t)
\sim
c^{1/\beta}t^{-1/\beta}
\]

and therefore

\[
f(t)^2-\lambda^2
\sim
c^{1/\beta}t^{-1/\beta}.
\]

Equivalently,

\[
\boxed{
\lambda>0
\Longrightarrow
f(t)-\lambda
\sim
\frac{c^{1/\beta}}{2\lambda}\,t^{-1/\beta},
}
\]

while at the zero threshold

\[
\boxed{
\lambda=0
\Longrightarrow
f(t)
\sim
c^{1/(2\beta)}t^{-1/(2\beta)}.
}
\]

This closes the first quantitative gate left open by AF-507: a specified divergence profile can force an explicit approach rate, and the exact intermediate object is the distance of the admission sublevels from the critical quotient point.

## The accessibility profile is positive and tends to zero

Because `a` is lower semicontinuous and convex, every finite sublevel `C_r` is closed and convex. The family is increasing:

\[
r_1\le r_2
\Longrightarrow
C_{r_1}\subseteq C_{r_2}.
\]

Therefore `rho` is nonincreasing wherever finite. Moreover

\[
\bigcup_{r\in\mathbb R}C_r
=
\operatorname{dom}a,
\]

so

\[
\inf_r\operatorname{dist}(0,C_r)^2
=
\inf_{z\in\operatorname{dom}a}\|z\|^2
=
\lambda^2.
\]

Hence `rho(r) downarrow 0` as `r to infinity`.

The no-contact assumption makes every finite value strictly positive. If `rho(r)=0` for some finite `r`, then the closed nonempty set `C_r` has a nearest point `z_r` to `0` with

\[
\|z_r\|=\lambda.
\]

Since `C_r subset dom a subset closure(dom a)`, uniqueness of the Hilbert projection onto the closed convex set `closure(dom a)` forces

\[
z_r=z_*.
\]

But `z_r in C_r` implies `a(z_*)<=r`, contradicting `a(z_*)=+infinity`.

Thus the no-contact branch is equivalently visible in the budget family as

\[
\rho(r)>0
\]

for every finite admissible budget, even though those positive defects converge to zero as the budget diverges.

## Exact scalarization of the AF-507 distance envelope

AF-507 proved

\[
E(t)
=
\inf_{z\in H}
\left(
\|z\|^2-\lambda^2+(a(z)-t)_+^2
\right).
\]

For any `z in dom a`, take `r=a(z)`. Since `z in C_r`,

\[
\rho(r)
\le
\|z\|^2-\lambda^2.
\]

Therefore

\[
\inf_r\bigl(\rho(r)+(r-t)_+^2\bigr)
\le E(t).
\]

Conversely, fix `r` with `C_r` nonempty. Because `C_r` is closed in finite-dimensional Hilbert space, choose a nearest point `z_r in C_r`. Then

\[
\|z_r\|^2-\lambda^2=\rho(r),
\qquad
a(z_r)\le r.
\]

Hence

\[
E(t)
\le
\rho(r)+(a(z_r)-t)_+^2
\le
\rho(r)+(r-t)_+^2.
\]

Taking the infimum in `r` proves

\[
E(t)
=
\inf_r\bigl(\rho(r)+(r-t)_+^2\bigr).
\]

The reduction is stronger than merely bounding the distance by one convenient sublevel. It shows that, after AF-507's epigraph representation, **all transverse geometry relevant to the scalar distance history is compressed into the single nested-sublevel distance profile `rho`**.

## The quadratic envelope has an exact local window

For `r<=t`, the hinge penalty vanishes. Since `rho` is nonincreasing,

\[
\inf_{r\le t}\rho(r)=\rho(t).
\]

Writing `r=t+h` on the remaining half-line gives

\[
E(t)
=
\min\left\{
\rho(t),
\inf_{h>0}\bigl(\rho(t+h)+h^2\bigr)
\right\}.
\]

The competitor `h=0` already has cost `rho(t)`. Any `h>sqrt(rho(t))` has

\[
h^2>\rho(t)
\]

and therefore cannot improve that competitor. This proves the exact localization

\[
E(t)
=
\inf_{0\le h\le\sqrt{\rho(t)}}
\bigl(\rho(t+h)+h^2\bigr).
\]

This identifies the precise scale on which further compression can alter the apparent rate. The observable at time `t` may benefit from a slightly larger admission budget, but only by looking ahead by at most

\[
\sqrt{\rho(t)}.
\]

Consequently

\[
\left(
\inf_{0\le h\le\sqrt{\rho(t)}}
\frac{\rho(t+h)}{\rho(t)}
\right)\rho(t)
\le E(t)\le\rho(t).
\]

A profile that is relatively stable on this intrinsic window survives the quadratic envelope asymptotically unchanged. A profile with arbitrarily sharp drops on this shrinking scale need not. Thus even after the correct rate carrier has been identified, one still has a second fidelity question: whether the final distance compression preserves that carrier's leading asymptotic.

## Boundary divergence and sublevel accessibility are generalized inverses

For `eta>=0`, put

\[
K_\eta
:=
\{z\in H:\|z\|^2-\lambda^2\le\eta\}.
\]

Each `K_eta` is compact. Since `a` is lower semicontinuous, its extended-real minimum on `K_eta` is attained, so

\[
A(\eta)=\min_{K_\eta}a
\]

is well defined.

Because `z_*` is in the closure of `dom a`, every `K_eta` with `eta>0` contains domain points sufficiently near `z_*`; hence `A(eta)` is finite for `eta>0`. At `eta=0`, no domain point can occur: any such point would have norm `lambda` and therefore equal the unique nearest point `z_*`, contradicting no-contact. Thus `A(0)=+infinity`.

If `A(eta)` failed to diverge as `eta downarrow 0`, there would be a sequence `eta_n downarrow 0` and minimizers `z_n in K_{eta_n}` with `a(z_n)` bounded above. Compactness gives `z_n to z_*` along a subsequence, while lower semicontinuity would imply `a(z_*)<infinity`, again a contradiction. Therefore

\[
A(\eta)\to+\infty.
\]

Now observe that

\[
A(\eta)\le r
\]

holds exactly when there exists a point satisfying both

\[
a(z)\le r,
\qquad
\|z\|^2-\lambda^2\le\eta.
\]

The first condition is `z in C_r`; minimizing the second over `C_r` gives precisely `rho(r)`. Hence

\[
A(\eta)\le r
\iff
\rho(r)\le\eta.
\]

So `A` and `rho` form a monotone generalized-inverse pair. The apparently geometric question "how close to the missing quotient point can budget `r` reach?" and the apparently analytic question "how much admission height is required to reach defect `eta`?" are the same discriminator in opposite coordinates.

## Power-law divergence transfers to a power-law approach rate

Suppose

\[
A(\eta)
\sim
c\eta^{-\beta}
\qquad(\eta\downarrow0)
\]

with `c,beta>0`. Monotone inversion of the exact equivalence above gives

\[
\rho(r)
\sim
\left(\frac c r\right)^{1/\beta}
=
c^{1/\beta}r^{-1/\beta}.
\]

For completeness, two-sided asymptotic bounds on `A` invert directly: for every fixed `epsilon>0`, sufficiently small `eta` satisfies

\[
(1-\epsilon)c\eta^{-\beta}
\le A(\eta)
\le
(1+\epsilon)c\eta^{-\beta},
\]

which brackets the transition `A(eta)<=r` between the corresponding powers of `r`. Letting `epsilon downarrow0` yields the displayed asymptotic for `rho`.

Such a regularly varying profile is stable on the intrinsic window because

\[
0\le h\le\sqrt{\rho(t)}
=O\left(t^{-1/(2\beta)}\right)
=o(t).
\]

Therefore

\[
\frac{\rho(t+h)}{\rho(t)}\to1
\]

uniformly on that window, and the locality inequality gives

\[
E(t)\sim\rho(t)
\sim c^{1/\beta}t^{-1/\beta}.
\]

The distinction between `lambda>0` and `lambda=0` comes only from converting squared-distance excess back to distance. If `lambda>0`,

\[
f(t)-\lambda
=
\frac{E(t)}{f(t)+\lambda}
\sim
\frac{E(t)}{2\lambda}.
\]

If `lambda=0`, then `f(t)=sqrt(E(t))`. This gives the two exponents stated in the claim.

The same reasoning gives coarse rates under two-sided power bounds. If

\[
A(\eta)=\Theta(\eta^{-\beta}),
\]

then

\[
\rho(t)=\Theta(t^{-1/\beta}),
\qquad
f(t)^2-\lambda^2=\Theta(t^{-1/\beta}),
\]

with the corresponding distance exponents after the same `lambda>0` / `lambda=0` split.

## A matched family with identical quotient data and arbitrary power exponents

The rate information is genuinely absent from the quotient image and from the no-contact bit.

Fix `L>0`. For every `beta>0`, work in `H=R` and define

\[
a_\beta(y)
:=
\begin{cases}
(y^2-L^2)^{-\beta},&y>L,\\
+\infty,&y\le L.
\end{cases}
\]

The finite branch is convex because

\[
a_\beta''(y)
=
2\beta (y^2-L^2)^{-\beta-2}
\bigl((2\beta+1)y^2+L^2\bigr)>0.
\]

Moreover `a_beta(y) to +infinity` as `y downarrow L`, so the extended-real function is proper, closed, and convex. Its domain and closed domain are independent of `beta`:

\[
\operatorname{dom}a_\beta=(L,\infty),
\qquad
\overline{\operatorname{dom}a_\beta}=[L,\infty),
\]

with

\[
z_*=L,
\qquad
\lambda=L,
\qquad
a_\beta(z_*)=+\infty.
\]

Thus every member has the same quotient image, the same quotient closure, the same asymptotic threshold, and the same negative contact bit.

But

\[
C_r
=
\left[\sqrt{L^2+r^{-1/\beta}},\infty\right)
\qquad(r>0),
\]

so

\[
\boxed{
\rho_\beta(r)=r^{-1/\beta}
}
\]

exactly. Equivalently,

\[
A_\beta(\eta)=\eta^{-\beta}.
\]

Hence

\[
f_\beta(t)-L
\sim
\frac1{2L}t^{-1/\beta}.
\]

Changing only `beta` realizes every positive power exponent while preserving all of the quotient-level data listed above. Therefore neither the full quotient image, its closure, the threshold, nor the no-contact bit can determine the quantitative approach rate. The missing information is not another Boolean mark; it is the near-boundary admission/sublevel profile.

This matched family is also a direct falsification control against claiming a rate from quotient geometry alone.

## Prior-art audit

The generic convex-analytic ingredients are classical, and no broad novelty is claimed for epigraph-distance formulas, sublevel value functions, generalized inverses, or power-law error-bound phenomena.

- M. Volle, **"The Use of Monotone Norms in Epigraphical Analysis,"** *Journal of Convex Analysis* 1 (1994), 203–224. Proposition 3.1 gives the distance from `(x,s)` to an epigraph as an infimum involving the horizontal distance and the positive part `(f(u)-s)_+` for a general monotone product norm. In the Hilbert `l2` case, AF-507's basic distance formula is a direct specialization of this classical epigraphical calculus.
- R. T. Rockafellar, *Convex Analysis*, Princeton University Press (1970). Closed proper convex functions, sublevel sets, epigraphs, recession directions, marginal/value functions, and metric projection supply the standard background.
- A. Y. Aravkin, J. V. Burke, M. P. Friedlander, **"Variational Properties of Value Functions,"** *SIAM Journal on Optimization* 23 (2013), 1689–1717, DOI `10.1137/120899157`. This develops inverse relationships between parameterized convex value functions and is close in spirit to the `A`/`rho` generalized-inverse reparameterization.
- A. Y. Aravkin, J. V. Burke, D. Drusvyatskiy, M. P. Friedlander, S. Roy, **"Level-set methods for convex optimization,"** *Mathematical Programming* 174 (2019), 359–390, DOI `10.1007/s10107-018-1351-8`. This is relevant prior art for replacing a constrained convex problem by a family of level-set value problems and studying the resulting scalar value function.
- G. Li, B. S. Mordukhovich, **"Hölder Metric Subregularity with Applications to Proximal Point Method,"** *SIAM Journal on Optimization* 22 (2012), DOI `10.1137/120864660`. Hölder/error-bound exponents are an established variational-analysis language for power-law distance/residual relations.

The Arithmetic Fidelity contribution here is therefore deliberately narrower: starting from AF-507's specific information-loss chain, identify the exact one-dimensional sublevel-distance object that carries the no-contact rate, prove the exact one-sided quadratic envelope and its intrinsic localization scale, show that the admission-divergence profile is its generalized inverse, and exhibit a matched family proving that quotient data plus the contact bit cannot recover the rate exponent.

## Representation audit and boundaries

- `rho` is **representation- and task-relative**. It depends on the fixed observation direction `u`, the Hilbert norm, and the distinguished quotient origin. It is not claimed to be a source-intrinsic invariant of `F` under arbitrary changes of representation.
- `A` and `rho` are equivalent for this target through the exact generalized-inverse relation. Persisting both does not constitute two independent information channels.
- The scalar distance history is a further compression of `rho` through the one-sided quadratic envelope. Exact recovery of `rho` from `E` is not claimed here.
- The rate-retention criterion is sufficient, not necessary. Profiles with sharp relative drops on the `sqrt(rho(t))` scale require a separate audit; the quadratic envelope may then change the apparent leading behavior.
- Finite dimensionality is used for compactness/projection and exact sublevel minimizers. Infinite-dimensional extensions need independent attainment and compactness hypotheses.
- The power-law theorem concerns divergence measured in the canonical transverse squared-excess coordinate `eta=||z||^2-lambda^2`. Translating an externally chosen Euclidean boundary-distance law into `eta` can change exponents depending on boundary geometry and must not be done silently.
- The matched family proves insufficiency of quotient-level data for the rate discriminator. It does not assert that `rho` is a universally minimal representation among all possible encodings.
- No arithmetic or RH consequence is established. The result is a generic compression theorem that can later be applied only if a concrete arithmetic quotient naturally supplies an admission/sublevel profile with independently controlled asymptotics.

## Consequence

AF-505 through AF-508 now resolve four successive information layers in the one-sided convex ray-contact channel:

\[
\text{closed quotient geometry}
\longrightarrow
\text{contact membership}
\longrightarrow
\text{admission height at contact}
\longrightarrow
\text{near-boundary admission profile}.
\]

They recover, respectively, the limiting threshold, whether the threshold is ever attained, the onset time when it is attained, and the quantitative approach rate when it is not.

For the no-contact branch, the next question is therefore sharper than "how fast does `a_F` diverge?" It is:

> **What structural hypotheses force a particular generalized-inverse profile `rho`, or prevent sharp losses when `rho` is passed through the one-sided quadratic envelope, and do any natural arithmetic quotients provide such hypotheses without inserting them as an external regularity assumption?**

That is the remaining bridge from this generic convex fidelity mechanism to an arithmetic application.