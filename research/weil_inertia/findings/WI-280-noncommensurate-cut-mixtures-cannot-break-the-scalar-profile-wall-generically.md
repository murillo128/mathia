# WI-280 — noncommensurate cut mixtures cannot break the scalar-profile wall generically

## Status

- **Evidence:** `EXACT-DERIVED + DECISIVE-NEGATIVE + HILBERT-CUT-GEOMETRY + PRIOR-ART-AUDITED`.
- **Scope:** closes a generic continuation left open after `WI-278` and `WI-279`. Allowing an arbitrary finite family of **noncommensurate** cut shifts does not by itself evade the scalar-profile ceiling. Any reserve obtained by taking a nonnegative linear combination of the firstness inequalities and then bounding the corresponding cut covariance using only abstract PSD/null-partition geometry is bounded by `sup_{0<r<a} r lambda_r`. Hence `WI-278`'s scalar counterprofile still stays below the one-signed archimedean budget for the whole arbitrary-shift linear-covariance architecture.
- **What it does not claim:** this does not rule out a genuinely source-specific noncommensurate compatibility law for the actual Suzuki null mode, a nonlinear joint constraint involving several shifts, a stronger numerator using the exact source equation, nodal/regularity information, or any argument outside the positive linear mixture considered here. In particular it does not prove RH and does not show that the actual cut covariances realize the generic countergeometry.
- **Novelty boundary:** translation covariance, Rayleigh bounds, and finite signed combinations of shifts are classical Hilbert-space/operator theory. `WI-276`--`WI-279` already establish the one-shift, commensurate Toeplitz, and oriented Hilbert-cut versions in this line. The new line-local deduction is the exact arbitrary-shift ceiling and the two-pulse null-partition witness showing that noncommensurability alone cannot make the covariance coefficient positive. No priority claim is made.

## Claim

Assume RH is false and use the first unrestricted crossing notation of `WI-279`:

\[
a=a_*:=\inf\{r>0:\lambda_r\le0\},
\qquad q_a\ge0,
\qquad \|v\|_2=1,
\qquad q_a(v)=0.
\tag{1}
\]

Let

\[
G_s=[v\mathbf1_{(-a,s)}]\in\mathcal H_q,
\qquad
\mathcal S_v=\int_{\mathbb R}\|G_s\|_q^2\,ds,
\tag{2}
\]

and

\[
C(h)=\int_{\mathbb R}\langle G_s,G_{s+h}\rangle_q\,ds.
\tag{3}
\]

`WI-279` proves the exact identity

\[
\mathcal F_v(r)=\mathcal S_v-C(2r)
\tag{4}
\]

and firstness gives

\[
\mathcal F_v(r)\ge r\lambda_r
\qquad(0<r<a).
\tag{5}
\]

Choose an arbitrary finite set of radii

\[
0<r_1,\ldots,r_m<a
\tag{6}
\]

with no commensurability assumption, and nonnegative weights `alpha_j`, not all zero. After combining duplicate radii, put

\[
A=\sum_{j=1}^m\alpha_j,
\qquad
N=\sum_{j=1}^m\alpha_j r_j\lambda_{r_j},
\qquad
M=\sup_{0<r<a}r\lambda_r.
\tag{7}
\]

Suppose a covariance step derived only from generic Hilbert cut geometry has the form

\[
\sum_j\alpha_j C(2r_j)\ge \eta\,\mathcal S_v
\tag{8}
\]

with a coefficient `eta` valid for every abstract PSD null-partition/cut path with support in an interval of length `2a`. Then necessarily

\[
\boxed{\eta<0.}
\tag{9}
\]

More quantitatively, for every index `j_0` with `alpha_{j_0}>0`, the generic coefficient obeys

\[
\boxed{\eta\le-\frac{\alpha_{j_0}}2.}
\tag{10}
\]

Consequently (4)--(5) and (8) can yield at most

\[
\mathcal S_v
\ge
\frac{N}{A-\eta}
<\frac{N}{A}
\le M.
\tag{11}
\]

Thus **no finite nonnegative linear mixture of arbitrary cut shifts can beat the scalar-profile ceiling `M` unless one proves additional information about the actual Suzuki cut path that excludes the generic two-pulse covariance geometry or strengthens the numerator beyond `r lambda_r`.**

