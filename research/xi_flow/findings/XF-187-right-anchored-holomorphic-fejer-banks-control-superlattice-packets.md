---
type: theorem
research_line: xi_flow
finding_id: XF-187
status: canonical
---

# XF-187 — Right-anchored holomorphic Fejer banks control super-lattice packets

**Evidence classification:** CLASSICAL-SEPARATED-FOURIER-FRAME + EXACT-QUADRATIC-JACOBI-RECIPROCITY-ESTIMATE + EXPLICIT-PHYSICAL-CONDITIONING-BOUND. XF-185 establishes a uniform linearized holomorphic Jacobi frame for a known consecutive square-lattice packet of size $m\le N$, anchored at its leftmost squared radius. Its stated obstruction when $m\gg N$ is exponential attenuation of the far endpoint under that particular anchor. Moving the real damping anchor to the **rightmost** squared radius eliminates this attenuation. For every fixed $0<\varepsilon<1$, the resulting full consecutive-frequency Fejer bank stays uniformly conditioned in *normalized squared-radius displacement coordinates* throughout $N\le m\le N^{2-\varepsilon}$. The sample count increases to $O(m^2/N)$; the reciprocal Jacobi term is uniformly negligible in the indicated regime. This is a linearized, known-window theorem, not an extension of XF-186's nonlinear constant-physical-cell result. In fact, the physical-displacement condition number of this particular bank has a lower bound of order $m/N$.

## Statement

Fix $\alpha>0$ and $0<\varepsilon<1$. Let $N,m$ be integers with

\[
N\ge N_0(\alpha,\varepsilon),\qquad N\le m\le N^{2-\varepsilon}.
\tag{1}
\]

Set

\[
\lambda_j=(N+j)^2\ (1\le j\le m),\quad
A=(N+1)^2,\quad C=(N+m)^2,\quad
D=2N+m+1,\quad R=C-A=(m-1)D.
\tag{2}
\]

Use the same linearized Jacobi defect $G_N(x)h$ as XF-185: for
$\mu_j(h)=\lambda_j+Rh_j$,

\[
D_{N,h}(x)=2\sum_{j=1}^m
\bigl(e^{-\pi\mu_j(h)x}-e^{-\pi\lambda_jx}\bigr),\quad
{\cal J}_{N,h}(x)=D_{N,h}(x)-x^{-1/2}D_{N,h}(1/x),\quad
G_N(x)h=\left.\frac{d}{dt}{\cal J}_{N,th}(x)\right|_{t=0},
\tag{3}
\]

with $\Re x>0$ and the principal square-root branch.

Retain the exact quadratic torus-node spacing

\[
y_j=\frac{(m-1)(\lambda_j-A)}{mR}
=\frac{(j-1)(2N+j+1)}{m(2N+m+1)},\qquad
\delta=\min_{j\ne k}\operatorname{dist}_{\mathbb T}(y_j-y_k,0)
=\frac{2N+3}{m(2N+m+1)}.
\tag{4}
\]

Put $\omega=2\pi(m-1)/m$, $L=\lceil2/\delta\rceil$,
$M=2L-1$, and $w_\ell=1-|\ell-L|/L$ for $1\le\ell\le M$.
The **right-anchored** samples and normalized linear map are

\[
x_\ell=\frac{\alpha}{\pi C}
+i\frac{\ell\omega}{\pi R},\qquad
(B^{\rm right}_{N,m}h)_\ell
=-\sqrt{w_\ell}\,
\frac{e^{\pi Cx_\ell}}{2\pi Rx_\ell}\,
G_N(x_\ell)h .
\tag{5}
\]

There are constants $0<c_\alpha<C_\alpha<\infty$, independent of
$N,m$ and $\varepsilon$, and an onset $N_0(\alpha,\varepsilon)$ such that

\[
\boxed{\quad
c_\alpha\sqrt L\,\|h\|_2
\le \|B^{\rm right}_{N,m}h\|_2
\le C_\alpha\sqrt L\,\|h\|_2
\quad(h\in\mathbb R^m).
\quad}
\tag{6}
\]

Moreover,

\[
L\le 4m^2/N+1,\qquad M\le8m^2/N+1.
\tag{7}
\]

Writing $G^{\rm raw}_{N,m}h=(G_N(x_\ell)h)_{\ell=1}^M$,
the diagonal row normalizer in (5) obeys

\[
\|Q^{\rm right}\|_{2\to2}\le \frac{e^\alpha}{2\pi},
\qquad
\|G^{\rm raw}_{N,m}h\|_2
\ge 2\pi e^{-\alpha}c_\alpha\sqrt L\,\|h\|_2 .
\tag{8}
\]

This is raw *linear* lower visibility for the declared
squared-radius coordinate; it is not a claim of uniform sensitivity
to one unit of physical displacement.

