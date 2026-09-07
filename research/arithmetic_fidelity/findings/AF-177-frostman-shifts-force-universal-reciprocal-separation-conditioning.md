# AF-177 — Frostman shifts force universal reciprocal-separation inverse conditioning

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `QUANTITATIVE-RECOVERY-BOUNDARY`, `CONDITIONING-CLASSIFICATION`, `FROSTMAN-SHIFT`, `GAUGE-QUOTIENT`, `NO-NOVELTY-CLAIM`

## Claim

AF-176 showed on the regular cyclic Blaschke family that local inverse conditioning of the zero divisor is at least one half of the reciprocal interpolation constant. That phenomenon is not special to the cyclic model.

Let

\[
B(z)=\eta\prod_{i=1}^n\phi_{a_i}(z),
\qquad
\phi_a(z)=\frac{z-a}{1-\overline a z},
\qquad n\ge 2,
\tag{1}
\]

be any finite Blaschke product with simple zeros `a_1,...,a_n`. Define

\[
\delta_i(B)
=(1-|a_i|^2)|B'(a_i)|
=\prod_{j\ne i}\rho(a_i,a_j),
\qquad
\delta(B)=\min_i\delta_i(B)>0,
\tag{2}
\]

where

\[
\rho(z,w)=\left|\frac{z-w}{1-\overline w z}\right|.
\tag{3}
\]

For `t\in\mathbb D`, let

\[
F_t(w)=\frac{w-t}{1-\overline t\,w},
\qquad
B_t=F_t\circ B.
\tag{4}
\]

Up to an irrelevant unimodular sign convention, this is the classical Frostman shift. Its zero divisor is the level set `B^{-1}(t)` counted with multiplicity.

Use the quotient output metric from AF-173--AF-176,

\[
\Delta(B,C)
=\inf_{|\lambda|=1}\|B-\lambda C\|_{H^\infty},
\tag{5}
\]

and the multiplicity-aware pseudohyperbolic bottleneck metric

\[
d_{\mathrm{div}}^\rho(B,C)
=\min_{\sigma\in S_n}\max_i\rho(a_i,b_{\sigma(i)}).
\tag{6}
\]

Then, as `t\to0`,

\[
\boxed{
\Delta(B,B_t)=2|t|,
}
\tag{7}
\]

and

\[
\boxed{
 d_{\mathrm{div}}^\rho(B,B_t)
 =\frac{|t|}{\delta(B)}+o(|t|).
}
\tag{8}
\]

Consequently

\[
\boxed{
\lim_{t\to0}
\frac{d_{\mathrm{div}}^\rho(B,B_t)}{\Delta(B,B_t)}
=\frac{1}{2\delta(B)}.
}
\tag{9}
\]

Thus the reciprocal-separation lower conditioning scale found in AF-176 is **universal at every finite simple Blaschke divisor**: a canonical postcomposition direction witnesses it without cyclic symmetry.

More precisely, define the local inverse condition number at `B` among same-degree finite Blaschke products by

\[
\kappa_{\mathrm{loc}}(B)
=
\limsup_{\substack{C\to B\\ \deg C=n}}
\frac{d_{\mathrm{div}}^\rho(B,C)}{\Delta(B,C)}.
\tag{10}
\]

Then AF-175 and `(9)` give the factor-two enclosure

\[
\boxed{
\frac{1}{2\delta(B)}
\le
\kappa_{\mathrm{loc}}(B)
\le
\frac{1}{\delta(B)}.
}
\tag{11}
\]

The interpolation constant is therefore not merely a sufficient regularity modulus and not merely a parameter exposed by one symmetric family. Up to a universal factor `2`, it is the local conditioning scale throughout the simple finite-Blaschke stratum for these source and output metrics.

## Derivation

### Frostman level sets move each simple zero at reciprocal derivative speed

Because every zero `a_i` is simple, the holomorphic inverse-function theorem gives, for `t` near `0`, a unique local branch `a_i(t)` satisfying

\[
B(a_i(t))=t,
\qquad
a_i(0)=a_i.
\tag{12}
\]

Differentiating at `t=0` gives

\[
a_i'(0)=\frac{1}{B'(a_i)},
\tag{13}
\]

so

