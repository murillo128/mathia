# PF-352 — complete transition lattices admit geometrically compatible corridor cancellation

**Status:** EXACT-DERIVED + CLASSICAL-SCHUR-METHODS + GEOMETRY-COMPATIBLE-CORRIDOR-CONTROL + ACTUAL-PRIME-FLUTE-ANGLE-OPEN.

PF-351's cancellation does not require selected transition nodes or an arbitrarily large *shared* transition set. In the same weighted corridor model, two **complete Fourier transition bands of a fixed positive width**, with ranks tending to infinity, can have exactly zero shorted edge correlation. Their periods and three corridor conductances can simultaneously satisfy the exact cuff-length/spine-distance relations of a zero-twist nonprime flute patch. All four cuff lengths can tend to infinity, with all three spine distances tending to zero.

This removes two possible objections to that model control: incompleteness of the Fourier bands and incompatibility of freely chosen conductances with cuff lengths. It does **not** identify the corridor model with the pant DtN form, realize the configuration on consecutive primes, or show that the full low/high angle is compact. The proof uses a sign change between two positive Schur problems, with a conditioning estimate to retain the thin geometric regime.

## 1. Odd unmatched transition rank forces a zero

Use PF-346/PF-351's Hilbert space and positively rescaled cosine functions

\[
\mathcal H=L^2(\mathbb R,\operatorname{sech}t\,dt),\qquad
k_x(t)=\frac{\cos(\xi_x t)}{\sqrt{\pi(x+1)}},\qquad
\xi_x=\pi^{-1}\operatorname{arcosh}x,
\]
\[
\langle k_x,k_y\rangle=C(x,y)=\frac1{x+y},\qquad x,y>1.
\tag{1}
\]

Let `1<a<b`, and let `A,B` be finite, disjoint sets of distinct nodes strictly between `a,b`. Retain two modes only on module 1:

\[
f_1=z_a k_a+z_b k_b+\sum_{x\in A}u_xk_x,
\qquad f_2=\sum_{y\in B}v_yk_y.
\]

For `tau>=0`, define

\[
E_\tau=\tau\|f_1\|^2+\|f_1-f_2\|^2+\tau\|f_2\|^2,
\qquad S_\tau=E_\tau^{/(u,v)}.
\tag{2}
\]

The superscript denotes the minimum over every indicated transition coefficient, leaving the two retained coefficients. Every coefficient matrix in (2), **including at `tau=0`**, is strictly positive: at zero it is the Gram matrix on the distinct union `{a,b} union A union B`, conjugated by the diagonal sign that negates module 2. Distinct exponentials in the integral representation of `C` are linearly independent. Thus `S_tau` is strictly positive and continuous for all `tau>=0`.

At zero grounding, `u` and `-v` eliminate the entire union. The Cauchy product identity gives

\[
(S_0)_{ab}=b_{A\cup B}(a)b_{A\cup B}(b)C(a,b),
\qquad b_U(x)=\prod_{y\in U}\frac{x-y}{x+y},
\]
\[
\operatorname{sign}(S_0)_{ab}=(-1)^{|A|+|B|},\qquad
\rho(S_0)=\rho_0:=\frac{2\sqrt{ab}}{a+b}.
\tag{3}
\]

In contrast, holding module 2 at zero and shorting only `A` gives

\[
S_\tau^{\rm loc}=(1+\tau)C^{/A},\qquad
\operatorname{sign}(S_\tau^{\rm loc})_{ab}=(-1)^{|A|},
\qquad \rho(S_\tau^{\rm loc})=\rho_0.
\tag{4}
\]

Completing the square in `f_2` gives the uniform form comparison

\[
\left(1-\frac1{(1+\tau)^2}\right)S_\tau^{\rm loc}
\le S_\tau\le S_\tau^{\rm loc}.
\tag{5}
\]

For the lower bound first minimize over **all** `f_2 in H`, obtaining
`[(1+tau)-(1+tau)^(-1)]||f_1||^2`, then minimize over `u`. For the upper bound choose `f_2=0`. This argument is independent of either transition rank.

