# ANF-010 — out-of-band form-factor positivity has a scalar-Gram sign obstruction

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + CLASSICAL-IDENTITY + NEGATIVE/STRUCTURAL-BOUNDARY`. The unconditional BGSST form factor already has the sign needed to discard a Cohn--Elkies negative Fourier tail outside the Montgomery band. The missing ingredient in transplanting that idea to an unconditional simple-critical-zero argument is therefore not an out-of-band pair-correlation estimate. It is a zero-side counting inequality that remains valid for complex zero configurations. Moreover, a single scalar translation-invariant positive-semidefinite Gram kernel cannot supply such a transplant: Bochner positivity forces its BGSST frequency profile to be nonnegative, whereas the Cohn--Elkies tail mechanism requires that profile to be nonpositive outside the known band. Their intersection is bandlimited support-one data.

## 1. BGSST already controls the sign outside the known asymptotic band

Let

\[
A_T:=\frac{T}{2\pi}\log T
\]

and use the normalization of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSST)

\[
\mathcal F_T(\alpha)
:=A_T^{-1}
\sum_{\substack{\rho,\rho'\\0<\gamma,\gamma'\le T}}
T^{\alpha(\rho-\rho')}
\,w(\rho-\rho'),
\qquad
w(u)=\frac4{4-u^2}.
\tag{1}
\]

Their unconditional Theorem 1 proves two logically different facts:

\[
\boxed{\mathcal F_T(\alpha)\ge0\quad\text{for every real }\alpha,}
\tag{2}
\]

and, uniformly for `0 <= alpha <= 1`,

\[
\mathcal F_T(\alpha)
=T^{-2\alpha}(\log T+O(1))
+\alpha+O((\log T)^{-1/2}).
\tag{3}
\]

The all-`alpha` positivity is not conditional on RH. BGSST prove it from an exact integral-of-a-square representation of the complex-zero form factor. Thus the region `|alpha|>1` is not devoid of unconditional information: its magnitude is not asymptotically known, but its sign is.

For a sufficiently regular real-even profile `g`, BGSST equation (3.2) gives the exact Fourier bridge

\[
\begin{aligned}
P_T(g)
&:=\sum_{\substack{\rho,\rho'\\0<\gamma,\gamma'\le T}}
\widehat g\!\left(
 i(\rho-\rho')\frac{\log T}{2\pi}
\right)
 w(\rho-\rho')\\
&=A_T\int_{\mathbb R}\mathcal F_T(\alpha)g(\alpha)\,d\alpha.
\end{aligned}
\tag{4}
\]

This identity itself also uses the full complex zeros, not RH ordinates.

## 2. The Cohn--Elkies tail-drop is therefore unconditional on the analytic side

Assume now that `g` is fixed, integrable and regular enough for (4), continuous at zero, and satisfies

\[
g(\alpha)\le0
\qquad(|\alpha|\ge1).
\tag{5}
\]

By (2), the unknown tail has the favorable sign:

\[
\int_{|\alpha|>1}\mathcal F_T(\alpha)g(\alpha)\,d\alpha\le0.
\tag{6}
\]

Hence

\[
A_T^{-1}P_T(g)
\le
\int_{-1}^{1}\mathcal F_T(\alpha)g(\alpha)\,d\alpha.
\tag{7}
\]

Using (3), evenness and the standard approximate-identity limit

\[
\int_{-1}^{1}
T^{-2|\alpha|}\log T\,g(\alpha)\,d\alpha
\longrightarrow g(0),
\tag{8}
\]

gives

\[
\boxed{
\limsup_{T\to\infty}A_T^{-1}P_T(g)
\le
g(0)+\int_{-1}^{1}|\alpha|g(\alpha)\,d\alpha.
}
\tag{9}
\]

Equation (9) is precisely the analytic shape exploited by the Cohn--Elkies enlargement in Chirre--Gonçalves--de Laat (CGdL): outside the region where the pair-correlation asymptotic is known, one asks only for the test profile to have the sign that lets the unknown contribution be discarded. The important correction to the frontier is that, after BGSST, **this tail-dropping step does not itself require RH**.

No numerical gain is asserted here. Equation (9) says only that the prime/pair-correlation side can legally evaluate the relevant upper-bound functional for such a signed tail.

## 3. Where RH enters the classical Cohn--Elkies simple-zero deduction

CGdL impose the dual sign pattern

\[
g(\alpha)\le0\quad(|\alpha|\ge1),
\qquad
\widehat g(x)\ge0\quad(x\in\mathbb R),
\tag{10}
\]

and optimize this larger Cohn--Elkies class by semidefinite programming. Under RH, every normalized zero difference in (4) is real:

\[
i(\rho-\rho')\frac{\log T}{2\pi}
=-\frac{(\gamma-\gamma')\log T}{2\pi}\in\mathbb R.
\tag{11}
\]

Moreover `w(\rho-\rho')=4/(4+(\gamma-\gamma')^2)>0`. The second inequality in (10) then makes every zero-side summand nonnegative, so the full pair sum dominates its equal-ordinate blocks and hence the multiplicity quantity used to bound `N^*(T)`. This is the zero-side step that yields CGdL's RH-conditional `1.3208` multiplicity constant and the corresponding `0.6792` simple-zero proportion.

Without RH, the argument of `widehat g` in (4) is generally complex and `w(\rho-\rho')` is not a positive real scalar term by term. Pointwise nonnegativity of `widehat g` on the real axis says nothing sufficient about these complex evaluations. Therefore (9) remains a legal unconditional **upper bound on the BGSST pair functional**, but the classical Cohn--Elkies **lower bound of that functional by a zero-counting quantity** no longer follows.

This localizes the missing theorem:

\[
\boxed{
\text{out-of-band analytic sign: available unconditionally}
\quad\text{but}\quad
\text{complex-zero counting certificate: missing.}
}
\tag{12}
\]

## 4. A scalar Gram kernel has exactly the wrong spectral sign

Lamzouri's `ANF-002` mechanism solves the complex-zero counting problem by replacing termwise positivity with a global Hilbert-space inequality. But the price of a scalar Hilbert/Gram construction is a different positivity constraint.

Let `G(x-y)` be a continuous scalar translation-invariant positive-semidefinite kernel on the real line. By Bochner's theorem it is the Fourier transform of a nonnegative measure `mu`. In the BGSST-compatible absolutely continuous case,

\[
G(x)=\widehat g(x)
\qquad\Longrightarrow\qquad
g(\alpha)\ge0\quad\text{a.e.}
\tag{13}
\]

If the same profile is also required to have the favorable Cohn--Elkies tail sign (5), then necessarily

\[
\boxed{g(\alpha)=0\quad\text{for a.e. }|\alpha|>1.}
\tag{14}
\]

Thus a **single scalar translation-invariant PSD Gram kernel cannot simultaneously** provide Hilbert-space counting positivity and exploit BGSST's out-of-band positivity through a negative tail. The common part of the two admissible classes is simply the bandlimited class.

For Lamzouri's actual tensor-square statistic this can be seen without invoking the general theorem. If

\[
K(z)=\widehat q(z),
\qquad q\ge0,
\]

then the pair kernel is `K(z)^2` and its BGSST frequency profile is

\[
g=q*q\ge0.
\tag{15}
\]

Allowing `q` wider support merely creates a **positive** out-of-band tail in `g`. Since `mathcal F_T>=0` there, that unknown contribution goes in the wrong direction for an unconditional upper bound. Restricting it away returns to support one and hence to the Montgomery--Taylor class already exhausted in `ANF-002`/`ANF-003`.

This is a sign incompatibility, not a numerical optimization failure.

## 5. Relation to the current obstruction chain

`ANF-002` established that BGSST pair correlation already carries horizontal information when conjugation symmetry is consumed globally rather than by termwise strip positivity. `ANF-003` then showed that common-translation vector features collapse to one scalar spectral density, and `ANF-004` showed that finite convex global pair-moment lifts have scalar affine dual witnesses. `ANF-005` isolated the remaining signed **support-one** affine problem.

The present result identifies a separate escape route and its exact first obstruction. Extending beyond support one does not require a new theorem giving the value of the form factor for `|alpha|>1`; BGSST positivity is already enough for a Cohn--Elkies negative tail. What fails is the attempt to combine that tail with the same scalar Gram positivity that makes Lamzouri's complex-configuration counting work.

Accordingly, a genuine out-of-band improvement must break at least one part of the scalar-Gram template. Examples of logically surviving architectures include an indefinite or difference-of-PSD certificate whose **total** complex-configuration inequality remains controlled, a genuinely matrix-valued/inertia argument that preserves a useful signature before scalarization, or another global conjugation-invariant counting theorem valid for a real-axis-nonnegative pair kernel whose spectral profile is signed. Merely widening a positive scalar Gram feature cannot work from BGSST Theorem 1 alone.

## 6. Prior art and novelty boundary

All ingredients are established prior art. BGSST Theorem 1 gives (2)--(3), their equation (3.2) gives (4), and CGdL introduced the Cohn--Elkies/semidefinite sign class and its RH-conditional improvement. Bochner's theorem supplies (13). Lamzouri's Hilbert construction supplies the scalar Gram counting mechanism whose spectral sign is being compared here.

Contemporary exploratory research artifacts outside Mathia have also noticed that unconditional form-factor positivity beyond the band is potentially useful and that known PSD/inertia-style certificates do not automatically spend it. Those artifacts are explicitly exploratory and are not used as evidence here. No publication-level novelty claim is made for the observation that the Cohn--Elkies sign pattern conflicts with scalar positive-definiteness.

The durable Mathia contribution is the **exact information-boundary classification**: the out-of-band datum is already available unconditionally, the classical RH dependence sits on the zero-counting side, and the intersection of scalar Gram positivity with the favorable tail-sign class collapses exactly to bandlimited support-one data.

## 7. Falsification boundary and next theorem

The analytic part would fail if BGSST positivity held only on `[-1,1]` or required RH. Their Theorem 1 explicitly states real, even and nonnegative for all real `alpha`, while restricting only the asymptotic formula to `0<=alpha<=1`; their integral-of-a-square identity gives the positivity mechanism directly.

The scalar-Gram obstruction would fail if a continuous scalar translation-invariant PSD kernel with an absolutely continuous BGSST profile could have negative spectral density on a set of positive measure. That would contradict Bochner's theorem. It does **not** rule out non-PSD signed kernels whose counting validity comes from a larger global or matrix inequality.

The sharp next target is therefore no longer "obtain some unconditional information for `|alpha|>1`". It is:

\[
\boxed{
\text{construct, or rule out, a conjugation-invariant complex-zero counting certificate}
\text{ that tolerates a Cohn--Elkies signed spectral tail.}
}
\tag{16}
\]

A successful certificate, combined with (9), would turn already-known unconditional analytic information into a larger zero-location bound. A no-go theorem showing that every relevant global counting certificate necessarily induces a PSD scalar spectral measure would instead prove that genuinely matrix-valued, higher-order, or otherwise non-Gram information is required.