---
type: theorem
research_line: xi_flow
finding_id: XF-185
status: canonical
---

# XF-185 — Fejer-overcomplete complex Jacobi banks make lattice-scale packets uniformly observable

**Evidence classification:** `CLASSICAL-FEJER/FOURIER-FRAME-MECHANISM + EXACT-XI-GEOMETRY + UNIFORM-GROWING-COMPLEXITY-ACQUISITION`. XF-184 removes the remote-index loss for a **fixed** known consecutive Xi packet by using anisotropic right-half-plane Jacobi samples whose real part preserves the remote Gaussian carrier while their imaginary part resolves the packet. The remaining question is whether the constants necessarily deteriorate when the packet complexity grows. They do not on the natural lattice-scale regime. If a consecutive packet has `m` atoms beginning near index `N` with `2<=m<=N`, an explicit Fejer-weighted bank of at most `6m-1` complex Jacobi samples has linearized singular values comparable to `sqrt(m)` with constants independent of both `N` and `m`. The reciprocal Jacobi image remains `exp(-cN^2)` after the full growing bank is included, and the row normalization used in the proof has uniformly bounded operator norm, so the same lower visibility is already present in the raw complex samples. Thus fixed packet complexity in XF-184 is not an intrinsic barrier: for a known packet whose width is at most its lattice location, complexity is paid linearly in the number of mesoscopic holomorphic samples rather than through worsening remote conditioning.

## Statement

Fix `alpha>0`. Let

\[
N\ge m\ge2,
\tag{1}
\]

and consider the consecutive Xi squared radii

\[
\lambda_j=(N+j)^2,
\qquad 1\le j\le m.
\tag{2}
\]

Retain the affine packet coordinates of XF-180--XF-184,

\[
A=(N+1)^2,
\qquad
D=2N+m+1,
\qquad
R=(N+m)^2-(N+1)^2=(m-1)D,
\tag{3}
\]

\[
u_j=\frac{\lambda_j-A}{R},
\qquad
a=\frac AR.
\tag{4}
\]

For normalized location displacements `h=(h_1,...,h_m)`, set

\[
\mu_j(h)=A+R(u_j+h_j)
\tag{5}
\]

and define

\[
D_{N,h}(x)
=
2\sum_{j=1}^m
\left(
e^{-\pi\mu_j(h)x}
-
e^{-\pi\lambda_jx}
\right),
\tag{6}
\]

\[
\mathcal J_{N,h}(x)
=
D_{N,h}(x)-x^{-1/2}D_{N,h}(1/x),
\qquad \Re x>0,
\tag{7}
\]

with the principal square-root branch. Let

\[
G_N(x)h
:=
\left.
\frac{d}{d\varepsilon}
\mathcal J_{N,\varepsilon h}(x)
\right|_{\varepsilon=0}.
\tag{8}
\]

Define the phase spacing

\[
\omega_m:=\frac{2\pi(m-1)}m
\tag{9}
\]

and the rescaled phase nodes

\[
y_j:=\frac{m-1}{m}u_j.
\tag{10}
\]

They satisfy the exact formula

\[
\boxed{
y_j=
\frac{(j-1)(2N+j+1)}{m(2N+m+1)}
}
\tag{11}
\]

and the exact circular separation

\[
\boxed{
\delta_{N,m}:=
\min_{j\ne k}\operatorname{dist}_{\mathbb T}(y_j-y_k,0)
=
\frac{2N+3}{m(2N+m+1)}.
}
\tag{12}
\]

Choose

\[
L:=\left\lceil\frac{2}{\delta_{N,m}}\right\rceil,
\qquad
M:=2L-1,
\tag{13}
\]

and, for `1<=ell<=M`, take the anisotropic samples

\[
\boxed{
x_\ell=
\frac{\alpha}{\pi A}
+
i\frac{\ell\omega_m}{\pi R},
\qquad
s_\ell:=\pi R x_\ell=rac{\alpha}{a}+i\ell\omega_m.
}
\tag{14}
\]

Put the centered triangular weights

\[
w_\ell:=1-\frac{|\ell-L|}{L},
\qquad 1\le\ell\le2L-1.
\tag{15}
\]

Thus `0<w_ell<=1` and

\[
\sum_{\ell=1}^{M}w_\ell=L.
\tag{16}
\]

Define the weighted normalized acquisition bank `B_{N,m}:R^m->C^M` by

\[
\boxed{
(B_{N,m}h)_\ell
:=-\sqrt{w_\ell}
\frac{e^{as_\ell}}{2s_\ell}
G_N(x_\ell)h.
}
\tag{17}
\]

Then there are constants

\[
0<c_\alpha<C_\alpha<\infty,
\qquad N_0(\alpha)<\infty,
\tag{18}
\]

