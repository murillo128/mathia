# NB-269 — Resolved multi-shell Hardy projection compresses a shallow matched Ford residue into a `1/K` center spike

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + HARDY-PROJECTED-MULTI-SHELL-GRAM + DISJOINT-CARRIER-BAND-ORTHOGONALITY + UNIFORM-POSITIVE-CARRIER + SHALLOW-MATCHED-CONTROL + VANISHING-HARD-WINDOW-ENERGY + NARROW-CENTER-SPIKE + NB-268-REFINEMENT + DESTINATION-INTERFACE + METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-268` separates the logarithmic-mesh `ell^1` obstruction of `NB-267` from a diagonal quadratic diagnostic: the uniform resolved carrier can retain the forced linear mass while its damped sample energy tends to zero. The live question was whether the **actual Hardy-projected Ford Gram form** restores order-one energy through off-diagonal interactions.

For the resolved `H`-separated multi-shell dictionary there is an exact answer at the `NB-250` hard-window level. After the legal `NB-249` Hardy projection, moving the observation center by the normalized coordinate

\[
z:=H(t-t_0)
\]

puts shell `j` on the center-frequency band

\[
j+\operatorname{supp}\phi.
\]

Because `diam(supp phi)<1`, these bands are pairwise disjoint. Full-line Plancherel therefore diagonalizes the shell index **exactly**:

\[
\boxed{
\int_{\mathbb R}|G_J^{(c)}(z)|^2\,dz
=
2\pi\sum_{j=0}^{K-1}|c_j|^2
\int_a^b |\phi(u)|^2|A_{j,J}(u)|^2\,du.
}
\]

Thus the hard-window Gram may contain cross-shell terms, but their total positive contribution can never exceed this diagonal full-line quantity.

Apply this identity to the uniform positive carrier of `NB-261`,

\[
c_j=\frac1K,
\qquad
J=mK,
\qquad
m\to\infty,
\qquad
K\to\infty,
\]

and to the same shallow matched packet at

\[
X(1-\beta)=\log m+d_*,
\qquad
\gamma_n-t_0=\frac{2\pi qn}{X},
\qquad
0\le n<M\asymp m.
\]

For sufficiently small fixed packet density, every resolved shell sees an order-one projected packet amplitude. Hence the full-line energy is

\[
\boxed{
\int_{\mathbb R}|G_J^{\rm pkt}(z)|^2\,dz
\asymp \frac1K.
}
\]

Moreover the same common-sector argument remains valid for `|z|<=c/K`, so the current itself stays order one on that interval. Therefore for every fixed hard-window radius `A>0`,

\[
\boxed{
\int_{-A}^{A}|G_J^{\rm pkt}(z)|^2\,dz
\asymp \frac1K
\longrightarrow0,
\qquad
|G_J^{\rm pkt}(0)|\gg1.
}
\]

There is no contradiction. The multi-shell source has normalized center bandwidth `Theta(K)`, so an order-one value may be compressed into a center spike of width `Theta(1/K)`. In the original center variable this is width `Theta(1/(KH))`, exactly the reciprocal of the physical multi-shell span. The single-shell hard-window-to-pointwise bridge of `NB-246`/`NB-247` is therefore not rank-uniform: after `K` resolved bands are introduced, the evaluation cost grows by `Theta(K)`.

This is a stronger route correction than the diagonal diagnostic in `NB-268`. For this explicit legal matched control, even the exact `NB-250` Hardy-projected hard-window quadratic form tends to zero. A generic positive off-diagonal Gram rescue at this stage is therefore impossible. This still does **not** say that the full Nyman distance tends to zero, and the packet remains a compatibility control rather than a claim about the actual zeros of zeta.

## 1. Exact multi-shell projected current

Retain the Ford normalization used in `NB-249`--`NB-268`,

\[
R=Q^{2/3}(\log Q)^{1/3},
\qquad
Y=\frac XR\asymp1,
\qquad
J=\frac RH\to\infty,
\]

and fix

\[
0<a<b<1,
\qquad
0\le\phi\in C_c^\infty((a,b)),
\qquad
\phi\not\equiv0,
\qquad
b-a<1.
\]

For `0<=j<K`, put the shell center at `X+jH`. As in `NB-255`, `NB-257`, and `NB-261`, let `c_j` denote the **Euler-normalized** coefficient and use the physical source coefficient

\[
e^{rjH/X}c_j.
\]

For a zero `rho=beta+i gamma`, define at the frozen center `t_0`

\[
d_\rho:=X(1-\beta)-\log J,
\qquad
\tau_\rho:=H(\gamma-t_0),
\]

\[
\theta_\rho:=H(1-\beta)
=\frac{\log J+d_\rho}{YJ},
\qquad
\eta_\rho:=H(1+r/X-\beta)
=\theta_\rho+\frac r{YJ}.
\]

The physical Euler renormalization cancels the artificial `r/X` displacement on the shell offset exactly:

\[
e^{rjH/X}
 e^{-jH(1+r/X-\beta)}
=
e^{-j\theta_\rho}.
\]

This is the same cancellation behind the legal complex carrier coordinate in `NB-255` and `NB-261`.

Use a finite ordinate cutoff `psi_L` as in `NB-250`. For the depth cutoff, allow a smooth compact cutoff `chi_J` depending on the rank and equal to one on the live packet. This point matters: the shallow packet below has

\[
d_\rho=-\log K+d_*+o(1),
\]

so a fixed cutoff supported at bounded `d` would not see it. The `NB-249` Hardy projection identity is exact for every smooth compact depth cutoff separately; translating the cutoff with `J` changes only which zeros are selected, and the cumulative projection still returns the factor `chi_J(d_rho)`.

After performing that legal positive-frequency projection **before squaring**, and after demodulating the common carrier `X`, the center-moving finite current is

\[
\boxed{
G_{J,L}^{(c)}(z)
=
\sum_{j=0}^{K-1}c_j
\int_a^b
\phi(u)A_{j,J,L}(u)e^{-i(j+u)z}\,du,
}
\tag{1}
\]

where

\[
\boxed{
A_{j,J,L}(u)
=
\frac{e^{-r}}J
\sum_\rho
m(\rho)e^{-d_\rho}
\chi_J(d_\rho)\psi_L(\tau_\rho)
 e^{-u\eta_\rho-j\theta_\rho}
 e^{i(YJ+j+u)\tau_\rho}.
}
\tag{2}
\]

To see the center frequency in (1) directly, move

\[
t=t_0+\frac zH.
\]

Then `tau_rho` becomes `tau_rho-z`. The large factor `e^{iYJ tau}` contributes the common phase `e^{-iYJz}`, which is demodulated exactly as in `NB-246` and `NB-250`; the shell offset contributes `e^{-ijz}` and the internal shell coordinate contributes `e^{-iuz}`. Hence the residual center frequency is exactly `j+u`.

Equation (1) is therefore not a heuristic decomposition of the Gram form. It is the direct multi-shell extension of the legally projected current in `NB-249`/`NB-250`.

## 2. Disjoint shell bands diagonalize the full-line Hardy energy

For each shell define

\[
g_j(z):=
\int_a^b\phi(u)A_{j,J,L}(u)e^{-i(j+u)z}\,du.
\]

Its Fourier support is contained in

\[
j+\operatorname{supp}\phi.
\]

Since `diam(supp phi)<1`, these sets are pairwise disjoint for distinct integer `j`. Orthogonality in the center-frequency variable is therefore exact. With the Fourier convention in `NB-250`, Plancherel gives

\[
\boxed{
\int_{\mathbb R}
|G_{J,L}^{(c)}(z)|^2\,dz
=
2\pi
\sum_{j=0}^{K-1}|c_j|^2
\int_a^b
|\phi(u)|^2|A_{j,J,L}(u)|^2\,du.
}
\tag{3}
\]

No estimate on cross-shell phases is required: they vanish from the **full-line** Gram form because the frequency cells are disjoint.

For a fixed hard window

\[
I_{A,L}^{(c)}:=
\int_{-A}^{A}|G_{J,L}^{(c)}(z)|^2\,dz,
\]

positivity immediately gives

\[
\boxed{
I_{A,L}^{(c)}
\le
2\pi
\sum_j|c_j|^2
\int_a^b|\phi(u)|^2|A_{j,J,L}(u)|^2\,du.
}
\tag{4}
\]

The hard-window expansion itself does contain off-diagonal shell terms, just as the zero expansion contains off-diagonal zero terms. Equation (4) shows that those terms cannot manufacture more total hard-window energy than is present in the orthogonal full-line decomposition.

This is the exact Gram calculation left open by the route diagnosis in `NB-268` for the resolved shell direction.

## 3. The shallow matched packet has order-one amplitude in every channel

Now specialize to the positive uniform family from `NB-261`. Suppress harmless floor errors and write

\[
J=mK,
\qquad
m\to\infty,
\qquad
K\to\infty,
\qquad
c_j=\frac1K.
\tag{5}
\]

Take the matched compatibility packet

\[
M=\lfloor\delta m\rfloor,
\qquad
\gamma_n-t_0=\frac{2\pi qn}{X},
\qquad
0\le n<M,
\tag{6}
\]

at common depth

\[
X(1-\beta)=\log m+d_*.
\tag{7}
\]

Here `q>=1` and `d_*` are fixed, while `delta>0` will be chosen sufficiently small. The corresponding Ford coordinates satisfy

\[
d_*^{(J)}
:=X(1-\beta)-\log J
=-\log K+d_*.
\tag{8}
\]

Choose `chi_J=1` at this depth and `psi_L=1` on the finite packet. Because

\[
\frac{e^{-r-d_*^{(J)}}}{J}
=
\frac{e^{-r-d_*}}m,
\tag{9}
\]

and because

\[
\tau_n
=H(\gamma_n-t_0)
=\frac{2\pi qn}{YJ},
\tag{10}
\]

while `e^{iYJ tau_n}=e^{2pi iqn}=1`, the packet part of (2) is exactly

\[
\boxed{
A_j^{\rm pkt}(u)
=
\frac{e^{-r-d_*}}m
 e^{-u\eta_*-j\theta_*}
\sum_{n=0}^{M-1}
 e^{i(j+u)\tau_n},
}
\tag{11}
\]

with

\[
\theta_*
=
\frac{\log m+d_*}{YJ},
\qquad
\eta_*
=
\theta_*+\frac r{YJ}.
\tag{12}
\]

The largest imaginary attenuation across the resolved dictionary is

\[
K\theta_*
=
\frac{\log m+d_*}{Ym}
=o(1).
\tag{13}
\]

The largest phase sweep in (11) is, uniformly for `0<=j<K`, `u in supp phi`, and `n<M`,

\[
|(j+u)\tau_n|
\le
\frac{2\pi q\delta}{Y}+o(1).
\tag{14}
\]

Since `Y` stays in a fixed compact subset of `(0,infinity)`, choose `delta` so small that the right side is strictly below a fixed angle `<pi/4`. All summands in (11) then remain in one common right half-plane. Consequently there are constants `0<c_1<c_2<infinity`, independent of `j` and `J`, such that for all sufficiently large `J`,

\[
\boxed{
c_1
\le
|A_j^{\rm pkt}(u)|
\le
c_2
}
\tag{15}
\]

uniformly on `u in supp phi`.

Substituting (15) and `c_j=1/K` into (3) yields

\[
\boxed{
\int_{\mathbb R}|G_J^{\rm pkt}(z)|^2\,dz
\asymp
\frac1{K^2}\sum_{j<K}1
\asymp
\frac1K.
}
\tag{16}
\]

Therefore every fixed hard window satisfies the upper bound

\[
I_A^{\rm pkt}=O(K^{-1}).
\tag{17}
\]

## 4. The hard-window energy is exactly of spike scale

The upper bound (17) is not merely leaking energy to large `|z|`. The same packet has an order-one spike near the selected center.

Expand (1) and (11). Up to fixed positive factors, the phases of the packet integrand are

\[
e^{i(j+u)(\tau_n-z)}.
\]

At `z=0`, the common-sector estimate (14) gives the `NB-261` pointwise lower bound. More generally choose a fixed `c>0` so small that, together with the previous choice of `delta`,

\[
|(j+u)(\tau_n-z)|<\frac\pi3
\]

for all packet indices whenever

\[
|z|\le\frac cK.
\]

The damping factors are positive and equal to `1+o(1)` uniformly, and `phi>=0`. Hence the real part of the complete packet current remains bounded below on this shrinking center interval:

\[
\boxed{
\inf_{|z|\le c/K}
|G_J^{\rm pkt}(z)|
\ge c_0>0.
}
\tag{18}
\]

For every fixed `A>0`, the interval `[-c/K,c/K]` is eventually contained in `[-A,A]`. Thus

\[
I_A^{\rm pkt}
\ge
\int_{-c/K}^{c/K}|G_J^{\rm pkt}(z)|^2\,dz
\gg
\frac1K.
\tag{19}
\]

Combining (17) and (19) gives the sharp hard-window scale

\[
\boxed{
I_A^{\rm pkt}
\asymp
\frac1K
\longrightarrow0,
\qquad
|G_J^{\rm pkt}(0)|\gg1.
}
\tag{20}
\]

The apparent tension is exactly bandwidth concentration. The union of the shell-frequency cells spans `Theta(K)` in the normalized center frequency, so a point evaluation can cost `Theta(K)` in squared norm. Schematically the single-shell reproducing estimate becomes

\[
\boxed{
|G_J^{(c)}(0)|^2
\lesssim
K\int_{\mathbb R}|G_J^{(c)}(z)|^2\,dz,
}
\tag{21}
\]

with the same scaling for a localized reproducing kernel. Equation (20) saturates that rank factor at the level of order of magnitude.

In the original center variable, `z=H(t-t_0)`, the spike width is

\[
\Delta t\asymp\frac1{KH}.
\tag{22}
\]

Since the physical carrier span is `W\asymp KH`, this is precisely the reciprocal span `1/W` already singled out by the positivity/coherence analysis in `NB-254` and `NB-261`. The pointwise Ford obstruction has not disappeared; it has been compressed to the uncertainty scale created by the enlarged legal carrier support.

## 5. Relation to `NB-251`, `NB-267`, and `NB-268`

`NB-251` found, at the level of a bandwidth-only control, that the `NB-231` matched-packet energy dies once the tested carrier bandwidth is a diverging multiple of `H`. At that stage no legal Mellin operation producing the required bandwidth had been identified. The resolved multi-shell dictionary supplies such a legal realization: its total span is `KH`, and because the component bands are disjoint, Plancherel turns that span into an exact `ell^2` averaging gain.

The later pointwise results `NB-253`--`NB-267` remain correct. They show that scalar recombination cannot make the selected residue uniformly small: the obstruction migrates to a shallower boundary layer, and Euler-anchor reconstruction still forces aggregate response. Equation (20) shows why that does not automatically yield quadratic hard-window coercivity. A residue can remain order one at the selected center while occupying only a `1/K` fraction of a fixed normalized center window.

`NB-268` exhibited vanishing **diagonal sample energy** on the logarithmic carrier-locked mesh, with scale `Theta(1/m)` after damping. The quantity in (20) is different: it is the exact moving-center Hardy-projected hard-window norm of the finite matched current, and its scale is `Theta(1/K)`. The two decay rates measure different directions of the geometry and should not be identified. What is common is the conclusion: neither aggregate mesh `ell^1` mass nor generic quadratic positivity by itself supplies an order-one destination lower bound.

Most importantly, (3)--(4) rule out one possible repair proposed after `NB-268`: **cross-shell off-diagonal terms in the `NB-250` hard-window Gram cannot restore an order-one floor for this resolved uniform control**, because the entire hard-window norm is bounded by a full-line norm of order `1/K`.

## 6. Prior art, boundaries, and surviving target

The generic ingredients are classical: Mellin/Hardy formulations of the Nyman--Beurling criterion, Plancherel orthogonality for disjoint frequency supports, and the elementary concentration behavior of finite Fourier blocks. Báez-Duarte's 2002 paper *New versions of the Nyman--Beurling criterion for the Riemann hypothesis* is a standard anchor for Nyman--Beurling approximation, while recent work such as Hugh Carvill's 2025 preprint on Beurling--Nyman Gram structure studies Mellin-smoothed off-diagonal Gram decay. A fresh targeted search did not locate the specific rank-coupled statement here: the exact Ford moving-center Hardy projection of an `H`-resolved multi-shell source, combined with the `X(1-beta)=log(J/K)+O(1)` shallow matched packet and the resulting `Theta(1/K)` hard-window energy. This is a prior-art boundary, not a claim that the generic Fourier ingredients are new. No external theorem is load-bearing, so `SOURCES.md` needs no new dependency.

Several nonclaims are essential.

First, the shallow packet is a **matched compatibility control**. It is compatible with the imported zero-free and counting ledger used in `NB-261`; it is not a theorem that the zeros of zeta occupy those sites.

Second, (20) is an exact statement about the `NB-249`/`NB-250` **Hardy-projected Ford current** after the selected finite depth/ordinate localization. It is not a proof that the complete Nyman--Beurling approximation error is `O(1/K)`. Other target terms, global coupling, or arithmetic restrictions on the actual zero set may still enforce a lower bound.

Third, the moving depth cutoff is not cosmetic. A fixed bounded-`d` cutoff from the original critical-layer calculation would miss the shallow packet because `d=-log K+d_*`. The projection calculation is reused only in its valid form: for each `J`, a compact smooth cutoff equal to one on the live packet, after which the `NB-249` cumulative Hardy identity is exact.

Fourth, disjoint-band diagonalization requires the resolved geometry `diam(supp phi)<1` and `H`-spaced shell centers. Unresolved overlapping shells need a different Gram calculation. Signed/complex coefficients still satisfy the exact identity (3) under the same disjoint geometry, but the packet lower bound (18) uses the positive uniform control.

The next non-circular target is therefore no longer to search for a generic off-diagonal rescue **inside the `NB-250` local hard-window Gram**. This finding shows that such a rescue cannot hold uniformly over legal resolved carriers. The remaining bridge has to use structure outside this local norm: a rank-uniform coupling from the localized projected current to the full Nyman target, an arithmetic theorem excluding the concentrating shallow packet for the actual zeta zero set, or another destination invariant that charges center concentration rather than only integrated energy.

## Consequence

The source-side obstruction and the quadratic destination diagnostic now have a precise uncertainty relation. Enlarging the legal resolved carrier span to `W\asymp KH` preserves an order-one matched Ford residue but allows it to concentrate on center width `1/W`. The exact hard-window energy then falls like `1/K`.

So the obstacle left after `NB-268` is not an unidentified positive Gram cross term. It is the absence of a **rank-uniform bridge from pointwise/shallow Ford obstruction to the complete Nyman distance**. Any continuation of this route should attack that bridge directly rather than attempting to recover order-one energy from the already-diagonalized local multi-shell Hardy form.