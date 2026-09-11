---
type: theorem
research_line: xi_flow
finding_id: XF-184
status: canonical
---

# XF-184 — Mesoscopic complex Jacobi phases remove the remote packet acquisition barrier

**Evidence classification:** `CLASSICAL-FOURIER-MECHANISM + EXACT-DERIVED + ASYMPTOTIC-DFT + UNIFORM-LOCAL-INVERSE`. XF-182--XF-183 expose a sharp obstruction only for **positive-real** Jacobi acquisition: at `x~N^-2` a remote `m`-atom packet survives with polynomial amplitude but its internal geometry collapses into the ladder `N^-1,...,N^-m`, while at the resolving real scale `x~N^-1` the packet geometry is well conditioned only after division by an `exp(-Theta(N))` reference. This tradeoff is not intrinsic to the holomorphic Jacobi source. A right-half-plane sample can use its real part to control Gaussian damping and its imaginary part to resolve the packet. For a fixed consecutive `m`-atom Xi packet, taking `Re x~N^-2` and `Im x~N^-1` gives an `m`-sample complex acquisition bank whose absolute linearized singular values stay bounded above and below independently of the remote index. After only bounded row renormalization, the bank converges to the discrete Fourier transform and its condition number tends to one. The reciprocal Jacobi image is `exp(-Theta_m(N^2))`, so it does not restore the positive-real loss. Thus the XF-183 exponential denominator is a boundary of the positive-real information model, not an information-theoretic obstruction for the holomorphic theta/Jacobi source.

## Statement

Fix

\[
m\ge2,\qquad \alpha>0.
\tag{1}
\]

For `N>=m`, retain the consecutive Xi squared radii and affine packet coordinates of XF-180--XF-183,

\[
\lambda_j=(N+j)^2,\qquad
A=(N+1)^2,
\qquad
R=(N+m)^2-(N+1)^2,
\tag{2}
\]

\[
u_j=\frac{\lambda_j-A}{R},
\qquad
a_N=\frac AR.
\tag{3}
\]

Then

\[
0=u_1<\cdots<u_m=1,
\qquad
u_j\longrightarrow \frac{j-1}{m-1},
\qquad
a_N\sim\frac{N}{2(m-1)}.
\tag{4}
\]

For a normalized location displacement `h=(h_1,...,h_m)`, put

\[
\mu_j(h)=A+R(u_j+h_j)
\tag{5}
\]

and define the finite-packet heat defect and Jacobi residual, with the principal square-root branch on `Re x>0`,

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
D_{N,h}(x)
-
x^{-1/2}D_{N,h}(1/x).
\tag{7}
\]

Both sides are holomorphic for `Re x>0`. Let

\[
\omega_m:=\frac{2\pi(m-1)}m
\tag{8}
\]

and, for `1<=ell<=m`, choose the anisotropic complex samples

\[
\boxed{
x_{N,\ell}
=
\frac{\alpha}{\pi A}
+
i\,\frac{\ell\omega_m}{\pi R}.
}
\tag{9}
\]

Equivalently, with

\[
s_{N,\ell}:=\pi R x_{N,\ell}
=
\frac{\alpha}{a_N}
+
i\ell\omega_m,
\tag{10}
\]

one has

\[
\pi A x_{N,\ell}=a_Ns_{N,\ell}
=
\alpha+i\,a_N\ell\omega_m.
\tag{11}
\]

Thus the remote Gaussian carrier has the exact fixed modulus

\[
\boxed{
|e^{-\pi A x_{N,\ell}}|=e^{-\alpha},
}
\tag{12}
\]

while the normalized packet separation is already order one because

\[
\operatorname{Im}(\pi R x_{N,\ell})
=
\ell\omega_m.
\tag{13}
\]

Let `G_N(x):R^m->C` be the linearization

\[
G_N(x)h
:=
\left.
\frac{d}{d\varepsilon}
\mathcal J_{N,\varepsilon h}(x)
\right|_{\varepsilon=0}.
\tag{14}
\]

Define the boundedly row-normalized `m x m` acquisition matrix `C_N` by

\[
(C_Nh)_\ell
:=
-\frac{e^{a_Ns_{N,\ell}}}{2s_{N,\ell}}
G_N(x_{N,\ell})h.
\tag{15}
\]

The normalization in `(15)` has no remote-index gain:

\[
\left|e^{a_Ns_{N,\ell}}\right|=e^\alpha,
\qquad
|s_{N,\ell}|\asymp_{m,\alpha}1.
\tag{16}
\]