Indeed, for infinitesimal physical displacements
$\lambda_j(\eta)=(N+j+\eta_j)^2$,
the normalized Jacobian is
$B^{\rm phys}=B^{\rm right}_{N,m}
\operatorname{diag}(2(N+j)/R)$. It satisfies

\[
\boxed{\quad
\kappa_2(B^{\rm phys})\ \ge\
\frac{1}{2e^\alpha+1}\frac{N+m}{N+1}.
\quad}
\tag{9}
\]

Thus this **single right-anchored bank** is not uniformly
conditioned in Euclidean physical displacement when $m/N\to\infty$.

## 1. Exact separation and sampling cost

The formula (4) is valid without the restriction $m\le N$:
successive nodes have gaps

\[
y_{j+1}-y_j=\frac{2N+2j+1}{mD}
\quad(1\le j<m),
\]

which increase with $j$, whereas the circular wrap gap is $1/m$.
Hence the minimum is the first gap $(2N+3)/(mD)$.
For $m\ge N$ one has $D=2N+m+1\le4m$ and
$2N+3\ge2N$, so

\[
L\le 2mD/(2N+3)+1\le4m^2/N+1.
\]

This proves (7). Crucially, $L\delta\ge2$ still holds even
when the earliest phase gaps are much smaller than $1/m$.
The bound is a sufficient cost for this consecutive-frequency
construction, not a universal lower bound on the number of
complex samples or a claim about optimally selected rows.

## 2. Right anchoring removes distant-column attenuation

Differentiating (3), the direct contribution to the normalized
matrix (5) is exactly

\[
(B^{\rm dir})_{\ell j}
=\sqrt{w_\ell}\,
e^{\pi(C-\lambda_j)x_\ell}
=\sqrt{w_\ell}\,d_j\,
e^{\,i\ell\omega(C-\lambda_j)/R},
\qquad
d_j=\exp\{\alpha(1-\lambda_j/C)\}.
\tag{10}
\]

Because $A\le\lambda_j\le C$, every column weight now obeys

\[
1\le d_j\le e^\alpha,
\tag{11}
\]

independently of the ratio $m/N$. The phases differ from the
Fejer torus phases $e^{-2\pi i\ell y_j}$ only by a unit-modulus
factor common to each row.

For the centered triangular weights,
$\sum_{\ell=1}^{2L-1}w_\ell e^{-2\pi i\ell t}
=e^{-2\pi iLt}F_L(t)$,
where $F_L$ is the classical Fejer kernel. If
$q=\min(|j-k|,m-|j-k|)$, the shortest circular arc
contains at least $q$ gaps of size $\delta$, whence
$\operatorname{dist}_{\mathbb T}(y_j-y_k,0)\ge q\delta$.
Using $|\sin(\pi t)|\ge2\operatorname{dist}_{\mathbb T}(t,0)$
and at most two columns per $q$, the sum of normalized absolute
off-diagonal Gram entries is at most

\[
\rho\le\frac{\pi^2}{12L^2\delta^2}
\le\frac{\pi^2}{48}<1.
\tag{12}
\]

Gershgorin and (11) therefore give the **direct** frame bounds

\[
\sqrt{L(1-\rho)}\,\|h\|_2
\le\|B^{\rm dir}h\|_2
\le e^\alpha\sqrt{L(1+\rho)}\,\|h\|_2 .
\tag{13}
\]

No new general Vandermonde or superresolution theorem is claimed
in this step.

## 3. The reciprocal image remains negligible below the quadratic-width threshold

The reciprocal derivative in $G_N$ contributes, after
multiplication by the row factor in (5),

\[
E_{\ell j}
=-\sqrt{w_\ell}\,e^{\pi Cx_\ell}
x_\ell^{-5/2}e^{-\pi\lambda_j/x_\ell}
\quad\text{where }B^{\rm right}=B^{\rm dir}+E .
\tag{14}
\]

Here the branch is inherited from (3); only its modulus is used.
Since $m\ge N\ge2$ and $R=(m-1)D$,

\[
\frac LR
\le\frac{2m}{(m-1)(2N+3)}+\frac1R
\le\frac3N.
\tag{15}
\]

Consequently, for every row,
$|\Im x_\ell|\le4L/R\le12/N$ and
$0<\Re x_\ell=\alpha/(\pi C)\le\alpha/N$.
Also $|x_\ell|\ge\omega/(\pi R)\ge1/R$.
Thus

\[
\frac1R\le|x_\ell|\le\frac{12+\alpha}{N},
\qquad
R\le4m^2,\quad C\le4N^{4-2\varepsilon}.
\tag{16}
\]

The reciprocal Gaussian exponent is *exactly*

\[
\Re\left(\frac{\pi\lambda_j}{x_\ell}\right)
=\frac{\alpha\lambda_j}{C|x_\ell|^2}
\ge
\frac{\alpha}{4(12+\alpha)^2}N^{2\varepsilon}
=:c_\alpha' N^{2\varepsilon}.
\tag{17}
\]

