# PF-271 — separated propagation only needs sublinear low-output leakage

**Status:** `EXACT-DERIVED + DYADIC-SPECTRAL-REDUCTION + GRAPH-LOCALITY-WEAKENING + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-269-pre-propagation-robin-smoothing-is-an-overstrong-gate|PF-269]] shows that the normalized Robin boundary conversion need not smooth before propagation, while [[research/prime_flute/findings/PF-270-post-propagation-smoothing-needs-only-one-sided-graph-locality|PF-270]] gives a clean sufficient replacement: if the complete pre-separation conversion `B` preserves a positive graph scale,

\[
K^{-q}BK^q\in\mathcal B
\]

for some `q>1`, and the far leg pays the same `q` derivatives, then the composed map has the `R>1` regularity required by PF-243.

That criterion is still stronger than the composition actually needs. Positive separation already pays for output that remains at any sufficiently large transverse scale. The only dangerous part of `B` is the part that sends an input shell near `\Lambda` into an output window that grows **sublinearly** in `\Lambda`; for genuinely exponential propagation, the dangerous window can be reduced to order `\log\Lambda`.

The reduction is elementary but useful. If the far leg is smoothing of arbitrary polynomial order, it is enough to prove, for one `0<\theta<1`,

\[
\left\|
\mathbf 1_{[\kappa,\Lambda^\theta]}(K)
B
\mathbf 1_{[\Lambda,2\Lambda)}(K)
\right\|
\lesssim
\Lambda^{-R-\varepsilon}.
\tag{1}
\]

No estimate is required on conversion from `\Lambda` to comparable output scales: the far leg absorbs it. If the far leg is the exact spectral propagator `e^{-dK}`, it is enough to replace `\Lambda^\theta` by `A\log\Lambda`, with `dA>R`, and a bounded composed map necessarily forces quantitative decay into every smaller logarithmic window.

Thus PF-244 and PF-268 fall on opposite sides of the correct discriminator. PF-244's high-to-fixed-low mixer violates the necessary leakage condition. PF-268's `N^{-2}` floor lives on proportional high-high blocks and therefore does **not** obstruct a separated composition. The next Prime-Flute test should target truly low spectral leakage of the actual Robin/reflection conversion, not full graph-domain invariance.

## Claim

Let `K\ge\kappa I>0` be self-adjoint on a Hilbert space `H`, let `B\in\mathcal B(H)`, and fix `Z\ge\max\{1,\kappa\}`. For `j\ge0` set

\[
\Lambda_j=2^j Z,
\qquad
E_j=\mathbf 1_{[\Lambda_j,2\Lambda_j)}(K).
\tag{2}
\]

### A. Arbitrary-order far smoothing

Let `P:H\to G` be bounded into another Hilbert space and suppose that, for every exponent needed below,

\[
PK^p\in\mathcal B(H,G).
\tag{3}
\]

Fix `R\ge0`. Suppose there are `\theta\in(0,1)` and `\varepsilon>0` such that

\[
\boxed{
\left\|F_jBE_j\right\|
\le C\Lambda_j^{-R-\varepsilon},
\qquad
F_j:=\mathbf 1_{[\kappa,\Lambda_j^\theta]}(K),
}
\tag{4}
\]

uniformly in `j`. Then

\[
\boxed{
PBK^R\mathbf 1_{[Z,\infty)}(K)\in\mathcal B(H,G).
}
\tag{5}
\]

It is enough in (3) to have one exponent `p` satisfying `\theta p>R`.

### B. Exponential far smoothing

Assume instead that the far leg satisfies the spectral tail estimate

\[
\boxed{
\|P\mathbf 1_{[M,\infty)}(K)\|
\le C_0e^{-dM}
\qquad(M\ge\kappa)
}
\tag{6}
\]

for some `d>0`. Fix `R\ge0` and choose `A>R/d`. If, for some `\varepsilon>0`,

\[
\boxed{
\left\|L_jBE_j\right\|
\le C\Lambda_j^{-R-\varepsilon},
\qquad
L_j:=\mathbf 1_{[\kappa,A\log\Lambda_j]}(K),
}
\tag{7}
\]

for all sufficiently large `j`, then (5) again holds.

For the exact propagator `P=e^{-dK}`, boundedness of

\[
T_R:=e^{-dK}BK^R\mathbf 1_{[Z,\infty)}(K)
\tag{8}
\]

also has a converse leakage consequence. For every function `M(\Lambda)\ge\kappa`,

\[
\boxed{
\left\|
\mathbf 1_{[\kappa,M(\Lambda)]}(K)
B
\mathbf 1_{[\Lambda,2\Lambda)}(K)
\right\|
\le
2^R\|T_R\|e^{dM(\Lambda)}\Lambda^{-R}.
}
\tag{9}
\]

In particular, for `M(\Lambda)=A\log\Lambda` with `0<A<R/d`,

\[
\boxed{
\left\|
\mathbf 1_{[\kappa,A\log\Lambda]}(K)
B
\mathbf 1_{[\Lambda,2\Lambda)}(K)
\right\|
\lesssim
\Lambda^{-(R-dA)}.
}
\tag{10}
\]

For every fixed output window `M`, equation (9) forces the full `\Lambda^{-R}` high-to-low decay, up to a fixed constant.

### C. PF-270 graph locality is sufficient but not necessary for this reduction

If

\[
K^{-q}BK^q\in\mathcal B
\tag{11}
\]

for some `q>R`, then for every

\[
0<\theta<1-\frac Rq
\tag{12}
\]

one has

\[
\|F_jBE_j\|
\lesssim
\Lambda_j^{-q(1-\theta)},
\tag{13}
\]

so (4) holds with positive room. Therefore PF-270 is recovered as a convenient sufficient route whenever the far leg pays enough derivatives.

The converse is false at the level of this reduction: (4) controls only the spectral sector that can outrun the later propagation. It places no restriction on `B` between comparable high-frequency shells, and it allows behavior there that can violate the global conjugation (11).

## 1. Dyadic proof of the arbitrary-order criterion

Write

\[
T_j:=PBK^RE_j.
\tag{14}
\]

Since the `E_j` are orthogonal and sum to the high spectral projection, it is enough to prove the stronger estimate

\[
\sum_{j\ge0}\|T_j\|<\infty.
\tag{15}
\]

Split the output of `B` at the sublinear scale,

\[
I=F_j+(I-F_j).
\tag{16}
\]

For the low-output part, (4) and

\[
\|K^RE_j\|\le(2\Lambda_j)^R
\tag{17}
\]

give

\[
\|PF_jBK^RE_j\|
\le
\|P\|C2^R\Lambda_j^{-\varepsilon}.
\tag{18}
\]

The right side is summable in `j`.

For the complementary output choose any `p` with `\theta p>R`. Because `K` commutes with `F_j`,

\[
P(I-F_j)
=(PK^p)K^{-p}(I-F_j),
\tag{19}
\]

and hence

\[
\begin{aligned}
\|P(I-F_j)BK^RE_j\|
&\le
\|PK^p\|\,
\|K^{-p}(I-F_j)\|\,
\|B\|\,
\|K^RE_j\|\\
&\le
C_p\|B\|2^R\Lambda_j^{R-\theta p}.
\end{aligned}
\tag{20}
\]

This is also summable because `R-\theta p<0`. Equations (18)--(20) prove (15) and therefore (5).

The proof shows exactly what is being spent. Strong far smoothing handles all output above `\Lambda^\theta`; only conversion below that moving window needs an independent high-to-low estimate.

## 2. Exponential propagation reduces the dangerous window to logarithmic size

Under (6), split instead at

\[
M_j=A\log\Lambda_j,
\qquad
L_j=\mathbf 1_{[\kappa,M_j]}(K).
\tag{21}
\]

The low part is again bounded by a constant times `\Lambda_j^{-\varepsilon}`. For the high part, (6) gives

\[
\begin{aligned}
\|P(I-L_j)BK^RE_j\|
&\le
C_0e^{-dM_j}\|B\|(2\Lambda_j)^R\\
&=
C_0\|B\|2^R\Lambda_j^{R-dA}.
\end{aligned}
\tag{22}
\]

Since `dA>R`, the dyadic series is summable. This proves the exponential version.

The logarithm is not cosmetic. It is the scale at which an exponential output penalty and a polynomial input weight balance:

\[
e^{-dM}\Lambda^R\asymp1
\quad\Longleftrightarrow\quad
M\asymp\frac Rd\log\Lambda.
\tag{23}
\]

Output substantially above this scale is automatically affordable. The only route-killing conversion is leakage below it.

## 3. Exact propagators force low-window decay

Assume now `P=e^{-dK}` and (8) is bounded. Let

\[
F_{\Lambda,M}=\mathbf 1_{[\kappa,M]}(K),
\qquad
E_\Lambda=\mathbf 1_{[\Lambda,2\Lambda)}(K).
\tag{24}
\]

On the range of `F_{\Lambda,M}`, `e^{dK}` is bounded by `e^{dM}`. On the range of `E_\Lambda`,

\[
\|K^{-R}E_\Lambda\|\le\Lambda^{-R}.
\tag{25}
\]

Therefore

\[
F_{\Lambda,M}BE_\Lambda
=
e^{dK}F_{\Lambda,M}
\,F_{\Lambda,M}T_RE_\Lambda\,
K^{-R}E_\Lambda,
\tag{26}
\]

and taking norms proves (9). Equation (10) is immediate.

Thus the same composition that makes global graph locality unnecessary still imposes a sharp qualitative obligation: sufficiently high input cannot retain order-one mass in a fixed or slowly growing low-output spectral sector. PF-244 violates precisely this obligation.

## 4. Relation to PF-268 and PF-270

PF-268 proves a lower floor of order `N^{-2}` on proportional blocks

\[
i\asymp N,
\qquad
j\asymp N.
\tag{27}
\]

For every fixed `\theta<1`, those output indices eventually lie in the complementary region `i>N^\theta`. Hence PF-268 is invisible to the low-output condition (4). This is exactly as it should be: once the output remains of order `N`, any genuinely separated all-order Poisson propagation can pay arbitrarily many powers of the input scale.

PF-244 has the opposite geometry. Its abstract positive seam sends a sparse sequence of arbitrarily high inputs into one fixed low mode before propagation. For any `\theta>0`, the corresponding block norm in (4) stays bounded below along that sequence instead of decaying like `\Lambda^{-R-\varepsilon}`. Equations (9)--(10) show that such a mixer cannot be hidden by exact positive separation.

PF-270's graph condition controls both behaviors at once, including many spectral sectors that do not threaten the composed theorem. It remains a valuable sufficient target, especially because PF-255/PF-256 already provide `q=2` graph control for coordinate transports. But it should no longer be treated as the unique next gate for the complete actual Robin/reflection conversion.

## 5. Prime-Flute consequence

The live PF-243 target is a composed separated Robin--Poisson estimate, not a theorem about the boundary conversion by itself. If a far leg can be isolated after the last unsmoothed spectral conversion and shown to pay arbitrarily high output derivatives, the required `R>1` estimate can be obtained by proving only the sublinear leakage bound (4). If the isolated far leg has a genuine `e^{-dK_a}` spectral factor, the still smaller logarithmic window (7) is sufficient.

This changes the next discriminator. Instead of first proving

\[
K_a^{-q}B_{\rm unsmoothed}K_a^q\in\mathcal B
\tag{28}
\]

on the complete spectrum, one may attack directly

\[
\boxed{
\left\|
\mathbf 1_{[\kappa,\Lambda^\theta]}(K_a)
B_{\rm unsmoothed}
\mathbf 1_{[\Lambda,2\Lambda)}(K_a)
\right\|
\lesssim
\Lambda^{-R-\varepsilon}
}
\tag{29}
\]

for some `R>1`, `\varepsilon>0`, and one `\theta<1`, together with arbitrary-order smoothing of the remaining far leg.

This is particularly compatible with the existing exact fixed-axis Green analysis. PF-264--PF-267 become stronger as the output/input ratio tends to zero, whereas PF-268's obstruction is only on proportional high-high rays. No claim is made here that the **combined actual Robin factor** already satisfies (29); the polar/finite-seam/reflection structure still has to be inserted honestly. The point is that the relevant Green-function regime is now the strongly separated spectral cone, not the proportional cone already killed by PF-268.

For the fully sheared PF-241/PF-243 family, one must also prove the required far-leg smoothing uniformly in `t` and the canonical tail. The present result does not obtain that elliptic estimate for free.

## 6. Prior-art and novelty audit

Global off-diagonal matrix decay and its stability under inversion are classical subjects. Jaffard studies polynomially and exponentially localized infinite matrices and proves inverse-localization results:

S. Jaffard, *Propriétés des matrices « bien localisées » près de leur diagonale et quelques applications*, Annales de l'Institut Henri Poincaré C, Analyse non linéaire **7** (1990), 461--476, DOI `10.1016/S0294-1449(16)30287-6`.

Gröchenig and Klotz develop related approximation-space and inverse-closed Banach-algebra frameworks:

K. Gröchenig and A. Klotz, *Noncommutative Approximation: Inverse-Closed Subalgebras and Off-Diagonal Decay of Matrices*, Constructive Approximation **32** (2010), 429--466, DOI `10.1007/s00365-010-9101-z`.

Those works are broader localization theories; equations (4)--(10) do not claim a new matrix algebra, inverse-closedness theorem, or semigroup theorem. The proof here is a dyadic spectral split plus the spectral theorem. Its project-specific value is logical: it identifies which part of PF-270's graph-locality hypothesis is actually consumed by **later positive separation**, and turns the current Prime-Flute search from full graph invariance into a much narrower low-output leakage problem.

No novelty is claimed for dyadic decompositions, spectral projections, almost-diagonal operator methods, or exponential semigroup smoothing.

## 7. Boundaries and falsification

1. **The far leg must really smooth after the last unsmoothed conversion.** One cannot move a noncommuting Robin/reflection factor across `P` to manufacture (3) or (6).
2. **All-order smoothing is an input to part A, not a conclusion.** In the sheared long-strip/Hardy family it still has to be proved uniformly.
3. **The leakage estimate is operator-norm, not entrywise.** A large number of individually small high-to-low entries may still violate (4).
4. **The exponent has real slack.** The dyadic proof uses `\varepsilon>0` to make the shell norms summable. Endpoint refinements would require an almost-orthogonality or square-function argument not supplied here.
5. **The output window is spectral in the same `K` used for propagation.** Replacing it with a coordinate cutoff or an unrelated matched operator requires a justified comparison.
6. **PF-268 remains valid.** This finding does not restore bare finite-seam `R>1` weighting; it explains why that failure is not decisive after later propagation.
7. **PF-270 remains valid.** Its graph-locality theorem is retained as a stronger sufficient condition; only its status as the preferred route is narrowed.
8. **No global conclusion follows.** The actual Robin/reflection leakage, uniform sheared far smoothing, Hardy ends, physical `P/H` recoupling, finite-pant completion, global weak-trace reassembly, scattering/determinants, prime/clone separation, zeta zeros, and RH remain open.

## Decisive next test

For each PF-243 far leg, place the factorization boundary **after the last operator capable of changing the `K_a` spectral scale**. Then test two quantities separately: arbitrary-order output smoothing of the remaining genuinely separated propagation, and high-input leakage of the complete preceding conversion into `K_a` output below `\Lambda^\theta`, for one small fixed `\theta<1`.

If an exact `e^{-dK_a}` factor survives, sharpen the second test to the logarithmic window `K_a\le A\log\Lambda`. Use PF-264--PF-267 to attack that strongly separated regime for the fixed-axis seam before spending effort on full graph conjugation. A negative result must exhibit enough mass in this sublinear/logarithmic output window to violate (29); proportional high-high tails alone are no longer a route-level falsification.
