# PF-118 — shift-clone pants are asymptotically arc-Lipschitz close

**Status:** `LITERATURE+DERIVED + POSITIVE/BOUNDARY`.  The finite-type arc-distance/Lipschitz theorem and the classification of simple arcs in a one-puncture pair of pants are standard.  The project-specific result is that the exact prime/shift-clone pants have arc distance tending to zero in both directions, with a **summable forward optimal Lipschitz cost** but a **nonsummable reverse lower bound** forced by the shrinking cross-cuff seam.  No homeomorphic, quasiconformal, global-flute, resolvent, scattering, or RH conclusion is claimed.

## 1. Exact finite arc-distance reduction

Use the notation of PF-114.  Let `P_n` be the one-cusp tight pair of pants in the exact prime flute with finite cuffs

\[
\ell_n,\qquad \ell_{n+1},
\]

and let `P_n^+` be the matched pant in the all-composite shift clone `p -> p+1`.  Write

\[
S_n
\]

for the unique simple orthogeodesic seam joining the two finite cuffs, and

\[
Y_{A,n},\qquad Y_{B,n}
\]

for the two returning simple orthogeodesics, one based on each finite cuff.  Superscript `+` denotes the corresponding clone quantities.

For the topological surface `S_{0,2,1}` (genus zero, two compact boundary components, one puncture), every essential simple proper arc is properly homotopic to exactly one of these three types: the cross-cuff seam or one of the two returning waves.  There is no nonperipheral simple closed curve other than the two geodesic boundary classes.  Therefore the arc distance of Liu--Papadopoulos--Su--Théret / Alessandrini--Disarlo reduces here to the finite maximum

\[
\boxed{
 d_A(P_n,P_n^+)
 =\max\left\{
 \log\frac{\ell_n^+}{\ell_n},
 \log\frac{\ell_{n+1}^+}{\ell_{n+1}},
 \log\frac{S_n^+}{S_n},
 \log\frac{Y_{A,n}^+}{Y_{A,n}},
 \log\frac{Y_{B,n}^+}{Y_{B,n}}
 \right\}.
}
\tag{1}
\]

The reverse distance is the same maximum with all ratios inverted.

This is an exact reduction, not an approximation or a claim that general measured-lamination data on a more complicated surface are finite.

## 2. The prime-to-clone arc-distance costs are summable

PF-107 proves that the clone cuffs are eventually longer and that their relative defects are summable:

\[
\ell_j^+>\ell_j,
\qquad
\sum_j \frac{\ell_j^+-\ell_j}{\ell_j}<\infty.
\tag{2}
\]

Hence, using `log(1+x) <= x`,

\[
\sum_j \log\frac{\ell_j^+}{\ell_j}<\infty.
\tag{3}
\]

PF-114 proves

\[
\sum_n\left|\log\frac{Y_{A,n}^+}{Y_{A,n}}\right|<\infty,
\qquad
\sum_n\left|\log\frac{Y_{B,n}^+}{Y_{B,n}}\right|<\infty,
\tag{4}
\]

while the seam satisfies

\[
\log\frac{S_n^+}{S_n}
=-\frac1{p_n}+o(p_n^{-1})<0
\tag{5}
\]

on the tail.  The seam therefore cannot maximize the **forward** arc distance once the positive cuff ratios are present.  From (1)--(4),

\[
0\le d_A(P_n,P_n^+)
\le
\log\frac{\ell_n^+}{\ell_n}
+\log\frac{\ell_{n+1}^+}{\ell_{n+1}}
+\left|\log\frac{Y_{A,n}^+}{Y_{A,n}}\right|
+\left|\log\frac{Y_{B,n}^+}{Y_{B,n}}\right|.
\]

Consequently

\[
\boxed{
\sum_n d_A(P_n,P_n^+)<\infty.
}
\tag{6}
\]

In particular `d_A(P_n,P_n^+) -> 0`.

## 3. The reverse distance tends to zero but has a nonsummable seam lower bound

In the reverse direction the same seam contributes with the opposite sign.  Equation (5) gives

\[
\boxed{
 d_A(P_n^+,P_n)
 \ge
 \log\frac{S_n}{S_n^+}
 =\frac1{p_n}+o(p_n^{-1}).
}
\tag{7}
\]

Euler's divergence of the reciprocal-prime sum therefore implies

\[
\boxed{
\sum_n d_A(P_n^+,P_n)=\infty.
}
\tag{8}
\]

This divergence is compatible with pointwise closeness.  PF-107 and PF-114 show that every one of the five logarithmic ratios appearing in the finite maximum tends to zero.  Hence

\[
\boxed{
 d_A(P_n^+,P_n)\longrightarrow0
 \quad\text{and}\quad
 d_A(P_n,P_n^+)\longrightarrow0.
}
\tag{9}
\]

The distinction is therefore not failure of local convergence but a directional summability asymmetry:

\[
\boxed{
\text{prime -> clone arc cost is }\ell^1,
\qquad
\text{clone -> prime arc cost has a non-}\ell^1\text{ seam floor}.
}
\tag{10}
\]

No claim is made that the reverse distance itself is asymptotic to `1/p_n`; other arc ratios could dominate on subsequences.  The lower bound (7) is all that is needed for (8).

## 4. A uniform local Lipschitz consequence without an upper cuff bound

Alessandrini--Disarlo prove for every finite-type hyperbolic surface with nonempty compact geodesic boundary that

\[
 d_A(X,Y)=d_{L\partial}(X,Y),
\]

and, more precisely, that there exists a continuous marking-compatible map

