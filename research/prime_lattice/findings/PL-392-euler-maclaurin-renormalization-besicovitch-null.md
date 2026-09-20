# PL-392 — Euler–Maclaurin gives zero-faithful zeta truncations whose continuation correction is Besicovitch-null

**Evidence:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-391`.

**Related findings:** `PL-361`, `PL-362`, `PL-390`, `PL-391`.

**Status:** `THE-CANONICAL-ONE-TERM-EULER--MACLAURIN-RENORMALIZATION-OF-THE-ZETA-ENERGY-CUTOFF-CONVERGES-LOCALLY-UNIFORMLY-TO-ZETA-THROUGHOUT-Re(s)>0-AWAY-FROM-THE-POLE-AND-THEREFORE-RECOVERS-EVERY-ISOLATED-CRITICAL-STRIP-ZERO-WITH-MULTIPLICITY. YET-ON-EVERY-FIXED-VERTICAL-LINE-0<sigma<1-THE-RENORMALIZING-COUNTERTERM-IS-A-C0-PERTURBATION-WITH-EXACTLY-ZERO-BESICOVITCH-B2-SEMINORM. HENCE-THE-SINGLE-ZERO-FAITHFUL-ANALYTIC-CORRECTION-LIES-IN-THE-KERNEL-OF-THE-NATIVE-VERTICAL-MEAN-SQUARE-QUOTIENT. LINEAR-OR-QUADRATIC-BOHR/BESICOVITCH-BULK-GEOMETRY-CANNOT-RECOVER-THIS-CORRECTION; A-SURVIVING-ROUTE-MUST-RETAIN-THE-DISTINGUISHED-ANALYTIC-REPRESENTATIVE-OR-USE-NONLINEAR-ZERO-SENSITIVE-DATA`.

## Claim

Let

\[
P_N(s)=\sum_{n\le N}n^{-s}
\tag{PL392-1}
\]

be the canonical exponent-lattice energy cutoff, and define the one-term Euler--Maclaurin renormalization

\[
Q_N(s)
:=P_N(s)+\frac{N^{1-s}}{s-1}.
\tag{PL392-2}
\]

The classical Euler--Maclaurin representation gives, for `Re(s)>0`,

\[
\zeta(s)
=Q_N(s)
-s\int_N^\infty
\frac{x-\lfloor x\rfloor}{x^{s+1}}\,dx.
\tag{PL392-3}
\]

Consequently `Q_N -> zeta` locally uniformly on every compact subset of

\[
\{s:\Re s>0\}\setminus\{1\}.
\tag{PL392-4}
\]

By Hurwitz/Rouche zero stability, every isolated zero of `zeta` in the critical strip is therefore reproduced, with multiplicity, by zeros of `Q_N` in a sufficiently small neighborhood for all sufficiently large `N`.

This supplies exactly the **single-zero-sensitive analytic-continuation bridge** that raw finite Dirichlet polynomials lack in `PL-391`. But it exposes a sharp incompatibility with the native Bohr/Besicovitch vertical geometry of `PL-390`. Fix `0<sigma<1`. On the line `s=sigma+it`,

\[
Q_N(\sigma+it)-P_N(\sigma+it)
=
\frac{N^{1-\sigma}e^{-it\log N}}
{\sigma-1+it}.
\tag{PL392-5}
\]

The right side is a nonzero function in `C_0(R)`, yet its Besicovitch `B^2` seminorm is exactly zero:

\[
\boxed{
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^{T}
\left|
\frac{N^{1-\sigma}e^{-it\log N}}
{\sigma-1+it}
\right|^2dt
=0.
}
\tag{PL392-6}
\]

Hence, for every finite `N` and every `0<sigma<1`,

\[
\boxed{
[Q_N(\sigma+i\cdot)]_{B^2}
=
[P_N(\sigma+i\cdot)]_{B^2}.
}
\tag{PL392-7}
\]

Thus a correction that is **load-bearing for analytic continuation and individual zero convergence is literally invisible in the native vertical mean-square quotient**. This is stronger than saying that `B^2` loses isolated zero values after the fact: even the canonical counterterm that turns the wrong critical-strip approximation into a zero-faithful one lies in the quotient kernel.

## 1. Local-uniform convergence and individual zero fidelity

NIST DLMF §25.2 records the Euler--Maclaurin identity

\[
\zeta(s)
=
\sum_{n=1}^N n^{-s}
+\frac{N^{1-s}}{s-1}
-s\int_N^\infty
\frac{\{x\}}{x^{s+1}}\,dx,
\qquad \Re s>0,
\tag{PL392-8}
\]

where `0<={x}<1`. This is a continuation formula, not a formal continuation of the Euler product.

Let `K` be a compact subset of `Re(s)>0` avoiding `s=1`, and put

\[
\delta=\min_{s\in K}\Re s>0,
\qquad
M=\max_{s\in K}|s|.
\]

Then (PL392-8) gives the uniform estimate

\[
\sup_{s\in K}|\zeta(s)-Q_N(s)|
\le
M\int_N^\infty x^{-\delta-1}\,dx
=
\frac{M}{\delta}N^{-\delta}.
\tag{PL392-9}
\]

So (PL392-4) follows directly, with an explicit compact-set rate.

Now let `rho` be any nontrivial zero of zeta. Choose a small closed disk `D` centered at `rho`, contained in `0<Re(s)<1`, whose boundary contains no zeta zero and whose interior contains no other distinct zero. Uniform convergence on `D` implies, by Hurwitz's theorem equivalently by Rouche on the boundary for large `N`, that `Q_N` and `zeta` have exactly the same number of zeros in `D`, counted with multiplicity. Therefore the renormalized finite objects do not merely reproduce a normalized zero density: they approximate each fixed zero locally.

This answers one precise gap in `PL-391`. The failure of the raw `P_N` to approximate analytic continuation is repairable by an elementary source-defined term. The important question is what representation retains that repair.

## 2. The correction is exactly null in vertical `B^2`

For fixed `0<sigma<1`, set `a=1-sigma>0`. From (PL392-5),

\[
|Q_N(\sigma+it)-P_N(\sigma+it)|^2
=
\frac{N^{2-2\sigma}}{a^2+t^2}.
\tag{PL392-10}
\]

Therefore

\[
\begin{aligned}
\frac1{2T}\int_{-T}^{T}
|Q_N-P_N|^2\,dt
&=
\frac{N^{2-2\sigma}}{2T}
\int_{-T}^{T}\frac{dt}{a^2+t^2}\\
&=
\frac{N^{2-2\sigma}}{aT}
\arctan\!\left(\frac{T}{a}\right)
\longrightarrow0.
\end{aligned}
\tag{PL392-11}
\]

This is exact and requires no limiting relation between `N` and `T`: **for each fixed `N`**, the counterterm represents the zero element of the Besicovitch `B^2` quotient.

At the same time it is not a pointwise-negligible correction in the analytic approximation problem. On bounded height windows its size is generally of order `N^(1-sigma)` divided by a bounded denominator, precisely the scale needed to cancel the divergent main term of `P_N` described in `PL-361` and `PL-362`. The two topologies are asking different questions: local-uniform convergence sees the counterterm strongly, while the long-height mean-square quotient kills it.

This distinction should not be weakened to the statement that the correction merely has small `B^2` norm as `N->infinity`. Its seminorm is **identically zero for every `N`**.

## 3. Bohr part versus archimedean tail

For fixed `N` and `sigma`,

\[
P_N(\sigma+it)
=\sum_{n\le N}n^{-\sigma}e^{-it\log n}
\tag{PL392-12}
\]

is a finite Bohr almost-periodic exponential polynomial, with

\[
\log n=\langle v(n),(\log p)_{p\le N}\rangle.
\tag{PL392-13}
\]

The continuation correction has the same lattice character `e^{-it log N}` in its phase but is multiplied by the non-almost-periodic envelope

\[
\frac{N^{1-\sigma}}{\sigma-1+it},
\tag{PL392-14}
\]

which tends to zero as `|t|->infinity`. Hence

\[
Q_N(\sigma+i\cdot)
\in AP(\mathbb R)+C_0(\mathbb R).
\tag{PL392-15}
\]

This is the standard asymptotically-almost-periodic decomposition. Moreover `AP(R) cap C_0(R)={0}`: if a nonzero Bohr almost-periodic function had a nonzero value at some point, relative density of sufficiently accurate almost-periods would reproduce a comparable value arbitrarily far out, contradicting vanishing at infinity. Thus the decomposition into the finite torus part and the decaying continuation tail is intrinsic within `AP+C_0`.

The geometric interpretation is therefore precise. The exponent lattice supplies the compact recurrent part. The first analytic-continuation correction is an **archimedean boundary tail**, not another constant-amplitude torus character, even though its oscillatory phase uses the boundary frequency `log N`. Quotienting by long-height mean square projects away exactly this tail.

This gives a concrete version of the warning in the canonical research mandate: arithmetic information must survive analytic continuation, not merely exist before it. Here the torus quotient keeps the prime frequencies while deleting a term that is essential to the continued analytic representative.

## 4. Relation to `PL-390` and `PL-391`

`PL-390` proved that for `sigma>1/2` the analytically continued vertical zeta function has a legitimate Besicovitch `B^2` representative with coefficient frequencies `-log n`, but the quotient is blind to isolated pointwise zeros. `PL-391` then showed that finite Bohr/Jessen geometry can be nonlinear enough to recover a zero-density measure and that recent prior art makes this mass concentrate at `1/2`; however, the raw partial sums do not converge to analytic zeta in the strip and normalized density cannot see a sparse exceptional zero.

The present result bridges those two observations. There is a canonical finite approximation that **does** converge to analytic zeta strongly enough to preserve every fixed zero, namely `Q_N`. But its difference from the raw finite Bohr polynomial is a `B^2`-null term. Therefore replacing `P_N` by the zero-faithful `Q_N` does not change any invariant that factors only through the vertical `B^2` class.

In particular, no linear or quadratic invariant of that quotient can distinguish the zero-faithful continuation-corrected truncation from the analytically wrong raw truncation. This includes all constructions depending only on Besicovitch Fourier coefficients, mean-square norms, or the corresponding Hilbert-space vector.

The statement deliberately does **not** include the Jessen functional

\[
\lim_{T\to\infty}\frac1{2T}
\int_{-T}^{T}\log|f(\sigma+it)|\,dt.
\]

The logarithm is nonlinear and singular at zeros. A `C_0` or `B^2`-null perturbation can move zeros and can in principle affect logarithmic/argument data. Thus `PL-392` does not close the Jensen route. It identifies why such a nonlinear distinguished-representative invariant is necessary if one wants to retain both prime-lattice recurrence and the analytic continuation correction.

## 5. Prior-art and novelty audit

No theorem-level novelty is claimed for the ingredients.

1. NIST Digital Library of Mathematical Functions, §25.2(iii), equation 25.2.8, https://dlmf.nist.gov/25.2 : authoritative Euler--Maclaurin continuation formula used in (PL392-8).
2. A. Hurwitz's classical zero-stability theorem under locally uniform convergence; a modern statement is the *Encyclopedia of Mathematics*, “Hurwitz theorem,” https://encyclopediaofmath.org/wiki/Hurwitz_theorem .
3. The decomposition `AAP=AP+C_0` is standard in almost-periodic-function theory; for a modern explicit formulation and uniqueness statement see the background section of *Infinite-dimensional Lure systems with almost periodic forcing*, *Mathematics of Control, Signals, and Systems* (2020), DOI `10.1007/s00498-020-00262-y`, https://doi.org/10.1007/s00498-020-00262-y .
4. The neighboring finite-Bohr/Jessen zero-density result is Eric Dubon, “Zero-Density Concentration for Dirichlet Polynomials,” arXiv:2609.17875 (2026), already audited in `PL-391`.

A targeted literature search on 20 September 2026 combined Euler--Maclaurin/regularized zeta partial sums, Hurwitz zero convergence, Besicovitch almost periodicity, asymptotically almost-periodic decompositions, and zeta zero approximations. It recovered the classical continuation formula, general almost-periodic decomposition theory, and literature on zeros of ordinary or functional-equation-based zeta approximants, but no source was found making the specific route comparison (PL392-7): the canonical one-term zero-faithful Euler--Maclaurin correction is exactly null in the vertical `B^2` quotient. Absence of a located source is not a novelty claim. The durable Mathia contribution is the **representation obstruction** obtained by putting standard facts in the exact topology used by `PL-390`--`PL-391`.

A matched generic control also prevents overclaiming. The mechanism is not prime-specific: whenever a Dirichlet-type cutoff requires a decaying vertical counterterm to remove a summatory main term, long-height mean seminorms may erase that counterterm. Thus (PL392-7) is not RH rigidity and does not itself single out `1/2`; it holds for every fixed `0<sigma<1`.

## 6. Adversarial boundaries

The following limits are load-bearing.

**The result is about the quotient, not the function.** `Q_N-P_N` is a nonzero analytic function. It is zero only as a Besicovitch seminorm class on a fixed vertical line.

**The correction is not Bohr almost periodic.** The factor `(sigma-1+it)^(-1)` decays. Treating (PL392-5) as just one more torus Fourier mode would erase the exact feature responsible for the mismatch.

**Zero fidelity uses local-uniform convergence, not `B^2`.** The Hurwitz/Rouche step is valid on compact subsets of the analytic critical strip. No implication from mean-square convergence to zero convergence is being used.

**No claim is made that Jessen means are unchanged.** The map `f -> log|f|` is not continuous through zeros in the `B^2` quotient. Indeed, its possible sensitivity to this mean-null tail is one of the surviving structures worth testing.

**The half-line is not selected here.** Euler--Maclaurin continuation repairs the whole region `Re(s)>0`; the `B^2` nullity calculation holds throughout `0<sigma<1`. The critical line enters only through additional structures such as the coefficient-energy/Jessen concentration of `PL-391` or genuinely zeta-specific global symmetry.

**Finite `N` precedes the vertical mean.** Equation (PL392-6) is an exact fixed-`N` statement. It does not justify interchanging `N->infinity` with `T->infinity` in a nonlinear zero statistic.

## Consequence for the research line

The combination of `PL-390`--`PL-392` now separates three representation levels that should not be conflated. The finite Bohr torus exactly represents the raw exponent-lattice cutoff. The Euler--Maclaurin tail supplies a canonical analytic renormalization that restores local convergence and individual-zero fidelity. The native Besicovitch quotient then deletes that tail exactly.

Therefore a future harmonic mechanism cannot be judged only by whether it retains the frequencies `log n=<v(n),log p>` or even by whether it has the correct `B^2` vertical representative. It must specify how the **distinguished analytic continuation data outside the recurrent torus component** is retained. Plausible surviving targets are nonlinear Jessen/argument currents applied to `Q_N`, a topology stronger than vertical mean square that still admits the continuation tail, or a target-relative model-space/operator construction where the archimedean correction is not quotiented away.

The immediate next test is correspondingly sharp: if a proposed finite-torus/Jessen invariant is applied to the zero-faithful `Q_N`, determine whether its off-line-zero-sensitive part survives without collapsing, after normalization, to the same coefficient-energy bulk law as `P_N`. A mechanism that cannot distinguish `Q_N` from `P_N` at this stage cannot supply the missing analytic-continuation bridge to RH.