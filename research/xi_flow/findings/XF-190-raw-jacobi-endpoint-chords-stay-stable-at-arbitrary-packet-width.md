---
type: theorem
research_line: xi_flow
finding_id: XF-190
status: canonical
---

# XF-190 — Raw Jacobi endpoint chords stay stable at arbitrary packet width

**Evidence classification:** EXACT-DERIVED + CLASSICAL-FOURIER-CHORD-BOUNDARY. In the raw (unnormalized) right-anchored Jacobi bank, physical displacements of a single known endpoint atom remain uniformly recoverable with no upper restriction on packet width. This replaces the narrower XF-189 theorem, whose restriction \(m\le N^{2-\varepsilon}\) came solely from discarding Gaussian suppression before taking a polynomial prefactor in the reciprocal-image estimate. The proof below keeps the Gaussian envelope and matches the finite-chord and infinitesimal regimes. It makes no claim about an unknown-support or multi-atom nonlinear inverse, nor about the de Bruijn--Newman constant.

## Statement and exact observation model

Fix \(\alpha>0\). For every integer \(N\ge N_0(\alpha)\) and **every integer \(m\ge N\), without any upper bound on \(m\)**, define

\[
p=N+m,\quad C=p^2,\quad D=2N+m+1,\quad R=(m-1)D,
\]
\[
\omega=\frac{2\pi(m-1)}m,\quad
L=\left\lceil\frac{2mD}{2N+3}\right\rceil,\quad
M=2L-1,\quad w_\ell=1-\frac{|\ell-L|}{L},
\]
\[
x_\ell=\frac{\alpha}{\pi C}+i\frac{\ell\omega}{\pi R},
\qquad 1\le\ell\le M,\qquad W=\operatorname{diag}(w_1,\ldots,w_M).
\tag{1}
\]

Use the unnormalized *complete* Jacobi defect of XF-187,

\[
D_{N,h}(x)=2\sum_{j=1}^m
\left(e^{-\pi((N+j)^2+Rh_j)x}-e^{-\pi(N+j)^2x}\right),
\qquad
\mathcal J_{N,h}(x)=D_{N,h}(x)-x^{-1/2}D_{N,h}(1/x),
\tag{2}
\]

with the principal square root. All atoms and their weights are known, except that the final atom of physical radius \(p\) may move to \(p+\tau\), \(\tau\in[-1/4,1/4]\). Thus

\[
h(\tau)=\frac{(p+\tau)^2-C}{R}e_m,\qquad
\mathbf J(\tau)=\bigl(\mathcal J_{N,h(\tau)}(x_\ell)\bigr)_{\ell=1}^{M}.
\tag{3}
\]

Then for all \(\eta,\zeta\in[-1/4,1/4]\),

\[
\boxed{\quad
\|W^{1/2}(\mathbf J(\eta)-\mathbf J(\zeta))\|_2
\ge\frac{e^{-2\alpha}}{4\pi}\sqrt L\,|\eta-\zeta|.
\quad}
\tag{4}
\]

Since \(0<w_\ell\le1\), the same bound holds for the ordinary unweighted raw sample norm. In particular, if \(y=\mathbf J(\eta)+e\), \(\|e\|_2\le\sigma\), and an admissible estimate \(\widehat\eta\) fits the raw data with \(\|y-\mathbf J(\widehat\eta)\|_2\le\sigma\), then

\[
|\widehat\eta-\eta|
\le \frac{8\pi e^{2\alpha}}{\sqrt L}\sigma .
\tag{5}
\]

This is deterministic feasibility stability, not an optimizer or a sampling-access algorithm. The sample count remains \(M=O(m^2/N)\), potentially very large.

## 1. Finite direct Fourier chords retain a two-regime margin

Put \(d=|\eta-\zeta|\le1/2\) and, for \(\tau\) in the physical cell,

\[
q_\tau=e^{-\alpha(p+\tau)^2/C},\quad
\theta_\tau=\frac{\omega(p+\tau)^2}{R},\quad
\beta=\frac{\theta_\eta-\theta_\zeta}{2}
=\frac{\pi(\eta-\zeta)(2p+\eta+\zeta)}{mD},\quad u=L|\beta|.
\tag{6}
\]

The direct part of the raw Jacobi chord is exactly

