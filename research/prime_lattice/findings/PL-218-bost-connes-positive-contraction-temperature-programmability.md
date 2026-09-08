# PL-218 — Finite-prime positive contractions uniformly program Bost–Connes temperature profiles below the phase transition

## Claim

The positivity/norm-budget escape left explicitly open by `PL-217` does **not** restore scalar-temperature rigidity near the Riemann half. In the canonical Bost–Connes high-temperature state, finitely many prime-divisibility coordinates already provide positive contractions whose scalar KMS profiles uniformly approximate arbitrary continuous `[0,1]`-valued functions on every compact interval strictly below the thermodynamic transition.

Precisely, let `phi_beta` be the unique Bost–Connes `KMS_beta` state for `0<beta<=1`. For every

\[
0<a<b<1,
\qquad
f\in C([a,b],[0,1]),
\qquad
\varepsilon>0,
\]

there exists a **finite-prime diagonal positive contraction** `X` in the Bost–Connes algebra such that

\[
0\le X\le1,
\qquad
\|X\|\le1,
\]

and

\[
\boxed{
\sup_{\beta\in[a,b]}
|\phi_\beta(X)-f(\beta)|<\varepsilon.
}
\]

The construction is explicit. For primes `p` in a dyadic block `(P,2P]`, let

\[
Y_p=1_{\{v_p\ge1\}}
\]

be the diagonal divisibility projection. Under the canonical product measure from `PL-215`, the `Y_p` are independent Bernoulli variables with

\[
\phi_\beta(Y_p)=p^{-\beta}.
\]

The block average of these projections estimates `beta` uniformly on `[a,b]`; composing that estimator with `f` and functional calculus on the finite commuting family `{Y_p}` gives the desired positive contraction.

Thus even the conjunction

\[
\text{finite prime support}
+\text{positivity}
+\|X\|\le1
+\text{arbitrary continuous scalar profile near }\beta=1/2
\]

is a **programmable control**, not an RH mechanism. A viable Bost–Connes route must still obtain its content from source-forced operator relations, a canonical infinite object, complex continuation, a trace/positivity identity tied to the completed zeta function, or another constraint not reproduced by the finite-prime statistical experiment below.

