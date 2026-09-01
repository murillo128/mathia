# WP-090 — Fixed positive mixtures of shifted cover resolvents cannot cancel the digamma contamination

**Status:** `EXACT-DERIVED + DECISIVE-COMPATIBILITY-OBSTRUCTION + POSITIVE-MIXTURE-RIGIDITY + MATCHED-CONTROL + CLASSICAL-INGREDIENTS`.

`WP-075` leaves a natural positive escape open. A single shifted cover-resolvent defect

\[
R_{n,c}
=
n\widetilde W_n^*(L+cI)^{-1}\widetilde W_n
-
\left(L+\frac cn I\right)^{-1}
\succeq0,
\qquad c>-\frac12,
\tag{1}
\]

has trace

\[
\tau_n(c)
=
\log n
+
\psi\!\left(\frac12+\frac cn\right)
-
\psi\!\left(\frac12+c\right).
\tag{2}
\]

For one fixed shift, exact finite Weil weight forces `c=0`; but one could try to average several positive shifts, including shifts of opposite sign, so that their degree-dependent digamma errors cancel while positivity survives by convexity.

That escape is impossible for every fixed finite positive mixture.

Let `mu` be a finite positive Borel measure on `(-1/2,infinity)`, independent of the cover degree, and define whenever finite

\[
R_{n,\mu}
:=
\int R_{n,c}\,d\mu(c)
\succeq0,
\qquad
T_\mu(n)
:=
\operatorname{Tr}R_{n,\mu}
=
\int\tau_n(c)\,d\mu(c).
\tag{3}
\]

Then the following rigidity holds.

> **Positive-mixture rigidity theorem.** If `T_mu(2)=log 2` and `T_mu(n_j)=log n_j` on any unbounded sequence of integers `n_j -> infinity`, then
> \[
> \boxed{\mu=\delta_0.}
> \tag{4}
> \]
> In particular, if the exact finite-place normalization is required on every prime,
> \[
> T_\mu(p)=\log p\qquad\text{for every prime }p,
> \tag{5}
> \]
> the only fixed positive mixture is the zero-shift defect of `WP-074`/`WP-075`.

Thus positive averaging cannot separate the two pieces of (2). Any nonzero mass at shifted resolvents retains an unavoidable finite-place contamination somewhere on the prime degrees. The only mixture preserving all exact prime coefficients has no shifted/digamma component at all.

This is stronger than the pointwise uniqueness in `WP-075`: cancellation between positive and negative shifts is allowed, arbitrary finite positive Borel mixtures are allowed, and exact matching is assumed only at degree `2` plus an unbounded degree set. No zeta zeros, analytic continuation, or RH-equivalent positivity enters the proof.

## 1. Positivity survives arbitrary fixed positive mixing

The normalized pointed-cover isometry and half-integer scale operator are those of `WP-073`--`WP-075`:

\[
\widetilde W_n e_k
=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad
L=N+\frac12 I,
\qquad
\widetilde W_n^*L\widetilde W_n=nL.
\tag{6}
\]

`WP-075` proves directly, by strict convexity of `x -> 1/x` on each cover block, that every `R_{n,c}` in (1) is positive trace class for `c>-1/2`. Hence if `T_mu(n)<infinity`, then

\[
\int \|R_{n,c}\|_1\,d\mu(c)
=
\int \operatorname{Tr}R_{n,c}\,d\mu(c)
=T_\mu(n)<\infty.
\tag{7}
\]

The trace-class integral in (3) therefore exists, is positive, and Tonelli gives the trace formula in (3). This is a genuine inherited sign theorem: no subtraction of positive operators is introduced by the mixing step.

Put

\[
\delta_n(c)
:=
\psi\!\left(\frac12+\frac cn\right)
-
\psi\!\left(\frac12+c\right),
\tag{8}
\]

so that

\[
\tau_n(c)=\log n+\delta_n(c).
\tag{9}
\]

The question is whether a fixed positive measure can make the signed scalar errors `delta_n(c)` cancel for all arithmetic degrees while retaining nonzero shifted mass.

## 2. Exact matching on an unbounded degree set forces total mixture mass one

Let

\[
M:=\mu((-1/2,\infty))<\infty.
\tag{10}
\]

For each fixed `c`,

\[
\frac{\tau_n(c)}{\log n}\longrightarrow1
\qquad(n\to\infty),
\tag{11}
\]

because `psi(1/2+c/n)` tends to `psi(1/2)` while the remaining digamma difference is independent of `n`.

To pass the limit through an arbitrary finite positive mixture, split the shifts by sign.

