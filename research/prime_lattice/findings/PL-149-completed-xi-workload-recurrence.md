# PL-149 — Completed `xi` forbids terminal Suzuki workload regimes; recovery existence is continuation-generic

## Claim

The exact workload dynamics isolated in `PL-146` has an unconditional recurrence property that can be proved directly from Suzuki's completed transform, without assuming RH. If

`Y(t) = -Psi'(t)`

is taken on the prime-power intervals with either one-sided value at the jump points, then `Y` is neither eventually nonnegative nor eventually nonpositive. Consequently it takes both signs arbitrarily far out and has infinitely many sign changes. In the unit-drift checkpoint dynamics of `PL-146`, this means there are infinitely many prime-power restarts from negative to positive workload and infinitely many later recovery crossings from positive to negative workload. No terminal permanently active or permanently inactive regime is possible.

The mechanism is not a bare prime-lattice theorem. Suzuki's one-sided Fourier-Laplace transform gives, initially for `Re(a)>1/2`,

`L_Y(a) = integral_0^infinity Y(t) exp(-a t) dt = -(1/a) (xi'/xi)(1/2+a)`.

The right-hand side continues meromorphically to the whole `a`-plane, is regular on the entire real axis, and has genuine nonreal poles at the shifted nontrivial zeros `a=rho-1/2`. A Landau one-sign theorem then forbids an eventually one-signed tail: an eventually nonnegative Laplace transform with finite abscissa must have a singularity at its real abscissa of convergence, while the completed logarithmic derivative has no real singularity; the alternative of abscissa `-infinity` would make the tail transform entire, contradicting its inherited nonreal zero poles.

This independently reconstructs the core "terminal episode" conclusion advertised in Rainer Andreas Mittermeier's August 2026 checkpoint preprints. Those preprints are therefore direct current prior art for the recurrence organization, not novelty evidence. The useful line-level consequence is negative: **mere existence of infinitely many recoveries cannot be the missing RH theorem.** That recurrence follows already from analytic continuation, completion symmetry, and the nonreal zero divisor. The unresolved RH content remains the sign of the *values* at the recurrent minima/checkpoints, not whether the workload ever recovers.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + STRUCTURAL-REDUCTION + NEGATIVE/OBSTRUCTION`. Suzuki's transform and growth estimate are peer-reviewed literature; the Landau theorem is classical and is also stated and used explicitly in Suzuki's later weighted-Chebyshev paper. The sign-recurrence deduction below is an exact application of those ingredients. It is not claimed as a new theorem because the same terminal-episode conclusion is present in Mittermeier's current self-published checkpoint program.

## Exact Laplace transform of the checkpoint workload

Suzuki proves for his completed zeta screw function `Psi`, for `Im(z)>1/2`,

`integral_0^infinity Psi(t) exp(i z t) dt = -(1/z^2) (xi'/xi)(1/2-i z)`.

Put `z=i a`. Then `Im(z)=Re(a)`, so for `Re(a)>1/2`,

`integral_0^infinity Psi(t) exp(-a t) dt = (1/a^2) (xi'/xi)(1/2+a)`.

Suzuki also gives `Psi(0)=0` and the unconditional bound

`Psi(t) << exp(t/2-c sqrt(t))`

for some positive constant `c`. Hence integration by parts is legitimate in the same half-plane. With `Y=-Psi'` away from the discrete prime-power jump set,

`integral_0^infinity Y(t) exp(-a t) dt`

`= -a integral_0^infinity Psi(t) exp(-a t) dt`

`= -(1/a) (xi'/xi)(1/2+a)`.

The derivative jumps do not create distributional delta masses because `Psi` itself is continuous; `Y` is simply the piecewise-smooth one-sided derivative with ordinary jump discontinuities.

The apparent factor `1/a` is harmless at `a=0`. The completed function satisfies `xi(s)=xi(1-s)`, so `xi'/xi` is odd around `s=1/2`; moreover `xi(1/2)` is nonzero. Thus `(xi'/xi)(1/2+a)=O(a)` and `L_Y` has a removable singularity at the origin.

Classically `xi` has no real zeros, while it has infinitely many nonreal zeros. Therefore the meromorphic continuation of `L_Y` has **no real poles at all**, but has a genuine nonreal pole at

`a=rho-1/2`

for every nontrivial zero `rho` of zeta. A multiple zero still produces a simple logarithmic-derivative pole, with nonzero residue. This is the only zero information needed below; no assumption on the real parts of those zeros enters.

## Landau one-sign obstruction

Assume first, for contradiction, that there is a `T` such that `Y(t)>=0` for almost every `t>=T`. Define

`f_T(t)=Y(t) 1_(t>=T)`.

