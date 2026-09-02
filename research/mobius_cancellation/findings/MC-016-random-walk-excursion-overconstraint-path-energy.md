# MC-016 — Random-walk cancellation permits quadratic excursion mass while path energy remains diffusive

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `DECISIVE-NEGATIVE`, `MATCHED-RANDOM-CONTROL`, `CANDIDATE-NEW-STRUCTURE`, `NO-NOVELTY-CLAIM`.

## Claim

The excursion-length second moment `E_2(N)` from `MC-014` is a valid sufficient statistic for mean-absolute cancellation, but it is structurally much stronger than diffusive cancellation itself. Even the canonical exact-support independent-sign model can have a macroscopic nonzero excursion, hence quadratic `E_2`, at a horizon where its mean-absolute partial-sum size is already at square-root scale.

Let `q(n)=mu(n)^2`, write the square-free positions as `r_1<r_2<...`, choose independent Rademacher signs `epsilon_j`, and define

\[
a(r_j)=\varepsilon_j,\qquad a(n)=0\quad(q(n)=0),
\tag{1}
\]

with

\[
A(k)=\sum_{n\le k}a(n).
\tag{2}
\]

Then `|a(n)|=mu(n)^2` exactly, and `MC-S10` implies that almost every realization has the full qualitative Chowla property.

For every sufficiently large `m`, put `Y_m=r_{2m}+1`. There exists a deterministic realization of (1), still with the full qualitative Chowla property, such that simultaneously

\[
\boxed{D_a(Y_m):=\frac1{Y_m}\sum_{k<Y_m}|A(k)|\le4\sqrt{Y_m}}
\tag{3}
\]

and

\[
\boxed{E_{2,a}(Y_m)\ge\frac{Y_m^2}{16}}.
\tag{4}
\]

Thus exact square-free support, qualitative Chowla, and square-root mean-absolute cancellation at the tested horizon do **not** force the excursion-square scale `E_2(N)<<N^(3/2+epsilon)`. Long excursions are not themselves evidence of poor cancellation: a diffusive recurrent walk naturally produces them.

A more cancellation-aligned exact carrier is the quadratic path energy

\[
V_a(N)=\sum_{k<N}A(k)^2.
\tag{5}
\]

It satisfies

\[
\boxed{D_a(N)^2\le\frac{V_a(N)}N},
\tag{6}
\]

while the random support-matched model has

\[
\mathbb E V_a(N)
=\sum_{k<N}Q(k)
=\left(\frac3{\pi^2}+o(1)\right)N^2,
\tag{7}
\]

where `Q(k)=sum_{n<=k}mu(n)^2`. For every fixed `epsilon>0`, almost surely

\[
V_a(N)\ll_\varepsilon N^{2+\varepsilon}.
\tag{8}
\]

Finally, if

\[
C_h(X)=\sum_{n\le X}a(n)a(n+h),
\tag{9}
\]

then exactly

\[
\boxed{
V_a(N)
=
\sum_{n=1}^{N-1}(N-n)a(n)^2
+2\sum_{h=1}^{N-2}\sum_{X=1}^{N-1-h}C_h(X).
}
\tag{10}
\]

For `a=mu`, the diagonal term is already `(3/pi^2+o(1))N^2`. The surviving arithmetic question is therefore amplitude-sensitive: can genuinely signed growing-scale correlation or multiplicative information control the full off-diagonal aggregate in (10) at `N^(2+epsilon)` scale without replacing it by the absolute-value budget that produced the logarithmic ceiling in `MC-006`?

## 1. Random-walk last return forces a macroscopic excursion

Set

\[
T_j=\sum_{i\le j}\varepsilon_i,
\qquad
Q(k)=\sum_{n\le k}q(n).
\tag{11}
\]

Then exactly `A(k)=T_{Q(k)}`. The calendar path is therefore a simple symmetric random walk in operational square-free time, stretched by deterministic gaps between square-free positions.

Let

\[
Z_{2m}=\max\{0\le j\le2m:T_j=0\}
\tag{12}
\]

be its last operational-time zero before time `2m`. The classical discrete last-return arcsine law (`MC-S23`) gives

\[
\Pr(Z_{2m}=2j)=u_{2j}u_{2m-2j},
\qquad
u_{2j}=4^{-j}\binom{2j}{j},
\tag{13}
\]

for `0<=j<=m`. By symmetry under `j -> m-j`,

\[
\Pr(Z_{2m}\le m)\ge\frac12.
\tag{14}
\]

On this event, `T_j!=0` for every `m<j<=2m`, hence

\[
A(k)\ne0\qquad(r_{m+1}\le k\le r_{2m}).
\tag{15}
\]

The square-free asymptotic `Q(x)=(6/pi^2)x+O(sqrt x)` from `MC-S12` gives `r_j~(pi^2/6)j`, so

\[
\frac{r_{2m}-r_{m+1}+1}{Y_m}\longrightarrow\frac12.
\tag{16}
\]

For all sufficiently large `m`, one calendar excursion therefore has length at least `Y_m/4`, proving (4) on an event of probability at least `1/2`.

## 2. Diffusive mean-absolute size survives the same event

For each fixed `k`, independence gives

\[
\mathbb E A(k)^2=Q(k).
\tag{17}
\]

Thus

\[
\mathbb E|A(k)|\le\sqrt{Q(k)}\le\sqrt{k},
\]

and therefore

\[
\mathbb E D_a(Y)
\le\frac1Y\sum_{k<Y}\sqrt{k}
\le\frac23\sqrt Y.
\tag{18}
\]

Markov gives