If `c>=0`, monotonicity of `psi` gives `delta_n(c)<=0`, while positivity of `R_{n,c}` gives `tau_n(c)>0`. Therefore

\[
0<\frac{\tau_n(c)}{\log n}\le1.
\tag{12}
\]

If `-1/2<c<0`, define

\[
h_c(x):=\psi\!\left(\frac12+cx\right),
\qquad0\le x\le1.
\tag{13}
\]

The digamma function is strictly concave on `(0,infinity)`, so `h_c` is concave; it is decreasing because `c<0` and `psi` is increasing. Hence

\[
0\le\delta_n(c)
\le h_c(0)-h_c(1).
\tag{14}
\]

Concavity at the midpoint gives

\[
h_c(1/2)
\ge\frac{h_c(0)+h_c(1)}2,
\]

or equivalently

\[
h_c(0)-h_c(1)
\le2\bigl(h_c(1/2)-h_c(1)\bigr)
=2\delta_2(c).
\tag{15}
\]

Since `T_mu(2)=log 2`, the positive function `tau_2` is integrable, and on the negative-shift sector `0<=delta_2<=tau_2`; thus `delta_2` is integrable there. For every `n>=2`, (14)--(15) yield the integrable domination

\[
0<\frac{\tau_n(c)}{\log n}
\le
1+\frac{2\delta_2(c)}{\log2}.
\tag{16}
\]

Dominated convergence applied to (11)--(16) now gives

\[
\boxed{
\frac{T_\mu(n)}{\log n}\longrightarrow M.
}
\tag{17}
\]

If `T_mu(n_j)=log n_j` on any unbounded sequence, the left side of (17) is identically one along that sequence. Therefore

\[
\boxed{M=1.}
\tag{18}
\]

So an unbounded exact normalization first forces the positive mixture to be a probability measure. No hidden rescaling remains available.

## 3. The endpoint cancellation and the degree-two cancellation force zero shift

With `M=1`, exact matching becomes

\[
\int\delta_n(c)\,d\mu(c)=0
\tag{19}
\]

for every degree at which `T_mu(n)=log n`. In particular,

\[
\boxed{
\int\delta_2(c)\,d\mu(c)=0.
}
\tag{20}
\]

Now take the unbounded matching sequence `n_j`. For `c<0`, `delta_{n_j}(c)` increases monotonically to

\[
\delta_\infty(c)
:=
\psi(1/2)-\psi(1/2+c)>0.
\tag{21}
\]

For `c>0`, `-delta_{n_j}(c)` increases monotonically to

\[
-\delta_\infty(c)
:=
\psi(1/2+c)-\psi(1/2)>0.
\tag{22}
\]

The negative-shift side is dominated by `2 delta_2` from (15), so it has finite endpoint integral. Equation (19) on the matching sequence says the positive and negative parts have equal integrals for every `j`; monotone convergence on the two sign sectors therefore gives

\[
\boxed{
\int\delta_\infty(c)\,d\mu(c)=0,
}
\tag{23}
\]

with both signed parts finite.

The decisive quantity is the midpoint concavity defect

\[
D(c)
:=
\psi\!\left(\frac12+\frac c2\right)
-
\frac12\psi\!\left(\frac12\right)
-
\frac12\psi\!\left(\frac12+c\right).
\tag{24}
\]

For every `c != 0`, the three arguments lie on a nonconstant affine segment inside `(0,infinity)`. Strict concavity of `psi` therefore gives

\[
\boxed{D(c)>0\quad(c\ne0),}
\qquad
D(0)=0.
\tag{25}
\]

But in terms of the two already-integrable cancellation defects,

\[
D(c)
=\delta_2(c)-\frac12\delta_\infty(c).
\tag{26}
\]

Equations (20) and (23) imply

\[
\int D(c)\,d\mu(c)=0.
\tag{27}
\]

A nonnegative function which is strictly positive away from `c=0` can have zero integral against a positive measure only if that measure is supported at `0`. Together with total mass one from (18),

\[
\boxed{\mu=\delta_0,}
\tag{28}
\]

proving the theorem.

The strict concavity used here is classical. NIST DLMF §5.15 records

\[
\psi'(x)=\sum_{k=0}^\infty\frac1{(k+x)^2},
\qquad x>0,
\tag{29}
\]

and differentiation gives

\[
\psi''(x)
=-2\sum_{k=0}^\infty\frac1{(k+x)^3}<0.
\tag{30}
\]

Thus the new content is not a new special-function inequality; it is the rigidity consequence of applying that classical concavity to the exact Mathia cover-resolvent trace family of `WP-075`.

## 4. Exact prime matching is already enough

