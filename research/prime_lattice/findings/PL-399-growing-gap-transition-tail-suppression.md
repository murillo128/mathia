# PL-399 — Growing additive gaps push the larger mode into an algebraic continuation tail

**Evidence/status:** `CLASSICAL-SPECIAL-FUNCTION+EXACT-DERIVED + NEGATIVE/ROUTE-RESTRICTION`.

**Parent findings:** `PL-396`, `PL-397`, `PL-398`.

## Claim

`PL-398` left one explicit escape from its fixed-gap meet/join collapse: let the additive gap itself grow, so that the prime support of the gap is no longer frozen. In the same continuation-faithful incomplete-gamma representation used in `PL-396`, that escape has an analytic cost.

Let

\[
q=r+d,
\qquad
d=d(r)\to\infty,
\qquad
d=o(r),
\]

and evaluate the normalized incomplete-gamma weights at the nominal cross-channel saddle

\[
T=2\pi rq,
\qquad
s=\frac12+iT,
\qquad
Q_n(T)=Q\!\left(\frac{s}{2},\pi i n^2\right).
\]

Then

\[
\boxed{
|Q_q(T)|
=\frac{1+o(1)}{\sqrt2\,\pi d}
}
\tag{1}
\]

and

\[
\boxed{
Q_r(T)=1+O(d^{-1}).
}
\tag{2}
\]

Thus the order-one two-sided transition found in `PL-396` is genuinely a **fixed-gap** phenomenon. Once `d` grows while remaining `o(r)`, the larger mode is pushed `d` transition widths into the complementary-error-function tail and its continuation coefficient decays algebraically like `1/d`.

This closes the most immediate version of the escape proposed in `PL-398`: allowing `d` to acquire an increasing prime support does not preserve the order-one overlap of the continuation kernel. Any arithmetic coupling that relies on the newly available prime factors of `d` must compensate at least this `1/d` analytic penalty while still supplying an independently controlled sign, positivity, cancellation, trace, or zero-sensitive mechanism.

The result is a route restriction, not an RH mechanism and not a new theorem about incomplete gamma functions.

## 1. Uniform transition variable in the mesoscopic-gap regime

Use the exact notation already justified in `PL-396`:

\[
a=\frac{s}{2},
\qquad
z_n=\pi i n^2,
\qquad
\lambda_n=\frac{z_n}{a}=\frac{2\pi i n^2}{s},
\]

and define `eta` by

\[
\frac12\eta^2=\lambda-1-\log\lambda,
\qquad
\eta\sim\lambda-1
\quad(\lambda\to1).
\tag{3}
\]

The uniform incomplete-gamma expansion is

\[
Q(a,z)
=
\frac12\operatorname{erfc}\!\left(\eta\sqrt{a/2}\right)
+
\frac{e^{-a\eta^2/2}}{\sqrt{2\pi a}}
\{c_0(\eta)+O(a^{-1})\},
\tag{4}
\]

with `c_0` regular at `eta=0`. This is the same expansion used in `PL-396`; DLMF §8.12 gives the corresponding uniform formula and the removable singularity of the coefficient functions at the transition.

Put

\[
\delta=\frac dr,
\qquad
L=\frac qr=1+\delta.
\]

Because `d=o(r)`, one has `delta->0`. At `T=2 pi r q`, direct expansion of the exact quotient gives

\[
\lambda_q
=L+\frac{i}{4\pi r^2}+O(r^{-4}),
\tag{5}
\]

uniformly in this regime. For

\[
f(\lambda)=\lambda-1-\log\lambda,
\]

we have

\[
f(L)=\frac{\delta^2}{2}+O(\delta^3),
\qquad
\eta_q=\delta\{1+O(\delta)\}+O(r^{-2}).
\tag{6}
\]

Define the transition variable

\[
y_q:=\eta_q\sqrt{a/2}.
\tag{7}
\]

Since `|a|=pi r q(1+o(1))`, (6) implies

\[
|y_q|
=\sqrt{\frac\pi2}\,d\{1+o(1)\},
\qquad
\arg y_q=\frac\pi4+o(1).
\tag{8}
\]

The fact that the argument tends to `pi/4` matters: this is a Stokes-direction geometry where the large-`erfc` tail is algebraic in magnitude rather than exponentially small.

## 2. The exponential factor has bounded modulus

To use the large-argument `erfc` expansion one must control the apparently dangerous factor `e^{-y_q^2}`. From (3) and (7),

\[
y_q^2=a f(\lambda_q).
\tag{9}
\]