Then

\[
\boxed{
(C_N)_{\ell j}
=
e^{-u_js_{N,\ell}}
+
O_{m,\alpha}\!\left(
N^{5/2}e^{-c_{m,\alpha}N^2}
\right)
}
\tag{17}
\]

uniformly in `ell,j`, and hence

\[
\boxed{
C_N
\longrightarrow
F_m,
\qquad
(F_m)_{\ell j}
=
e^{-2\pi i\ell(j-1)/m}.
}
\tag{18}
\]

The limiting matrix is the discrete Fourier matrix, with rows indexed by `1,...,m`. Therefore

\[
F_m^*F_m=mI_m
\tag{19}
\]

and

\[
\boxed{
\frac{s_r(C_N)}{\sqrt m}\longrightarrow1
\quad(1\le r\le m),
\qquad
\kappa_2(C_N)\longrightarrow1.
}
\tag{20}
\]

In particular, for all sufficiently large `N`,

\[
\boxed{
c_{m,\alpha}\|h\|_2
\le
\|C_Nh\|_2
\le
C_{m,\alpha}\|h\|_2
}
\tag{21}
\]

with constants independent of the remote index.

The same statement holds in the XF-181 adapted cusp basis. If `Q_N` is the orthogonal matrix whose columns are the directions `q^(0),...,q^(m-1)`, then the adapted acquisition matrix is `C_NQ_N`, so it has exactly the same singular values. Consequently **all `m` adapted packet modes have order-one absolute complex-Jacobi visibility**. The graded positive-real spectrum `N^-1,...,N^-m` of XF-182 disappears without dividing by an exponentially small packet reference.

Even the unnormalized complex bank has no `N`-dependent loss. Let

\[
(M_N)_{\ell k}
=
G_N(x_{N,\ell})q^{(k)}.
\tag{22}
\]

Since `(15)` differs from `(22)` only by row factors with fixed nonzero moduli `2|s_(N,ell)|e^(-alpha)`, equations `(20)--(21)` imply

\[
\boxed{
\|M_N\|_2=\Theta_{m,\alpha}(1),
\qquad
\|M_N^{-1}\|_2=\Theta_{m,\alpha}(1),
\qquad
\kappa_2(M_N)=O_{m,\alpha}(1).
}
\tag{23}
\]

Thus no hidden `e^(Theta(N))` normalization is being used.

## 1. The complex direction separates Gaussian survival from packet resolution

The direct part of `(14)` is the complex continuation of the exact XF-182 formula. For arbitrary `h`,

\[
G_N^{\rm dir}(x)h
=
-2\pi Rx\,e^{-\pi Ax}
\sum_{j=1}^m h_je^{-\pi Ru_jx}.
\tag{24}
\]

Writing `s=pi R x` gives

\[
\boxed{
G_N^{\rm dir}(x)h
=
-2s\,e^{-a_Ns}
\sum_j h_je^{-u_js}.
}
\tag{25}
\]

On the positive real axis, the same scalar `s` controls both effects. Keeping `a_Ns=O(1)` forces `s=O(N^-1)` and collapses the normalized packet, while keeping `s=Theta(1)` makes `e^(-a_Ns)=e^(-Theta(N))`. That is exactly the XF-182--XF-183 tradeoff.

For `(9)`, the two jobs are split between the two components of `s`. Its real part is

\[
\operatorname{Re}s_{N,\ell}=\frac{\alpha}{a_N},
\tag{26}
\]

so `a_N Re s=alpha` and the Gaussian modulus is constant. Its imaginary part is

\[
\operatorname{Im}s_{N,\ell}=\ell\omega_m=\Theta_m(1),
\tag{27}
\]

so consecutive packet positions acquire order-one relative phase. There is therefore no contradiction with the positive-real optimization in XF-182: the escape uses a genuinely different acquisition geometry, not a better choice of real scale.

The anisotropy is explicit in the original variable:

\[
\boxed{
\operatorname{Re}x_{N,\ell}=\Theta_m(N^{-2}),
\qquad
\operatorname{Im}x_{N,\ell}=\Theta_m(N^{-1}).
}
\tag{28}
\]

The real part is the atom-survival scale of XF-182; the imaginary part is the packet-width resolution scale of XF-183.

## 2. The packet geometry becomes an asymptotic Fourier frame

Apply the bounded row normalization `(15)` to the direct term `(25)`. One obtains exactly

