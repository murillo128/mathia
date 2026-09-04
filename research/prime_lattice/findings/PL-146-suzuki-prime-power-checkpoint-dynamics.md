# PL-146 — Suzuki positivity reduces to convex prime-power checkpoints and an exact unit-drift event dynamics

## Claim

Suzuki's pointwise RH criterion admits a sharper arithmetic reduction than the continuous screw-function picture suggests. Write, for `t>0`,

`Psi(t) = R(t) - sum_(n<=exp(t)) Lambda(n)/sqrt(n) * (t-log n)`,

where `R(t)` is the explicit smooth pole/archimedean part of Suzuki's formula. Since `Lambda(n)` is supported on prime powers, the only arithmetic events are

`lambda_q = log q`,  `q=p^k`,

with jump weight

`w_q = Lambda(q)/sqrt(q) = log(p)/p^(k/2)`.

Between two consecutive prime-power energies, the arithmetic state is constant and `Psi` is **strictly convex**. More precisely, differentiating Suzuki's smooth term gives

`R''(t) = e^(t/2)+e^(-t/2) - 1/(4 cosh(t/2)) - 1/(4 sinh(t/2))`

and, with `x=e^t`,

`R''(t) = (x^3-x-1)/(sqrt(x)(x^2-1))`.

The numerator changes sign at the plastic constant `rho=1.324717...`, the positive root of `x^3-x-1=0`. Since `rho<2`, every arithmetic interval beginning at the first event `log 2` lies in the region `R''(t)>0`.

Consequently Suzuki's continuum condition

`RH <=> Psi(t)>=0 for all real t`

reduces exactly, after the already-unconditionally-positive initial interval, to **one constrained minimum per interval between consecutive prime powers**. If the active prime powers through an event have cumulative states

`P_j = sum_(q<=q_j) w_q`,

`Q_j = sum_(q<=q_j) w_q log q`,

then on `I_j=[log q_j, log q_(j+1)]`,

`Psi(t)=R(t)-P_j t+Q_j`,

and the unique constrained checkpoint is

`t_j^* = argmin_(t in I_j) [R(t)-P_j t]`.

Its margin is

`m_j = Q_j - sup_(t in I_j) [P_j t-R(t)]`.

Thus the entire prime contribution relevant to this scalar RH criterion is compressed to a two-state event stream

`(P,Q) -> (P+w_q, Q+w_q log q)`

on the prime-power axis rays `k e_p`. Mixed exponent vectors never enter this channel.

There is also an exact dynamical normal form. On `t>=log 2` set the strictly increasing archimedean clock

`tau=R'(t)`

and the workload

`Y(t)=-Psi'(t)`.

Between arithmetic events,

`Y=P_j-tau`,

so

`dY/dtau=-1`.

At `q=p^k`, `P` jumps by `w_q`, hence

`Y^+ = Y^- + w_q`.

The completed zeta scalar criterion is therefore an exact piecewise-deterministic **unit-drift jump system** driven by the ordered prime-power energies. Local minima of `Psi` are the recovery points where the positive workload drains to zero. This is a genuine dynamical interpretation of the prime-power exponent rays, but it does not solve the tail sign problem: it reorganizes it into nonnegativity of the checkpoint margins.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + STRUCTURAL-REDUCTION`. Suzuki's formula and `RH <=> Psi>=0` are peer-reviewed literature. The curvature factorization, checkpoint reduction, restricted Legendre form, and unit-drift clock follow by exact differentiation and elementary convexity. A very recent self-published Zenodo preprint series by Rainer Andreas Mittermeier independently develops essentially this same checkpoint/service-clock organization, so none of that organization is claimed as Mathia novelty. The preprints' large finite computer certificates and stronger tail claims are not needed for the exact result stored here and are not promoted to theorem status here without independent audit.

## Exact convexity calculation

Suzuki's equation (1.1) can be separated as

`Psi(t)=R(t)-A(t)`,

where

`A(t)=sum_(n<=exp(t)) Lambda(n)/sqrt(n) * (t-log n)`.

On an open interval containing no prime-power energy, the active set is fixed. Put

`P=sum Lambda(n)/sqrt(n)`,

`Q=sum Lambda(n) log(n)/sqrt(n)`

over that fixed active set. Then

`A(t)=Pt-Q`,

and therefore

`Psi'(t)=R'(t)-P`,

`Psi''(t)=R''(t)`.

Suzuki explicitly differentiates the prime-free formula and obtains

`R'(t)=2(e^(t/2)-e^(-t/2))+c-arctan(e^(t/2))+arctanh(e^(-t/2))`,

