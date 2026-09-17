# NB-178 — Coordinatewise phase codes recover linear source-complexity certificates

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-SPECIFIC + COORDINATEWISE-DUAL-CERTIFICATE + PHASE-CODE + CAPPED-TRANSPORT + NB-177-ESCAPE-ROUTE`.

`NB-177` shows that the canonical Euler witness of `NB-176` is compact for a structural reason: all Euler coordinates are packed into one jointly contractive Hilbert-valued map, so their total squared dual budget is bounded. The resulting square-summed spectrum has a uniformly summable tail and cannot provide arbitrarily many nondegenerate singular directions at bounded capped-transport amplitude.

That obstruction is real for the Hilbert witness, but it does not exhaust the dual geometry available to `NB-174`. If the probes are required to be contractive **coordinate by coordinate** rather than sharing one global `ell^2` budget, the factorization estimate changes by exactly one factor equal to the number of probes. A dense orthogonal sign/phase response can repay that factor completely. Thus a Hadamard-scale response matrix once again forces linear growth of the approximate source complexity.

This finding does **not** construct such a phase code from natural Nyman--Beurling samplers. Its contribution is to isolate a mathematically valid witness architecture that survives the `NB-177` compactness ceiling, together with the precise spectral target that an arithmetic construction would have to realize.

## Claim

Fix one `T` and abbreviate

\[
\|\sigma\|_{P,T}
:=
\frac{\mathsf D_{a_T}(\sigma)}{q_T}
\]

for zero-mass finite signed measures supported on `[-B,B]`, as in `NB-174`--`NB-177`. Let `mathcal R_T` be the realized template range.

Choose any `N` templates

\[
\nu_1,\ldots,\nu_N\in\mathcal R_T
\]

and any `K` linear functionals `ell_1,...,ell_K` satisfying the **coordinatewise contraction**

\[
\boxed{
|\ell_k(\sigma)|
\le
\|\sigma\|_{P,T}
\qquad
(1\le k\le K)
}
\tag{1}
\]

for every zero-mass signed measure `sigma`. No joint `ell^2` bound across `k` is assumed.

Form the `N x K` response matrix

\[
A_{ik}:=\ell_k(\nu_i)
\]

and put

\[
r:=\min\{N,K\}.
\]

Then for every `epsilon>=0`,

\[
\boxed{
\mathfrak L_T(\epsilon)
\ge
\frac{
\left(
\|A\|_*
-
\epsilon\sqrt{NKr}
\right)_+^2
}{NK}.
}
\tag{2}
\]

Consequently the coordinatewise dual quantity

\[
\mathfrak C_T^{\infty}(\epsilon)
:=
\sup
\frac{
\left(
\|A\|_*
-
\epsilon\sqrt{NK\min\{N,K\}}
\right)_+^2
}{NK},
\tag{3}
\]

where the supremum runs over all finite choices of realized templates and all finite coordinatewise-contractive probe families satisfying (1), obeys

\[
\boxed{
\mathfrak C_T^{\infty}(\epsilon)
\le
\mathfrak L_T(\epsilon).
}
\tag{4}
\]

The superscript is mnemonic for the fact that the map

\[
\sigma\mapsto(\ell_1(\sigma),\ldots,\ell_K(\sigma))
\]

is contractive into `ell^infinity_K`, not into `ell^2_K` as in `NB-175`.

A dense phase-code corollary is immediate. Suppose `N=K` and all singular values of `A` satisfy

\[
s_j(A)\ge \alpha\sqrt N
\qquad(1\le j\le N).
\tag{5}
\]

Then

\[
\|A\|_*
\ge
\alpha N^{3/2},
\]

and (2) gives

\[
\boxed{
\mathfrak L_T(\epsilon)
\ge
N(\alpha-\epsilon)_+^2.
}
\tag{6}
\]

In particular, whenever a Hadamard matrix `H_N` exists and one can realize

\[
A=\alpha H_N,
\qquad
H_NH_N^{\mathsf T}=NI_N,
\tag{7}
\]

then (6) is exact at the level of this certificate.

More generally, no literal `+-1` Hadamard matrix is needed. Any bounded-entry response matrix with a positive proportion of its singular values on the `sqrt N` scale gives a linear-in-`N` lower bound, up to the corresponding constants and tolerance loss.

## Derivation

Take any admissible `epsilon`-approximate dictionary in the definition of `mathfrak L_T(epsilon)` from `NB-174`:

\[
\nu_i
=
\sum_{j=1}^{m}\beta_{ij}\tau_j+r_i,
\qquad
\|\tau_j\|_{P,T}\le1,
\qquad
\|r_i\|_{P,T}\le\epsilon,
\tag{8}
\]

with each coefficient row satisfying

\[
\sum_{j=1}^{m}|\beta_{ij}|^2\le Y^2.
\tag{9}
\]

Let `B` be the `N x m` coefficient matrix, let `D` be the `m x K` dictionary-response matrix

\[
D_{jk}:=\ell_k(\tau_j),
\]

and let `E` be the `N x K` residual-response matrix

\[
E_{ik}:=\ell_k(r_i).
\]

Then

\[
A=BD+E.
\tag{10}
\]

The coefficient bound gives

\[
\|B\|_F\le\sqrt N\,Y.
\tag{11}
\]

Coordinatewise contraction is weaker than the joint Hilbert contraction used in `NB-175`, but it still bounds every dictionary response separately:

\[
|D_{jk}|\le1.
\]

Hence

\[
\|D\|_F\le\sqrt{mK}.
\tag{12}
\]

Likewise

\[
|E_{ik}|\le\epsilon,
\qquad
\|E\|_F\le\epsilon\sqrt{NK}.
\tag{13}
\]

Using the Schatten--Holder product bound and the rank estimate for the nuclear norm,

\[
\|BD\|_*
\le
\|B\|_F\|D\|_F
\le
\sqrt{NmK}\,Y,
\tag{14}
\]

while

\[
\|E\|_*
\le
\sqrt{\operatorname{rank}E}\,\|E\|_F
\le
\epsilon\sqrt{NKr}.
\tag{15}
\]

Therefore

\[
\|A\|_*
\le
\sqrt{NmK}\,Y
+
\epsilon\sqrt{NKr}.
\]

Rearranging, squaring and dividing by `NK` gives

\[
mY^2
\ge
\frac{
(\|A\|_* - \epsilon\sqrt{NKr})_+^2
}{NK}.
\]

Taking the infimum over admissible dictionaries proves (2), and taking the supremum over finite coordinatewise witnesses proves (4).

## Why the extra probe budget does not make the certificate vacuous

The price of abandoning the shared Hilbert budget is visible in (2): relative to `NB-175`, the denominator acquires a factor `K`, and the residual penalty grows accordingly. The theorem therefore does not obtain complexity merely by listing more probes.

For example, repeating the same scalar probe `K` times multiplies the nuclear response only by `sqrt K`; at `epsilon=0` this increase is cancelled exactly by the denominator `K`. There is no artificial gain from duplicated coordinates.

Likewise, mere coordinate separation is not enough. If `N=K` and

\[
A=I_N,
\]

then `||A||_*=N`, so (2) gives only an order-one certificate at zero tolerance. To force order-`N` complexity the responses must be **dense and spectrally spread**: the nuclear norm must reach the `N^(3/2)` scale allowed by `N^2` bounded entries. Orthogonal sign or phase codes are the extremal model for exactly this behavior.

This distinction is the useful content of the new witness class. It asks not merely whether templates can be told apart, but whether many bounded scalar source observables can reuse the same templates with coherently different phase patterns so that the response matrix has large stable rank and large nuclear norm.

## Relation to the NB-177 compactness ceiling

`NB-175` packages its probes into one map taking values in a Hilbert space. Joint contractivity means that, for every normalized source displacement,

\[
\sum_k|\ell_k(\sigma)|^2\le1.
\tag{16}
\]

`NB-176` then chooses the actual square-summed Euler coordinates, and `NB-177` proves that those coordinates have a uniformly compact spectral tail. This makes the average singular value of the canonical Euler response matrix decay with `N`.

The present witness changes exactly the budget responsible for that conclusion. Equation (1) permits

\[
\sum_{k=1}^{K}|\ell_k(\sigma)|^2
\le K\|\sigma\|_{P,T}^2,
\]

so total Hilbert energy may grow like `K`; formula (2) charges that growth explicitly through the factor `K`. A dense orthogonal code has nuclear norm `Theta(N sqrt K)` when `N=K`, so it can repay the entire tariff.

Therefore `NB-177` should not be read as saying that all source-faithful dual certificates are compact. It says that the **one jointly square-summed canonical Euler embedding** is compact. A coordinatewise phase-sensitive architecture remains mathematically viable, provided the arithmetic source can actually realize enough coherent response patterns.

There is no contradiction with `NB-177`: its proof uses the square-summability of one Hilbert feature map, whereas (1) deliberately allows a family whose combined `ell^2` norm grows with the number of coordinates.

## Capped-Poisson scalar probes and the arithmetic construction problem

The coordinatewise class is still tied to the same source geometry. If `f_k:[-B,B]->R` satisfies

\[
|f_k(u)-f_k(v)|
\le
d_{a_T}(u,v)
:=
\min\left\{1,\frac{|u-v|}{a_T}\right\},
\tag{17}
\]

then

\[
\ell_k(\sigma)
:=
\frac1{q_T}\int f_k(u)\,d\sigma(u)
\tag{18}
\]

satisfies (1) by the same capped Kantorovich--Rubinstein argument used in `NB-167` and `NB-175`. Thus the larger witness class does not regain power by changing the metric or the source resolution; it changes only how many scalar dual directions are allowed to coexist.

What is missing is now concrete. For natural Nyman--Beurling template families, construct `N` realized templates and `N` scalar capped-Poisson probes whose response matrix has many singular values of order `sqrt N` after an order-one normalization. A plausible arithmetic mechanism would make different probes reuse the same prime frequencies with different coherent sign or phase patterns, instead of assigning each Euler frequency an orthogonal Hilbert coordinate and square-summing them as in `NB-176`.

That last sentence is a target, not a theorem. No source-native construction of such a matrix is supplied here.

## Self-adversarial audit

Several possible overinterpretations are excluded.

First, (2) is a **lower certificate** for `mathfrak L_T(epsilon)`, not a dual characterization. Large approximate source complexity need not produce a large coordinatewise nuclear witness, and no converse is claimed.

Second, arbitrary individually contractive probes may be chosen after the finite template sample is selected. The theorem is therefore still a geometric existence certificate. To become source-faithful in the stronger arithmetic sense, the probes should arise from a uniform construction tied to the Nyman/Euler representation rather than from opaque Hahn--Banach separation of a finite sample.

Third, a Hadamard-like response is a strong requirement. Individual contractivity alone does not imply it. Realizing `N` almost orthogonal sign columns simultaneously means that the span of the selected templates must support many bounded dual functionals with the required values. That is precisely the nontrivial source geometry that remains to be established.

Fourth, the tolerance term matters. At `N=K`, a dense code of amplitude `alpha` is useful only above the `NB-174` resolution when `alpha>epsilon`. Taking more tiny phase coordinates does not defeat source resolution.

Finally, nothing here removes the sparse exceptional-height escape or the ultra-thin `a_T\lesssim T^(-1/2)` regime inherited from `NB-168`--`NB-174`. The result concerns how to certify the approximate repertoire needed by the existing positive-density obstruction.

## Representation and prior-art audit

The matrix argument is generic. Schatten--Holder, the inequality `||M||_*<=sqrt(rank M)||M||_F`, orthogonality of Hadamard matrices, and the surrounding language of factorization norms are classical matrix/operator theory. A focused literature search found the expected neighboring theory of `gamma_2`, trace/nuclear factorization norms and absolutely summing operators; none of that is claimed as new here.

The line-specific content is narrower: `mathfrak L_T(epsilon)` is the approximate stationary-dictionary currency isolated in `NB-174`; the norm in (1) is the capped Poisson transport norm forced by `NB-167`; and the reason for considering the `ell^infinity` rather than Hilbert probe budget is the concrete square-summability ceiling proved for the canonical Euler witness in `NB-177`.

No new external theorem is load-bearing. The proof uses only elementary finite-dimensional norm inequalities, so no new durable source anchor is required in `SOURCES.md`.

## Research consequence

The witness frontier after `NB-177` can now be stated without the vague phrase “find a more phase-sensitive certificate.” A sufficient target is:

\[
\boxed{
\text{construct source-natural coordinatewise contractions with }
\|A\|_*\asymp N^{3/2}
\text{ at }K=N,
}
\tag{19}
\]

or, more robustly, show that a positive proportion of the singular values of `A` remain on the `sqrt N` scale above the `NB-174` tolerance.

If such matrices can be produced from coherent prime phases of natural Nyman templates, (6) immediately supplies the linear source-complexity lower bound that the square-summed Euler witness cannot reach. If every source-natural coordinatewise construction instead has sub-Hadamard nuclear growth, that failure would expose a stronger compactness principle than `NB-177` and would itself become the next structural obstruction to understand.
