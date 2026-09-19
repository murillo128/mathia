# AF-433 — Free left-tail amplitude is not a source discriminator

## Status

`EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `ARITHMETIC-FIDELITY` · `SOURCE-PROVENANCE` · `DOUBLE-SCALING` · `SHRINKING-TARGET` · `NO-NOVELTY-CLAIM`

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

The exact square values `a=m^2`, equivalently `c=2\pi m`, do not repair this provenance gap. They are singled out downstream by equality of adjacent saddle rates in AF-421--AF-426. That is a target-side collision condition, not a source-side rule selecting one member of `(2)`.

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

## 2. Pointwise exceptional membership is tunable without a source selector

Suppose a downstream theorem defines a nontrivial target set `E` of amplitudes by some property `P(a)`. As long as the admissible source-side probe family remains `(2)`, the source can be evaluated along a path whose amplitude lies in `E` whenever `E` is nonempty, and along a path outside `E` whenever its complement is nonempty.

This is not a statement that the target property is arbitrary. AF-426--AF-432 impose highly nontrivial arithmetic and asymptotic restrictions on which amplitudes satisfy their packet-balance conditions. The obstruction is instead one of **provenance**: those restrictions classify the pair `(source, chosen diagonal path)`, while the source function alone does not select the path.

Accordingly, a pointwise theorem such as

\[
a_*\in\mathcal E_q
\qquad\text{or}\qquad
a_*\notin\mathcal E_q
\]

becomes a source-fidelity statement only after `a_*` has been independently derived from source data under an admissible normalization or symmetry rule. Choosing `a_*` because it has desirable saddle behavior reverses the required direction of explanation.

## 3. AF-432 pulls back exactly to the free diagonal family

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
\tag{8}
\]

Its exceptional set is residual but metrically thin. Under `(3)`, `(8)` is simply a condition on `c` through `a=\phi(c)`. Homeomorphisms preserve dense `G_\delta` sets, while on each compact interval `\phi` and `\phi^{-1}` are Lipschitz. Covering `(0,\infty)` by compact intervals bounded away from zero transfers nullness and Hausdorff dimension in both directions, giving `(7)`.

This makes the provenance issue explicit: the strongest current supercritical genericity result remains true after returning to the original free scaling parameter. No arithmetic identity has yet picked one point of that parameter line.

## 4. Critical square collisions are target-defined, not source-defined

AF-421 identifies the transition `b=m^2` because two adjacent full-column saddle rates agree there. AF-422--AF-426 then analyze the finer packet balance at that collision. At exact square amplitude `a=m^2`, AF-426 proves an irreducible source-packet gap.

That negative theorem remains valid and useful, but the equality `a=m^2` enters because of the downstream saddle geometry. Rewriting it as `c=2\pi m` does not turn it into a canonical property of the original source function. A future source theorem could independently select one of these constants, but no such theorem is present in AF-412--AF-432.

## Prior-art and novelty audit

No novelty is claimed for the elementary diffeomorphism `(3)`, for transporting category/measure/dimension statements through a smooth change of coordinates, or for the general fact that double-scaling asymptotics may contain externally varied parameters. Parameter-dependent and critical double-scaling regimes are standard in asymptotic Hankel-determinant analysis.

The durable Mathia result is narrower: it audits the exact provenance chain AF-416--AF-432 and shows that the current amplitude variable is still a free probe coordinate. Therefore the existing residual/null exceptional-set theorems cannot by themselves supply the rational-prime or source discriminator sought by Arithmetic Fidelity.

No external theorem is needed for the obstruction; it follows directly from the quantified `c>0` statements in AF-416 and AF-417 and the definition `(1)` used downstream.

## Boundaries and falsification checks

- The result does **not** invalidate AF-416--AF-432. Their analytic, asymptotic, metric, and category statements remain unchanged.
- It does not say that no intrinsic source-selection rule for `c` exists. It says that none has been established in the current canonical chain.
- It does not prohibit importing a genuinely independent arithmetic construction that canonically produces `c` or `a`; such a construction would reopen the pointwise membership gate.
- A normalization is not enough merely because it gives a convenient constant. To count as source selection it must be justified independently of the downstream exceptional target and survive the relevant source symmetries or gauges.
- Square amplitudes are not source-forced merely because they are analytically distinguished saddle collisions.
- The pullback statement `(7)` uses local bi-Lipschitz equivalence on compact subsets of `(0,\infty)`; no claim is made about adding the endpoints `0` or `\infty`.
- No rational-prime discriminator, zeta-zero recovery, or implication for RH is established.

## Consequence for the research line

The next gate is earlier than the one stated after AF-432. Before attempting a Diophantine membership theorem for a supposedly distinguished amplitude, the line must first exhibit a **source-intrinsic amplitude selector**: a canonical rule deriving `c` (or `a`) from the arithmetic/source object without consulting the desired saddle cancellation or shrinking-target outcome.

Only after such a selector is proved does pointwise membership in the AF-428 critical exceptional set or AF-432 supercritical fine-hit set become mathematically capable of distinguishing the source. If no source selector exists within the current construction, further pointwise analysis of arbitrarily chosen amplitudes would refine the geometry of the probe family but would not advance arithmetic fidelity.