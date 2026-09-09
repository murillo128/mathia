# XF-130 — one root-spacing off-circle heat trace determines the entire unit-circle divisor

**Status:** `EXACT-DERIVED` + `STRUCTURAL/POSITIVE-BOUNDARY` + `POINT-OBSERVABILITY` + `CROSS-SCALE` + `ROOT-SPACING-OFF-CIRCLE`. XF-124--XF-128 show that many coordinatewise power-sum interfaces remain collision-blind, while XF-129 proves that the complete upper half of the harmonic heat histories is universally identifying. The next source-facing question is whether that `Theta(N)` family of harmonic channels can be replaced by a physically simpler observable that still mixes enough Vieta shells to cross the collision-identifiability boundary.

It can, at the exact periodic level. Let

\[
E(w,0)=\prod_{j=1}^N(1+\nu_j w)=\sum_{k=0}^N E_k w^k,
\qquad |\nu_j|=1,
\tag{1}
\]

and evolve by the XF-067 normalized coefficient heat flow

\[
E(w,s)=\sum_{k=0}^N E_k e^{-\delta_k s}w^k,
\qquad
\delta_k=\alpha k(N-k),
\qquad \alpha>0.
\tag{2}
\]

Fix any nonzero observation point `zeta` with

\[
|\zeta|\ne1
\tag{3}
\]

and observe only the single complex scalar heat trace

\[
\boxed{
Q_\zeta(s):=E(\zeta,s),\qquad s\ge0.
}
\tag{4}
\]

Then `Q_zeta` determines every coefficient `E_0,...,E_N`, hence the complete target root multiset with multiplicity. In particular, if two unit-circle targets have the same normalized one-point trace, then they have identical collision geometry and identical periodic transition time.

Moreover the observation point need not be macroscopically far from the unit circle. Taking

\[
|\zeta_N|=e^{\sigma/N},\qquad \sigma\ne0\ \text{fixed},
\tag{5}
\]

keeps the shell-pair inversion polynomially conditioned: its worst spatial amplification is only `O_sigma(N)`. Through the physical trigonometric representation of XF-067, `(5)` is a vertical displacement of order `L/N`, i.e. one root-spacing scale. Thus the `Theta(N)` high-harmonic histories of XF-129 admit an exact **single-spatial-channel** replacement: one normalized heat trace at a point only `Theta(L/N)` off the real line.

## 1. A one-point trace separates the heat spectrum into reflected Vieta pairs

The heat rates satisfy

\[
\delta_k=\delta_{N-k}
\tag{6}
\]

and are strictly increasing for

\[
0\le k\le \lfloor N/2\rfloor.
\tag{7}
\]

Therefore `(4)` can be grouped as a finite exponential sum with distinct rates,

\[
\boxed{
Q_\zeta(s)
=\sum_{k=0}^{\lfloor N/2\rfloor}
B_k(\zeta)e^{-\delta_k s}.
}
\tag{8}
\]

The amplitudes are

\[
B_0=1+E_N\zeta^N,
\tag{9}
\]

\[
B_k=E_k\zeta^k+E_{N-k}\zeta^{N-k},
\qquad 1\le k<N/2,
\tag{10}
\]

and, when `N=2c`,

\[
B_c=E_c\zeta^c.
\tag{11}
\]

Because the rates in `(8)` are known and distinct, the complete scalar history uniquely determines every `B_k`. One explicit extraction is successive tail peeling:

\[
B_0=\lim_{s\to\infty}Q_\zeta(s),
\tag{12}
\]

and, after subtracting the already recovered slower modes,

\[
B_k
=\lim_{s\to\infty}
 e^{\delta_k s}
 \left(
 Q_\zeta(s)-\sum_{j<k}B_j e^{-\delta_j s}
 \right).
\tag{13}
\]

The infinite-time notation is not essential. Since `(8)` has only `M=\lfloor N/2\rfloor+1` known distinct exponents, the jet

\[
Q_\zeta(s_*),Q_\zeta'(s_*),\ldots,Q_\zeta^{(M-1)}(s_*)
\tag{14}
\]

at any one heat time `s_*` also determines all amplitudes through the corresponding Vandermonde system. Likewise, equality of two traces on any nonempty open heat-time interval implies equality of all amplitudes.

