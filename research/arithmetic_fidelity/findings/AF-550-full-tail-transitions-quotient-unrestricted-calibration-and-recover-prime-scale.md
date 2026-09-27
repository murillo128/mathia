# AF-550 — Full tail transitions quotient unrestricted calibration and recover prime scale

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · NONLOCAL-LIFT · COMPLETE-INVARIANT · DIRICHLET-TAIL · CONDITIONING · NO-NOVELTY-CLAIM

## Claim

AF-548 and AF-549 show that unrestricted orientation-preserving output recalibration destroys every nonconstant invariant carried by finitely many separated finite jets, while exact coincident jets have only zero robust margin. The full-profile boundary left open by AF-549 is genuinely different.

Let I and J be intervals and let

\[
f_i:I\to J,\qquad i\in\mathcal I,
\]

be labelled \(C^1\) diffeomorphisms onto the same range. A common orientation-preserving output recalibration acts by

\[
f_i\longmapsto \phi\circ f_i
\]

with \(\phi:J\to K\) an orientation-preserving diffeomorphism. Fix a reference branch \(f_1\) and define the relative transition profiles

\[
\boxed{H_i=f_1^{-1}\circ f_i.}
\tag{1}
\]

Then every \(H_i\) is exactly invariant under the common recalibration. Moreover, the family \((H_i)_{i\ne1}\), together with the orientation sign of \(f_1\), is a complete invariant of the common-postcomposition orbit: two labelled profile families have the same transition profiles and the same reference orientation if and only if one is obtained from the other by one common orientation-preserving target diffeomorphism.

This is the nonlocal escape that finite separated jets cannot see. It uses cross-evaluation of an entire reference profile, not finitely many target jets at independently programmable output values.

For an arithmetic stress test, let

\[
0<\lambda_1<\lambda_2<\cdots,\qquad
T_n(s)=\sum_{k\ge n}e^{-\lambda_k s},
\tag{2}
\]

on a half-line \(s>\sigma_0\), assuming the series converges there and every tail diverges as \(s\downarrow\sigma_0\). Then each \(T_n\) is a decreasing diffeomorphism from \((\sigma_0,\infty)\) onto \((0,\infty)\), so

\[
H_n=T_1^{-1}\circ T_n
\tag{3}
\]

is an exact invariant under an arbitrary common monotone recalibration of the observed tail values.

Write

\[
d_n=\lambda_{n+1}-\lambda_n,\qquad
\alpha_n=\frac{\lambda_n}{\lambda_1}.
\]

For each fixed \(n\),

\[
\boxed{
H_n(s)
=
\alpha_n s
+
\frac1{\lambda_1}
\left(
e^{-\alpha_n d_1 s}
-
e^{-d_n s}
\right)
+
o\!\left(e^{-\beta_n s}\right),
}
\tag{4}
\]

where

\[
\beta_n=\min\{\alpha_n d_1,d_n\}.
\tag{5}
\]

Hence

\[
\alpha_n=\lim_{s\to\infty}\frac{H_n(s)}s.
\tag{6}
\]

If the first correction is nonresonant,

\[
\alpha_n(\alpha_2-1)\ne \alpha_{n+1}-\alpha_n,
\tag{7}
\]

then its decay rate is also observable from the invariant profile:

\[
\boxed{
\beta_n
=
-\lim_{s\to\infty}
\frac1s
\log|H_n(s)-\alpha_n s|.
}
\tag{8}
\]

Since

\[
\beta_n
=
\lambda_1
\min\{
\alpha_n(\alpha_2-1),
\alpha_{n+1}-\alpha_n
\},
\]

one nonresonant transition recovers the absolute logarithmic scale:

\[
\boxed{
\lambda_1
=
\frac{\beta_n}{
\min\{
\alpha_n(\alpha_2-1),
\alpha_{n+1}-\alpha_n
\}
}.
}
\tag{9}
\]

All generators then follow from \(\lambda_k=\alpha_k\lambda_1\).

For the rational primes, \(\lambda_k=\log p_k\), the \(n=2\) transition is nonresonant and in fact

