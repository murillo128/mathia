# VIS-164 — anchored held-out-prime collision scores have a dimension-coded Haar tail

## Claim

Let

`P={p_0,p_1,...,p_d}`

be a finite retained set of distinct rational primes with `d>=1`, let `r` be a prime not in `P`, and define

`Phi_P(t)=(p^(-it))_(p in P)`,

`A_r(t)=r^(-it)`.

Use `p_0` as an anchor and put

`alpha_j = log p_j / log p_0` for `1<=j<=d`,

`beta = log r / log p_0`.

At the exact `p_0`-return lags

`Delta_q = 2 pi q / log p_0`, `q=1,2,...`,

define the held-out-prime collision score

`C_q = |A_r(t+Delta_q)-A_r(t)| / ||Phi_P(t+Delta_q)-Phi_P(t)||_2`.

The score is independent of `t` and has the exact form

`C_q = |sin(pi q beta)| / sqrt(sum_(j=1)^d sin^2(pi q alpha_j))`.

Then:

1. the sequence

   `(q alpha_1,...,q alpha_d,q beta) mod 1`

   is Haar-equidistributed in `T^(d+1)`;
2. for every fixed threshold `L>0`,

   `lim_(Q->infinity) Q^(-1) #{1<=q<=Q : C_q>L} = mu_d(L)`,

   where

   `mu_d(L) = int_[0,1] int_[0,1]^d 1{|sin(pi y)| > L sqrt(sum_j sin^2(pi x_j))} dx dy`;
3. as `L->infinity`,

   `mu_d(L) ~ c_d L^(-d)`,

   with

   `c_d = Gamma((d+1)/2) / ( pi^((d+1)/2) Gamma(d/2+1)^2 )`.

In particular, the exact-return held-out-prime control has a **support-dimension-coded heavy tail**: the exceedance exponent is precisely

`d = |P|-1`.

Examples are