Its Laplace transform `F_T(a)` converges at least for `Re(a)>1/2`, and on that half-plane

`F_T(a)=L_Y(a)-integral_0^T Y(t) exp(-a t) dt`.

The second term is entire because `Y` is locally integrable. Hence `F_T` has a meromorphic continuation to the whole plane whose singularities are exactly the nonreal poles inherited from `L_Y`; in particular, it is analytic at every real `a`.

Let `sigma_c` be the abscissa of convergence of the nonnegative tail transform. It cannot be `-infinity`. If it were, `F_T` would be entire. But on `Re(a)>1/2` it equals the displayed meromorphic continuation, and the identity theorem would then remove every shifted-zero pole, contradicting the genuine poles of `xi'/xi`.

Thus `sigma_c` is finite. Landau's theorem for a nonnegative Laplace/Mellin transform says that the real boundary point `a=sigma_c` must be a singularity of the analytic function represented by the transform. That is impossible here, because the explicit meromorphic continuation is analytic on the full real axis. Therefore `Y` cannot be eventually nonnegative.

Applying the same argument to `-Y` shows that `Y` cannot be eventually nonpositive either. It follows that both signs occur arbitrarily far out. Since `Y` is piecewise continuous with only the prime-power jumps, finite total sign variation would imply an eventual one-sided sign. Hence `Y` changes sign infinitely often.

This use of continuation is essential. The conclusion is not obtained by inserting the critical line into an Euler product or a Dirichlet series beyond absolute convergence. The Laplace identity is first established by Suzuki in its valid half-plane and then the **completed meromorphic logarithmic derivative** supplies the continuation on which Landau's contradiction operates.

## Prime-lattice dynamical consequence

For a prime-power event `q=p^k`, `PL-146` writes

`lambda_q = log q = <k e_p,(log r)_r>`,

`w_q = Lambda(q)/sqrt(q) = log(p) exp(-lambda_q/2)`.

After the archimedean clock change `tau=R'(t)`, the workload satisfies

`dY/dtau=-1`

between events and

`Y(lambda_q^+) = Y(lambda_q^-) + w_q`

at the event. Thus `Y` can cross from positive to negative only during the deterministic downward drift, while a negative-to-positive restart can occur only through a prime-power jump.

Because the preceding section forces both signs arbitrarily far out, there must be infinitely many such cycles. In particular:

- infinitely many prime-power events participate in negative-to-positive workload restarts;
- infinitely many later descending inter-event segments, possibly reaching zero at their right event endpoint before the upward jump, contain a recovery zero where `Y` passes from positive to nonpositive;
- neither an eventually positive "terminal active episode" nor an eventually negative permanently idle state is possible.

This is stronger than merely observing that a finite computation has found many recovery witnesses. It is an unconditional infinite-tail statement, but it controls only the **derivative/workload state**. It says nothing about whether the corresponding local minimum of `Psi` lies above or below zero.

That distinction is exactly the RH boundary. Suzuki's theorem remains

`RH <=> Psi(t)>=0 for every real t`,

and `PL-146` reduces this to nonnegativity of every checkpoint margin. Infinite recovery only says those checkpoints continue to occur; it does not supply their required sign.

## Prior-art and novelty audit

Primary theorem-level sources:

- **Masatoshi Suzuki**, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **108**(4) (2023), 1448–1487. DOI `10.1112/jlms.12785`; arXiv `2206.03682`. Theorem 1.1 gives the one-sided Fourier transform of `Psi`, its continuity and growth estimate; the same paper supplies the explicit prime-power formula and the RH-equivalent positivity used in `PL-143`--`PL-148`.
- **Masatoshi Suzuki**, “On variants of Chebyshev’s conjecture,” *The Ramanujan Journal* **68** (2025), article 95. DOI `10.1007/s11139-025-01238-9`; arXiv `2411.07436`. Proposition 1 states the Landau-type Mellin theorem used there to turn eventual one-sign information into a boundary singularity. The later correction concerns the arithmetic-progression portion and does not affect this general proposition or the zeta theorem used in `PL-147`.

Direct current novelty controls:

- **Rainer Andreas Mittermeier**, “Recovery Witnesses in the Prime-Power Checkpoint Program: Service-Clock Geometry and an Exact Quantifier Reduction for the Riemann-Hypothesis Tail — Part 4,” Zenodo preprint, 26 August 2026, DOI `10.5281/zenodo.22076079`. Its public description gives the same unit-drift service-clock/recovery-witness organization already audited in `PL-146`.
- **Rainer Andreas Mittermeier**, “Deep Episodes in the Prime-Power Checkpoint Program: An Unconditional Terminal-Episode Theorem, an Exact Chebyshev Bridge, and Sharp Recovery Recurrence — Part 5,” Zenodo preprint, 26 August 2026, DOI `10.5281/zenodo.22076088`. Its public description explicitly advertises exclusion of a terminal active episode by a Pringsheim--Landau/analytic-continuation argument and infinitely many finite recoveries.