At `tau=1`, the positive difference in (5) is at most `S_1^loc/4`. Its mixed entry is therefore at most one quarter of the product of the local diagonal square roots. Whenever `rho_0>1/4`, `(S_1)_{ab}` has the local sign `(-1)^|A|`. If `|B|` is odd, (3) has the opposite sign. The intermediate value theorem proves

\[
\boxed{\exists\,\tau_*\in(0,1):\quad
(S_{\tau_*})_{ab}=0,\qquad (S_{\tau_*})_{aa},(S_{\tau_*})_{bb}>0.}
\tag{6}
\]

No uniqueness or monotonicity of the mixed entry is asserted. This is cancellation of one retained pair; it is not vanishing of an entire retained cross operator.

## 2. Complete physical Fourier bands with growing odd mismatch

Fix a sufficiently large integer `M` and set `eta=1/M`. The transition interval is the **fixed** physical band `(1,1+eta)`. For `j=0,1,...`, put

\[
N=M(2j+2),\qquad L_1=2\pi(N-\tfrac12),\qquad L_2=2\pi N.
\tag{7}
\]

On module 1 retain its nearest exterior lattice modes

\[
\alpha=\frac{N-1}{N-1/2}<1,\qquad
\beta=\frac{N+N/M}{N-1/2}>1+\eta.
\tag{8}
\]

Take **every** positive Fourier frequency strictly inside the transition band on each module:

\[
\Xi_1=\left\{\frac{k}{N-1/2}:N\le k\le N+N/M-1\right\},
\]
\[
\Xi_2=\left\{\frac{k}{N}:N+1\le k\le N+N/M-1\right\}.
\tag{9}
\]

Consequently

\[
|\Xi_1|=2j+2,\qquad |\Xi_2|=2j+1.
\tag{10}
\]

The modes exactly at the two cutoffs on module 2 are exterior modes, fixed to zero in this pair compression. None has been omitted from the open transition band.

The two lattices intersect only at even integer frequencies: `k/(N-1/2)=l/N` implies `k=(2N-1)r`, `l=2Nr`, and frequency `2r`. For `M>=4` there is no intersection in `(1,1+eta)`. Apply (6) with

\[
a=\cosh(\pi\alpha),\quad b=\cosh(\pi\beta),\quad
A=\cosh(\pi\Xi_1),\quad B=\cosh(\pi\Xi_2).
\tag{11}
\]

The local correlation tends to

\[
\rho_*(\eta)=\frac{2\sqrt{\cosh\pi\,\cosh(\pi(1+\eta))}}
{\cosh\pi+\cosh(\pi(1+\eta))},
\tag{12}
\]

which tends to one as `eta` decreases. Thus `rho_0>1/4` on the tail for all sufficiently large fixed `M`, and (6) applies with both transition ranks diverging.

Allowing **all sine modes as well** in both bands leaves this even-sector Schur complement unchanged: every cosine/sine inner product vanishes against the even weight in (1), including intermodule terms. Positive rescaling to the usual physical Fourier normalization `sqrt(2/L_i)` is a diagonal coefficient congruence; it does not change zero mixed entries or absolute normalized correlations. This is the full tangential transition band in the model, not a fixed-rank cosine surrogate. It does not add the actual seam's separate face-parity dynamics.

## 3. A root need not force the neighboring geometry out of the thin regime

The existence proof alone gives no lower bound on `tau_*`. An excessively small value could force large outer spine distances when conductances are tied to geometry. The following estimate excludes that problem for the family (7).

Let `D=2N/M+1` be the number of distinct cosine nodes including the two retained nodes, and `m=D-1=2eta N`. For `M>=4`, all their frequencies lie in `[1/2,2]`. Ordered consecutive frequencies are separated by at least `1/(4N)`: within either lattice this is immediate; between lattices the neighboring differences are

\[
\frac{k}{2N(N-1/2)},\qquad
\frac{N-1/2-k/2}{N(N-1/2)},
\tag{13}
\]

