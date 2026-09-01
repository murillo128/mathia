# PF-155 — the local heat-invariant tower is area-only on the hyperbolic flute

**Status:** `LITERATURE+DERIVED + EXACT-PROJECT-SPECIALIZATION + NEGATIVE/BOUNDARY`. The general heat-kernel and Selberg-trace facts used below are classical. The project-specific conclusion is that the scalar Laplacian's entire **local short-time heat-invariant tower**, not only the critical first-resolvent residue isolated in PF-151, is blind to the prime-dependent cuff moduli on the exact curvature-`-1` prime flute. Any surviving heat/spectral signal must therefore enter through genuinely nonlocal closed-geodesic, scattering/end, interface, or relative-operator data.

This finding does **not** claim that the full infinite prime flute has a heat trace or a standard relative heat expansion. PF-033 proves the opposite for the absolute/ordinary Selberg heat trace. The statement concerns the local bulk coefficients and a boundary-free compact audit of matched prime/shift pants.

## Claim

Let `(M,g)` be any closed hyperbolic surface of curvature `-1`, and let `Delta_g` be the nonnegative scalar Laplacian. Write the classical short-time heat expansion as

\[
\operatorname{Tr}(e^{-t\Delta_g})
\sim
\frac{1}{4\pi t}
\sum_{j\ge 0} A_j(g)t^j,
\qquad t\downarrow0.
\tag{1}
\]

Then for every `j>=0` there is a universal numerical constant `c_j`, independent of the point in Teichmüller space, such that

\[
\boxed{A_j(g)=c_j\operatorname{Area}_g(M).}
\tag{2}
\]

Equivalently, all scalar local heat coefficients of a closed curvature-`-1` surface depend only on its area, hence only on its Euler characteristic by Gauss--Bonnet.

For the exact prime-flute pants this has the following concrete consequence. Fix any pant index `n` and any `epsilon>0`. Replace the cusp of the prime pant by a geodesic boundary of length `epsilon`, do the same for the corresponding exact all-composite shift-clone pant `p_k -> p_k+1`, and double both compact pants across all three geodesic boundaries. Denote the resulting closed genus-two hyperbolic surfaces by

\[
M_{n,\epsilon},\qquad M^+_{n,\epsilon}.
\tag{3}
\]

Both have exact area `4 pi`, independently of their prime-dependent cuff lengths. Therefore

\[
\boxed{
A_j(M_{n,\epsilon})=A_j(M^+_{n,\epsilon})
\quad\text{for every }j\ge0.
}
\tag{4}
\]

If the corresponding cuffs differ, the two hyperbolic metrics are nevertheless generally nonisometric. Thus the complete local heat-invariant sequence cannot distinguish a prime pant from its exact all-composite matched control.

Moreover, for each fixed pair `(n,epsilon)` the compact Selberg trace formula gives

\[
\boxed{
\operatorname{Tr}(e^{-t\Delta_{M_{n,\epsilon}}})
-
\operatorname{Tr}(e^{-t\Delta_{M^+_{n,\epsilon}}})
=
H_{n,\epsilon}(t)-H^+_{n,\epsilon}(t),
}
\tag{5}
\]

where `H,H^+` are the hyperbolic closed-geodesic orbital sums. The identity/area terms cancel exactly. Since each fixed compact double has positive systole, there is a constant `c_{n,epsilon}>0` such that

\[
\operatorname{Tr}(e^{-t\Delta_{M_{n,\epsilon}}})
-
\operatorname{Tr}(e^{-t\Delta_{M^+_{n,\epsilon}}})
=
O\!\left(t^{-1/2}e^{-c_{n,\epsilon}/t}\right)
\tag{6}
\]

as `t downarrow 0`. Hence the moduli dependence is **beyond all algebraic orders** of the local heat expansion; it lives in the nonlocal length-spectrum sector.

## 1. Why every local coefficient collapses to area

For a Laplace-type operator on a closed manifold, each local heat coefficient is a universal scalar polynomial in the curvature tensor, its contractions, and finitely many covariant derivatives. For the scalar Laplace--Beltrami operator there is no auxiliary bundle curvature or potential.

On a hyperbolic surface,

