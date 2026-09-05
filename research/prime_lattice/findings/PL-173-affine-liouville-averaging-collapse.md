# PL-173 — Canonical affine Liouville averaging becomes square energy or a moving strong-zero observable

## Claim

The proposed averaging escape from `PL-172` has a sharp obstruction for the canonical uniform translation averages. Let

`H e_n=(log n)e_n`, `S_h e_n=e_(n+h)`, and `J e_n=lambda(n)e_n` on `ell^2(N_{>=1})`, and write

`J_h:=S_h^* J S_h`, so `J_h e_n=lambda(n+h)e_n`.

Then the fixed-shift parity operator of `PL-172` is `K_h=J J_h`. For `R>=1`, its uniform anchored average is

`A_R := (1/R) sum_(h=1)^R K_h = J U_R`,

where

`U_R := (1/R) sum_(h=1)^R J_h`.

The diagonal coefficients are exact:

`A_R e_n = lambda(n) [L(n+R)-L(n)]/R * e_n`,

`U_R e_n = [L(n+R)-L(n)]/R * e_n`,

with `L(x)=sum_(m<=x) lambda(m)`. Since the prime number theorem gives `L(x)=o(x)`, both `U_R` and `A_R` converge strongly to zero as `R->infinity` (their coefficients are bounded by one and converge pointwise to zero). Thus the most literal fixed-origin uniform shift average does not leave a nonzero limiting parity operator.

In the ordinary trace-class half-plane, the same conclusion holds for the first heat trace:

`Tr(exp(-sH) A_R) = (1/R) sum_(h=1)^R C_h(s) -> 0`, `Re(s)>1`,

where

`C_h(s)=sum_(n>=1) lambda(n)lambda(n+h)n^(-s)`

is the fixed-shift Chowla Dirichlet series from `PL-172`. This limit uses only dominated convergence inside the region where the trace is already absolutely defined; it supplies no continuation of any fixed `C_h` through `Re(s)=1`.

The unconditional averaged-Chowla theorem of Matomaki--Radziwill--Tao does provide a genuine cancellation theorem once **both shift endpoints are averaged and the aperture grows with the observation scale**. Operatorically, its two-point channel is exactly the finite-window trace of the square

`U_R^2`:

`Tr(P_X U_R^2)
 = (1/R^2) sum_(a,b<=R) sum_(n<=X) lambda(n+a)lambda(n+b)
 = sum_(n<=X) |(1/R)sum_(a<=R)lambda(n+a)|^2`.

Their theorem states, for fixed `k` and `R=R(X)<=X` with `R(X)->infinity`,

`sum_(h_1,...,h_k<=R) |sum_(n<=X) prod_j lambda(n+h_j)| = o(R^k X)`.

For `k=2` this implies `Tr(P_X U_R^2)=o(X)` along that growing-aperture regime. But this is a **moving two-parameter family** `U_(R(X))`, not the analytic continuation of a fixed Dirichlet-series trace. If `R` is held fixed, the first trace remains a finite linear combination of the still-unresolved fixed-shift channels `C_h(s)`.

There is also an exact finite-window control showing what happens when every admissible positive displacement is included once. If `P_M` projects onto `e_1,...,e_M`, then

`sum_(h=1)^(N-1) Tr(P_(N-h) K_h)
 = sum_(1<=n<m<=N) lambda(n)lambda(m)
 = [L(N)^2-N]/2`.

So the complete triangular all-shift first trace does retain Liouville signs, but only by collapsing the pair observable to the square of the classical one-point summatory function. Any square-root-scale RH criterion extracted from this identity is therefore a re-expression of the classical Liouville summatory criterion, not a new geometric or spectral selector.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, decisive for the canonical uniform/complete-window averaging route and resolving the local averaged-affine-parity clue in narrowed form.

The Matomaki--Radziwill--Tao averaged theorem is prior art. The operator identities, strong-limit calculation, and complete-window square identity are elementary exact deductions from the affine Liouville representation. No novelty is claimed for averaged Chowla, the prime-number-theorem estimate `L(x)=o(x)`, or the classical equivalence between square-root Liouville summatory bounds and RH.

## 1. Uniformly averaging the PL-172 shifts gives an explicit moving Liouville average

For `h>=0`, define

`J_h=S_h^* J S_h`.

Since `S_h e_n=e_(n+h)`, one has

`J_h e_n=lambda(n+h)e_n`.

All the `J_h` commute because they are diagonal, and `J_0=J`. Therefore

`K_h=J_0 J_h`.

The uniform average over the shifts appearing in `PL-172` is not an abstract new operator family. It is