Thus the only nontrivial issue is the exact degeneracy `(6)`: a point trace sees the pair `(k,N-k)` through one complex amplitude `B_k`. The unit-circle geometry supplies precisely the missing relation.

## 2. Moving the observation point off the unit circle breaks the reflected-shell degeneracy

For a unit-circle target, XF-067/XF-129 give the self-inversive identity

\[
\boxed{
E_{N-k}=E_N\overline{E_k},
\qquad |E_N|=1.
}
\tag{15}
\]

The zero-rate amplitude immediately gives

\[
\boxed{
E_N=\frac{B_0-1}{\zeta^N}.
}
\tag{16}
\]

Fix `1<=k<N/2`, put `x=E_k`, and use `(15)` in `(10)`:

\[
B_k=a_k x+b_k\overline{x},
\qquad
a_k:=\zeta^k,
\qquad
b_k:=E_N\zeta^{N-k}.
\tag{17}
\]

Together with its conjugate this is a real-linear `2x2` system. Its determinant is

\[
\boxed{
D_k
=|a_k|^2-|b_k|^2
=|\zeta|^{2k}-|\zeta|^{2(N-k)}.
}
\tag{18}
\]

Since `k<N/2`, condition `(3)` gives `D_k\ne0`. Hence

\[
\boxed{
E_k
=
\frac{\overline{a_k}B_k-b_k\overline{B_k}}
{|a_k|^2-|b_k|^2},
\qquad
E_{N-k}=E_N\overline{E_k}.
}
\tag{19}
\]

If `N=2c`, the central shell is not paired and `(11)` gives directly

\[
E_c=\frac{B_c}{\zeta^c}.
\tag{20}
\]

Equations `(16)`, `(19)`, and `(20)` recover every Vieta coefficient. The target polynomial and its root multiset are therefore uniquely determined.

This also identifies why a genuinely off-circle sample is structurally useful. On `|zeta|=1`, every determinant `(18)` vanishes: a single spatial sample sees only one real projection of each self-inversive pair. Moving even infinitesimally off the circle turns those projections into invertible real-linear coordinates.

## 3. One root-spacing of complex displacement is already enough, with only linear spatial conditioning

Exact invertibility by itself would be less useful if it required a fixed radial displacement, because a fixed `|zeta|-1` corresponds to an imaginary displacement of order the full period `L`. Instead choose

\[
|\zeta_N|=r_N=e^{\sigma/N},
\qquad \sigma\ne0
\tag{21}
\]\nwith `sigma` fixed. For `k<N/2`, write `h=N-2k>=1`. Then `(18)` becomes

\[
|D_k|
=r_N^{2k}\left|1-r_N^{2h}\right|.
\tag{22}
\]

All powers of `r_N` are bounded above and below by constants depending only on `sigma`, while on `1<=h<=N`

\[
\left|1-e^{2\sigma h/N}\right|
\ge c_\sigma\frac{h}{N}.
\tag{23}
\]

Consequently

\[
\boxed{
|D_k|\ge c_\sigma\frac{N-2k}{N},
}
\tag{24}
\]

and the real-linear inversion in `(19)` has amplification at most

\[
\boxed{
C_\sigma\frac{N}{N-2k}\le C_\sigma N.
}
\tag{25}
\]

The worst conditioning occurs only at the shell immediately adjacent to the center. Recovering `E_N` in `(16)` and the even central shell in `(20)` costs only fixed factors because `r_N^N=e^\sigma` and `r_N^{N/2}=e^{\sigma/2}`.

Thus the spatial symmetry breaking needed for exact tomography can be made microscopically small while paying only a polynomial, not exponential, price. This is substantially better aligned with the Xi window than a fixed-radius off-circle probe.

The estimate `(25)` concerns only the **spatial reflected-pair inversion**. Extracting the amplitudes `B_k` from noisy or finite-time data in `(8)` is a separate spectral-conditioning problem; no uniform Xi-scale stability for that temporal inversion is claimed here.

## 4. In physical periodic coordinates the probe is one near-real complex value

XF-067 writes the periodic heat representative as

\[
G(z,s)
=A_0(s)e^{\pi iNz/L}
\sum_{k=0}^N
E_k(s)\left(-e^{-2\pi iz/L}\right)^k.
\tag{26}
\]