\[
a_i(t)-a_i
=\frac{t}{B'(a_i)}+O(|t|^2).
\tag{14}
\]

The pseudohyperbolic denominator obeys

\[
|1-\overline{a_i}a_i(t)|
=(1-|a_i|^2)+O(|t|),
\tag{15}
\]

and hence

\[
\rho(a_i,a_i(t))
=
\frac{|t|}{(1-|a_i|^2)|B'(a_i)|}+o(|t|)
=
\frac{|t|}{\delta_i(B)}+o(|t|).
\tag{16}
\]

Since the original zero set is finite and has positive minimum pairwise pseudohyperbolic separation, these inverse branches lie in disjoint neighborhoods for sufficiently small `t`. Any matching that sends `a_i` to the branch born from a different zero then has a positive-order cost, whereas the branchwise matching has cost `O(|t|)`. Thus the optimal bottleneck matching is branchwise once `t` is small enough, and

\[
d_{\mathrm{div}}^\rho(B,B_t)
=
\max_i\rho(a_i,a_i(t))
=
\frac{|t|}{\min_i\delta_i(B)}+o(|t|),
\tag{17}
\]

which proves `(8)`.

### Postcomposition makes the output displacement independent of the divisor

A finite Blaschke product maps the unit circle onto itself. Therefore, for every unimodular `\lambda`,

\[
\|B-\lambda F_t\circ B\|_{H^\infty}
=
\sup_{|w|=1}|w-\lambda F_t(w)|.
\tag{18}
\]

Taking the infimum over `\lambda` reduces the quotient distance exactly to the degree-one disk-automorphism problem:

\[
\Delta(B,B_t)
=
\Delta(\operatorname{id},F_t).
\tag{19}
\]

AF-173's exact quotient identity, specialized to degree one and parameters `0,t`, gives

\[
\Delta(\operatorname{id},F_t)=2\rho(0,t)=2|t|,
\tag{20}
\]

proving `(7)`. Combining `(7)` and `(17)` yields `(9)`.

### AF-175 supplies the matching universal upper scale

AF-175 proved that if a reference finite Blaschke product satisfies `\delta(B)\ge\delta>0`, then for sufficiently small output error

\[
d_{\mathrm{div}}^\rho(B,C)
\le
\omega_\delta(\Delta(B,C)),
\qquad
\omega_\delta(s)=\frac{s}{\delta}+O_\delta(s^2).
\tag{21}
\]

For any `0<\delta<\delta(B)`, this gives

\[
\kappa_{\mathrm{loc}}(B)\le\frac1\delta.
\tag{22}
\]

Letting `\delta\uparrow\delta(B)` gives the upper half of `(11)`, while the Frostman family `B_t` gives the lower half. Thus all simple finite Blaschke products have local inverse conditioning pinned to the reciprocal interpolation constant within a factor of two.

## Prior art and novelty assessment

No theorem-level novelty in complex analysis is claimed. The ingredients are classical; the derived content is their use as an Arithmetic Fidelity conditioning identity for the specific source/output metrics fixed by AF-173--AF-176.

- Raymond Mortini and Artur Nicolau, **“Frostman shifts of inner functions,”** *Journal d'Analyse Mathématique* 92 (2004), 285--326, DOI `10.1007/BF02787765`, develops the classical Frostman-shift framework in terms of level sets, zero distributions, and pseudohyperbolic derivatives.
- Pamela Gorkin and Raymond Mortini, **“Value Distribution of Interpolating Blaschke Products,”** *Journal of the London Mathematical Society* 72(1) (2005), 151--168, DOI `10.1112/S0024610705006411`, explicitly studies shifted products of the form `(a-B)/(1-\overline a B)` and the separation quantity `(1-|z|^2)|B'(z)|` on their level-set zeros.
- Stephan Ramon Garcia, Javad Mashreghi, and William T. Ross, ***Finite Blaschke Products and Their Connections***, Springer (2018), DOI `10.1007/978-3-319-78247-8`, is modern background for finite Blaschke products, disk automorphisms, boundary maps, and level sets.
- AF-175 already derives the Hoffman/Rouché upper recovery modulus, and AF-176 derives the factor-`1/2` lower bound on a cyclic radial family.

The inverse-function expansion `(13)`--`(17)` is elementary local complex analysis. The exact output identity `(18)`--`(20)` is inherited from the quotient metric already established in AF-173. A targeted prior-art search found mature literature on Frostman shifts and the separation of shifted level sets. It does not justify presenting `(9)` as a new theorem of Blaschke-product theory. The line-specific advance is the recognition that the classical Frostman shift supplies a **universal worst-direction witness of the same reciprocal-separation conditioning scale** that had previously been proved only on the cyclic calibration family.

## Boundary conditions and falsification checks

- The reference product must have simple zeros, equivalently `\delta(B)>0`. At a multiple zero the local level-set branches have fractional-power splitting and AF-174's Hölder regime replaces the Lipschitz analysis.
- Equation `(8)` is local as `t\to0`. It is not a global Lipschitz statement for arbitrary level sets or arbitrary pairs of Blaschke products.
- The branchwise bottleneck conclusion uses finiteness and positive separation of the fixed reference divisor. It is not asserted uniformly as the reference divisor itself approaches a collision stratum.
- The lower bound is for the same quotient `H^\infty` output metric and pseudohyperbolic divisor bottleneck metric used in AF-173--AF-176. Changing either metric can change the numerical constant and may change the conditioning notion.
- The factor `2` comes from the exact quotient output normalization. The robust structural statement is reciprocal dependence on `\delta(B)`, not that `1/2` is metric-independent.
- The upper bound in `(11)` is inherited from AF-175 and need not be sharp. AF-177 narrows the remaining constant gap to at most a factor of two; it does not prove the exact full local condition number.
- Frostman postcomposition is a canonical perturbation of the retained inner function, but its usefulness here does not imply that every other perturbation has the same first-order cost. It supplies a lower-bound witness, not a complete tangent-space classification.
- No arithmetic or RH consequence follows. A transfer to a Mathia arithmetic construction would require an intrinsic analogue of the interpolation modulus and an independently justified correspondence between its source perturbations and the downstream compression metric.

## Consequences for the research line

AF-176 left open whether reciprocal separation was genuinely universal or an artifact of the exactly solvable cyclic family. AF-177 closes that ambiguity at the local level. Every finite simple Blaschke product possesses a canonical Frostman direction whose source divisor moves at speed `1/\delta(B)` while its quotient-output representation moves at fixed speed `2`.

The resulting factor-two enclosure `(11)` is a stronger fidelity classification than either an injectivity statement or a one-sided recovery theorem. It identifies an intrinsic source modulus and shows both that preserving it is sufficient for stable recovery and that allowing it to collapse necessarily destroys uniform conditioning. This is the reusable pattern sought by the Arithmetic Fidelity mandate: a compression should be audited not only for exact distinguishability, but for the source regularity quantity that controls how distinguishability survives perturbation.