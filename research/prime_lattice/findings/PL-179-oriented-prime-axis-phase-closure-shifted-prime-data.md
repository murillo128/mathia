# PL-179 — Oriented prime-axis phase closure is only shifted-prime multiplicative data

## Claim

The most canonical phase-valued refinement of the one-prime-axis affine closure in `PL-178` does not preserve a new exponent-lattice holonomy. Let

\[
f:\mathbb N\to\mathbb T
\]

be any completely multiplicative unit-modulus function, let `r,q` be primes, and define the oriented affine plaquette phase

\[
\mathcal C_f(n;r,q)
=
f(n)\overline{f(rn)}\,\overline{f(qn)}f((r+q-1)n).
\]

Because

\[
rn+qn=n+(r+q-1)n,
\]

this is the standard conjugated four-point phase attached to the same additive parallelogram used in `PL-177` and `PL-178`. Complete multiplicativity gives the exact pointwise reduction

\[
\boxed{
\mathcal C_f(n;r,q)
=
\overline{f(r)}\,\overline{f(q)}f(r+q-1),
}
\]

so the base point `n` disappears identically.

For the canonical total-exponent phase

\[
f_z(m)=z^{\Omega(m)}
=z^{\langle v(m),\mathbf 1\rangle},
\qquad |z|=1,
\]

all primes have the same phase `f_z(p)=z`, and therefore

\[
\boxed{
\mathcal C_{f_z}(n;r,q)
=z^{\Omega(r+q-1)-2}.
}
\]

After freezing `r` and averaging over the prime `q`, the entire phase-valued lattice observable is consequently just

\[
\boxed{
\frac1{\pi(X)}\sum_{q\le X}\mathcal C_{f_z}(n;r,q)
=
z^{-2}\frac1{\pi(X)}\sum_{q\le X}z^{\Omega(q+r-1)}.
}
\]