Therefore, for a purely imaginary physical displacement `z=iy`,

\[
\boxed{
\frac{G(iy,s)}{A_0(s)e^{-\pi Ny/L}}
=Q_{\zeta}(s),
\qquad
\zeta=-e^{2\pi y/L}.
}
\tag{27}
\]

Choose

\[
y_N=\frac{\sigma L}{2\pi N}.
\tag{28}
\]

Then `|zeta|=e^{sigma/N}` exactly as in `(21)`. If the mean root spacing is

\[
\ell=\frac LN,
\tag{29}
\]

this is simply

\[
\boxed{
|y_N|=\frac{|\sigma|}{2\pi}\ell.
}
\tag{30}
\]

At the current Xi scaling `ell asy 1/log T`, the observation point is only `Theta(1/log T)` off the real line. No evaluation at a period seam or at imaginary height `Theta(L)` is needed.

This gives the exact periodic meaning of the compression: instead of separately observing `Theta(N)` root harmonics as in XF-129, observe one normalized value of the periodic heat solution at one nearby complex point through heat time. The off-real displacement mixes all Vieta shells at once, while their distinct heat rates spectrally separate the reflected pairs.

## 5. Consequence for collision and transition identifiability

Suppose two unit-circle target slices `E` and `E_tilde` satisfy

\[
Q_\zeta(s)=\widetilde Q_\zeta(s)
\qquad\text{for all }s\ge0
\tag{31}
\]

at one fixed `zeta` with `|zeta|!=1`. Sections 1--2 force

\[
E_k=\widetilde E_k
\qquad(0\le k\le N).
\tag{32}
\]

Hence the target polynomials agree exactly, not merely up to the even central rotation left by XF-129. Their coefficient heat trajectories then agree at every real time under the diagonal XF-067 evolution. In particular,

\[
\boxed{
Q_\zeta(\cdot)=\widetilde Q_\zeta(\cdot)
\Longrightarrow
\Lambda_{\rm per}(E)=\Lambda_{\rm per}(\widetilde E).
}
\tag{33}
\]

The collision-blind controls of XF-120--XF-128 therefore cannot match this observable unless they match the entire divisor. There is no contradiction with their lower bounds: a one-point off-circle heat trace is not a sparse set of root harmonics. It is a global cross-scale mixture of **all** Vieta shells, with heat time acting as the spectral decoder.

This is the first exact positive interface after XF-129 that reduces the number of spatial channels rather than merely moving the harmonic threshold. It answers the algebraic part of XF-129's final question: comparable upper-half Vieta information can be encoded in one physically local complex trace.

## 6. Prior-art boundary and the remaining Xi-specific gate

Recovering finitely many known exponential modes from a scalar time trace is a standard finite-dimensional observability/moment phenomenon, and self-inversive coefficient symmetry for unit-circle polynomials is classical. The literature audit found broad single-point observability results for parabolic equations and the classical self-inversive polynomial theory, but no external theorem is needed for `(8)`--`(25)`: the proof is the explicit finite spectral decomposition plus a `2x2` real-linear inversion. No new source is load-bearing, so `SOURCES.md` does not need a new anchor.

The line-specific point is the interaction of three structures already established inside `xi_flow`: the exact paired heat spectrum `delta_k=delta_{N-k}`, unit-circle self-inversivity, and the physical trigonometric representation. Their combination shows that the otherwise fatal reflected-rate degeneracy is broken by an off-real displacement of only one root-spacing scale, with worst spatial conditioning `O(N)`.

This is still a **periodic observability theorem**, not an Xi source theorem and not a bound on the actual de Bruijn--Newman constant. Equation `(27)` requires the normalized periodic carrier `G/A_0`, whereas the true source supplies the nonperiodic Xi heat solution. The next source-specific gate is therefore much narrower than controlling `Theta(N)` individual high harmonics: prove a relative localization/periodization estimate for a single normalized complex trace at

\[
|\operatorname{Im}z|\asymp L/N,
\tag{34}
\]

with enough quantitative control to survive the temporal spectral inversion and the `O(N)` reflected-pair conditioning. The accepted Gaussian-reference/localization route is naturally adjacent to this question, but the present result does not resolve that clue: normalization by the outer carrier, periodization error, and noisy finite-time observability remain open.