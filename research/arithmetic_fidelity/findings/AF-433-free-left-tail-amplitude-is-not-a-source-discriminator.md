# AF-433 — Free left-tail amplitude is not a source discriminator

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `SOURCE-PROVENANCE` · `DOUBLE-SCALING` · `SHRINKING-TARGET` · `NO-NOVELTY-CLAIM`

## Claim

In the AF-416--AF-432 left-tail hierarchy, the source function is fixed but the reciprocal-order probe family

\[
x_n(c)=\frac cn,
\qquad c>0,
\tag{1}
\]

retains a free positive parameter. Writing

\[
h(x)=-\log\!\left(\frac{1-e^{-x}}x\right),
\qquad
R:=R(h)=2\pi,
\tag{2}
\]

the downstream amplitude is

\[
\boxed{a=\left(\frac cR\right)^2.}
\tag{3}
\]

Thus `c\mapsto a` is a smooth bijection from `(0,\infty)` to `(0,\infty)`. The critical and supercritical exceptional sets of AF-421--AF-432 therefore classify exceptional **probe paths through the fixed source** unless an independent source-side rule first restricts `c`.

The source nevertheless contains more structure than a single radius. If

\[
g(x)=\frac{1-e^{-x}}x,
\qquad g(0)=1,
\tag{4}
\]

then its nonzero zeros are exactly

\[
2\pi i k,\qquad k\in\mathbb Z\setminus\{0\},
\tag{5}
\]

and they are simple. Hence the germ `h=-\log g` has logarithmic singularities there and

\[
h'(x)=-\frac{g'(x)}{g(x)}
\tag{6}
\]

has simple poles at the same points. The source therefore supplies the canonical ordered singularity-shell radii

\[
\boxed{r_m=2\pi m=mR,\qquad m=1,2,\ldots.}
\tag{7}
\]

This corrects the narrower provenance statement that the integer `m` in the square transitions is introduced only downstream. AF-421 proves that adjacent full-column saddle rates collide exactly at

\[
a=m^2,
\tag{8}
\]

and `(3)` plus `(7)` gives the exact equivalence

\[
\boxed{a=m^2\iff c=mR=r_m.}
\tag{9}
\]

So every square transition aligns the `m`-th target packet collision with the modulus of the `m`-th source singularity shell. The integer index has independent source-side and target-side realizations.

This does **not** yet produce a unique arithmetic/source discriminator. The source singularity data canonically reduces the continuum of especially distinguished probe scales to the countable ladder `{r_m}`, but it does not by itself select one shell index for the research question. The first shell `r_1=R` is intrinsically distinguished as the nearest singularity and therefore gives a genuinely source-defined candidate `c=R` (`a=1`); however, using that candidate as the unique probe still requires a stated admissibility/minimality principle explaining why nearest-singularity selection, rather than another source functional or shell, is the relevant notion of canonicity.

For AF-432, if `\mathcal E_q` is the packet-corrected fine-hit amplitude set at fixed rational density `q>2`, then under

\[
\phi(c)=\left(\frac cR\right)^2
\tag{10}
\]

the corresponding probe set `\mathcal C_q=\phi^{-1}(\mathcal E_q)` is again dense `G_\delta`, Lebesgue-null, and has the same Hausdorff dimension bound

\[
\dim_H\mathcal C_q=\dim_H\mathcal E_q\le 1-\frac1q.
\tag{11}
\]

Thus the residual/null dichotomy remains a statement about probe paths until one first restricts the source-side probe rule. Equation `(9)` identifies a nontrivial intrinsic subfamily on which that restriction can now be tested.

## 1. The diagonal parameter is free before source selection

AF-416 proves its full-diagonal asymptotic locally uniformly for `x=c/n` with `c` in arbitrary compact positive intervals. AF-417 retains the same family under derivative shifts. Nothing in that construction requires `c` to lie on the singularity ladder `(7)`.

Consequently, for any nonempty amplitude set `E\subset(0,\infty)`, some admissible probe parameter satisfies `\phi(c)\in E`; and when the complement is nonempty, another admissible parameter satisfies `\phi(c)\notin E`. Pointwise exceptional membership cannot by itself establish source fidelity.

This obstruction concerns provenance, not the validity of the target condition. AF-426--AF-432 impose genuine arithmetic/asymptotic restrictions on packet balance. Those restrictions become source statements only after the admissible probe family has been independently narrowed.

## 2. The source fixes both a unit and a singularity ladder

The zero set in `(5)` follows directly from

\[
1-e^{-x}=0\iff e^{-x}=1\iff x=2\pi i k.
\tag{12}
\]

At every nonzero such point the numerator derivative is `e^{-x}=1`, so the zero is simple. The Taylor germ of `h` is therefore holomorphic on `|x|<2\pi` and cannot extend holomorphically through the nearest zeros. Hence

\[
R(h)=2\pi.
\tag{13}
\]

The same scale is classical in the Bernoulli generating function

\[
\frac{x}{e^x-1}=\sum_{n\ge0}B_n\frac{x^n}{n!},
\qquad |x|<2\pi.
\tag{14}
\]

AF-416's exact even-coefficient formula may accordingly be written

\[
c_{2k}=(-1)^k\frac{\zeta(2k)}{kR^{2k}},
\tag{15}
\]

so the Cauchy resummation depends on the normalized speed `c/R`, yielding `(3)`.

The earlier radius-only naturality audit remains valid. Under the rescaled source family `h_\lambda(y)=h(y/\lambda)`, the radius becomes `\lambda R`; any selector using only the scalar radius and required merely to be similarity-equivariant has the form

\[
S(R)=\kappa R,
\qquad \kappa>0.
\tag{16}
\]

