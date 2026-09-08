# AF-206 — Higher-convex order is the positive Peano cone for Euler transfer

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-BRIDGE`, `ARITHMETIC-CONTROL`, `SOURCE-CLASS-CLASSIFICATION`, `QUANTITATIVE-RECOVERY`, `NO-NOVELTY-CLAIM`

## Claim

AF-205 proves that, for the minimal-support order-`m` moment-flat source, fixed-band Euler transfer is controlled by the positive Peano B-spline carrier. Minimal support is not the reason positivity works. The exact larger source cone is classical **`m`-convex stochastic order**: equality of the first `m-1` moments together with a nonnegative order-`m` Peano kernel.

Fix

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad T<\infty,
\]

and let `mu_-` and `mu_+` be probability measures supported on `[x,\infty)` with finite `m`-th moments. Put

\[
\nu:=\mu_+-\mu_-.
\tag{1}
\]

Assume

\[
\int u^j\,d\nu(u)=0,
\qquad j=0,1,\ldots,m-1,
\tag{2}
\]

and define the Peano kernel

\[
K_\nu(t)
:=
\frac1{(m-1)!}
\int (u-t)_+^{m-1}\,d\nu(u),
\qquad t\ge x.
\tag{3}
\]

Then the classical shifted-truncated-moment characterization of `m`-convex order gives

\[
\boxed{
\mu_-\preceq_{m\text{-cx}}\mu_+
\quad\Longleftrightarrow\quad
K_\nu(t)\ge0\ \text{for every }t\ge x,
}
\tag{4}
\]

under the moment equalities `(2)`. Thus sign-definite Peano transport is not a special property of divided differences: it is exactly the positive cone selected by higher-convex order.

Suppose the pair is nontrivial and satisfies `(4)`. Define the surviving `m`-th moment

\[
\Delta_m:=\int u^m\,d\nu(u)>0.
\tag{5}
\]

Then

\[
\int_x^\infty K_\nu(t)\,dt
=\frac{\Delta_m}{m!},
\tag{6}
\]

so

\[
\beta_\nu(dt)
:=\frac{m!}{\Delta_m}K_\nu(t)\,dt
\tag{7}
\]

is a probability measure on `[x,\infty)`. For every `C^m` test function for which the expressions are integrable,

\[
\boxed{
\int f(u)\,d\nu(u)
=
\frac{\Delta_m}{m!}
\int f^{(m)}(t)\,d\beta_\nu(t).
}
\tag{8}
\]

Hence every nontrivial higher-convex ordered source pair carries a canonical positive Peano probability. The minimal-support B-spline of AF-199/AF-205 is one extremal finite-support realization of this general object, not a separate mechanism.

Now take the Euler local logarithm

\[
F_s(u)=-\log(1-e^{-su}),
\qquad s=\sigma+i\tau,
\qquad |\tau|\le T,
\tag{9}
\]

and the sign-corrected derivative

\[
g_{m,\tau}(u)
:=(-1)^mF_{\sigma+i\tau}^{(m)}(u)
=(\sigma+i\tau)^m
\sum_{k\ge1}k^{m-1}e^{-k(\sigma+i\tau)u}.
\tag{10}
\]

Equation `(8)` becomes

\[
\boxed{
(-1)^m\int F_{\sigma+i\tau}(u)\,d\nu(u)
=
\frac{\Delta_m}{m!}
\int g_{m,\tau}(t)\,d\beta_\nu(t).
}
\tag{11}
\]

On the real axis, `g_{m,0}` is positive and strictly decreasing. Define the endpoint localization defect

\[
\Lambda_{m,\sigma}(\beta_\nu)
:=
1-
\frac{1}{g_{m,0}(x)}
\int g_{m,0}(t)\,d\beta_\nu(t)
\in[0,1].
\tag{12}
\]

The same one-positive-anchor argument as in AF-205 no longer needs any B-spline or knot hypothesis. There is a finite constant

\[
C=C(m,x,\sigma,T)
\tag{13}
\]

such that

\[
\boxed{
\frac{\Delta_m g_{m,0}(x)}{m!}
\Lambda_{m,\sigma}(\beta_\nu)
\le
\sup_{|\tau|\le T}
\left|
(-1)^m\int F_{\sigma+i\tau}\,d\nu
-
\frac{\Delta_m}{m!}g_{m,\tau}(x)
\right|
\le
\frac{C\Delta_m g_{m,0}(x)}{m!}
\Lambda_{m,\sigma}(\beta_\nu).
}
\tag{14}
\]

Thus, on the entire higher-convex source cone, the exact fixed-band transfer resource is

\[
\boxed{
\Delta_m\,\Lambda_{m,\sigma}(\beta_\nu).
}
\tag{15}
\]

If a declared source scale `delta>0` is used and

\[
Q_m:=\frac{\Delta_m}{\delta^m},
\tag{16}
\]

then the normalized transfer error is two-sided comparable to

\[
\boxed{Q_m\Lambda_{m,\sigma}(\beta_\nu).}
\tag{17}
\]

This is the general source-side extension that AF-205 did not provide. The observation sees neither raw support diameter nor raw transport distance by itself. It sees the surviving moment amplitude multiplied by the localization defect of the positive Peano carrier induced by the source order.

## Derivation

### 1. Higher-convex order is exactly Peano-kernel positivity

For probability laws `X` and `Y`, the classical `m`-convex order is characterized by equality of the first `m-1` moments and the shifted truncated-moment inequalities

\[
\mathbb E(X-t)_+^{m-1}
\le
\mathbb E(Y-t)_+^{m-1}
\qquad\text{for every }t.
\tag{18}
\]

Apply this with `X\sim\mu_-` and `Y\sim\mu_+`. Subtracting the two expectations and dividing by `(m-1)!` gives precisely `(3)`. Therefore `(18)` is equivalent to `K_\nu\ge0`, proving `(4)`.

The indexing matters. Here `m=2` is the ordinary convex order: equal means and a nonnegative stop-loss difference. The corresponding Peano kernel multiplies `f''`. More generally, order `m` cancels polynomials below degree `m`, uses the truncated power `(u-t)_+^{m-1}`, and transports the `m`-th derivative.

### 2. The surviving moment is exactly the Peano mass

Integrating `(3)` over `t\in[x,\infty)` and using Tonelli on the positive and negative parts separately gives

\[
\begin{aligned}
\int_x^\infty K_\nu(t)\,dt
&=
\frac1{(m-1)!}
\int
\left[\int_x^u(u-t)^{m-1}\,dt\right]
 d\nu(u)\\
&=
\frac1{m!}
\int(u-x)^m\,d\nu(u).
\end{aligned}
\tag{19}
\]

Expanding `(u-x)^m`, every lower-degree term cancels by `(2)`, so

\[
\int(u-x)^m\,d\nu(u)=\int u^m\,d\nu(u)=\Delta_m,
\tag{20}
\]

which proves `(6)`.

Since `K_\nu\ge0`, `(6)` also shows `\Delta_m\ge0`. If `\Delta_m=0`, then `K_\nu=0` almost everywhere; the shifted-truncated-moment characterization then gives equality in both directions and the two laws coincide. Thus a nontrivial ordered pair has `(5)`.

### 3. Taylor remainder gives the canonical positive carrier

For `u\ge x`, Taylor's formula with integral remainder gives

\[
f(u)
=
\sum_{j=0}^{m-1}
\frac{f^{(j)}(x)}{j!}(u-x)^j
+
\frac1{(m-1)!}
\int_x^u f^{(m)}(t)(u-t)^{m-1}\,dt.
\tag{21}
\]

Integrating against `nu`, the polynomial part vanishes by `(2)`. Fubini then yields

\[
\int f\,d\nu
=
\int_x^\infty f^{(m)}(t)K_\nu(t)\,dt.
\tag{22}
\]

Substituting `(7)` proves `(8)`. The finite `m`-th moment assumption is enough for the Euler functions below because their derivatives are bounded on `[x,\infty)` and decay exponentially.

This also makes the relationship to AF-199 exact. For a minimal `m+1`-knot divided-difference source, `K_\nu` is a positive B-spline up to normalization. For a general higher-convex ordered pair it need not be a spline, atomic-support extremizer, or finite-dimensional object; positivity and total mass are nevertheless identical.

### 4. Euler transfer needs only positivity, not minimal support

The Euler series

\[
F_s(u)=\sum_{k\ge1}\frac{e^{-ksu}}k
\tag{23}
\]

converges absolutely for `u\ge x>0` and `\Re s=\sigma>0`. Differentiating termwise gives `(10)`. At `tau=0`,

\[
g_{m,0}(u)
=
\sigma^m\sum_{k\ge1}k^{m-1}e^{-k\sigma u}>0,
\tag{24}
\]

with

\[
g_{m,0}'(u)
=-\sigma^{m+1}
\sum_{k\ge1}k^m e^{-k\sigma u}<0.
\tag{25}
\]

Substituting `f=F_s` into `(8)` proves `(11)`.

Put

\[
h(t):=g_{m,0}(x)-g_{m,0}(t)\ge0.
\tag{26}
\]

For fixed `m,x,sigma,T`, the exponential series gives finite constants

\[
M:=\sup_{t\ge x,\ |\tau|\le T}|g_{m,\tau}(t)|,
\qquad
L:=\sup_{t\ge x,\ |\tau|\le T}|g_{m,\tau}'(t)|.
\tag{27}
\]

As in AF-205, strict monotonicity of `g_{m,0}` on `[x,x+1]` and its positive gap beyond `x+1` imply a finite `C` such that

\[
|g_{m,\tau}(t)-g_{m,\tau}(x)|
\le C h(t)
\qquad(t\ge x,\ |\tau|\le T).
\tag{28}
\]

Integrating `(28)` against the positive probability `beta_nu` gives the upper bound in `(14)`. At `tau=0`, the error has one sign and is exactly

\[
\frac{\Delta_m}{m!}
\left(g_{m,0}(x)-\int g_{m,0}\,d\beta_\nu\right)
=
\frac{\Delta_m g_{m,0}(x)}{m!}
\Lambda_{m,\sigma}(\beta_\nu),
\tag{29}
\]

which gives the lower bound.

No step in this argument uses support cardinality, alternating atomic weights, knot diameter, the Dirichlet barycentric representation, or B-spline geometry. Those structures are needed only when one wants to convert the abstract carrier defect into a simpler source coordinate, as AF-205 does for minimal support.

## Exact recovery and localization consequences

Because `g_{m,0}` is bounded, continuous, strictly decreasing on `[x,\infty)`, and uniquely maximized at `x`, the scalar defect `(12)` detects weak endpoint concentration:

\[
\boxed{
\Lambda_{m,\sigma}(\beta_n)\to0
\quad\Longleftrightarrow\quad
\beta_n\Rightarrow\delta_x
}
\tag{30}
\]

for any sequence of probability carriers supported on `[x,\infty)`. This is the all-order, arbitrary-support analogue of AF-201.

Consequently, on any higher-convex source family with normalized profiles satisfying

\[
0<q_-\le Q_{m,n}\le q_+<\infty,
\tag{31}
\]

uniform finite-band transfer to the anchored order-`m` Euler model is equivalent to

\[
\beta_{\nu_n}\Rightarrow\delta_x.
\tag{32}
\]

If `Q_{m,n}\to0`, transfer can occur without localization because the surviving source amplitude itself disappears. If `Q_{m,n}` grows, weak concentration alone is insufficient; the exact weighted condition remains `(17)`.

This separates two questions that minimal-support geometry partially conflates:

1. **observation-side positivity and localization:** completely described here by `m`-convex order, the canonical carrier `beta_nu`, and `Lambda`;
2. **source-side coercivity:** whether a chosen source metric, complexity budget, optimizer, or arithmetic constraint forces `Q_m Lambda` to stay nonzero or to vanish.

The second question is where genuinely new inverse-fidelity content must now enter.

## Arithmetic Fidelity consequence

The positive-carrier mechanism behind AF-201--AF-205 is therefore substantially more general than the original finite-difference controls. The relevant source category is not "minimal alternating stencils" but **moment-matched source pairs ordered by higher convexity**.

This gives a reusable audit for any proposed arithmetic compression based on smooth completely monotone/Euler-type observables. If two matched source systems lie in an `m`-convex order relation, then all lower polynomial information has been canceled, the first surviving signed information is packaged into the positive Peano carrier, and every fixed Euler band observes that carrier only through the weighted defect `(15)`.

Minimal-support controls remain useful because their carrier can be reduced further to knot geometry. But a lower recovery theorem proved only for those controls is not automatically a lower theorem on the full source cone. Extra support can change the carrier shape while keeping the same lower moments and the same order. The correct extension question is therefore whether the declared arithmetic source class imposes additional restrictions on admissible higher-convex Peano carriers.

For the eventual rational-prime application, this result is still a control theorem, not prime specificity. It says how a broad family of matched generalized-generator perturbations can hide or retain an order-`m` discriminator under Euler compression. It does not show that rational primes themselves sit in one side of a useful higher-convex order, nor that such an order controls zeta zeros or RH.

## Prior art and novelty assessment

The source-order mathematics is classical.

- Michel Denuit, Claude Lefèvre, and Moshe Shaked, **“The s-convex orders among real random variables, with applications,”** *Mathematical Inequalities & Applications* 1(4) (1998), 585--613, especially Theorem 3.2. Their shifted-truncated-moment characterization gives exactly the equivalence between equality of the first `s-1` moments plus `E(X-t)_+^{s-1}<=E(Y-t)_+^{s-1}` and `s`-convex order. This is the prior-art source for `(4)` and fixes the indexing used here.
- The Peano-kernel representation of a linear functional that annihilates lower-degree polynomials is classical numerical analysis; AF-199 already audits that bridge through Carl de Boor, **“Divided Differences,”** *Surveys in Approximation Theory* 1 (2005), 46--69, arXiv:`math/0502036`. For arbitrary signed functionals rather than only divided differences, the same representation is the classical Peano kernel theorem.
- Shayne Waldron, **“Refinements of the Peano Kernel Theorem,”** *Numerical Functional Analysis and Optimization* 20(1--2) (1999), 147--161, DOI `10.1080/01630569908816885`, treats general forms and refinements of the Peano-kernel theorem and confirms that the representation itself is established theory.

A targeted search found the higher-convex order and Peano-kernel ingredients to be classical and found no basis for a novelty claim about them. No novelty is claimed for `(4)`, `(8)`, stochastic orders, Peano kernels, or shifted truncated moments. The durable Arithmetic Fidelity contribution is the exact specialization and extension of AF-205: **the fixed-band Euler calibration by one positive localization defect holds on the whole higher-convex source cone, not merely on minimal-support B-spline controls.**

## Boundaries and falsification checks

- **Higher-convex order is a real restriction.** Moment matching alone does not force `K_nu` to have one sign. If the Peano kernel changes sign, cancellation inside the carrier can invalidate the one-positive-anchor lower bound even though the formal Peano representation still holds.
- **The common half-line anchor matters.** The scalar defect `(12)` detects concentration because every carrier lies in `[x,\infty)` and `g_{m,0}` has its unique maximum at the boundary point `x`. Allowing mass on both sides permits compensation.
- **Finite bandwidth matters.** The constant in `(28)` depends on `T`. Growing bandwidth is a separate resource problem and AF-181--AF-194 show that frequency resolution can change the stability regime.
- **Finite `m`-th moments matter.** They justify the normalized carrier mass and the Taylor/Peano interchange. Weaker tail assumptions may suffice for a specific Euler transform but would define a different source class.
- **The source scale is external to convex order.** Equation `(17)` is meaningful only after declaring `delta`; `m`-convex order by itself does not choose Wasserstein, diameter, logarithmic generator distance, or another recovery geometry.
- **Carrier localization is not source reconstruction.** Distinct source pairs can induce the same or nearly the same positive Peano carrier at the observation layer. This theorem controls Euler transfer, not injectivity of the map from source pair to carrier.
- **Minimal-support diameter bounds do not survive automatically.** AF-205's comparison of `Lambda` with a saturated knot diameter uses the Dirichlet/B-spline structure and cannot be imported into arbitrary-support ordered pairs.
- **No RH consequence follows.** The result identifies a broad arithmetic-control cone and its exact fixed-band fidelity resource; it neither proves a rational-prime discriminator nor a zero-selection mechanism.

## Dependencies and evidence boundary

- **AF-195 / AF-199:** identify minimal moment-flat controls with divided differences and positive Peano B-spline carriers.
- **AF-201 / AF-204:** isolate weak carrier concentration and the weighted real-axis localization defect as the quartic finite-band transfer mechanism.
- **AF-205:** extends that calibration to every fixed order on minimal-support sources and shows how B-spline geometry converts the abstract defect to saturated knot diameter.
- **This finding:** removes the minimal-support hypothesis from the positive-carrier transfer theorem by identifying the exact classical source cone that guarantees Peano positivity. It does not solve source-side coercivity or the optimizer problem left open by the local clue.