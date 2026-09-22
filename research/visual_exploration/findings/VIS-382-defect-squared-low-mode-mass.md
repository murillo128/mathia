# VIS-382 — order-one output orientation forces defect-squared low-mode mass

## Claim

Continue with the finite-dimensional source-packet setup of `VIS-381`. Let

`Delta_H = sum_j ad_(H_j)^* ad_(H_j)`

be the positive semidefinite joint commutator Laplacian, let `P_0` be the orthogonal projection onto `ker Delta_H`, and let `G` be a Hermitian Gram tangent with defect energy

`epsilon_G^2 = <G, Delta_H G>_F`.

Let `C=C(H_1,...,H_m)` be an admitted bounded positive rational source output, write

`q = ||[G,C]||_F`,

and let

`omega = omega(C) = lambda_max(C)-lambda_min(C)`

be its spectral spread. Assume the nontrivial case `q>0`, hence `omega>0`.

For every `beta>1`, define the orientation-adapted threshold

`tau_beta = beta omega^2 epsilon_G^2 / q^2`.

Then

`||P_(0,tau_beta] G||_F >= (q/omega) sqrt(1-1/beta)`.

In particular, at `beta=2`,

`tau_2 = 2 omega^2 epsilon_G^2/q^2`

and

`||P_(0,tau_2] G||_F >= q/(sqrt(2) omega)`.

Thus order-one output orientation under bounded spectral spread forces order-one Gram-tangent mass into positive commutator modes whose eigenvalues are on the **defect-squared scale** `O(epsilon_G^2)`. This sharpens the scale-dependent localization statement of `VIS-381`: one does not merely need mass somewhere below an arbitrary threshold satisfying `epsilon_G^2 << tau`; persistent orientation itself furnishes a threshold proportional to `epsilon_G^2` at which a fixed fraction of the required noncommuting mass must already be present.

For a sequence with

`q_T >= c > 0`,

`omega_T <= Omega < infinity`,

and `epsilon_T -> 0`, one obtains for every fixed `beta>1`

`||P_(0, beta Omega^2 epsilon_T^2/c^2] G_T||_F >= (c/Omega) sqrt(1-1/beta)`.

So any bounded-spread output retaining order-one orientation while the source defect vanishes forces a uniformly nonzero amount of Gram-tangent mass into an `O(epsilon_T^2)` commutator band.

