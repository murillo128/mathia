# PF-361 — finite corridor windows preserve the narrow-band model angle

**Status:** LITERATURE+DERIVED + UNIFORM-RELATIVE-TRUNCATION + CORRIDOR-MODEL-OBSTRUCTION + ACTUAL-TRACE-TRANSPORT-OPEN.

Replacing the infinite weighted corridor integral by the finite growing corridor window does not remove PF-359/PF-360's essential-angle-one obstruction, provided the **combined transition and retained high strip is sufficiently narrow**. The comparison is relative on every combination of both neighboring frequency lattices, independent of their minimum separation, coefficient conditioning, and network conductances. It therefore survives global transition shorting in the specified energy completion.

The ingredient is the classical Turán–Nazarov inequality, not a new Cauchy identity. This settles finite-window truncation for the straight-coordinate corridor model. It does not replace the actual boundary-coordinate correspondence by the identity, add the nonsingular pant/seam energy, or identify a surface spectral operator.

## 1. A weighted tail bound independent of frequency separation

Let

\[
p(t)=\sum_{j=1}^{N}z_j e^{i\xi_jt},\qquad \xi_j\in\mathbb R,
\qquad H[p]=\int_{\mathbb R}|p(t)|^2\operatorname{sech}t\,dt.
\tag{1}
\]

Repeated frequencies can be combined. No separation, magnitude bound, or lattice assumption is imposed on the remaining frequencies. Assume `p` is nonzero and `N>=2`, and put `m=N-1`. Let `A>=e` be an absolute constant for the Turán–Nazarov inequality

\[
\sup_I|p|\le\left(\frac{A|I|}{|E|}\right)^m\sup_E|p|,
\qquad E\subset I,\quad |E|>0.
\tag{2}
\]

The general theorem has an additional factor involving the real parts of the exponents; here all exponents are purely imaginary, so that factor is one. Define

\[
B=1+2\log(8A/e)>1.
\]

Then, for every `T>=m`,

\[
\boxed{\int_{|t|>T}|p(t)|^2\operatorname{sech}t\,dt
\le\frac8m\exp\{Bm-T/2\}\,H[p].}
\tag{3}
\]

The estimate is useful when its factor is below one. For a single exponential the tail fraction is at most `4 exp(-T)/pi`. Zero polynomials require no estimate. One may use any upper bound for the number of terms in (2); all ensuing estimates remain valid with that order budget.

### Proof

For `R>0`,

\[
\int_{-R}^{R}|p(t)|^2dt\le\cosh R\,H[p]\le e^R H[p].
\]

The subset

\[
E_R=\{t\in[-R,R]:|p(t)|^2\le e^R H[p]/R\}
\]

has measure at least `R`, by the integral bound. Apply (2) on `[-t,t]`, for `t>=R`, with this same subset:

\[
\max\{|p(t)|^2,|p(-t)|^2\}
\le\left(\frac{2At}{R}\right)^{2m}\frac{e^R}{R}H[p].
\tag{4}
\]

Since `sech(t)<=2 exp(-t)` for `t>=0`, integrating both tails gives

\[
\int_{|t|>T}|p(t)|^2\operatorname{sech}t\,dt
\le\frac{4e^R}{R}H[p]
 \left(\frac{2A}{R}\right)^{2m}
 \int_T^\infty e^{-t}t^{2m}dt.
\tag{5}
\]

The function `t^(2m) exp(-t/2)` has its maximum at `t=4m`. Thus the final integral is at most

\[
2e^{-T/2}(4m/e)^{2m}.
\]

Set `R=m`, which is permitted by `T>=m`. Equation (5) becomes (3). In particular the proof never divides by a Gram eigenvalue or a frequency difference.

## 2. Why the term count must enter

The linear relationship between window length and order cannot be removed uniformly, even with all frequencies in an arbitrarily small interval. For fixed integer `m>=1`, consider

\[
p_{\epsilon,m}(t)=\left(\frac{e^{i\epsilon t}-1}{\epsilon}\right)^m.
\tag{6}
\]