\[
\phi:X\to Y,
\qquad \phi(\partial X)\subset\partial Y,
\]

with optimal Lipschitz constant

\[
\log\operatorname{Lip}(\phi)=d_A(X,Y).
\tag{11}
\]

Their theorem allows punctures and does not impose an upper bound on the geodesic boundary lengths.  Applying it pant by pant gives maps

\[
\phi_n:P_n\to P_n^+,
\qquad
\psi_n:P_n^+\to P_n
\]

such that

\[
\operatorname{Lip}(\phi_n)=e^{d_A(P_n,P_n^+)},
\qquad
\operatorname{Lip}(\psi_n)=e^{d_A(P_n^+,P_n)}.
\tag{12}
\]

Therefore

\[
\boxed{
\operatorname{Lip}(\phi_n)\to1,
\qquad
\operatorname{Lip}(\psi_n)\to1,
\qquad
\sum_n\log\operatorname{Lip}(\phi_n)<\infty.
}
\tag{13}
\]

This removes one local ambiguity in the accepted relative-operator clue: **unbounded perturbed cuffs plus a cusp do not prevent asymptotically optimal boundary-respecting Lipschitz maps in the finite pant problem**.  The conclusion is stronger in this category than what could be extracted from Minsky's coarse `K(C)` statement, because the optimal constant is computed by the intrinsic arc spectrum itself.

## 5. Why this still does not solve the common-manifold problem

The theorem deliberately stops at exactly the missing gate.

Alessandrini--Disarlo's optimal map in Corollary 1.5 is a continuous Lipschitz map in the marking class with boundary sent to boundary.  Their paper explicitly leaves open in general whether the arc distance equals the **homeomorphic** Lipschitz distance `d_Lh`; the generalized stretch maps need not be known to be injective.  Thus (11)--(13) do not provide:

- a homeomorphism or quasiconformal map between the matched pants;
- affine or otherwise prescribed boundary parametrizations on a shared cuff;
- compatibility of the restrictions from the two pants adjacent to a cuff;
- a bilipschitz common-manifold identification;
- metric-norm or volume-density control after gluing;
- compactness/Schatten control of a relative Laplacian.

The nonsummable reverse seam floor is also a useful warning.  Any attempted global construction that budgets **multiplicative** inverse distortion by summing pantwise costs cannot use an `ell^1` estimate in both directions.  On the other hand the lower bound tends to zero, and PF-108 shows that the seam's additive and area-weighted defects are summable, so (8) is not itself an obstruction to strong metric equivalence or compact relative resolvent.

The operator clue is therefore sharpened to a boundary-coherence/homeomorphism question rather than a local existence-of-near-Lipschitz-map question.

## 6. Prior art / novelty audit

The relevant general results are established literature:

- L. Liu, A. Papadopoulos, W. Su, G. Théret, *Length spectra and the Teichmüller metric for surfaces with boundary*, Monatsh. Math. 161 (2010), 295--311, DOI `10.1007/s00605-009-0145-8`, develops the length/arc-spectrum framework for finite-type surfaces with boundary and records the one-puncture pair-of-pants arc geometry used in PF-114.
- D. Alessandrini, V. Disarlo, *Generalizing Stretch Lines for Surfaces with Boundary*, Int. Math. Res. Not. 2022 (23), 18919--18991, DOI `10.1093/imrn/rnab222`, proves `d_A=d_{L\partial}` and existence of the optimal boundary-respecting Lipschitz map, while explicitly distinguishing this from the still-open homeomorphic equality in their setting.
- Q. Chen, L. Liu, *The arc metric on Teichmüller spaces of surfaces of infinite type with boundary*, arXiv:1612.04213, develops an infinite-type arc metric under additional geometric hypotheses.  It does not directly apply the finite-pant maps above to the prime flute: the distinguished cuffs are internal gluing curves of the complete flute, not an infinite family of actual boundary components, and its hypotheses do not supply the missing boundary-compatible common-manifold identification.

Directed searches for the exact cotangent endpoint flute, the all-composite shift `p_n -> p_n+1`, and the resulting forward/reverse arc-distance summability split found no matching statement.  No novelty is claimed for arc distance, pair-of-pants arc classification, optimal Lipschitz maps, or reciprocal-prime divergence.  The durable Mathia contribution is the specialization

\[
\boxed{
\text{shift-clone local arc spectrum}
\Rightarrow
\text{two-sided }d_A\to0
\text{ but one-sided }\ell^1\text{ asymmetry}.
}
\]

This is a local comparison theorem for the accepted operator program, not evidence for RH.

## 7. Falsification core

The result can be audited at five independent gates:

1. verify that `S_{0,2,1}` has exactly the seam and two returning-wave proper homotopy classes of essential simple arcs, and no extra nonperipheral simple closed class beyond its geodesic boundaries;
2. insert those five classes into the definition of `d_A` to obtain the finite maximum (1);
3. verify PF-107's summable relative cuff defects and PF-114's summable wave defects plus seam asymptotic (5);
4. derive (6)--(10) only from maxima, positivity, and Euler's reciprocal-prime divergence, without assuming an unproved asymptotic for the full reverse distance;
5. check Alessandrini--Disarlo Corollary 1.5 gives an optimal **continuous boundary-respecting Lipschitz map**, and do not silently upgrade it to a homeomorphism or a gluable common-manifold comparison.

Breaking any of steps 1--4 falsifies the project-specific claim.  Step 5 is the literature bridge and the main boundary protecting the result from overinterpretation.