\[
\boxed{
H_2(s)
=
\frac{\log 3}{\log 2}s
-
\frac1{\log 2}\left(\frac35\right)^s
+
o\!\left(\left(\frac35\right)^s\right).
}
\tag{10}
\]

Therefore the full invariant transition family recovers the entire marked rational-prime sequence without supplying \(p_1=2\) as an external anchor. The slopes recover all ratios \(\log p_n/\log2\), while the exponentially small curvature of \(H_2\) away from its affine asymptote recovers \(\log2\) itself.

This exact recovery is sharply weaker in a stability sense. The scale \(\lambda_1\) lives in an exponentially small residual. Any generic transition error that decays more slowly than \(e^{-\beta_n s}\) can dominate the quantity used in (8), even though it may be negligible relative to the \(O(s)\) leading profile. Thus the full-profile quotient is exactly faithful under arbitrary common recalibration, but absolute-scale recovery is not uniformly stable under coarse finite-resolution observation.

## Complete invariant under common output recalibration

Suppose \(g_i:I\to K\) is another labelled family of diffeomorphisms with the same relative transitions,

\[
g_1^{-1}\circ g_i=f_1^{-1}\circ f_i
\qquad\text{for every }i,
\tag{11}
\]

and with \(g_1\) having the same orientation as \(f_1\). Define

\[
\phi=g_1\circ f_1^{-1}.
\tag{12}
\]

The orientation hypothesis makes \(\phi\) orientation preserving. From (11),

\[
g_i
=
g_1\circ(f_1^{-1}\circ f_i)
=
\phi\circ f_i.
\tag{13}
\]

Conversely, common postcomposition cancels identically:

\[
(\phi\circ f_1)^{-1}\circ(\phi\circ f_i)
=
f_1^{-1}\circ f_i.
\tag{14}
\]

So the transition family is not merely invariant: it parameterizes the quotient by unrestricted common target recalibration.

This is exactly the information unavailable to AF-548's separated finite jets. Computing \(f_1^{-1}(f_i(s))\) requires the reference branch at the output value attained by another branch. No fixed collection of local jets at separated base values contains that cross-value relation.

## Dirichlet-tail asymptotics

For fixed \(n\), absolute convergence at one point to the right of \(\sigma_0\) gives, by dominated convergence,

\[
T_n(s)
=
e^{-\lambda_n s}
\left[
1+e^{-d_n s}
+o(e^{-d_n s})
\right].
\tag{15}
\]

Indeed, after dividing by the second term, the contribution from \(k\ge n+2\) is

\[
\sum_{k\ge n+2}
e^{-(\lambda_k-\lambda_{n+1})s}
\longrightarrow0.
\]

Therefore

\[
\log T_n(s)
=
-\lambda_n s
+
e^{-d_n s}
+
o(e^{-d_n s}).
\tag{16}
\]

Let

\[
H_n(s)=\alpha_n s+\delta_n(s).
\]

The identity \(T_1(H_n(s))=T_n(s)\), together with (16), first gives \(\delta_n(s)=o(s)\), and then in fact \(\delta_n(s)\to0\). Substituting again yields

\[
-\lambda_1\delta_n(s)
+
e^{-d_1H_n(s)}(1+o(1))
=
e^{-d_ns}(1+o(1)).
\]

Because \(\delta_n(s)\to0\),

\[
e^{-d_1H_n(s)}
=
e^{-\alpha_nd_1s}(1+o(1)),
\]

and (4) follows.

When the two exponents differ, the slower-decaying term in (4) has nonzero coefficient \(\pm1/\lambda_1\), proving (8) and (9). At resonance the two first corrections cancel and a deeper expansion is required; no absolute-scale conclusion is inferred from (4) in that case.

## Rational-prime specialization

Take

\[
\lambda_1=\log2,\qquad
\lambda_2=\log3,\qquad
\lambda_3=\log5.
\]

The resonance condition at \(n=2\) would be

\[
\alpha_3=\alpha_2^2,
\qquad\text{equivalently}\qquad
(\log3)^2=(\log2)(\log5).
\tag{17}
\]

It is decisively false. For example, the elementary bounds

