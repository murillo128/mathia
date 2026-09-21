# VIS-349 — finite cross-order Wang interactions are confluent exponential polynomials

## Claim

Let Wang's exact summatory-remainder multiplier be

`m(xi)=4(1+i xi)/(4+xi^2)`.

For each large `X`, consider a finite translated-dilate bank

`M_X(xi)=sum_j c_(j,X) exp(-i b_(j,X) xi) m(a_(j,X) xi)`,

with `a_(j,X)>0` and frequency-independent complex coefficients. Use the exact high-frequency coefficients from `VIS-343`,

`beta_(2n+1)=4 i (-4)^n`,
`beta_(2n+2)=4 (-4)^n`,

and for each translation `b` and order `k>=1` define

`S_(b,k,X)=sum_(j:b_(j,X)=b) c_(j,X) a_(j,X)^(-k)`,

`P_(k,X)(xi)=sum_b S_(b,k,X) exp(-i b xi)`.

Fix an integer `q>=1` and define the truncated interacting tail

`E_(q,X)(xi)=sum_(k=1)^q beta_k xi^(q-k) P_(k,X)(xi)`.

Then the following statements hold without assuming that any lower moment polynomial vanishes.

First, `E_(q,X)` is exactly an exponential polynomial with polynomial coefficients:

`E_(q,X)(xi)=sum_b exp(-i b xi) Q_(b,q,X)(xi)`,

where

`Q_(b,q,X)(xi)=sum_(k=1)^q beta_k S_(b,k,X) xi^(q-k)`

has degree at most `q-1`.

Second, if `B_X` is the set of distinct translations appearing in these first `q` moment layers, then

`[prod_(b in B_X) (D+i b)^q] E_(q,X)=0`,

where `D=d/dxi`. Thus the entire finite interaction among the first `q` Wang tail orders lies in the classical confluent exponential-polynomial space spanned by

`xi^r exp(-i b xi)`, `b in B_X`, `0<=r<=q-1`.

Third, exact cross-order cancellation does not create a new algebraic escape. If `E_(q,X)` vanishes on a nonempty interval, then it vanishes identically, and linear independence of the confluent exponential basis forces

`S_(b,k,X)=0`

for every `b in B_X` and every `1<=k<=q`. Equivalently, every `P_(k,X)` through order `q` vanishes identically. Exact cancellation between different nonzero tail orders on an interval is therefore impossible unless the ordinary phase-fiber moments already cancel order by order.

Fourth, local approximate cancellation also reduces exactly to this finite-dimensional concentration problem. Let

`T_(q+1,X)=sum_j |c_(j,X)| a_(j,X)^(-(q+1))`.

With the same finite constant `C_q` from `VIS-348`, the exact remainder identity gives

`xi^q M_X(xi)=E_(q,X)(xi)+R~_(q,X)(xi)`,

with

`|R~_(q,X)(xi)| <= C_q T_(q+1,X)/xi`, `xi>0`.

Hence, if `J_X subset [X,2X]` and

`sup_(xi in J_X) |M_X(xi)| <= C_0 X^(-(q+1))`,

then necessarily

`sup_(xi in J_X) |E_(q,X)(xi)|`
` <= [2^q C_0 + C_q T_(q+1,X)]/X`.

This implication requires no exact lower-moment cancellation. Any finite-window gain attributed to interaction among several nonzero inverse-frequency orders is therefore a claim that a confluent exponential polynomial is unusually small on `J_X`, with its phase geometry, polynomial multiplicities and coefficient conditioning exposed explicitly.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL CONFLUENT EXPONENTIAL-POLYNOMIAL REDUCTION + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This result does not provide a sharp Turán--Nazarov-style lower bound for the variable-parameter confluent system. It therefore does not by itself exclude approximate cross-order concentration purchased by growing phase count, coalescing phases, shrinking windows or ill-conditioned polynomial coefficients. Frequency-dependent coefficients, source-dependent coefficients, infinite expansions and direct signed arithmetic cancellation in `G` remain outside the claim.

## 1. Reuse the exact Wang remainder with no moment-vanishing assumption

`VIS-348` defines, for fixed `q`,

`R_q(z)=m(z)-sum_(k=1)^q beta_k z^(-k)`

and proves the global bound

`|R_q(z)| <= C_q z^(-(q+1))`, `z>0`,

for a finite constant `C_q` depending only on `q`.

Substituting `z=a_(j,X) xi`, summing the bank and grouping translations gives the exact finite-order decomposition

`M_X(xi)`
` = sum_(k=1)^q beta_k xi^(-k) P_(k,X)(xi) + R_(bank,q,X)(xi)`,

with

`|R_(bank,q,X)(xi)|`
` <= C_q xi^(-(q+1)) T_(q+1,X)`.

Multiplying by `xi^q` yields

`xi^q M_X(xi)`
` = sum_(k=1)^q beta_k xi^(q-k) P_(k,X)(xi)`
`   + xi^q R_(bank,q,X)(xi)`
` = E_(q,X)(xi)+R~_(q,X)(xi)`,

and therefore

`|R~_(q,X)(xi)| <= C_q T_(q+1,X)/xi`.

Unlike `VIS-348`, no assumption `P_1=...=P_(q-1)=0` has been made. All low-order terms are retained and allowed to interact.

## 2. Grouping by phase produces a confluent exponential polynomial

Insert

`P_(k,X)(xi)=sum_b S_(b,k,X) exp(-i b xi)`

into `E_(q,X)`. Finite interchange gives

`E_(q,X)(xi)`
` = sum_b exp(-i b xi)`
`   [sum_(k=1)^q beta_k S_(b,k,X) xi^(q-k)]`.

