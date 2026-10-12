---
type: theorem
research_line: xi_flow
finding_id: XF-189
status: canonical
---

# XF-189 — Raw Jacobi endpoint chords stay stable beyond lattice-scale packet width

**Evidence classification:** EXACT-DERIVED + CLASSICAL-FOURIER-CHORD-BOUNDARY. XF-188 proves collapse of finite nonlinear chords in XF-187's *normalized* right-anchored Fejer bank when `m/N -> infinity`. It does **not** imply collapse for the original, unnormalized Jacobi samples. In fact, a known single endpoint atom remains uniformly recoverable in the *physical displacement metric* from those same raw samples throughout XF-187's super-lattice regime. The proof uses a weighted Fourier-chord estimate and a separate bound on the complete reciprocal Jacobi image. This is a restricted one-atom inverse theorem, not a multi-atom nonlinear chart.

## Statement

Fix `alpha>0` and `0<epsilon<1`. Let `N,m` be integers with

\[
N\ge N_0(\alpha,\varepsilon),\qquad N\le m\le N^{2-\varepsilon},
\tag{1}
\]

and use XF-187's *right-anchored* definitions

\[
p=N+m,\quad C=p^2,\quad D=2N+m+1,\quad
R=(m-1)D,\quad \omega=2\pi(m-1)/m,
\]
\[
L=\left\lceil\frac{2mD}{2N+3}\right\rceil,\quad
M=2L-1,\quad w_\ell=1-|\ell-L|/L,\quad
x_\ell=\frac{\alpha}{\pi C}
+i\frac{\ell\omega}{\pi R},\quad 1\le\ell\le M.
\tag{2}
\]

All atoms except the final atom at squared radius `C` are known and unchanged. Move that atom to `(p+eta)^2`, with `eta in [-1/4,1/4]`, and denote by

\[
\mathbf J(\eta)
=(\mathcal J_{N,h(\eta)}(x_\ell))_{\ell=1}^{M},
\qquad
h(\eta)=\frac{(p+\eta)^2-C}{R}e_m
\tag{3}
\]

the **original raw Jacobi defect** of XF-187, with no diagonal row normalization. Let `W=diag(w_1,...,w_M)`. Then, for all `eta,zeta in [-1/4,1/4]`,

\[
\boxed{\quad
\|W^{1/2}(\mathbf J(\eta)-\mathbf J(\zeta))\|_2
\ \ge\ \frac{e^{-2\alpha}}4
\sqrt L\,|\eta-\zeta|.\quad}
\tag{4}
\]

As `0<w_ell<=1`, the same lower bound holds for the **unweighted** raw observations:

\[
\boxed{\quad
\|\mathbf J(\eta)-\mathbf J(\zeta)\|_2
\ \ge\ \frac{e^{-2\alpha}}4
\sqrt L\,|\eta-\zeta|.\quad}
\tag{5}
\]

The constant is independent of `N,m,epsilon`; only the large-`N` onset depends on `alpha,epsilon`. Arbitrary additive raw noise is permitted. If `y=\mathbf J(\eta)+e`, `||e||_2<=sigma`, and a candidate `\widehat\eta in [-1/4,1/4]` fits the raw data to residual at most `sigma`, then

\[
|\widehat\eta-\eta|
\le \frac{8e^{2\alpha}}{\sqrt L}\,\sigma.
\tag{6}
\]

## 1. An exact Fejer estimate for two endpoint positions

Write `d=|eta-zeta|`, `q_tau=exp[-alpha(p+tau)^2/C]`, and `theta_tau=omega(p+tau)^2/R`. The difference of **direct** parts in the `ell`th *raw* sample is exactly

\[
J^{\rm dir}_\ell(\eta)-J^{\rm dir}_\ell(\zeta)
=2\big(q_\eta e^{-i\ell\theta_\eta}
       -q_\zeta e^{-i\ell\theta_\zeta}\big).
\tag{7}
\]

Set

\[
\beta=\frac{\theta_\eta-\theta_\zeta}{2}
=\frac{\pi(\eta-\zeta)(2p+\eta+\zeta)}{mD},
\qquad u=L|\beta|.
\tag{8}
\]

Since `m>=N>=2`, `|eta|,|zeta|<=1/4`, and `2p+eta+zeta<=2D`,

\[
|\beta|\le \pi/m\le\pi/2.
\tag{9}
\]

Also `L>=2mD/(2N+3)` and `2p+eta+zeta>=4N-1/2>=2N+3`, so

\[
u\ge2\pi d.
\tag{10}
\]

The centered triangular weights obey `sum w_ell=L` and `w_ell=ell/L` for `1<=ell<=L`. Define

\[
S(\beta)=\sum_{\ell=1}^{2L-1}
 w_\ell\sin^2(\ell\beta).
\tag{11}
\]

**Claim:** `S(beta)>=L d^2/64`.

For `u>=pi`, the Fejer identity gives

\[
S(\beta)=\frac12\left[
L-\cos(2L\beta)\frac1L
\left(\frac{\sin(L\beta)}{\sin\beta}\right)^2\right].
\tag{12}
\]

Because `|sin beta|>=2|beta|/pi`, the absolute value of the second term in brackets is at most `L*pi^2/(4u^2)<=L/4`. Therefore `S>=3L/8>=Ld^2/64`, as `d<=1/2`.