with the relevant indices in the band, and the omitted cutoff modes only enlarge a gap. Write `R=cosh(2pi)`, `v=pi sinh(pi/2)`. The ordered Cauchy nodes satisfy

\[
x_i+x_k\le2R,\qquad |x_i-x_k|\ge\frac{v}{4N}|i-k|.
\]

The exact inverse diagonal formula and the factorial estimate used in PF-348 yield

\[
(C^{-1})_{ii}
=2x_i\prod_{k\ne i}\left(\frac{x_i+x_k}{x_i-x_k}\right)^2
\le2R\left(\frac{8eR}{v\eta}\right)^{2m},
\]
\[
\boxed{\lambda_{\min}(C)\ge
\frac1{2RD}\left(\frac{v\eta}{8eR}\right)^{2m}.}
\tag{14}
\]

Indeed `i!(m-i)!>=m!/2^m>=(m/(2e))^m`. Since `L_1=2pi(N-1/2)`, for every

\[
a_0>A(\eta):=\frac{2\eta}{\pi}\log\frac{8eR}{v\eta}
\]

we have `lambda_min(C)>=exp(-a_0 L_1)` after a finite head. Here `A(eta)->0`.

In the signed union coefficient basis, `E_0` is orthogonally congruent to `C`, while

\[
0\le E_\tau-E_0\le\frac{\tau D}{2}I.
\tag{15}
\]

The last estimate follows from the trace of the two positive local Gram blocks: every diagonal `1/(2x_i)<=1/2`. Choose fixed

\[
A(\eta)<a_0<b_0<1/2,\qquad \tau_0=e^{-b_0L_1}.
\]

Equations (14)--(15) give

\[
E_0\le E_{\tau_0}\le(1+\epsilon_N)E_0,
\qquad \epsilon_N\le\tfrac D2e^{-(b_0-a_0)L_1}\longrightarrow0.
\tag{16}
\]

Shorting preserves this sandwich. After normalizing the two diagonals of `S_0` to one, the mixed perturbation is at most `epsilon_N`, whereas the absolute mixed entry of `S_0` is `rho_0`, bounded away from zero. Thus `S_(tau_0)` still has the zero-grounding sign. At `tau=1` the sign is opposite by (5). We may therefore select the root in (6) so that

\[
\boxed{e^{-b_0L_1}<\tau_*<1.}
\tag{17}
\]

This lower bound is deliberately crude. It is sufficient to compare the grounding scale with the exponential cuff-length scale; it is not a uniform positive grounding bound.

## 4. Exact cuff and conductance compatibility

For the two prescribed periods define the exact collar mesh variables from PF-032/PF-107,

\[
h_i=2\log\coth(L_i/4),\quad i=1,2,
\qquad L_i=2\log\coth(h_i/4).
\tag{18}
\]

They obey `h_1+h_2=O(exp(-L_1/2))`. For a root satisfying (17), choose the two neighboring mesh variables

\[
h_0=\frac{h_1+h_2}{\tau_*}-h_1,
\qquad h_3=\frac{h_1+h_2}{\tau_*}-h_2.
\tag{19}
\]

Both are positive since `tau_*<1`. The exact tight-pant spine distances and the model conductances are

\[
s_i=(h_i+h_{i+1})/2,\quad c_i=1/s_i,\qquad i=0,1,2.
\]

Then

\[
\boxed{\frac{c_0}{c_1}=\frac{s_1}{s_0}=\tau_*,
\qquad \frac{c_2}{c_1}=\frac{s_1}{s_2}=\tau_*.}
\tag{20}
\]

Hence the corridor difference energy with the two exterior cuffs fixed at zero is exactly

\[
c_0\|f_1\|^2+c_1\|f_1-f_2\|^2+c_2\|f_2\|^2
=c_1E_{\tau_*}.
\tag{21}
\]

The common factor changes neither the zero nor the normalized correlation. In addition, (17)--(19) imply