**Evidence/status:** `EXACT-DERIVED + SPECTRAL LOCALIZATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No sufficiency claim is made. The result does not identify the low eigenspace geometrically, show that it carries arithmetic information, construct a recovery mechanism, or imply a new zeta/RH criterion.

## 1. Remove the exact commutant component

Set

`g = (I-P_0)G`.

As in `VIS-381`, every matrix in `ker Delta_H` commutes with all source coordinates and hence with every admitted rational source output `C`. Therefore

`[G,C]=[g,C]`.

The Frobenius operator norm of `ad_C` is bounded by the spectral spread of `C`, so

`q = ||[g,C]||_F <= omega ||g||_F`.

Consequently

`||g||_F^2 >= q^2/omega^2`.

This lower bound is purely geometric: order-one output orientation requires at least `q/omega` total Gram-tangent mass outside the exact joint commutant.

## 2. Defect energy bounds the high spectral tail

Let `nu_G` be the spectral measure of `g` for `Delta_H` on the positive spectrum. Then

`||g||_F^2 = integral_(lambda>0) d nu_G(lambda)`

and

`epsilon_G^2 = integral_(lambda>0) lambda d nu_G(lambda)`.

For every `tau>0`, the standard spectral Markov/Chebyshev estimate gives

`||P_(tau,infty)G||_F^2`
` = nu_G((tau,infty))`
` <= epsilon_G^2/tau`.

At the orientation-adapted threshold

`tau=tau_beta=beta omega^2 epsilon_G^2/q^2`,

this becomes

`||P_(tau_beta,infty)G||_F^2 <= q^2/(beta omega^2)`.

Subtracting the high-mode mass from the total positive-spectrum mass yields

`||P_(0,tau_beta]G||_F^2`
` = ||g||_F^2 - ||P_(tau_beta,infty)G||_F^2`
` >= q^2/omega^2 - q^2/(beta omega^2)`
` = (q^2/omega^2)(1-1/beta)`.

Taking square roots proves the claim.

The argument uses no choice of eigenbasis and remains valid through degeneracies or eigenvalue crossings.

## 3. Uniform sequence consequence

Suppose `q_T>=c>0` and `omega_T<=Omega`. The exact threshold satisfies

`tau_(beta,T)`
` = beta omega_T^2 epsilon_T^2/q_T^2`
` <= beta Omega^2 epsilon_T^2/c^2`.

Because the low-mode projector mass is monotone in its threshold,

`||P_(0, beta Omega^2 epsilon_T^2/c^2]G_T||_F`
` >= ||P_(0,tau_(beta,T)]G_T||_F`
` >= (q_T/omega_T)sqrt(1-1/beta)`
` >= (c/Omega)sqrt(1-1/beta)`.

Hence the relevant approximate-commutant channel cannot live merely at some unspecified scale tending to zero. Under persistent bounded-spread orientation it must carry order-one Gram mass already at spectral scale proportional to the square of the commutator defect.

This is stronger than the asymptotic corollary in `VIS-381`, which allowed any threshold with `epsilon_T^2 << tau_T << 1`. The present estimate reaches the borderline `tau_T = Theta(epsilon_T^2)` once the observed output orientation `q_T` and spread `omega_T` are included in the scale.

## 4. Interpretation

`VIS-380` showed that a collapsing commutator gap is necessary for bounded output orientation to survive vanishing defect. `VIS-381` showed that the Gram tangent must actually align with the collapsing low modes rather than merely coexist with them. The present result fixes the scale of that alignment.

The obstruction can therefore be stated more sharply: if an admissible source-packet construction has vanishing defect but its Gram tangent carries vanishing mass in every positive commutator band of width `O(epsilon_G^2)`, then no bounded-spread rational source output can retain order-one orientation.

Conversely, observing order-one low-mode mass at this scale is only a necessary condition. A universal near-reducibility, duplicated coordinate, block decomposition, normalization artifact, or other source-independent degeneracy could generate exactly the same spectral concentration. The low eigenspace still has to be interpreted and stress-tested before it can count as an arithmetic channel.

## Controls and boundaries

The nontrivial statement assumes `q>0`. If `q=0`, there is no retained output orientation to explain. If `omega=0`, then `C` is scalar on the relevant finite-dimensional space and necessarily `q=0`.

If `epsilon_G=0`, then `G` lies in `ker Delta_H`, so it commutes with every admitted rational source output and again `q=0`. Thus the formula never requires interpreting a positive-orientation case with a zero denominator hidden in the threshold.

No lower bound on the dimension of the low eigenspace follows. The required mass may lie in one mode or a highly degenerate band. Nor does the estimate say that the low spectral vectors are recoverable from source data without already knowing `G`; it is a necessary localization statement, not a reconstruction algorithm.

The spectral-spread normalization remains essential. Allowing `omega(C)` to diverge can preserve `q` without forcing the same bounded-scale conclusion, exactly as in the earlier source-packet obstruction chain.

## Prior-art and novelty audit

The proof is an immediate combination of standard finite-dimensional spectral calculus with the elementary Markov/Chebyshev tail estimate for a nonnegative spectral measure and the standard commutator bound

`||[X,C]||_F <= omega(C)||X||_F`.

These ingredients belong to the same matrix Poincare / approximate-commutant background already bounded as prior art in `VIS-380` and `VIS-381`. No novelty is claimed for the abstract inequality, spectral tail bound, or projector argument.

The Mathia-specific contribution is narrower: applying those standard facts to the exact source-packet defect/orientation variables isolates the **defect-squared spectral scale** forced by persistent bounded-spread output orientation. This should be treated as a sharpened control boundary for the current representation program, not as a new theorem of operator theory.

## Research consequence

The next discriminating question is whether admissible source-derived structure can force, detect, or characterize order-one Gram-tangent mass in the spectrum of `Delta_H` at `lambda=O(epsilon_G^2)` without importing hidden target information.

That is a separate research question. Any positive mechanism must distinguish arithmetic/source-specific defect-squared localization from generic near-reducibility and other matched matrix controls.

## Dependencies

- `research/visual_exploration/findings/VIS-381-bounded-output-orientation-requires-low-commutator-mode-alignment.md`
- the source-packet setup and rational-output assumptions inherited there from `VIS-380`