`A_R=(1/R)sum_(h=1)^R K_h=J_0 U_R`,

with

`U_R=(1/R)sum_(h=1)^R J_h`.

On each basis vector,

`U_R e_n
 = (1/R)sum_(h=1)^R lambda(n+h)e_n
 = [L(n+R)-L(n)]/R * e_n`.

Thus averaging the additive displacement turns the two-point sign `lambda(n)lambda(n+h)` into a local moving average of the one-point Liouville sequence. This is already a substantial loss of the fixed-shift channel: the shift index has become an averaging variable rather than a retained arithmetic label.

The classical prime number theorem implies `L(x)=o(x)`. Hence for each fixed `n`,

`[L(n+R)-L(n)]/R -> 0`.

Also `||U_R||<=1` and `||A_R||<=1`. For any `x=(x_n) in ell^2`,

`||U_R x||^2
 = sum_n |x_n|^2 |[L(n+R)-L(n)]/R|^2 -> 0`

by dominated convergence; the same holds for `A_R=J U_R` because `J` is unitary. Therefore

`U_R -> 0` strongly and `A_R -> 0` strongly.

No operator-norm convergence is asserted. The point is narrower and exact: a fixed vector cannot retain a nonzero parity observable under the canonical uniform translation average as the aperture tends to infinity.

## 2. The fixed first heat trace either stays in the Chowla wall or vanishes in the safe half-plane

For `Re(s)>1`, `exp(-sH)A_R` is trace class and

`Tr(exp(-sH)A_R)
 = (1/R)sum_(h=1)^R sum_(n>=1)lambda(n)lambda(n+h)n^(-s)
 = (1/R)sum_(h=1)^R C_h(s)`.

For each fixed `n`, the coefficient

`lambda(n)[L(n+R)-L(n)]/R`

tends to zero and has modulus at most one. Hence, if `sigma=Re(s)>1`,

`sum_n n^(-sigma)<infinity`

is an absolute dominating series and

`Tr(exp(-sH)A_R) -> 0`.

This is not a continuation theorem. It proves the limit only where every fixed `C_h(s)` already has an absolutely convergent defining series and where the operator trace is ordinary trace class.

If instead `R` is fixed, then

`Tr(exp(-sH)A_R)=(1/R)sum_(h<=R)C_h(s)`

is merely a finite linear combination of fixed-shift two-point Liouville correlation series. The standard fixed-shift Cesaro Chowla problem remains open; `PL-172` already records that logarithmic or averaged substitutes cannot be silently upgraded to the ordinary fixed-shift statement. Thus finite shift averaging does not create the missing critical-strip continuation.

## 3. The theorem-level averaged Chowla input changes the observable as the scale grows

Matomaki, Radziwill, and Tao prove an averaged form of Chowla's conjecture. For fixed `k`, if `R=R(X)<=X` and `R(X)->infinity`, then

`sum_(h_1,...,h_k<=R)
 |sum_(n<=X) lambda(n+h_1)...lambda(n+h_k)|
 = o(R^k X)`.

Their paper explicitly contrasts this with the ordinary fixed-shift Chowla conjecture, which remains unproved for `k>=2` in the statement of the source.

For `k=2`, the exact operator matching is particularly transparent. Because the `J_a` commute,

`U_R^2
 = (1/R^2)sum_(a,b<=R)J_aJ_b`,

and therefore

`Tr(P_X U_R^2)
 = (1/R^2)sum_(a,b<=R)sum_(n<=X)lambda(n+a)lambda(n+b)`.

On the other hand, direct diagonalization gives

`Tr(P_X U_R^2)
 = sum_(n<=X) [(1/R)sum_(a<=R)lambda(n+a)]^2 >=0`.

By the triangle inequality and the `k=2` averaged-Chowla theorem,

`Tr(P_X U_R^2)=o(X)`

whenever `R=R(X)->infinity` in the theorem's allowed range.

This is a genuine unconditional signed-correlation statement with exactly declared averaging weights, and it is stronger than an unsigned divisor-density surrogate. But the parameter regime is load-bearing: the shift aperture must grow with `X`. There is no single fixed `R` operator whose first trace is thereby analytically continued, and taking `R->infinity` first returns the strong-zero operator already derived above.

Thus the available theorem succeeds only after replacing the desired fixed arithmetic channel by a moving family whose local Liouville average is itself being driven to zero.

## 4. Complete finite-window averaging collapses exactly to the summatory square

A second canonical averaging prescription is to count every unordered pair of integers in one finite observation window exactly once. This corresponds to summing over all positive shifts with the compatible truncation:

