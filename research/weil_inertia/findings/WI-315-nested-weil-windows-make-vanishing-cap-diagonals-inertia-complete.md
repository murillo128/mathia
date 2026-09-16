# WI-315 — Nested Weil windows make every vanishing-cap diagonal inertia-complete

**Status:** `EXACT-DERIVED + CLASSICAL-MINMAX + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-302, WI-307, WI-311, WI-314.

WI-314 proves that, at one fixed outer aperture, the strict comparison count below `-1/2` recovers the source negative index as the capped-tail error tends to zero. Its Section 6 then gives an abstract one-dimensional countermodel showing that this need not survive a diagonal limit if the source form itself is allowed to change arbitrarily with the aperture.

That countermodel is valid as an abstract warning but **does not model the actual compact-support Weil family**. The physical outer-aperture spaces

\[
\mathcal D_L=C_c^\infty((-L,L);\mathbf C)
\]

are nested restrictions of one and the same global Weil quadratic form `Q`. Once a negative compactly supported test appears at some finite aperture, its Rayleigh quotient is frozen: enlarging the aperture does not make that old negative direction shallower. This nesting is enough to remove the diagonal zero-margin obstruction completely.

More generally, let `L_j -> infinity` and let `delta_j -> 0`. At each aperture suppose a source-exact capped-tail decomposition has

\[
Q=\widehat{\mathcal D}_j+\widehat{\mathcal T}_j
\qquad\text{on }\mathcal D_{L_j},
\]

with

\[
\left(\frac12-\delta_j\right)I
\preceq\widehat{\mathcal T}_j
\preceq\frac12I.
\]

Then the strict comparison counts below `-1/2` recover the **entire compact-support negative index** along that single diagonal. If that index is finite, the counts are eventually exactly equal to it; if it is infinite, the counts tend to infinity. No aperture-uniform negative-depth estimate, no cofinal saturation at each fixed aperture, no commutation, and no spectral discreteness are required.

For the RH objective this has a particularly sharp consequence. Weil's criterion is formulated on compactly supported smooth tests. Therefore, if RH is false, there is one fixed finite-support witness `f` with `Q(f)<0`; every cofinal aperture sequence eventually contains that same `f`, with the same fixed negative margin, and every cap sequence `delta_j -> 0` eventually resolves it below the comparison threshold `-1/2`. Thus one vanishing-cap/cofinal-aperture diagonal is already sign-complete. The remaining difficulty is not limit order: it is to prove, from independent source-valid information, that the corresponding comparisons have no spectrum below `-1/2`.

This corrects the application-level scope of WI-314 §6--§9. WI-314's fixed-aperture theorem and its abstract varying-source countermodel remain mathematically correct; what fails is treating that arbitrary varying-source countermodel as an obstruction for the nested compact-window restrictions of the actual Weil form.

## 1. The aperture family is one quadratic form on nested domains

The source normalization audited in WI-302 is

\[
Q(f)=\mathcal P(f)
+\frac1{2\pi}\int_{\mathbf R}A(t)|F_f(t)|^2\,dt
-\sum_{n\ge2}\frac{2\Lambda(n)}{\sqrt n}H_f(\log n),
\tag{1}
\]

with domain restricted, for a compact-window problem, to

\[
\mathcal D_L=C_c^\infty((-L,L);\mathbf C).
\tag{2}
\]

If `L_1<L_2`, then

\[
\mathcal D_{L_1}\subset\mathcal D_{L_2},
\tag{3}
\]

and the value of `Q(f)` for `f in D_{L_1}` is identical whether it is regarded as a test in `D_{L_1}` or `D_{L_2}`. Nothing in (1) depends on the aperture after `f` itself is fixed.

The apparent growth of the active prime-power list with `L` does not change this fact. If `f` is supported in `(-L_0,L_0)`, then its autocorrelation satisfies

\[
H_f(x)=0\qquad(|x|\ge2L_0),
\tag{4}
\]

so prime powers newly admitted by a larger bookkeeping aperture contribute exactly zero to the old vector. The same observation applies to the localization identities used in WI-307--WI-311: the aperture chooses a domain and a comparison construction, not a new source quadratic form on vectors that were already present.

Write

\[
\mathcal D_c:=\bigcup_{L>0}\mathcal D_L=C_c^\infty(\mathbf R;\mathbf C).
\tag{5}
\]

Define the compact-support variational negative index

\[
\nu_c(Q)
:=
\sup\left\{
\dim V:
V\subset\mathcal D_c,\quad
Q[v]<0\text{ for every }0\ne v\in V
\right\}.
\tag{6}
\]

This is an extended nonnegative integer. It deliberately stays on the common smooth core; no closure or compact-resolvent statement is needed for the argument below.

## 2. Vanishing-cap diagonal theorem

Let `L_j -> infinity`. For each `j`, suppose there is an exact decomposition on `D_{L_j}`

\[
Q=\widehat{\mathcal D}_j+\widehat{\mathcal T}_j
\tag{7}
\]

with

\[
\left(\frac12-\delta_j\right)I
\preceq
\widehat{\mathcal T}_j
\preceq
\frac12I,
\qquad
\delta_j>0,
\qquad
\delta_j\to0.
\tag{8}
\]

No monotonicity of `L_j` or `delta_j` is assumed; only the two limits are needed. Put

\[
E_j:=\frac12I-\widehat{\mathcal T}_j.
\tag{9}
\]

Then

\[
0\preceq E_j\preceq\delta_j I,
\qquad
\boxed{
\widehat{\mathcal D}_j+\frac12I=Q+E_j.
}
\tag{10}
\]

Define the strict fixed-threshold count on the smooth aperture domain by

\[
d_j
:=
\sup\left\{
\dim V:
V\subset\mathcal D_{L_j},\quad
\widehat{\mathcal D}_j[v]<-\frac12\|v\|^2
\text{ for every }0\ne v\in V
\right\}.
\tag{11}
\]

Then

\[
\boxed{
d_j\longrightarrow\nu_c(Q)
}
\tag{12}
\]

in the extended nonnegative integers. Explicitly:

- if `nu_c(Q)=k<infinity`, then `d_j=k` for every sufficiently large `j`;
- if `nu_c(Q)=infinity`, then for every finite `m`, one has `d_j>=m` for every sufficiently large `j`.

The statement applies directly to the WI-311 capped-tail family: there

\[
\delta_j=\frac1{4N_j}+\frac{\epsilon_j}{2},
\tag{13}
\]

so any choice with `N_j -> infinity`, `epsilon_j -> 0`, and `L_j -> infinity` is a sign-complete diagonal, irrespective of how slowly the cap is saturated relative to the aperture.

## 3. Proof

The upper bound is immediate from positivity of the cap defect. If a subspace `V subset D_{L_j}` is counted by `d_j`, then by (10)

\[
(Q+E_j)[v]<0
\qquad(0\ne v\in V).
\]

Since `E_j` is positive semidefinite,

\[
Q[v]\le(Q+E_j)[v]<0,
\]

so `V` is also a source-negative subspace. Therefore

\[
\boxed{d_j\le\nu_c(Q)}
\tag{14}
\]

for every `j`. In particular the fixed threshold has no false positives even while the aperture varies.

For the converse, take any finite-dimensional source-negative subspace

\[
V\subset\mathcal D_c,
\qquad
Q[v]<0\quad(0\ne v\in V).
\tag{15}
\]

A finite basis of `V` consists of compactly supported functions, so there is one finite `L_V` with

\[
V\subset\mathcal D_{L_V}.
\tag{16}
\]

On the unit sphere of `V`, the restricted quadratic form is continuous and strictly negative. Compactness therefore gives a fixed number

\[
\eta_V
:=-\max_{\substack{v\in V\\ \|v\|=1}}Q[v]
>0
\tag{17}
\]

such that

\[
Q[v]\le-\eta_V\|v\|^2
\qquad(v\in V).
\tag{18}
\]

Because `L_j -> infinity` and `delta_j -> 0`, eventually both

\[
L_j>L_V,
\qquad
\delta_j<\eta_V.
\tag{19}
\]

For such `j`, equations (10), (18), and `E_j<=delta_j I` give

\[
\begin{aligned}
\left(\widehat{\mathcal D}_j+\frac12I\right)[v]
&=Q[v]+E_j[v]\\
&\le-(\eta_V-\delta_j)\|v\|^2<0
\end{aligned}
\tag{20}
\]

for every nonzero `v in V`. Hence

\[
d_j\ge\dim V
\tag{21}
\]

for all sufficiently large `j`.

If `nu_c(Q)=k<infinity`, choose a `k`-dimensional negative subspace and combine (14) with (21) to get eventual equality. If `nu_c(Q)=infinity`, apply (21) successively to negative subspaces of arbitrary finite dimension. This proves (12).

The proof is purely variational. The operators need not commute; the negative spectrum need not be discrete; the cap defects may point in unrelated directions for different `j`; and no eigenvector tracking is required.

## 4. Why WI-314's diagonal countermodel is not a Weil-window countermodel

WI-314 §6 takes

\[
Q_L=-\frac{\delta_L}{2}I,
\qquad
\widehat{\mathcal T}_L=\left(\frac12-\delta_L\right)I,
\tag{22}
\]

so the sole source-negative Rayleigh quotient itself tends to zero with `delta_L`. This proves exactly what it claims for an arbitrary family of unrelated source forms: scalar cap control cannot resolve a negative direction if the underlying source is allowed to make that same direction shallower at the same time.

But (22) violates the consistency property (3) of the actual aperture restrictions. In the Weil family, once a fixed `v in D_{L_0}` has

\[
Q[v]=-\eta\|v\|^2<0,
\tag{23}
\]

that identity remains unchanged in every `D_L` with `L>=L_0`. Enlarging the aperture can introduce *new* negative directions with smaller margins, but it cannot erase or shallow the old one. For strict sign detection, one persistent old witness is enough.

Accordingly, a sequence of newly appearing negative eigenvalues whose depths tend to zero is not itself an escape. Even if every new mode is shallower than the contemporaneous `delta_j`, any earlier finite-dimensional negative packet remains present with its original finite-dimensional margin and is eventually detected when `delta_j` drops below that fixed margin.

This distinction also separates the compact-window problem from Bombieri's coefficient-space truncation issue recorded in WI-236. A moving finite coordinate truncation can exhibit coefficient mass escape and shrinking spectral margins. The present theorem does not assert that those matrices are principal restrictions of the compact-window form in the sense needed here. It uses only the literal nesting of compactly supported test spaces for the same global Weil functional.

## 5. RH consequence and the remaining gate

Bombieri's classical formulation states that the Weil quadratic functional is positive semidefinite on the compactly supported test class if and only if RH is true. In the notation above,

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\nu_c(Q)=0.
}
\tag{24}
\]

Combining (12) and (24), every source-exact diagonal satisfying (7)--(8), `L_j -> infinity`, and `delta_j -> 0` obeys

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
d_j\to0.
}
\tag{25}
\]

Because the `d_j` are integer-valued and a false RH supplies one fixed compact negative witness, the reverse direction is stronger than a subsequence statement: if RH is false, then

\[
\boxed{d_j\ge1\quad\text{for every sufficiently large }j.}
\tag{26}
\]

If RH is true, positivity of `Q` and `E_j>=0` give `d_j=0` for every `j`.

Equations (25)--(26) are **not an RH proof**. WI-311 constructs decompositions with arbitrarily small `delta_j`, but it does not prove

\[
\widehat{\mathcal D}_j\succeq-\frac12I
\tag{27}
\]

for any cofinal aperture family. Establishing (27), or otherwise proving `d_j=0` eventually from source-valid arithmetic/operator information, remains the entire hard step. The present result only shows that a separate uniform source-negative margin theorem is *not* required to justify the diagonal passage once such a comparison estimate exists.

Thus the capped-tail branch has a cleaner falsifiable target than WI-314 left it with:

\[
\boxed{
\text{construct one cofinal WI-311 diagonal and rule out comparison spectrum below }-1/2.
}
\tag{28}
\]

There is no additional limit-order loophole after (28): if it can be proved, Weil's criterion closes the argument.

## 6. Prior-art and novelty audit

The load-bearing source facts are classical. Bombieri's *Remarks on Weil's quadratic functional in the theory of prime numbers, I* (2000) states that the Weil quadratic functional is positive semidefinite if and only if RH and explicitly studies its restriction to functions supported in a prescribed interval. That is the relevant classical precedent for viewing the compact-window problems as restrictions of one global form rather than unrelated forms.

The variational step is elementary finite-dimensional compactness plus monotonicity under a positive bounded perturbation. General monotone-convergence results for increasing variational subspaces are classical; for example R. D. Brown's work on monotone convergence for variational triples treats the broader approximation framework. No novelty is claimed for that functional-analytic principle.

Recent compact-window work likewise treats a single profile obtained by restricting the Weil form to windows `[-L,L]`; it does not supply the capped-tail diagonal theorem above. A targeted audit around Weil compact-window positivity, increasing support domains, min--max convergence, bounded perturbations, and capped/clipped localization tails found no source stating the exact fixed-`-1/2` diagonal recovery (12) for the WI-311 source-exact decomposition. Search absence is not a priority claim.

The durable new content is the line-local deduction that the **actual nested Weil domains invalidate the only diagonal countermodel left in WI-314**, together with the exact extended-index convergence (12) and its RH consequence (25). This is a structural correction, not new arithmetic input.

### Validation boundary

The theorem is exact on the common smooth compact-support core. It does not identify the full negative spectral index of any completed global Hilbert-space realization unless the corresponding form-core and closure hypotheses are supplied separately. Those extra statements are unnecessary for (25), because Weil's RH criterion itself is already a compact-support test criterion.

No claim is made that Liu's recent `17/16` computational certificate is independently validated, no new simple-zero percentage is obtained, and no global Weil positivity estimate is imported. WI-302 is used only for the source normalization/domain, while WI-311 supplies the exact capped-tail order interval.

## Research consequence

The zero-spectral-margin issue must now be kept separate for two different truncation geometries. It remains meaningful for Bombieri-style moving coordinate truncations, where a negative mode can move outward in coefficient space. It is **not** a barrier to a cofinal chain of physical compact-support apertures equipped with WI-311 cap errors tending to zero: old negative compact witnesses persist with fixed depth.

For the current capped-tail program, the next useful result is therefore not another abstract aperture-uniform margin estimate. It is a source-valid estimate on the comparison itself, strong enough to show that one cofinal family satisfies `d_j=0`, equivalently that no test in that family falls strictly below the fixed cap threshold. If such an estimate cannot hold, the right negative result is an explicit source-compatible sequence producing deep comparison modes, not an arbitrary varying-source scalar model.