\[
(C_N^{\rm dir}h)_\ell
=
\sum_{j=1}^m h_je^{-u_js_{N,\ell}}.
\tag{29}
\]

As `N->infinity`, equations `(4)` and `(10)` give

\[
e^{-u_js_{N,\ell}}
\longrightarrow
\exp\!\left(
-i\frac{j-1}{m-1}\,
\ell\frac{2\pi(m-1)}m
\right)
=
e^{-2\pi i\ell(j-1)/m}.
\tag{30}
\]

Thus the limiting packet acquisition is not merely nonsingular; it is exactly a Fourier basis. The special phase spacing `(8)` is chosen so that the asymptotically equispaced normalized Xi packet maps to the `m`th roots of unity. Continuity of singular values already proves `(20)` for the direct matrix.

This also gives a transparent stress test against hidden moment cancellation. A direction can annihilate arbitrarily many low **real** Taylor moments of the packet, as in XF-178 and the high adapted modes of XF-182, but it cannot annihilate all `m` Fourier samples `(30)` unless the `m`-vector itself vanishes. The complex bank reads the packet across its full normalized spatial bandwidth instead of reconstructing that bandwidth from a collapsing Taylor jet.

The mechanism is classical at the finite exponential-sum level: complex Laplace samples combine damping with Fourier phase, and Fourier/Prony sampling of finite exponential sums is standard. The line-specific statement is the exact Xi scaling `(9)` and the fact that it lands on a DFT limit while retaining constant absolute carrier amplitude.

## 3. The reciprocal Jacobi image remains exponentially negligible

It remains necessary to check that complexifying `x` does not awaken the reciprocal image. The reciprocal part of the linearized Jacobi residual is

\[
G_N^{\rm rec}(x)h
=
2\pi R x^{-3/2}
e^{-\pi A/x}
\sum_{j=1}^m
h_j e^{-\pi Ru_j/x}.
\tag{31}
\]

For `x=s/(pi R)` with `s=s_(N,ell)`, `Re s>0` and therefore `Re(1/x)>0`. Moreover

\[
\operatorname{Re}\!\left(\frac{\pi A}{x}\right)
=
\pi^2AR\,
\frac{\operatorname{Re}s}{|s|^2}
=
\boxed{
\frac{\pi^2\alpha R^2}{|s|^2}.
}
\tag{32}
\]

Since `1<=ell<=m`, the denominator in `(32)` is bounded above by a constant depending only on `m,alpha`. Hence

\[
\operatorname{Re}\!\left(\frac{\pi A}{x_{N,\ell}}\right)
\ge
c_{m,\alpha}R^2
\asymp_m N^2.
\tag{33}
\]

Also `Re(pi R/x)>0`, so for `u_j>=0` the final sum in `(31)` is bounded by `||h||_1`. Finally `|x|^(-3/2)=O_(m,alpha)(R^(3/2))`. After the bounded normalization `(15)`,

\[
\boxed{
\|C_N-C_N^{\rm dir}\|_2
\le
C_{m,\alpha}
N^{5/2}e^{-c_{m,\alpha}N^2}.
}
\tag{34}
\]

This proves `(17)--(20)`. The reciprocal image is less suppressed than the `e^(-Theta(N^3))` image at the real packet-width scale of XF-183, but it is still Gaussian-small and completely negligible relative to the order-one direct complex signal.

## 4. The improvement survives a fixed nonlinear packet neighborhood

The DFT limit is not only an infinitesimal artifact. Define the normalized nonlinear observation map

\[
\mathcal F_N(h)_\ell
:=
-\frac{e^{a_Ns_{N,\ell}}}{2s_{N,\ell}}
\mathcal J_{N,h}(x_{N,\ell}).
\tag{35}
\]

Its direct part is exactly

\[
\mathcal F_N^{\rm dir}(h)_\ell
=
-\frac1{s_{N,\ell}}
\sum_{j=1}^m
\left(
e^{-(u_j+h_j)s_{N,\ell}}
-
e^{-u_js_{N,\ell}}
\right),
\tag{36}
\]

and therefore

\[
D\mathcal F_N^{\rm dir}(0)=C_N^{\rm dir}.
\tag{37}
\]

For `||h||_infinity<=rho`, the direct Jacobian differs from `(37)` by `O_(m,alpha)(rho)`. If `rho` is chosen sufficiently small depending only on `m,alpha`, all perturbed squared radii remain positive and ordered for the corresponding ordered sub-neighborhood, while the reciprocal Jacobian remains `O(N^(5/2)e^(-cN^2))`. Combining this with `(20)` gives constants