The restriction `b<1` is essential to the proof. The dyadic block contains enough occupied prime coordinates uniformly only strictly below the Bost–Connes transition. No density statement at the endpoint `beta=1` is claimed.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/CONTROL + PRIOR-ART-AUDITED + NO-NOVELTY-CLAIM`.

## 1. Prime-divisibility coordinates are independent Bernoulli observations of temperature

`PL-215` records the canonical adelic realization

\[
\mu_\beta=\bigotimes_p\mu_{\beta,p}
\]

and the exact valuation law

\[
\mu_{\beta,p}\{v_p=k\}
=(1-p^{-\beta})p^{-k\beta},
\qquad k\ge0.
\]

This is a real-temperature measure identity, not an analytic continuation of the Gibbs partition function. Summing over `k>=1` gives

\[
\boxed{
\mu_\beta\{v_p\ge1\}=p^{-\beta}.
}
\]

Because the adelic measure is a product over primes, the events `{v_p>=1}` are independent for distinct `p`.

In the diagonal algebra `C(\widehat{\mathbb Z})` these events are clopen cylinder sets, so their indicators `Y_p` are commuting projections. Equivalently, they are finite-coordinate elements of the standard Bost–Connes diagonal. Hence any bounded function of finitely many `Y_p` is a fixed finite-prime element of the algebra, independent of temperature.

The primary product-measure input is classical Bost–Connes/Neshveyev theory already audited in `PL-215`: Sergey Neshveyev, “Ergodicity of the action of the positive rationals on the group of finite adeles and the Bost-Connes phase transition theorem,” *Proceedings of the American Mathematical Society* **130**(10) (2002), 2999–3003, DOI `10.1090/S0002-9939-02-06449-3`, arXiv `math/0002141`. Neshveyev writes the canonical measure explicitly as `mu_beta=otimes_p mu_{beta,p}` with the local density proportional to `|a|_p^(beta-1)`, from which the valuation law above follows exactly.

## 2. A dyadic prime block estimates `beta` uniformly for every `b<1`

Let

\[
\mathcal P_P=\{p\text{ prime}:P<p\le2P\},
\qquad
N_P=|\mathcal P_P|,
\]

and define the commuting positive contraction

\[
A_P=\frac1{N_P}\sum_{p\in\mathcal P_P}Y_p.
\]

Its expectation is

\[
m_P(\beta)=\phi_\beta(A_P)
=\frac1{N_P}\sum_{p\in\mathcal P_P}p^{-\beta}.
\]

For `beta in [a,b]`, every prime in the block satisfies

\[
(2P)^{-\beta}\le p^{-\beta}\le P^{-\beta},
\]

so

\[
(2P)^{-\beta}\le m_P(\beta)\le P^{-\beta}.
\]

Put

\[
\beta_P^*(\beta)
=-\frac{\log m_P(\beta)}{\log P}.
\]

Then

\[
\boxed{
0\le\beta_P^*(\beta)-\beta
\le\frac{b\log2}{\log P}
}
\]

uniformly on `[a,b]`. Thus the mean itself determines `beta` up to `O(1/log P)` without needing any zeta zero, functional equation, or interaction between prime phases.

Independence gives

\[
\operatorname{Var}_\beta(A_P)
=\frac1{N_P^2}
\sum_{p\in\mathcal P_P}p^{-\beta}(1-p^{-\beta})
\le\frac{m_P(\beta)}{N_P}.
\]

Chebyshev therefore yields

\[
\mathbb P_\beta\!\left(
|A_P-m_P(\beta)|>\frac12m_P(\beta)
\right)
\le
\frac4{N_Pm_P(\beta)}.
\]

The prime number theorem gives

\[
N_P\sim\frac{P}{\log P}.
\]

Since `beta<=b<1`,

\[
N_Pm_P(\beta)
\ge N_P(2P)^{-b}
\asymp\frac{P^{1-b}}{\log P}
\longrightarrow\infty
\]

uniformly for `beta in [a,b]`. Hence the relative-error probability above tends to zero uniformly.

This is exactly where the strict inequality `b<1` enters. At `beta=1`, a single dyadic block has expected occupied-coordinate count only of order `1/log P`, so this estimator no longer concentrates. The present argument therefore isolates the thermodynamic endpoint rather than silently claiming a critical-half effect there.

## 3. A finite-prime positive contraction realizes any continuous `[0,1]` profile

Define the estimator

\[
\widehat\beta_P=
\Pi_{[a,b]}\!\left(
-\frac{\log A_P}{\log P}
\right)
\]

when `A_P>0`, where `Pi_[a,b]` denotes clipping to `[a,b]`; when `A_P=0`, set `widehat beta_P=b`.

On the event

\[
\frac12m_P(\beta)\le A_P\le\frac32m_P(\beta),
\]

we have

\[
\left|
\frac{\log A_P-\log m_P(\beta)}{\log P}
\right|
\le\frac{\log2}{\log P}.
\]

Clipping cannot increase the distance from the true `beta in [a,b]`. Combining this with the deterministic mean estimate gives

\[
\boxed{
|\widehat\beta_P-\beta|
\le
\frac{(b+1)\log2}{\log P}
}
\]

on the good event. Moreover

\[
\sup_{\beta\in[a,b]}
\mathbb P_\beta(\text{bad event})
\ll_{a,b}
\frac{\log P}{P^{1-b}}
\longrightarrow0.
\]

Therefore `widehat beta_P` is a uniformly consistent estimator of inverse temperature from finitely many prime-divisibility coordinates.

Now let `f in C([a,b],[0,1])`. Since `A_P` has finite spectrum

\[
\left\{0,\frac1{N_P},\ldots,1\right\},
\]

`f(widehat beta_P)` is an ordinary finite functional calculus of `A_P`. More explicitly, if `Q_{P,k}` is the spectral projection onto the event that exactly `k` primes in `mathcal P_P` divide the adelic coordinate, then

\[
X_P
=
\sum_{k=0}^{N_P}
 f\!\left(
 \Pi_{[a,b]}\!\left(-\frac{\log(k/N_P)}{\log P}\right)
 \right)
 Q_{P,k},
\]

with the `k=0` coefficient defined as `f(b)`.

The projections `Q_{P,k}` are finite sums of products of `Y_p` and `1-Y_p`; they are pairwise orthogonal and sum to `1`. Every coefficient lies in `[0,1]`. Consequently

\[
\boxed{0\le X_P\le1,\qquad\|X_P\|\le1.}
\]

This is an exact operator inequality, not an estimate whose constant deteriorates with approximation accuracy.

Let `omega_f` be the modulus of continuity of `f`. For every fixed `eta>0`, once `P` is large enough that `(b+1)log 2/log P<eta`,

\[
\begin{aligned}
|\phi_\beta(X_P)-f(\beta)|
&=\left|\mathbb E_\beta f(\widehat\beta_P)-f(\beta)\right|\\
&\le
\omega_f(\eta)
+\mathbb P_\beta(|\widehat\beta_P-\beta|>\eta).
\end{aligned}
\]

Taking the supremum over `beta in [a,b]`, then first choosing `eta` and afterwards `P`, proves

\[
\boxed{
\sup_{\beta\in[a,b]}
|\phi_\beta(X_P)-f(\beta)|\longrightarrow0.
}
\]

Thus the approximants simultaneously obey finite prime support, positivity, and a uniform norm-one budget.

## 4. Adversarial controls and exact boundary of the claim

This construction survives the main obvious attacks.

**The observable is not temperature-dependent after construction.** For each target profile `f` and scale `P`, `X_P` is one fixed element of the finite-prime diagonal algebra. The same `X_P` is evaluated against every `phi_beta` in the interval.

**Positivity is genuine.** The proof does not approximate a positive scalar function by a polynomial with uncontrolled sign. It first estimates `beta` with commuting projections and then assigns a coefficient in `[0,1]` to each joint eigenspace. Positivity and `||X_P||<=1` are exact.

**The result is not produced by analytic continuation.** All identities are expectations under real `KMS_beta` states. The argument never evaluates `zeta(beta)` for `beta<=1` and never continues an Euler product across its absolute-convergence boundary.

**The half is not selected by the construction.** The theorem works uniformly on every compact `[a,b]` inside `(0,1)`, whether or not the interval contains `1/2`. Its information source is statistical identifiability of the exponent-coordinate product measure, not a feature specific to Riemann zeros.

**The endpoint `beta=1` is not covered.** The proof needs `P^{1-b}/log P -> infinity`. This prevents turning the statement into an artificial claim that the whole closed high-temperature interval has the same finite-block concentration property.

**The construction uses a growing set of primes.** Unlike `PL-217`, it is not a one-prime theorem. This is the price of preserving positivity and norm while programming an arbitrary profile. The number of prime coordinates grows with the required accuracy.

**Source-forcing is still outside the control.** `X_P` is chosen from the desired function `f`; it is not a canonical arithmetic observable. A fixed observable selected independently by a zeta/adelic/Weil rule can still carry genuine information if the selection rule imposes a relation that these controls cannot match.

**Complex-temperature structure is not controlled.** Each finite-prime expectation has an elementary finite exponential dependence on real `beta`, but no normal-family estimate, functional equation, or controlled complex continuation of the sequence `X_P` is asserted. The theorem cannot by itself manufacture the zeta zero divisor.

## 5. Prior-art and novelty audit

The product-measure input is classical. Neshveyev's 2002 paper gives the canonical factorization `mu_beta=otimes_p mu_{beta,p}` and the local `p`-adic density used in `PL-215`; Bost--Connes theory supplies the underlying diagonal KMS system. The concentration step uses only independence, Chebyshev's inequality, and the prime number theorem. The positive contraction is finite functional calculus in a finite commuting projection algebra.

A targeted literature audit around Bost--Connes KMS observables, finite-prime/cylinder observables, inverse-temperature estimation, positive contractions, and approximation of temperature profiles did not expose a dedicated theorem with this exact line-specific conclusion. That absence is not treated as evidence of novelty. The statement is an elementary synthesis of classical ingredients, and **no novelty claim is made**.

The closest durable precursor inside this line is `PL-215`: its Kakutani calculation shows that distinct high-temperature canonical product measures are mutually singular. Pairwise singularity alone does not provide the present finite-block, uniform-in-`beta`, positive-contraction approximation theorem. `PL-217` then proves arbitrary scalar-profile approximation using one prime but explicitly leaves positivity and a fixed norm budget open. `PL-218` closes exactly that caveat on compact intervals below `beta=1` by exploiting many independent prime coordinates.

The matched-control interpretation is deliberately generic. Any product system with sufficiently many independent coordinates whose activation probabilities behave like `e^{-beta lambda_j}` over a growing energy block would admit the same statistical-temperature reconstruction. Therefore the theorem does **not** distinguish rational primes from a generic multiplicative thermodynamic system; that failure is precisely why such scalar profiles cannot satisfy the line's rational-prime specificity requirement.

## Consequence for the research line

The surviving Bost--Connes route is narrower than after `PL-217`. It is no longer enough to demand that a proposed critical-half observable be positive or have a uniform norm bound: those properties can coexist with essentially arbitrary scalar KMS behavior on any compact neighborhood of `beta=1/2` contained in `(0,1)`.

A potentially meaningful mechanism must instead impose structure that cannot be chosen after specifying the desired temperature graph. Examples remain a source-forced relation among prime channels, a canonical infinite observable with controlled complex continuation, an operator-valued identity, or a positivity/trace formula whose arithmetic input is fixed independently of the target output. The mere existence of a bounded positive observable whose expectation has a special feature at `beta=1/2` is now a matched-control failure.