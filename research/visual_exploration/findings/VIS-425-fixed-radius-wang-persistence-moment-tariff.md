# VIS-425 — fixed-radius Wang persistence reduces to finite-offset moment tariffs

## Claim

Let

`F_N(z)=sum_(a in S_N) b_(N,a) z^a`

be a nonzero finite Laurent polynomial on a finite prime torus, with real-time character frequencies

`lambda_a=sum_p a_p log p`.

Write

`S_N=||F_N||_infinity`,

`W_N=(sum_a |b_(N,a)|)/S_N`,

and suppose the frequency radius is uniformly bounded,

`Omega_N=max_a |lambda_a| <= Omega_* < infinity`.

For an offset `u`, put

`X_(N,u)(z)=|F_N(z tau(u))|^2/S_N^2`,

where `tau(u)=(p^(-iu))_p`. For each fixed integer `R>=1`, define the structural mixed divisor

`delta^*_(N,R)`

as the smallest nonzero absolute value of a frequency

`sum_(j=1)^R (lambda_(a_j)-lambda_(c_j))`,

with `a_j,c_j in S_N`, and set `delta^*_(N,R)=+infinity` if no nonzero value occurs.

If for every fixed `R>=1`

`W_N^(2R) [ 1/N + R Omega_*/log N + (log N)/(N delta^*_(N,R)) ] -> 0`,

then every fixed-radius persistence observable has the same dyadic Gram-block asymptotic as its exact prime-torus Haar self-null. More precisely, for every fixed `rho>0`, define

`Q_(N,rho)(z)=sup_(|u|<=rho) |F_N(z tau(u))|/S_N in [0,1]`.

Then for every fixed continuous `phi:[0,1]->C`,

`(1/N) sum_(N<k<=2N) phi(Q_(N,rho)(z(g_k)))`
` - int phi(Q_(N,rho)(z)) dm_H(z) -> 0`.

For a fixed threshold `t in (0,1)`, the same hypotheses imply convergence of the Gram low-persistence frequency to the Haar self-null probability whenever

`lim_(eta->0+) limsup_(N->infinity) m_H{|Q_(N,rho)-t|<=eta}=0`.

For the strict near-band Wang dyadic shells of `VIS-313`, the uniform-bandwidth hypothesis is automatic because every shell frequency satisfies

`|lambda|<log 2`.

If the shell has dyadic arithmetic height `Y_N`, so every participating prime power is at most `2Y_N`, then the structural divisor has the elementary lower bound

`delta^*_(N,R) >= (2Y_N)^(-2R)`.

Thus a completely explicit sufficient persistence tariff is

`W_N^(2R) [ 1/N + R/log N + (log N)(2Y_N)^(2R)/N ] -> 0`

for every fixed `R`, up to constants depending only on the fixed outer bandwidth.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION-CERTIFIED + QUANTITATIVE CONTROL + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

This is a sufficient reduction, not a proof that the actual growing Wang family satisfies the tariffs. It gives no RH consequence and does not turn failure of a sufficient bound into evidence of a Gram-point anomaly.

## 1. Finite collections of offsets obey the same character tariff

For fixed offsets `u_1,...,u_J`, each shifted squared amplitude has the Laurent expansion

`X_(N,u_j)(z)`

with the same character-frequency support as `X_(N,0)`; the offset changes only coefficient phases. The Wiener-algebra norm therefore satisfies

`||X_(N,u_j)||_A <= W_N^2`.

Consider a mixed monomial

`P_N(z)=product_(j=1)^J X_(N,u_j)(z)^(r_j)`

of total degree

`R=sum_j r_j`.

Submultiplicativity gives

`||P_N||_A <= W_N^(2R)`.

Every character frequency in `P_N` is a sum of `R` differences `lambda_a-lambda_c`, so its magnitude is at most `2R Omega_*`, while every nonzero frequency is at least `delta^*_(N,R)` in absolute value. Hence the three `VIS-423` tariffs satisfy

`A_0(P_N) <= W_N^(2R)`,

`A_1(P_N) <= 2R Omega_* W_N^(2R)`,

