# AF-433 — Free left-tail amplitude is not a source discriminator

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `SOURCE-PROVENANCE` · `DOUBLE-SCALING` · `SHRINKING-TARGET` · `NO-NOVELTY-CLAIM`

## Claim

In the AF-416--AF-432 left-tail hierarchy, the amplitude

\[
a=\frac{c^2}{4\pi^2}
\tag{1}
\]

is not presently selected by the underlying analytic source. The source function and left-tail germ are fixed, but AF-416 evaluates them on the whole reciprocal-order family

\[
x_n(c)=\frac cn,
\qquad c>0,
\tag{2}
\]

and AF-417 retains the same arbitrary positive parameter under derivative shifts. The map

\[
\phi:(0,\infty)\to(0,\infty),
\qquad
\phi(c)=\frac{c^2}{4\pi^2},
\tag{3}
\]

is a smooth bijection with smooth inverse `c=2\pi\sqrt a`. Therefore every positive amplitude appearing in AF-421--AF-432 can be realized by tuning the external diagonal constant `c`, without changing the intrinsic source function.

Consequently, for any subset `E\subset(0,\infty)`:

\[
E\neq\varnothing
\iff
\exists c>0:\phi(c)\in E,
\tag{4}
\]

and, if `E` is proper,

\[
(0,\infty)\setminus E\neq\varnothing
\iff
\exists c>0:\phi(c)\notin E.
\tag{5}
\]

Thus membership of `a` in a critical or supercritical shrinking-target exceptional set is **not an intrinsic source-fidelity statement** unless an independent source-side rule first selects `c` (equivalently `a`) before the target condition is inspected.

For AF-432 in particular, let `\mathcal E_q` be its first packet-corrected fine-hit set for a fixed rational density `q>2`, and define the corresponding diagonal-parameter set

\[
\mathcal C_q:=\phi^{-1}(\mathcal E_q).
\tag{6}
\]

Because `\phi` is a homeomorphism and is bi-Lipschitz on every compact subinterval of `(0,\infty)`, AF-432 immediately implies that `\mathcal C_q` is a dense `G_\delta`, has Lebesgue measure zero, and satisfies

\[
\dim_H \mathcal C_q
=
\dim_H \mathcal E_q
\le 1-\frac1q.
\tag{7}
\]

Hence the residual/null dichotomy survives unchanged when expressed in the original diagonal constant. It classifies exceptional **probe paths** through the fixed source, not distinguished source amplitudes.

There is, however, a source-intrinsic scale hidden in `(1)`. For

\[
h(x)=-\log\!\left(\frac{1-e^{-x}}x\right),
\]

the Taylor germ at the origin has exact analyticity radius

\[
\boxed{R(h)=2\pi.}
\tag{8}
\]

Therefore the downstream amplitude is exactly

\[
\boxed{a=\left(\frac c{R(h)}\right)^2.}
\tag{9}
\]

The source thus canonically supplies the **unit in which the diagonal speed is measured**. It does not, from the radius data alone, select one dimensionless speed `c/R(h)`. Under the rescaled source family `h_\lambda(y)=h(y/\lambda)`, one has `R(h_\lambda)=\lambda R(h)`, and every rule

\[
c_\kappa(h)=\kappa R(h),\qquad \kappa>0,
\tag{10}
\]

is target-independent and similarity-equivariant. Hence analyticity radius plus scale covariance leaves a full dimensionless continuum `\kappa`; it removes a scale gauge but does not by itself close the amplitude-provenance gate.

In particular, the exact square values satisfy

\[
a=m^2
\iff
c=mR(h).
\tag{11}
\]

Their factor `R(h)=2\pi` is genuinely source-side, while the integer label `m` is singled out downstream by adjacent-saddle collisions in AF-421--AF-426. The special choice `c=R(h)` (`a=1`) is therefore a natural source-normalized candidate, but radius and similarity-equivariance alone do not force the normalized value `\kappa=1`; an additional source-side characterization would still be required to promote it from normalization to discriminator.

## 1. The diagonal constant remains free in the canonical source chain

AF-416 fixes

\[
f(t)=-\log(1-e^{-e^t})
\]

and its left-tail analytic decomposition, then proves its full-diagonal asymptotic **uniformly for every compact positive interval of `c`** at `x=c/n`. Nothing in that construction chooses one `c` over another.

AF-417 keeps exactly the same family `x=c/n`, with arbitrary `c>0`, while allowing derivative depths `s_n/n\to\sigma`. Its fixed-excess limit depends on the combination

\[
e^\sigma\frac{c^2}{4\pi^2}.
\]

Introducing `a=c^2/(4\pi^2)` is therefore a useful asymptotic coordinate, but it does not add source information. Equations `(1)` and `(3)` show that the change of variables is lossless and onto.

Later critical and supercritical analyses constrain derivative depth, packet index, saddle location, or integer realizability. None of AF-421--AF-432 supplies an additional rule that reduces the admissible continuum `c>0` to a source-determined point.

