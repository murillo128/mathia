# ANF-002 — unconditional pair correlation already carries horizontal zero information through a global Hilbert inequality

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE` for the claim that unconditional pair-correlation information can affect only vertical multiplicity unless one first places every zero in a narrow box, and for attempts to improve the Montgomery--Taylor constant by optimizing one factorized bandwidth-one squared kernel.

## 1. A new proof changes the information map

Lamzouri, arXiv:2609.02882v1 (2 September 2026), gives a new unconditional proof of the Alpöge--Furman bound

\[
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge
C_0
:=
\frac32-\frac1{\sqrt2}\cot\!\frac1{\sqrt2}
=0.6725007\ldots,
\]

and the corresponding distinct-zero proportion

\[
\liminf_{T\to\infty}\frac{N_d(T)}{N(T)}
\ge
\frac{1+C_0}{2}=0.8362503\ldots .
\]

The numerical theorem is not new relative to Alpöge--Furman. The important new input for `analytic_frontier` is the mechanism: the finite Weil matrix and rank--trace argument can be replaced by a Hilbert-space inequality applied directly to the unconditional Montgomery pair-correlation formula of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh (BGSST).

This exposes a sharper fact about the information content of unconditional pair correlation. The pair-correlation theorem itself need not be supplemented by an a priori narrow-box hypothesis in order to force a positive proportion of zeros to be both simple and on the critical line. The missing horizontal information can instead be extracted from the global conjugation symmetry of the full zero multiset.

## 2. The exact horizontal dictionary

For each nontrivial zero `rho`, define the scaled complex point

\[
z_\rho
:=
i\left(\rho-\frac12\right)\frac{\log T}{2\pi}.
\tag{1}
\]

The functional equation sends `rho` to `1-\bar rho`, so the multiset

\[
\mathcal Z_T=\{z_\rho:0<\operatorname{Im}\rho\le T\}
\]

is invariant under complex conjugation, with multiplicities preserved. Moreover

\[
z_\rho\in\mathbb R
\quad\Longleftrightarrow\quad
\operatorname{Re}\rho=\frac12,
\tag{2}
\]

and multiplicity is unchanged by the scaling. Thus the zeta problem becomes a finite geometric counting problem: simple critical zeros are exactly the simple real elements of a conjugation-invariant complex multiset.

Let `eta` be real, even and supported in `(-lambda,lambda)`, normalized by

\[
\widehat{\eta^2}(0)=1,
\]

and put

\[
K(\xi)=\widehat{\eta^2}(\xi).
\]

Lamzouri's Proposition 2.1 proves for every finite conjugation-invariant multiset `Z` that

\[
\#\{z\in Z\cap\mathbb R:m_z=1\}
\ge
2|Z|-\sum_{z,s\in Z}K(z-s)^2,
\tag{3}
\]

and

\[
\#\{\text{distinct elements of }Z\}
\ge
\frac32|Z|-\frac12\sum_{z,s\in Z}K(z-s)^2.
\tag{4}
\]

Crucially, (3) is a **global** inequality. Individual terms `K(z-s)^2` need not be nonnegative or even real. The proof realizes the kernel through feature functions `eta(u)e^{-2 pi i u z}`, separates the conjugation-even and conjugation-odd directions, and applies Bessel/Parseval inequalities to nested Hilbert subspaces. Horizontal location is therefore recovered from the geometry of the whole Gram system rather than from termwise positivity of a kernel on complex differences.

## 3. This kills the global-positive-kernel obstruction, not by solving it but by bypassing it

The predecessor narrow-box arguments sought kernels whose real part remains positive on the complex strip containing all scaled zero differences. If one tries to remove every horizontal restriction while retaining that termwise strategy, one would need a nonconstant entire kernel with nonnegative real part on all of `C`, which does not exist.

Lamzouri does not find such a kernel. Equation (3) makes it unnecessary. This is an important analytic-frontier correction: **termwise positivity is not the right abstraction for extracting horizontal information from unconditional pair correlation**.

The mechanism is also more informative than a scalar zero-density bound. It directly counts real points inside a conjugation-invariant complex configuration. In particular, it demonstrates that a second-order zero statistic can carry horizontal information even though the underlying unconditional BGSST theorem was historically introduced as a pair-correlation theorem.

## 4. Why the quadratic form is unconditionally evaluable

For the zeta application Lamzouri takes `eta` supported in `(-1/2,1/2)` and sets

\[
Q=\eta^2*\eta^2.
\]

Then

\[
\widehat Q=K^2,
\qquad
\operatorname{supp}Q\subset[-1,1].
\tag{5}
\]

BGSST's unconditional Montgomery theorem evaluates, for real even `f` supported in `[-1,1]`, a weighted complex-difference sum of the form

\[
\sum_{\rho,\rho'}
\widehat f\!\left(i(\rho-\rho')\frac{\log T}{2\pi}\right)
\frac{4}{4-(\rho-\rho')^2}.
\tag{6}
\]

The Hilbert inequality needs the same sum without the rational weight. Lamzouri removes it by a derivative correction to the compactly supported test function: combining `Q` with a `Q''/(\log T)^2` term multiplies its Fourier transform by the inverse rational factor needed to cancel (6). Hence the desired unweighted sum has asymptotic

\[
\sum_{\rho,\rho'}
K\!\left(i(\rho-\rho')\frac{\log T}{2\pi}\right)^2
=
\left(C_\eta+o(1)\right)N(T),
\tag{7}
\]

where

\[
C_\eta
=
Q(0)+2\int_0^1 \alpha Q(\alpha)\,d\alpha.
\tag{8}
\]

Combining (3) and (7) gives

\[
\frac{N_0^s(T)}{N(T)}\ge 2-C_\eta-o(1).
\tag{9}
\]

Thus the analytic input required to obtain horizontal information is still only the known support-one unconditional pair-correlation formula; the new ingredient is the global Hilbert-space counting inequality.

## 5. The single factorized squared-kernel route has an exact Montgomery--Taylor ceiling

This simplification also makes the next barrier unusually clean. Lamzouri cites Corollary 14 of Carneiro--Chandee--Littmann--Milinovich, *Hilbert spaces and the pair correlation of zeros of the Riemann zeta-function* (2017), to obtain

\[
C_\eta\ge C_{\rm MT}
:=
\frac12+\frac1{\sqrt2}\cot\!\frac1{\sqrt2}
=1.3274992\ldots .
\tag{10}
\]

The Montgomery--Taylor extremizer attains the infimum in the appropriate limiting sense. Therefore (9) cannot exceed

\[
2-C_{\rm MT}=0.6725007\ldots
\tag{11}
\]

within this method. This is not merely evidence that the currently chosen kernel is suboptimal: the entire single-feature class `K=\widehat{eta^2}` with the squared-kernel quadratic form is exhausted.

This agrees structurally with `WI-001`, where the finite-compression proof reaches the same constant and the first-two-moment information admits explicit extremizers. Lamzouri's proof shows that the matrix apparatus is not itself the source of the ceiling: after eliminating it completely, the same second-moment extremal problem remains.

## 6. The nearest known escape points outside the exhausted class

There are two mathematically distinct signs that the `0.6725007...` ceiling is a **class ceiling**, not a universal pair-correlation ceiling.

First, Chirre--Gonçalves--de Laat (Adv. Math. 361 (2020), 106926) showed under RH that a broader Cohn--Elkies/semidefinite test-function class gives

\[
N^*(T)\le(1.3208+o(1))N(T),
\]

and therefore at least `0.6792` of the zeros are simple. Their gain comes from relaxing compact Fourier support to a sign condition outside the support-one region and then using a nonnegative pair-correlation function to discard the uncontrolled tail. Their proof, however, assumes RH; its pair-correlation asymptotic is a real-ordinate statement and cannot simply be inserted into (3) for arbitrary complex zero differences.

Second, `WI-001` records an unaudited contemporary claim by Devine of an unconditional `0.673399` simple-critical proportion from several bandlimited profiles and pair-interaction constraints. If valid, that would already demonstrate that combining several legal second-order observables escapes the one-kernel optimization (10). It is not used as evidence here because its analytic and numerical certificate chain has not been accepted by Mathia.

These comparisons sharpen the open problem. The next gain does not require inventing a statistic that is horizontal-sensitive from scratch; (3) already supplies one. It requires **strictly more usable quadratic information than one factorized squared kernel**, or a controlled extension beyond support one, while retaining the unconditional complex-zero treatment.

## 7. Relation to ANF-001

`ANF-001` remains valid: fixed-`sigma` zero-additive-energy exponents lose their power saving when transported to the microscopic horizontal scale `sigma-1/2=O(1/log T)`. Lamzouri's result does not upgrade those energy estimates.

What changes is the interpretation of the analytic frontier. A microscopic fixed-`sigma` energy theorem is **not the only possible way** to make pair information horizontal. The conjugation-symmetric Hilbert inequality extracts horizontal location without first binning zeros by `beta` at all. Consequently future work should distinguish two targets:

- stronger near-line energy/correlation estimates that attack the bounded-depth exceptional population directly; and
- richer global quadratic certificates that use the existing unconditional complex-difference pair-correlation formula more efficiently than the single-kernel class.

The second target is now concrete and independently motivated by the conditional semidefinite gain.

## 8. Prior-art and novelty assessment

Theorem 1.1, Proposition 2.1, the BGSST pair-correlation input, the derivative weight-removal trick, and the Montgomery--Taylor optimality statement are all literature results from Lamzouri and the papers he cites. The `0.6792` semidefinite bound is likewise prior art of Chirre--Gonçalves--de Laat. No novelty is claimed for them.

The Mathia-specific contribution of this finding is the information-boundary classification: the newest proof proves that unconditional support-one pair correlation already contains recoverable horizontal information once termwise kernel positivity is replaced by conjugation-symmetric Hilbert geometry, while simultaneously identifying an exact ceiling for the resulting one-factor quadratic class. This converts the vague question “can pair correlation say anything horizontal?” into the narrower question “what additional legal quadratic or out-of-band information breaks the Montgomery--Taylor extremal problem?”

## 9. Decisive falsification / upgrade test

This finding should be revised if either boundary changes:

- if Proposition 2.1 or the claimed unconditional evaluation (7) is found to require an unstated horizontal hypothesis, then the horizontal-information classification fails; or
- if a kernel inside the exact factorized class of Proposition 2.1 produces `C_eta<C_MT`, then the stated ceiling fails and would contradict the cited extremal theorem.

For progress beyond the finding, the decisive first test is to construct a rigorously evaluable unconditional quadratic certificate outside the one-factor class whose normalized constant is strictly below `C_MT`. A successful certificate would immediately improve `0.6725007...`; a no-go theorem showing that every support-one positive-semidefinite lift collapses to a convex combination of one-factor certificates would instead prove that genuinely new support or higher-order correlation information is necessary.