---
type: theorem
research_line: xi_flow
finding_id: XF-188
status: canonical
---

# XF-188 — Right-anchored Fejer nonlinear chords lose uniform coercivity beyond lattice scale

**Evidence classification:** EXACT-DERIVED + NEGATIVE/OBSTRUCTION. XF-187 gives a uniform *linearized* right-anchored Fejer/Jacobi frame for known quadratic packets with \(N\le m\le N^{2-\varepsilon}\), even when \(m/N\to\infty\). That linear frame does not extend to uniform *nonlinear* lower chord bounds on a fixed-size physical lattice cell. A constant physical displacement of only the final atom makes the high-frequency Fejer bank's finite difference much smaller than its well-conditioned derivative predicts. This is a no-go result for that specific normalized bank and metric, not for all holomorphic measurement schemes.

## Statement

Fix \(\alpha>0\), \(0<\varepsilon<1\), and a physical displacement \(0<\eta\le1/4\). For integers \(N\le m\le N^{2-\varepsilon}\), use exactly XF-187's definitions
\[
\lambda_j=(N+j)^2,\quad C=(N+m)^2,\quad
D=2N+m+1,\quad R=(m-1)D,\quad
\delta=\frac{2N+3}{mD},
\]
\[
L=\lceil 2/\delta\rceil,\quad M=2L-1,\quad
w_\ell=1-\frac{|\ell-L|}{L},\quad
\omega=\frac{2\pi(m-1)}m,\quad
x_\ell=\frac{\alpha}{\pi C}+i\frac{\ell\omega}{\pi R}
\quad(1\le\ell\le M).
\]
Extend its normalized *linear* map to the actual nonlinear Jacobi defect from XF-187:
\[
\mathfrak B_{N,m}(h)_\ell
=-\sqrt{w_\ell}\frac{e^{\pi Cx_\ell}}{2\pi R x_\ell}
\,\mathcal J_{N,h}(x_\ell),\qquad
\mu_j(h)=\lambda_j+Rh_j .
\tag{1}
\]
In particular \(\mathfrak B(0)=0\) and \(D\mathfrak B(0)=B^{\rm right}_{N,m}\).

Move only the final physical atom from \(N+m\) to \(N+m+\eta\), leaving every other atom fixed. Its normalized squared-radius vector is \(h=t e_m\), where
\[
t=\frac{2(N+m)\eta+\eta^2}{R}.
\tag{2}
\]
For \(0<t\le1\) and \(Lt\ge2\), the *complete* direct-plus-reciprocal Jacobi bank satisfies
\[
\boxed{\;
\frac{\|\mathfrak B_{N,m}(t e_m)-\mathfrak B_{N,m}(0)\|_2}
{\sqrt L\,t}
\le
\frac{\sqrt{4+\log(Lt)}}{Lt}
+e^\alpha R^{5/2}\exp\!\left(
-\frac{\alpha N^2}{(12+\alpha)^2}\right).
\;}
\tag{3}
\]
Consequently, along **every** admitted sequence with \(N\to\infty\) and \(m/N\to\infty\),
\[
t\sim\frac{2\eta}{m},\qquad Lt\sim\frac{2\eta m}{N},
\qquad
\boxed{\quad
\frac{\|\mathfrak B_{N,m}(t e_m)-\mathfrak B_{N,m}(0)\|_2}
{\sqrt L\,\|t e_m\|_2}\longrightarrow0 .
\quad}
\tag{4}
\]
The ratio has the explicit asymptotic upper bound
\(O_\eta((N/m)\sqrt{1+\log(m/N)})
+O_\alpha(N^{10}e^{-c_\alpha N^2})\), where
\(c_\alpha=\alpha/(12+\alpha)^2>0\).