`c_1=4/pi^2`, `c_2=1/(2 pi)`, `c_3=16/(9 pi^3)`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-KRONECKER-WEYL-PUSHFORWARD + MATCHED-NULL + NO-NOVELTY-CLAIM`.

This is a fixed-support, fixed-threshold limiting law. It is not a finite-`Q` discrepancy estimate, an extreme-value law for `max_(q<=Q) C_q`, a joint limit with `L=L(Q)`, a theorem uniform in growing support, or a zeta/RH result.

## 1. Exact anchoring reduces the collision quotient to a discrete torus observable

For `Delta_q=2 pi q/log p_0`,

`p_0^(-i Delta_q)=1`.

For each other retained prime,

`|p_j^(-i Delta_q)-1| = 2 |sin(pi q alpha_j)|`,

while for the omitted prime

`|r^(-i Delta_q)-1| = 2 |sin(pi q beta)|`.

The common factor `2` cancels in the collision quotient, giving

`C_q = |sin(pi q beta)| / sqrt(sum_(j=1)^d sin^2(pi q alpha_j))`.

Thus one retained phase is forced to return exactly, and the remaining collision geometry is a discrete rotation on a `(d+1)`-torus.

The same lag is a legitimate witness for the finite-window Lipschitz constant from `VIS-162` and `VIS-163`. If

`T_q = pi q/log p_0`,

then the pair `t=T_q`, `u=-T_q` lies in `[-T_q,T_q]` and has difference `Delta_q`, so

`Lambda_P(A_r;[-T_q,T_q]) >= C_q`.

The anchored scores therefore form a structured lower-bound witness family for the full finite-window collision complexity.

## 2. Prime-logarithm independence gives discrete Haar equidistribution

Suppose integers `m_0,m_1,...,m_d,m_r` satisfy

`m_0 + sum_(j=1)^d m_j alpha_j + m_r beta = 0`.

Multiplying by `log p_0` gives

`m_0 log p_0 + sum_(j=1)^d m_j log p_j + m_r log r = 0`.

Exponentiating and moving negative powers across the equality yields an equality between two rational-prime factorizations. Unique factorization forces every coefficient to vanish.

Hence

`1, alpha_1,...,alpha_d,beta`

are rationally independent. By the discrete Kronecker--Weyl theorem,

`q (alpha_1,...,alpha_d,beta) mod 1`

is Haar-equidistributed in `T^(d+1)`.

For fixed `L>0`, the boundary of

`E_L = {(x,y): |sin(pi y)| > L sqrt(sum_j sin^2(pi x_j))}`

has Haar measure zero. Therefore the indicator of `E_L` is Riemann integrable, and equidistribution gives the asserted frequency limit `mu_d(L)`.

This step is exactly the fixed-threshold regime. It supplies no convergence rate in `Q` and no uniformity when the threshold grows with `Q`.

## 3. The large-threshold tail is a torus small-ball calculation

Write

`V_d(rho) = meas{x in T^d : sqrt(sum_j sin^2(pi x_j)) < rho}`.

As `rho->0`, only a shrinking neighborhood of the torus origin contributes. In signed local coordinates `u_j` around that origin,

`sin(pi u_j) = pi u_j + O(u_j^3)`.

Therefore the sublevel set is asymptotic to a Euclidean `d`-ball of radius `rho/pi`, and

`V_d(rho) ~ v_d pi^(-d) rho^d`,

where

`v_d = pi^(d/2) / Gamma(d/2+1)`

is the volume of the unit ball in `R^d`.

Conditioning on the held-out coordinate `y` gives

`mu_d(L) = int_0^1 V_d(|sin(pi y)|/L) dy`.

Because `|sin(pi y)|/L <= 1/L`, the small-ball asymptotic is uniform over the argument entering this integral as `L->infinity`. Thus

`mu_d(L)`
` ~ v_d pi^(-d) L^(-d) int_0^1 |sin(pi y)|^d dy`.

The standard beta integral gives

`int_0^1 sin^d(pi y) dy`
` = Gamma((d+1)/2) / (sqrt(pi) Gamma(d/2+1))`.

Combining the constants yields

`c_d = Gamma((d+1)/2) / ( pi^((d+1)/2) Gamma(d/2+1)^2 )`.

The exponent comes only from the codimension of an anchored near-return: after pinning `p_0` exactly, all `d` remaining retained phases must simultaneously enter a small neighborhood, while the held-out phase is free to remain macroscopically separated.

## 4. This sharpens the held-out-prime control without creating an extreme-value theorem

`VIS-163` proved that the global omitted-prime collision quotient is infinite and that finite-window constants diverge. The present result identifies a canonical discrete family on which the obstruction is visible and gives the **limiting exceedance law at every fixed threshold**.

For each fixed `L`, a positive Haar proportion `mu_d(L)` of anchored indices eventually exceed `L`. Since `mu_d(L)>0` for every finite `L`, this alone reproves qualitative divergence along anchored returns.

But the order of limits matters. The theorem first sends `Q->infinity` with `L` fixed, then analyzes the Haar quantity `mu_d(L)` as `L->infinity`. It does **not** justify substituting `L=L(Q)`, and therefore does not imply that the maximum among the first `Q` anchored scores scales like `Q^(1/d)` or follows any Poisson/extreme-value law.

Such claims require quantitative shrinking-target or discrepancy information for this specific Kronecker sequence, which is deliberately outside the present result.

## 5. Consequence for source-sensitive decoder comparisons

A fixed-support zeta-facing decoder experiment now has a stronger matched null than mere divergence of `Lambda_P`.

If the candidate statistic is evaluated on a predeclared anchored recurrence family, an omitted-prime control already has a fully specified fixed-threshold asymptotic distribution. In particular, the baseline tail exponent changes automatically with retained support:

`tail exponent = |P|-1`.

Therefore an apparent reduction of large collisions after adding retained primes is not by itself source evidence; the held-out-prime null becomes geometrically thinner in exactly this dimension-coded way.

A source-sensitive positive claim should instead freeze the retained support, anchor, candidate observable and normalization, base-height/window rule, thresholds, and held-out-prime matching rule, then demonstrate a separation from the corresponding anchored control law. If support grows with height, the dimension effect must be accounted for before interpreting the change as improved zeta-specific recoverability.

This gives the accepted prime-phase recursive-geometry clue a quantitative control surface that was absent from `VIS-163`: compare distributions or normalized collision geometry, not only whether the optimal Lipschitz constant diverges.

## 6. Prior art and novelty boundary

The dynamical input is classical Kronecker--Weyl theory. `VIS-071` already records the standard character proof for rationally independent prime-logarithm flows and anchors it to Håkan Hedenmalm, Peter Lindqvist, and Kristian Seip, **A Hilbert space of Dirichlet series and systems of dilated functions in L^2(0,1)**, *Duke Mathematical Journal* 86:1 (1997), 1--37, DOI `10.1215/S0012-7094-97-08601-4`, together with the classical Kronecker-theorem literature.

Quantitative discrepancy and shrinking-target behavior of Kronecker sequences are established subjects in Diophantine approximation. The present theorem intentionally avoids importing a finite-`Q` rate: its empirical statement is only ordinary fixed-set equidistribution, and the `L^(-d)` asymptotic is an elementary local Haar-volume calculation for the specific collision observable.

No novelty is claimed for Kronecker equidistribution, torus small-ball asymptotics, beta-integral constants, or general quantitative recurrence theory. The Mathia-specific content is the matched-control organization: anchoring one retained prime turns ordinary omitted-source instability into an explicit dimension-coded collision-tail baseline for later zeta-facing decoder tests.

## 7. Boundaries and falsification

The result assumes a fixed finite retained set and an omitted rational prime. The anchor `p_0` must belong to the retained support, and the other prime logarithm ratios together with the omitted ratio are rationally independent with `1`; unique factorization supplies this for distinct rational primes.

The score uses exact phases and the chordal Euclidean torus metric inherited from `VIS-162`. A different metric or a different anchoring rule can change the local small-ball constant and may change the effective exponent if its near-zero geometry is not Euclidean of dimension `d`.

The law is a Cesaro frequency statement over integer anchor index `q`. It says nothing by itself about short blocks, finite numerical resolution, the speed of convergence, or the first occurrence of a collision larger than a prescribed threshold.

Falsify the fixed-threshold law by finding `L>0` for which the empirical exceedance frequency has a limit different from the displayed Haar measure. Falsify the tail constant by showing that the Haar sublevel volume of `sqrt(sum_j sin^2(pi x_j))` has a different leading small-radius term. Either would contradict the equidistribution or local-volume calculation above.

## Research consequence

The omitted-prime baseline is no longer only qualitative. On exact returns of one retained prime, its collision scores have a canonical fixed-threshold Haar law with a support-dimension tail `c_d L^(-d)`.

The next useful positive step is therefore not another proof that a zeta-facing observable has large collisions. It is a **predeclared relative test**: does the candidate's anchored collision distribution, after the same normalization and support choice, differ from the held-out-prime law in a way that survives finite-window validation and the changing dimension of any growing-support regime?