Combining this with `WI-278`, whose explicit profile satisfies

\[
M<\frac1{20}<K_+,
\tag{12}
\]

shows that the currently certified scalar profile constraints cannot force the one-signed source reserve past the positive archimedean budget merely by replacing commensurate Toeplitz shifts with arbitrary noncommensurate shifts.

## 1. Arbitrary shifts enter the firstness inequality only through one weighted covariance

Multiply (4)--(5) by `alpha_j` and sum. This gives exactly

\[
N
\le
A\mathcal S_v
-
\sum_j\alpha_j C(2r_j).
\tag{13}
\]

If a generic covariance lower bound (8) is available, then

\[
N\le(A-\eta)\mathcal S_v,
\tag{14}
\]

which is the reserve in (11). No lattice or commensurability has been used. The only possible way for this positive linear mixture to beat the weighted scalar average `N/A` is therefore to have a **strictly positive** universal covariance coefficient `eta`.

The rest of the argument shows that abstract PSD/null-partition geometry allows the opposite sign for every finite shift family.

## 2. A two-pulse cut path makes one selected covariance strictly negative and all others zero

Write

\[
h_j=2r_j\in(0,2a).
\tag{15}
\]

Fix an index `j_0` with `alpha_{j_0}>0` and put `h=h_{j_0}`. Because the shift family is finite and duplicate shifts were combined, choose a nonempty interval `I` so short that

\[
I,\quad I+h
\tag{16}
\]

lie inside `(-a,a)` and no translate by any `h_j\ne h` creates an overlap among the two intervals. Concretely, it is enough to choose its length smaller than

\[
\min\left(
\min_j h_j,
\min_{h_j\ne h}|h_j-h|,
2a-h
\right)
\tag{17}
\]

after translating `I` into the available interior. Let `g` be a nonzero real smooth function supported in `I`, and in a one-dimensional real Hilbert space define

\[
G(s)=g(s)\xi-g(s-h)\xi,
\qquad \|\xi\|=1.
\tag{18}
\]

The two pulses have opposite orientation. Their energy is

\[
\mathcal S=\int\|G(s)\|^2ds
=2\|g\|_2^2.
\tag{19}
\]

At the selected shift,

\[
C_G(h)
=\int\langle G(s),G(s+h)\rangle ds
=-\|g\|_2^2
=-\frac12\mathcal S.
\tag{20}
\]

By the separation in (17), every other chosen shift has zero covariance:

\[
C_G(h_j)=0
\qquad(h_j\ne h).
\tag{21}
\]

Therefore

\[
\sum_j\alpha_jC_G(h_j)
=-\frac{\alpha_{j_0}}2\mathcal S.
\tag{22}
\]

Any coefficient `eta` valid for the whole generic cut-path class must satisfy (10), proving (9).

This is not merely an arbitrary function inserted into a covariance formula. The path (18) is realizable by an abstract PSD null-partition model of exactly the kind used to calibrate `WI-279`. For example, take the rank-one translation-invariant positive form

\[
q(u)=\left|\int_{\mathbb R}u(x)dx\right|^2
\tag{23}
\]

on compactly supported `L^2` functions and choose

\[
v=G'.
\tag{24}
\]

Then `v` is smooth and compactly supported, `\int v=0`, hence `q(v)=0`, while the cumulative cut class is

\[
[v\mathbf1_{(-\infty,s)}]=G(s)\xi.
\tag{25}
\]

Thus the negative covariance in (22) survives the null-sum and PSD requirements. It is excluded only by information beyond generic Hilbert cut geometry.

## 3. The scalar-profile ceiling follows immediately

At a first crossing, `lambda_r>0` for `r<a`, so `N>0`. From (10), every generic coefficient in (8) has `eta<0`; hence

\[
A-\eta>A.
\tag{26}
\]

Also, by the definition of `M`,

\[
N
=\sum_j\alpha_jr_j\lambda_{r_j}
\le
M\sum_j\alpha_j
=MA.
\tag{27}
\]

Substituting (26)--(27) into (14) proves (11).

