# PF-325 — physical translations convert the local Hilbert–Schmidt gate into a packet-position integral

**Status:** `EXACT-DERIVED + FOURIER-PARSEVAL + POSITION-SPACE-REDUCTION + ROUTE-SHARPENING`.

PF-318 reduces the remaining direct-angle endpoint to a local squared Hilbert–Schmidt estimate on the fixed physical-low target. Its exact formula uses an orthonormal Fourier basis of that low band. PF-322--PF-324, by contrast, produce the useful adversarial objects in physical position: fixed-band Dirichlet packets translated to a critical interior window whose outgoing seam distance remembers the consecutive prime-gap ratio.

These are two representations of the same finite-dimensional low sector. The translation orbit of one equal-amplitude fixed-band packet is a continuous tight frame, so the Hilbert–Schmidt mass of any local low/high block is **exactly** a one-dimensional integral of packet responses over the physical cuff coordinate. Since the number of retained modes is proportional to the cuff length, the proportionality constant stays bounded away from zero and infinity. There is no `1/log P_n` dilution from replacing the Fourier sum by a position integral.

Thus the PF-318 fallback can be attacked in physical space: instead of estimating every low Fourier row separately, estimate the completed high leakage of one translated packet family and integrate over its center. Conversely, any fixed-width set of packet centers carrying too much completed response already violates the PF-318 budget. This does not prove that the PF-323 critical packet survives the seam normalization or common pant completion; it gives the exact accounting identity needed to decide that question in the localized representation in which PF-323--PF-324 are naturally stated.

## Claim

Fix a cuff of physical length `L` and a fixed physical cutoff `kappa>0`. Put

\[
N=\left\lfloor\frac{\kappa L}{2\pi}\right\rfloor,
\qquad
m=2N,
\]

and let

\[
e_k(s)=L^{-1/2}e^{2\pi i k s/L},
\qquad 1\le |k|\le N,
\]

be the orthonormal basis of the nonconstant fixed physical-low band

\[
\mathcal L_{\kappa,L}
=\operatorname{span}\{e_k:1\le |k|\le N\}.
\]

For `t in R/LZ`, define the unit translated packet

\[
\boxed{
\psi_t
=\frac1{\sqrt m}
\sum_{1\le |k|\le N}
e^{-2\pi i kt/L}e_k.
}
\tag{1}
\]

Let `B:\mathcal H\to\mathcal L_{\kappa,L}` be any Hilbert--Schmidt operator. Then

\[
\boxed{
\frac1L\int_0^L\|B^*\psi_t\|_{\mathcal H}^2\,dt
=\frac1m\|B\|_{\mathcal S_2}^2,
}
\tag{2}
\]

or equivalently

\[
\boxed{
\|B\|_{\mathcal S_2}^2
=\frac mL\int_0^L\|B^*\psi_t\|^2\,dt.
}
\tag{3}
\]

Since

\[
\frac mL
=\frac\kappa\pi+O(L^{-1}),
\tag{4}
\]

the PF-318 target

\[
\|B_{n,r}\|_{\mathcal S_2}^2
\lesssim
\frac{1+\log P_n}{P_n^2}
\tag{5}
\]

is equivalent, up to constants depending only on the fixed cutoff and the finite number of low boundary components, to the position-space estimate

\[
\boxed{
\int_0^{L_n}
\|(B_{n,r})^*\psi_{n,t}\|^2\,dt
\lesssim
\frac{1+\log P_n}{P_n^2}.
}
\tag{6}
\]

The same statement applies to the shear-deleted intrinsic angle block after it has been placed in the normalized physical `L/H` Hilbert coordinates used by PF-320: construct the packet orbit from an orthonormal Fourier basis of that normalized low sector and apply (2)--(3).

Two immediate consequences are useful for falsification.

First, for every center `t`,

\[
\boxed{
\|B^*\psi_t\|^2\le\|B\|_{\mathcal S_2}^2.
}
\tag{7}
\]