\[
\Pr(D_a(Y_m)>4\sqrt{Y_m})\le\frac16.
\tag{19}
\]

Combining (14) and (19), the long-excursion event and the diffusive-mean event intersect with probability at least `1/3`. The full qualitative Chowla event has probability one by `MC-S10`, so its intersection still has positive probability. This proves the deterministic existence statement (3)–(4).

The realization supplied by this argument may depend on `m`; no claim is made that one fixed realization satisfies (3)–(4) along infinitely many horizons.

## 3. Quadratic path energy matches the random baseline

Equation (6) is Cauchy-Schwarz. From (17),

\[
\mathbb E V_a(N)=\sum_{k<N}Q(k).
\]

Using the square-free estimate from `MC-S12`,

\[
\mathbb E V_a(N)
=\frac3{\pi^2}N^2+O(N^{3/2}),
\tag{20}
\]

which proves (7).

For fixed `epsilon>0`, Markov on dyadic scales gives

\[
\Pr(V_a(2^j)>2^{j(2+\varepsilon)})\ll2^{-j\varepsilon}.
\tag{21}
\]

The series converges. Borel-Cantelli and monotonicity of `V_a(N)` then give the almost-sure envelope (8), with a realization-dependent constant. Hence the `N^(2+epsilon)` energy budget is compatible with the same exact-support random comparator for which the `N^(3/2+epsilon)` excursion-square budget fails with constant probability at each tested operational horizon.

## 4. Exact signed-correlation form

Expanding (5), a diagonal product `a(n)^2` appears in `N-n` partial sums, while an off-diagonal product `a(n)a(n+h)` appears in `N-n-h` partial sums. Thus

\[
V_a(N)
=
\sum_{n=1}^{N-1}(N-n)a(n)^2
+2\sum_{h=1}^{N-2}\sum_{n=1}^{N-1-h}(N-n-h)a(n)a(n+h).
\tag{22}
\]

Also

\[
\sum_{X=1}^{N-1-h}C_h(X)
=
\sum_{n=1}^{N-1-h}(N-n-h)a(n)a(n+h),
\tag{23}
\]

which proves (10).

For Möbius, the diagonal is `sum_{k<N}Q(k)` and hence `(3/pi^2+o(1))N^2`. A bound

\[
V_\mu(N)\ll_\varepsilon N^{2+\varepsilon}
\tag{24}
\]

would imply the desired square-root-scale **mean-absolute** bound after renaming `epsilon` in (6). This is not established here, and no claim is made that (24) is easier than the target.

The informational distinction from `MC-006` is exact. `MC-006` controls an average of **absolute** two-point correlations and shows that this black-box norm has only logarithmic quantitative strength. Equation (10) retains signs across both shift `h` and prefix `X`. Any new gain would have to use cancellation or arithmetic consistency in this two-parameter aggregate rather than demand that each correlation be independently tiny.

## Prior art and novelty assessment

The simple-random-walk last-return arcsine law is classical; `MC-S23` is an elementary modern derivation. The support-matched random Chowla construction is already covered by Shi (`MC-S10`), and square-free density is classical (`MC-S12`). Cauchy-Schwarz, Borel-Cantelli, and (10) are elementary.

No novelty is claimed for random-walk excursion theory, second moments of partial sums, or the correlation identity in isolation. A targeted search for mean-square Mertens formulations supplied no basis for promoting (24) as a new criterion or theorem.

The durable line-specific contribution is the matched-control distinction between the two information carriers: `MC-014` proves that `E_2` is sufficient, while the present control proves that its required scale is not a generic signature of diffusive cancellation. `V_a` retains amplitude and has the expected diffusive polynomial scale in that same comparator, while exposing the signed growing-scale correlation aggregate that would require genuine arithmetic control.

## Boundaries and failure modes

This finding establishes no new bound for the actual Mertens function and does not prove RH.

- The independent-sign comparator is not multiplicative, so it does not rule out a specifically Möbius-arithmetic theorem forcing small `E_2`.
- Equation (4) kills `E_2` as a **generic cancellation-faithful or randomness-derived target**, not as a mathematically valid sufficient condition.
- The realization in (3)–(4) may depend on `m`.
- `V_a(N)<<N^(2+epsilon)` is only a sufficient energy target for mean-absolute cancellation, not a necessary characterization.
- Equation (10) is an exact rearrangement, not an independent estimate; its off-diagonal term may be as hard as the original problem unless extra arithmetic structure is exhibited.
- Taking absolute values in (10) risks recreating the information loss quantified in `MC-006`.
- The recent Pintz mean-absolute-to-zero-boundary theorem remains `NEEDS-AUDIT` in `MC-009`, so no RH implication is inferred here from the mean-absolute scale.

A decisive continuation must either derive a non-circular signed/multiplicative estimate for the off-diagonal aggregate in (10) at `N^(2+epsilon)` scale, or construct a stronger matched **multiplicative** control showing that even this amplitude-sensitive interface can remain large while the currently available local/correlation inputs hold.

## Consequences for the line

The accepted mean-absolute transfer direction is narrowed again:

- **retained as exact but overstrong:** the excursion-square sufficient condition of `MC-014`;
- **killed as a generic randomness target:** proving mean-absolute cancellation merely by making long nonzero excursions rare;
- **new exact candidate interface:** quadratic path energy `V_mu(N)` and the signed all-shift/all-prefix identity (10).

The active question is now amplitude-sensitive. A useful local-to-global mechanism must preserve the cancellation that makes a long low-amplitude excursion harmless, and must exploit more than qualitative Chowla or the entrywise absolute correlation budget already ruled too weak in `MC-006`.