\[
\Delta J_\ell^{\mathrm{dir}}
=2\left(q_\eta e^{-i\ell\theta_\eta}
       -q_\zeta e^{-i\ell\theta_\zeta}\right).
\tag{7}
\]

For \(m\ge N\ge2\), the bank geometry gives \(L\ge4\), \(|\beta|\le\pi/m\le\pi/2\), and

\[
u\ge 2\pi d,\qquad
\frac{p\,d}{u}\le
\frac{p(2N+3)}{2\pi(2p-1/2)}
\le\frac{2N+3}{2\pi}\le N
\quad(d>0).
\tag{8}
\]

Indeed \(L\ge2mD/(2N+3)\) and
\(2p+\eta+\zeta\ge2p-1/2\ge2N+3\); the final comparison in (8) uses \(N\ge2\).

Define \(S(\beta)=\sum_{\ell=1}^{2L-1}w_\ell\sin^2(\ell\beta)\).
For \(0<u\le\pi\), put \(n=\lfloor L/2\rfloor\ge L/4\). Since
\(w_\ell=\ell/L\) for \(1\le\ell\le n\), and
\(|\ell\beta|\le\pi/2\),

\[
S(\beta)\ge\frac{4\beta^2}{\pi^2L}
\sum_{\ell=1}^{n}\ell^3
\ge \frac{L u^2}{256\pi^2}.
\tag{9}
\]

For \(u\ge\pi\), the exact shifted Fejér identity gives

\[
S(\beta)
=\frac12\left[L-\frac{\cos(2L\beta)}L
\left(\frac{\sin(L\beta)}{\sin\beta}\right)^2\right]
\ge\frac{3L}{8},
\tag{10}
\]

because \(|\sin\beta|\ge2|\beta|/\pi\). Thus, including \(u=0\) by continuity,

\[
S(\beta)\ge\frac{L}{256\pi^2}\min(u^2,1).
\tag{11}
\]

The exact identity
\(
|q_\eta e^{-i\ell\theta_\eta}
 -q_\zeta e^{-i\ell\theta_\zeta}|^2
=(q_\eta-q_\zeta)^2+4q_\eta q_\zeta\sin^2(\ell\beta)
\)
and \(q_\tau\ge e^{-2\alpha}\) imply

\[
\boxed{\quad
\|W^{1/2}\Delta\mathbf J^{\mathrm{dir}}\|_2
\ge \frac{e^{-2\alpha}}{4\pi}\sqrt L\min(u,1).
\quad}
\tag{12}
\]

The two regimes in (12) are essential: an estimate merely proportional to \(d\) is too weak to compare reciprocal derivatives uniformly when \(m\) is unbounded.

## 2. Gaussian suppression before polynomial row gains

The sample geometry of XF-187, equations (15)--(16), follows algebraically from \(m\ge N\ge2\) and does **not** use \(m\le N^{2-\varepsilon}\). Thus

\[
0<|x_\ell|\le\frac{A_\alpha}{N},\qquad
A_\alpha=12+\alpha,\qquad\sum_\ell w_\ell=L.
\tag{13}
\]

Throughout the physical cell \((p+\tau)^2/C\ge1/2\), and therefore

\[
\left|\exp\!\left[-\frac{\pi(p+\tau)^2}{x_\ell}\right]\right|
=\exp\!\left[-\frac{\alpha(p+\tau)^2}{C|x_\ell|^2}\right]
\le\exp\!\left[-\frac{\alpha}{2|x_\ell|^2}\right].
\tag{14}
\]

For \(k>0\), split the exponent in half. The elementary maximum of
\(z^{-k}\exp[-\alpha/(4z^2)]\) over \(z>0\) is
\(E_{\alpha,k}=(2k/(\alpha e))^{k/2}\).
From (13), uniformly over **all** rows and all \(m\ge N\),

\[
|x_\ell|^{-k}
\exp\!\left[-\frac{\alpha}{2|x_\ell|^2}\right]
\le E_{\alpha,k}\exp[-c_\alpha N^2],
\qquad c_\alpha=\frac{\alpha}{4A_\alpha^2}.
\tag{15}
\]

This bound retains the Gaussian factor when the row gain is large. It is independent of the potentially enormous \(R\), \(p\), and \(L\).

