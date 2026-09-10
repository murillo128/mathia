# PF-269 — pre-propagation Robin smoothing is an overstrong gate

**Status:** `EXACT-DERIVED + COMMUTING-CALIBRATION + NEGATIVE/OBSTRUCTION + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-268-lowest-finite-seam-pole-forbids-bare-supercritical-separated-weighting|PF-268]] shows that the bare finite-seam relative kernel cannot itself carry a supercritical separated weight: its lowest massive pole leaves proportional blocks of order `N^{-2}`, so `R>1` fails before any Robin normalization or spatial propagation is used. A natural repair was to ask whether the normalized Robin source factor from [[research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform|PF-257]] could supply the missing positive-order smoothing *before* the Poisson leg.

The exact commuting calibration from [[research/prime_flute/findings/PF-246-commuting-seam-normalizers-force-all-order-separated-robin-poisson-smoothing|PF-246]] shows that this is an overstrong intermediate gate. Take the operator-matched Robin seam

\[
Q=K
\]

on any positive unbounded transverse spectral sector. Then the PF-257 relative square-root map and normalized Robin injection are

\[
X=K^{-1/2}Q^{1/2}=I,
\qquad
B:=X(I+X^*X)^{-1}=\frac12 I.
\]

Hence for every `R>0` and every high-frequency projection `P_Z=1_{[Z,\infty)}(K)` whose range contains arbitrarily high `K`-spectrum,

\[
\boxed{BK^RP_Z=\tfrac12K^RP_Z\ \text{is unbounded}.}
\]

Nevertheless PF-246 proves that the **composed separated Robin-Poisson source-to-bulk map** for the same matched seam is smoothing of every order across every fixed positive longitudinal distance. Thus positive longitudinal propagation can supply all of the required transverse powers even when the normalized boundary injection supplies none.

The live PF-243 theorem should therefore not be factored through a global estimate `BK^RP_Z\in\mathcal B(H)` as a prerequisite. What remains load-bearing is joint control of **spectral conversion plus positive separation** for the actual noncommuting seam. PF-244 still prevents us from discarding the source factor: high input converted to genuinely low output before propagation can evade the exponential high-mode damping. The correct discriminator is therefore whether the actual normalized Robin source conversion, immediately followed by the designated separated Poisson leg and its reflection structure, suppresses all such leakage strongly enough for some `R>1`.

## Claim

Let `K>=0` be self-adjoint on a Hilbert space and assume its positive spectrum is unbounded. On the positive spectral subspace take the commuting matched seam

\[
Q=K.
\tag{1}
\]

With PF-257 notation,

\[
A_Q=(K+Q)^{-1}Q^{1/2},
\qquad
B=K^{1/2}A_Q
   =X(I+X^*X)^{-1},
\qquad
X=K^{-1/2}Q^{1/2}.
\tag{2}
\]

Then

\[
X=I,
\qquad
A_Q=\frac12K^{-1/2},
\qquad
\boxed{B=\frac12I.}
\tag{3}
\]

Consequently, for every `Z>0` for which `P_Z=1_{[Z,\infty)}(K)` has unbounded spectral support and every `R>0`,

\[
\boxed{
\|BK^RP_Z\|=\infty.
}
\tag{4}
\]

On the other hand, put this same seam at both ends of the product corridor in PF-246. Its reflection coefficients are identically zero,

\[
r_i(k)=\frac{k-q_i(k)}{k+q_i(k)}=0
\qquad(q_i(k)=k),
\tag{5}
\]

and PF-246 gives, for every fixed longitudinal separation `d>0`, every `R>=0`, and every far cutoff `chi`,

\[
\boxed{
\max\left\{
\|\chi^{1/2}\partial_XP_1K^RP_Z\|,
\|\chi^{1/2}KP_1K^RP_Z\|
\right\}<\infty.
}
\tag{6}
\]

Equations (4) and (6) hold simultaneously. Therefore a positive-order pre-propagation bound on `B` is **not a necessary intermediate condition** for arbitrarily high separated Robin-Poisson smoothing, even in an exact positive model belonging to the canonical commuting calibration.

## 1. The matched seam leaves no hidden Robin smoothing

The calculation is completely rigid. From `Q=K`,

\[
K+Q=2K,
\qquad
Q^{1/2}=K^{1/2},
\]

so on the positive spectral subspace

\[
K^{1/2}(K+Q)^{-1}Q^{1/2}
=K^{1/2}(2K)^{-1}K^{1/2}
=\frac12I.
\tag{7}
\]

The same conclusion follows from the PF-257 polar-free representation: `X=I` and `X(I+X^*X)^{-1}=1/2 I`. There is therefore no concealed Jacobi, fractional-power, or off-diagonal gain in the boundary injection that could absorb `K^R` before propagation.

This is stronger than saying that a proof of such a bound is currently missing. In the matched calibration the bound is false for every positive order.

## 2. Positive separation supplies the missing powers after the source map

PF-246 solves the commuting product-corridor problem mode by mode. When `q_i(k)=k`, both Robin reflections vanish, while the normalized boundary source coefficient is

\[
\frac{\sqrt{k}}{k+k}=\frac1{2\sqrt{k}}.
\tag{8}
\]

The far leg then carries the ordinary longitudinal factor `e^{-dk}`. PF-246's exact estimate contains

\[
\sup_{k\ge Z} k^R e^{-dk}<\infty
\tag{9}
\]

for every finite `R`. Thus the separated interior map can gain arbitrarily many transverse powers although its energy-normalized Robin boundary factor is merely the order-zero contraction `1/2 I`.

The proof architecture matters: source normalization and longitudinal propagation are not two independent regularity gates whose exponents must each be positive. They are parts of one composed operator, and the propagation factor may carry the entire high-frequency gain on channels that remain at high transverse frequency.

## 3. What PF-244 still forbids

The matched calibration does **not** license replacing the actual source factor by an arbitrary bounded contraction. [[research/prime_flute/findings/PF-244-one-sided-seam-domination-does-not-imply-separated-poisson-smoothing|PF-244]] constructs the opposite failure mode: noncommuting boundary spectral conversion can send arbitrarily high input into a cheap low transverse mode *before* the Poisson propagation acts. The longitudinal semigroup damps according to the **output** transverse frequency, so a genuinely low output mode does not remember that the input carried a large `K^R` weight.

PF-257 makes the relevant physical source factor

\[
B_w=X_w(I+X_w^*X_w)^{-1}
\tag{10}
\]

rather than the naked polar partial isometry. PF-269 says only that `B_wK_a^RP_Z` need not be bounded as a standalone prerequisite. The actual theorem must instead control the composition appearing in [[research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing|PF-243]], strongly enough to rule out dangerous high-to-low conversion while allowing positive spatial separation to pay for the channels that remain high.

This is a sharper target than either extreme:

- demanding full positive-order smoothing from `B_w` before propagation is too strong;
- assuming boundedness of `B_w` is enough is too weak.

The remaining mechanism is a **joint conversion/propagation estimate** for the actual complete-lift seam.

## 4. Prior-art and novelty audit

No new general theorem about Robin boundary problems, functional calculus, or Poisson semigroups is claimed here. The identities `B=1/2 I` for the matched seam and exponential high-frequency damping across a product corridor are elementary/classical consequences of the exact PF-246/PF-257 framework.

The project-specific contribution is the logical combination of those two already-audited pieces: an exact canonical calibration simultaneously violates every positive-order standalone `B` estimate and satisfies all-order separated Robin-Poisson smoothing. This removes a stronger-than-necessary intermediate proof obligation from the current Prime-Flute route. The novelty claim is therefore only **route narrowing inside the persisted Mathia program**, not a claim of new operator theory.

## 5. Boundaries and falsification

This finding does **not** prove that the actual complete-lift `B_w` lacks positive-order smoothing. It may have useful localized or off-diagonal decay that the matched seam does not. Equation (4) proves only that such global pre-propagation gain cannot be required as a structural prerequisite for the separated theorem.

It also does not prove PF-243's four actual-seam source-to-bulk estimates, control the noncommuting reflection factors, justify the full infinite-corridor/Hardy-end realization, perform finite-pant or physical `P/H` recoupling, establish a global weak-trace/scattering/determinant statement, separate primes from matched controls, or imply anything about zeta zeros or RH.

A falsification of the route now has to target the **composed actual source-to-bulk operator**: exhibit high-frequency boundary data whose conversion by the physical normalized Robin map places enough mass in insufficiently damped output channels that the fixed positive spatial separation still cannot absorb one `K_a^R` weight for any `R>1`. Failure of a standalone `B_wK_a^R` bound is no longer such a falsification.

## Consequences for the research line

The literal pre-propagation target in [[research/prime_flute/clues/CLUE-critical-jacobi-square-root-decay-window|CLUE-critical-jacobi-square-root-decay-window]] is no longer load-bearing and can be closed as a narrowed route: whether the actual `B_w` happens to enjoy additional standalone decay remains interesting but is not the theorem PF-243 needs.

The surviving local target is [[research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate|CLUE-robin-homotopy-separated-poisson-shear-estimate]]. Its four far-leg estimates already keep the Robin conversion and positive separation in the same operator. After PF-268 and PF-269, that combined estimate is the correct place to test whether the actual arithmetic seam supplies enough control to cross the `R>1` threshold.