The real part of `f(L)` is `O(delta^2)`. The small imaginary displacement in (5) contributes

\[
\Im f(\lambda_q)
=O\!\left(\frac{\delta}{r^2}\right),
\]

because `f'(L)=1-L^{-1}=O(delta)`. Since `Re(a)=1/4` and `Im(a)=pi r q=Theta(r^2)`, (9) gives

\[
\Re(y_q^2)=O(\delta)=o(1).
\tag{10}
\]

Consequently

\[
|e^{-y_q^2}|=1+o(1).
\tag{11}
\]

This rules out an exponential gain or loss hidden in the complex complementary-error-function direction. The tail is genuinely of reciprocal-distance size.

## 3. The larger-mode coefficient is `1/d`

DLMF §7.12 gives, uniformly in a closed subsector containing `arg y=pi/4`,

\[
\operatorname{erfc}(y)
=
\frac{e^{-y^2}}{\sqrt\pi\,y}
\left\{1+O(|y|^{-2})\right\}.
\tag{12}
\]

Applying (8)--(11),

\[
\left|
\frac12\operatorname{erfc}(y_q)
\right|
=
\frac{1+o(1)}{2\sqrt\pi\,|y_q|}
=
\frac{1+o(1)}{\sqrt2\,\pi d}.
\tag{13}
\]

The correction term in (4) is `O(r^{-1})`: `eta_q->0`, so `c_0(eta_q)` stays bounded, `|a|^{-1/2}=Theta(r^{-1})`, and (11) controls its exponential factor. Since `d=o(r)`,

\[
r^{-1}=o(d^{-1}).
\]

Therefore (13) yields (1).

For the smaller member, the same calculation gives

\[
y_r
=-d\sqrt{\frac{\pi i}{2}}\{1+o(1)\}.
\]

Rather than use the `erfc` expansion on the opposite Stokes boundary directly, use the exact identity

\[
\operatorname{erfc}(y_r)
=2-\operatorname{erfc}(-y_r).
\]

Now `-y_r` approaches the same `pi/4` ray as `y_q`, so (12) gives

\[
Q_r(T)=1+O(d^{-1})+O(r^{-1})=1+O(d^{-1}),
\]

which is (2).

## 4. Scale interpretation

The same conclusion follows geometrically from the transition scales isolated in `PL-396`. For mode `q`, the incomplete-gamma transition is centered at

\[
t_q=2\pi q^2.
\]

The pair saddle is at

\[
T=2\pi rq.
\]

Their separation is

\[
t_q-T
=2\pi q(q-r)
=2\pi qd.
\tag{14}
\]

The transition width is `Theta(q)`. Hence, measured in transition widths,

\[
\frac{t_q-T}{q}=2\pi d.
\tag{15}
\]

For fixed `d`, this is the order-one coalescing saddle/transition layer of `PL-396` and `PL-397`. For `d->infinity`, the saddle moves arbitrarily many transition widths into the tail. Equation (1) supplies the complex-Stokes asymptotic rate: the loss is `1/d`, not an exponential cutoff.

This bridges the two regimes already stored in `PL-396`: fixed `d` has an order-one limiting coefficient, whereas ratio separation `q/r->c>1` suppresses the larger mode. The mesoscopic range

\[
1\ll d\ll r
\]

now has an explicit interpolation law at the nominal saddle.

## 5. Consequence for exponent-lattice couplings

`PL-398` showed that at fixed `d`

\[
v(r)\wedge v(r+d)=v(\gcd(r,d)),
\]

so the meet sees only the finite prime support of `d`. A natural attempted escape was therefore to let `d` grow, allowing more prime coordinates to enter through `v(d)`.

Equations (1)--(2) expose the tradeoff:

- keeping `d=O(1)` preserves order-one continuation overlap but freezes the meet into a finite divisor alphabet;
- letting `d->infinity` can enlarge the arithmetic support of `d`, but the larger-mode continuation coefficient loses a factor `Theta(1/d)` at the pair saddle.

The second statement does **not** prove that every growing-gap arithmetic mechanism dies. A weight depending on `v(d)`, `v(r)`, and `v(r+d)` can itself grow or can be aggregated over many gaps. The durable restriction is that such a proposal cannot count the expanding prime support as free new information: it must show a quantitatively controlled arithmetic gain that survives the `1/d` continuation tail and the subsequent signed summation.

In particular, this finding does not touch hard shifted correlations such as