The point is structural. Commensurability in `WI-277` and `WI-279` made the covariance coefficient computable by a finite Toeplitz matrix. Removing commensurability changes the operator used to estimate the covariance, but it does not change the sign obstruction: a finite family of shifts always admits a compact two-pulse cut path with negative weighted covariance. Therefore a generic arbitrary-shift spectral coefficient cannot turn the scalar numerator into a reserve larger than `M`.

## 4. Relation to the WI-278 wall

`WI-278` constructs a continuous strictly decreasing first-crossing profile compatible with every scalar profile constraint used in the current program, including Suzuki's small-aperture asymptotic and the certified compact-window data, while satisfying

\[
\sup_{0<r<1}r\widetilde\lambda(r)
<\frac1{20}<K_+.
\tag{28}
\]

That finding explicitly closed the harmonic reserve and every fixed **commensurate** nonnegative Toeplitz reserve then available. `WI-279` retained the signed Hilbert orientation and replaced the top Toeplitz eigenvalue by the stronger bottom eigenvalue, but its numerator remained a positive combination of `r lambda_r`, so the same scalar wall survived.

The present argument removes commensurability from that conclusion for the entire positive linear covariance architecture. For the counterprofile in `WI-278`, every reserve of the form (14), regardless of the finite radii selected, remains below `1/20` and hence below `K_+`.

This does **not** close the source-specific noncommensurate direction named in `WI-278`. Rather, it identifies exactly what the word *source-specific* must buy. A successful continuation must prove that the actual Suzuki cut path cannot realize the two-pulse anti-covariance geometry, force a positive weighted covariance by the prime/archimedean source equation, replace the scalar numerator `r lambda_r` by a stronger source-conditioned quantity, or use a genuinely nonlinear compatibility constraint not reducible to (13)--(14).

## 5. Prior-art and novelty audit

The Hilbert-space ingredients are classical. `WI-276` anchors Haagerup--de la Harpe's nilpotent numerical-radius theorem for the one-shift compact-support problem; `WI-277` audits finite/truncated Toeplitz theory for commensurate shift polynomials; and `WI-279` already records that tensoring finite real symmetric shift matrices with a Hilbert identity introduces no new operator-theoretic theorem. Finite sums of translations and their covariance quadratic forms are standard Fourier/operator theory.

A fresh targeted search for finite sums of translation operators, noncommensurate/quasiperiodic shift covariances, numerical ranges, and Hilbert-valued autocorrelation inequalities located generic almost-periodic and translation-operator frameworks, but no source coupling those generic facts to Suzuki's localized Weil first-crossing cut path. Search absence is audit context only and is not a priority claim.

The Mathia-specific content is the boundary statement (9)--(11): after `WI-278`--`WI-279`, **noncommensurability alone is not an escape hatch**. The explicit two-pulse null-partition realization (18)--(25) shows why. Any improvement must consume actual source/eigenfunction information, not merely a denser or irrational family of generic cut shifts.

## Audit and falsification tests

A falsification must locate an error in at least one load-bearing point:

1. the exact first-crossing identity `F_v(r)=S_v-C(2r)` or lower bound `F_v(r)>=r lambda_r` imported from `WI-279`;
2. the finite separation choice (17) for arbitrary distinct shifts in `(0,2a)`;
3. the covariance calculation (19)--(22), especially the factor `1/2`;
4. the realization (23)--(25) as a PSD null cumulative-cut path rather than a free covariance function;
5. the implication that any covariance coefficient using only that generic path class must satisfy `eta<=-alpha_j/2`;
6. the scalar averaging step `N/A<=sup r lambda_r`.

The theorem is intentionally narrow about proof architecture. A source-specific theorem proving `sum alpha_j C(2r_j)>0` for the **actual** Suzuki null mode would not contradict this finding; it would supply precisely the missing information that the generic countermodel lacks.

## Consequence for the research line

The generic `more shifts / irrational shifts / denser shift family` continuation is closed as a route around the `WI-278` budget wall. The live noncommensurate question is now sharper: derive an exact compatibility law from Suzuki's signed prime-plus-archimedean source that forbids the two-pulse negative-covariance pattern for the actual first null mode, or abandon linear covariance reserves and use a different invariant. This keeps the research frontier on source/eigenfunction structure rather than further scalar-profile or generic shift optimization.