where the constant `c` is irrelevant to curvature. Differentiating once more gives

`R''(t)=e^(t/2)+e^(-t/2)-1/(4 cosh(t/2))-1/(4 sinh(t/2))`.

Let `y=e^(t/2)>1`. Direct algebra yields

`R''(t)=(y^6-y^2-1)/(y(y-1)(y+1)(y^2+1))`.

With `x=y^2=e^t`, this becomes

`R''(t)=(x^3-x-1)/(sqrt(x)(x^2-1))`.

The denominator is positive for `t>0`. The cubic `x^3-x-1` is strictly increasing after `x=1/sqrt(3)` and has a unique positive root `rho≈1.324717957`. Hence

`t>log rho  => R''(t)>0`.

Because `log rho < log 2`, every interval between prime powers lies wholly in the strictly convex regime. The non-smoothness at an event is equally simple: the new ramp has value zero at activation, so `Psi` remains continuous, while its right derivative decreases by `w_q`. No formal Euler-product continuation is involved anywhere in this argument.

## One checkpoint per prime-power interval

Order the prime powers as

`2=q_1<q_2<...`,

and let `lambda_j=log q_j`. Include the event at the left endpoint in the post-event state

`P_j=sum_(i<=j) w_(q_i)`,

`Q_j=sum_(i<=j) w_(q_i) lambda_i`.

On the closed interval `I_j=[lambda_j,lambda_(j+1)]`, the value at the right endpoint is still given by the old state because the newly activated ramp there has zero length. Thus

`Psi(t)=R(t)-P_j t+Q_j`

throughout `I_j` in the value sense. Strict convexity gives a unique constrained minimizer. Equivalently, since `R'` is strictly increasing there,

- the minimum is the left endpoint if `P_j<=R'(lambda_j)`;
- it is the unique interior solution of `R'(t)=P_j` when `P_j` lies between the endpoint derivative values;
- it is the right endpoint if `P_j>=R'(lambda_(j+1))`.

The minimum can be written without cases using the restricted Legendre transform

`R^*_(I_j)(y)=sup_(t in I_j) [y t-R(t)]`:

`m_j=Q_j-R^*_(I_j)(P_j)`.

If the minimizer is interior, the drawdown from either endpoint is the Bregman divergence of the strictly convex function `R`. For example,

`Psi(lambda_j)-m_j = R(lambda_j)-R(t_j^*)-R'(t_j^*)(lambda_j-t_j^*) >= 0`.

Suzuki proves unconditionally that `Psi(t)>0` on an interval extending beyond `log 2`. Combining that initial positivity with his Theorem 1.7 therefore gives the exact countable criterion

`RH <=> m_j>=0 for every prime-power interval I_j`.

This is a reduction of quantifiers, not a proof of the inequalities.

## Prime-exponent and dynamical interpretation

For an event `q=p^k`,

`v(q)=k e_p`,

`lambda_q=<v(q),(log r)_r>=k log p`,

`w_q=log p * exp(-lambda_q/2)`.

Thus the event stream is the image of the prime-power axis skeleton under the lattice energy map, with the critical `1/2` normalization appearing in the event amplitude. The full exponent lattice does not enter directly: even the complete history of the scalar function on an arithmetic interval is summarized by only

`P_j=sum w_q`,  `Q_j=sum w_q lambda_q`.

The clock change makes the dynamics even more explicit. Between events,

