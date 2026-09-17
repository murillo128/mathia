# AF-403 — Complete confluent flags globalize strict translation total positivity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TARGET-FIDELITY` · `TOTAL-POSITIVITY` · `ECT` · `CONFLUENT-CERTIFICATE` · `STRICT-INTERIOR` · `NO-NOVELTY-CLAIM`

## Claim

Let `r>=1` and let

\[
f\in C^{2r-2}(\mathbb R).
\]

For `1<=m<=r`, define the oriented fully confluent translation determinant

\[
H_m(t)
:=
(-1)^{m(m-1)/2}
\det\!\left(f^{(i+j)}(t)\right)_{i,j=0}^{m-1}.
\tag{1}
\]

Assume the complete initial confluent flag is strictly positive:

\[
H_m(t)>0
\qquad
\text{for every }t\in\mathbb R
\text{ and every }1\le m\le r.
\tag{2}
\]

Then the translation kernel

\[
K_f(x,y)=f(x-y)
\tag{3}
\]

is **strictly totally positive through order `r`**: for every `1<=m<=r` and every strictly increasing tuples

\[
x_1<\cdots<x_m,
\qquad
y_1<\cdots<y_m,
\]

one has

\[
\boxed{
\det\bigl(f(x_i-y_j)\bigr)_{i,j=1}^m>0.
}
\tag{4}
\]

Thus, on the strict confluent source class `(2)`, the entire continuum of arbitrary row/column placements is target-faithfully compressed to the `r` one-variable functions

\[
H_1,\ldots,H_r.
\]

The mechanism is a two-step extended-complete-Chebyshev (`ECT`) collocation argument. It is classical Chebyshev-system mathematics, and a July 2026 de Bruijn--Newman-kernel proof uses exactly this complete-confluent-flag-twice mechanism through order four. No novelty is claimed for the mechanism or theorem pattern.

The Arithmetic Fidelity consequence is nevertheless material: the current higher-order frontier does **not** require an additional finite-placement or global-topology resource inside the strict confluent interior. Once the complete local flag is strictly positive, arbitrary placement is forced. Any higher-order residual obstruction must therefore come from proving the local confluent signs, from zeros/degenerate strata where strictness fails, or from an observation scheme that does not retain the full flag.

## First ECT pass: collision data recover every derivative-collocation packet

Fix `x\in\mathbb R`. For `j=0,\ldots,r-1`, define functions of `y`

\[
\phi_j(y)=\partial_x^jK_f(x,y)=f^{(j)}(x-y).
\tag{5}
\]

For each `m<=r`, the initial Wronskian of

\[
\phi_0,\ldots,\phi_{m-1}
\]

with respect to `y` is

\[
\begin{aligned}
W_y(\phi_0,\ldots,\phi_{m-1})(y)
&=
\det\!\left(\partial_y^i\phi_j(y)\right)_{i,j=0}^{m-1}\\
&=
\det\!\left((-1)^i f^{(i+j)}(x-y)\right)_{i,j=0}^{m-1}\\
&=
(-1)^{m(m-1)/2}
\det\!\left(f^{(i+j)}(x-y)\right)_{i,j=0}^{m-1}\\
&=H_m(x-y)>0.
\end{aligned}
\tag{6}
\]

The classical Wronskian criterion for an `ECT` system therefore applies on every compact interval containing any finite packet of `y`-nodes. Hence, for every

\[
y_1<\cdots<y_m,
\]

the ordered collocation determinant of the initial system is positive. After transposing the collocation matrix, this says

\[
D_m(x;y_1,\ldots,y_m)
:=
\det\!\left(f^{(i-1)}(x-y_j)\right)_{i,j=1}^{m}
>0.
\tag{7}
\]

One can see the sign without importing a convention from the `ECT` theorem. The ordered-node chamber is connected, the Chebyshev property prevents the determinant from vanishing there, and when the nodes coalesce its sign is fixed by the positive Wronskian in `(6)` and the positive Vandermonde orientation. Thus `(7)` has the stated positive sign globally.

So the one-variable fully confluent flag has already recovered all ordered **one-sided derivative-collocation** packets.

## Second ECT pass: derivative-collocation packets recover arbitrary translation minors

Now freeze an arbitrary ordered column packet