This has `m+1` real frequencies. As `epsilon -> 0`, its squared modulus tends to `|t|^(2m)` and is bounded by that function. Dominated convergence applies in `L^2(sech(t) dt)` and on every finite interval. For the limiting polynomial,

\[
\frac{\int_{-T}^{T}t^{2m}\operatorname{sech}t\,dt}
     {\int_{\mathbb R}t^{2m}\operatorname{sech}t\,dt}
\le\frac{T^{2m+1}}{(2m+1)!}
\le\left(\frac{eT}{2m+1}\right)^{2m+1}.
\tag{7}
\]

The denominator bound uses `sech(t)>=exp(-t)` for positive `t`; the numerator uses `sech(t)<=1`. Therefore if `T_m=o(m)`, the central mass fraction tends to zero. For each `m`, choose `epsilon_m` small enough to approximate this fraction and to keep `m epsilon_m` below any prescribed positive band width. Modulation places the frequencies in any desired interval without changing the norm. A real cosine version is obtained along even `m` from `(sin(epsilon t)/epsilon)^m`.

This is a stress test for (3), not a statement about the prime Fourier lattices. It rules out replacing the order budget by a bound on frequency magnitude alone. No optimal constant in (3) is claimed.

## 3. Application to both neighboring prime-cuff lattices

Use the physical periods `L_i` and embedded corridor half-windows

\[
T_i=\operatorname{arsinh}\frac{\theta}{\sinh s_i},
\qquad s_i=(h_i+h_{i+1})/2,
\tag{8}
\]

from PF-216, for fixed sufficiently small `theta>0`. The geometric/arithmetic bounds used in PF-348 give

\[
T_i\ge b_0\max\{L_i,L_{i+1}\}-C,
\qquad b_0=19/80,
\qquad L_i\longrightarrow\infty.
\tag{9}
\]

Indeed `s_i<=C p_i^(-19/40)` by the Baker–Harman–Pintz gap input, while both adjacent periods are at most `2 log p_i+O(1)`; neighboring prime ratios tend to one. Equation (9) concerns the embedded window after the natural strip removal as in PF-216, not a full cuff fundamental interval.

Fix `kappa>0`. On each cuff allow every sine/cosine lattice mode whose positive frequency lies in `[kappa,kappa+W]`, and optionally the constant and first nonzero sine/cosine modes. The parameter `W>0` is fixed. Let `f_i` be any linear combination of these traces, including arbitrary Fourier normalization factors. The straight-coordinate edge difference

\[
p_i(t)=f_{i+1}(t)-f_i(t)
\tag{10}
\]

has an exponential-term budget

\[
N_i\le\frac{W}{\pi}(L_i+L_{i+1})+C_0
\le\frac{2W}{\pi}L_i^*+C_0,
\qquad L_i^*=\max\{L_i,L_{i+1}\}.
\tag{11}
\]

The constant `C_0` handles endpoint rounding and the optional low modes. Coincident frequencies reduce this count; arbitrarily close frequencies do not change the estimate.

Choose, for example,

\[
0<W<\frac{\pi b_0}{8B}.
\tag{12}
\]

Equations (9)–(12) ensure `T_i>=N_i-1` on a sufficiently far tail. Applying (3), and treating the one-term case separately, gives constants `C_1<infinity` and `c=b_0/4>0` such that

\[
\boxed{\int_{|t|>T_i}|f_{i+1}(t)-f_i(t)|^2\operatorname{sech}t\,dt
\le C_1e^{-cL_i^*}\,H[f_{i+1}-f_i].}
\tag{13}
\]

This holds uniformly for every coefficient vector on both entire local bands. It requires neither PF-354's rational independence nor a Diophantine lower bound on neighboring Fourier gaps. It is stronger than a coefficient-space estimate such as `O(N exp(-T)) ||z||^2`, which would still need a lower Gram eigenvalue before becoming relative.