\[
K\equiv-1,
\qquad
\nabla^m\operatorname{Riem}=0
\quad(m\ge1).
\tag{7}
\]

Every complete contraction that can appear in the `j`th coefficient therefore evaluates to a universal constant depending only on `j`. Intrinsically, the coefficient density has the form

\[
a_j(x,g)\,dA_g
=c_j\,dA_g.
\tag{8}
\]

Integrating gives (2). The first instances are the familiar volume and scalar-curvature coefficients; the argument is not restricted to those first terms because constant curvature kills every derivative invariant and fixes every curvature contraction at every order.

The same statement applies to the **bulk coefficient density** on each exact prime-flute pant before gluing. Each pant has hyperbolic area

\[
\operatorname{Area}(P_n)=2\pi,
\tag{9}
\]

so the integral of the `j`th bulk density over a complete pant is simply `2 pi c_j`, independent of the two distinguished cuff lengths and hence independent of the prime gaps entering

\[
\ell_n\sim2\log(4p_n/g_n).
\tag{10}
\]

This is an intrinsic statement about the local scalar Laplacian. It does not impose a boundary condition on the cuffs.

## 2. The compact double separates local from nonlocal information exactly

The compact audit in (3) avoids every ambiguity associated with cusps, continuous spectrum, infinite area, or artificial heat boundary conditions.

A hyperbolic pair of pants with three geodesic boundary lengths has area `2 pi` by Gauss--Bonnet. Doubling across its geodesic boundary gives a smooth closed genus-two hyperbolic surface of area `4 pi`. Therefore the prime and shift-clone doubles have identical identity contribution in the Selberg trace formula for **every** positive time `t`, not merely to leading order.

For the heat test function, the compact Selberg formula separates the trace into

```text
identity term determined by Area(M)
+
hyperbolic orbital sum determined by closed geodesics.
```

The identity terms of the two doubles cancel exactly because their areas agree. What remains is the difference of the two closed-geodesic sums, proving (5).

For a fixed compact hyperbolic surface the primitive length spectrum has a positive lower bound. The heat orbital factor contains the Gaussian

\[
\exp\!\left(-\frac{(k\ell_\gamma)^2}{4t}\right),
\tag{11}
\]

so the whole hyperbolic term is exponentially small as `t downarrow 0`. Standard closed-geodesic counting and the Gaussian dominate the infinite orbit sum, yielding (6) for some positive `c_{n,epsilon}`.

Thus two nonisometric matched doubles can have different Laplace spectra and different length spectra while agreeing in **every** algebraic heat coefficient. The missing information is not hidden in a higher Seeley--DeWitt coefficient waiting farther down the expansion.

## 3. Relation to PF-151, PF-152, and PF-033

PF-151 identified one especially natural critical scalar: in dimension two the order-`-2` first resolvent has Wodzicki residue density

\[
\operatorname{wres}_x((\Delta_g+\mu)^{-1})
=\frac{1}{2\pi}dA_g.
\tag{12}
\]

PF-155 shows that this area universality is not an isolated accident of the critical pseudodifferential order. It is the first visible member of a stronger constant-curvature phenomenon: **the entire local heat tower is area/topology only**.

PF-152 then showed that subtracting the common critical residue does not canonize an unweighted finite part; weighted finite parts retain a classical regularization anomaly. PF-155 closes a different attempted repair:

```text
critical residue is universal
  -> inspect higher local heat coefficients
  -> hope a later coefficient sees prime gaps.
```

No later scalar bulk heat coefficient can do so.

PF-033 supplies the complementary global obstruction. On the full infinite prime flute the absolute heat trace is infinite because the area is infinite, and even after removing the identity/area background the standard hyperbolic orbital part diverges for every `t>0` because primitive closed geodesics accumulate at length zero.

Taken together, the two facts identify the boundary sharply:

```text
local heat sector       -> universal / area-only;
ordinary global sector  -> divergent from short-orbit accumulation;
possible surviving data -> genuinely relative/nonlocal construction.
```

Local counterterm subtraction cannot manufacture a prime-sensitive heat invariant from the universal coefficient tower.

## 4. Boundary, cusp, and nonuniformity audits