The Mittermeier items are self-published current preprints and are used here only as novelty/prior-art controls. The proof stored above does not depend on their unpublished details: it is reconstructed from Suzuki's peer-reviewed transform plus the classical Landau theorem. Accordingly no novelty is claimed for the terminal-episode/recovery conclusion.

## Generic matched control

The same argument exposes why this recurrence is not yet the rational-prime rigidity sought by the line. Abstractly, suppose a real locally integrable function `Psi_F` has a tail transform

`integral_0^infinity (-Psi_F'(t)) exp(-a t) dt = -C(a) F'/F(s_0+a)`

in some right half-plane, where the right-hand side has a meromorphic continuation, is regular on the real `a`-axis, and retains at least one genuine nonreal pole. Then the identical Landau argument forbids eventual one-sign behavior of `-Psi_F'`, provided the tail transform has the usual finite initial abscissa.

Any completed spectral function satisfying those hypotheses therefore gives the same qualitative obstruction. What is special to the Riemann prime lattice in the Suzuki realization is the *forcing decomposition*: its jumps occur exactly at

`log(p^k)`

with weights `Lambda(p^k)/sqrt(p^k)`. The theorem that this forcing cannot remain forever on one side after completion is instead a continuation/zero-divisor phenomenon. It does not distinguish the exact rational-prime norm map from a broader completed spectral system.

This generic control is important under the line mandate. A candidate mechanism that merely rediscovers recurrent recoveries, even if phrased geometrically in the exponent lattice, has not yet passed the Helson/Beurling/generic-spectrum falsification bar. It must extract a property of the **checkpoint values or their arithmetic coupling** that is unavailable from the completed logarithmic derivative alone.

## Adversarial boundaries and falsification

1. **This is not an RH proof or a new RH criterion.** The theorem only excludes eventual one-sign behavior of `Y=-Psi'`. `Psi` itself may in principle have negative recurrent minima; ruling those out is precisely the unresolved RH content.

2. **The existence of nonreal zeta zeros is unconditional and sufficient.** No zero needs to lie off the critical line. In fact the known critical-line zeros already supply nonreal poles of the shifted logarithmic derivative in the `a`-plane.

3. **No real-zero pole is being hidden.** The completed Riemann `xi` has no zeros on the real `s`-axis, so `a -> (xi'/xi)(1/2+a)` is regular for real `a`. The point `a=0` is removable because of the functional equation symmetry and `xi(1/2)!=0`.

4. **The sign statement is insensitive to the values assigned at event points.** Prime-power events form a discrete set. Eventual nonnegativity/nonpositivity for the Landau argument is an almost-everywhere tail property, while the dynamics can use either one-sided representative at the jumps.

5. **Infinitely many sign changes do not imply a uniform recovery reserve.** `PL-146` already shows, conditionally on RH, that checkpoint margins have infimum zero. The present theorem is compatible with arbitrarily deep or arbitrarily shallow episodes and gives no positive lower bound.

6. **The half-weight is still inserted by the completed explicit formula.** The event amplitudes `Lambda(q)/sqrt(q)` are not derived from the abstract free exponent cone. This finding explains a consequence of the completed critical normalization, not why the normalization must be `1/2`.

7. **The full exponent lattice remains absent.** As in `PL-146`--`PL-148`, the arithmetic forcing is supported only on axis points `k e_p`. Mixed-support exponent vectors are not recovered by the recurrence proof.

A falsification would require failure of Suzuki's transform/growth identity, a real zero of the completed `xi`, absence of all nonreal zeros, or a failure of the classical Landau boundary-singularity theorem for the nonnegative tail transform. None is compatible with the cited classical/peer-reviewed inputs.

## Consequence for the research line

Do not spend further passes trying to prove RH by establishing only that Suzuki's prime-power workload recovers infinitely often or that terminal episodes are impossible. That qualitative recurrence is already forced unconditionally by the completed transform and is direct current prior art.

The surviving checkpoint target is **recovery-conditioned value control**: determine whether exact rational-prime structure supplies a constraint on the accumulated height `Psi` at the recurrent workload zeros strong enough to prevent a crossing below zero. Any successful mechanism must distinguish that value constraint from the generic Landau recurrence shared by other completed spectral systems. Equivalently, the research burden has moved from proving that recovery occurs to explaining why every recovered minimum should have nonnegative reserve.