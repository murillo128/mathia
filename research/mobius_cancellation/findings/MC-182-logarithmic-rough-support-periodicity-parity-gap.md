# MC-182 — Logarithmic rough support is uniformly power-regular while the signed parity variance remains hard

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The live logarithmic rough Möbius target from `MC-180`--`MC-181` has an exact same-cutoff unsigned control which is substantially easier than the signed problem. This rules out rough-support irregularity itself as the missing fixed-power input.

Keep the current frontier scale

\[
H=X^\theta,
\qquad
0<\theta<1,
\qquad
y=c\log X,
\qquad
0<c<\min(\theta,1-\theta),
\tag{1}
\]

and put

\[
q=Q_y:=\prod_{p\le y}p,
\qquad
P_y:=\frac{\varphi(q)}q=\prod_{p\le y}\left(1-\frac1p\right).
\tag{2}
\]

The signed rough coefficient is

\[
g_y(n)=\mu(n)\mathbf 1_{P^-(n)>y}.
\tag{3}
\]

Forget only its sign and retain its support:

\[
\alpha_y(n):=\mathbf 1_{P^-(n)>y}
=\mathbf 1_{(n,q)=1}.
\tag{4}
\]

Thus `alpha_y` is exactly `q`-periodic. For integer `H`, write

\[
H=kq+r,
\qquad 0\le r<q,
\tag{5}
\]

and define the centered unsigned interval discrepancy

\[
D_y(x,H)
:=
\sum_{x<n\le x+H}\alpha_y(n)-HP_y.
\tag{6}
\]

Every interval containing `q` consecutive integers contains exactly `phi(q)` reduced residues modulo `q`. Hence, **pointwise for every real `x`**,

\[
\boxed{D_y(x,H)=D_y(x,r).}
\tag{7}
\]

The entire contribution of the `k` complete primorial blocks cancels against the deterministic mean. This is the exact periodicity noted for rough-number variance by Gorodetsky.

Let

\[
W_y(X,H)
:=
\int_X^{2X}|D_y(x,H)|^2\,dx.
\tag{8}
\]

For square-free `q`, Hausman--Shapiro and Montgomery--Vaughan studied the reduced-residue variance

\[
V_q(r)
:=
\frac1q\sum_{a\bmod q}
\left(
\sum_{1\le h\le r}\mathbf 1_{(a+h,q)=1}-rP_y
\right)^2.
\tag{9}
\]

Montgomery--Vaughan's classical upper bound gives

\[
\boxed{V_q(r)\le rP_y.}
\tag{10}
\]

Since `D_y(x,r)^2` is `q`-periodic in `x` and is constant between consecutive integers,

\[
\int_0^q |D_y(x,r)|^2\,dx=qV_q(r).
\tag{11}
\]

Decomposing `[X,2X]` into complete `q`-periods and at most one residual piece, then using `(7)`--`(11)`, yields

\[
\boxed{
W_y(X,H)
\le
(X+q)V_q(r)
\le
(X+q)qP_y.
}
\tag{12}
\]

The prime number theorem gives

\[
\log q=\vartheta(y)=y+o(y),
\qquad
q=X^{c+o(1)},
\tag{13}
\]

and Mertens' theorem gives `P_y=X^{o(1)}` more precisely `P_y~e^{-gamma}/log y`. Because `c<theta` and `c<1`, `(12)` becomes

\[
\boxed{
W_y(X,H)
\le
X^{1+c+o(1)}.
}
\tag{14}
\]

Compare this with the live **signed** rough-parity target of `MC-180`:

\[
V_y(X,H)
:=
\int_X^{2X}
\left|\sum_{x<n\le x+H}g_y(n)\right|^2dx
\le
X^{1+o(1)}H^{2-\eta},
\qquad 0<\eta\le1.
\tag{15}
\]

For every fixed `0<eta<=1`,

\[
\frac{W_y(X,H)}{XH^{2-\eta}}
\le
X^{c-\theta(2-\eta)+o(1)}
\le
X^{-(\theta-c)+o(1)}.
\tag{16}
\]

So the unsigned rough support satisfies a variance estimate that is **better by a fixed power of `X` than every signed fixed-power target in the current `eta<=1` family**. In particular, at the strongest endpoint `eta=1`, where the signed target is `X^{1+o(1)}H`, the unsigned support already has

\[
W_y(X,H)
\le
XH\,X^{-(\theta-c)+o(1)}.
\tag{17}
\]