`B_N := sum_(h=1)^(N-1) Tr(P_(N-h)K_h)`.

Using the diagonal of `K_h`,

`B_N
 = sum_(h=1)^(N-1)sum_(n=1)^(N-h)lambda(n)lambda(n+h)
 = sum_(1<=n<m<=N)lambda(n)lambda(m)`.

Since `lambda(n)^2=1`,

`L(N)^2
 = sum_(n,m<=N)lambda(n)lambda(m)
 = N + 2 sum_(1<=n<m<=N)lambda(n)lambda(m)`.

Therefore

`boxed: B_N=[L(N)^2-N]/2`.

This is exactly one of the failure modes anticipated by the clue: the averaged two-point trace becomes a summatory-function square. It has not lost the sign information in the sense of taking absolute values, but it has lost the distinction between individual additive correlations. All pair geometry has compressed into the single scalar `L(N)`.

The identity is useful as a control because it prevents a misleading interpretation of square-root-looking scales. A statement such as `L(N)=O_epsilon(N^(1/2+epsilon))` is a classical RH-equivalent summatory criterion. Rewriting it through `B_N` does not supply a new reason for that cancellation or a new spectral object that forces it.

## 5. Prior-art and novelty audit

Primary theorem-level source:

- **Kaisa Matomaki, Maksym Radziwill, Terence Tao**, “An averaged form of Chowla's conjecture,” *Algebra & Number Theory* **9**(9) (2015), 2167--2196, DOI `10.2140/ant.2015.9.2167`, arXiv `1503.05121` (current arXiv revision 1 March 2022). The abstract states the fixed-shift Chowla conjecture, notes that it remains unproved for `k>=2`, and proves the displayed average over `h_1,...,h_k<=R` whenever `R=R(X)<=X` tends to infinity.

The operator realization used here is line-local and elementary: `J_h` is simply the translated Liouville diagonal, and `U_R` is its uniform average. The square identity for `Tr(P_XU_R^2)` is the standard expansion of a short-interval Liouville mean square; it is not claimed as a new analytic-number-theory theorem. Likewise, the complete-window identity is the elementary polarization identity for a sign sequence.

The research contribution is therefore a **route classification**, not a novelty claim: after `PL-172` identified the deleted fixed-shift trace, the most canonical attempts to recover it by shift averaging are now separated exactly into (i) a fixed finite average that retains the unresolved Chowla wall, (ii) an infinite uniform average that converges strongly to zero, (iii) the theorem-controlled growing-aperture average, which is a moving finite-window object, and (iv) a complete all-pair average that collapses to `L(N)^2`.

## 6. Adversarial controls and scope

1. **No upgrade from averaged to fixed Chowla.** The Matomaki--Radziwill--Tao theorem requires a growing shift aperture and averages all shift tuples. It is not used to infer cancellation for any prescribed fixed `h`.
2. **Strong convergence is not norm convergence.** Only `A_R x->0` and `U_R x->0` for each fixed `x in ell^2` are asserted. The operator norms need not tend to zero.
3. **No trace continuation is inferred from the strong limit.** The heat-trace limit is proved only for `Re(s)>1`, where `sum n^(-sigma)` supplies absolute domination.
4. **The all-pair identity is a zero-spectral-weight finite trace.** It is a decisive control for complete finite-window averaging, not a claim that every nonuniform `n^(-s)`-weighted average factors as `L(N)^2`.
5. **Nonuniform source-forced weights are not ruled out.** A future mechanism could use weights forced by an independent arithmetic or spectral construction and avoid both the complete-window square collapse and the uniform strong-zero limit. It would still need a theorem at the exact same weights and a fixed analytic object whose first-order signed carrier survives.
6. **No RH implication is claimed.** The finding explains why these averaging operations do not create new RH rigidity; it does not solve the underlying Liouville cancellation problem.

## Consequence for the research line

The local averaging clue is resolved in narrowed form. Merely replacing the fixed additive displacement in `PL-172` by a uniform family does not recover the first trace deleted by `det_2` in a useful fixed object. The anchored average converges strongly to zero; the two-ended average is theoremically controllable only when its aperture grows with the observation window; and the complete finite-window pair sum is exactly a classical Liouville summatory square.

A surviving averaged affine route must therefore specify a **nonuniform, source-forced weighting or comparison operation** before seeing the desired conclusion. Its weights must neither average the parity observable to zero nor collapse the pair data to a one-point summatory statistic, and an unconditional theorem must control precisely that same weighted first trace. Absent those ingredients, “average over shifts” is not an analytic-continuation mechanism but a change of observable.