The conclusion controls the combined width `W`, not just the transition width. An arbitrary broad retained low/high block does not have the order budget (11).

## 4. Relative comparison survives the infinite transition elimination

Take a fixed sufficiently far half-line of modules, relabel its first index as `1`, and put `f_0=0`. Use the same allowed frequency sets as above and arbitrary finite `c_i>0`, `g_i>=0`. Define on finitely supported fields

\[
\mathcal E[f]=\sum_{i\ge0}c_i H[f_{i+1}-f_i]
                  +\sum_{i\ge1}g_iH[f_i],
\]
\[
\mathcal E_{\rm win}[f]=
\sum_{i\ge0}c_i\int_{-T_i}^{T_i}
 |f_{i+1}(t)-f_i(t)|^2\operatorname{sech}t\,dt
 +\sum_{i\ge1}g_iH[f_i].
\tag{14}
\]

The on-site terms are deliberately identical. They may all vanish. This is the physical-cosine realization of PF-359's Cauchy network, with its edge integrals truncated and its trace correspondence still the identity. The bordering grounded edge uses the corresponding physical window; its zero endpoint only lowers the term count.

Let `epsilon_tail` be the supremum of the factors in (13) over this tail, chosen less than one. Then for all fields

\[
(1-\epsilon_{\rm tail})\mathcal E
\le\mathcal E_{\rm win}\le\mathcal E.
\tag{15}
\]

Both forms are definite: zero window energy makes each analytic edge difference vanish on an interval, hence identically, and the grounded endpoint forces all fields to zero. Equation (15) identifies their completions as equivalent Hilbert topologies on the same algebraic fields. Their closures of the specified transition, low and high algebraic subspaces correspond under this identification. This does not assert equality of their orthogonal projections.

Write `A[u]` for the squared distance of a finitely supported low field `f_u` to the transition space in the full energy, and `F[u]` for its squared distance to the sum of transition and high spaces, taking closures. Define `A_win,F_win` by the same infima in the windowed energy. Variational minimization of (15) gives

\[
A_{\rm win}[u]\ge(1-\epsilon_{\rm tail})A[u],
\qquad F_{\rm win}[u]\le F[u].
\tag{16}
\]

PF-359 (constants) and PF-360 (first nonzero cosines, with constants absent) construct infinite-dimensional far-tail low spans satisfying `F[u]/A[u] -> 0` uniformly on each progressively farther span, when

\[
\gamma>R\delta,\quad
\delta=-\frac2\pi\int_{\kappa}^{\kappa+\eta}
              \log\tanh(\pi\xi/2)d\xi,\quad
\gamma=-\frac2\pi\int_{\kappa+\eta}^{\kappa+W}
              \log\tanh(\pi\xi/2)d\xi,
\tag{17}
\]

where `R>40/19` bounds neighboring prime-period ratios and `0<eta<W`. The transition sector is the full open band `(kappa,kappa+eta)`; the retained high strip is `[kappa+eta,kappa+W]`. Conditions (12) and (17) are compatible: first fix any sufficiently small `W>0`, then choose `eta>0` sufficiently small. Sine transitions decouple from the cosine witnesses in both even-weight forms.

By (16), these spans also satisfy

\[
\frac{F_{\rm win}[u]}{A_{\rm win}[u]}
\le\frac{F[u]}{(1-\epsilon_{\rm tail})A[u]}\longrightarrow0.
\tag{18}
\]

Their residual dimensions are preserved by the lower bound in (16). If `Z_win` is the projection angle between the closed residual low/high spaces in the windowed completion, the distance interpretation gives `||Z_win x||^2/||x||^2=1-F_win[u]/A_win[u]` on these spans. Each finite-rank operator has a nonzero kernel vector on every infinite-dimensional span. The same finite-rank distance argument as PF-359 therefore proves

\[
\boxed{\|Z_{\rm win}\|_{\rm ess}=1.}
\tag{19}
\]

