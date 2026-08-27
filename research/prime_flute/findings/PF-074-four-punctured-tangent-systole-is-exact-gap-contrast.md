# PF-074 — the four-punctured tangent systole is exactly the unordered adjacent-gap contrast

**Status:** `EXACT-DERIVED` + `POSITIVE-SPECTRAL-CANDIDATE`; strengthens PF-063 from the hierarchical regime to every positive adjacent-gap ratio.

## 1. Setup

For the four-punctured tangent produced by three ordered offsets

\[
\eta_1<\eta_2<\eta_3,
\qquad
d_1=\eta_2-\eta_1,
\quad
d_2=\eta_3-\eta_2,
\]

put

\[
r=\frac{d_1}{d_2}>0.
\]

The exact cusp-side holonomy from PF-029 gives three standard essential simple separating classes (the three pairings of the four punctures). Their **positive absolute traces** are

\[
\boxed{
X=2+4r,
\qquad
Y=2+\frac4r,
\qquad
Z=6+4r+\frac4r.
}
\]

For the first two classes this is equivalent to the already established exact identities

\[
\sinh^2\frac{L_X}{4}=r,
\qquad
\sinh^2\frac{L_Y}{4}=\frac1r.
\]

The issue left open by PF-063 was global: could some *other* simple closed curve, deeper in the Farey/curve-complex tree of \(S_{0,4}\), be shorter except in the small-\(r\) collar-lemma regime?

The answer is no.

## 2. The exact parabolic Markoff relation

For a four-punctured sphere all four boundary traces are parabolic. With the positive-trace convention above, the three traces at every Farey vertex satisfy the generalized Markoff/Fricke equation

\[
\boxed{
X^2+Y^2+Z^2-XYZ+8(X+Y+Z)+28=0.
}
\]

This is the \((8,8,8,-28)\) four-holed-sphere Markoff surface in the sign convention used here. Treating this equation as a quadratic in one coordinate gives the standard Vieta/edge mutation

\[
\boxed{
Z^*=XY-Z-8,
}
\]

and cyclically

\[
X^*=YZ-X-8,
\qquad
Y^*=XZ-Y-8.
\]

The correspondence between essential simple curves on \(S_{0,4}\), complementary regions of the Farey dual tree, and these Markoff mutations is classical (Bowditch; Tan–Wong–Zhang; Maloni–Palesi–Tan; Palesi).

For our exact prime-tangent triple, direct substitution gives

\[
\boxed{
XY-2Z-8=0,
}
\]

while

\[
\boxed{
YZ-2X-8
=16\frac{(r+1)^2}{r^2}>0,
}
\]

and

\[
\boxed{
XZ-2Y-8
=16(r+1)^2>0.
}
\]

Equivalently,

\[
X^*>X,
\qquad
Y^*>Y,
\qquad
Z^*=Z.
\]

Thus the initial Farey vertex is a Markoff **sink** (with a tie in the \(Z\)-direction) for every \(r>0\), not only for hierarchical ratios.

## 3. A self-contained monotonicity argument gives the global systole

The sink observation by itself is local. In this special positive Fuchsian case, however, it propagates through the whole Farey tree.

Root the trivalent dual tree at the vertex with coordinates \((X,Y,Z)\). Suppose a step away from the root replaces, say, \(z\) by

\[
z'=xy-z-8\ge z.
\]

