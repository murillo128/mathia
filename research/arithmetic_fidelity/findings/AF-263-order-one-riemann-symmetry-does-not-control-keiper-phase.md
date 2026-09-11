# AF-263 — Order-one Riemann symmetry does not control Keiper phase

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `LI-DOMINANT-MODE-CONTROL`, `SOURCE-SPECIFIC-NO-GO`, `SYMMETRIC-ZERO-SURGERY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-261 shows that an unrestricted irrational phase can realize any prescribed profinite cancellation level, while AF-262 shows that algebraic unit phases have zero profinite cancellation. The next source question is therefore whether the classical global analytic structure of the Riemann xi function already forces the zero-derived Keiper phase toward the safe side. It does not.

Fix

\[
\frac12<\beta<1,
\qquad
c\in(0,+\infty],
\qquad
H>0.
\tag{1}
\]

There exists an irrational `alpha` and a height `gamma>H` such that

\[
\rho=\beta+i\gamma,
\qquad
\alpha=\frac{\theta_\rho}{\pi},
\qquad
1-\frac1\rho=r_\rho e^{i\theta_\rho},
\tag{2}
\]

and

\[
\boxed{K_{\mathrm{pc}}(\alpha)=c.}
\tag{3}
\]

Moreover the quartet

\[
Q_\rho=
\{\rho,\overline\rho,1-\rho,1-\overline\rho\}
\tag{4}
\]

can be inserted into the Riemann xi zero divisor without leaving the classical order-one reflection-symmetric entire-function category. Namely, let

\[
P_\rho(s)
=
\prod_{z\in Q_\rho}(s-z),
\qquad
F_\rho(s)
=
\frac{P_\rho(s)}{P_\rho(0)}\,\xi(s).
\tag{5}
\]

Then

\[
\boxed{
\begin{aligned}
&F_\rho \text{ is entire of order }1,\\
&F_\rho(1-s)=F_\rho(s),\\
&F_\rho(\overline s)=\overline{F_\rho(s)},\\
&F_\rho(0)=\xi(0),\qquad F_\rho(1)=\xi(1),
\end{aligned}}
\tag{6}
\]

and every zero of `F_rho` still lies in the open critical strip `0<Re(s)<1`. Its zero divisor is exactly the xi divisor with one additional copy of each point in `(4)`. Consequently, for the usual upper-half-plane zero count,

\[
N_{F_\rho}(T)=N_\xi(T)+2
\qquad(T>\gamma),
\tag{7}
\]

counting multiplicity, so `F_rho` has the same Riemann--von Mangoldt leading zero-count asymptotics as `xi`.

For finite `c>0`, the construction may be made with `gamma` so large that

\[
\boxed{c>\log q_\rho,\qquad q_\rho=r_\rho^{-1}>1.}
\tag{8}
\]

Thus AF-261's periodically-complete pair rate becomes

\[
q_\rho e^{-K_{\mathrm{pc}}(\alpha)}
=q_\rho e^{-c}<1.
\tag{9}
\]

The same analytic symmetry/growth class therefore contains arbitrarily high off-critical zero quartets whose Keiper phases have enough profinite cancellation to erase the superunit one-pair witness. No theorem using only order one, the Riemann reflection law, conjugation symmetry, strip location, endpoint normalization, or the leading zero-count asymptotic can supply the source-specific phase restriction sought after AF-262.

## Why it matters

AF-018 established a positive rigidity statement: **once the complete zero divisor is fixed**, order-one growth plus reflection reduces the zero-free ambiguity to a scalar, and one normalization recovers the exact entire function. The present finding identifies the complementary boundary. Those same global constraints do not determine which admissible symmetric zero divisor occurs in the first place. Finite reflection-symmetric zero surgery stays inside the category.

This distinction matters at the current RH-facing frontier. AF-262 leaves open the possibility that some classical analytic property of zeta forces the actual Keiper phases to be Diophantine enough for `K_pc=0` or at least `K_pc<log q_rho`. Equations `(3)`--`(9)` rule out a broad family of such properties before any deep number theory is attempted. The missing source theorem must use structure that distinguishes zeta from the controls `(5)`: for example Dirichlet-series coefficients, Euler-product/arithmetic information, an equivalent zeta-specific constraint, or another input not implied by the completed entire-function symmetry class.

The result also separates two uses of analytic rigidity. A rigid **reconstruction map from a known divisor** does not imply rigidity of the **admissible divisor family**. Arithmetic Fidelity must audit both fibers separately.

## Exact derivation

### 1. AF-261 can realize every cancellation level at arbitrarily small phase

AF-261 constructs its irrational by a continued fraction

\[
\alpha=[0;a_1,a_2,\ldots]
\tag{10}
\]

starting from `a_1=2`, so that the first selected convergent denominator is even and the previous denominator is odd. Nothing in the induction uses the numerical value `2`; it uses only that parity state.

For any integer `m>=1`, start instead with

\[
a_1=2m,
\qquad
q_0=1,
\qquad
q_1=2m.
\tag{11}
\]

Then `q_1` is even and `q_0` is odd, so every subsequent AF-261 step is unchanged: the next partial quotient tunes the exponential jump, an odd bridge makes the following denominator invertible modulo the requested modulus, and one more odd partial quotient steers the next half-denominator into the requested congruence cylinder. The resulting irrational still satisfies `(3)` for the prescribed `c`.

At the same time,

\[
0<\alpha<\frac1{2m},
\tag{12}
\]

so these exact realization controls can be chosen with `alpha` arbitrarily small.

### 2. Small phase pulls back to an arbitrarily high off-critical zero

AF-256 gives the exact zero-coordinate/Keiper-phase relation. Put

\[
A_\beta=\beta(1-\beta),
\qquad
\theta=\pi\alpha.
\tag{13}
\]

For `0<theta<pi/2`, the unique positive height whose Keiper phase is `theta` is

\[
\boxed{
\gamma
=
\frac12\left(
\cot\theta
+
\sqrt{\cot^2\theta+4A_\beta}
\right).
}
\tag{14}
\]

Indeed `(14)` is exactly the inverse of

\[
\cot\theta_\rho
=\gamma-\frac{A_\beta}{\gamma}.
\tag{15}
\]

As `alpha->0`, `theta->0`, hence `cot(theta)->+infinity` and `(14)` gives `gamma->+infinity`. Applying `(12)` with sufficiently large `m` therefore forces `gamma>H` while preserving `(3)`.

The radial factor has the exact form

\[
r_\rho^2
=
\frac{(1-\beta)^2+\gamma^2}
{\beta^2+\gamma^2},
\qquad
q_\rho^2
=
\frac{\beta^2+\gamma^2}
{(1-\beta)^2+\gamma^2}.
\tag{16}
\]

Because `beta>1/2`, one has `q_rho>1`, while

\[
\log q_\rho
=
\frac12\log
\frac{\beta^2+\gamma^2}
{(1-\beta)^2+\gamma^2}
\longrightarrow0
\qquad(\gamma\to\infty).
\tag{17}
\]

For every fixed finite `c>0`, enlarge `m` once more so that `(8)` holds. For `c=+infinity` the inequality is automatic in the extended sense.

### 3. The zero quartet preserves the Riemann symmetries

The multiset `(4)` is invariant under both

\[
z\longmapsto1-z
\qquad\text{and}\qquad
z\longmapsto\overline z.
\tag{18}
\]

It has four elements because `beta` is strictly between `1/2` and `1` and `gamma>0`. Therefore `P_rho` is a real monic quartic. The reflected polynomial `P_rho(1-s)` has the same zeros and the same leading coefficient as `P_rho(s)`, hence

\[
P_\rho(1-s)=P_\rho(s).
\tag{19}
\]

Conjugation invariance similarly gives

\[
P_\rho(\overline s)=\overline{P_\rho(s)}.
\tag{20}
\]

The endpoint value is

\[
P_\rho(0)
=|\rho|^2|1-\rho|^2>0,
\tag{21}
\]

and `(19)` gives `P_rho(1)=P_rho(0)`.

Classically, `xi` is a real entire function of order one and satisfies `xi(1-s)=xi(s)`. Multiplication by a nonzero polynomial does not change its order. Equations `(19)`--`(21)` therefore prove every assertion in `(6)`. They also imply that `F_rho(1/2+it)` is real for real `t`, exactly as for the usual Riemann `Xi` restriction.

Since `0<1-beta<1/2<beta<1`, all four added zeros lie in the open critical strip. The polynomial adds exactly two upper-half-plane zeros, `rho` and `1-overline(rho)`, counting multiplicity. This proves `(7)` and hence preservation of the leading zero-count asymptotic.

### 4. The inserted phase retains the prescribed profinite obstruction

By construction `(14)` makes the zero `rho` satisfy

\[
\alpha_\rho
=\frac{\theta_\rho}{\pi}
=\alpha.
\tag{22}
\]

Thus its profinite cancellation invariant is exactly the AF-261 value `(3)`. For finite positive `c`, equations `(8)` and AF-261's one-pair periodically-complete rate formula give `(9)`. The analytic control therefore reproduces precisely the dangerous source behavior that the post-AF-262 theorem would have to exclude.

This is not a perturbative statement: `c` may be any prescribed positive value, the inserted quartet may be placed above any prescribed height, and the reflection/conjugation symmetries remain exact.

## Prior-art audit

The entire-function ingredients are classical. Riemann's `xi` is an entire function of order one satisfying `xi(s)=xi(1-s)` and the usual conjugation symmetry; standard references include Titchmarsh and the *Encyclopedia of Mathematics* entry **“Riemann xi-function.”** Multiplying an entire function by a polynomial to insert finitely many zeros is elementary, and Weierstrass/Hadamard factorization gives the much broader classical framework for prescribing zero divisors. No novelty is claimed for finite symmetric zero insertion, reflection-symmetric polynomials, order preservation under polynomial multiplication, or the Riemann--von Mangoldt asymptotic.

The relevant rigidity boundary is also classical. Alberto Perelli, **“Converse theorems: from the Riemann zeta function to the Selberg class,”** arXiv:`1605.02354` (2016), surveys Hamburger's converse theorem and its descendants: once suitable Dirichlet-series and regularity hypotheses are added, a Riemann-type functional equation can become highly rigid. This is exactly the kind of extra source structure absent from `(5)`.

Takashi Nakamura, **“Dirichlet series with periodic coefficients, Riemann's functional equation and real zeros of Dirichlet L-functions,”** arXiv:`2008.02570` (2020), gives a neighboring warning in the other direction: certain Dirichlet series with periodic coefficients satisfy Riemann's functional equation, and for non-real primitive characters his examples have infinitely many zeros off the critical line. Thus even adding some Dirichlet-series structure without the full zeta arithmetic constraints need not make the functional equation a zero-location theorem.

The durable Arithmetic Fidelity contribution is therefore not a new converse theorem or a new entire-function construction. It is the exact coupling of AF-261's full profinite-cancellation realization spectrum with AF-256's zero-coordinate pullback, inside a control that preserves the standard completed-function symmetry/growth layer. That coupling identifies a precise information boundary for the current source problem.

## Boundaries

**The control is not an L-function.** `F_rho` is generally not the completion of a Dirichlet series with the Riemann coefficients, Euler product, or arithmetic local factors. The theorem is specifically a no-go for the coarser entire-function layer, not for the stronger arithmetic category that may ultimately provide the needed phase restriction.

**AF-018 is not contradicted.** AF-018 fixes the complete zero divisor first and then classifies the zero-free fiber inside the order-one reflection category. Here the divisor itself is changed by one finite symmetric quartet. The two results together say: the divisor is enough to reconstruct a function inside that category, but the category does not determine the divisor.

**Only a one-pair obstruction is asserted.** Equation `(9)` concerns the AF-261/AF-258 rate attached to the inserted right-half-strip conjugate pair. It does not claim that the full Li sequence of `F_rho` has a particular asymptotic after cancellations with every other zero.

**Leading zero density is coarse.** Adding finitely many zeros preserves the Riemann--von Mangoldt leading term by construction. This does not preserve finer zero statistics, exact counting constants at finite height, Euler-product identities, or explicit-formula coefficients.

**Endpoint values are preserved, not all local jets.** Normalization by `P_rho(0)` fixes `F_rho(0)=xi(0)` and, by reflection, the value at `1`. Derivatives at the endpoints generally change. Stronger local normalization data could therefore contain information not tested by this control.

**No claim about actual zeta zeros.** The inserted `rho` is a matched analytic control, not a claimed Riemann zero. The conclusion is that the listed coarse analytic properties cannot by themselves distinguish actual zeta zero phases from dangerous matched phases.

## Research consequence

After AF-261 and AF-262, the remaining source problem can now be sharpened one step further. A proof of

\[
K_{\mathrm{pc}}(\alpha_\rho)<\log q_\rho
\tag{23}
\]

for every hypothetical off-critical Riemann zero cannot come merely from the completed function being entire of order one, reflection-symmetric, real under conjugation, normalized at the endpoints, confined to the critical strip, or having the usual leading zero density. All of those properties survive a control with arbitrary prescribed positive profinite cancellation.

The next useful source theorem must consume additional zeta-specific information. Natural audit targets are exact Dirichlet-series/Euler-product constraints, explicit-formula coefficient structure, or another independently justified arithmetic condition strong enough to rule out exponentially accurate approach of the actual zero coordinates to the AF-256 resonance mesh. The decisive standard for such a condition is now concrete: it must fail on the controls `(5)` while holding for zeta, and it must quantitatively imply `(23)` rather than merely restating functional-equation symmetry.