independent of `m`, such that for every `N>=N_0(alpha)` and every `2<=m<=N`,

\[
\boxed{
c_\alpha\sqrt L\,\|h\|_2
\le
\|B_{N,m}h\|_2
\le
C_\alpha\sqrt L\,\|h\|_2
\qquad(h\in\mathbb R^m).
}
\tag{19}
\]

In particular,

\[
\boxed{
\kappa_2(B_{N,m})\le C_\alpha/c_\alpha
}
\tag{20}
\]

uniformly in both the remote index and the packet complexity. Moreover the bank has linear size:

\[
\boxed{
L\le3m,
\qquad
M\le6m-1.
}
\tag{21}
\]

The normalization in `(17)` does not hide a growing gain. If `\mathcal G_{N,m}:R^m->C^M` denotes the raw bank

\[
(\mathcal G_{N,m}h)_\ell:=G_N(x_\ell)h,
\tag{22}
\]

then

\[
\boxed{
\|\mathcal G_{N,m}h\|_2
\ge
2\pi e^{-\alpha}\,
\|B_{N,m}h\|_2.
}
\tag{23}
\]

Thus the order-`sqrt(m)` lower visibility is already present in the unnormalized holomorphic Jacobi samples themselves.

## 1. The squared Xi lattice has an explicit phase separation at growing packet size

From `(2)--(4)`,

\[
u_j
=
\frac{(j-1)(2N+j+1)}{(m-1)(2N+m+1)}.
\tag{24}
\]

Multiplying by `(m-1)/m` gives `(11)`. Consecutive differences are therefore

\[
\boxed{
y_{j+1}-y_j
=
\frac{2N+2j+1}{m(2N+m+1)},
\qquad 1\le j<m.
}
\tag{25}
\]

They increase with `j`, so the smallest ordinary gap is the first one. At the wrap-around edge,

\[
1-y_m+y_1=\frac1m,
\tag{26}
\]

which is larger than the first gap. Hence `(12)` follows.

The restriction `m<=N` gives a simple uniform consequence. Since

\[
\delta_{N,m}^{-1}
=
m\frac{2N+m+1}{2N+3},
\tag{27}
\]

and `m<=N`,

\[
2(2N+m+1)<3(2N+3),
\tag{28}
\]

so

\[
\boxed{
\delta_{N,m}^{-1}<\frac{3m}{2}.
}
\tag{29}
\]

Equations `(13)` and `(29)` give `(21)`. Thus no hidden superlinear sample count is being introduced when the packet complexity grows.

There is also no growing attenuation across the packet. Since `u_j in [0,1]`, the direct column factor introduced below is

\[
d_j:=e^{-\alpha u_j/a}.
\tag{30}
\]

For `m<=N`,

\[
\frac RA
=
\frac{(m-1)(2N+m+1)}{(N+1)^2}
<3,
\tag{31}
\]

because the left side is increasing in `m` and, at `m=N`,

\[
3(N+1)^2-(N-1)(3N+1)=4(2N+1)>0.
\tag{32}
\]

Therefore

\[
\boxed{
e^{-3\alpha}\le d_j\le1.}
\tag{33}
\]

This is the growing-complexity analogue of the fixed-`m` bounded carrier factor in XF-184.

## 2. Fejer oversampling gives a uniform Fourier frame

The direct part of the linearized residual is exactly

\[
G_N^{\rm dir}(x)h
=
-2s e^{-as}
\sum_{j=1}^m h_j e^{-u_js},
\qquad s=\pi R x.
\tag{34}
\]

After `(17)`, its acquisition matrix has entries

\[
(B^{\rm dir}_{N,m})_{\ell j}
=
\sqrt{w_\ell}\,
e^{-u_js_\ell}
=
\sqrt{w_\ell}\,d_j
e^{-2\pi i\ell y_j}.
\tag{35}
\]

The centered triangular weights have the exact Fourier sum

\[
\sum_{\ell=1}^{2L-1}
w_\ell e^{-2\pi i\ell t}
=
e^{-2\pi iLt}F_L(t),
\tag{36}
\]

where

\[
F_L(t)
=
\frac1L
\left(
\frac{\sin(\pi Lt)}{\sin(\pi t)}
\right)^2
\tag{37}
\]

is the Fejer kernel. In particular, the diagonal Gram entries before the `d_j` column factors equal `L`.

For `j!=k`, let

\[
q:=\min(|j-k|,m-|j-k|).
\tag{38}
\]

Because every adjacent circular gap is at least `delta_(N,m)`,

\[
\operatorname{dist}_{\mathbb T}(y_j-y_k,0)
\ge q\delta_{N,m}.
\tag{39}
\]

Using