## 2. The nearest source singularity fixes the unit but not the normalized speed

Set

\[
g(x)=\frac{1-e^{-x}}x,
\qquad g(0):=1.
\]

Then `g` is entire and its nonzero zeros are exactly

\[
2\pi i k,\qquad k\in\mathbb Z\setminus\{0\}.
\tag{12}
\]

They are simple because the numerator derivative `e^{-x}` equals one there. The germ `h=-\log g` is therefore holomorphic throughout `|x|<2\pi`. It cannot extend holomorphically across `x=\pm2\pi i`, because

\[
h'(x)=-\frac{g'(x)}{g(x)}
\]

has simple poles at those zeros. This proves `(8)` exactly. The classical Bernoulli generating function records the same radius: DLMF §24.2 gives the expansion of `x/(e^x-1)` for `|x|<2\pi`.

This source radius is already visible algebraically in AF-416. Its exact coefficient formula is

\[
c_{2k}=(-1)^k\frac{\zeta(2k)}{kR(h)^{2k}},
\tag{13}
\]

so every partition displacement by total excess `2d` carries the dimensionless factor

\[
\left(\frac{x}{R(h)}\right)^{2d}.
\tag{14}
\]

On `x=c/n`, the resummed Cauchy limit can therefore be written without a special numerical constant as

\[
\exp\!\left(-\left(\frac c{R(h)}\right)^2\right).
\tag{15}
\]

Thus `2\pi` in the AF-416--AF-432 amplitude is not an arbitrary target normalization: it is the nearest-singularity scale of the source germ.

That observation does **not** yet select a point on the amplitude line. To isolate what scale naturality can prove, consider the similarity orbit

\[
h_\lambda(y):=h(y/\lambda),\qquad \lambda>0.
\tag{16}
\]

Its radius is `R(h_\lambda)=\lambda R(h)`. A scalar selector `S` that depends only on the radius and is equivariant under these similarities must obey

\[
S(\lambda R)=\lambda S(R).
\tag{17}
\]

Putting `R=1` after rescaling shows that every such selector has the form

\[
\boxed{S(R)=\kappa R}
\tag{18}
\]

for one constant `\kappa>0`, and conversely every `\kappa` gives an equivariant selector. Hence the radius determines the physical unit but leaves the normalized coordinate

\[
\kappa=\frac cR
\tag{19}
\]

undetermined.

This is the exact provenance distinction needed here. A rule may still select `\kappa` by using additional source structure, a variational principle, a source symmetry-breaking condition, or a separately justified normalization. But the statement "the source has nearest singularities at distance `2\pi`" alone cannot distinguish `c=2\pi` from `c=\kappa 2\pi` for another fixed `\kappa`.

## 3. Pointwise exceptional membership is tunable without a source selector

Suppose a downstream theorem defines a nontrivial target set `E` of amplitudes by some property `P(a)`. As long as the admissible source-side probe family remains `(2)`, the source can be evaluated along a path whose amplitude lies in `E` whenever `E` is nonempty, and along a path outside `E` whenever its complement is nonempty.

This is not a statement that the target property is arbitrary. AF-426--AF-432 impose highly nontrivial arithmetic and asymptotic restrictions on which amplitudes satisfy their packet-balance conditions. The obstruction is instead one of **provenance**: those restrictions classify the pair `(source, chosen diagonal path)`, while the source function alone does not select the path.

Accordingly, a pointwise theorem such as

\[
a_*\in\mathcal E_q
\qquad\text{or}\qquad
a_*\notin\mathcal E_q
\]

becomes a source-fidelity statement only after `a_*` has been independently derived from source data under an admissible normalization or symmetry rule. Choosing `a_*` because it has desirable saddle behavior reverses the required direction of explanation.

After `(8)--(19)`, this gate can be stated more sharply: the source already supplies the scale `R(h)`, so what remains to be selected is the **dimensionless ratio** `\kappa=c/R(h)`. Merely rediscovering `2\pi` from Bernoulli coefficients or complex singularities does not solve that remaining selection problem.

## 4. AF-432 pulls back exactly to the free diagonal family

For fixed rational `q=u/v>2`, AF-432 studies

\[
\widehat\tau_n(a)
=
\tau_n(a)+a e^q R_n(a)/n^2
\]

and the infinitely-often target

\[
\operatorname{dist}(\widehat\tau_n(a),\mathbb Z)
=o(R_n(a)/n^2).
\tag{20}
\]

Its exceptional set is residual but metrically thin. Under `(3)`, `(20)` is simply a condition on `c` through `a=\phi(c)`. Homeomorphisms preserve dense `G_\delta` sets, while on each compact interval `\phi` and `\phi^{-1}` are Lipschitz. Covering `(0,\infty)` by compact intervals bounded away from zero transfers nullness and Hausdorff dimension in both directions, giving `(7)`.

