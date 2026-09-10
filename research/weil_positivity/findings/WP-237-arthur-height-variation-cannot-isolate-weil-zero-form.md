# WP-237 — Arthur-height variation cannot isolate the Weil zero form: the T-invariant explicit distribution cancels or survives intact

**Status:** `EXACT-DERIVED + MAASS-SELBERG-POSITIVE-CONTROL + RELATIVE-TRUNCATION-NO-GO + ALL-LINEAR-HEIGHT-FILTER-NO-GO + MATCHED-SCATTERING-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

The Maaß–Selberg/Arthur-truncation route is much closer to the Weil Positivity mandate than the local positive completions ruled out earlier: for positive-type tests it starts from an independently positive global Hilbert-space distribution, and the same continuous spectral term contains the logarithmic derivative of a global scattering normalizer whose explicit formula contains the nontrivial zero divisor, finite-prime terms, and archimedean/polar terms.

However, the most canonical operation suggested by `CLUE-maass-selberg-remainder-sign-interface` — comparing two or more Arthur truncation heights — has an exact structural obstruction. In the Riemann-zeta specialization of Wong's Maaß–Selberg formula, **every explicit-formula constituent carried by the logarithmic derivative has exactly the same dependence on the truncation height: none at all**. Consequently, a linear operation acting only on the height variable either cancels the whole explicit-formula distribution, including the zero divisor, or retains it as one inseparable block with the finite-prime and archimedean companions.

Thus relative subtraction between canonical heights cannot project the positive truncated distribution onto the Weil zero form. This is an exact no-go for height-only linear filtering, not a no-go for a genuinely new internal geometric projection of the continuous spectral space.

## 1. The positive truncated family has a common T-independent explicit-formula block

The source is Tian An Wong, *Explicit formulas for the spectral side of the trace formula of SL(2)*, Acta Arith. 195 (2020), 149–175, arXiv:1608.02296. Wong's Lemma 5.1 states that Arthur's truncated continuous spectral distribution is positive definite. In the rank-one zeta specialization, the proof of Corollary 1.3 gives, for the positive-type test class used there,

\[
Q_T(g)
=
 g(1)\log T
-
\frac{1}{4\pi}
\int_{-\infty}^{\infty}
\frac{m'}{m}(it)\widehat g(it)\,dt
+
\frac{1}{4\pi i}
\int_{-\infty}^{\infty}
m(it)\widehat g(it)\frac{T^{it}}{t}\,dt,
\tag{1}
\]

and

\[
Q_T(g)\ge 0.
\tag{2}
\]

Here `T` is the Arthur truncation height and `m` is the scalar scattering/intertwining normalizer in Wong's conventions. The important point for the present argument is not a sign convention but the exact separation of the `T` dependence in (1).

Define

\[
D(g)
:=
-
\frac{1}{4\pi}
\int_{-\infty}^{\infty}
\frac{m'}{m}(it)\widehat g(it)\,dt
\tag{3}
\]

and

\[
B_T(g)
:=
 g(1)\log T
+
\frac{1}{4\pi i}
\int_{-\infty}^{\infty}
m(it)\widehat g(it)\frac{T^{it}}{t}\,dt.
\tag{4}
\]

Then the entire positive family has the exact affine decomposition

\[
\boxed{Q_T(g)=D(g)+B_T(g).}
\tag{5}
\]

Wong's Theorem 1.1 is precisely an explicit formula for the `T`-independent distribution `D`. In particular it decomposes into the nontrivial-zero contribution together with finite-prime, conductor/polar, and archimedean terms. Schematically, with all source normalizations absorbed into the named pieces,

\[
D(g)=W(g)+P_{\rm fin}(g)+A_\infty(g)+C_{\rm pol}(g).
\tag{6}
\]

The exact formulas in Wong are stronger than the schematic notation (6); the notation is used only to make the height argument transparent. Crucially, **all four terms in (6) occur inside the same `T`-independent block (3)**.

This is the sign gap already identified in the clue and in the bounded read of `PL-253`: positivity of `Q_T` yields a lower bound for `W`, but does not by itself make `W` positive.

## 2. Relative truncation cancels the zero divisor together with everything else in D

Take two admissible source-fixed heights `T_1,T_2`. Subtracting (5) gives

\[
\boxed{
Q_{T_2}(g)-Q_{T_1}(g)
=
B_{T_2}(g)-B_{T_1}(g).
}
\tag{7}
\]

The complete distribution `D(g)` cancels identically. By (6), this means that the nontrivial-zero functional does not survive the relative-height operation:

\[
W(g),\;P_{\rm fin}(g),\;A_\infty(g),\;C_{\rm pol}(g)
\quad\text{all cancel together.}
\tag{8}
\]

Therefore even if one could prove an independent sign for the relative quantity on the right of (7), that sign would not be a sign theorem for the zero divisor: the target functional has disappeared from the relative distribution.

This kills the most literal candidate in `CLUE-maass-selberg-remainder-sign-interface`: **a relative subtraction between two canonical Arthur truncation heights cannot isolate the Weil zero form**, because height variation has no resolution inside the explicit-formula block that contains it.

The conclusion does not depend on whether `T_1` and `T_2` are numerically special, geometrically preferred, or chosen from a discrete canonical family. It follows before any choice of heights is made.

## 3. The obstruction covers every linear filter in the height variable

The same argument is not restricted to a two-height difference. Let

\[
\mathcal L_T
\tag{9}
\]

be any linear functional acting only on the `T` dependence of the family (5), defined at least on the constant function `1` and on the boundary profiles in (4). This includes finite linear combinations of values, relative differences, derivatives or finite differences in `log T`, and linear averaging/regularization schemes for which the expressions exist.

Because `D(g)` is constant in `T`, linearity gives

\[
\boxed{
\mathcal L_T[Q_T(g)]
=
\mathcal L_T[1]D(g)
+
\mathcal L_T[B_T(g)].
}
\tag{10}
\]

There are only two cases.

If

\[
\mathcal L_T[1]=0,
\tag{11}
\]

then the entire explicit-formula block vanishes:

\[
\mathcal L_T[Q_T(g)]=\mathcal L_T[B_T(g)].
\tag{12}
\]

In particular `W(g)` has been eliminated.

If instead

\[
\mathcal L_T[1]\ne0,
\tag{13}
\]

then `D(g)` survives only as the scalar multiple `\mathcal L_T[1]D(g)`. Its internal decomposition (6) is unchanged:

\[
\mathcal L_T[1]D(g)
=
\mathcal L_T[1]
\bigl(W+P_{\rm fin}+A_\infty+C_{\rm pol}\bigr)(g).
\tag{14}
\]

No height-only linear filter can change the coefficient of `W` relative to the finite-prime and archimedean/polar constituents because all of them occupy the same constant `T` mode.

For a finite combination this becomes especially explicit. If

\[
R(g)=\sum_{j=1}^N a_jQ_{T_j}(g),
\tag{15}
\]

then

\[
R(g)
=
\left(\sum_j a_j\right)D(g)
+
\sum_j a_jB_{T_j}(g).
\tag{16}
\]

Thus `sum a_j=0` kills the whole explicit formula, while `sum a_j != 0` retains all of it. There is no third linear-height case in which the zero divisor survives but its companions do not.

## 4. Differentiating, averaging, or renormalizing T does not evade the block obstruction

Several natural variants reduce to (10).

A derivative in `log T` satisfies `dD/d(log T)=0`; it probes only the truncation/boundary response. Higher derivatives do the same. Finite differences are the discrete version of the same zero-mass filter.

An average over several truncation heights with total weight one preserves `D` exactly, and therefore preserves all of its explicit-formula constituents together. Changing the averaging kernel cannot distinguish the zero term from the prime or Gamma terms unless the operation uses additional information beyond the height profile.

A renormalized limit also does not by itself produce the desired projection. Wong notes that the oscillatory term has a controlled asymptotic as `T` tends to infinity. Subtracting the divergent `g(1) log T` term and taking such a limit can modify the boundary contribution, but the common `D(g)` remains the same block. One may obtain `D` plus or minus additional evaluation terms; one does not separate `W` from the other pieces already assembled inside `D`.

This is important because it distinguishes **removing truncation artefacts** from **isolating the Weil form**. The first may be canonical. The second requires an operator that resolves the internal arithmetic/archimedean decomposition of (3), not merely the external truncation coordinate.

## 5. Test-dependent optimization is a lower-bound device, not a Weil-positive quadratic form

Wong explicitly remarks after Corollary 1.3 that allowing `T` to vary may optimize the lower bound for different test functions. This is compatible with (5): for each fixed `g`, one may search the boundary term `B_T(g)` for the best numerical inequality.

That does not answer the present mandate. If `T=T(g)` is selected after inspecting the test-dependent bound, then

\[
g\longmapsto Q_{T(g)}(g)
\tag{17}
\]

is no longer the value of one fixed source-defined quadratic distribution on the full Weil positive-type class. The clue explicitly excludes this post-sign/test tuning. More importantly, even a uniform source-fixed choice `T=T_0` leaves (5) unchanged: positivity still applies to `D+B_{T_0}`, not to the zero-divisor summand of `D` alone.

So height optimization can improve analytic lower bounds without supplying the missing sign-preserving projection.

## 6. Matched control: the no-go is structural, not arithmetic

The obstruction survives if the zeta scattering normalizer is replaced by a matched scalar unitary scattering factor for which the same rank-one Maaß–Selberg decomposition is defined. Write formally

\[
D_m(g)
=-\frac1{4\pi}\int \frac{m'}m(it)\widehat g(it)\,dt,
\qquad
Q_{T,m}=D_m+B_{T,m}.
\tag{18}
\]

Any linear operation in `T` still acts on the common component as

\[
\mathcal L_T[D_m]=\mathcal L_T[1]D_m.
\tag{19}
\]

Therefore the inability of height variation to distinguish constituents of `D` is not a special rigidity of rational primes, the Gamma factor, or the zeta zeros. It is a consequence of the Maaß–Selberg separation between the logarithmic-derivative term and the truncation-dependent boundary terms.

This matched control matters for the Mathia mandate. The negative result does not uncover an arithmetic positivity theorem; it shows that a particular geometric degree of freedom — the Arthur height — carries **too little source information** to perform the desired projection. The arithmetic content enters inside `D`, while height variation only sees whether that entire block is retained or annihilated.

## 7. What is and is not ruled out

The result is intentionally narrower than a no-go for automorphic or trace-formula approaches.

It **does** rule out obtaining the Weil zero-form sign by linear relative subtraction, averaging, differentiation, finite differences, or other linear filtering that acts only on the Arthur truncation height of Wong's positive family while leaving the internal spectral object untouched.

It does **not** rule out an orthogonal decomposition inside the continuous spectral Hilbert space that is defined before the scalar distribution (5) is formed. Such a decomposition could, in principle, act differently on the normalizing factor, finite places, and archimedean scattering data rather than merely on their common `T` profile. It also does not rule out a source-selected finite–archimedean pairing that packages the complement as a genuine boundary square, nor a new cohomological/intersection construction whose positivity theorem has a different geometric origin.

It likewise does not rule out nonlinear operations on the underlying operators. But a nonlinear operation on the scalar values `{Q_T(g)}` would have to recover a quadratic/linear functional of `g` on the full Weil test class and be fixed before observing the target sign. That is an additional structural theorem, not a consequence of height variation. No such theorem is supplied here.

Finally, one could of course isolate `W` algebraically by inserting/subtracting the known prime and archimedean terms of the explicit formula. That is exactly the target-defined repackaging excluded by the research mandate unless those subtractions themselves arise as independently signed canonical geometric summands.

## 8. Prior art and novelty boundary

No historical novelty is claimed for Arthur truncation, the Maaß–Selberg relation, positivity of the truncated Eisenstein inner product, the appearance of the logarithmic derivative of the scattering/intertwining normalizer, or its conversion to a Weil explicit formula. These are classical. Wong's paper is the direct primary source for the exact formulas used here and already presents the consequence as a lower bound rather than a proof of Weil positivity. Wong also explicitly notes the possibility of optimizing the lower bound by varying `T` with the test.

Relevant classical anchors are:

- Tian An Wong, *Explicit formulas for the spectral side of the trace formula of SL(2)*, Acta Arith. 195 (2020), 149–175, DOI `10.4064/aa190115-9-10`, arXiv `1608.02296`; especially Theorem 1.1, Corollary 1.3, Lemma 5.1, Remark 5.2, and the proof of Corollary 1.3.
- James Arthur, *An introduction to the trace formula*, Clay Math. Proc. 4 (2005), 1–263, for the general truncation and spectral framework cited by Wong.
- Standard Maaß–Selberg formulas for `SL(2)`, in which the truncation parameter occurs in boundary powers while the logarithmic derivative of the scattering factor is the `T`-independent term.

A bounded literature audit around Maaß–Selberg relations, Arthur truncation, varying/relative truncation parameters, and explicit-formula lower bounds did not surface a separate theorem advertised as the exact no-go (10). That absence is not a historical novelty proof. The Mathia-specific delta is the **application of the classical decomposition as a decisive falsifier of the proposed height-subtraction interface**: because the Weil zero term and its finite/archimedean companions all lie in the same `T`-independent spectral block, height filtering has rank one on that decomposition and cannot be the missing sign-preserving projection.

## 9. Aggressive falsification

**Could a clever choice of two canonical heights retain the zero term?** No. Equation (7) is exact for every admissible pair: the zero term is inside `D` and cancels before the values of the heights matter.

**Could more heights solve a linear system that separates zeros, primes, and Gamma?** No. Their coefficient vectors in the height variable are identical constants. The linear system has only one column for the whole block `D`; equations (10)–(16) make this rank defect explicit.

**Could a signed height measure with infinitely many support points separate them?** Not through the height variable alone. Whenever the linear functional is defined on the constant profile, it multiplies every constituent of `D` by the same scalar `L[1]`.

**Could one differentiate in height and then integrate back with a boundary condition?** Differentiation deletes `D`. Integrating back restores an undetermined constant distribution; identifying that constant specifically with `W` rather than the whole `D` requires exactly the extra internal information the method lacked.

**Could positivity of each `Q_T` imply positivity of `D` by taking a limit?** Only if one independently proves that the limiting/renormalized boundary contribution has the required sign or vanishes uniformly over the full test class. Wong's result does not give that, and arbitrary subtraction of the boundary term would merely restate the missing remainder-sign problem. The present finding does not claim that such a new theorem is impossible; it shows that varying `T` itself cannot distinguish the target summand.

**Could optimizing `T` separately for each positive-type `g` force `W(g)>=0`?** A per-test optimizer is explicitly excluded by the clue and does not define one fixed quadratic distribution. Moreover, a lower bound approaching zero would itself require a uniform theorem on `B_T(g)` strong enough to close the original sign gap; it is not obtained algebraically from the existence of the height parameter.

**Does this show the trace-formula route is equivalent to RH?** No. It proves only a block-separation obstruction for one class of operations. The positive automorphic object remains a valuable matched control and may contain additional internal structure not visible after taking the scalar truncated trace.

## Consequence for the live frontier

The Maaß–Selberg route survives as a qualitatively stronger global control than local Prime Circle/Prime Lattice positive completions: it already supplies nonfactorizing automorphic assembly, analytic continuation, a true Hilbert-space positivity theorem, and the complete scattering normalizer. But its obvious extra geometric knob, the Arthur truncation height, cannot perform the missing projection.

The next viable test must therefore act **inside** the source geometry before the constituents collapse into the common distribution `D`. Concretely, a useful construction would need a canonical orthogonal/cohomological/boundary decomposition of the continuous spectral object, or a source-forced finite–archimedean pairing, whose sign is independently geometric and whose scalarization isolates the Weil zero form while preserving the full positive-type class. Reweighting the external truncation height is not enough.

## Dependencies

- `research/weil_positivity/clues/CLUE-maass-selberg-remainder-sign-interface.md`
- `research/prime_lattice/findings/PL-253-maass-selberg-positivity-lower-bound-weil-gap.md` at the clue-authorized source revision `ff734900b636e6ab0e0e06e70a813682d18fea05`
- `research/weil_positivity/findings/WP-235-gamma-bost-connes-metric-defect-is-not-of-negative-type-on-two-prime-forks.md`
- `research/weil_positivity/findings/WP-236-bounded-order-prime-marginals-do-not-determine-critical-cauchy-coupling.md`

## Bottom line

For Wong's positive Riemann-zeta Maaß–Selberg/Arthur-truncation family, the zero divisor, finite-prime contribution, Gamma/archimedean contribution, and polar/conductor terms all live inside one `T`-independent logarithmic-derivative distribution `D`. Therefore **every linear operation acting only on truncation height either annihilates that whole explicit-formula block or preserves it with all constituents in their original relative combination**. Relative subtraction between canonical heights cannot isolate the Weil zero form. Any successful continuation of this route must introduce a genuinely internal source-defined projection or pairing, not another manipulation of the external Arthur height.