This is compatible with XF-187's uniformly positive lower singular-value bound
\(\|D\mathfrak B(0)v\|_2\ge c_\alpha'\sqrt L\|v\|_2\).
For any fixed \(\kappa>0\), choose \(\eta<\min(\kappa/4,1/4)\).
Then \(t e_m\) belongs eventually to the cube
\(\|h\|_\infty\le\kappa/m\), yet its normalized chord ratio tends to zero.
Thus **no** positive \(N,m\)-uniform nonlinear inverse-Lipschitz constant
at scale \(\sqrt L\) exists on such a cube throughout \(m/N\to\infty\).

## Exact one-atom chord

Set \(s_\ell=\pi R x_\ell=\alpha R/C+i\ell\omega\). Multiplying the direct Gaussian difference in (1) by its row factor and using \(\lambda_m=C\) gives the exact identity
\[
\mathfrak B^{\rm dir}(t e_m)_\ell
=\sqrt{w_\ell}\frac{1-e^{-t s_\ell}}{s_\ell}.
\tag{5}
\]
Since \(t>0\) and \(\Re s_\ell>0\),
\[
\left|\frac{1-e^{-ts_\ell}}{s_\ell}\right|
=\left|t\int_0^1e^{-ut s_\ell}\,du\right|
\le t,\qquad
\left|\frac{1-e^{-ts_\ell}}{s_\ell}\right|
\le\frac2{|s_\ell|}\le\frac{2}{\omega\ell}
\le\frac1\ell .
\tag{6}
\]
No lower singular-value estimate can be integrated here without
accounting for the oscillatory variation of the moving column.

## Fejer weight localization of the finite difference

The triangular bank puts weight \(w_\ell=\ell/L\) on \(1\le\ell\le L\)
and \(w_\ell\le1\) above \(L\). When \(t\le1\) and \(Lt\ge2\), let
\(K=\lceil1/t\rceil\le L\). By (6), split the sum of squares at \(K,L\):
\[
\begin{aligned}
\|\mathfrak B^{\rm dir}(t e_m)\|_2^2
&\le
\frac{t^2}{L}\sum_{\ell=1}^{K}\ell+
\frac1L\sum_{\ell=K+1}^{L}\frac1\ell+
\sum_{\ell=L+1}^{2L-1}\frac1{\ell^2}\\
&\le
\frac3L+\frac{\log(L/K)}L+\frac1L\\
&\le \frac{4+\log(Lt)}L .
\end{aligned}
\tag{7}
\]
Here \(K\le 2/t\) and \(K+1\le3/t\) bound the first term;
the integral test bounds both tails; and \(K\ge1/t\).
This is a finite deterministic estimate for the *exact*
nonuniform quadratic-grid bank. Its one-column derivation
does not approximate those nodes by an equispaced surrogate.

The derivative of (5) at \(t=0\) is instead
\(\sqrt{w_\ell}\) in every row, of squared norm
\(\sum_\ell w_\ell=L\). Frequencies of order \(1/t\) and
above therefore contribute fully to the derivative while their
integrated finite difference saturates at order \(1/\ell\).

## Reciprocal Jacobi image cannot restore the chord

The normalized reciprocal derivative in column \(m\), at any
intermediate \(z e_m\), is exactly XF-187's reciprocal matrix entry
\[
\partial_{h_m}\mathfrak B^{\rm rec}(z e_m)_\ell
=-\sqrt{w_\ell}\,e^{\pi Cx_\ell}
 x_\ell^{-5/2}e^{-\pi(C+Rz)/x_\ell}.
\tag{8}
\]
For \(z\ge0\), the physical squared radius is at least \(C\).
XF-187's elementary bank geometry gives, throughout this
parameter range,
\[
\frac1R\le |x_\ell|\le\frac{12+\alpha}{N},
\qquad \sum_{\ell=1}^{2L-1}w_\ell=L,\qquad
\Re\frac{\pi(C+Rz)}{x_\ell}
=\frac{\alpha(C+Rz)}{C|x_\ell|^2}
\ge\frac{\alpha N^2}{(12+\alpha)^2}.
\tag{9}
\]
Taking the Euclidean norm of this single derivative column, and
using \(|e^{\pi Cx_\ell}|=e^\alpha\), therefore yields
\[
\sup_{0\le z\le t}
\|\partial_{h_m}\mathfrak B^{\rm rec}(z e_m)\|_2
\le e^\alpha R^{5/2}\sqrt L\,e^{-c_\alpha N^2}.
\tag{10}
\]
Integration over \(0\le z\le t\), followed by the triangle
inequality with (7), proves (3). Moreover
\(R\le4m^2\le4N^{4-2\varepsilon}\), so
\(R^{5/2}e^{-c_\alpha N^2}\le
32N^{10}e^{-c_\alpha N^2}\to0\) uniformly.

Finally, \(L=2mD/(2N+3)+O(1)\).
Inserting (2) and \(m/N\to\infty\) gives
\(t\sim2\eta/m\) and \(Lt\sim2\eta m/N\), establishing (4).
The Jacobian bound from XF-187 thus coexists with vanishing
finite-chord coercivity, with no appeal to numerics or a
linearization outside its valid scale.

## Scope and prior-art boundary

The obstruction concerns **one fixed right-anchored bank**,
a **known consecutive packet**, **equal fixed atom weights**,
the specified Fejer rows, and the **Euclidean normalized
squared-radius metric**. It does not assert that arbitrary
complex Jacobi observations, alternative/adaptive multiscale
banks, unknown-support acquisition, or unnormalized raw samples
suffer the same decay. In particular, a small normalized
difference cannot be converted into a small raw difference by
using only the bounded forward normalizer: that implication
would require an inverse row-gain estimate, which is absent.
The positive XF-186 chart for \(m\le N\) is untouched.

The separation-conditioned Fourier theory of Moitra
(*STOC*, 2015, DOI 10.1145/2746539.2746561) and the local
Lipschitz/weak Wasserstein superresolution results of
Hockmann--Kunis (arXiv:2108.11925; *SIAM J. Imaging Sci.*,
2023, DOI 10.1137/22M1521353) are the relevant classical
prior-art boundaries recorded in SOURCES.md. The
derivative-versus-secant distinction and Fourier phase
cancellation are not claimed as new general principles.
The specific result is the explicit estimate (3) for
XF-187's right-anchored Jacobi bank, including its exact
nonlinear phase, triangular rows, physical-to-squared-radius
conversion, and reciprocal-image suppression.

This is a theta/Jacobi source-side no-go result, **not** a
bound on the de Bruijn--Newman constant, a zero-collision
criterion, or evidence excluding any hypothetical
\(\Lambda>0\) Xi flow. Its next useful role is to separate
local packet frame inversion from nonlinear unknown-support
and multiscale acquisition; it does not itself supply
the required Xi-source-to-zero bridge.