`Y=-Psi'=P_j-R'(t)`.

Since `tau=R'(t)` and `d tau/dt=R''(t)>0`,

`dY/dtau=-1`.

At an event, the new von-Mangoldt ramp subtracts `w_q` from `Psi'`, so `Y` jumps upward by `w_q`. Therefore the only arithmetic forcing is a sequence of positive jumps at the ordered prime-power times; the archimedean completion supplies the deterministic service clock.

When `Y>0`, `Psi` decreases. If no new event arrives first, the unit drift eventually brings `Y` to zero and `Psi` reaches the unique interval minimum. An event can raise `Y` again and extend the descending episode. This is the precise mathematical content behind the recent "recovery witness" language: it is not an analogy imported from queueing theory but an exact time-changed differential/jump identity.

The reduction is useful diagnostically. Any proposed full-lattice or mixed-prime geometric mechanism that is meant to act **through Suzuki's scalar `Psi`** must first show how its extra information changes or constrains this two-state axis process. Otherwise those mixed exponent coordinates are invisible to the criterion being analyzed.

## No uniform checkpoint reserve can be the missing theorem

The checkpoint form also gives an exact asymptotic boundary. Under RH, Suzuki's zero expansion is

`Psi(t)=sum_gamma (1-cos(gamma t))/gamma^2`,

with real zero ordinates and `sum_gamma |gamma|^(-2)<infinity`. The series is uniformly absolutely convergent. For any finite set of ordinates, simultaneous Diophantine approximation gives arbitrarily large `t` for which all corresponding phases are arbitrarily close to multiples of `2pi`; the uniformly small tail then gives

`liminf_(t->infinity) Psi(t)=0`.

No simplicity or rational linear independence assumption is required for this liminf statement: if a finite frequency set has an exact common period, arbitrarily large multiples give recurrence; otherwise the simultaneous approximants themselves have an unbounded subsequence.

Under RH every checkpoint margin is nonnegative, and the checkpoint in the interval containing such a recurrent `t` is no larger than `Psi(t)`. Hence

`RH => inf_j m_j=0`.

So a strategy that seeks a uniform estimate

`m_j>=c>0`

for all sufficiently large prime-power intervals is not merely stronger than needed; it is incompatible with the expected/conditional zeta dynamics under RH. The required infinite-tail theorem must control **no crossing below zero with vanishing reserves**, not establish a positive global margin.

This sharpens the practical meaning of the recent checkpoint literature: finite certification can be a rigorous bounded theorem, but no amount of finite positive margin by itself extrapolates to RH.

## Prior-art and novelty audit

Primary and current sources:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487, DOI `10.1112/jlms.12785`. Equation (1.1) supplies the exact completed prime-power formula, Theorem 1.7 proves `RH <=> Psi(t)>=0`, Section 4 proves initial positivity past `log 2`, and Section 11 supplies the shifted family used in `PL-145`.
- **Rainer Andreas Mittermeier**, “Prime-power checkpoints for the Riemann zeta screw function: Plastic-Constant Convexity and a Restricted Legendre--Mangoldt Representation,” Zenodo preprint, version 3, 9 August 2026, DOI `10.5281/zenodo.21859280`. Its public abstract states the same plastic-constant curvature factorization, one-checkpoint-per-prime-power-interval reduction, restricted Legendre--Mangoldt/Bregman organization, and two-state recurrence. This is a self-published preprint and is used here chiefly as a novelty/prior-art control; the core statements above were rederived directly from Suzuki's peer-reviewed formula.
- **Rainer Andreas Mittermeier**, “Recovery Witnesses in the Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact Quantifier Reduction for the Riemann-Hypothesis Tail — Part 4,” Zenodo preprint, 26 August 2026, DOI `10.5281/zenodo.22076079`. Its public abstract states the same unit-drift service-clock dynamics and recovery-witness reduction. Again this is used as current prior art rather than as independent authority for the elementary identities rederived above.
- **Rainer Andreas Mittermeier**, “Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence — Part 5,” Zenodo preprint, 26 August 2026, DOI `10.5281/zenodo.22076088`. The abstract continues the program to a weighted-Chebyshev bridge and explicitly notes that no positive uniform reserve can close the tail. The stronger terminal-episode theorem and quantitative tail architecture have not been independently reconstructed in this finding and are therefore not promoted as canonical evidence here.

