# PF-270 — post-propagation smoothing needs only one-sided graph locality

**Status:** `EXACT-DERIVED + ONE-SIDED-GRAPH-LOCALITY + POST-PROPAGATION-SMOOTHING + HIGH-LOW-BLOCK-DECAY + ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-269-pre-propagation-robin-smoothing-is-an-overstrong-gate|PF-269]] shows that the normalized Robin conversion need not gain any positive transverse derivative before propagation: in the exact matched calibration the energy-normalized injection is `B=I/2`, so `BK^R` is unbounded for every `R>0`, while fixed positive longitudinal separation still gives smoothing of every order. [[research/prime_flute/findings/PF-244-one-sided-seam-domination-does-not-imply-separated-poisson-smoothing|PF-244]] identifies the opposite failure: a bounded boundary conversion can send arbitrarily high input into genuinely low output before propagation, where the longitudinal damping is cheap.

The missing distinction is not “smoothing versus no smoothing.” It is **one-sided graph locality**. Let `K>=kappa I>0` be the transverse scale, let `B` be the boundary conversion acting before the far propagation, and suppose for some `q>0` that

\[
\boxed{
C_q:=\overline{K^{-q}BK^q}\in\mathcal B(H).
}
\tag{1}
\]

This condition says that `B` is order zero in the one orientation that matters: high input cannot be converted into much lower `K`-frequency faster than `q` powers. It does **not** say that `B` gains derivatives. Indeed `B=I/2` satisfies (1) for every `q` while `BK^R` remains unbounded for every `R>0`.

If `P:H\to G` is the remaining far-propagation/observation map and fixed positive separation gives

\[
\boxed{PK^q\in\mathcal B(H,G),}
\tag{2}
\]

then for every `0<=R<=q`,

\[
\boxed{
PBK^R=(PK^q)\,C_q\,K^{R-q}\in\mathcal B(H,G).
}
\tag{3}
\]

Thus the strict exponent `R>1` required by [[research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing|PF-243]] does not require any positive-order standalone estimate on `B`. A sufficient local currency is instead **any one-sided graph-locality order `q>1`**, together with the corresponding separated propagation estimate. The natural target `q=2` is already the exact regularity class proved for the hypercycle/corridor coordinate transports in [[research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound|PF-255]] and [[research/prime_flute/findings/PF-256-variable-corridor-graph-equivalence-transfers-two-derivative-locality-to-the-actual-transverse-scale|PF-256]].

This sharply narrows the surviving Robin question. The actual normalized boundary conversion need not be a smoothing operator. It only has to preserve enough of the `K_a` graph scale in the **high-input-to-low-output direction** before the designated positive-separation leg acts.

## Claim

Let `H,G` be Hilbert spaces, let `K` be positive self-adjoint on `H` with

\[
K\ge\kappa I,
\qquad \kappa>0,
\tag{4}
\]

and let `B\in\mathcal B(H)`. Fix `q>0` and assume the operator initially defined on `Dom(K^q)` by

\[
K^{-q}BK^q
\tag{5}
\]

has a bounded extension `C_q\in\mathcal B(H)`. Let `P:H\to G` be bounded and assume `PK^q`, initially defined on `Dom(K^q)`, also has a bounded extension.

Then:

1. for every `0<=R<=q`, `PBK^R` has a bounded extension and
   \[
   \boxed{
   \|PBK^R\|
   \le
   \|PK^q\|\,\|C_q\|\,\kappa^{R-q};
   }
   \tag{6}
   \]
2. if `E_K` is the spectral resolution of `K`, then for `\kappa<=M<N`,
   \[
   \boxed{
   \|E_K([\kappa,M])\,B\,E_K([N,\infty))\|
   \le
   \|C_q\|\left(\frac MN\right)^q;
   }
   \tag{7}
   \]
3. (1) is therefore a quantitative high-to-low spectral-conversion condition, not a Sobolev smoothing condition;
4. if `P=e^{-dK}` for any `d>0`, then (2) holds for every finite `q`, with
   \[
   \|e^{-dK}K^q\|=\sup_{\lambda\ge\kappa}\lambda^qe^{-d\lambda}<\infty;
   \tag{8}
   \]
5. consequently, for a fixed positive-separation Poisson leg, any `q>1` satisfying (1) supplies a nonempty admissible range `1<R<=q`.

No commutation of `B` with `K` is assumed.

## 1. Moving derivatives through an order-zero conversion

By definition of `C_q`, on `Dom(K^q)` one has

\[
BK^q=K^qC_q.
\tag{9}
\]

For `0<=R<=q`, functional calculus gives a bounded negative power

\[
K^{R-q}\in\mathcal B(H),
\qquad
\|K^{R-q}\|\le\kappa^{R-q}.
\tag{10}
\]

On `Dom(K^R)` the factorization

\[
PBK^R
=P\,BK^qK^{R-q}
=(PK^q)C_qK^{R-q}
\tag{11}
\]

is therefore legitimate on a core and the right side is bounded on all of `H`. This proves (3) and (6).

The point is that the `q` derivatives are not paid by `B`. They are **transported through** `B` and then paid by the far operator `P`. PF-269's matched calibration is the extreme example: for `B=I/2`, `C_q=I/2` for every `q`, even though `BK^R` itself is unbounded.

## 2. The same hypothesis is exactly a high-to-low block estimate

Let

\[
E_{\le M}=E_K([\kappa,M]),
\qquad
E_{\ge N}=E_K([N,\infty)).
\]

Equation (9) gives

\[
E_{\le M}BE_{\ge N}
=E_{\le M}K^qC_qK^{-q}E_{\ge N}.
\tag{12}
\]

Spectral calculus yields

\[
\|E_{\le M}K^q\|\le M^q,
\qquad
\|K^{-q}E_{\ge N}\|\le N^{-q},
\tag{13}
\]

which proves (7).

The **orientation matters**. Boundedness of `K^qBK^{-q}` controls low input converted to high output. PF-243's dangerous channel is the reverse one: high boundary input converted to low output before propagation. The correct graph conjugation is therefore precisely `K^{-q}BK^q`.

This also gives a clean interpretation of [[research/prime_flute/findings/PF-244-one-sided-seam-domination-does-not-imply-separated-poisson-smoothing|PF-244]]. Its bad mixer has an order-one high-to-fixed-low block, so (7) fails for every `q>0`; equivalently the conjugation (1) cannot be bounded. By contrast, an order-zero conversion such as the matched `I/2` has perfect graph locality despite having no smoothing at all.

## 3. PF-255/PF-256 already use the right regularity currency

PF-255 proves for the exact hypercycle half-density transport `V_c`, with `K_0=A^{1/2}`,

\[
A^{-1}V_cA\in\mathcal B(H).
\tag{14}
\]

Since `A=K_0^2`, this is exactly

\[
K_0^{-2}V_cK_0^2\in\mathcal B(H),
\tag{15}
\]

the case `q=2` of (1). PF-256 transports the same two-derivative graph locality to the actual variable corridor scale `K_a=T_a^{1/2}`:

\[
\boxed{K_a^{-2}V_cK_a^2\in\mathcal B(H)}
\tag{16}
\]

uniformly on the canonical tail, together with the corresponding `(M/N)^2` high-to-low block bound.

Those findings were already proving the correct type of estimate. Their significance after PF-269 is stronger: **two-derivative graph locality is enough to let later positive propagation absorb every input weight `R<=2`**. No intermediate claim that `V_cK_a^R` is globally smoothing is needed.

The same regularity target is therefore natural for the still-unresolved fixed-axis normalized Robin conversion from [[research/prime_flute/findings/PF-257-normalized-robin-injection-is-a-polar-free-resolvent-transform|PF-257]]. Its physical factor is

\[
B_w=X_w(I+X_w^*X_w)^{-1},
\tag{17}
\]

and the useful question is now whether the complete factor that acts **before the designated far propagation** satisfies (1) for some `q>1`, preferably `q=2`.

## 4. Why the finite-seam proportional-block obstruction is compatible

[[research/prime_flute/findings/PF-268-lowest-finite-seam-pole-forbids-bare-supercritical-separated-weighting|PF-268]] finds proportional high-mode blocks of the naked finite relative seam with individual entries of order `N^{-2}` and uses them to rule out `R>1` pre-propagation weighting. That result does not conflict with (7).

Graph locality controls **scale separation**. If output and input are proportional, say `M=cN` with fixed `0<c<1`, the right side of (7) is merely the fixed constant `c^q`; it promises no extra power of `N`. Such proportional output remains at high transverse frequency and is exactly the region on which fixed positive propagation is exponentially expensive.

The region propagation cannot pay for is instead `M/N\to0`, especially high input converted to bounded or slowly growing output. Equation (7) is targeted precisely at that region. Thus PF-268 and PF-270 divide the obstruction correctly: proportional high-high tails may survive before propagation, while genuinely high-to-low leakage must be ruled out by graph locality.

## 5. Consequence for the PF-243 far-leg gate

PF-243's four source-to-bulk energy maps already place the final estimate on a leg observed a fixed positive `X`-distance from its forcing boundary. PF-269 says not to factor those estimates through standalone positive-order smoothing of the Robin injection. PF-270 gives a weaker sufficient factorization.

If one of those far legs can be written, after the exact mass/unitary normalizations, as

\[
\mathcal T_{\rm far}=P_{\rm far}B_{\rm unsmoothed},
\tag{18}
\]

where `B_unsmoothed` includes every boundary conversion/reflection/conjugation factor that acts before the relevant positive separation, then it is enough to prove uniformly on the canonical tail

\[
K_a^{-q}B_{\rm unsmoothed}K_a^q\in\mathcal B,
\qquad
P_{\rm far}K_a^q\in\mathcal B
\tag{19}
\]

for one `q>1`. Equation (3) then gives the required right-weighted estimate for every `1<R<=q`.

The especially natural target is `q=2`, because it matches PF-255/PF-256 and leaves the full interval `1<R<2` available. But PF-270 does **not** assert that the actual sheared/Hardy Robin-Poisson legs already admit the factorization (18), that their unsmoothed boundary factor satisfies (19), or that reflection cycles preserve the same graph class. If the physical map cannot be separated cleanly into `P_far B_unsmoothed`, the equivalent task is to prove the same one-sided graph transport directly for the complete pre-separation conversion rather than isolate an artificial factor.

## 6. Prior-art and novelty audit

The operator identity (11), the spectral-block consequence (7), and the fact that a positive semigroup gains arbitrary powers after fixed positive time are elementary consequences of spectral calculus. General semigroup off-diagonal estimates, Davies--Gaffney methods, and their use in functional calculus are classical; [[research/prime_flute/findings/PF-260-davies-gaffney-closes-short-time-intrinsic-six-fractional-window|PF-260]] already records that prior-art boundary, while PF-255/PF-256 already use graph conjugation to quantify high-to-low locality.

A targeted literature audit of semigroup/off-diagonal and spectral-multiplier estimates found the expected established general theory and no reason to claim a new abstract theorem here. No external theorem is imported into the proof of (6)--(7), so no new source entry is required.

The project-specific delta is the **logical reduction of the current Prime-Flute gate** after PF-268/PF-269: the missing boundary conversion need not gain derivatives; it only needs enough one-sided graph locality to move derivatives through itself until the already-required positive-separation operator can pay for them. This identifies a strictly weaker, orientation-correct proof obligation and explains why the two-derivative estimates already proved for the geometric transports are the relevant currency.

## 7. Boundaries and falsification

- Boundedness of `B` alone does not imply (1); PF-244 is the canonical counterexample.
- The opposite conjugation `K^qBK^{-q}` is not a substitute for (1). It controls the wrong direction of spectral conversion.
- The constant in (1) and the separated propagation norm in (2) must be uniform in the canonical tail parameters needed by PF-243. A bound deteriorating uncontrollably with `s`, the corridor index, or homotopy parameter `t` does not close the local gate.
- Equation (2) is not silently granted for the actual sheared/Hardy far leg. It must be proved in the physical realization, or absorbed into a direct estimate for the full source-to-bulk map.
- Any Robin reflection or congruence factor acting before the paid positive separation must either satisfy the same one-sided graph control or be included inside `B_unsmoothed`; otherwise a hidden PF-244-type conversion can remain.
- PF-270 proves no trace-class reassembly, physical `P/H` recoupling, finite-pant completion, global scattering/determinant theorem, prime/control separation, zeta-zero statement, or RH consequence.

## Decisive next test

Use the exact actual-seam-normalized factorization underlying the four PF-243 far legs and isolate **all** spectral conversion that occurs before the fixed positive source-to-observation separation. Then prove, for that complete unsmoothed conversion and the actual transverse scale `K_a`, either

\[
\boxed{
\sup_{s,t}\|K_a^{-2}B_{s,t}K_a^2\|<\infty
}
\tag{20}
\]

(or any fractional/integer order `q>1`) together with the corresponding uniformly separated bound `P_{s,t}^{\rm far}K_a^q\in\mathcal B`, or construct a canonical high-input sequence showing that no `q>1` one-sided graph-locality exponent survives.

A positive `q=2` result would make some `1<R<2` available immediately through (3), without ever requiring the false/overstrong standalone gate `B_{s,t}K_a^R\in\mathcal B`. A negative result must exhibit genuine high-to-low conversion before the paid separation; proportional high-high tails of the PF-268 type are not sufficient.