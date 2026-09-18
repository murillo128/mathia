# PL-362 — Positive coefficientwise energy filters cannot continue zeta past `Re(s)=1` without renormalization

**Evidence:** `EXACT-DERIVED + CLASSICAL-POSITIVITY-CONTROL + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-361`.

**Related finding:** `PL-360`.

**Status:** `POSITIVE-COEFFICIENTWISE-SUMMATION-CANNOT-CROSS-THE-ZETA-CONVERGENCE-WALL + ANY-CRITICAL-STRIP-CONTINUATION-MUST-INTRODUCE-SIGNED-COMPLEX-OR-COUNTERTERM-STRUCTURE`.

## Precise claim

`PL-361` shows that changing the coefficient topology does not help if the ordinary energy cutoffs

\[
Z_N(s)=\sum_{n\le N}n^{-s}
\]

still converge to the completed zeta object and ordinary evaluation remains continuous. One apparent escape left there is to abandon the sharp cutoffs and replace them by a different summation family. There is, however, a broad class of such summation procedures that still cannot cross `Re(s)=1`: **coefficientwise-positive approximate identities**.

Let `I` be a directed set and let

\[
w_i(n)\ge 0\qquad(i\in I,\ n\ge1)
\tag{PL362-1}
\]

satisfy

\[
w_i(n)\longrightarrow1
\qquad\text{for every fixed }n.
\tag{PL362-2}
\]

For real `sigma`, define the extended nonnegative sum

\[
F_i(\sigma):=\sum_{n\ge1}w_i(n)n^{-\sigma}\in[0,+\infty].
\tag{PL362-3}
\]

Then for every real `sigma<=1`,

\[
\boxed{F_i(\sigma)\longrightarrow+\infty.}
\tag{PL362-4}
\]

No monotonicity of `i -> w_i(n)`, no common finite support, no Hilbert-space topology, and no continuity assumption are needed. Consequently, any diagonal prime-lattice energy regularization whose coefficients remain nonnegative and converge coefficientwise back to the coefficient-one zeta vector cannot produce a finite analytic-continuation value at any real point below `1` by unrenormalized evaluation.

This closes a specific escape left by `PL-361`: replacing sharp partial sums by **positive** Riesz/Cesaro/heat-like energy smoothing does not by itself create analytic continuation. To cross the ordinary convergence wall, the construction must introduce at least one genuinely new ingredient: signed or complex cancellation, a divergent counterterm/finite-part subtraction, non-coefficientwise mixing, a target-relative quotient/model geometry, or an unbounded/distributional evaluation mechanism.

## 1. Exact positive approximate-identity lemma

Fix real `sigma<=1` and `K>0`. Since

\[
\sum_{n\ge1}n^{-\sigma}=+\infty,
\]

there is `N` such that

\[
\frac12\sum_{n\le N}n^{-\sigma}>K.
\tag{PL362-5}
\]

For each of the finitely many integers `1<=n<=N`, (PL362-2) gives eventual inequality `w_i(n)>=1/2`. Directedness provides a common index `i_0` after which all those finitely many inequalities hold simultaneously. Therefore, for every `i>=i_0`,

\[
F_i(\sigma)
\ge
\sum_{n\le N}w_i(n)n^{-\sigma}
\ge
\frac12\sum_{n\le N}n^{-\sigma}
>K.
\tag{PL362-6}
\]

Since `K` was arbitrary, (PL362-4) follows.

The proof is deliberately elementary. It is a Fatou/positivity obstruction in its barest form: once every fixed coefficient is eventually restored with the same sign, the divergent positive mass of the coefficient-one Dirichlet series cannot disappear by smoothing the cutoff.

## 2. Prime-lattice energy formulation

Let

\[
H e_n=(\log n)e_n,
\qquad
\log n=\langle v(n),(\log p)_p\rangle,
\tag{PL362-7}
\]

be the canonical exponent-lattice energy operator. Consider any family of scalar spectral filters `phi_i` with

\[
\phi_i(\log n)\ge0,
\qquad
\phi_i(\log n)\to1
\quad(n\text{ fixed}).
\tag{PL362-8}
\]

Applying `phi_i(H)` to the formal coefficient-one vector produces the regularized Dirichlet expression

\[
Z_i(s)
=
\sum_{n\ge1}\phi_i(\log n)n^{-s}.
\tag{PL362-9}
\]

Whenever the right side is defined as an ordinary nonnegative sum on a real point `sigma<=1`, (PL362-4) gives

\[
Z_i(\sigma)\to+\infty.
\tag{PL362-10}
\]

This includes positive finite energy cutoffs and positive logarithmic Riesz weights such as

\[
\phi_L(\log n)
=
\left(1-\frac{\log n}{L}\right)_+^k,
\qquad k>0,
\tag{PL362-11}
\]

because for every fixed `n` the weight tends to `1` as `L->infinity`. More generally, the conclusion depends only on coefficientwise positivity and recovery, not on the detailed shape of the smoothing kernel.

The statement should **not** be inflated to arbitrary positive operators. A positive-semidefinite non-diagonal operator can have signed or complex matrix coefficients in the Dirichlet basis and can mix the coefficient-one vector into sign-changing output. The theorem concerns coefficientwise-positive filters, equivalently regularizations that preserve the positive cone relevant to (PL362-3).

## 3. Actual analytic continuation escapes by a signed counterterm

The standard Euler--Maclaurin continuation shows concretely what the positive-filter obstruction is demanding. The DLMF representation, initially obtained by Euler--Maclaurin rather than by continuing the Euler product, gives for `Re(s)>0`