`A_(-1)(P_N) <= W_N^(2R)/delta^*_(N,R)`.

Applying `VIS-423` shows that the Gram-block average of every fixed mixed monomial converges to its Haar average under the displayed hypotheses.

Ordinary multivariate polynomial approximation on the fixed cube `[0,1]^J` then gives the same conclusion for every fixed continuous function of the finite vector

`(X_(N,u_1),...,X_(N,u_J))`.

The important strengthening over `VIS-424` is that the offsets do not create a new family of frequencies. They only rephase the existing Laurent coefficients. The structural divisor `delta^*` is chosen before coefficient cancellation precisely so that it remains valid simultaneously for all fixed offset choices.

## 2. Uniform bandwidth turns a fixed path window into a fixed finite mesh

For a torus point `z`, the function

`u -> F_N(z tau(u))`

is a finite exponential polynomial of type at most `Omega_*`. Its real-axis absolute value is at most `S_N`, because the whole orbit remains inside the same prime torus. The classical Bernstein inequality therefore gives, uniformly in `z` and `N`,

`|d/du F_N(z tau(u))| <= Omega_* S_N`.

Thus the normalized amplitude

`A_N(z,u)=|F_N(z tau(u))|/S_N`

is `Omega_*`-Lipschitz in `u`, and its square `X_(N,u)=A_N(z,u)^2` is `2 Omega_*`-Lipschitz.

Fix `epsilon>0`. Choose a deterministic mesh `u_1,...,u_J` of `[-rho,rho]` with mesh radius at most

`epsilon/(2 Omega_*)`

when `Omega_*>0`. The number `J` depends only on `rho`, `Omega_*`, and `epsilon`, not on `N`. Then uniformly in `z`,

`| sup_(|u|<=rho) X_(N,u)(z) - max_(1<=j<=J) X_(N,u_j)(z) | <= epsilon`.

The degenerate case `Omega_*=0` is constant in `u` and needs no mesh.

Therefore a fixed-radius path supremum does not require a growing time discretization in the strict near-band Wang regime. Bandwidth converts it into a fixed-dimensional continuous observable to arbitrary fixed accuracy.

## 3. Finite-offset convergence plus mesh refinement closes continuous persistence tests

Let

`R_(N,rho)(z)=Q_(N,rho)(z)^2=sup_(|u|<=rho) X_(N,u)(z)`.

For the fixed mesh above put

`R_(N,rho,epsilon)(z)=max_j X_(N,u_j)(z)`.

The map

`(x_1,...,x_J) -> phi(sqrt(max_j x_j))`

is continuous on `[0,1]^J`. By the finite-offset result, its Gram-block average differs from its Haar average by `o(1)` for every fixed mesh.

Because `phi` is uniformly continuous and `R_(N,rho,epsilon)` differs uniformly from `R_(N,rho)` by at most `epsilon`, both the Gram and Haar replacement errors vanish with `epsilon`. Taking `N->infinity` first for a fixed mesh and then `epsilon->0` proves the claimed continuous-test convergence for `Q_(N,rho)`.

A threshold indicator is handled by the same continuous-sandwich argument as in `VIS-424`. Uniform Haar boundary mass near the threshold is the remaining condition needed to pass from continuous tests to a fixed low-persistence tail probability.

## 4. Wang ratio characters give an explicit structural small-divisor floor

For a strict near-band dyadic shell of arithmetic height `Y_N`, every mode is

`lambda=log(q/r)`

with prime powers `q,r<=2Y_N` and distinct base primes. A structural mixed frequency of order `R` has the form

`nu=sum_(j=1)^R [log(q_j/r_j)-log(q'_j/r'_j)] = log(A/B)`,

where `A` and `B` are positive integers, each a product of `2R` factors bounded by `2Y_N`. Hence

`A,B <= (2Y_N)^(2R)`.

If `nu!=0`, then `A!=B`. If `A>B`,

`log(A/B)=integral_B^A dt/t >= (A-B)/A >= 1/A`,

and the same argument with `A,B` exchanged handles `B>A`. Therefore

`|nu| >= (2Y_N)^(-2R)`.

