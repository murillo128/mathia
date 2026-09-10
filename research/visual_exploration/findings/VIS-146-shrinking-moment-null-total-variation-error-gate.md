# VIS-146 — shrinking moment-null packets cannot beat total-variation-linear error by rescaling

## Claim

Let `nu_b` be a finite signed Borel measure supported in `[-b,b]`, with `b>0`, total variation

`T_b = ||nu_b||_TV`,

and even packet moments

`m_(2j)(nu_b) = integral q^(2j) dnu_b(q)`.

Then for every integer `j>=1`,

`|m_(2j)(nu_b)| <= b^(2j) T_b`.

Consequently, if the first retained packet moment is normalized by

`|m_(2j)(nu_b)| = 1`,

then necessarily

`T_b >= b^(-2j)`.

For the support-edge design of `VIS-144`--`VIS-145`, impose `m_2(nu_b)=0`. If a smooth finite-window source correction `H` has finite sixth absolute moment and

`Delta_H(q)=integral H(x)[1-cos(2*pi*q*x)]dx`,

then

`integral Delta_H(q)dnu_b(q)`
` = -(2/3)pi^4 mu_4(H)m_4(nu_b) + R_6`,

where

`mu_4(H)=integral x^4 H(x)dx`,

`M_6(H)=integral |x|^6 |H(x)|dx`,

and

`|R_6| <= (4/45)pi^6 M_6(H)b^6 T_b`.

Thus a quartic-normalized second-moment-null packet, `m_2=0` and `|m_4|=1`, has the unavoidable cost

`T_b >= b^(-4)`.

More generally, packet rescaling cannot improve a signal against an uncertainty controlled only in the same total-variation norm. If the desired surviving term on `[-b,b]` is `A_(2j) q^(2j)` and an unknown deterministic error `e_b(q)` is known only through

`|e_b(q)| <= epsilon_b`,

then for every packet

`|A_(2j)m_(2j)(nu_b)| <= |A_(2j)| b^(2j) T_b`,

while

`sup_(||e_b||_infty<=epsilon_b) |integral e_b(q)dnu_b(q)| = epsilon_b T_b`.

Therefore the best possible robust signal-to-error ratio allowed by these envelopes is at most

`|A_(2j)| b^(2j) / epsilon_b`.

No scalar rescaling of the packet and no growth of `T_b` changes that ratio. In particular, a quartic post-cancellation carrier can dominate a total-variation-linear theorem/transfer uncertainty uniformly only if its coefficient and bandwidth satisfy the necessary gate

`epsilon_b < |A_4| b^4`

for strict worst-case separation, and asymptotically strong separation requires `epsilon_b/(|A_4|b^4) -> 0`.

**Evidence/status:** `EXACT-DERIVED + SIGNED-MEASURE/MOMENT CAPACITY + MINIMAX ERROR OBSTRUCTION + NEGATIVE/REDESIGN CONTROL + NO-NOVELTY-CLAIM`.

No finite-height zeta coefficient, Rudnick--Sarnak uniformity improvement, stochastic covariance theorem, or RH implication is claimed.

## 1. A shrinking support has finite moment capacity per unit variation

Let `|nu_b|` be the variation measure. Because `|q|<=b` on the support,

`|m_(2j)(nu_b)|`
` = |integral q^(2j)dnu_b(q)|`
` <= integral |q|^(2j)d|nu_b|(q)`
` <= b^(2j) |nu_b|([-b,b])`
` = b^(2j) T_b`.

The estimate uses no positivity, symmetry, discreteness, or finite-complexity assumption. Extra vanishing moments such as `m_2=0` do not weaken it. Hence normalizing a surviving `2j`-th moment to order one costs at least `b^(-2j)` in total variation.

This already changes the interpretation of moment cancellation in a shrinking band. Cancelling a lower Taylor coefficient may remove a deterministic null term algebraically, but if the useful carrier first reappears two orders later, keeping that carrier macroscopic requires a correspondingly larger signed-measure norm unless the source coefficient itself grows with the external scale.

## 2. After second-moment cancellation the common finite-window channel is quartic

Taylor's theorem with bounded sixth derivative gives, for every real `u`,

`|(1-cos u) - u^2/2 + u^4/24| <= |u|^6/720`.

With `u=2*pi*q*x`, integrate against the signed kernel `H`:

`Delta_H(q)`
` = 2*pi^2 mu_2(H)q^2`
`   -(2/3)pi^4 mu_4(H)q^4`
`   + r_6(q)`,

with

`|r_6(q)| <= (4/45)pi^6 M_6(H)|q|^6`.

Integrating this identity against `nu_b` and imposing `m_2(nu_b)=0` yields the displayed quartic formula and remainder bound.

This strengthens the order statement in `VIS-145`. Under a common smooth finite-window centered-cosine representation, the first possible post-`m_2` deterministic distinction is not merely bounded by `O(b^4 T_b)`; when a nonzero fourth spatial moment exists, its explicit leading packet functional is `mu_4(H)m_4(nu_b)`.

If one also imposes `m_4=0`, the same Taylor argument moves the first possible common-channel distinction to sixth order and the generic moment-capacity cost to at least `b^(-6)` after unit normalization. Repeating moment cancellation therefore creates a ladder of increasingly expensive shrinking-support norms rather than a free sequence of null removals.

## 3. Total-variation-linear uncertainty creates a normalization-invariant gate

Let the desired retained contribution be exactly `S(q)=A_(2j)q^(2j)` on the packet band. Its packet response obeys

`|integral S dnu_b| <= |A_(2j)| b^(2j) T_b`.

