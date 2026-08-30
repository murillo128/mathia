# WI-029 — published near-line zero density localizes any density-scale off-line defect to the screening scale

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL + DECISIVE-NEGATIVE`. The near-critical-line zero-density theorem used below is classical literature, not a Mathia claim: Jutila sharpened Selberg's mollified estimate to an exponent coefficient arbitrarily close to `1`. The new research consequence is the coupling with WI-005/WI-006. On the natural horizontal coordinate `Y=|beta-1/2| log(T/2pi)`, the published zero-density theorem gives an exponentially decaying count tail, so any positive-density off-line population must have a positive-density core at **bounded** `Y`. But bounded `Y` is exactly the regime in which WI-006 constructs long critical-lattice blocks of off-line mirror pairs that are operator-equivalent, up to sublinear boundary cost, to on-line double zeros. Thus scalar zero-density tail information by itself does not break the double/off-line screening degeneracy and cannot supply the desired defect-to-zero bootstrap for the same single-scale compression.

## 1. The published near-line input

Let

\[
N(\sigma,T)
:=\#\{\rho=\beta+i\gamma:\ 0<\gamma\le T,\ \beta>\sigma\},
\]

counting zeros with multiplicity. Selberg proved the near-critical-line estimate

\[
N(\sigma,T)\ll
T^{1-\frac14(\sigma-\frac12)}\log T.
\tag{1}
\]

Jutila's published refinement, in the near-line range relevant here, is

\[
\boxed{
N(\sigma,T)
\ll_{\varepsilon}
T^{1-(1-\varepsilon)(\sigma-\frac12)}\log T
}
\qquad(\varepsilon>0).
\tag{2}
\]

For every fixed displacement `A` used below, `sigma=1/2+A/log(T/2pi)` lies in that near-line range for all sufficiently large `T`. Modern accounts of the near-line density problem state (2) explicitly. Simonič's explicit Selberg paper also records the historical comparison: Selberg gives coefficient `1/4`, Jutila improves it to `1-epsilon`, while Conrey announced a coefficient `8/7-epsilon` but did not publish the proof. This finding uses only the published Jutila strength, not the Conrey announcement.

Primary/historical anchors:

- Matti Jutila, **Zeros of the zeta-function near the critical line**, in *Studies in Pure Mathematics to the Memory of Paul Turán*, Birkhäuser, 1983, pp. 385--394.
- Aleksander Simonič, **Explicit zero density estimate for the Riemann zeta-function near the critical line**, *J. Math. Anal. Appl.* 491 (2020), 124303; arXiv:1910.08274. Role here: explicit Selberg theorem and modern historical audit of the Jutila/Conrey coefficients.

No novelty is claimed for (1) or (2).

## 2. Exact exponential tail on the Alpöge--Furman horizontal scale

Write

\[
L_T:=\log(T/2\pi),
\qquad
N_T:=N(2T)-N(T)
\sim \frac{T}{2\pi}L_T,
\]

and define the dyadic off-line tail

\[
D_T(A)
:=\#\left\{\rho:\ T<\gamma\le2T,
\quad |\beta-\tfrac12|L_T>A\right\},
\tag{3}
\]

again with multiplicity. Functional-equation symmetry maps a zero at `beta+i gamma` to one at `1-beta+i gamma`, so the two horizontal sides have equal multiplicity. Hence, harmlessly enlarging the ordinate range,

\[
D_T(A)
\le
2N\!\left(\frac12+\frac{A}{L_T},2T\right).
\tag{4}
\]

Apply (2) with

\[
\sigma_T=\frac12+\frac{A}{L_T}.
\]

For every fixed `A>0`,

\[
N(\sigma_T,2T)
\ll_{\varepsilon}
(2T)^{1-(1-\varepsilon)A/L_T}\log(2T).
\tag{5}
\]

Because

\[
(2T)^{-(1-\varepsilon)A/L_T}
=
\exp\!\left[-(1-\varepsilon)A
\frac{\log(2T)}{L_T}\right]
=
e^{-(1-\varepsilon)A+o(1)},
\tag{6}
\]

Riemann--von Mangoldt and (4)--(6) give the normalized tail estimate

\[
\boxed{
\limsup_{T\to\infty}
\frac{D_T(A)}{N_T}
\ll_{\varepsilon}
 e^{-(1-\varepsilon)A}.
}
\tag{7}
\]

The implied constant depends on `epsilon` but not on the fixed `A` in the stated near-line range. Consequently

\[
\boxed{
\lim_{A\to\infty}
\limsup_{T\to\infty}
\frac{D_T(A)}{N_T}=0.
}
\tag{8}
\]

Equivalently, the normalized horizontal displacement

\[
Y_\rho:=|\beta-\tfrac12|L_T
\tag{9}
\]

is exponentially tight in density. A standard diagonal choice also gives a slowly growing `A(T)->infinity` for which the zeros with `Y>A(T)` are `o(N_T)`; (8), not a particular growth rate for `A(T)`, is the robust statement needed here.

Selberg alone would already give the same qualitative conclusion with tail `exp(-A/4)`. Jutila identifies the substantially sharper published scale: any exponential rate strictly below `1` is available.

## 3. A positive-density off-line complement must have a bounded-depth core

Let

\[
E_T
:=\#\{\rho:\ T<\gamma\le2T,\ \beta\ne\tfrac12\}.
\]

Suppose, only for the purpose of characterizing a possible exceptional population, that along some sequence of heights

\[
\frac{E_T}{N_T}\ge p+o(1)
\tag{10}
\]

for a fixed `p>0`. Choose `epsilon>0` and then a fixed `A` large enough that the right side of (7), including its implied constant, is below `p/2`. Along the same sequence,

\[
\boxed{
\#\{\rho:\ T<\gamma\le2T,
\ 0<Y_\rho\le A\}
\ge (p/2+o(1))N_T.
}
\tag{11}
\]

Thus an off-line population of positive density cannot hide primarily at horizontal distances much larger than `1/log T`. Up to an arbitrarily small density tail, it is forced into a strip

\[
\boxed{
0<|\beta-\tfrac12|
\le \frac{A}{\log(T/2\pi)}
}
\tag{12}
\]

for some fixed `A`.

This is a useful structural constraint on the uncertified complement. It does **not** assert that such a positive-density off-line population exists; it says what its horizontal scale would have to be if it did.

## 4. That bounded-depth core is exactly the WI-006 screening regime

WI-005/WI-006 use precisely the same normalized coordinate

\[
y=\delta L_T,
\qquad
\delta=\beta-\tfrac12.
\]

For every fixed bounded `y`, WI-006 proves on the infinite critical vertical lattice that a simple functional-equation mirror pair

\[
\frac12+y/L_T+it_j,
\qquad
\frac12-y/L_T+it_j
\]

produces, after summing over lattice centers `t_j=t_0+j(2pi/L_T)`, **the same full compressed Weil operator** as an on-line double zero at every center:

\[
\sum_jR_j^{(y/L_T)}
=
\sum_jD_j.
\tag{13}
\]

For a block of `M` consecutive centers, uniformly for each fixed bounded `y`, WI-006 further gives

\[
\boxed{
\|Q_J^{(y/L_T)}-D_J\|_1
\ll_y \sqrt M+\log L_T.
}
\tag{14}
\]

Hence for the macroscopic blocks `M\asymp L_T` used in the adversarial construction, the replacement cost per zero tends to zero. Different long blocks may carry different bounded normalized depths, with the same sublinear boundary mechanism block by block.

Equations (8)--(12) and (13)--(14) fit together in the unfavorable direction: **classical zero density removes the very-deep count tail, but leaves the density-scale question in exactly the bounded-`y` regime where the single-scale compression has an operator-level double/off-line gauge.**

This is not a claim that the actual zeta zeros form critical lattices. The point is logical: the scalar zero-density theorem supplies no vertical-arrangement information that excludes the screenable adversary already constructed in WI-005/WI-006.

## 5. Decisive no-go for the naive zero-density bootstrap

A natural proposed bootstrap was:

1. use a zero-density theorem to show sufficiently deep off-line zeros are rare;
2. use the depth-dependent negative eigenvalue of each remaining off-line pair to charge the residual negative inertia/trace mass;
3. feed that charge back into the rank--trace remainder and iterate toward zero defect.

The first step is much stronger than merely qualitative: (7) gives an exponential count tail. But the second step still fails at density scale because bounded-depth pairs can screen collectively.

More formally, any argument whose only new arithmetic information about the off-line set is a scalar family of bounds of the form

\[
D_T(A)/N_T\le F(A)+o(1),
\qquad F(A)\to0,
\tag{15}
\]

and whose zero-side observable is asymptotically invariant under the WI-006 double/off-line replacement cannot force a positive-density bounded-`Y` population to disappear. The deep tail in (15) can be made arbitrarily small; the remaining bounded-`Y` population still admits the screenable zero-side model.

Therefore

\[
\boxed{
\text{published scalar zero density}
+
\text{the same single-scale Weil compression}
\not\Rightarrow
\text{a defect-to-zero bootstrap by horizontal depth alone}.
}
\tag{16}
\]

This closes an important weak route explicitly listed in the research objective. Zero-density information can still be useful when coupled to an input that constrains **vertical geometry**; (16) only rules out treating the horizontal tail bound itself as the missing anti-screening ingredient.

## 6. Why pair correlation is qualitatively different

The relevant prior art points to the missing type of information. Goldston--Lee--Schettler--Suriajaya prove that the full pair-correlation conjecture, without assuming RH, implies asymptotically `100%` of zeta zeros are both simple and on the critical line. Their mechanism uses **horizontal multiplicity** together with vertical pair statistics. In particular, the horizontal-multiplicity ledger explicitly confronts the same combinatorial ambiguity that appears here: two zeros at one ordinate may be an on-line double or a symmetric simple off-line pair.

Thus full PCC is not merely a stronger numerical zero-density estimate. It supplies vertical-statistical structure capable of ruling out a positive-density exceptional horizontal-multiplicity population. That is qualitatively the sort of information missing from (15).

This also prevents a terminology trap in recent follow-up drafts. A hypothesis described as convergence of a bounded-depth horizontal profile or as a `zero-density convergence` assumption is stronger than the classical Selberg/Jutila theorem used here. Jutila gives tail tightness as `A->infinity`; it does **not** say that the mass at every fixed nonzero normalized depth tends to zero.

## 7. A secondary threshold: published zero density is also borderline for raw depth weights

There is a related reason not to over-read (7). For the ideal flat window, WI-005 computes the isolated-pair negative magnitude at normalized depth `y` as

\[
r(y)-1
=
\frac{\sinh y}{y}-1
\sim \frac{e^y}{2y}.
\tag{17}
\]

Jutila supplies tail decay at every exponent `c<1`, but not a published `c>1`. Therefore (7) controls normalized exponential moments `e^{\theta Y}` for every fixed `theta<1`, while it is **insufficient by itself** to control a raw `e^Y/Y` isolated-pair charge uniformly by tail integration. The announced but unpublished Conrey coefficient `8/7` would cross that scalar integrability threshold if available, but it still would not remove the collective screening identity (13).

This is a secondary observation, not an input to (16): the primary no-go already follows from the bounded-depth screening geometry.

## 8. Prior-art and novelty audit

Literature-backed inputs:

- Selberg's coefficient `1/4` near-line zero-density theorem.
- Jutila's published improvement to every coefficient `1-epsilon`.
- functional-equation symmetry and Riemann--von Mangoldt.
- Goldston--Lee--Schettler--Suriajaya's conditional PCC-to-density-one theorem via horizontal multiplicity.

Previously established Mathia input:

- WI-005/WI-006's exact critical-lattice screening and double/off-line operator replacement for fixed bounded normalized depth.

New exact deductions in this finding:

- the rescaling of Jutila's theorem to the Alpöge--Furman coordinate, equations (7)--(8);
- the bounded-depth-core consequence (11)--(12);
- the synthesis showing that published scalar zero-density information localizes any density-scale off-line obstruction **into**, rather than out of, the existing screening regime;
- the corresponding no-go (16) for a depth-only zero-density bootstrap using an observable invariant under WI-006 replacement.

A bounded search found no source making this specific zero-density/screening synthesis. No priority claim is made from absence of a search hit.

## 9. Falsification and next target

The finding would be invalidated by any of the following:

- the quoted Jutila exponent failing in the near-line range containing `sigma=1/2+A/L_T` for fixed `A`;
- a normalization error in passing from (2) to the dyadic tail (7);
- a failure of functional-equation symmetry at fixed ordinate/multiplicity;
- a hidden hypothesis in WI-006 that excludes the fixed bounded-`Y` regime used here.

Those points have been checked against the cited theorem statements and WI-006's exact formulas. The conclusion is deliberately limited: it does not claim actual zeta zeros realize the screening lattice.

The next anti-screening target should constrain the **vertical arrangement of the bounded-depth core**, not its horizontal tail. Two concrete forms would suffice to escape this obstruction:

1. prove an unconditional local-spacing/correlation statement showing that a positive-density bounded-`Y` off-line population cannot organize into long near-critical screening blocks up to `o(N)` edits; or
2. construct a cross-scale / wider-support observable that changes by an order-one amount per zero under the permanent WI-006 double-to-off-line replacement test.

Until one of those ingredients is available, classical zero-density improvement alone is not the missing bootstrap.