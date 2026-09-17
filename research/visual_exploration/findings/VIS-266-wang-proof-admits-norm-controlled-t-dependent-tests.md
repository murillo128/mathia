# VIS-266 — Wang's proof admits norm-controlled `T`-dependent tests inside a fixed support margin

## Claim

The `O_g` notation in Biao Wang's 2026 short-interval pair-correlation theorem hides more usable uniformity than the fixed-test statement alone suggests. Reading the proof of Theorem 2.2 quantitatively shows that, for fixed

`0 < lambda < theta < 1`, `H=T^theta`, `L=log T`,

one may let the smooth even test function vary with `T`, provided all tests remain supported in the same fixed interval `[-lambda,lambda]` and their elementary seminorms do not grow too fast.

Define

`W_I(g) = sum_(gamma,gamma' in I) hat g(i(rho-rho')L/(2*pi)) w(rho-rho')`,

with `I=(T,T+H]` and `w(z)=4/(4-z^2)`. For every real even `g_T in C_c^infinity(R)` with

`supp(g_T) subset [-lambda,lambda]`,

Wang's proof gives the quantitative family bound

`W_I(g_T)`
` = (H L/(2*pi)) [g_T(0) + integral_R |alpha| g_T(alpha) d alpha]`
`   + O_(lambda,theta)( H ||g_T'||_infinity`
`       + ||g_T||_infinity [H + H/sqrt(L) + T^lambda L^2 + 1] ).`

Equivalently, after dividing by `H L/(2*pi)`,

`(2*pi/(H L)) W_I(g_T)`
` = g_T(0) + integral_R |alpha| g_T(alpha) d alpha`
`   + O_(lambda,theta)( ||g_T'||_infinity/L`
`       + ||g_T||_infinity [1/L + L^(-3/2) + T^(lambda-theta)L + 1/(H L)] ).`

Hence the simpler sufficient condition

`||g_T'||_infinity/L`
` + ||g_T||_infinity [1/L + T^(lambda-theta)L] -> 0`

is enough for the usual leading Montgomery functional to remain asymptotically valid for a `T`-dependent family.

This materially sharpens the transfer boundary in `VIS-265`: **the obstruction is not merely that Wang states Theorem 2.2 for fixed `g`**. Some shrinking or otherwise changing smooth probes are already certified by the proof. The real surviving gates are the fixed support margin `lambda<theta`, the growth of the test-function seminorms, and the absence of a lower-order arithmetic term beneath the normalized `1/L` error scale.

**Evidence/status:** `LITERATURE+DERIVED + EXACT ERROR-BOOKKEEPING + UNIFORM-TEST-FAMILY TRANSFER + PACKET-CONDITIONING GATE + NO-NOVELTY-CLAIM`.

No new pair-correlation theorem, moving-support theorem, support-edge estimate, lower-order arithmetic coefficient, or RH implication is claimed.

## 1. The proof exposes the dependence hidden by `O_g`

The source is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1, Theorem 2.2 and its proof.

Wang first proves, uniformly for `0<=alpha<=lambda`,

`F_I(T^alpha)`
` = (H/(2*pi)) [L^2 exp(-2L alpha) + L alpha]`
`   + O_(lambda,theta)( H + H L exp(-2L alpha)`
`       + H sqrt(L) exp(-L alpha) + L^3 exp(L alpha)`
`       + L exp(-L alpha/2) ).`

The exact Fourier inversion step then gives

`W_I(g)=2 integral_0^lambda g(alpha) F_I(T^alpha) d alpha.`

The linear cusp term contributes exactly

`(H L/(2*pi)) integral_R |alpha| g(alpha) d alpha.`

For the concentrated exponential term, Wang writes

`2 L^2 integral_0^lambda g(alpha) exp(-2L alpha) d alpha`
` = L g(0) + 2 L^2 integral_0^infinity [g(alpha)-g(0)] exp(-2L alpha) d alpha.`

The mean-value theorem gives

`|g(alpha)-g(0)| <= ||g'||_infinity alpha`,

and therefore

`|2 L^2 integral_0^infinity [g(alpha)-g(0)] exp(-2L alpha) d alpha|`
` <= (1/2) ||g'||_infinity.`

After restoring the factor `H/(2*pi)`, this part of the remainder is `O(H ||g'||_infinity)` with no hidden need for `g` to be independent of `T`.

For the five error terms in the uniform estimate for `F_I(T^alpha)`, taking absolute values gives a factor `||g||_infinity`. Their integrals over `[0,lambda]` are respectively

`O(H)`, `O(H)`, `O(H/sqrt(L))`, `O(T^lambda L^2)`, and `O(1)`.

The displayed family bound follows directly. The implied constant may depend on the fixed outer parameters `lambda` and `theta`, exactly as in Wang's setup, but not on the particular member `g_T` once its sup norm and first derivative norm are written explicitly.

## 2. A concrete shrinking-packet gate

The bound turns qualitative packet conditioning into an explicit scale restriction. Let `a` be fixed with `|a|<lambda`, let `phi` be a fixed smooth compactly supported bump, and form an even two-sided packet of width `b=b(T)` whose amplitude scales like `b^(-A)`, for example

`g_(T,b)(alpha) = b^(-A) [phi((alpha-a)/b) + phi((alpha+a)/b)]`,

with `b` small enough that the support remains inside the same fixed `[-lambda,lambda]`.

Then

`||g_(T,b)||_infinity = O(b^(-A))`,

`||g_(T,b)'||_infinity = O(b^(-A-1)).`

Wang's proof therefore certifies the leading short-interval Montgomery law whenever