This makes the provenance issue explicit: the strongest current supercritical genericity result remains true after returning to the original free scaling parameter. No arithmetic identity has yet picked one point of that parameter line.

## 5. Critical square collisions mix a source scale with a target index

AF-421 identifies the transition `b=m^2` because two adjacent full-column saddle rates agree there. AF-422--AF-426 then analyze the finer packet balance at that collision. At exact square amplitude `a=m^2`, AF-426 proves an irreducible source-packet gap.

Equation `(11)` now separates the provenance of `c=2\pi m`: the factor `2\pi=R(h)` is intrinsic to the source germ, whereas the integer `m` comes from the downstream saddle-packet collision. Rewriting a target collision in source units therefore reveals a genuine source scale, but it does not make the target packet label source-forced.

The case `m=1` deserves the narrower statement. It coincides with the source-normalized choice `c=R(h)`, so it can no longer be dismissed as numerically unrelated to source structure. However, radius data alone still leave every `c=\kappa R(h)` scale-equivariant; one must independently justify why the normalized speed should be `\kappa=1` before AF-426's `m=1` obstruction can be interpreted as the fate of a distinguished source probe rather than one natural normalization among a continuum.

## Prior-art and novelty audit

No novelty is claimed for the elementary diffeomorphism `(3)`, for transporting category/measure/dimension statements through a smooth change of coordinates, for the general fact that double-scaling asymptotics may contain externally varied parameters, or for the radius-of-convergence calculation in `(8)`. DLMF §24.2 records the classical Bernoulli generating function with convergence domain `|x|<2\pi`; the zero set of `(1-e^{-x})/x` gives the same boundary directly.

The similarity calculation `(16)--(18)` is elementary homogeneity, not a new invariant-theory result. Its role is to audit the exact source/normalization boundary: the nearest complex singularity explains why `2\pi` is the intrinsic scale in AF-416, while scale covariance alone cannot choose the remaining dimensionless probe speed.

The durable Mathia result is therefore narrower: it audits the exact provenance chain AF-416--AF-432 and shows that the current amplitude variable is still a free probe coordinate **after quotienting out its source-determined scale**. The existing residual/null exceptional-set theorems cannot by themselves supply the rational-prime or source discriminator sought by Arithmetic Fidelity.

Source:

- NIST Digital Library of Mathematical Functions, §24.2(i), Bernoulli generating function `x/(e^x-1)=\sum B_nx^n/n!` with `|x|<2\pi`: https://dlmf.nist.gov/24.2

## Boundaries and falsification checks

- The result does **not** invalidate AF-416--AF-432. Their analytic, asymptotic, metric, and category statements remain unchanged.
- It does not say that no intrinsic source-selection rule for `c` exists. It says that none has been established in the current canonical chain, and now isolates the unresolved part as selection of the dimensionless ratio `\kappa=c/R(h)`.
- It does not prove that `c=R(h)` is an inadmissible selector. A separately justified rule such as a variational principle or source theorem may genuinely force `\kappa=1`; if so, that selected amplitude must be tested against the existing critical/supercritical gates.
- Conversely, merely observing that `R(h)=2\pi`, or declaring "one analyticity radius" as a normalization, does not by itself prove uniqueness: every `\kappa R(h)` is similarity-equivariant.
- The rescaling family `(16)` is used only to audit scale naturality. It does not assert that all rescaled germs represent the identical physical/arithmetic source under every richer structure.
- Square amplitudes mix provenances: `R(h)` is source-derived, while the integer `m` in `c=mR(h)` is introduced by the downstream saddle collision unless another source theorem independently selects it.
- The result does not rule out selectors built from dimensionless invariants of the **full normalized germ** rather than its radius alone. Such a proposal must state its admissible source family and naturality/minimality criterion so that canonicity is falsifiable rather than a choice of formula.
- The pullback statement `(7)` uses local bi-Lipschitz equivalence on compact subsets of `(0,\infty)`; no claim is made about adding the endpoints `0` or `\infty`.
- No rational-prime discriminator, zeta-zero recovery, or implication for RH is established.

## Consequence for the research line

The source-selection gate now splits cleanly into two parts. The **scale gate is solved** for the current analytic germ: its nearest singularities give the exact unit `R(h)=2\pi`, and the AF-416 amplitude is simply the squared normalized speed `a=(c/R(h))^2`. The remaining **ratio gate** is the substantive one: derive a source-intrinsic, normalization-stable rule selecting `\kappa=c/R(h)` without consulting the downstream saddle cancellation or shrinking-target outcome.

Only after such a ratio selector is proved does pointwise membership in the AF-428 critical exceptional set or AF-432 supercritical fine-hit set become mathematically capable of distinguishing the source. Exact square amplitudes do not bypass this gate: they correspond to `\kappa=m`, where `m` is presently a target packet index. If no additional source structure selects `\kappa`, further pointwise analysis of arbitrarily chosen amplitudes would refine the geometry of the probe family but would not advance arithmetic fidelity.