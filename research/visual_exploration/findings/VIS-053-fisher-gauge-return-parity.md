# VIS-053 — Fisher-gauge return counts have the parity of the residual sign budget

## Claim

Assume the nondegenerate two-ratio Fisher configuration of `VIS-049` together with the exact one-coordinate finite-gauge reduction of `VIS-050` and the return polynomial of `VIS-052`. Thus `0<|kappa|<1`, and for a fixed real log-gauge direction `h`,

`kappa_h(s)=kappa  <=>  D_h(s)=0`,

where after aggregating equal `h` values,

`D_h(s)=sum_(j=1)^K c_j exp(a_j s)`,

with `a_1<...<a_K`, `sum_j c_j=0`, and the zero `c_j` deleted when sign changes are counted. Let `V(c)` denote the number of sign changes in the resulting ordered nonzero coefficient sequence. Assume `D_h` is not identically zero.

Let `N` be the total number of real zeros of `D_h`, counted with multiplicity. Let

`r=min{m>=1 : Delta_m != 0}`

be the first unmatched class cumulant from `VIS-051`, so `s=0` is a zero of multiplicity exactly `r` by `VIS-052`. Then:

1. `N <= V(c)` and, more sharply,

   `N ≡ V(c) (mod 2)`.

2. If `N_*` is the total multiplicity of all nonzero exact balance returns, then

   `N_* = N-r`,

   and therefore

   `0 <= N_* <= V(c)-r`,

   `N_* ≡ V(c)-r (mod 2)`.

   Hence the only possible nonzero-return multiplicities are

   `V(c)-r, V(c)-r-2, V(c)-r-4, ...`

   down to `0` or `1`.

3. In particular:

   - `V(c)=r` forces `s=0` to be the unique exact balance return, recovering the extremal case of `VIS-052`;
   - `V(c)=r+1` forces **exactly one** nonzero balance return, and that return is simple as a zero of `D_h`;
   - `V(c)=r+2` allows either no nonzero return or total nonzero multiplicity two;
   - more generally, an odd residual budget `V(c)-r` forces at least one remote exact balance return.

4. Write

   `A=Delta_r/r!`.

   Let `c_-` and `c_+` be respectively the first and last nonzero coefficients in increasing `a_j` order. A nonzero return is forced on the positive half-line whenever

   `sign(c_+) != sign(A)`,

   and on the negative half-line whenever

   `sign(c_-) != (-1)^r sign(A)`.

   In the minimal odd-budget case `V(c)=r+1`, exactly one of these two endpoint mismatches occurs, so the unique remote return is localized to that half-line.

5. Every balance root of multiplicity `m` produces a Fisher-angle contact of order exactly `2m` by `VIS-052`. Thus when `V(c)=r+1`, the forced remote balance return appears in `kappa_h(s)` as one isolated quadratic tangency to the baseline angle, not as a transverse crossing.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-GENERALIZED-DESCARTES + REPRESENTATION CONTROL + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

The result is a representation diagnostic. It does not assert that empirical zeta/CUE residuals satisfy the exact two-ratio model, that an observed remote tangency is arithmetic, or that the parity statement is a new theorem about generalized polynomials.

## 1. Endpoint coefficient signs determine root-count parity

`VIS-052` already gives the generalized Descartes bound

`N <= V(c)`

for the real zeros of `D_h`, counted with multiplicity. The missing information is parity.

Let `c_-` be the first nonzero coefficient and `c_+` the last. Because the exponents are strictly ordered,

`sign D_h(s) -> sign(c_-)` as `s -> -infinity`,

and

`sign D_h(s) -> sign(c_+)` as `s -> +infinity`.

A real zero of even multiplicity does not change the sign of a real analytic function across the zero, while a zero of odd multiplicity does. Since `D_h` has only finitely many real zeros, transporting the sign from `-infinity` to `+infinity` gives

`sign(c_+)/sign(c_-)=(-1)^N`.

On the other hand, traversing the ordered nonzero coefficient sequence flips sign exactly `V(c)` times, so

`sign(c_+)/sign(c_-)=(-1)^(V(c))`.

Therefore

`N ≡ V(c) (mod 2)`.

This parity argument is elementary once the finite-zero property is known. It is the endpoint-sign complement to the generalized Descartes upper bound rather than an additional zero-counting theorem.

## 2. The baseline cumulant order removes a fixed part of the parity budget

Both class moment-generating functions equal one at `s=0`, so `D_h(0)=0`. `VIS-051` and `VIS-052` show that if `r` is the first unmatched class cumulant, then

`D_h(s)=A s^r+O(s^(r+1))`,

with `A=Delta_r/r! != 0`. Hence the baseline root has multiplicity exactly `r`.

Writing `N=N_*+r` and combining this identity with the Descartes bound and parity relation gives

`N_* <= V(c)-r`

and

`N_* ≡ V(c)-r (mod 2)`.

This turns the residual sign budget from a mere ceiling into a discrete admissible set. The gap `V(c)-r` cannot be consumed by an arbitrary number of remote exact returns: only values of the same parity are possible.