All remote transition variables have been minimized in the same completion. This is not an inference from independently normalized finite sections. Conductance contrast and arbitrarily small grounding do not affect (15)–(19).

The two versions of (19) are retained constants and constants fixed to zero with first-cosine carriers. It is not claimed here that **shorting constants** remains isometric to excluding them after edge-dependent truncation: PF-360's common scalar residual isometry used the full scalar kernel, which (14) changes.

## 5. Exact scope of the geometric advance

The finite corridor window is now controlled without a frequency-separation assumption, even on unions of neighboring unequal lattices. PF-348's single-cuff conditioning argument did not give this coupled relative estimate. Finite-window truncation alone cannot regularize the model's low/high angle in the sufficiently narrow combined band.

The remaining actual-pant boundary is substantive. Along a Fermi ray, the opposite endpoint carries a trace in a **different boundary coordinate**. Already before strip removal, in a hyperboloid parametrization the two geodesics are

\[
(\cosh t,\sinh t,0),\qquad
(\cosh s\cosh u,\sinh u,\sinh s\cosh u).
\]

A normal ray from the first meets the second at

\[
\tanh u=\cosh s\,\tanh t.
\tag{20}
\]

Thus the transverse difference involves `f(t)-g(u(t))`, not (10). The map exists on the embedded window, but is nonlinear. The transported trace is not the exponential polynomial used in (2), and (13) cannot be silently applied to it. Parallel artificial seams require their own correspondence as well. The derivation of (20) is simply equality of the second-to-first hyperboloid coordinate ratio along the ray.

No estimate here controls that transport, tangential energy, positive-shift mass, chart remainder, actual Fourier-diagonal seam terms, or their effect relative to the globally shorted energy. PF-350's antisymmetric comparison remains useful only after a suitable global symmetric **actual-form** witness is proved. Fixed finite heads with additional freedoms and other boundary conditions at infinity are not automatically identified with the grounded tail completion in (14).

The lemma is universal and applies to nonprime controls with the same window/order bounds. It proves no intrinsic trace-ideal, scattering, zeta-zero, or RH statement. It also gives no numerical value for an admissible width without an explicit choice of the classical constant `A`.

## 6. Prior art and validation boundary

The imported theorem is F. L. Nazarov, *Local estimates for exponential polynomials and their applications to inequalities of the uncertainty principle type*, Algebra i Analiz 5 (1993), no. 4, 3–66; English translation, St. Petersburg Math. J. 5 (1994), 663–717 ([original record](https://www.mathnet.ru/eng/aa397)). The precise version (2), including its independence from imaginary exponents, is reproduced as Theorem 1.1 in O. Friedland and Y. Yomdin, *An observation on the Turán–Nazarov inequality*, Studia Math. 218 (2013), 27–39 ([primary paper](https://arxiv.org/abs/1107.0039)). Equation (3) is an elementary weighted-tail consequence proved above, not a claimed new general uncertainty theorem.

Related weighted Fourier concentration is treated by C. Gaillac and E. Gautier, *Estimates for the SVD of the Truncated Fourier Transform on L2(cosh(b·)) and Stable Analytic Continuation* ([author manuscript](https://publications.ut-capitole.fr/id/eprint/32479/1/wp_tse_1013.pdf)). Their operator has a `sech` convolution kernel and their spectral estimates also use Turán-type inequalities. Their SVD is not the finite-lattice edge comparison or the shorted network angle defined here; no result from that paper is needed for (3)–(19).

The project-specific addition is the separation-independent relative cutoff estimate on both neighboring physical lattices and its preservation through the infinite transition infimum. The source theorem, the direct inequalities (4)–(5), the coalescing-frequency control (6)–(7), and the two independent restrictions (12), (17) make every step auditable. The proof does not use numerical recognition of tiny Gram eigenvalues. No machine-certified optimal constant, Lean verification, numerical pant solve, or independent adversarial approval is claimed. A formalization handoff is not warranted merely to transcribe the classical concentration estimate; the unresolved geometric transport remains outside this theorem.