The finite explicit-formula coefficient on a primitive prime ray requires

\[
(\log p)p^{-k/2}.
\tag{31}
\]

If the positive orbit Gram kernel of `WP-074` is scaled by the mixed positive trace `T_mu(p)`, its first row is

\[
T_\mu(p)p^{-k/2}.
\tag{32}
\]

Exact finite-place matching therefore requires only

\[
T_\mu(p)=\log p
\tag{33}
\]

for every prime `p`; it does **not** require a logarithmic response on all composite degrees.

The theorem was deliberately stated to respect that weaker requirement. The prime set contains `2` and is unbounded, so (33) already implies (28). Therefore the obstruction is not an artifact of imposing a stronger all-integer preprimitive law.

This also shows why matching at one or finitely many primes is not evidence. Opposite-sign shifts can be positively weighted so that their scalar errors cancel at a selected degree. What fails is simultaneous exact cancellation across the unbounded arithmetic family while keeping one fixed positive mixing law.

## 5. Prior-art and novelty audit

The mathematical ingredients are classical:

- Hansen--Pedersen operator Jensen theory is the standard noncommutative setting behind compression inequalities for operator-convex functions such as the inverse; `WP-075` in fact proves the needed positivity directly in the Hardy basis rather than relying on the abstract theorem.
- NIST DLMF §5.15 gives the polygamma series from which strict increase and strict concavity of the digamma function follow immediately.
- Positive mixtures preserving convexity/concavity are elementary measure-theoretic consequences of Jensen theory.

A targeted search across operator Jensen/compression inequalities, digamma and polygamma concavity, Gauss multiplication identities, shifted resolvent traces, and positive-measure mixtures did not locate a literature theorem asserting the specific rigidity (4) for the pointed-cover trace family (2). That absence is **not** treated as a novelty proof. The durable claim here is only the exact derived Mathia-specific obstruction: once the classical shifted-resolvent family of `WP-075` is fixed, its positive mixtures cannot preserve the exact prime logarithms unless all mass collapses to zero shift.

The result therefore classicalizes rather than upgrades the mechanism. It rules out a natural convex-combination repair inside a family whose positivity and digamma behavior are already classical functional calculus.

## 6. Matched control and sharp scope boundary

Nothing in the proof uses primality except to choose the unbounded matching set containing degree `2`. The same theorem holds for ordinary integer block covers or any matched refinement system with the trace law (2). It is a structural rigidity of this positive shifted-resolvent family, not hidden arithmetic evidence.

The theorem closes:

\[
\boxed{
\text{fixed finite positive measure over real shifts}
+\text{positive shifted cover resolvents}
+\text{exact prime log weights}
\Longrightarrow
\text{zero shift only}.
}
\tag{34}
\]

It does **not** close:

1. degree-dependent measures `mu_n` whose mixing law itself changes with the cover degree;
2. infinite-mass or non-finite mixtures for which the normalization/trace limit in (17) falls outside the theorem;
3. signed mixtures, which no longer inherit positivity from (1);
4. complex shifts, for which the individual real self-adjoint positivity theorem already fails on the critical line as noted in `WP-075`;
5. noncommutative coupling of shifted channels **before** taking the trace;
6. nonlinear scalarizations or determinants not equal to the additive trace mixture (3);
7. the nonperiodic/infinite auxiliary sectors and moving-principal-angle mechanisms left open by `WP-089`.

The first escape is particularly important: one can manufacture cancellation by allowing the mixing law to inspect `n`, just as `WP-089` exhibits a degree-dependent moving angle with determinant `1/n`. Such a construction is not forbidden here, but it must be forced by additional Mathia geometry rather than chosen to repair the target coefficient.

## Consequence for the Weil-positivity search

`WP-075` showed that a single real archimedean-like resolvent shift contaminates the finite coefficient. `WP-090` shows that **positive averaging cannot repair that incompatibility**. The whole fixed finite-mass convex cone generated by these shifted positive defects has exactly one ray whose trace agrees with all prime logarithms: the zero-shift ray.

That ray is the already-known positive finite carrier

\[
\operatorname{Tr}R_{p,0}=\log p,
\tag{35}
\]

and its digamma correction vanishes identically. Therefore this Stieltjes/resolvent direction cannot intrinsically produce both the finite-prime logarithms and a nontrivial archimedean Gamma profile merely by mixing its independently positive members.

A surviving same-structure completion must introduce genuinely new coupling before scalarization, a degree-forced moving spectral scale, an infinite/global sector, or another operation outside fixed positive shift mixtures. This leaves the core mandate unchanged but removes a natural cancellation escape from one of the strongest Mathia-native positive finite carriers.