`b^(-A-1)/L -> 0`

and

`b^(-A) T^(lambda-theta) L -> 0`,

with `b^(-A)/L -> 0` as the remaining elementary term. Because `theta-lambda` is a fixed positive power margin, the polynomially decaying factor `T^(lambda-theta)` is harmless for many logarithmic packet scales. The derivative term is then the main conditioning barrier.

For the illustrative choice `b=L^(-q)`, a sufficient derivative condition is

`q(A+1) < 1`.

Thus an amplitude-bounded shrinking bump (`A=0`) may narrow more slowly than `1/L`, while a mass-normalized bump (`A=1`) requires, at this crude seminorm level, `b` to shrink more slowly than `L^(-1/2)`. Higher-amplitude signed packets pay correspondingly more. These are consequences of this proof bound, not asserted optimal packet thresholds.

The relevance to the current visual thread is direct. A packet's total-variation or moment-cancellation conditioning cannot be discussed independently of the smooth test through which it is inserted into a theorem. Wang's proof supplies one explicit test-function norm budget against which such a mollified packet construction can be checked.

## 3. What this corrects in the fixed-test reading

`VIS-265` correctly treated Wang's published theorem statement conservatively: it is stated for fixed `g`, with `O_g`, and therefore one cannot simply substitute a `T`-dependent family into the theorem as written.

The proof, however, makes the relevant dependence elementary. On a fixed support interval, the only test-function quantities used in the final integration are `||g||_infinity` and `||g'||_infinity`. Consequently a `T`-dependent family is legitimate when those quantities satisfy the displayed asymptotic budget.

This removes one false bottleneck. The current branch should not say that every shrinking packet is excluded merely because the theorem says "fixed `g`". The sharper statement is:

- fixed-margin `T`-dependent smooth tests are available under an explicit seminorm-growth condition;
- approaching the support boundary is a different problem because `lambda` itself would have to move, and the present proof has not been audited uniformly in that moving outer parameter;
- lower-order extraction is a different problem because even a fixed well-conditioned test retains a normalized `O(1/L)` theorem error.

These distinctions matter because only the first issue is relaxed by the present bookkeeping.

## 4. The support-edge and lower-order gates remain

Nothing here weakens the support-length law from `VIS-265`. The estimate is derived with fixed `lambda<theta`. It gives no uniform control as `lambda=lambda(T)` approaches `theta`, and therefore no route to the Montgomery edge `|alpha|=1` inside a power-short interval with `theta<1`.

Nor does the family estimate expose the lower-order arithmetic carrier sought by `VIS-260`--`VIS-264`. For a fixed test with bounded norms, the normalized error remains at least certified only at `O(1/L)`. For a shrinking packet, the derivative contribution is larger by the packet's conditioning factor unless its width decreases sufficiently slowly.

Thus a proposed arithmetic residual of normalized size `c/L` still cannot be assigned a coefficient from Wang's leading theorem. A useful source for the accepted support-edge clue must either provide a lower-order term with a remainder small after the relevant packet norm amplification, or improve the error sufficiently that the candidate coefficient survives the packetization step.

## Prior-art and novelty assessment

The load-bearing mathematics is Wang's published Proposition 2.6 and proof of Theorem 2.2. The source itself states Theorem 2.2 only for fixed `g`; the norm-dependent family inequality above is obtained by retaining the explicit `||g||_infinity` and `||g'||_infinity` factors in Wang's displayed proof instead of collapsing them into `O_g`.

No novelty is claimed for this proof-reading as an independent analytic-number-theory theorem. It is a Mathia transfer audit: an exact statement of how much `T`-dependence the published proof already supports and how that budget composes with the packet-conditioning requirements of the existing visual branch.

A stronger source may give better seminorm dependence, moving-support uniformity, or a lower-order expansion. Any such result should supersede the corresponding gate rather than be forced into this bound.

## Boundary and falsification

The family estimate assumes one fixed pair `lambda<theta`. It does not control constants as either parameter varies with `T`. It also assumes each `g_T` is real, even, smooth, compactly supported inside the fixed interval, exactly matching the structural test class used in the proof.

The packet example is only a scaling diagnostic. It does not prove that the specific cusp-adapted signed packet used elsewhere in the branch has amplitude exponent `A`, nor that the displayed sufficient conditions are sharp. A faithful application must compute the actual smooth test's sup and derivative norms after all moment cancellations, mollification, translations, and normalizations.

The conclusion would be falsified if some earlier step of Wang's Proposition 2.6 carried an unrecorded dependence on `g`; it does not, because Proposition 2.6 is a uniform estimate for `F_I(x)` before `g` is introduced. It would also need revision if a later version of the source materially changes that proof or its uniformity range.

No untouched confirmation-zero data are used.

## Research consequence

The accepted Montgomery support-edge thread now has a more precise theorem-interface test. For any proposed smooth packet inside a fixed admissible support margin, compute `||g_T||_infinity` and `||g_T'||_infinity` first and compare them against

`||g_T'||_infinity/L + ||g_T||_infinity [1/L + T^(lambda-theta)L].`

If this tends to zero, Wang's proof already certifies the leading local Montgomery law for that moving family; searching for another theorem merely to remove the words "fixed `g`" would be wasted effort. The live obstruction then moves to what the theorem does not contain: a moving support edge, bounded/polylogarithmic source localization, or a lower-order arithmetic term with packet-compatible remainder.

This is a natural stopping boundary for the current invocation. The next useful step is not another reformulation of Wang's leading theorem, but an explicit comparison between this seminorm budget and the exact smooth realization of the accepted cusp packet, or a source carrying the desired lower-order term itself.
