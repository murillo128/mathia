# WI-346 — uniformly analytic bow features remain compressible

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + LITERATURE+DERIVED + PRIOR-ART-AUDITED + STRUCTURAL-RIGIDITY + NON-RH`.

## Claim

WI-345 shows that fixed-degree polynomial/tensor feature banks cannot turn one fixed-aperture bow carrier into a growing family of scale-preserving height directions. The apparent next escape is to replace the bounded-degree polynomial by a genuinely non-polynomial analytic feature map. Under a uniform analytic coefficient budget and nonvanishing transmission, that escape also remains compressed.

Let `S_T` be a finite source set with

\[
\log n\in[x_c-\Delta/2,x_c+\Delta/2],
\qquad n\in S_T,
\tag{1}
\]

and let

\[
w_U(n)=\frac{a_n n^{iU}}{\|a\|_2},
\qquad
|U-U_c|\le H/2,
\tag{2}
\]

so `||w_U||=1`. Write `\mathcal H_T=\ell^2(S_T)`. For each `T`, let `\mathcal K_T` be a Hilbert space and suppose a height-independent feature map has an absolutely convergent bi-homogeneous tensor expansion on the unit sphere

\[
F_T(z)
=
\sum_{r,s\ge0}
A_{T,r,s}
\bigl(z^{\otimes r}\otimes\bar z^{\otimes s}\bigr),
\tag{3}
\]

where

\[
A_{T,r,s}:\mathcal H_T^{\otimes r}\otimes
\overline{\mathcal H_T}^{\otimes s}\to\mathcal K_T
\tag{4}
\]

is bounded and linear. Assume that for some fixed `R>1`, independent of `T`,

\[
\boxed{
M_R:=
\sup_T\sum_{r,s\ge0}
\|A_{T,r,s}\|R^{r+s}<\infty,
}
\tag{5}
\]

and that the outputs do not vanish on the height window:

\[
\boxed{
\mu:=\inf_{T,U}\|F_T(w_U)\|>0.
}
\tag{6}
\]

Then for every pair of integers `P,d>=0` there is a subspace
`W_T(P,d)\subset\mathcal K_T`, independent of `U`, such that

\[
\boxed{
\dim W_T(P,d)\le(2P+1)(d+1)
}
\tag{7}
\]

and uniformly for `|U-U_c|<=H/2`,

\[
\boxed{
\operatorname{dist}\bigl(F_T(w_U),W_T(P,d)\bigr)
\le
M_R\left[
R^{-(P+1)}+
\frac{(PH\Delta/4)^{d+1}}{(d+1)!}
\right].
}
\tag{8}
\]

For sampled heights `U_1,...,U_m`, put

\[
h_j:=\frac{F_T(w_{U_j})}{\|F_T(w_{U_j})\|}
\tag{9}
\]

and let `G=(\langle h_i,h_j\rangle)` have decreasing eigenvalues `lambda_1>=...>=lambda_m>=0`. Then

\[
\boxed{
\sum_{j>(2P+1)(d+1)}\lambda_j(G)
\le
m\left\{
\frac{M_R}{\mu}
\left[
R^{-(P+1)}+
\frac{(PH\Delta/4)^{d+1}}{(d+1)!}
\right]
\right\}^2.
}
\tag{10}
\]

In particular, at fixed Gallagher aperture `H Delta<=1`, fixed `R>1`, fixed relative analytic budget `M_R/mu`, and fixed tail tolerance, the normalized feature family has uniformly bounded effective dimension, independent of `T`, `|S_T|`, the output dimension, and the number of sampled heights. A non-polynomial analytic feature map is therefore not by itself an escape from the bow source-height rank obstruction.

More quantitatively, for a prescribed spectral-tail fraction `tau>0`, set

\[
\theta:=\frac{\mu\sqrt\tau}{2M_R}.
\tag{11}
\]

When `0<theta<1`, choose `P` with `R^{-(P+1)}<=theta`, and put `N=d+1` with

\[
N\ge
\max\left\{
\frac{ePH\Delta}{2},
\log_2\frac1\theta
\right\}.
\tag{12}
\]

Then the right side of (10) is at most `tau m`. At `H Delta<=1` this gives a rank cutoff

\[
\boxed{
(2P+1)N
=
O_R\!\left(
\left[1+\log\frac{M_R}{\mu\sqrt\tau}\right]^2
\right).
}
\tag{13}
\]

Thus a route that genuinely needs effective rank `r(T)->infinity` at fixed aperture and fixed tail tolerance must pay somewhere outside the uniform analytic regime: the analytic radius may collapse toward the unit sphere, the coefficient budget relative to transmitted output may diverge, the feature map may become nonsmooth or height-dependent, the source aperture may grow, or the needed cancellation must come from arithmetic phase structure rather than generic feature rank. Choosing `P,N` proportional to `sqrt(r)` in (10) also shows the quantitative conditioning pressure: for fixed `R>1` and fixed aperture, retaining a fixed normalized Gram-tail fraction beyond rank `r` forces `M_R/mu` to grow at least like `exp(c_R sqrt(r))`, up to constants depending on the fixed tail threshold.

## 1. Charge grouping removes the sector-count loss

Put

\[
\log n=x_c+\xi_n,
\qquad |\xi_n|\le\Delta/2.
\tag{14}
\]

Fix one bi-degree `(r,s)`, write `q=r+s` and `k=r-s`, and put `delta=U-U_c`. On a tensor coordinate indexed by `r` source indices and `s` conjugate-source indices, the phase change from `U_c` to `U` is

\[
\exp\!\bigl(i\delta(kx_c+\Xi)\bigr),
\tag{15}
\]

where

\[
\Xi=
\sum_{j=1}^r\xi_{n_j}
-
\sum_{j=1}^s\xi_{m_j},
\qquad
|\Xi|\le\frac{q\Delta}{2}.
\tag{16}
\]

For sectors with `q<=P`, therefore,

\[
|\delta\Xi|\le\frac{PH\Delta}{4}.
\tag{17}
\]

Let `X_{r,s}` denote the diagonal self-adjoint tensor operator whose coordinate eigenvalue is `Xi`, so `||X_{r,s}||<=q Delta/2`. Relative to the tensor at `U_c`, the sector contribution is

\[
e^{i\delta kx_c}
A_{T,r,s}
\bigl(e^{i\delta X_{r,s}}v_{r,s}\bigr),
\tag{18}
\]

where `||v_{r,s}||=1`. Taylor's integral remainder on the real spectrum gives

\[
\left\|
e^{i\delta X_{r,s}}
-
\sum_{j=0}^{d}
\frac{(i\delta X_{r,s})^j}{j!}
\right\|
\le
\frac{(PH\Delta/4)^{d+1}}{(d+1)!}.
\tag{19}
\]

The key improvement over the sector-by-sector count in WI-345 is that sectors can be summed **before** taking the approximating span. For fixed charge `k` and Taylor order `j`, define the fixed output vector

\[
v_{k,j}^{(T)}
:=
\sum_{\substack{r,s\ge0\\r+s\le P\\r-s=k}}
\frac1{j!}
A_{T,r,s}\bigl(X_{r,s}^{\,j}v_{r,s}\bigr).
\tag{20}
\]

The complete degree-`<=P` Taylor approximation is

\[
\sum_{k=-P}^{P}
\sum_{j=0}^{d}
 e^{i\delta kx_c}(i\delta)^j v_{k,j}^{(T)}.
\tag{21}
\]

Hence it lies in the span of only `(2P+1)(d+1)` fixed vectors, proving (7). The ambient tensor sectors never need to remain orthogonal after `F_T`; only the integer charge `k=r-s` and Taylor order survive as height modes.

## 2. Uniform analytic control gives the error bound

For `q=r+s>P`, (5) gives

\[
\begin{aligned}
\sum_{q>P}\|A_{T,r,s}\|
&\le
R^{-(P+1)}
\sum_{q>P}\|A_{T,r,s}\|R^q\\
&\le M_RR^{-(P+1)}.
\end{aligned}
\tag{22}
\]

Because every tensor monomial of the unit carrier has norm one, (22) bounds the entire discarded analytic tail in output norm.

For `q<=P`, sum (19) after applying the corresponding `A_{T,r,s}`. Since `R^q>=1`,

\[
\sum_{q\le P}\|A_{T,r,s}\|
\le M_R,
\tag{23}
\]

so the total low-degree Taylor remainder is at most

\[
M_R\frac{(PH\Delta/4)^{d+1}}{(d+1)!}.
\tag{24}
\]

Adding (22) and (24) proves (8). This argument allows the source dimension, target Hilbert space, and all coefficients `A_{T,r,s}` to vary with `T`; only the radius/majorant in (5) is required uniformly.

## 3. Normalized Gram tails and the fixed-aperture barrier

Let `Q_T` be orthogonal projection onto the closure of `W_T(P,d)`. By (6)--(8),

\[
\|(I-Q_T)h_j\|
\le
\frac{M_R}{\mu}
\left[
R^{-(P+1)}+
\frac{(PH\Delta/4)^{d+1}}{(d+1)!}
\right].
\tag{25}
\]

If `C:\mathbf C^m\to\mathcal K_T` is the column operator `Ce_j=h_j`, then `Q_TC` has rank at most `(2P+1)(d+1)`. The Frobenius residual therefore bounds the optimal low-rank residual:

\[
\sum_{j>(2P+1)(d+1)}s_j(C)^2
\le
\|(I-Q_T)C\|_F^2,
\tag{26}
\]

and `s_j(C)^2=lambda_j(G)`. This proves (10).

For `N=d+1`, the elementary Stirling lower bound `N!>=(N/e)^N` gives

\[
\frac{(PH\Delta/4)^N}{N!}
\le
\left(\frac{ePH\Delta}{4N}\right)^N.
\tag{27}
\]

Under (12) the ratio in parentheses is at most `1/2`, hence the Taylor term is at most `2^{-N}<=theta`; the analytic tail is also at most `theta`. Equations (10)--(12) then prove the `tau m` tail statement and (13).

There is also a useful contrapositive. At fixed `H Delta<=1` and fixed `R>1`, take `P` and `N` proportional to `sqrt(r)` with `(2P+1)N<r`. Both error terms in (10) are then `O(exp(-c_R sqrt(r)))`. If a normalized family keeps a fixed positive spectral-tail fraction beyond rank `r`, (10) forces

\[
\frac{M_R}{\mu}\ge c\,e^{c_R\sqrt r}
\tag{28}
\]

for constants depending only on the fixed radius and tail threshold. Thus growing effective rank cannot be hidden inside a uniformly well-conditioned analytic feature family.

As an immediate sharpening of WI-345, a polynomial map of total degree `p` has no degree tail once `P=p`. If its total coefficient budget divided by transmitted norm stays bounded and `H Delta<=1`, taking `N=O(p)` yields effective dimension `O(p^2)`, not the sector-by-sector `O(p^3)` estimate implicit in WI-345. Consequently an extensive effective rank `r` requires at least `p=Omega(sqrt(r))` under stable transmission.

## 4. Prior art and novelty boundary

The broad mechanism is prior art, not a new principle. Cohen and DeVore proved that algebraic Kolmogorov-width decay is preserved, with a loss in exponent, under holomorphic mappings between Banach spaces:

- Albert Cohen and Ronald DeVore, **Kolmogorov widths under holomorphic mappings**, *IMA Journal of Numerical Analysis* 36 (2016), 1--12; arXiv:1502.06795, https://arxiv.org/abs/1502.06795.

A recent strengthening obtains nearly optimal width preservation and treats exponentially decaying regimes:

- Yuwen Li and Guozhi Zhang, **Nearly optimal Kolmogorov widths under holomorphic mappings**, arXiv:2608.05581 (submitted 6 Aug 2026), https://arxiv.org/abs/2608.05581.

These papers materially narrow the novelty claim: **holomorphic maps preserve compressibility in broad settings is established literature**. The Mathia delta here is only the specialized, family-uniform BOW estimate (7)--(13): it exploits the exact multiplicative carrier, groups all tensor sectors by the charge `r-s`, gives the explicit `(2P+1)(d+1)` rank count and analytic-tail constant, and converts those quantities into a normalized-Gram conditioning barrier tailored to the live bow `L^2` gate. No priority claim is made for the broad holomorphic-width mechanism.

The theorem is also deliberately narrower than arbitrary analyticity stated without quantitative control. A generic map may be analytic separately for every `T` while its radius shrinks or its Taylor coefficient norms explode with height; such a family need not satisfy (5). Complex-holomorphic maps are the special case `s=0`; maps analytic in both the coordinates and their conjugates fit (3) only when the displayed absolutely summable bi-homogeneous expansion is available with the stated uniform majorant.

A line-local novelty audit checked the current bow clue, WI-195, WI-343, WI-344, and WI-345 together with external searches for holomorphic Kolmogorov widths, analytic reduced-basis compression, nonlinear time--bandwidth concentration, and tensor/Volterra feature maps. No earlier canonical line finding located in that audit gives the charge-grouped uniform analytic bound above. The external literature does contain the broad width-preservation principle, so this finding records a specialized quantitative obstruction rather than a new general theorem about analytic images.

## 5. Boundary conditions and falsification controls

The conclusion can fail only by violating a load-bearing hypothesis or by using a mechanism to which feature-space rank is irrelevant. The principal escapes are:

1. **Shrinking analytic radius.** If the usable `R=R(T)` tends to `1`, the degree tail in (22) need not be uniformly small.
2. **Growing coefficient budget or vanishing transmission.** If `M_R(T)/mu(T)` diverges, normalization can expose tiny high-order components; (28) records the quantitative price.
3. **Nonsmooth or threshold-like maps.** ReLU, hard thresholds, branch singularities, or other maps without a uniform expansion of the form (3)--(5) are outside the theorem.
4. **Height-dependent nonlinear complexity.** Coefficients may explicitly inject new `U`-frequencies or complexity whose analytic norm grows with height.
5. **Growing source aperture.** If `H Delta` grows, the time--bandwidth product grows and the Taylor cutoff in (12) is no longer height-independent.
6. **Direct arithmetic cancellation.** A distinguished-twist covariance or signed arithmetic identity can suppress the BOW off-diagonal term without generating a large generic feature rank. This remains the central escape allowed by the current clue.

The theorem itself has a finite audit path: verify the tensor phase decomposition (15)--(17), Taylor's operator remainder on the bounded diagonal generator, the charge grouping (20)--(21), the coefficient-majorant bounds (22)--(24), and the Frobenius/Eckart--Young passage (25)--(26). A counterexample with fixed `R>1`, fixed `M_R/mu`, fixed `H Delta`, and a fixed positive normalized Gram-tail fraction beyond every fixed rank would directly contradict (10).

## Consequence for the research line

WI-345 left `non-polynomial feature map` as one possible nonlinear escape from fixed-aperture compression. That label is now too broad. **Every uniformly tensor-analytic feature family with stable radius, coefficient budget, and transmission remains compressed, even when infinitely many polynomial degrees are present.** The cheap nonlinear continuation is therefore closed not only at every fixed polynomial degree but throughout this controlled analytic class.

This does not solve the live distinguished-twist cancellation question and does not exclude any off-critical zeta zero by itself. It sharpens what a viable bow continuation must contain: singular/nonsmooth structure, worsening analytic conditioning, growing aperture or height-dependent complexity, or an arithmetic signed-cancellation theorem whose force does not come from manufacturing many generic height directions.