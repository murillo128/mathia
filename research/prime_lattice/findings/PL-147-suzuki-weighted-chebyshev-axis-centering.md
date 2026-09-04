# PL-147 — Suzuki’s weighted-Chebyshev criterion is already RH-equivalent on the prime-power axis; archimedean completion cancels its linear drift

## Claim

A peer-reviewed result of Masatoshi Suzuki gives an exact RH-equivalent scalar criterion whose arithmetic input is supported only on prime powers. Let

`F(x) = sum_(n<=x) Lambda(n)/sqrt(n) * log(x/n) - 4 sqrt(x)`.

Suzuki's Theorem 1 proves

`RH <=> F(x) <= 0 for every sufficiently large x`,

and also

`RH <=> F(x)/log x -> -alpha`,

where

`alpha = zeta'(1/2)/zeta(1/2) = 2.68609... > 0`.

Because `Lambda(n)` vanishes away from `n=p^k`, the arithmetic forcing in this criterion lives entirely on the prime-power exponent rays `k e_p`; mixed exponent vectors are absent. This is therefore a decisive prior-art redirect for the `prime_lattice` line: once the critical weight `n^(-1/2)`, the elementary pole barrier `4 sqrt(x)`, and Mellin analytic continuation are supplied, full RH equivalence does **not** require mixed-prime lattice points in this scalar channel.

Suzuki simultaneously identifies this weighted-Chebyshev statistic with the non-archimedean component `g_0` of the completed zeta screw function. For `t>=0`,

`g_0(t) = sum_(n<=exp(t)) Lambda(n)/sqrt(n) * (t-log n) - 4(exp(t/2)+exp(-t/2)-2)`.

Hence, exactly,

`g_0(log x) = F(x) + 8 - 4/sqrt(x)`.

Suzuki's Corollary 1 gives

`RH <=> -g_0(t) >= 0 for every sufficiently large t`.

However, he also proves a crucial negative boundary: **`g_0` cannot itself be a screw function even assuming RH**. The prime-power-axis criterion is logically RH-equivalent, but it does not possess the positive-definite Hilbert/screw geometry of the completed object.

The archimedean completion has an exact asymptotic role. Writing

`g_zeta(t)=g_0(t)+g_infty(t)`,

Suzuki gives

`g_infty(t) = -(t/2)(Gamma'/Gamma(1/4)-log pi) - (1/4)(Phi(1,2,1/4)-exp(-t/2) Phi(exp(-2t),2,1/4))`

for `t>=0`. Since `xi'/xi(1/2)=0`,

`alpha = -(1/2)(Gamma'/Gamma(1/4)-log pi)`.

Therefore the explicit archimedean term satisfies unconditionally

`g_infty(t)/t -> +alpha`.

Combining this with Suzuki's Theorem 1 and `g_0(log x)=F(x)+O(1)` yields the exact derived equivalences

`RH <=> g_0(t)/t -> -alpha`

and

`RH <=> g_zeta(t)/t -> 0`.

Thus, under RH, the archimedean factor cancels the deterministic negative linear drift of the RH-equivalent prime-power statistic. Completion is not needed for logical RH equivalence, but it is what removes that drift and permits the known screw/Hilbert geometry of the completed zeta object.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`. The weighted-Chebyshev equivalences, the formulas for `g_0` and `g_infty`, the non-archimedean interpretation of `g_0`, Corollary 1, and the impossibility of `g_0` being a screw function are peer-reviewed literature. The two displayed asymptotic equivalences and the exact cancellation interpretation are immediate algebraic consequences of those formulas and are not claimed as novel theorems.

## Exact relation to the exponent lattice

For every nonzero von-Mangoldt event `q=p^k`,

`v(q)=k e_p`,

`log q = <v(q),(log r)_r> = k log p`,

and its weighted amplitude is

`Lambda(q)/sqrt(q) = log p * exp(-<v(q),log r>/2)`.

Consequently

`F(exp(t)) = sum_(p^k<=exp(t)) log(p) exp(-k log(p)/2) (t-k log p) - 4 exp(t/2)`.

The arithmetic part is literally a sum over the axis skeleton of the positive exponent cone. This sharpens `PL-146`, where the same support structure appeared inside Suzuki's completed pointwise criterion: the restriction to prime-power rays is not merely a convenient event decomposition of the completed screw function. Suzuki's later weighted-Chebyshev theorem shows that this axis forcing, together with the elementary pole term, already carries an RH-equivalent eventual-sign and asymptotic criterion.

This does **not** mean the bare exponent axes alone prove or explain RH. The half-weight `exp(-E/2)` is inserted from the start, and the barrier `4 exp(t/2)` is an external elementary term corresponding to the pole structure. The result is instead an information-channel restriction: any proposed mechanism whose only purpose is to inject mixed exponent vectors into this particular scalar von-Mangoldt channel must explain what extra constraint they provide, because exact RH equivalence already exists without them.

## Why the analytic continuation is legitimate

Suzuki does not obtain the criterion by formally continuing the Euler product. If

`f(x)=sum_(n<=x) Lambda(n)/sqrt(n) log(x/n)`,

then, for `Re(s)>1`, absolute convergence and Fubini give

`integral_1^infinity (-f(x)) x^(-s+1/2) dx/x = (s-1/2)^(-2) zeta'(s)/zeta(s)`.