\[
\mu(r)\mu(r+d),
\qquad
\Lambda(r)\Lambda(r+d),
\]

except to impose the analytic coefficient with which they would enter this particular continuation channel.

## 6. Prior-art and novelty audit

No theorem-level novelty in incomplete-gamma asymptotics is claimed. Paris--Cang provide the exact absolutely convergent zeta representation used in `PL-396`; Paris (2022) explicitly develops its uniform complementary-error-function smoothing. DLMF §8.12 records the standard transition variable and uniform `Q(a,z)` expansion, while DLMF §7.12 records the large-complex-argument asymptotic of `erfc` used in (12).

Targeted searches for Riemann--Siegel/incomplete-gamma work involving fixed or growing additive pair gaps, near-diagonal `q-r`, and this saddle/transition scaling returned the classical smoothing literature but no source assigning an RH mechanism to the `d->infinity, d=o(r)` tail. Accordingly, (1) is stored only as a **line-specific derived route restriction** obtained by applying standard special-function asymptotics to the growing-gap escape explicitly left open by `PL-398`.

### Sources

1. `PL-396`, which records the exact Paris--Cang continuation formula, the normalization of `lambda` and `eta`, and the uniform transition expansion used here.
2. R. B. Paris and S. Cang, “An asymptotic representation for `zeta(1/2+it)`,” *Methods and Applications of Analysis* **4**(4) (1997), 449--470. Full text: https://intlpress.com/site/pub/files/_fulltext/journals/maa/1997/0004/0004/MAA-1997-0004-0004-a006.pdf.
3. R. B. Paris, “An asymptotic approximation for the Riemann zeta function revisited,” arXiv:2203.07863 (2022). https://arxiv.org/abs/2203.07863.
4. NIST Digital Library of Mathematical Functions, §8.12, “Uniform Asymptotic Expansions for Large Parameter,” especially (8.12.1)--(8.12.4) and the regularity statement around (8.12.9)--(8.12.11): https://dlmf.nist.gov/8.12.
5. NIST Digital Library of Mathematical Functions, §7.12(i), “Complementary Error Function,” especially (7.12.1): https://dlmf.nist.gov/7.12.

## 7. Adversarial boundaries and falsification tests

1. **The regime is mesoscopic, not arbitrary.** The derivation assumes `d->infinity` and `d=o(r)`. It does not claim uniformity through `d asymp r`; `PL-396` already treats ratio-separated pairs qualitatively.

2. **The height is the nominal pair saddle.** Equation (1) is evaluated at `T=2 pi r(r+d)`. A coupled observable may integrate over a moving height window; any such construction must redo the joint saddle/transition analysis rather than transplant (1) blindly.

3. **The decay is algebraic, not exponential.** The transition argument tends to the `pi/4` complex ray, and (10) keeps `|e^{-y^2}|` asymptotically one. Any claim of Gaussian `e^{-c d^2}` suppression in this geometry is wrong.

4. **The incomplete-gamma correction is subordinate only because `d=o(r)`.** It is `O(r^{-1})`, which is `o(d^{-1})` in the stated regime. Dropping this relation would invalidate the asymptotic comparison.

5. **No total pair contribution is asserted.** The exact continued zeta expression contains phases, the reflected channel, and an archimedean correction. Equation (1) controls the larger-mode continuation coefficient. A proposed bilinear or trace observable must show how that coefficient actually enters its invariant completed quantity.

6. **Arithmetic compensation remains possible.** This finding rules out a free growing-gap escape, not all growing-gap mechanisms. A genuine counterexample to the route restriction would be an independently controlled arithmetic coupling whose completed contribution stays order one or larger after the `1/d` coefficient and all signed aggregation are included.

7. **Matched-control gate remains active.** The `1/d` tail itself is purely archimedean/scalar and is reproduced by any matched energy model. Prime-specific content must come from the arithmetic weight that is coupled to it, not from the transition law.

## Research consequence

The continuation-aware frontier now has a quantitative tradeoff. **Fixed additive gaps give order-one transition overlap but only finite gap-supported meet geometry; growing mesoscopic gaps can expose an expanding gap factorization, but the larger-mode continuation coefficient decays as `1/d`.**

This removes the simplest idea that one can recover an unbounded set of prime directions merely by letting the fixed-gap parameter drift slowly with the saddle while retaining the `PL-397` order-one kernel. A viable next mechanism must instead demonstrate arithmetic amplification/cancellation strong enough to survive this tail, or use a separate-vector coupling whose factor sensitivity is not purchased solely by increasing the gap support.