Using (14), (16), $M\le9m^2/N$, and the Frobenius bound,

\[
\begin{aligned}
\|E\|_{2\to2}
&\le e^\alpha R^{5/2}\sqrt{Mm}\,
       e^{-c_\alpha' N^{2\varepsilon}}\\
&\le C_\alpha'
     \frac{m^{13/2}}{\sqrt N}
       e^{-c_\alpha' N^{2\varepsilon}}
\le C_\alpha' N^{13}e^{-c_\alpha'N^{2\varepsilon}}
=o(1)
\end{aligned}
\tag{18}
\]

uniformly in the admitted $m$. For sufficiently large
$N_0(\alpha,\varepsilon)$ this error is smaller than
$\tfrac12\sqrt{L(1-\rho)}$.
Equation (6) follows from (13), for instance with
$c_\alpha=\tfrac12\sqrt{1-\pi^2/48}$ and
$C_\alpha=e^\alpha\sqrt{1+\pi^2/48}+1$.

For the raw transfer, let
$Q^{\rm right}_{\ell\ell}
=-\sqrt{w_\ell}e^{\pi Cx_\ell}/(2\pi Rx_\ell)$.
Its modulus is at most
$e^\alpha/(2|\pi Rx_\ell|)\le e^\alpha/(2\pi)$,
because $|\pi Rx_\ell|\ge\ell\omega\ge\pi$.
Thus $B^{\rm right}=Q^{\rm right}G^{\rm raw}$ implies (8).
Unlike an inverse normalization, this estimate charges the exact
operator norm on arbitrary raw observation noise.

The upper width restriction is an honest boundary of this
argument. For $m$ comparable to or larger than $N^2$, the
minimum reciprocal exponent in (17) need not dominate the
polynomial prefactor in (18). Nothing here proves the frame
fails in that regime; this particular perturbative suppression
proof merely stops applying.

## 4. Physical displacement exposes a remaining conditioning loss

For a physical perturbation $\eta_j$ one has
$\partial_{\eta_j}\lambda_j=2(N+j)$, so the chain rule gives
$B^{\rm phys}=B^{\rm right}\operatorname{diag}(2(N+j)/R)$.
The direct column norms of $B^{\rm right}$ are exactly
$\sqrt L\,d_j$; (18) makes each reciprocal column correction
$o(\sqrt L)$, uniformly in $j$.

At the right endpoint $d_m=1$, while at the left endpoint
$d_1\le e^\alpha$. Increasing $N_0$ if necessary ensures
$\|E\|\le\tfrac12\sqrt L$. Therefore

\[
\frac{\|B^{\rm phys}e_m\|_2}
{\|B^{\rm phys}e_1\|_2}
\ge\frac{N+m}{N+1}
\frac{1-1/2}{e^\alpha+1/2}
=\frac{N+m}{(N+1)(2e^\alpha+1)}.
\tag{19}
\]

Since for any full-column-rank matrix the spectral condition
number is at least the ratio of the norms of any two columns,
(19) proves (9). The normalized $h$-coordinate absorbs the
different derivatives of $(N+j)^2$. Such a change of metric
must not be reported as uniformly conditioned recovery of
equal-sized *physical* lattice displacements.

## Scope, controls, and prior-art boundary

The result uses a **known single consecutive window**,
a linearization at the unperturbed square lattice, and direct
right-half-plane complex Jacobi samples. It does not give an
unknown-support locator, nonlinear stability on a constant
physical cell, weight robustness, an analytic-continuation
algorithm from noisy positive-real samples, or any Xi-zero
transition implication. The lower-bound loss (9) concerns
this particular right-anchored bank, not all possible
measurement designs. When $m\gg N$, one may still need
overlapping recentered frames or an adaptive multi-scale
physical metric.

The Fourier separation/conditioning input is classical:
Moitra, *Super-resolution, Extremal Functions and the
Condition Number of Vandermonde Matrices* (STOC 2015,
DOI 10.1145/2746539.2746561), and Aubel--Bölcskei,
*Vandermonde Matrices with Nodes in the Unit Disk and the
Large Sieve* (ACHA 2019, DOI 10.1016/j.acha.2017.07.006),
already delimit the generic prior-art territory and are
recorded in this line's SOURCES.md. The specific new
line-local step is the **right endpoint damping dictionary**
(10)--(11) together with the exact quadratic-grid
high-frequency cost (7), full Jacobi reciprocal control
(14)--(18), raw row-gain audit (8), and the physical-coordinate
boundary (9). This finding is not an RH proof or an upper
bound on the de Bruijn--Newman constant.

XF-185's left-anchored $m\le N$ bank remains useful and
XF-186's nonlinear theorem remains restricted to that
regime. Right anchoring allows larger *normalized linear*
packets at a larger sampling cost, but does not remove the
physical scaling barrier or the missing source-to-zero bridge.