At `z=-1` this is exactly `PL-178`. For general `z`, replacing Liouville parity by the full one-parameter `Omega` phase therefore lands on the classical theory of multiplicative functions on shifted primes rather than producing a new geometric or spectral invariant of the prime-exponent lattice.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT + NEGATIVE/OBSTRUCTION`. The phase reduction is elementary and exact. The shifted-prime classification is anchored by peer-reviewed work of Hildebrand, Timofeev, Khripunova, and Lichtman. A September 2026 preprint of Biao Wang is used only as a current-literature audit of the fixed-versus-shift-averaged dynamical frontier. This finding is decisive only for the canonical **oriented** unitary phase lift of the affine plaquette, and especially for the intrinsic constant-prime phase family `z^Omega`; it does not exclude non-oriented observables, prime-dependent phase assignments, genuinely joint source conditioning, or target/completion data inserted before the collapse.

## Exact phase derivation

For a unitary completely multiplicative function,

\[
f(rn)=f(r)f(n),\qquad
f(qn)=f(q)f(n),\qquad
f((r+q-1)n)=f(r+q-1)f(n).
\]

Hence

\[
\begin{aligned}
\mathcal C_f(n;r,q)
&=f(n)\overline{f(r)f(n)}\,
  \overline{f(q)f(n)}f(r+q-1)f(n)\\
&=\overline{f(r)}\,\overline{f(q)}f(r+q-1),
\end{aligned}
\]

because `|f(n)|=1`. There is no limiting argument, Fourier estimate, or analytic continuation in this step.

The orientation is not cosmetic. For a general complex phase, the ordinary unsigned product of the four values contains `f(n)^4`; the conjugated pattern above is the canonical phase analogue of a second multiplicative difference / `U(1)` plaquette observable. When `f=lambda`, all values are real signs and conjugation is invisible, so the formula reduces to the parity identity already used in `PL-178`.

For `f_z(m)=z^{Omega(m)}`, complete additivity of `Omega` gives

\[
\Omega(rn)=\Omega(n)+1,
\quad
\Omega(qn)=\Omega(n)+1,
\quad
\Omega((r+q-1)n)=\Omega(n)+\Omega(r+q-1),
\]

and therefore the exponent in the oriented product is

\[
\Omega(n)-\Omega(rn)-\Omega(qn)+\Omega((r+q-1)n)
=\Omega(r+q-1)-2.
\]

In exponent-vector language, `f_z` is the character obtained by projecting `v(m)` onto the total occupation number `sum_p v_p(m)`. The oriented plaquette removes the common base vector exactly. Thus the apparent phase holonomy does not measure curvature of the exponent cone: after the additive closure it measures only the factor-count phase of the shifted integer `q+r-1`.

## Classical shifted-prime prior art

This reduction lands in a long-standing literature rather than an unexplored lattice problem.

Adolf Hildebrand, *Additive and Multiplicative Functions on Shifted Primes*, *Proceedings of the London Mathematical Society* (3) **59** (1989), 209--232, DOI `10.1112/plms/s3-59.2.209`, proves several mean-value and distribution results for additive and multiplicative functions on the sequence `{p+1}`, including a complete Erdos--Wintner analogue for additive functions and a partial Halasz analogue for multiplicative functions. This is already the natural classical setting for `z^{Omega(p+1)}` and related phases.

N. M. Timofeev, *Multiplicative functions on the set of shifted prime numbers*, *Izvestiya Mathematics* **39**(3) (1992), 1189--1207, DOI `10.1070/IM1992v039n03ABEH002243`, treats multiplicative functions on `{p+a}` for a nonzero fixed integer `a`, giving estimates or asymptotics for their averages under the paper's hypotheses. Thus the general fixed `r` output `f_z(q+r-1)` is already in the established shifted-prime mean-value framework.

There is even phase-specific fixed-shift prior art. M. B. Khripunova, *On a multiplicative function on the set of shifted primes*, *Mathematical Notes* **64**(3) (1998), 394--400, DOI `10.1007/BF02314850`, proves that if a multiplicative `f` has a fixed nontrivial cube-root value `zeta` on the primes and satisfies the stated cube-root condition on prime powers, then

\[
\left|\sum_{p\le x}f(p+1)\right|\le\theta\pi(x)
\]

for some `theta<1`. The canonical `f_z(n)=z^{Omega(n)}` with primitive cube-root `z` satisfies those algebraic hypotheses. Taking the frozen source `r=2` in the present lattice reduction gives exactly `z^{-2} z^{Omega(q+1)}`. Khripunova's theorem is therefore a direct classical estimate for one non-parity phase of the canonical single-axis plaquette. It is a strict contraction, not a proof that the normalized mean tends to zero.

Jared Duker Lichtman's peer-reviewed *Averages of the Mobius Function on Shifted Primes*, *Quarterly Journal of Mathematics* **73**(2) (2022), 729--757, DOI `10.1093/qmath/haab054`, proves cancellation after averaging over a sufficiently long range of shifts for Mobius/Liouville and also gives a theorem for general nonpretentious bounded multiplicative functions in the polynomial shift range. The paper explicitly separates these averaged results from the folklore fixed-shift Mobius/Liouville problem. This is the same structural boundary exposed by `PL-178` and persists for phase-valued multiplicative functions unless an independent fixed-shift theorem applies.

## Current dynamical frontier

Biao Wang's recent preprint, *A dynamical generalization of Chowla's conjecture on average*, arXiv:`2608.16108` (current manuscript dated 2 September 2026), provides a useful current audit but is not used as peer-reviewed authority. For a uniquely ergodic system `(X,nu,T)`, Wang proves a prime analogue in which one averages simultaneously over the prime variable and over all shifts `h_1,...,h_k<=N`:

\[
\frac1{N^k\pi(N)}
\sum_{h_1,\ldots,h_k\le N}
\sum_{p\le N}
F\!\left(T^{\Omega(p+h_1)+\cdots+\Omega(p+h_k)}x\right)
\longrightarrow
\int_X F\,d\nu.
\]

The same paper explicitly presents the corresponding statement for prescribed fixed shifts as an expected pointwise strengthening rather than as the proved theorem. Taking a finite cyclic rotation turns the averaged theorem into a root-of-unity phase statement; taking circle rotations gives the analogous dynamical characteristic-function viewpoint. Thus broad shift averaging of `Omega` phases is already part of current dynamical/number-theoretic prior art, while fixed or specially conditioned shifts remain the hard boundary.

This current preprint reinforces the negative interpretation but is not required for the exact reduction or for the claim that shifted-prime multiplicative phases are classical prior art.

## Novelty and conflicting-claim audit

This is a classicalization/redirect, not a novelty claim. The identity for `mathcal C_f` is an elementary consequence of complete multiplicativity once the oriented plaquette is specified. The literature audit shows that the scalar object remaining after the cancellation belongs to an established shifted-prime theory dating at least to Hildebrand and Timofeev.

No source found in the audit justifies claiming unconditional zero mean for

\[
\frac1{\pi(X)}\sum_{q\le X}z^{\Omega(q+h)}
\]

for every prescribed fixed `h` and every nontrivial unit phase `z`. In particular, Khripunova's cube-root result gives a uniform contraction for `h=1`, not convergence to zero, while Lichtman and Wang obtain strong conclusions only after averaging over the input shift in the relevant statements cited here. The fixed-shift phase problem must therefore not be silently promoted to a solved equidistribution theorem.

The audit also does not identify an RH-sensitive rate or a continuation theorem associated with these shifted-prime phase means. Even if a fixed-shift phase mean were proved to vanish, that would be a multiplicative-pseudorandomness statement unless an additional quantitative bridge to `Re(s)=1/2`, the functional equation, or a Weil/Nyman criterion were supplied.

## Adversarial checks and limitations

- **Orientation is essential.** The cancellation of `n` uses the conjugated `+,-,-,+` phase pattern. An arbitrary nonlinear or unsigned four-phase observable is not covered.
- **The exact all-unitary statement is only base cancellation.** For a general prime-dependent completely multiplicative phase, the residual is `overline{f(r)} overline{f(q)} f(r+q-1)` and still contains the source phase `f(q)`. Only the intrinsic constant-prime family `f_z=z^Omega` reduces to the unweighted shifted-prime characteristic function displayed above.
- **Fixed shifts remain distinct from averaged shifts.** Results that average over `h` cannot be specialized to the sparse values `h=r-1` with `r` prime, nor to one prescribed `r`, without an additional uniform theorem.
- **A growing frozen source needs separate uniformity.** If `r=r(X)` grows with `X`, the pointwise algebraic reduction remains exact but fixed-`h` prior art does not by itself control the resulting family uniformly.
- **Khripunova does not prove Haar flatness.** The cube-root estimate gives modulus bounded by a constant strictly below `1`; it is compatible both with eventual zero mean and with a nonzero limiting phase bias.
- **Wang 2026 is a preprint.** Its role here is only to locate the current averaged dynamical frontier. The durable negative already follows from the exact reduction plus classical peer-reviewed shifted-prime literature.
- **No analytic continuation.** Every identity in this finding is finite and arithmetic. No Euler product is continued through `Re(s)=1`, and no critical-line statement is obtained.
- **No RH implication.** The total-exponent character `z^Omega` is a natural phase lift of Liouville parity, but the reduction supplies no mechanism selecting zeta zeros or the line `Re(s)=1/2`.
- **Target-relative and jointly conditioned constructions survive.** A coupling that inserts a distinguished Nyman/Weil/completion target, conditions `(r,q)` jointly before forming the plaquette, or transports additional data before the multiplicative cancellation is not ruled out.

## Consequence for the research line

The accepted affine non-Haar clue should no longer treat a bare `Omega`-phase upgrade of the canonical one-prime-axis plaquette as a new phase-conditioned escape. The natural `U(1)`-oriented observable cancels the base exponent vector exactly and leaves only a classical shifted-prime multiplicative phase.

A surviving phase-conditioned branch must therefore add information **before** this reduction: a genuinely non-product or thin condition on the source pair, a prime-dependent phase whose residual coupling is independently justified and not merely another unresolved correlation, or completed/target-relative data that cannot factor out with the base phase. Replacing `lambda` by `z^Omega` and then relabeling the shifted-prime characteristic function as a holonomy, trace, or spectrum does not create new RH structure.