Now suppose the theorem, transfer, approximation, or model remainder is represented only by an unknown function `e_b` satisfying `||e_b||_infty<=epsilon_b`. By the defining dual bound for total variation,

`|integral e_b dnu_b| <= epsilon_b T_b`.

This upper bound is sharp as an uncertainty-class statement: in the polar decomposition `dnu_b=h_b d|nu_b|`, where `|h_b|=1` almost everywhere with respect to `|nu_b|`, the admissible choice `e_b=epsilon_b h_b` attains `epsilon_b T_b`.

Therefore a packet that must work uniformly over the whole allowed error class can satisfy

`|integral S dnu_b| > sup |integral e_b dnu_b|`

only if

`|A_(2j)| |m_(2j)(nu_b)| > epsilon_b T_b`.

Since `|m_(2j)|/T_b<=b^(2j)`, a necessary condition is

`epsilon_b < |A_(2j)| b^(2j)`.

This is the key obstruction: multiplying all packet weights by a large factor multiplies signal and the admitted total-variation-linear error by the same factor. Normalization can make the plotted or deterministic mean amplitude large, but it cannot improve the robust separation certified by this error model.

For the quartic channel of the accepted moment-cancelled clue, `A_4=-(2/3)pi^4 mu_4(H_L)` when the actual finite-height zeta-minus-finite-CUE correction has the common smooth kernel representation. A uniform transfer/theorem remainder bounded by `epsilon_L` must therefore beat the scale

`|mu_4(H_L)| b_L^4`

up to the explicit constant before packet optimization can matter. If only a weaker bound is available, no signed reweighting inside `|q|<=b_L` can repair the deficit under total-variation control alone.

## 4. The quartic `b^-4` variation exponent is attainable by a fixed two-scale shape

The lower bound `T_b>=b^-4` for `m_4=1` is not an artifact of a loose estimate. Fix any `0<rho<1` and define

`nu_b^(rho)`
` = [b^-4/(1-rho^2)] [delta_b - rho^-2 delta_(rho b)]`.

Then

`m_2(nu_b^(rho))`
` = [b^-4/(1-rho^2)] [b^2-rho^-2(rho b)^2]`
` = 0`,

while

`m_4(nu_b^(rho))`
` = [b^-4/(1-rho^2)] [b^4-rho^-2(rho b)^4]`
` = 1`.

Its total variation is

`||nu_b^(rho)||_TV`
` = b^-4 (1+rho^-2)/(1-rho^2)`.

Hence the exponent `b^-4` is sharp for a bounded-complexity packet family. If an even packet is required, replace each point mass by the average of its `+q` and `-q` copies; all even moments and the total variation are unchanged.

The design constant can be optimized over `rho`, but that changes only a fixed factor. It cannot alter the `b^-4` law or the normalization-invariant error gate above.

## 5. Stress tests and boundaries

The minimax gate concerns deterministic uncertainty bounded in `L^infinity` on the packet band and then integrated against the signed packet. A theorem remainder controlled in a stronger norm, with known sign, orthogonality, oscillation, covariance, or another structure correlated with the moment-null packet may admit a better estimate. Such structure must be proved; it is exactly the kind of additional information carrier that the current clue is looking for.

Likewise, a source coefficient may grow with height/window scale. The conclusion is not that every quartic channel dies, but that its relevant quantity is the combined scale `|A_4(L)|b_L^4` versus the per-mode error envelope, not the visually or algebraically normalized packet amplitude.

The result is deterministic and says nothing by itself about stochastic variance. A signed packet with large total variation can have covariance cancellations, but those require the actual covariance kernel. Total variation is therefore a hard generic cost and not a complete noise model.

The sixth-order Taylor remainder is useful only when `M_6(H_L)b_L^2` is small compared with `|mu_4(H_L)|` after the common factors are removed. If the moments of `H_L` grow nonuniformly, that nonuniformity remains a legitimate escape and must be carried explicitly.

No untouched confirmation-zero data are used.

## 6. Prior-art and novelty audit

The measure inequality `|integral f dnu|<=||f||_infinity ||nu||_TV` and the moment-capacity bound are standard signed-measure/total-variation facts. Vanishing moments cancelling low-order Taylor or polynomial terms are standard harmonic-analysis and filter-design structure. The cosine expansion is elementary. No general theorem novelty is claimed.

The Mathia-specific value is their composition with the shrinking Rudnick--Sarnak-safe companion architecture of `VIS-141`--`VIS-145`. That composition shows that the apparent advantage of algebraic moment cancellation does not remove the normalization pressure identified earlier: once the useful source term moves to order `2j`, any error controlled only linearly by packet total variation faces the same `b^(2j)` support-capacity gate.

## Research consequence

The accepted support-edge clue should no longer treat packet normalization as a degree of freedom that might rescue a weak quartic arithmetic term. Before designing additional signed packets, derive the actual finite-height zeta-minus-finite-CUE coefficient `A_4(L)` and the strongest theorem/transfer error envelope `epsilon_L` in the same frozen companion coordinate.

If `epsilon_L/(|A_4(L)|b_L^4)` fails to tend to zero, quartic moment cancellation cannot yield asymptotically strong robust separation under a total-variation-linear error bound, regardless of scalar normalization or bounded-complexity packet shape. If that ratio is favorable, then packet shape, sixth-order remainder, stochastic variance, and cross-window covariance become meaningful next questions.

Do not add an `m_4=0` packet merely to cancel another universal term unless a sixth-order source coefficient and its error budget are already identified: the generic support cost then worsens from `b_L^-4` to at least `b_L^-6` after unit moment normalization.