At the new vertex \((x,y,z')\), consider either of the two mutations that continue away from the root. For example,

\[
x'=yz'-x-8
\ge yz-x-8.
\]

If the corresponding outward mutation was non-decreasing at the previous vertex, then

\[
yz-x-8\ge x,
\]

and hence \(x'\ge x\). The same argument applies to the other forward coordinate. Therefore the three sink inequalities at the root propagate inductively along **every** ray of the Farey tree.

Consequently every trace introduced anywhere in the Markoff tree is at least

\[
\min\{X,Y,Z\}.
\]

Since the regions of this tree enumerate all essential unoriented simple closed curves of \(S_{0,4}\), the trace systole of our tangent is exactly

\[
\boxed{
\operatorname{tys}(Y_r)
=\min\left\{2+4r,\,2+\frac4r\right\}
=2+4\min(r,r^{-1}).
}
\]

The third trace is always larger:

\[
Z-X=4\frac{r+1}{r}>0,
\qquad
Z-Y=4(r+1)>0.
\]

Using \(|\operatorname{tr}\gamma|=2\cosh(\ell_\gamma/2)\), this proves the exact global systole formula

\[
\boxed{
\operatorname{sys}(Y_r)
=4\operatorname{arsinh}\sqrt{\min(r,r^{-1})}
\qquad(r>0).
}
\]

At \(r=1\) the two adjacent separating classes tie. For \(r\neq1\) the shorter of those two is the unique trace minimum in this rooted Markoff sector; reversing the order of the punctures exchanges \(r\leftrightarrow r^{-1}\).

## 4. Direct relation to distinguished cuffs

For an occurrence of the same three-offset pattern near prime scale \(P\), the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1).
\]

Hence

\[
\min(r,r^{-1})
=
\lim_{P\to\infty}
\exp\left(-\frac{|\ell_1(P)-\ell_2(P)|}{2}\right).
\]

Combining with the exact tangent systole gives

\[
\boxed{
\lim_{P\to\infty}
\exp\left(-\frac{|\ell_1(P)-\ell_2(P)|}{2}\right)
=
\sinh^2\left(\frac{\operatorname{sys}(Y_r)}4\right).
}
\]

Equivalently,

\[
\boxed{
\lim_{P\to\infty}|\ell_1(P)-\ell_2(P)|
=-4\log\sinh\left(\frac{\operatorname{sys}(Y_r)}4\right).
}
\]

Thus the *absolute contrast* between two consecutive distinguished cuffs survives as an intrinsic, unmarked systolic invariant of the finite hyperbolic tangent. The orientation of the contrast is necessarily lost: \(Y_r\) and \(Y_{1/r}\) are related by reversing the puncture order, so an unmarked spectral invariant cannot distinguish them.

## 5. Spectral/resonance consequence

For finite-area hyperbolic surfaces, the resonance set determines the length spectrum (and conversely, with the standard accompanying topological data). More generally, Borthwick–Judge–Perry prove the resonance-to-length-spectrum implication for geometrically finite hyperbolic surfaces.

Therefore the **unmarked resonance set** of the four-punctured tangent determines its systole and hence

\[
\boxed{
\mathcal R(Y_r)
\Longrightarrow
\min(r,r^{-1})
=
\sinh^2\left(\frac{\operatorname{sys}(Y_r)}4\right).
}
\]

This strengthens PF-063: no small-r / collar-lemma threshold is needed. Every positive adjacent-gap ratio is recoverable **up to the unavoidable inversion \(r\leftrightarrow1/r\)** from unmarked resonance data of the tangent.

The statement is about the finite tangent \(Y_r\), not a globally defined resonance set of the infinite prime-flute. PF-064 remains the route for realizing its systolic signal through spatially localized spectral data of the global Laplacian.

## 6. Novelty audit

Known ingredients, not claimed as new:

- the Farey-tree description of simple curves on the four-punctured sphere;
- generalized Markoff maps and their edge orientations/sinks for the four-holed sphere (Bowditch; Tan–Wong–Zhang; Maloni–Palesi–Tan; Palesi);
- Palesi's trace-systole/sink theory, published in *Journal of Topology and Analysis* in July 2026 (DOI `10.1142/S1793525326500457`);
- Hanada's classification of the number of systoles and second systoles on the four-punctured sphere;
- the fact that resonance data determine the length spectrum for finite-area/geometrically finite hyperbolic surfaces.

Directed searches for the exact one-parameter trace triple

\[
(2+4r,\ 2+4/r,\ 6+4r+4/r)
\]

and for the formula

\[
\operatorname{sys}=4\operatorname{arsinh}\sqrt{\min(r,r^{-1})}
\]

in the four-punctured-sphere literature did not locate this specialization. The general Markoff machinery is classical; the potentially novel part is the exact specialization forced by the prime tangent and its consequence that an adjacent prime-gap/cuff contrast is globally the systolic/resonance invariant for **all** ratios, not only in a degeneration regime.

## 7. Research consequence

PF-063's hierarchical restriction can be removed. For the first moduli-sensitive tangent,

\[
\boxed{
\text{adjacent cuff contrast}
\to
\text{four-punctured tangent}
\to
\text{unmarked systole}
\to
\text{unmarked resonance data}
}
\]

is exact up to the geometrically unavoidable reversal symmetry.

This is a stronger target for the localized-global program than another Selberg determinant: it asks whether the prime-flute's spatially localized Laplacian/resolvent can recover this **global Markoff minimum** canonically, rather than merely a preselected separating geodesic.