\[
0.69<\log2<0.70,\quad
1.09<\log3<1.10,\quad
1.60<\log5<1.61
\]

give

\[
(\log2)(\log5)<1.127<1.1881<(\log3)^2.
\tag{18}
\]

Thus

\[
d_2=\log(5/3)
<
\alpha_2d_1,
\]

so (4) reduces to (10).

Define from the invariant transition data

\[
\widehat\alpha_n
=
\lim_{s\to\infty}\frac{H_n(s)}s
\]

and

\[
\widehat\beta_2
=
-\lim_{s\to\infty}
\frac1s
\log(\widehat\alpha_2s-H_2(s)).
\]

Then

\[
\widehat\alpha_n=\frac{\log p_n}{\log2},
\qquad
\widehat\beta_2=\log(5/3),
\]

and

\[
\boxed{
\log2
=
\frac{\widehat\beta_2}{
\widehat\alpha_3-\widehat\alpha_2
},
\qquad
p_n
=
\exp\!\left(
\widehat\alpha_n
\frac{\widehat\beta_2}{
\widehat\alpha_3-\widehat\alpha_2
}
\right).
}
\tag{19}
\]

No prime-number theorem, zero information, or RH input enters this reconstruction. The source data are the complete ordered tail profiles themselves.

## Matched power-rescaling control

The slopes alone are not enough. Replace the generators by

\[
q_n=p_n^c,\qquad c>0.
\]

The corresponding tails satisfy

\[
T_n^{(c)}(s)=T_n(cs),
\]

so

\[
H_n^{(c)}(s)
=
\frac1cH_n(cs).
\tag{20}
\]

Consequently,

\[
\lim_{s\to\infty}\frac{H_n^{(c)}(s)}s
=
\frac{\log p_n}{\log2}
\]

for every \(c\). A compression retaining only the asymptotic slopes therefore identifies the entire one-parameter power family.

The full transition profile does not. From (10),

\[
H_2^{(c)}(s)
=
\alpha_2s
-
\frac1{c\log2}
e^{-c\log(5/3)s}
+
o\!\left(e^{-c\log(5/3)s}\right),
\tag{21}
\]

so its residual decay rate is \(c\log(5/3)\). Thus the exact nonlocal profile breaks a matched generalized-prime control that every slope-only summary misses.

This is the concrete arithmetic distinction required by the line mandate: the retained relational object separates the rational-prime scale from a natural non-prime deformation at the same leading information layer.

## Conditioning boundary

Exact invariance to nuisance is not the same as stable recoverability from noisy data.

First, suppose an estimated transition obeys

\[
\widehat H_n(s)=H_n(s)+\varepsilon_n(s).
\]

The slope \(\alpha_n\) survives any error \(\varepsilon_n(s)=o(s)\). By contrast, the decay-rate decoder (8) is generically protected only when the error is small relative to the exponentially small residual. A sufficient condition is

\[
\varepsilon_n(s)=o(e^{-\beta_ns}).
\tag{22}
\]

Errors that vanish polynomially, or exponentially at a slower rate, can dominate \(H_n(s)-\alpha_ns\) and change the apparent value of \(\beta_n\). Hence the extra information that breaks the power-rescaling control is exact but exponentially ill-conditioned in this asymptotic coordinate.

Second, even forming the transition from raw tails has its own metric cost. From (15),