\[
\zeta(s)
=
\sum_{n=1}^{N}n^{-s}
+
\frac{N^{1-s}}{s-1}
-
s\int_N^\infty
\frac{x-\lfloor x\rfloor}{x^{s+1}}\,dx.
\tag{PL362-12}
\]

For real `0<sigma<1`, the raw partial sum is positive and grows on the scale `N^(1-sigma)`. The explicit correction

\[
\frac{N^{1-\sigma}}{\sigma-1}<0
\tag{PL362-13}
\]

has precisely the opposite sign and cancels the divergent leading mass. Thus classical continuation does not contradict (PL362-4): it leaves the positive coefficient cone by adding a source-forced divergent counterterm.

This is the structural point relevant to the lattice program. A proposed critical-strip completion cannot merely say that a smoother positive spectral cutoff replaces the sharp `H`-energy cutoff. It must identify where the compensating signed/complex contribution comes from and why that contribution is forced by arithmetic or global symmetry rather than inserted as the already-known continuation.

## 4. Relation to `PL-360` and `PL-361`

The three obstructions remove distinct increasingly broad naive completions.

`PL-360` rules out **diagonal Hilbert weights** that simultaneously contain the coefficient-one zeta vector and make ordinary evaluation bounded in the critical strip. `PL-361` removes diagonality: if the raw energy cutoffs themselves converge in any Hausdorff completion and evaluation is continuous, scalar convergence forces `Re(s)>1`. The present result changes the approximating family as well: even if sharp cutoffs are abandoned entirely, every coefficientwise-positive approximate identity still diverges at every real `sigma<=1`.

Thus the surviving completion problem is not simply “choose better weights” or “smooth the cutoff.” A viable summation mechanism has to cross the positive cone somewhere, or else change the meaning of coefficient recovery/evaluation sufficiently that (PL362-1)--(PL362-3) no longer describe it.

## 5. Prior-art and novelty audit

No theorem-level novelty is claimed for the positivity lemma. It is an elementary consequence of finite-set pointwise convergence and divergence of the positive Dirichlet series, and it sits in the classical neighborhood of **Landau's theorem**: an ordinary Dirichlet series with nonnegative coefficients has a singularity on the real line at its abscissa of absolute convergence. A modern paper explicitly stating and extending that classical theorem is Brian Maurizi, *Extending Landau's Theorem on Dirichlet Series with Non-Negative Coefficients*, arXiv:1009.0228.

The analytic-continuation control is NIST DLMF §25.2, especially equations 25.2.1 and 25.2.8: the coefficient-one Dirichlet series represents zeta only for `Re(s)>1`, while the Euler--Maclaurin formula adds the counterterm in (PL362-12) and continues it to `Re(s)>0`. Modern Riesz-summability theory for Dirichlet series, including Andreas Defant and Ingo Schoolmann, *Riesz means in Hardy spaces on Dirichlet groups*, arXiv:1908.06458, confirms that noncanonical Riesz means are a standard analytic tool; it does not remove the elementary obstruction for a positive approximate identity acting on the coefficient-one series at real `sigma<=1`.

The durable mathematical delta relative to `PL-361` is therefore a **route restriction**, not a new summability theorem: the “altered summation” escape from the Schauder/raw-cutoff obstruction must be sign-indefinite, complex, renormalized, non-coefficientwise, or target-relative if it is to represent the finite continuation of zeta inside the critical strip.

## 6. Adversarial boundaries

1. **Coefficientwise positivity is load-bearing.** Signed or complex weights can cancel the divergent mass and are not covered.

2. **Coefficient recovery is load-bearing.** A family that does not satisfy `w_i(n)->1` for each fixed `n` is not an approximate identity in the sense used here. Such a family may define another transform, but an independent argument is then required to show that it still recovers zeta rather than a different function.

3. **The obstruction is strongest on the real axis.** Positivity of the coefficients does not by itself control cancellation from the phases `n^{-it}` at a nonreal point. The theorem therefore rules out a global critical-strip continuation scheme containing real points below `1`; it does not claim that every complex-only local summation problem is impossible.

4. **The pole at `s=1` is not a contradiction.** Divergence there is consistent with zeta's pole. The decisive continuation obstruction is at real `sigma<1`, where analytic continuation is finite away from the trivial singularity.

5. **Renormalized finite parts are outside the theorem.** Subtracting a divergent counterterm before taking the limit, as Euler--Maclaurin does, changes the observable. That is an allowed escape, but the counterterm then becomes the load-bearing structure to audit.

6. **Positive-semidefinite is not coefficientwise-positive.** Non-diagonal Gram or kernel constructions are not excluded merely because the associated operator is positive. Only preservation of the relevant coefficient cone triggers (PL362-4).

7. **The exact lemma is generic rather than prime-specific.** Rational-prime structure enters through the canonical energy `log n=<v(n),log p>` and the interpretation of `phi_i(H)`. The divergence argument itself applies to any positive coefficient series at its convergence wall. It supplies no RH rigidity by itself.

## Research consequence

After `PL-360`--`PL-362`, a continuation topology that stays entirely inside the positive coefficient cone is no longer a credible route. The next candidate must state explicitly **which load-bearing operation creates the signed/complex cancellation required to cross `Re(s)=1`**, and then show that this operation is independently forced by the rational-prime lattice, the completed functional equation, a target-relative quotient, or another global arithmetic structure.

A construction that merely subtracts the known Euler--Maclaurin divergence, inserts the functional equation by hand, or declares a finite-part value has crossed the analytic wall but has not yet produced an RH mechanism. The remaining test is whether the nonpositive/renormalized structure retains zero-sensitive arithmetic information and naturally singles out the critical half-axis rather than repackaging the already-known continuation.