After adding the `4 sqrt(x)` term,

`integral_1^infinity (-F(x)) x^(-s+1/2) dx/x = (s-1/2)^(-2) zeta'(s)/zeta(s) + 4/(s-1)`.

The pole at `s=1` cancels. If `F(x)<=0` eventually, the tail integrand is nonnegative. Suzuki applies a standard Mellin/Laplace analogue of Landau's theorem to move the abscissa of convergence to at most `1/2`; the resulting analytic continuation of the transform forces `zeta'/zeta` to have no poles in `Re(s)>1/2`, hence no zeta zeros there, and RH follows by the functional equation. The passage into the critical strip is therefore a genuine analytic-continuation argument controlled by a one-sign transform, not an illicit continuation of the prime sum.

The same point is visible in Suzuki's proof of Corollary 1. For `Re(s)>1`,

`integral_0^infinity (-g_0(t)) exp(-t(s-1/2)) dt`

`= (s-1/2)^(-2) [ zeta'(s)/zeta(s) + 1/(s-1) + 1/s ]`.

Again the `s=1` pole is canceled before the one-sign Mellin argument is used. This is the precise mechanism by which a statistic supported arithmetically only on prime powers can constrain zeros in the critical strip.

## Archimedean cancellation versus RH equivalence

Set

`alpha=zeta'(1/2)/zeta(1/2)>0`.

Suzuki's Theorem 1 gives under RH, and equivalently only under RH,

`F(x) = -alpha log x + o(log x)`.

Because `g_0(log x)=F(x)+8-4/sqrt(x)`, this is exactly

`g_0(t) = -alpha t + o(t)`.

On the other hand, the explicit Hurwitz-Lerch term in `g_infty(t)` is bounded as `t->infinity`, while `xi'/xi(1/2)=0` gives the coefficient of the linear term. Hence

`g_infty(t)=+alpha t+O(1)`.

Therefore

`g_zeta(t)=g_0(t)+g_infty(t)=o(t)`

if and only if RH holds. This should not be overread as a new spectral proof: it is a direct repackaging of Suzuki's weighted-Chebyshev asymptotic criterion. Its value for this research line is structural. The finite-place statistic by itself has a deterministic drift of magnitude `alpha`; the archimedean place supplies exactly the opposite drift. The completed screw object is the centered combination.

This also clarifies the role of the smooth term in `PL-146`. There the completed pointwise criterion `Psi=-g_zeta` is organized as a prime-power jump system against a deterministic smooth clock. The present finding shows that the completion is not needed to obtain an RH-equivalent scalar inequality, because `-g_0` already has one eventually. What completion changes is the geometry: the non-archimedean component cannot be a screw function even under RH, whereas the completed zeta screw function has the Krein-Langer/Hilbert-space positivity structure under RH.

## Prior-art and novelty audit

Primary source:

- **Masatoshi Suzuki**, “On variants of Chebyshev’s conjecture,” *The Ramanujan Journal* **68** (2025), article 95, DOI `10.1007/s11139-025-01238-9`; arXiv `2411.07436` (v3, 10 November 2025). Theorem 1 is the weighted-Chebyshev eventual-sign/asymptotic equivalence with RH. Equations (7)–(9) identify `g_0`, `g_infty`, and the non-archimedean/archimedean split. Corollary 1 is the eventual-sign criterion for `g_0`. The introduction explicitly notes that `g_0` cannot itself be a screw function even assuming RH. The proof of Theorem 1 supplies the Mellin/Landau continuation argument.
- **Masatoshi Suzuki**, “Correction: On variants of Chebyshev’s conjecture,” *The Ramanujan Journal* **69** (2026), article 19, DOI `10.1007/s11139-025-01289-y`, published 19 December 2025. The correction concerns the arithmetic-progression portion (including Theorem 7 and later formulas) and does not alter Theorem 1, Corollary 1, or the zeta formulas used here.
- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487, DOI `10.1112/jlms.12785`. This is the underlying completed screw-function theory already used in `PL-120`, `PL-143`–`PL-146`.

A current-literature check also finds Rainer Andreas Mittermeier's August 2026 Zenodo checkpoint/recovery series, especially Part 5, explicitly connecting the checkpoint workload to a weighted Chebyshev error. Those self-published preprints are useful novelty control but are not needed as authority here: Suzuki's peer-reviewed 2025 theorem already establishes the exact RH-equivalent weighted-Chebyshev channel, and all additional identities used above were independently reduced to Suzuki's displayed formulas.

Accordingly, neither the axis-only RH equivalence nor the archimedean/non-archimedean organization should be claimed as Mathia novelty. The exact drift-cancellation statement is a short derived consequence and is stored as a route clarification, not as a novelty claim.

## Adversarial boundaries and falsification

1. **This is not an RH proof.** Eventual negativity of `F`, eventual nonnegativity of `-g_0`, and the stated asymptotic limits are equivalent criteria whose unresolved content is exactly RH.

2. **The arithmetic support is axis-only, but `g_0` is not “bare primes.”** The term `-4(exp(t/2)+exp(-t/2)-2)` encodes the elementary `s(s-1)` part together with the zeta factor in Suzuki's non-archimedean decomposition. The criterion therefore consists of prime-power forcing plus a fixed external pole barrier.

3. **The critical exponent is assumed, not derived.** The factor `Lambda(n)n^(-1/2)` already singles out `1/2`. This finding gives no mechanism deriving the critical line from the abstract lattice geometry.

4. **No hidden Hilbert-Polya operator has appeared.** Suzuki explicitly rules out `g_0` itself being a screw function even under RH. Logical RH equivalence of a scalar sign statistic is weaker than a self-adjoint spectral localization mechanism.

5. **Mixed exponent vectors remain invisible only in this channel.** This does not prove they are irrelevant to every possible arithmetic-lattice formulation. It says they are unnecessary for this exact scalar criterion and cannot be justified merely by claiming that RH equivalence requires full-lattice information.

6. **The completion does more than subtract a line.** The asymptotic linear cancellation is exact, but the full `g_infty` contains a nontrivial bounded Hurwitz-Lerch term, and the completed object has analytic/Hilbert structure not present in `g_0`. “Centers the drift” is an asymptotic statement, not a claim that the archimedean factor is otherwise dispensable.

7. **The analytic continuation step is essential.** The prime-power sum identity is initially justified only for `Re(s)>1`; RH information enters when one-sign Mellin theory forces analytic continuation of the transform into `Re(s)>1/2`. Omitting that step would reduce the argument to a tautological Euler-product re-encoding.

A falsification of the stored structural claim would require an error in Suzuki's Theorem 1 or Corollary 1, a failure of the exact relation `g_0(log x)=F(x)+8-4/sqrt(x)`, or a different linear coefficient in the explicit `g_infty`. The published formulas fix all three.

## Consequence for the research line

Do not spend further research passes seeking a new **scalar** RH-equivalent eventual-sign criterion built merely from `Lambda(p^k)`, the energy `k log p`, and the critical weight `p^(-k/2)`: Suzuki already supplies one in peer-reviewed literature. Nor should archimedean completion be advertised as necessary merely to make a finite-place scalar statistic logically equivalent to RH.

The surviving questions are narrower and more structural. A genuinely new prime-lattice mechanism must explain why the half-weight and pole barrier are canonical rather than inserted, or must exploit completion to obtain a rigidity unavailable to `g_0`—for example an operatorial/positive-definite mechanism that actually forces zero localization rather than restating it as eventual sign. If mixed exponent vectors are introduced, they need to constrain that surviving mechanism in a way the exact prime-power-axis criterion cannot already capture.