\[
\rho_{m,\alpha}>0,
\qquad
0<c_{m,\alpha}<C_{m,\alpha}<\infty
\tag{38}
\]

such that, for all sufficiently large `N` and all `h,h'` in the ordered cube `||h||_infinity,||h'||_infinity<=rho_(m,alpha)`,

\[
\boxed{
c_{m,\alpha}\|h-h'\|_2
\le
\|\mathcal F_N(h)-\mathcal F_N(h')\|_2
\le
C_{m,\alpha}\|h-h'\|_2.
}
\tag{39}
\]

Thus a fixed-complexity remote packet has a genuinely remote-index-uniform local inverse from this complex right-half-plane bank. The result is not limited to a formal first-order distinguishability statement.

## Stress tests and boundaries

The right-half-plane hypothesis is essential. It makes both the direct theta sums and their reciprocal images absolutely controlled and fixes the principal square-root branch. No sample crosses `Re x=0`; `(9)` stays strictly inside the holomorphy domain.

The result does **not** contradict XF-182 or XF-183. Those findings optimize or normalize observations on the positive real axis. Equation `(28)` uses a phase direction larger than its damping direction by a factor `Theta(N)`, which is unavailable in a one-parameter positive-real sample. The complex bank therefore changes the admitted information topology.

For the same reason, `(23)` must not be read as a free stability theorem from approximate positive-real data. Analytic continuation from noisy values on `x>0` to points with `Im x/Re x=Theta(N)` can be severely ill-conditioned. If the only source input is an additive real-axis estimate, the XF-182--XF-183 barriers can reappear in the continuation step. The gain is legitimate only when the source supplies the holomorphic value directly — as the exact theta series does — or when a modular/arithmetic identity controls the required complex samples before additive error is introduced.

The packet location and fixed packet complexity `m` are still known. The theorem does not discover an unknown support window, give an `m`-uniform inverse, or defeat the unbounded-complexity controls of XF-178. It also does not connect complex source acquisition to a positive-`Lambda` transition. Stable source discrimination and transition-sensitive zero geometry remain separate gates.

## Prior-art and novelty audit

Nothing in the finite-dimensional Fourier step is new in isolation. Prony-type reconstruction of finite exponential sums from complex/Fourier samples is classical; modern generalized Prony formulations explicitly treat sparse exponential expansions and deterministic sample recovery. Likewise, holomorphy and modular transformation of the Jacobi theta function in its complex half-plane are classical.

A focused search did not identify a result matching the specific Xi-flow statement needed here: the consecutive squared-lattice scaling `A~N^2`, width `R~N`, anisotropic right-half-plane sampling `Re x~A^-1`, `Im x~R^-1`, asymptotic DFT acquisition of the XF-181 packet modes, and simultaneous `e^(-Theta(N^2))` suppression of the reciprocal Jacobi image. Those pieces are derived directly above. Because no external theorem is load-bearing for `(17)--(39)`, `SOURCES.md` needs no new dependency.

The novelty boundary should therefore be read conservatively. The **mechanism** “use complex exponential samples to separate damping from phase resolution” is classical. The durable Xi-flow contribution is the exact placement of that mechanism against the positive-real acquisition barrier of XF-182--XF-183.

## Consequence for the Xi-flow frontier

XF-183 leaves two apparent source-side escapes: acquire a remote tail relatively before additive error, or restrict admissible packet complexity. XF-184 adds a third, and for every fixed packet complexity it is strictly cheaper at the acquisition level: **complex right-half-plane theta/Jacobi samples acquire the full packet at order-one absolute scale, with no exponentially small denominator and no `N^-m` mode ladder.**

The next gate is therefore no longer finite-packet observability. It is an interface question. One must determine whether the exact Xi theta/modular source can feed these anisotropic complex samples into a zero-sensitive estimate for the de Bruijn--Newman flow without paying an equally bad analytic-continuation or target-conditioning cost. A theorem that accesses `(9)` directly from the source would cross the acquisition barrier rather than renormalize it; a theorem that first approximates only the positive real axis and then continues analytically has not yet done so.

This distinction also reconnects the source program with the earlier off-real observability lesson of XF-130: phase-bearing complex observations can compress a large real family of moments when their geometric reach is admitted. Here the same principle occurs on the theta-source side, with a quantified remote-packet scale and an exact DFT limit. What remains is to prove that this stronger source topology is transported by an admissible Xi-flow identity rather than merely available algebraically.
