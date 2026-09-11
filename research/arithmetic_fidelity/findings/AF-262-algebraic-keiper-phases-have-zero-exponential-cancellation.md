# AF-262 — Algebraic Keiper phases have zero exponential cancellation

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `DIOPHANTINE-FIDELITY`, `LI-DOMINANT-MODE-CONTROL`, `SOURCE-SPECIFIC-POSITIVE`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-261 shows that periodic completeness alone cannot suppress the worst half-integer cancellation exponent: arbitrary irrational phases can be engineered so that every congruence cylinder carries any prescribed common exponential cancellation level. The algebraic unit-circle regime is qualitatively different.

Let

\[
\alpha\in\mathbb R,
\qquad
u=e^{2\pi i\alpha},
\qquad |
u|=1,
\tag{1}
\]

and define

\[
d_\alpha(n)=\operatorname{dist}\!\left(n\alpha,\mathbb Z+\frac12\right),
\qquad
\kappa_{1/2}(\alpha)
=
\limsup_{n\to\infty}
\frac{-\log d_\alpha(n)}{n}.
\tag{2}
\]

Assume that `nu` is algebraic.

If `nu` is not a root of unity, then

\[
\boxed{\kappa_{1/2}(\alpha)=0.}
\tag{3}
\]

More precisely, there exist constants `C>0` and `tau<infinity`, depending only on `nu`, such that

\[
\boxed{
d_\alpha(n)\ge C n^{1-\tau}
\qquad(n\ge1).}
\tag{4}
\]

Hence no unbounded retained index set can produce positive exponential half-integer cancellation.

If `nu` is a root of unity, then `alpha` is rational modulo one. In this torsion case the unrestricted exponent in `(2)` can be infinite because exact half-integer hits may recur, but the periodically-complete obstruction of AF-258 still vanishes:

\[
\boxed{K_{\mathrm{pc}}(\alpha)=0.}
\tag{5}
\]

Consequently every algebraic unit phase satisfies `(5)`, and every algebraic non-torsion unit phase satisfies the stronger `(3)`.

For a hypothetical off-critical Keiper zero from AF-255,

\[
a_\rho
=1-\frac1\rho
=r_\rho e^{i\theta_\rho},
\qquad
\alpha_\rho=\frac{\theta_\rho}{\pi},
\tag{6}
\]

define its doubled phase

\[
\nu_\rho
:=e^{2i\theta_\rho}
=\frac{a_\rho}{\overline{a_\rho}}
=\frac{(\rho-1)\overline\rho}
{\rho(\overline\rho-1)}.
\tag{7}
\]

If `nu_rho` is algebraic, then

\[
\boxed{K_{\mathrm{pc}}(\alpha_\rho)=0.}
\tag{8}
\]

If it is algebraic and not a root of unity, then also

\[
\boxed{\kappa_{1/2}(\alpha_\rho)=0.}
\tag{9}
\]

In particular, if the zero coordinate `rho` itself is algebraic, then `nu_rho` is algebraic and `(8)` follows. Thus the AF-261 engineered controls with positive profinite cancellation exponent cannot occur inside the algebraic Keiper-phase class.

## Why it matters

AF-258--AF-261 progressively isolate the source-side obstruction left after imposing periodically complete output sampling. The exact obstruction is not ordinary recurrence, modular coverage, or even the ambient irrationality base: it is the possibility that exponentially strong half-integer approximations remain present throughout every finite congruence cylinder. AF-261 proves that continued-fraction dynamics alone do not prevent this.

Equation `(8)` supplies a genuine source restriction. Algebraicity of the doubled Keiper phase collapses the entire profinite obstruction to zero. In the non-torsion case the conclusion is stronger than periodic-complete fidelity: polynomial Diophantine separation prevents positive exponential cancellation on **any** unbounded subsequence.

This does not solve the actual zeta source problem, because no algebraicity theorem for nontrivial Riemann zeros or their Keiper phases is being assumed. Its value is a sharp boundary on what a dangerous phase must look like. Any hypothetical off-critical zero capable of producing `K_pc(alpha_rho)>0` must have a doubled Keiper phase outside the algebraic unit-circle class. The source theorem sought after AF-261 therefore concerns genuinely transcendental phase arithmetic rather than merely exceptionally large continued-fraction coefficients in an unrestricted class.

## Exact derivation

### 1. Algebraic non-torsion unit phases have Diophantine arguments

Ferreira and Ribas prove that if `nu` is algebraic, `|nu|=1`, and `nu` is not a root of unity, then

\[
\frac{\operatorname{Arg}(\nu)}{2\pi}
\tag{10}
\]

is Diophantine: there exist `c>0` and finite `tau` such that

\[
\left|
\frac{\operatorname{Arg}(\nu)}{2\pi}
-\frac pq
\right|
\ge \frac{c}{q^\tau}
\qquad(p\in\mathbb Z,\ q\ge1).
\tag{11}
\]

Because `(1)` implies

\[
\alpha
\equiv
\frac{\operatorname{Arg}(\nu)}{2\pi}
\pmod{\mathbb Z},
\tag{12}
\]

and Diophantine approximation is unchanged by an integer translate, the same estimate holds for `alpha`, after changing only notation for the numerator.

For each `n`, choose an odd integer `p_n` realizing the nearest half-integer in `(2)`. Then

\[
d_\alpha(n)
=
\left|n\alpha-\frac{p_n}{2}\right|
=n\left|\alpha-\frac{p_n}{2n}\right|.
\tag{13}
\]

