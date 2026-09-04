# WI-156 — finite adaptive scalar portfolios stay at the Montgomery--Taylor barrier

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`.

WI-143 closes fixed positive mixtures and direct sums of separately valid Lamzouri scalar windows, while WI-144 closes two coherent positive-Hilbert multi-window lifts. WI-153 then shows that every individually valid support-one scalar Lamzouri-form census pays at least the sharp Carneiro--Chandee--Littmann--Milinovich/Montgomery--Taylor one-delta cost. Those findings deliberately leave genuinely joint multi-profile arguments open.

There is nevertheless a larger scalar portfolio class that also cannot improve the support-one constant: **post-hoc adaptive selection among finitely many separately valid scalar censuses**. Let `H_1,...,H_J` be normalized scalar kernels, and for every finite conjugation-invariant multiset `Z` write

\[
Q_j(\mathcal Z):=\sum_{z,w\in\mathcal Z}H_j(z-w),
\qquad
L(\mathcal Z):=2|\mathcal Z|-s(\mathcal Z),
\tag{1}
\]

where `s(Z)` is the number of simple real elements. Assume that each channel separately satisfies the universal Lamzouri-form census

\[
\boxed{Q_j(\mathcal Z)\ge L(\mathcal Z)\qquad(1\le j\le J)}.
\tag{2}
\]

Then one may choose the kernel **after seeing the whole configuration**, or choose configuration-dependent convex weights, but the strongest consequence available from the separate inequalities remains

\[
\boxed{
 s(\mathcal Z)
 \ge
 2|\mathcal Z|-\min_{1\le j\le J}Q_j(\mathcal Z).
}
\tag{3}
\]

For a finite portfolio the post-hoc minimum commutes with the asymptotic pair-correlation evaluation. If the actual zeta multisets satisfy, for each fixed channel,

\[
\frac{Q_j(T)}{N(T)}\longrightarrow R_j,
\tag{4}
\]

then

\[
\boxed{
\frac{\min_jQ_j(T)}{N(T)}
\longrightarrow
\min_jR_j.
}
\tag{5}
\]

Consequently, under the support-one regularity/universality hypotheses of WI-153, every `R_j` is at least the sharp one-delta constant

\[
C_{\rm MT}
=
\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2},
\tag{6}
\]

so the **certified constant produced by any finite adaptive portfolio of separately valid scalar censuses** obeys

\[
\boxed{
2-\min_jR_j
\le
H_{\rm MT}
:=
\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}
=0.672500703679\ldots .
}
\tag{7}
\]

This is a method ceiling, not an upper bound for the true proportion of simple critical zeros. It does not touch the established Gram-defect improvements above `H_MT`, because those improvements retain joint matrix/local geometry that is not implied by a collection of independent scalar pair-sum censuses.

The result sharpens the surviving-route language after WI-143--WI-155. A useful multi-profile escape cannot consist merely of many scalar inequalities followed by a clever configuration-dependent choice of the best one. It must establish a **genuinely joint constraint** that is stronger than the coordinatewise facts `Q_j>=L`, or obtain an infinite/growing family together with arithmetic information that is genuinely stronger than pointwise fixed-profile convergence.

## 1. Exact finite adaptive-selection lemma

Equation (2) is equivalent to

\[
L(\mathcal Z)\le Q_j(\mathcal Z)
\qquad\text{for every }j.
\tag{8}
\]

Taking the minimum preserves the inequality:

\[
L(\mathcal Z)
\le
\min_jQ_j(\mathcal Z).
\tag{9}
\]

Since `L=2N-s`, rearranging (9) gives (3). Thus it is completely legitimate to inspect the configuration and choose

\[
j_*(\mathcal Z)\in\operatorname*{argmin}_jQ_j(\mathcal Z)
\tag{10}
\]

post hoc. No measurability, continuity, or predetermined choice rule is needed for a finite multiset and finite portfolio.

More generally, let the weights depend arbitrarily on the configuration,

\[
a_j(\mathcal Z)\ge0,
\qquad
\sum_{j=1}^Ja_j(\mathcal Z)=1.
\tag{11}
\]

Then

\[
\sum_ja_j(\mathcal Z)Q_j(\mathcal Z)
\ge
\min_jQ_j(\mathcal Z)
\ge
L(\mathcal Z).
\tag{12}
\]

Hence adaptive convex mixing is never stronger than best-channel selection, and best-channel selection is already exactly (3). This strictly contains WI-143's fixed convex-mixture statement: the weights in (11) may depend on every feature of `Z` and need not converge as the multiset grows.

There is also an order-theoretic formulation that makes the boundary explicit. The only information supplied by the separate censuses is that the vector

\[
Q(\mathcal Z)=(Q_1(\mathcal Z),\ldots,Q_J(\mathcal Z))
\tag{13}
\]

lies in the orthant

\[
[L(\mathcal Z),\infty)^J.
\tag{14}
\]

Among its coordinates, the minimum is the smallest penalty that is forced by this orthant information. Any proposed scalar penalty `P(Q)` with

\[
P(Q)<\min_jQ_j
\tag{15}
\]

at some feasible vector cannot be justified from (14) alone: the diagonal point `(L,...,L)` is compatible with the coordinatewise constraints. To prove such a stronger `P`, one must add a joint exclusion of part of the orthant. That additional exclusion is exactly the mathematical content a real multi-profile improvement would need to provide.

## 2. Finite minima commute with the pair-correlation limit

Let

\[
q_j(T):=\frac{Q_j(T)}{N(T)}.
\tag{16}
\]

For any two real vectors `x,y in R^J`,

\[
\left|\min_jx_j-\min_jy_j\right|
\le
\max_j|x_j-y_j|.
\tag{17}
\]

Indeed, if `j_x` minimizes `x`, then

\[
\min_jy_j
\le y_{j_x}
\le x_{j_x}+\max_j|x_j-y_j|
=
\min_jx_j+\|x-y\|_\infty,
\]

and exchanging `x,y` gives (17).

When `J` is fixed and finite, the individual convergences (4) imply

\[
\max_{1\le j\le J}|q_j(T)-R_j|\longrightarrow0.
\tag{18}
\]

Applying (17) proves (5). Therefore there is no asymptotic selection bonus hidden in switching kernels with `T`, even if the identity of the minimizing channel oscillates indefinitely:

\[
\lim_{T\to\infty}\min_j q_j(T)
=
\min_j\lim_{T\to\infty}q_j(T).
\tag{19}
\]

This is the exact point at which finiteness matters. A growing or infinite portfolio does not follow from merely pointwise convergence of every fixed channel; uniform control is then an additional arithmetic theorem rather than a formal consequence.

## 3. The support-one one-delta theorem closes every individual channel

The primary modern zero-side input is Proposition 2.1 of Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026). For his concrete square kernel it gives the universal finite census abstracted in (2). The present argument allows different scalar kernels and assumes only that the same census has actually been proved separately for each one.

WI-153 identifies the support-one arithmetic optimization for any such scalar channel. Under its hypotheses, the two-real-point configurations force the real-gap kernel to be nonnegative, normalized, integrable and Fourier-supported in `[-1,1]`. It is therefore an admissible function for the one-delta extremal theorem of Carneiro, Chandee, Littmann and Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182, especially Corollary 14. Their sharp theorem gives the cost (6).

Thus every individually valid support-one channel has

\[
R_j\ge C_{\rm MT}.
\tag{20}
\]

Combining (5) and (20),

\[
\min_jR_j\ge C_{\rm MT},
\tag{21}
\]

and substituting (21) into the adaptive finite census (3) yields the ceiling (7) on the **number certified by this architecture**.

The direction of (7) is important. The method gives a lower bound

\[
\liminf\frac{N_0^s(T)}{N(T)}
\ge
2-\min_jR_j.
\tag{22}
\]

Since `min R_j>=C_MT`, the right side of (22) cannot exceed `H_MT`. Nothing here says that the actual `liminf` is at most `H_MT`; later Gram-defect findings already certify a larger value by using information outside the scalar portfolio abstraction.

## 4. Fixed indefinite matrix contractions do not escape by themselves

WI-154 and WI-155 close natural matrix routes when the real-gap matrix kernel is pointwise PSD or when the finite census itself is asserted in Loewner order. Their scope statements correctly leave sign-indefinite matrix scalarizations open because Loewner positivity need not survive an indefinite contraction.

There is a useful additional distinction. Suppose a matrix-valued observable `R(z)` is contracted by one fixed real linear functional `ell` to

\[
H_\ell(z):=\ell(R(z)),
\tag{23}
\]

and suppose a new argument actually proves the **scalar** universal census

\[
s(\mathcal Z)
\ge
2N-\sum_{z,w\in\mathcal Z}H_\ell(z-w).
\tag{24}
\]

Then the matrix provenance of `H_ell` no longer matters for the one-delta step. Equation (24) is exactly a `J=1` scalar census, so WI-153 applies under support one. The functional `ell` may be indefinite; positivity of `ell`, pointwise PSD of `R`, and a Hilbert representation are unnecessary once (24) itself has been established.

Likewise, a finite collection of fixed contractions `ell_1,...,ell_J`, each separately satisfying (24), is covered by Sections 1--3 even if one chooses the best contraction after seeing `Z`. Therefore **“use an indefinite matrix channel and then adaptively select a favorable fixed scalar contraction” is not by itself an escape**.

What remains outside this conclusion is precisely a matrix/joint theorem whose validity is not decomposable into the scalar censuses (24). A sign-indefinite block-inertia inequality can constrain the whole matrix while none of its scalar contractions separately obeys Lamzouri's census; such an architecture is genuinely different and is not ruled out here.

## 5. Infinite portfolios require uniform arithmetic, not just more kernels

Let `Theta` be any index set of separately valid scalar kernels and write

\[
q_\theta(T)=\frac{Q_\theta(T)}{N(T)}.
\]

If one has the **uniform** arithmetic evaluation

\[
\sup_{\theta\in\Theta}
|q_\theta(T)-R_\theta|
\longrightarrow0,
\tag{25}
\]

then the finite-min argument extends verbatim because

\[
\left|
\inf_\theta q_\theta(T)
-
\inf_\theta R_\theta
\right|
\le
\sup_\theta|q_\theta(T)-R_\theta|.
\tag{26}
\]

If every channel is support-one CCLM-admissible after the universal real two-point test, then every `R_theta>=C_MT`, so even continuum adaptivity with (25) cannot beat `H_MT`.

This identifies a genuine boundary rather than a loophole. For a `T`-dependent or growing family, pointwise pair-correlation convergence for every fixed kernel does **not** imply (25). One could in principle choose a profile whose complexity, regularity norm, support-edge concentration, or other parameter degenerates with `T` fast enough that fixed-test error estimates are nonuniform. But then the claimed improvement rests on proving an explicit uniform zeta pair-correlation theorem for that family, or on exploiting the nonuniform error in a controlled way. Merely increasing the portfolio size does not supply that arithmetic information.

The same warning applies to an infimum over all admissible support-one kernels. CCLM already gives the sharp limiting variational cost, while the unconditional zeta theorem is normally stated for fixed tests. Passing a `T`-dependent near-extremizing or singular family through the explicit formula requires its own uniform error analysis. No such passage is assumed here.

## 6. Stress tests and surviving routes

This finding is intentionally narrower than a no-go for all multi-profile arguments.

First, the coordinatewise hypothesis (2) is load-bearing. A genuine joint theorem may say that a nonlinear function of `(Q_1,...,Q_J)` controls `L` even though no individual `Q_j` does. Such a theorem can exclude the diagonal orthant point used after (14) and is exactly the kind of new incidence/geometric information WI-143 and WI-144 leave open.

Second, the argument concerns scalar pair-sum penalties. The Gram-defect refinements beginning with WI-009 retain local Gram realizability and nonlinear spectral information before scalar collapse, so they are not contradicted by (7). The same is true of a future block-inertia certificate that retains off-line signature information jointly.

Third, the support-one ceiling comes specifically from WI-153/CCLM. Justified wider Fourier support changes the arithmetic extremal problem. The result also does not turn the currently known higher vertical correlations into useful horizontal information; WI-119 separately shows that the standard fixed-order bandlimited complexification is screened below the Rudnick--Sarnak support boundary.

Fourth, Chirre--Gonçalves--de Laat's stronger RH-conditional SDP mechanism is not a counterexample. Its favorable signed Fourier tail lies outside the unconditional universal Lamzouri scalar-census class being assumed here. WI-143 and WI-144 already isolate that distinction.

Finally, configuration-dependent **weights** do not constitute a joint constraint. They only decide how to consume already-established coordinatewise inequalities. A claim that an adaptive portfolio escapes this theorem must exhibit an inequality unavailable from `Q_j>=L` separately, or an arithmetic uniformity theorem strong enough to justify a genuinely `T`-dependent infinite-family passage.

## 7. Prior-art and novelty audit

The sharp scalar one-delta theorem is established prior art: Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182, arXiv:1406.5462, solve the relevant support-one extremal problem and trace its zeta origin to Montgomery--Taylor. Youness Lamzouri, arXiv:2609.02882v1, supplies the current universal finite scalar census for his concrete Hilbert kernel and explicitly identifies the same one-delta optimum in his support-one application.

WI-143 is the direct Mathia predecessor: it proves that **fixed** positive convex mixtures/direct sums of Lamzouri windows neither change the Fourier-positive cone nor beat the best constituent asymptotic cost. WI-144 narrows coherent positive-Hilbert multi-window lifts. WI-153 closes each separately valid signed support-one scalar census at the same CCLM constant. WI-154--WI-155 then close pointwise-PSD and direct-Loewner matrix rewrites.

A targeted literature and current-follow-up search around multiple/adaptive pair-correlation test functions, Lamzouri multi-kernel bounds, one-delta portfolios, and post-hoc selection located the classical scalar extremal literature and recent Lamzouri/Alpoge--Furman developments, but no theorem using finite post-hoc selection among separately valid universal scalar censuses to evade the one-delta optimum. The mathematical lemma (17)--(19) is elementary and no priority claim is made. The durable contribution recorded here is the **scope closure**: the nonlinear-looking operation left after fixed convex mixing—configuration-dependent best-of-finitely-many scalar selection—still collapses exactly to the best fixed asymptotic channel, and the first possible escape must contain new joint information rather than only a more elaborate selector.

## Research consequence

Finite scalar portfolio optimization under separate Lamzouri-form validity should be treated as closed. This includes fixed mixtures, arbitrary configuration-dependent convex weights, best-of-`J` post-hoc selection, and finite families of fixed indefinite matrix contractions once each contraction has separately been proved to satisfy the scalar census. All of them inherit the same support-one Montgomery--Taylor one-delta ceiling.

The surviving multi-profile target is therefore sharper: construct a **joint zero-side inequality whose feasible set is strictly smaller than the coordinatewise orthant** `Q_j>=L`, so that the combined penalty can beat `min_j Q_j` on every admissible zero configuration, and pair it with an established arithmetic evaluation of the joint observables. For infinite or `T`-dependent portfolios, prove the required uniform pair-correlation control rather than assuming that pointwise fixed-test asymptotics commute with an infimum. Those are genuine new-information gates; adaptive selection by itself is not.

## References

- Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), especially Proposition 2.1 and the support-one optimization in Section 3.
- Emanuel Carneiro, Vorrapan Chandee, Friedrich Littmann and Micah B. Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function*, J. Reine Angew. Math. 725 (2017), 143--182; arXiv:1406.5462, especially Section 3.5 and Corollary 14.
- H. L. Montgomery and A. E. Taylor, *Distribution of the zeros of the Riemann zeta function*, Michigan Math. J. 23 (1976), 21--37, classical origin of the one-delta zeta extremal.
- Andrés Chirre, Felipe Gonçalves and David de Laat, *Pair Correlation Estimates for the Zeros of the Riemann Zeta Function via Semidefinite Programming*, Advances in Mathematics 361 (2020), 106926; arXiv:1810.08843, comparison architecture whose RH-conditional signed-tail mechanism lies outside the scalar universal class considered here.