The first nontrivial consequence is counterintuitive from a visual-robustness perspective. If `V(c)-r=1`, a remote exact return is not merely allowed; it is unavoidable. A plot showing one additional baseline touch in that case is therefore forced by the declared gauge representation and cannot be counted as independent structure.

## 3. Endpoint mismatches localize forced returns

The local expansion at the baseline gives

`sign D_h(s)=sign(A)`

for sufficiently small positive `s`, while for sufficiently small negative `s`,

`sign D_h(s)=(-1)^r sign(A)`.

At the far ends the signs are `sign(c_+)` and `sign(c_-)`. Therefore the intermediate value theorem forces at least one positive zero whenever

`sign(c_+) != sign(A)`,

and at least one negative zero whenever

`sign(c_-) != (-1)^r sign(A)`.

More precisely, each mismatch forces an odd total multiplicity of roots on that half-line; a sign match forces even total multiplicity there. Summing the two half-lines recovers the global parity rule.

When `V(c)=r+1`, the residual budget allows total nonzero multiplicity only one. Hence only one half-line can have an endpoint mismatch, and the forced root there must be simple. This supplies a deterministic location test before drawing the gauge-sweep curve.

## 4. Fisher normalization doubles the visible contact order

At any balance point `s_0`, `VIS-052` gives the exact local relation

`kappa_h(s)-kappa = [kappa(1-kappa^2)/8] q_h(s)^2 + O(q_h(s)^4)`.

Because `q_h` and `D_h` have the same zero multiplicity at a balance point, a zero of multiplicity `m` in `D_h` becomes a zero of multiplicity `2m` in the Fisher-angle defect.

Thus the return-parity statement is deliberately formulated on `D_h`, where crossings and multiplicities retain their ordinary sign meaning. The normalized Fisher angle hides those crossings by squaring the leading balance coordinate. In particular, the unique remote root forced by `V(c)=r+1` is simple in the balance equation but appears as a quadratic touch in the rendered Fisher angle.

This is exactly the sort of visual false-positive mechanism the line is meant to classify: repeated or isolated baseline contacts can be mandated by coefficient-sign topology even though the plotted scalar never changes sign around them.

## 5. Prior art and novelty boundary

The zero upper bound is classical generalized Descartes/Laguerre theory. The direct source already used in `VIS-052` is G. J. O. Jameson, **Counting zeros of generalised polynomials: Descartes' rule of signs and Laguerre's extensions**, *The Mathematical Gazette* 90:518 (2006), 223–234, DOI `10.1017/S0025557200179628`.

Broader Descartes-system literature also studies when sign variation gives parity-sharp zero information; for example J. M. Carnicer, **Characterizations of the Optimal Descartes' Rules of Signs**, *Mathematische Nachrichten* 189 (1998), 33–48, DOI `10.1002/mana.19981890104`. No general theorem from that paper is needed here: after `VIS-052` supplies finiteness and the upper bound, the parity statement follows directly from the signs at the two real endpoints and multiplicity parity.

No novelty is claimed for Descartes parity, endpoint sign continuation, exponential polynomials, or the intermediate value theorem. The durable Mathia contribution is the specialization to the exact Fisher-gauge reduction: the first unmatched cumulant order consumes a fixed multiplicity `r`, leaving a parity-constrained residual budget `V(c)-r` for remote visual returns.

## 6. Boundary conditions and falsification

All hypotheses of `VIS-052` remain active: finite support, fixed residual tensors, exact reciprocal two-ratio classes, fixed class weights, one fixed real perturbation field `h`, and `0<|kappa|<1`. Equal `h` values must be aggregated before zero coefficients are deleted and `V(c)` is counted.

The theorem counts **exact** roots with multiplicity. Near-returns under sampling noise, approximate two-ratio structure, refitted tensors, thresholded plots, or gauge-dependent rebinning are outside the claim. A numerical curve can also miss an even-contact root unless the balance coordinate is inspected directly.

Falsify the result by constructing a valid nonzero `D_h` satisfying the `VIS-052` hypotheses for which the total real-root multiplicity has parity different from `V(c)`; by finding a case in which `V(c)=r+1` but there is not exactly one simple nonzero balance root; or by finding an endpoint-sign mismatch on a half-line with no balance root there.

## Research consequence

For any frozen empirical comparison close enough to the two-ratio regime to justify this exact model, compute `r`, `V(c)`, `A`, and the first/last nonzero coefficient signs **before** interpreting a gauge-sweep plot. These four quantities already predict whether remote exact returns are impossible, optional in parity-constrained pairs, or forced, and in the minimal odd-budget case they identify which half-line contains the unique return.

A rendered Fisher-angle touch that is forced by this sign/cumulant budget is a representation effect, not evidence of arithmetic robustness. The next genuinely informative question is quantitative stability: how these exact root-count and location certificates deform when the reciprocal ratio classes and class moment laws are only approximately satisfied.