A structural literature search using the exact terms `plastic constant`, `prime-power checkpoints`, `service clock`, Suzuki's `Psi`, and convex interval minima found this August 2026 preprint series as the direct match and no earlier source with the same checkpoint organization. The underlying ingredients remain Suzuki's established explicit formula plus elementary calculus/convexity. Accordingly, **the mathematical reduction is substantive for this research line but is current prior art, not a novelty claim**.

This does not duplicate `PL-044`, which isolates the prime-power activation thresholds in localized Weil operators but does not reduce Suzuki's pointwise scalar criterion to strict-convex checkpoints. It sharpens `PL-144`, which identified `Psi>=0` as the minimal completed positivity target, by discretizing that target exactly. It also complements `PL-145`: the shifted-omega Volterra flow transports the entire scalar family in the wrong order direction, whereas the present result resolves the fixed `omega=0` scalar problem into its intrinsic prime-power event dynamics.

## Adversarial boundaries and falsification

1. **The checkpoint reduction is not an RH proof.** `RH <=> all m_j>=0` is another exact equivalent criterion. The unresolved burden is the infinite family of inequalities.

2. **Strict convexity is interval-local.** `Psi'` has downward jumps at prime-power events, so `Psi` is not globally convex. The theorem is one constrained minimum per event interval, not one global minimum.

3. **The plastic constant is archimedean, not prime arithmetic.** It arises from the smooth completed term `R''`; its significance here is only that the curvature transition occurs before the first prime-power event. It does not geometrically explain the critical line.

4. **The critical `1/2` is already in the Weil/Suzuki normalization.** Event weights are `Lambda(q)/sqrt(q)`. The checkpoint dynamics does not derive that exponent from the abstract exponent lattice.

5. **Mixed exponent vectors are absent, not secretly encoded as primitive events.** `Lambda` restricts the forcing to `q=p^k`. Composite mixed-prime integers can only enter through external identities that re-express or constrain the cumulative states; they do not appear in Suzuki's event forcing itself.

6. **Finite computer certificates do not settle the tail.** Recent preprints report rigorous directed-rounding verification to large finite cutoffs, but this finding does not rely on those computations, and finite positivity cannot establish the required infinite no-crossing statement.

7. **The no-uniform-margin statement is conditional only through RH.** It says any successful proof of RH must be compatible with checkpoint margins approaching zero; it does not assert unconditionally that the actual margins are nonnegative.

A decisive falsification of the exact structural claim would require an error in Suzuki's prime-power formula, an arithmetic interval with `R''<=0` after `log 2`, more than one constrained minimum on an event interval despite strict convexity, or a non-prime-power term in the von-Mangoldt forcing. The displayed factorization and support rules exclude those possibilities.

## Consequence for the research line

The fixed-`omega=0` completed-zeta route now has a very explicit frontier:

`prime-power exponent rays -> ordered energies log(p^k) -> positive jumps Lambda(p^k)/sqrt(p^k) -> unit-drift archimedean clock -> checkpoint reserve m_j`.

This is a genuine arithmetic dynamical system tied to the completed explicit formula, but it is only two-state and axis-supported. The most useful next question is therefore not to invent another continuous geometry for `Psi`. It is whether exact rational-prime structure can force the **vanishing-margin no-crossing law** for this event process — for example via a rigorous weighted-Chebyshev, correlation, or global-duality inequality — without simply assuming an RH-equivalent positivity statement. Any proposed full exponent-lattice mechanism should be tested by whether it produces a new constraint on `(P_j,Q_j)` or on the recovery/checkpoint margins; if it does not, it cannot affect this canonical scalar channel.