The bracket is the polynomial `Q_(b,q,X)` of degree at most `q-1`. Thus the cross-order interaction does not produce a new functional class: for each fixed `X` it is a finite sum of polynomially weighted exponentials.

For one term `exp(-i b xi)Q(xi)` with `deg Q<q`,

`(D+i b)^q [exp(-i b xi)Q(xi)]`
` = exp(-i b xi) Q^(q)(xi)`
` = 0`.

Operators `D+i b` commute, so multiplying these factors over the distinct active phases annihilates the complete `E_(q,X)`. Its ambient dimension is at most `q |B_X|`, with any absent polynomial coefficients lowering that dimension.

This ODE description is a representation identity, not a concentration theorem. Its use is to expose exactly what finite cross-order interaction can and cannot contain.

## 3. Exact cross-order cancellation collapses to ordinary moment cancellation

Suppose `E_(q,X)` vanishes on a nonempty interval. It is entire as a finite sum of polynomial-exponential terms, so the identity theorem gives `E_(q,X) == 0`.

For distinct translations `b`, the functions

`xi^r exp(-i b xi)`, `0<=r<=q-1`,

are linearly independent. Equivalently, they are the standard generalized-eigenfunction basis of the constant-coefficient differential operator with characteristic roots `-i b` and multiplicity `q`. Therefore every coefficient polynomial `Q_(b,q,X)` must vanish identically.

But

`Q_(b,q,X)(xi)=sum_(k=1)^q beta_k S_(b,k,X) xi^(q-k)`

and every `beta_k` is nonzero. Distinct powers of `xi` are independent, so

`S_(b,k,X)=0`

for every active phase `b` and every `k<=q`. Hence `P_(k,X)==0` for all `k<=q`.

The converse is immediate. Exact cancellation of the first `q` interacting orders is therefore **equivalent** to the phase-fiber moment cancellation already exposed in `VIS-344`; mixing different powers of `xi^-1` does not create an additional exact nullspace.

## 4. One extra local order forces a small confluent exponential polynomial

Assume on `J_X subset [X,2X]` that

`|M_X(xi)| <= C_0 X^(-(q+1))`.

For `xi in J_X`,

`|E_(q,X)(xi)|`
` <= xi^q |M_X(xi)| + |R~_(q,X)(xi)|`
` <= (2X)^q C_0 X^(-(q+1)) + C_q T_(q+1,X)/X`
` = [2^q C_0 + C_q T_(q+1,X)]/X`.

So approximate interaction among nonzero orders has been reduced to a precise local-smallness problem in the confluent exponential-polynomial space. This is the correct place to charge phase count, phase spacing, polynomial multiplicity, window length and coefficient conditioning.

In the special case where all `P_k` below the first surviving order vanish, the polynomial coefficient at that order becomes constant after the normalization used in `VIS-348`, and the problem collapses to the ordinary exponential-polynomial Turán--Nazarov gate already derived there. The present result is the exact finite-order envelope that contains that special case.

## Prior-art audit

The general functional class is classical. A. J. van der Poorten, **Generalisations of Turán's main theorems on lower bounds for sums of powers**, *Bulletin of the Australian Mathematical Society* 2:1 (1970), 15--37, DOI `10.1017/S0004972700041575`, explicitly generalizes Turán's lower-bound theorems to exponential sums with polynomial coefficients using determinant estimates. This is direct prior art for treating sums `sum_b Q_b(x) exp(lambda_b x)` as a classical Turán-type concentration class rather than a new mathematical object.

The elementary constant-coefficient ODE representation and linear independence of the functions `x^r exp(lambda x)` are likewise classical. No novelty is claimed for confluent exponential polynomials, generalized eigenfunctions, Hermite/Vandermonde structure, or Turán-type lower-bound theory with polynomial coefficients.

The Mathia-specific content is the exact reduction for Wang's rational multiplier: **without assuming lower moment cancellation**, all interaction among the first `q` inverse-frequency tail orders becomes one explicit confluent exponential polynomial, and any claimed extra local Wang order forces that object down to `O(X^-1)` with the remainder conditioning shown above.

This finding deliberately does not import a quantitative inequality from van der Poorten as though it were already uniform in Mathia's scale-dependent phase collisions, polynomial coefficient norms and moving windows. Establishing the sharp bound in that variable-parameter regime is the remaining analytic question.

## Dependencies

- `VIS-333`: exact Wang multiplier and one-order log-frequency smoothing.
- `VIS-343`: nonzero Wang tail coefficients and pure-dilate moment cancellation.
- `VIS-344`: translation-fiber moment polynomials and exact uniform cancellation hierarchy.
- `VIS-346`: fixed-bank Turán--Nazarov short-window obstruction.
- `VIS-347`: variable first-moment phase-entropy budget.
- `VIS-348`: global fixed-order remainder control and higher-moment phase-entropy gate after exact lower cancellations.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed here.

## Research consequence

The phrase "interaction among several nonzero asymptotic orders" is no longer an independent algebraic escape for a finite translated-dilate bank with frequency-independent coefficients. At every fixed truncation depth, the interaction is exactly a classical confluent exponential polynomial. Exact cancellation reduces to the already-known fiberwise moment equations, while approximate cancellation must pay through concentration and conditioning of this finite-dimensional system.

The accepted Wang clue remains open because the **quantitative** confluent concentration problem is not yet closed in the scale-dependent regime. A viable finite-bank escape must now exhibit controlled phases and polynomial coefficients and prove that the required local smallness is achievable without dimension growth, phase coalescence, shrinking-window collapse or coefficient degeneration that merely pays for the gain. Genuinely frequency/source-dependent coefficients, infinite expansions and direct signed information in `G` remain separate live mechanisms.