Radius plus homogeneity alone therefore does not force `\kappa=1`.

But the **full singularity set** sharpens the provenance picture. It canonically carries the integer shell order `(7)`. A rule `c=r_m` is target-independent once `m` is specified, while `c=r_1=R` is the unique smallest positive singularity modulus. This is stronger than saying that `2\pi` is merely a convenient numerical normalization, though it still does not prove that the research problem should privilege one shell-selection rule.

## 3. Square packet transitions have dual provenance

AF-421 derives the target-side saddle hierarchy

\[
L_r(b)=\frac{b^r}{(r!)^2},
\qquad
\frac{L_{r+1}(b)}{L_r(b)}=\frac{b}{(r+1)^2}.
\tag{17}
\]

Two adjacent packets tie precisely when `b=m^2`. On the exact critical path this becomes the square-amplitude fiber `a=m^2` studied by AF-422--AF-426.

Combining this target statement with the source singularity ladder yields `(9)`. The coincidence is exact: the same positive integer `m` labels both the source shell radius `r_m=mR` and the adjacent target-packet transition `a=m^2` after the source-normalized coordinate `a=(c/R)^2` is formed.

No novelty is claimed for the singularity lattice or for the algebra in `(9)`. The durable correction is the provenance classification: square amplitudes are **not purely target-generated choices**. They form a canonical source-attached subfamily as well. What remains unresolved is whether the shell/packet index matching reflects a deeper transfer mechanism or is exhausted by the normalization `(3)` together with the elementary square saddle law `(17)`.

AF-426 still supplies a decisive negative result on every exact square fiber: the integer derivative source cannot tune the two complete adjacent packets to cancellation. The present correction does not weaken that theorem. Instead it makes AF-426 more relevant to source fidelity, because its whole square family now has an intrinsic source-side interpretation through `(7)--(9)`.

## 4. Exceptional-set pullback still does not choose a source shell

For fixed rational `q>2`, AF-432 studies the packet-corrected target

\[
\operatorname{dist}\!\left(\widehat\tau_n(a),\mathbb Z\right)
=o(R_n(a)/n^2)
\tag{18}
\]

and proves that the corresponding amplitude set `\mathcal E_q` is residual but metrically thin. Because `\phi` is a homeomorphism and is bi-Lipschitz on every compact subinterval of `(0,\infty)`, category, nullness, and Hausdorff dimension transfer to `\mathcal C_q`, giving `(11)`.

The new shell interpretation does not change this genericity result. A source-side question can now be sharpened to the discrete family

\[
a_m=m^2,
\qquad m\ge1,
\tag{19}
\]

or to the uniquely nearest-shell candidate `a_1=1`, but residuality or nullness of `\mathcal E_q` says nothing by itself about membership of those fixed source-attached points.

## Prior-art and novelty audit

No novelty is claimed for the Bernoulli generating function, its convergence radius, the zeros of `(1-e^{-x})/x`, logarithmic singularities at simple zeros, or transport of category/measure/dimension under smooth one-dimensional changes of variable.

NIST DLMF §24.2 gives the classical Bernoulli generating function `x/(e^x-1)` with `|x|<2\pi`. The singularity locations `(5)` are elementary consequences of the exponential equation and directly explain that radius. The similarity calculation `(16)` is elementary homogeneity.

The Mathia-specific result is the audited provenance chain across AF-416--AF-432: the source fixes the normalization scale and in fact a complete singularity-shell ladder; the target independently has square packet collisions; under the derived amplitude coordinate the two integer ladders coincide exactly. This corrects the previous claim that the square index was solely target-side while preserving the broader obstruction that no unique probe is forced by the current chain.

Source:

- NIST Digital Library of Mathematical Functions, §24.2(i), Bernoulli generating function `x/(e^x-1)=\sum B_nx^n/n!` with `|x|<2\pi`: https://dlmf.nist.gov/24.2

## Boundaries and falsification checks

- The result does **not** invalidate AF-416--AF-432; their analytic, asymptotic, metric, and category statements are unchanged.
- The admissible diagonal family remains all `c>0`. The singularity ladder is a distinguished source-attached subfamily, not an automatic restriction of AF-416.
- `c=R` is source-defined as the nearest singularity modulus, but declaring that this is the uniquely relevant probe still requires an admissibility or minimality principle. Similarity-equivariance alone is insufficient.
- Likewise, `c=mR` is source-defined for every `m>=1`; choosing an `m` because its downstream packet behavior is desirable would still reverse the provenance direction.
- The exact index coincidence in `(9)` does not itself prove a causal source-to-packet mechanism. A decisive strengthening would derive the packet transition from the singularity-shell structure without merely substituting `a=(c/R)^2` into the already-known square law.
- AF-426's obstruction applies to the complete exact-square family and remains valid after the provenance correction.
- The pullback statement `(11)` uses local bi-Lipschitz equivalence on compact subsets of `(0,\infty)`; no endpoint claim at `0` or `\infty` is made.
- No rational-prime discriminator, zeta-zero recovery theorem, or implication for RH is established.

## Consequence for the research line

The source-selection gate is now narrower than previously stated. The source does not merely supply the unit `R=2\pi`; it supplies the ordered singularity scales `r_m=mR`, and these map exactly to the square transition amplitudes `a=m^2`. Therefore the square hierarchy should no longer be dismissed as having purely downstream provenance.

The next source-fidelity test is twofold. First, determine whether nearest-shell selection `c=R` or another shell rule is forced by a principled admissibility/minimality criterion rather than chosen for its target behavior. Second, determine whether the exact shell/packet index matching has a derivable transfer mechanism beyond the coordinate identity `(9)`. Until one of those gates is passed, the continuum of admissible probes remains too large for exceptional-set membership alone to identify the source.