\[
y_1<\cdots<y_r
\]

and define functions of `x`

\[
g_j(x)=f(x-y_j),
\qquad j=1,\ldots,r.
\tag{8}
\]

For every initial subsystem `g_1,\ldots,g_m`, its Wronskian with respect to `x` is exactly the determinant obtained in the first pass:

\[
\begin{aligned}
W_x(g_1,\ldots,g_m)(x)
&=
\det\!\left(g_j^{(i-1)}(x)\right)_{i,j=1}^{m}\\
&=
D_m(x;y_1,\ldots,y_m)>0.
\end{aligned}
\tag{9}
\]

Thus

\[
g_1,\ldots,g_r
\]

is itself an `ECT` system. Applying the collocation theorem a second time gives, for every ordered row packet

\[
x_1<\cdots<x_m,
\]

\[
\det\!\left(g_j(x_i)\right)_{i,j=1}^{m}
=
\det\!\left(f(x_i-y_j)\right)_{i,j=1}^{m}>0.
\tag{10}
\]

This proves `(4)`.

The information flow is therefore exact and unusually strong:

\[
\text{complete fully confluent flag}
\Longrightarrow
\text{all derivative-collocation packets}
\Longrightarrow
\text{all ordinary translation packets}.
\tag{11}
\]

No sampling mesh, arbitrary column geometry, or additional global placement invariant remains once the strict complete flag is retained.

## Relation to the order-three curvature results

AF-393 and AF-394 become the first nontrivial instance of this general mechanism in the strict interior.

For a positive profile write

\[
g=\log f,
\qquad
q=-g''.
\tag{12}
\]

Direct differentiation gives

\[
\frac{H_1}{f}=1,
\qquad
\frac{H_2}{f^2}=q,
\tag{13}
\]

and