For `u<=pi`, take `n=floor(L/2)>=L/4`; note `L>=4`. For `1<=ell<=n`, `|ell beta|<=pi/2`, hence `sin^2(ell beta)>=4 ell^2 beta^2/pi^2`. Consequently,

\[
S(\beta)\ge\frac{4\beta^2}{\pi^2L}
\sum_{\ell=1}^{n}\ell^3
\ge \frac{\beta^2L^3}{256\pi^2}
=\frac{Lu^2}{256\pi^2}
\ge\frac{Ld^2}{64},
\tag{13}
\]

where the last inequality uses (10). This proves the claim, including arbitrarily small nonzero `d`; `d=0` is immediate.

The algebraic identity

\[
|q_\eta e^{-i\ell\theta_\eta}
 -q_\zeta e^{-i\ell\theta_\zeta}|^2
=(q_\eta-q_\zeta)^2+
4q_\eta q_\zeta\sin^2(\ell\beta)
\tag{14}
\]

now yields a genuinely **finite-chord** estimate, not an integrated Jacobian estimate. Since `(p+tau)^2/C<=2` on the cell, `q_tau>=e^{-2alpha}`, and by (7), (11)--(14),

\[
\begin{aligned}
\|W^{1/2}(\mathbf J^{\rm dir}(\eta)
 -\mathbf J^{\rm dir}(\zeta))\|_2^2
&\ge16q_\eta q_\zeta S(\beta)\\
&\ge\frac{e^{-4\alpha}}4 Ld^2 .
\end{aligned}
\tag{15}
\]

Thus the direct raw chord is at least `e^{-2alpha} sqrt(L) d/2`.

## 2. Reciprocal Jacobi image is uniformly negligible

The reciprocal part of `mathcal J` is `-x^{-1/2}D(1/x)`, with the principal square-root branch. Differentiate the *moving endpoint contribution* with respect to physical position `tau`:

\[
\partial_\tau J^{\rm rec}_\ell(\tau)
=4\pi(p+\tau)x_\ell^{-3/2}
\exp\!\left(-\frac{\pi(p+\tau)^2}{x_\ell}\right).
\tag{16}
\]

XF-187's bank geometry, which does not assume `m<=N`, gives

\[
R^{-1}\le|x_\ell|\le(12+\alpha)/N,
\qquad \sum_\ell w_\ell=L.
\tag{17}
\]

Throughout the physical cell, `(p+tau)^2>=C/2`. Therefore

\[
\Re\frac{\pi(p+\tau)^2}{x_\ell}
=\frac{\alpha(p+\tau)^2}{C|x_\ell|^2}
\ge c_\alpha N^2,\qquad
c_\alpha=\frac{\alpha}{2(12+\alpha)^2}>0.
\tag{18}
\]

Integrating (16) between `eta,zeta` and applying the weighted Euclidean norm gives

\[
\begin{aligned}
\|W^{1/2}(\mathbf J^{\rm rec}(\eta)
 -\mathbf J^{\rm rec}(\zeta))\|_2
&\le4\pi(p+1/4)R^{3/2}\sqrt L\,
 e^{-c_\alpha N^2}d\\
&\le C\,m^4e^{-c_\alpha N^2}\sqrt L\,d.
\end{aligned}
\tag{19}
\]

Here `p<=2m`, `R<=4m^2`, and `m<=N^{2-epsilon}`, so the final factor tends uniformly to zero and is at most `e^{-2alpha}/4` after enlarging `N_0(alpha,epsilon)`. Subtracting (19) from (15) proves (4), and `||W^{1/2}v||<=||v||` gives (5). Inequality (6) follows by the triangle inequality and (5).

## Mathematical significance, prior art, and boundaries

XF-188 is a valid *normalized-bank* nonlinear obstruction. Its row normalizer includes `1/(Rx_ell)`, strongly attenuating the raw high-frequency phases that separate the two endpoint positions in (7). The inverse row gains cannot be treated as bounded; hence XF-188's upper bound on a normalized chord cannot be transferred to an upper bound on the raw chord. The positive lower bound (5) identifies that missing implication exactly. Conversely, (5) does **not** repair uniform nonlinear stability of XF-187's normalized squared-radius chart, which remains false on the stated cell.

The trigonometric separation and finite-chord stability ideas are classical superresolution mathematics; see Moitra, *STOC* (2015, DOI 10.1145/2746539.2746561), Aubel--Bolcskei, *ACHA* (2019, DOI 10.1016/j.acha.2017.07.006), and Hockmann--Kunis, *SIAM Journal on Imaging Sciences* (2023, DOI 10.1137/22M1521353), all already anchored in `research/xi_flow/SOURCES.md`. The additional **line-local exact claim** is the weighted lower bound (4) for XF-187's specific right-anchored complex Jacobi rows, in a uniform physical one-atom cell with `N<=m<=N^{2-epsilon}`, including the reciprocal image and unrestricted *absolute raw-noise* transfer. No general Fourier-superresolution novelty is asserted.

The packet support, all other atom positions, and weights are assumed known. Only **one endpoint atom** moves; this proves neither multi-atom unknown-support recovery nor the full nonlinear physical-coordinate conditioning of the entire packet. The upper width cutoff belongs to the reciprocal-error estimate, not to a claimed information-theoretic impossibility beyond it. Complex right-half-plane Jacobi values are assumed observable; acquisition from the actual Xi/theta source with controlled physical error, and transfer to a Xi-zero transition bound, remain open. This theorem alone gives no bound on `Lambda` and does not advance an RH proof.