This bound is deliberately elementary and can be very far from sharp. Its role is to remove any ambiguity about whether the path discretization creates a qualitatively new small-divisor object: it does not. The persistence branch pays the same finite-order product-ratio arithmetic already exposed by the scalar moment analysis.

Substitution into the general tariff gives the explicit Wang sufficient condition stated in the claim. Whether the actual source family satisfies it is now concentrated in the growth of the normalized Wiener mass `W_N`, the shell-height transport `Y_N`, and Haar anti-concentration.

## 5. Prior art and novelty audit

The external ingredients are classical. Bernstein's derivative inequality for entire functions of exponential type bounded on the real axis is the same input already used in `VIS-416`; a standard reference is Clément Frappier, **Inequalities for Entire Functions of Exponential Type**, *Canadian Mathematical Bulletin* 27:4 (1984), 463--471, DOI `10.4153/CMB-1984-073-4`. Polynomial density in continuous functions on a fixed compact cube is the classical Stone--Weierstrass theorem.

The Gram-point character estimate is not imported anew here: it is exactly `VIS-423`. The scalar Wiener/moment reduction is `VIS-424`. A targeted prior-art orientation did not reveal a reason to interpret the finite-mesh argument as a new general theorem, and no such novelty is claimed. The durable Mathia content is the specialization showing that the remaining fixed-radius Wang persistence escape is governed by the same explicit growing-shell character resources rather than by an independent path-valued obstruction.

## 6. Representation audit, boundaries, and falsification

The representation is stable under torus-coordinate relabelling and time translation. The offset action `tau(u)` changes coefficient phases but not the character-frequency set, the Wiener norm bound, or the structural divisor definition. The path observable is recovered from the finite meshes by a representation-independent Lipschitz bound coming from the actual frequency radius.

The uniform-bandwidth assumption is essential. If `Omega_N` grows, a mesh fine enough to control the path supremum may require `J=J_N->infinity`, and the fixed-dimensional polynomial-approximation argument no longer applies without a separate quantitative approximation theorem.

The radius `rho` is fixed. A growing persistence radius likewise produces a growing mesh and is not covered. The theorem also does not establish the uniform Haar boundary-mass condition for a tail threshold.

The structural divisor `delta^*_(N,R)` may be smaller than the surviving-frequency divisor of the unshifted scalar moment in `VIS-424`; this is intentional. Offset phases can undo cancellations that happen at one time origin, so a path-uniform statement must use the pre-cancellation difference set.

Falsify the derivation by exhibiting a mixed offset monomial with Wiener norm above `W_N^(2R)`, a frequency outside the `2R Omega_*` envelope, a nonzero mixed Wang frequency below `(2Y_N)^(-2R)`, a fixed-bandwidth shell whose normalized amplitude is not uniformly Lipschitz in the offset, or a fixed continuous persistence test for which the finite-mesh/finite-offset limit fails under the stated tariffs.

## Dependencies

- `VIS-313`: strict near-band Wang shells have ratio frequencies `log(q/r)` and dyadic arithmetic-height control.
- `VIS-416`: Bernstein normalization supplies the coefficient-free uniform offset Lipschitz bound.
- `VIS-419`: each fixed Wang shell is a Laurent polynomial on the base-prime torus and Haar is its exact translation self-null.
- `VIS-423`: dyadic Gram blocks obey the character small-divisor tariff.
- `VIS-424`: normalized pointwise amplitude reduces to fixed scalar moment tariffs.

## Research consequence

For ordinary Gram points and the canonical strict near-band Wang shells, **fixed-radius persistence is no longer an independent nonlinear escape once the strengthened mixed-moment tariffs pass**. The uniform bound `Omega_N<log 2` makes the path window finitely discretizable at every fixed accuracy, and the ratio representation gives an explicit finite-order small-divisor floor.

The accepted phase-anchored small-value clue should therefore treat pointwise amplitude and fixed-radius persistence together. The remaining live resources are a quantified failure of the normalized Wiener/mixed-divisor tariffs, nonuniform Haar concentration at the chosen threshold, a persistence radius or bandwidth that genuinely grows with the source scale, or a different selector whose phase law is not already driven to the same self-null.