Several tempting overextensions are false and are excluded from the claim.

**Artificial pant boundary conditions.** If one cuts a pant out of the flute and imposes Dirichlet, Neumann, Robin, or another boundary condition on its cuffs, the heat expansion acquires boundary coefficients involving boundary length and boundary geometry. Those terms can see the cuff lengths. But the cuffs are internal gluing geodesics of the complete prime flute, not physical boundaries carrying a canonical scalar boundary condition. Such a standalone boundary heat trace therefore imports extra structure and is not the intrinsic bulk mechanism ruled on here.

**The cusp is not being declared spectrally invisible.** Noncompact finite-area heat regularizations can contain parabolic/scattering contributions. PF-155 only says that the ordinary local curvature coefficients cannot contain the prime gaps. Cusp-to-cusp scattering, relative heat kernels, and end corrections are nonlocal data and remain outside the negative.

**There is no uniform exponential estimate over the whole tail.** In (6), `c_{n,epsilon}` may tend to zero along degenerating prime patterns. One may not interchange `n -> infinity` with `t -> 0`. Indeed PF-005/PF-020/PF-033 show exactly why no uniform positive systole exists and why the full orbit sum becomes singular. This is not a loophole in (2)--(4); it is the nonlocal sector that survives after the local tower has cancelled.

**Localized cutoffs are extra data.** A weighted coefficient `int chi a_j dA` may vary if an externally chosen cutoff or marking is changed. Unless the cutoff is itself canonically selected by the intrinsic surface, that variation is not a new spectral invariant of the flute.

## 5. Prior art and novelty audit

No general heat-kernel theorem is claimed as new.

- The Minakshisundaram--Pleijel/Seeley--DeWitt--Gilkey heat expansion and the fact that its coefficients are integrals of universal local curvature invariants are classical. A convenient review with explicit coefficient formulas and boundary caveats is D. V. Vassilevich, *Heat kernel expansion: user's manual*, Physics Reports 388 (2003), 279--360, arXiv:`hep-th/0306138`, DOI `10.1016/j.physrep.2003.09.002`.
- The compact Selberg trace formula and its separation into an area/identity term and a closed-geodesic hyperbolic term are classical; standard references include D. Hejhal, *The Selberg Trace Formula for PSL(2,R)*, Vols. I--II, and P. Buser, *Geometry and Spectra of Compact Riemann Surfaces*, Birkhauser, 1992.
- Explicit all-order heat-invariant calculations for constant-curvature surfaces and orbifolds are part of the existing literature; see E. Ucar, *Spectral invariants for polygons and orbisurfaces*, arXiv:`1711.03405` (2017), for a directly neighboring treatment.

The project-specific contribution is the exact placement of those classical facts inside the prime-flute falsification hierarchy. PF-151 had only closed the critical first-resolvent residue. PF-155 records the stronger reusable negative:

\[
\boxed{
\text{prime-dependent hyperbolic moduli}
\not\to
\text{scalar local heat coefficients at any order}.
}
\tag{13}
\]

The matched all-composite control makes the information loss explicit without assuming anything about RH or about the eventual existence of a global relative determinant.

## 6. Consequence for the research line

Reject the natural branch

```text
prime-gap cuff/cross-ratio fluctuations
  -> higher Seeley--DeWitt / local heat coefficients
  -> canonical prime-sensitive spectral scalar
  -> RH-relevant selector.
```

The second arrow erases the moduli on constant-curvature pieces. Raising the heat-expansion order cannot repair that loss.

This does **not** reject the Laplacian itself. The compact Selberg audit shows exactly where moduli re-enter: the closed-geodesic orbital sector. On the infinite flute that sector is analytically difficult rather than absent, because short lengths accumulate and ordinary trace sums diverge. Likewise, relative scattering, spectral-shift, resonance, discrete-spectrum, or determinant constructions may still carry nonlocal information if they can be defined canonically and survive the exact all-composite controls.

The useful frontier is therefore not another local coefficient. It is a genuinely global relative object whose existence and comparison hypotheses can be proved on the exact infinite flute without importing an arbitrary subtraction or re-encoding the prime gaps by hand.