\[
|\sin(\pi t)|
\ge
2\operatorname{dist}_{\mathbb T}(t,0),
\tag{40}
\]

one obtains

\[
\frac{|F_L(y_j-y_k)|}{L}
\le
\frac{1}{4L^2\delta_{N,m}^2q^2}.
\tag{41}
\]

For each `q`, a fixed row has at most two columns at circular distance `q`. Hence the normalized off-diagonal row sum is at most

\[
\rho
:=
\frac1{2L^2\delta_{N,m}^2}
\sum_{q\ge1}\frac1{q^2}
=
\frac{\pi^2}{12L^2\delta_{N,m}^2}.
\tag{42}
\]

Since `L delta_(N,m)>=2`,

\[
\boxed{
\rho\le\frac{\pi^2}{48}<1.
}
\tag{43}
\]

Gershgorin applied to the normalized phase Gram matrix therefore gives

\[
L(1-\rho)I_m
\preceq
V^*WV
\preceq
L(1+\rho)I_m,
\tag{44}
\]

where `V_(ell j)=e^(-2 pi i ell y_j)` and `W=diag(w_ell)`. Combining `(33)` with `(44)` yields the explicit direct-bank bounds

\[
\boxed{
\sigma_{\min}(B^{\rm dir}_{N,m})
\ge
e^{-3\alpha}\sqrt{L(1-\rho)},
}
\tag{45}
\]

\[
\boxed{
\sigma_{\max}(B^{\rm dir}_{N,m})
\le
\sqrt{L(1+\rho)}.
}
\tag{46}
\]

Thus the fixed DFT limit of XF-184 is not needed once `m` grows. The exact phase separation of the squared lattice plus only constant-factor oversampling already gives a uniform Fourier frame.

## 3. The reciprocal Jacobi image remains Gaussian-small uniformly for `m<=N`

The sample geometry is still mesoscopic. From `(14)`,

\[
\Re x_\ell=\frac{\alpha}{\pi A}=\Theta_\alpha(N^{-2}).
\tag{47}
\]

Also `M<=6m-1`, `omega_m<2pi`, and

\[
R=(m-1)(2N+m+1)\ge mN,
\tag{48}
\]

so

\[
\boxed{
|\Im x_\ell|
\le
\frac{12}{N}
}
\tag{49}
\]

for all rows of the bank. Consequently

\[
|x_\ell|\le C_\alpha N^{-1}.
\tag{50}
\]

For the reciprocal linearized Jacobi term, the decisive exponent simplifies exactly because `Re x=alpha/(pi A)`:

\[
\operatorname{Re}\left(\frac{\pi A}{x_\ell}\right)
=
\frac{\pi A\Re x_\ell}{|x_\ell|^2}
=
\boxed{
\frac{\alpha}{|x_\ell|^2}
}
\ge
c_\alpha N^2.
\tag{51}
\]

The row normalization in `(17)` has fixed carrier modulus `|e^(as_ell)|=e^alpha`. The remaining reciprocal prefactor contributes at worst a polynomial power of `|x_ell|^(-1)`. Since `|s_ell|>=omega_m>=pi`, one also has

\[
|x_\ell|=\frac{|s_\ell|}{\pi R}\ge\frac1R,
\tag{52}
\]

and `m<=N` implies `R=O(N^2)`. Entrywise, therefore,

\[
|(B_{N,m}-B^{\rm dir}_{N,m})_{\ell j}|
\le
C_\alpha N^5 e^{-c_\alpha N^2}.
\tag{53}
\]

Because `M<=6N` and `m<=N`, the entire reciprocal perturbation satisfies

\[
\boxed{
\|B_{N,m}-B^{\rm dir}_{N,m}\|_2
\le
C_\alpha N^6e^{-c_\alpha N^2}.
}
\tag{54}
\]

This is negligible compared with the `sqrt(L)` lower singular value in `(45)`, uniformly over every `2<=m<=N`. Equations `(45)--(46)` and Weyl's singular-value perturbation bound prove `(19)--(20)` for sufficiently large `N`.

The key point is that growing the bank to `O(m)` rows never compensates the reciprocal Gaussian suppression. Even at the maximal admitted packet `m=N`, the polynomial matrix-size cost is swallowed by `e^(-cN^2)`.

## 4. The raw complex samples already contain the stable lower bound

It remains to exclude a normalization artifact analogous to the exponentially small denominator of XF-183. Write

\[
B_{N,m}=Q_{N,m}\mathcal G_{N,m},
\tag{55}
\]

where

\[
(Q_{N,m})_{\ell\ell}
=
-\sqrt{w_\ell}\,
\frac{e^{as_\ell}}{2s_\ell}.
\tag{56}
\]

Now