Hence the PF-318 endpoint budget forces **every** unit packet in this translation orbit to obey

\[
\boxed{
\|B_{n,r}^*\psi_{n,t}\|
\lesssim
\frac{\sqrt{1+\log P_n}}{P_n}.
}
\tag{8}
\]

Second, for every measurable set of centers `E_n subset R/L_n Z`,

\[
\boxed{
\frac m{L_n}
\int_{E_n}\|(B_{n,r})^*\psi_{n,t}\|^2dt
\le
\|B_{n,r}\|_{\mathcal S_2}^2.
}
\tag{9}
\]

Therefore a fixed-width physical window on which the completed packet response has a nonvanishing lower bound contributes order-one Hilbert--Schmidt mass. More generally, (9) gives the exact price of any response profile on the PF-323/PF-324 critical windows.

## 1. Translation orthogonality gives the identity exactly

Expand

\[
B^*\psi_t
=\frac1{\sqrt m}
\sum_{1\le |k|\le N}
e^{-2\pi i kt/L}B^*e_k.
\]

Then

\[
\begin{aligned}
\frac1L\int_0^L\|B^*\psi_t\|^2dt
&=\frac1m
\sum_{j,k}
\left(
\frac1L\int_0^L e^{2\pi i(j-k)t/L}dt
\right)
\langle B^*e_j,B^*e_k\rangle\\
&=\frac1m\sum_k\|B^*e_k\|^2\\
&=\frac1m\|B\|_{\mathcal S_2}^2.
\end{aligned}
\tag{10}
\]

No PDE estimate, asymptotic orthogonality, or translation invariance of `B` is used. The pant operator may depend strongly on position; only the exact Fourier orthogonality of the packet orbit is needed.

If one local PF module has a fixed finite number of low boundary components, apply (10) to each component and sum. This produces the full local Hilbert--Schmidt mass with only a fixed multiplicative bookkeeping constant.

## 2. The logarithmic target rank disappears into physical length

PF-212/PF-317 give

\[
\dim\mathcal L_{\kappa,L_n}=m_n=O(1+L_n)
=O(1+\log P_n).
\]

That logarithmic rank is exactly what PF-318 pays in its Fourier-basis criterion. Equation (3) shows what it means geometrically. Because

\[
m_n/L_n\to\kappa/\pi,
\]

the rank factor is simply the density of fixed-band states per unit physical cuff length. Passing from the discrete Fourier basis to packet centers therefore does not weaken the endpoint estimate: the Fourier sum becomes a physical-position integral at constant density.

This is useful because the difficult coefficients in PF-322--PF-324 are already localized in the physical cuff coordinate. A proof of (6) can split the long cuff into regions where the compactified coefficient is perturbative, critical, or boundary-dominated and estimate the packet response in the representation natural to each region, rather than requiring a worst-case estimate on every Fourier row.

## 3. Relation to the PF-323 critical packet

Ignoring the harmless choice of phase convention, the raw trigonometric polynomial in (1) is exactly the shifted nonconstant Dirichlet packet used in PF-322--PF-323. In raw `L^2(ds)` coordinates,

\[
\psi_t(s)
=\frac1{\sqrt{2NL}}
\sum_{1\le |k|\le N}
e^{2\pi i k(s-t)/L},
\tag{11}
\]

so the PF-323 packet is obtained by taking

\[
t=\tau_{n,\lambda}.
\]

There is, however, an important coordinate boundary. PF-317's seam-energy normalization is a Fourier-diagonal operator, and PF-320's intrinsic angle adds positive diagonal normalization inside the low/high sectors. A unit packet in the final normalized angle coordinates therefore need not be literally the raw `L^2` packet (11); pulling it back can change the fixed Fourier amplitudes even though translation still changes only their phases.

Accordingly, PF-325 does **not** assert that PF-323's raw unit packet is already a unit vector for the completed intrinsic angle. The correct use is:

- build the translation orbit in the exact normalized low Hilbert space to obtain the tight identity (2)--(3);
- pull that orbit back through the known Fourier-diagonal seam normalization when comparing with PF-323's compactification calculation;
- keep the non-translation-invariant pant completion inside `B`, where (10) requires no commutation.

This isolates rather than hides the remaining issue. Seam normalization changes the packet profile by an explicit mode multiplier; the pant response is the genuinely geometric part that must be estimated.

## 4. The PF-324 two-regime test becomes an integrated response test

PF-324 shows that the distinguished critical center has outgoing seam distance

\[
D_{n,\lambda}
=\log\frac{1+r_n}{\lambda}+o(1),
\qquad
r_n=\frac{h_{n+1}}{h_n},
\]

with source-realized subsequences on which the boundary remains at finite critical distance and others on which it escapes.

Equation (6) says that the PF-318 fallback is not a separate abstract singular-value problem after those regimes are examined. It is the integral of the squared completed packet response over **all** centers. The two PF-324 centers are particularly discriminating sample locations inside that integral, while fixed neighborhoods of those centers test whether a whole critical region contributes excessive Hilbert--Schmidt mass.

In particular, if a completed critical packet at one of the PF-324 centers has response larger than the right side of (8), then the PF-318 fallback already fails for that local block, regardless of whether the stronger PF-321 operator-norm target was being pursued. If a pointwise obstruction is absent, (6) gives the positive route: prove that the entire packet-response profile has the required small integrated mass.

The independent conditional channel `T_H` remains untouched.

## Prior-art and novelty audit

The identity (10) is classical Fourier orthogonality/Parseval in continuous-frame language. Translation or group orbits producing tight harmonic frames are standard in frame theory, and no novelty is claimed for that abstract mechanism. A targeted literature check found only the general harmonic/tight-frame framework and the classical Dirichlet-kernel/Fourier identities; none is needed as an imported theorem because (10) is a three-line finite Fourier calculation. `SOURCES.md` therefore needs no new dependency.

The project-specific contribution is the **exact change of diagnostic for the live Prime-Flute endpoint**: PF-318's logarithmic-rank Hilbert--Schmidt sum is equivalent to a constant-density physical-position integral of the same fixed-band packet family that PF-322--PF-324 use to probe the compactification-critical geometry. This is not a new general frame theorem; it is a new reduction of the current local PDE obligation into a representation aligned with the canonical geometric witness.

## Boundaries and falsification

1. **No angle lower bound is proved.** PF-325 supplies an exact accounting identity. It does not show that a PF-323 packet survives the finite-pant quotient, seam normalization, physical projection, or common completion.
2. **Use the correct normalized coordinates.** The exact tight identity applies to equal-amplitude translates of an orthonormal Fourier basis in the Hilbert space on which the tested block acts. Raw `L^2` packets and intrinsic-angle-normalized packets must not be silently identified.
3. **A single large unit response is already enough to falsify the HS budget.** Equation (7) is elementary but load-bearing: no averaging loophole can hide a packet whose completed response exceeds `O(sqrt(log P_n)/P_n)`.
4. **An isolated small response proves little.** The positive PF-318 route needs the integrated estimate (6), not merely smallness at the distinguished PF-324 center.
5. **Fixed bandwidth is essential.** The constant-density relation (4) uses fixed `kappa`. A growing physical cutoff changes the frame density and the endpoint bookkeeping.
6. **No translation symmetry of the pant is assumed.** All position dependence remains in `t mapsto B^*psi_t`; (10) is valid even when the completed pant geometry strongly breaks translation invariance.

## Consequence for the research line

The direct-angle calculation now has a spatially localized endpoint test. Continue to propagate the PF-323 critical family through the exact seam normalization and PF-320 common completion, separately in PF-324's finite-boundary and escaping-boundary regimes, but record the resulting response as a function of packet center. The stronger PF-321 route asks for uniform superlinear seam-scale decay; the PF-318 fallback asks exactly for the integrated square budget (6). This removes the need to treat the fallback as a separate opaque Fourier-row calculation.