\[
0<h_0,h_3\le(h_1+h_2)e^{b_0L_1}
=O(e^{-(1/2-b_0)L_1})\longrightarrow0.
\tag{22}
\]

Thus all four mesh variables tend to zero, all four corresponding cuff lengths tend to infinity, and all three spine distances tend to zero. These are compatible finite zero-twist tight-flute patches: positive `h_i` specify consecutive increasing endpoints by `u_(i+1)=u_i exp(h_i)`, or equivalently one glues the corresponding one-cusp pants with the positive lengths (18). A finite patch can be extended by further positive mesh values. No assertion about completeness or spectral behavior of an infinite extension is needed.

Equation (21) is still a **corridor model assigned to this geometry**. Exact cuff/spine compatibility does not make `c_i||f_i-f_(i+1)||_H^2` the exact shifted pant DtN energy. The trace-coordinate transport, finite corridor, positive-shift mass, chart remainder and seam terms have not been compared at the small shorted diagonal scale. Nor are the chosen endpoints asserted to be sampled primes or integers.

## Prior art, checks, and consequence

The ingredients are classical: Cauchy Schur structure in Gohberg--Kailath--Olshevsky, *Fast Gaussian Elimination with Partial Pivoting for Matrices with Displacement Structure* (1995), [Section 1](https://www2.math.uconn.edu/~olshevsky/papers/geppdsam.pdf); normalized Schur correlations in Forrester--Zhang, *Parametrising correlation matrices* (2020), [equations (2.6)--(2.7)](https://arxiv.org/abs/1812.07685); and grounded network elimination in Dörfler--Bullo, *Kron Reduction of Graphs With Applications to Electrical Networks* (2013), [primary manuscript](https://motion.me.ucsb.edu/pdf/2011d-db.pdf). These are already S23/S28. The finite positive-form comparisons are proved above; no new general Schur theorem is claimed. The standard prescribed-length tight-pants construction is described by Basmajian--Hakobyan--Šarić, *The type problem for Riemann surfaces via Fenchel--Nielsen parameters* (2022), [Section 9](https://arxiv.org/abs/2011.03166), already S2.

The derived addition is the **odd-rank sign mechanism on complete, interlaced physical lattices**, together with the small conditioning exponent that makes its grounding root compatible with four long cuffs. PF-351 allowed arbitrary interior nodes and tuned two grounds, with an arbitrarily large common sector. Here the bands are complete, disjoint, of fixed width and growing rank, and a single equal-grounding parameter suffices. Neither classical matrix theory nor this construction supplies the actual-PDE comparison or the required prime realization.

Supplementary checks used Python 3 with mpmath 1.4.1 at 650 decimal digits, `M=64` and `j=0,1,2,3`. Exact rational frequency arithmetic checked the full bands, disjointness, counts `(2,1),(4,3),(6,5),(8,7)` and spacing (13). Direct dense Schur elimination checked the zero-grounding Cauchy correlation, the opposite signs at `tau=exp(-L_1/4)` and `tau=1`, and positive shorted diagonals. Logarithmic bisection for 170 steps located a zero in each sign bracket, with absolute residual normalized correlations below `6e-50`. The resulting grounds were approximately `2.40573e-13`, `3.49443e-32`, `4.00748e-13`, `1.42665e-69`; different roots may occur, and no uniqueness is inferred. The resulting positive mesh variables satisfied (20). These finite-precision checks support the finite algebra only; the exact existence and asymptotic compatibility claims follow from (3)--(22), not from numerical roots.

The active transition question cannot be settled by claiming that full Fourier lattices plus the universal cuff/grounding relations rule out the cancellation in PF-351. They do not. A surviving prime-flute noncompactness proof must exploit further arithmetic/geometric restrictions or prove a normalized witness directly for the actual globally shorted form. Conversely, one zero pair in a family of grounded model patches proves no compactness, trace ideal, scattering relation or RH statement. A positive actual-surface conclusion still needs all retained modes, the correct seam completion and uniform passage through growing finite sections.