\[
\frac{T_1'(t)}{T_1(t)}\to-\lambda_1,
\]

so for \(y=T_1(t)\to0\),

\[
\left|(T_1^{-1})'(y)\right|
\sim
\frac1{\lambda_1y}.
\tag{23}
\]

Small additive output error therefore becomes large near the tail unless it is controlled relative to the observed tail magnitude. Under an arbitrary unknown recalibration \(\phi\), no calibration-independent additive output norm can be expected because \(\phi'\) may flatten or magnify that metric arbitrarily.

The correct conclusion is therefore two-level:

- as an exact quotient object, the full transition family is perfectly invariant to unrestricted common output recalibration;
- as a finite-resolution recovery mechanism, its absolute-scale discriminator requires relative tail accuracy and exponentially fine resolution of the transition residual.

This is precisely the distinction between exact sufficiency and stable fidelity emphasized by the line mandate.

## Prior-art / novelty audit

No novelty is claimed for the general group-quotient mechanism.

The relative transition \(f_1^{-1}\circ f_i\) is the elementary complete invariant of a family under common left composition once a reference branch is invertible. AF-548 and AF-549 already place the same cancellation inside classical left-equivalence and differential-invariant mathematics.

A close statistical analogue is the relative-distribution framework of Mark S. Handcock and Martina Morris, “Relative Distribution Methods,” Sociological Methodology 28 (1998), 53–97, DOI 10.1111/0081-1750.00042. Their reference-CDF/quantile compositions encode full distributional comparison rather than low-order summaries; this is neighboring prior art for retaining a complete relational profile instead of separate scalar features.

The prime-zeta function itself and its ordinary Dirichlet representation are classical; Carl-Erik Fröberg, “On the prime zeta function,” BIT 8 (1968), 187–202, is already recorded in the line source ledger. The asymptotic calculation here uses only first-term dominance in positive Dirichlet tails and an elementary inverse expansion. No novelty is claimed for Dirichlet-series uniqueness, inverse-function calculus, Q-Q/relative-distribution constructions, or maximal-invariant language.

A targeted literature search did not locate this exact prime-tail transition formulation or the scale-recovery formula (19), but absence from that search is not a novelty claim. The durable Arithmetic-Fidelity result is the exact placement of a source-natural nonlocal representation on the AF-548/AF-549 boundary, together with its matched power-rescaling control and its exponentially weak stability margin.

## Boundaries and failure modes

- **Full common range is load bearing.** The complete-orbit statement assumes the profiles are invertible onto a common interval. With only partial range overlap, transition invariants are local to the overlap and need not classify the full family.
- **Labelled tails are retained.** The index \(n\) is provenance. Forgetting which tail is which introduces an additional permutation quotient.
- **Monotone common nuisance only.** Separate branch recalibrations destroy (14); the theorem does not cover branch-specific output warps.
- **Exact profiles are infinite-dimensional data.** This is a legitimate nonlocal lift, not a claim of small compression.
- **Nonresonance is load bearing for first-correction scale recovery.** If (7) fails, equation (4) only shows cancellation of the first residual terms; deeper asymptotics must be audited before claiming absolute-scale recovery.
- **Exact recovery is not robust recovery.** The prime scale sits in an exponentially small residual and is invisible to coarse profile accuracy.
- **No RH consequence.** Recovering the rational-prime sequence from a representation that already contains all marked prime tails does not solve or reformulate RH. Its value is as a fidelity boundary and a stress test for downstream compressions.

## Decisive audit tests

1. Verify both directions of the complete-orbit statement by the explicit map \(\phi=g_1\circ f_1^{-1}\).
2. Starting from (15), independently derive (4), including the sign and coefficient of both first correction terms.
3. For \(2,3,5\), verify the strict nonresonance inequality (18) and recover (10).
4. Apply the power deformation \(p_n\mapsto p_n^c\) and verify (20)–(21): slopes must remain unchanged while the residual rate scales by \(c\).
5. Add an observation perturbation larger than \(e^{-\beta_2s}\) and verify that the scale decoder based on (8) can be changed while the leading slope remains intact.

## Consequence for the research line

AF-549's full-profile boundary is now resolved positively at the exact level and negatively at coarse resolution.

The prime-tail family naturally supplies overlapping complete profiles, and their relative transitions exactly quotient arbitrary common monotone output calibration. Unlike every separated finite-jet lift in AF-548/AF-549, this nonlocal representation retains enough relational structure to recover the entire rational-prime sequence and to distinguish common power-rescaled generalized-prime controls.

But the extra information beyond logarithmic prime ratios lives in an exponentially small departure from an affine asymptote. Any downstream representation that retains only coarse slopes, finite jets, polynomial-resolution profile accuracy, or another summary that erases this residual falls back into a non-faithful quotient. The next arithmetic question is therefore not whether full profiles can carry the prime discriminator—they can—but whether a representation relevant to an RH mechanism preserves a normed version of this exponentially weak relational residual with a useful transport modulus.