Yet `MC-180` shows that a bound of the form `(15)` for the signed coefficient transfers to full Möbius variance with only subpower loss, and `MC-181` shows the logarithmic split is subpower-reversible at the same exponent level on the required dilation-stable scale families. Therefore the live difficulty cannot be attributed to where the rough numbers occur. At this cutoff, their support is already more regular than the required variance scale. **The unresolved information is the Möbius orientation `(-1)^{\omega(n)}` on that support.**

This gives a same-object, same-cutoff parity control for the current frontier: any proposed proof of `(15)` that first replaces `g_y` by `|g_y|=alpha_y` and thereafter uses only support counts, unsigned sieve weights, or their centered variance has discarded the only part not already controlled at a stronger power scale.

## 1. Exact periodic cancellation of complete primorial blocks

Equation `(4)` is elementary but decisive in this regime. An integer has no prime factor at most `y` exactly when it is coprime to the primorial `q`. Hence translation by `q` preserves `alpha_y`.

For any real `x`, the `q` integers in `(x,x+q]` form one complete residue system modulo `q`. Exactly `phi(q)` of them are coprime to `q`, so

\[
\sum_{x<n\le x+q}\alpha_y(n)=\varphi(q)=qP_y.
\tag{18}
\]

Applying `(18)` to each of the `k` complete blocks in `(5)` proves `(7)` without averaging, probability, analytic continuation, or zero information.

This is stronger than an almost-all support theorem: **at lengths larger than the primorial period, all full-period support fluctuation vanishes identically**. Only the residual window `r=H mod q` can fluctuate.

At the logarithmic cutoff, `(13)` and `c<theta` imply

\[
q=X^{c+o(1)}=o(H),
\tag{19}
\]

by a fixed power. Thus every live polynomial window contains many complete support periods even though the signed values of `g_y` across those same periods need not cancel.

## 2. Reduced-residue variance prices the remaining unsigned fluctuation

The residual discrepancy in `(7)` is exactly the classical reduced-residue counting problem modulo the square-free integer `q`. Ofir Gorodetsky, *The variance of integers without small prime factors in short intervals*, Math. Z. 308, 59 (2024), DOI `10.1007/s00209-024-03601-w`, defines the same rough indicator `alpha_y`, records its primorial period and mean, and notes the exact reduction of the variance under `H -> H-q_y`.

For the one-period problem, Gorodetsky reviews the formula of Miriam Hausman and Harold Shapiro, *On the mean square distribution of primitive roots of unity*, Comm. Pure Appl. Math. 26 (1973), 539--547, DOI `10.1002/cpa.3160260407`, and the bounds of Hugh Montgomery and Robert Vaughan, *On the distribution of reduced residues*, Ann. of Math. 123 (1986), 311--333, DOI `10.2307/1971274`. In the normalization `(9)`, the latter gives `(10)`.

Because the integrand in `(8)` is nonnegative and `q`-periodic after `(7)`, an interval of length `X` is covered by at most `X/q+1` complete periods. Equation `(11)` and the classical upper bound `(10)` then prove `(12)`. No asymptotic formula for reduced-residue variance is needed.

This distinction matters for prior art. Gorodetsky's deeper theorem gives asymptotics for unsigned rough-number variance in a nontrivial moving-parameter range. The present argument does not improve that theory and makes **no novelty claim** about primorial periodicity or reduced-residue variance. It uses the classical facts only to price the unsigned comparator at the exact logarithmic cutoff selected independently by the signed Möbius decomposition.

## 3. Why the fixed-power comparison is decisive

The key inequality is not merely that `W_y=o(H^2X)`. The signed research target already asks for a specific fixed-power saving `H^eta`, and `(16)` compares the unsigned object directly against that currency.

Because `eta<=1`, the weakest exponent on the right side of the signed target is obtained at `eta=1`:

\[
H^{2-\eta}\ge H.
\tag{20}
\]

The bootstrap condition `c<theta` already gives `q=o(H)` by a fixed power. Therefore no further tuning of the cutoff is required: the same admissible `c` from `MC-180` automatically places the unsigned support below the entire signed target family.

This closes a plausible but misleading relaxation. One might hope that proving unusually strong distribution of logarithmically rough integers in short intervals would be a first approximation to `(15)`. In the current regime that approximation is already over-solved: complete primorial blocks have exactly their expected support mass, and the residual reduced-residue variance is bounded at scale `qP_y`, not `H`.

What remains is a signed covariance problem. Writing on the rough support

\[
g_y(n)=\alpha_y(n)(-1)^{\omega(n)},
\tag{21}
\]

shows that support theory retains `alpha_y` and deletes exactly the prime-factor parity phase. The fixed-power gap `(16)` therefore measures, on the live object rather than on a generic sieve model, how much stronger the unsigned information already is without touching the required orientation.

## 4. Relationship to the classical sieve parity barrier