Applying `(11)` with denominator `2n` gives

\[
d_\alpha(n)
\ge
n\frac{c}{(2n)^\tau}
=
\frac{c}{2^\tau}n^{1-\tau},
\tag{14}
\]

which is `(4)`. Therefore

\[
0
\le
\frac{-\log d_\alpha(n)}{n}
\le
\frac{(\tau-1)\log n+O(1)}{n}
\longrightarrow0,
\tag{15}
\]

proving `(3)`.

AF-257 then implies that every unbounded retained set has zero cancellation exponent for the associated two-mode signal. For a Keiper pair, multiplication by the radial factor `q_rho^n` therefore preserves the full pair root rate `q_rho`, not merely a superunit margin.

### 2. Torsion phases have a safe congruence cylinder

If `nu` is a root of unity, `(1)` implies

\[
\alpha\equiv\frac ab\pmod{\mathbb Z}
\tag{16}
\]

for integers `a,b` with `b>=1`. On the cylinder

\[
n\equiv0\pmod b,
\tag{17}
\]

one has `n alpha in Z`, hence

\[
d_\alpha(n)=\frac12.
\tag{18}
\]

Thus

\[
K_{b,0}(\alpha)
=
\limsup_{\substack{n\to\infty\\b\mid n}}
\frac{\log2}{n}
=0.
\tag{19}
\]

AF-258 defines `K_pc` as the infimum over congruence-cylinder exponents, so `(19)` proves `(5)`. This argument deliberately does not claim `(3)` in the torsion case: another residue class may contain exact half-integer hits, giving `d_alpha(n)=0` infinitely often.

### 3. Algebraic zero coordinates give algebraic doubled Keiper phases

Equation `(7)` follows directly from

\[
a_\rho=\frac{\rho-1}{\rho}
\tag{20}
\]

and `a_rho/overline{a_rho}=e^{2i theta_rho}`. If `rho` is algebraic, then `overline{rho}` is algebraic and the right side of `(7)` is obtained from algebraic numbers by field operations. Hence `nu_rho` is algebraic.

Combining this with the two cases above proves `(8)`. When `nu_rho` is non-torsion, `(9)` follows as well.

## Prior-art audit

The Diophantine core of this result is established prior art rather than a new Arithmetic Fidelity theorem. Geraldo César Gonçalves Ferreira and Sávio Ribas, **“Arithmetic properties of arguments of algebraic numbers on the unit circle,”** arXiv:`2602.23597` (2026), prove directly using lower bounds for linear forms in logarithms that the normalized argument of an algebraic unit-circle number which is not a root of unity is Diophantine. Their theorem is exactly the source needed in `(11)`.

Tomohiro Yamada, **“A note on Laurent’s paper on linear forms in two logarithms: the argument of an algebraic power,”** *Acta Arithmetica* 221 (2025), 153–163, DOI `10.4064/aa241112-2-6`, gives explicit lower bounds for the argument of powers of a fixed algebraic unit-circle number which is not a root of unity. This is even closer to the raw quantity `|nu^n+1|` underlying half-integer cancellation. Both results ultimately belong to the Baker/Laurent/Matveev theory of lower bounds for nonzero linear forms in logarithms of algebraic numbers.

No novelty is claimed for those transcendence-theoretic lower bounds, for rational/root-of-unity periodicity, or for the fact that algebraic numbers are closed under conjugation and field operations. The durable Arithmetic Fidelity contribution is the exact translation into the AF-257/AF-258 cancellation invariants and the Keiper source boundary `(8)`--`(9)` after AF-261 has shown that no phase-independent profinite theorem can exist.

## Boundaries

**No algebraicity claim for zeta zeros.** Nothing here proves or assumes that a nontrivial Riemann zero, `nu_rho`, or its phase is algebraic. The theorem is conditional on algebraicity of the doubled phase and therefore excludes one large structured source class rather than settling the actual zero-derived phase.

**Transcendental phases remain unrestricted.** Ferreira--Ribas and the logarithmic-form machinery do not control the engineered transcendental phases of AF-261. A transcendental `nu_rho` may be Diophantine or Liouville-like; algebraic-versus-transcendental is only a sufficient source distinction, not a classification of `K_pc`.

**Torsion and non-torsion conclusions differ.** Root-of-unity phases give `K_pc=0` because one congruence cylinder is perfectly safe, but may have exact cancellation on another cylinder. Non-torsion algebraic phases give the much stronger ambient exponent `kappa_{1/2}=0`.

**Two-mode pair statement.** The conclusion concerns the cancellation of one conjugate Keiper pair. Several co-dominant modes can cancel through a higher-dimensional trigonometric fiber and are governed by AF-246/AF-253 rather than by one scalar Diophantine phase.

## Research consequence

AF-261 shows that every nonnegative profinite cancellation level can be realized by an engineered irrational phase. AF-262 now proves that **none of the positive levels can be realized when the doubled phase is algebraic**. The remaining RH-facing source problem is therefore narrower: determine whether actual zero-derived phases satisfy a Diophantine property strong enough to force `K_pc=0` or at least `K_pc<log q_rho`, without assuming algebraicity.

A useful next target is any arithmetic or analytic constraint on

\[
\nu_\rho
=\frac{(\rho-1)\overline\rho}{\rho(\overline\rho-1)}
\tag{21}
\]

that rules out exponential rational approximation of its argument. The required conclusion is weaker than algebraicity; finite irrationality exponent, or any polynomial lower bound for half-integer approximation, already forces the full cancellation exponent to vanish.