\[
\frac{H_3}{f^3}
=
2q^3-qq''+(q')^2.
\tag{14}
\]

Where `q>0`, `(14)` is

\[
\frac{H_3}{f^3}
=
q^2\left(2q-(\log q)''\right).
\tag{15}
\]

Hence the AF-393 strict positive-curvature hypotheses

\[
q>0,
\qquad
(\log q)''<2q
\tag{16}
\]

are precisely strict positivity of the initial confluent flag through order three. AF-403 explains abstractly why those local conditions force every global order-three placement: they are the `ECT` certificate required by the two-pass argument.

This also clarifies why AF-394 still needs a global connected-support datum in the nonstrict regime. When `q` reaches zero, `H_2` reaches zero, the strict `ECT` hypothesis breaks, and the local-to-global implication above is no longer available. AF-394's curvature-component topology is therefore a **boundary-stratum phenomenon**, not evidence that strict higher-order translation positivity intrinsically carries an additional placement-topology variable.

## Higher-order consequence

For every fixed `r`, strict translation total positivity can now be attacked through the finite local hierarchy

\[
H_1(t)>0,\ldots,H_r(t)>0
\qquad(t\in\mathbb R).
\tag{17}
\]

The complexity has not disappeared; it has moved. `H_m` uses derivatives of `f` through order `2m-2`, so the local analytic certificate becomes rapidly more structured as `m` grows. At order four the new condition is a sixth-derivative local inequality for `f` (equivalently a condition involving `q=-(\log f)''` through its fourth derivative). But there is no separate arbitrary-node search once the entire strict flag is known.

This sharply narrows the live question recorded after AF-394. The productive higher-order frontier is now:

- determine usable structural criteria for the signs of the confluent hierarchy `H_m`;
- understand which parts of that hierarchy survive arithmetic compression or sparse sampling;
- classify what replaces strict `ECT` propagation when one or more `H_m` vanish;
- determine whether the nonstrict/degenerate strata leave finite global/topological residues analogous to AF-394;
- in Riemann-facing kernels, test the actual local confluent hierarchy before spending effort on arbitrary placement.

In particular, searching directly for an additional finite-placement invariant in a region where all `H_m` are already strictly positive is redundant.

## Arithmetic-fidelity interpretation

The target in this finding is not recovery of the source function `f`; it is recovery of the Boolean/ordered target property

\[
K_f\in STP_r.
\]

The compression

\[
f
\longmapsto
(H_1,\ldots,H_r)
\tag{18}
\]

is target-faithful on the source class defined by strict positivity of the retained flag: the retained local data force every omitted ordinary minor to have the correct sign.

This is a concrete instance of the line's main resource principle. A severe compression can be exact when the source class carries enough rigidity. Here the resource is not arithmetic provenance or a marking; it is **complete strict Chebyshev structure**. The omitted geometry is reconstructed by variation-diminishing/zero-count rigidity rather than stored explicitly.

The result also separates three notions that should not be conflated:

1. **source identification:** `(H_1,\ldots,H_r)` does not determine `f` uniquely;
2. **target fidelity:** the flag does determine strict total positivity through order `r` under `(2)`;
3. **stable recovery:** no quantitative conditioning statement follows merely from positivity, especially when some `H_m` approach zero.

Thus this is a target-faithful certificate, not an injective representation and not a robustness theorem.

## Prior-art and novelty audit

The engine of the proof is classical. Karlin and Studden's theory of Tchebycheff systems gives the Wronskian characterization of extended complete Chebyshev systems and the corresponding ordered collocation property. Karlin's total-positivity monograph supplies the surrounding kernel theory. Modern statements of the same criterion explicitly formulate an `ECT` system as equivalent to positivity of all initial Wronskians under the usual smoothness hypotheses.

More decisively, a current 22 July 2026 de Bruijn--Newman-kernel paper package/research note uses the **same two-pass mechanism**: positivity of the complete fully confluent flag `H_1,\ldots,H_4`, one `ECT` collocation in one variable, then a second `ECT` collocation in the other variable, to conclude global `PF_4`. Therefore neither the two-pass reduction nor its translation-kernel application is being claimed as new here.

Relevant sources:

- Samuel Karlin and William J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Interscience/Wiley, 1966. Role: classical `ECT`/Wronskian and collocation theory.
- Samuel Karlin, *Total Positivity, Vol. I*, Stanford University Press, 1968. Role: classical total-positivity kernel framework.
- R. A. Zalik, “Cebysev and Weak Cebysev Systems,” in *Total Positivity and Its Applications*, Mathematics and Its Applications 359, 1996, pp. 301--332. Role: survey bridge between Chebyshev-system and total-positivity language.
- “The de Bruijn-Newman kernel stops at order four,” kenan.works, 22 July 2026, with attached complete paper/verifier package. Role: recent independent use of exactly the complete-confluent-flag-twice `ECT` argument for a Riemann-adjacent translation kernel.
- Wojciech Michałowski, “On the Pólya Frequency Order of the de Bruijn--Newman Kernel: Certified Failure at Order Five,” arXiv:`2602.20313`, v2 20 July 2026. Role: certified order-five failure and the immediately preceding state in which global `PF_4` was still open.

The durable contribution here is therefore **portfolio correction and abstraction**, not a novelty claim: AF-403 identifies the exact classical rigidity mechanism that eliminates the apparent higher-order placement problem in the strict interior and states the resulting information-compression boundary in Arithmetic Fidelity language.

## Boundaries and falsification checks

- Strict positivity of the **complete initial flag** is load-bearing. Positivity of only `H_r`, or of only a selected subset of lower orders, does not supply the two `ECT` systems used in the proof.
- The theorem is sufficient, not claimed necessary for ordinary `STP_r`. Ordinary strict minors may converge to zero under collisions, so `STP_r` does not automatically imply strict positivity of every confluent determinant.
- Replacing `(2)` by `H_m>=0` is not justified by this argument. At zeros of a Wronskian the `ECT` step can fail, and AF-386--AF-394 already show that nonstrict boundary strata can retain additional support/topology information.
- The theorem compresses **node placement**, not determinant order. To establish all-order Pólya-frequency behavior one still needs the complete hierarchy for unbounded `m`; AF-372 remains the obstruction to any fixed-order cutoff on the unrestricted class.
- No arithmetic discriminator is created. The argument is source-independent and applies to any smooth translation profile satisfying `(2)`. A Riemann-facing use must prove the relevant confluent signs from the arithmetic source rather than importing them as assumptions.
- No conditioning statement is asserted. If `\inf_t H_m(t)` degenerates, exact sign fidelity can coexist with arbitrarily poor robustness.
- No RH consequence is claimed.