Only the endpoint changes, so the reciprocal raw chord has the exact expression

\[
\Delta J_\ell^{\mathrm{rec}}
=-2x_\ell^{-1/2}
\left(e^{-\pi(p+\eta)^2/x_\ell}
-e^{-\pi(p+\zeta)^2/x_\ell}\right),
\tag{16}
\]

and physical derivative

\[
\partial_\tau J_\ell^{\mathrm{rec}}(\tau)
=4\pi(p+\tau)x_\ell^{-3/2}
  e^{-\pi(p+\tau)^2/x_\ell}.
\tag{17}
\]

By (15) with \(k=1/2\), the two endpoint amplitudes give

\[
\|W^{1/2}\Delta\mathbf J^{\mathrm{rec}}\|_2
\le4E_{\alpha,1/2}e^{-c_\alpha N^2}\sqrt L.
\tag{18}
\]

Independently, integrating (17), applying (15) with \(k=3/2\), and using
\(p+1/4\le2p\), gives

\[
\|W^{1/2}\Delta\mathbf J^{\mathrm{rec}}\|_2
\le8\pi E_{\alpha,3/2}p\,d\,e^{-c_\alpha N^2}\sqrt L
\le8\pi E_{\alpha,3/2}N u\,e^{-c_\alpha N^2}\sqrt L.
\tag{19}
\]

Use (19) when \(u\le1\), and (18) when \(u\ge1\). With the explicit
\(K_\alpha=4E_{\alpha,1/2}+8\pi E_{\alpha,3/2}\), this yields the uniform, finite-chord comparison

\[
\boxed{\quad
\|W^{1/2}\Delta\mathbf J^{\mathrm{rec}}\|_2
\le K_\alpha N e^{-c_\alpha N^2}\sqrt L\min(u,1).
\quad}
\tag{20}
\]

For sufficiently large \(N_0(\alpha)\), the factor
\(K_\alpha N e^{-c_\alpha N^2}\) is at most
\(e^{-2\alpha}/(8\pi)\). Subtract (20) from (12):

\[
\|W^{1/2}\Delta\mathbf J\|_2
\ge\frac{e^{-2\alpha}}{8\pi}\sqrt L\min(u,1).
\tag{21}
\]

Finally, (8) gives \(u\ge2\pi d\), while \(d\le1/2\). Hence
\(\min(u,1)\ge2d\), proving (4). The raw-noise claim (5) follows by the triangle inequality.

## Exact scope, controls, and prior art

The exclusion of a width cutoff is a **source-specific improvement in the reciprocal estimate**, not a blanket extension of XF-187's *multi-column* frame theorem beyond its proved regime. The direct lower bound (12) concerns exactly one moving endpoint atom of a known fixed packet. It neither restores XF-188's false normalized multi-atom nonlinear chord coercivity nor removes the physical-coordinate condition-number barrier for a full simultaneous packet inversion.

The finite Fourier separation and Lipschitz ideas are standard superresolution mathematics: Moitra, *STOC* (2015, DOI 10.1145/2746539.2746561); Aubel--Bölcskei, *Applied and Computational Harmonic Analysis* 47 (2019, DOI 10.1016/j.acha.2017.07.006); Hockmann--Kunis, *SIAM Journal on Imaging Sciences* 16 (2023, DOI 10.1137/22M1521353). These references, recorded in the line's SOURCES.md, delimit classical Fourier conditioning; they are not invoked as black-box theorems for the complete Jacobi image. The additional claim here is only the model-specific all-width estimate (4), whose proof handles the reciprocal complex Gaussian image with an explicit small/large-chord split.

The exact cancellations were checked against the endpoint formulas and \(m=2\), \(m=N\), and \(m\gg N\) small-to-finite chord regimes; numerical Fejér sums corroborate (11), but are not evidence for the theorem. The argument is a finite exact inequality and requires neither a limiting packet measure nor assumed real Xi zeros. All other atoms and all weights must be known and unchanged; complex samples must actually be available at the stated raw-noise scale. The cost \(M=O(m^2/N)\) is not an efficient acquisition guarantee. No unknown-support recovery, passage from theta-side information to Xi-zero dynamics, upper bound on \(\Lambda\), or RH consequence follows.