\[
|e^{as_\ell}|=e^\alpha,
\qquad
0<\sqrt{w_\ell}\le1,
\qquad
|s_\ell|\ge\omega_m\ge\pi.
\tag{57}
\]

Hence

\[
\boxed{
\|Q_{N,m}\|_{2\to2}
\le
\frac{e^\alpha}{2\pi}.
}
\tag{58}
\]

Equation `(23)` follows immediately from `(55)` and `(58)`. The proof is therefore not recovering a small signal by multiplying it with an `N`- or `m`-dependent gain. Fejer weighting only attenuates rows, and the carrier-removal factor has bounded modulus. Stable acquisition is genuinely present in the direct holomorphic source data.

This is the main structural difference from positive-real packet acquisition. On the real axis, survival and resolution are tied to the same scalar scale and one must choose between a collapsing Taylor jet and an exponentially small resolved packet. In the right half-plane, damping is controlled by `Re x` while phase resolution is controlled by `Im x`; once that split is admitted, increasing packet dimension up to the lattice location costs more samples but not worse conditioning.

## Stress tests and boundaries

The theorem includes the maximal lattice-scale case `m=N`. Then `R=Theta(N^2)`, the normalized nodes still have separation `delta=Theta(1/N)`, `L=Theta(N)`, and the bank has only `Theta(N)` rows. The direct frame constants remain absolute after the fixed `alpha` damping, while the reciprocal image remains Gaussian-small.

The restriction `m<=N` is structural for this single-anchor argument, not a claim of impossibility beyond it. When `m>>N`, the packet width satisfies `R/A~(m/N)^2`; a sample bank centered at the left edge then exponentially attenuates the far edge even though its Fourier phases remain available. A wider packet may need several overlapping recentered banks or a genuinely multiscale construction. XF-185 does not establish that such a tiling is globally compatible with Jacobi reciprocity.

The packet support window `[N+1,N+m]` and its cardinality are assumed known. The theorem does not discover where a deformation is located, separate several unknown packets, or infer complexity from the observations. It is also a linearized location-displacement theorem. Uniform nonlinear inversion for an `m`-dependent neighborhood, weight perturbations, packet merging, and interactions between many windows are not proved here.

All samples stay in the right half-plane and satisfy

\[
\Re x=\Theta(N^{-2}),
\qquad
|\Im x|=O(N^{-1}).
\tag{59}
\]

The result therefore requires direct access to the holomorphic theta/Jacobi source. Analytically continuing noisy positive-real data to these anisotropic points may be severely ill-conditioned; XF-182--XF-183 remain the relevant obstruction in that weaker information model.

Finally, no zero-location or transition-time conclusion is claimed. Source observability is only one side of the Xi-flow problem. A separate theorem must still connect an admissible source defect, observed in this complex bank, to a transition-sensitive zero quantity capable of excluding `Lambda>0`.

## Prior-art and novelty audit

The Fourier-frame mechanism is classical. Constant-factor oversampling of separated points on the unit circle, large-sieve bounds for Vandermonde matrices, and the associated super-resolution phase transition are standard harmonic-analysis territory. In particular, Moitra gives sharp separation-dependent conditioning bounds for rectangular Vandermonde matrices, and Aubel--Bolcskei give a modern large-sieve treatment and survey the Selberg--Moitra unit-circle estimates. Those sources are added to `SOURCES.md` as the durable prior-art boundary.

No external theorem is load-bearing for `(19)`: the Fejer kernel estimate `(36)--(43)` gives a self-contained frame proof. The Xi-flow content is narrower and specific: the exact squared-lattice phase geometry `(11)--(12)`, the anisotropic Jacobi sampling `(14)` that simultaneously keeps the remote carrier at order one, the uniform suppression `(54)` of the reciprocal Jacobi image while `m` grows with `N`, and the raw-sample no-gain check `(55)--(58)`. The result should therefore not be read as a new generic Vandermonde conditioning theorem.

## Consequence for the Xi-flow frontier

XF-184 left growing packet complexity as one possible obstruction after fixed-complexity complex acquisition became uniformly stable. XF-185 removes that obstruction throughout the natural **lattice-scale** regime `m<=N` for a known consecutive packet. The local packet dimension can grow linearly with its remote index without producing either a condition-number loss or an exponentially small absolute signal; one pays only `O(m)` mesoscopic complex samples.

The live gate is consequently more global than finite-packet conditioning. A source-side coercivity theorem must now locate or isolate the relevant windows, adapt to unknown complexity, control nonlinear and overlapping deformations, and transport the resulting holomorphic source information into a zero-sensitive Xi-flow quantity. Conversely, a future no-go result cannot cite growing finite packet dimension alone while remaining inside the admitted right-half-plane information model: it must exploit support uncertainty, super-lattice packet width, nonlinear coupling, or the downstream source-to-zero interface.