`MC-082` established a general control pair: the two Liouville parity classes can have the same highly accurate local divisor-density main terms while differing maximally in prime content. That is an exact incarnation of the classical sieve parity phenomenon.

The present result is narrower and closer to the active target. It does not introduce a new comparator sequence. It takes the exact logarithmically rough support of `g_y` itself and proves that its centered short-interval variance is already power-smaller than the signed variance scale being sought. Thus the generic parity warning of `MC-082` becomes a quantitative same-cutoff statement:

\[
\text{rough support fluctuation}
\quad\ll\quad
\text{required signed rough-parity scale}
\]

by a fixed power, while the signed target remains strong enough to transfer back to Mertens cancellation.

This does not forbid a sieve-flavored proof. Friedlander--Iwaniec-type parity-sensitive methods remain a legitimate model precisely because they add bilinear or harmonic information beyond unsigned support. What `(12)`--`(17)` exclude is treating **better rough-number counting itself** as the missing ingredient.

## 5. Prior-art and novelty assessment

All mathematical ingredients on the unsigned side are classical or established literature:

- `alpha_y(n)=1_{(n,q_y)=1}`, its period `q_y`, and its mean `P_y` are standard and are stated explicitly in Gorodetsky's 2024 paper;
- the one-period mean-square problem is the reduced-residue variance studied by Hausman--Shapiro and Montgomery--Vaughan;
- the bound `V_q(r)<=r phi(q)/q` is classical Montgomery--Vaughan;
- `log q_y=y+o(y)` and the asymptotic for `P_y` are standard prime-number-theorem and Mertens-theorem consequences.

Accordingly, no new theorem about rough numbers or reduced residues is claimed. The durable contribution is the **parameter and information audit against the current signed frontier**: at `y=c log X` with `c<theta`, the support period lies a fixed power below the polynomial window, so classical reduced-residue variance already beats every required `eta<=1` signed variance scale. Combined with `MC-180`--`MC-181`, this isolates parity orientation rather than rough-support distribution as the unresolved fixed-power carrier.

A targeted literature check found the precise unsigned theory rather than an unrecognized signed bridge. Gorodetsky's work studies `alpha_y`, not `mu(n) alpha_y(n)`, and the classical reduced-residue results likewise forget the Möbius sign. They therefore support the control rather than solve `(15)`.

## 6. Boundaries and falsification tests

- The exact period belongs to the **support** `alpha_y`, not to the signed function `g_y`. The values `g_y(n+q)` need not equal `g_y(n)` because prime factors larger than `y` and their parity are not determined modulo `q`.
- The clean identity `(7)` is stated for integer `H`. Replacing a real `H` by its integer part changes an interval sum and deterministic mean by only `O(1)`, which is negligible at the asymptotic scales here.
- The classical bound `(10)` controls centered reduced-residue counts. It does not imply cancellation of `sum g_y(n)` because the signed sum has no `HP_y` main term to subtract and is not determined by support occupancy.
- The fixed-power comparison uses the same bootstrap inequality `c<theta` already required by `MC-180`. If the cutoff grows so that `q_y` is comparable with or exceeds `H`, complete-period cancellation no longer yields `(16)` in this form.
- Better constants or asymptotics for `V_q(r)` do not change the research conclusion. The crude classical upper bound is already stronger than the full signed target family by a fixed power.
- The result does not prove `(15)`, a global Mertens power bound, or RH. It eliminates an unsigned relaxation of the live target.
- A proposed method survives this obstruction only if it retains a statistic depending on the sign `(-1)^{omega(n)}` or an equivalent parity-sensitive coupling and proves a bound not reducible to the support variance `(8)`.

The claim is falsified if `alpha_y` is not exactly primorial-periodic, if complete `q`-blocks fail to contain `phi(q)` support points, if the reduced-residue upper bound `(10)` is misstated, or if the exponent comparison `(16)` fails under `0<c<theta` and `0<eta<=1`.

## Consequence for the active frontier

`MC-180` moved the problem from a dense polynomial smooth remainder to one logarithmically rough signed block. `MC-181` then showed that this change of coordinates is subpower-reversible at the fixed-power variance level. The present finding removes the most obvious unsigned source-side escape: **the rough support itself already has more than enough short-interval regularity**.

The next useful theorem must therefore see orientation inside the rough block. A Type-II or bilinear decomposition is valuable only if its cross-factor statistic changes when the parity signs in `(21)` change; a support-only sieve estimate, even one with excellent variance, cannot supply the missing fixed-power gain. This narrows the live question to a phase-sensitive rough-parity estimate rather than to further improvements in unsigned rough-number distribution.