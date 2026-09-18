# WI-347 — extensive bow feature rank requires projective resolution collapse

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-MECHANISM + PRIOR-ART-AUDITED + STRUCTURAL-RIGIDITY + NON-RH`.

## Claim

WI-343--WI-346 progressively rule out linear, fixed-degree polynomial, and uniformly analytic ways of turning one fixed-aperture bow source carrier into a power-growing family of scale-preserving height directions. The analyticity hypothesis is not the real dividing line. At fixed bow aperture, **any normalized feature family that is uniformly equicontinuous in the projective source geometry has uniformly bounded Gram effective dimension at every fixed tail tolerance**.

Let `S_T` be a finite source set with

\[
\log n\in[x_c-\Delta/2,x_c+\Delta/2],
\qquad n\in S_T,
\tag{1}
\]

and let

\[
w_U(n)=\frac{a_n n^{iU}}{\|a\|_2},
\qquad |U-U_c|\le H/2,
\tag{2}
\]

where the complex coefficients `a_n` are not all zero, so `||w_U||=1`. For unit vectors in a complex Hilbert space define the projective distance

\[
d_{\mathbb P}(u,v):=
\inf_{|\zeta|=1}\|u-\zeta v\|.
\tag{3}
\]

Let `F_T` be any height-independent source feature map whose outputs on this carrier orbit are nonzero, and write

\[
h_U:=\frac{F_T(w_U)}{\|F_T(w_U)\|}.
\tag{4}
\]

No linearity, polynomial representation, differentiability, or analyticity is assumed. Fix `epsilon>0`. Suppose there is a radius `rho_epsilon>0`, independent of `T`, such that on every relevant height window

\[
 d_{\mathbb P}(w_U,w_V)\le\rho_\varepsilon
 \quad\Longrightarrow\quad
 d_{\mathbb P}(h_U,h_V)\le\varepsilon.
\tag{5}
\]

For arbitrary sampled heights `U_1,...,U_m` in an interval of width `H`, let

\[
G=(\langle h_{U_i},h_{U_j}\rangle)_{i,j=1}^m,
\qquad
\lambda_1(G)\ge\cdots\ge\lambda_m(G)\ge0.
\tag{6}
\]

Then there is a subspace of output dimension at most

\[
\boxed{
N_\varepsilon
:=1+
\left\lceil
\frac{H\Delta}{2\rho_\varepsilon}
\right\rceil
}
\tag{7}
\]

within distance `epsilon` of every `h_{U_j}`, and hence

\[
\boxed{
\sum_{j>N_\varepsilon}\lambda_j(G)
\le m\varepsilon^2.
}
\tag{8}
\]

Consequently, at the natural bow/Gallagher aperture `H Delta<=1`, every family with a `T`-uniform projective modulus of continuity has bounded normalized Gram effective dimension, independent of the number of sampled ordinates, the source dimension, and the output dimension.

Equivalently, fix `tau in (0,1)` and define the spectral-tail rank

\[
r_\tau(G):=
\min\left\{
r:\sum_{j>r}\lambda_j(G)\le\tau m
\right\}.
\tag{9}
\]

If (5) holds with `epsilon=sqrt(tau)` at some radius `rho_tau`, then

\[
\boxed{
r_\tau(G)
\le
1+\left\lceil\frac{H\Delta}{2\rho_\tau}\right\rceil
\le
2+\frac{H\Delta}{2\rho_\tau}.
}
\tag{10}
\]

Thus if `H Delta<=1` while `r_tau(G)` grows without bound for some fixed `tau`, the feature family must suffer a **projective resolution collapse**: for every fixed source-projective radius `rho>0`, eventually there are two source carriers within that radius whose normalized outputs are more than `sqrt(tau)` apart projectively. More quantitatively, if `r_tau(G)>2`, every radius at which implication (5) holds with `epsilon=sqrt(tau)` must satisfy

\[
\boxed{
\rho_\tau
\le
\frac{H\Delta}{2\,[r_\tau(G)-2]}.
}
\tag{11}
\]

This closes not only the uniformly analytic escape of WI-346 but every uniformly projectively continuous nonsmooth escape. A successful one-window source-side feature mechanism must instead become increasingly sensitive/discontinuous in the projective carrier geometry, lose transmission under normalization, use the global carrier phase in an essential nonprojective way, enlarge the source aperture, introduce explicit height/cross-window structure, or obtain the needed sign directly from arithmetic covariance.

## 1. Exact projective geometry of the bow carrier

The source orbit itself has an elementary projective Lipschitz bound. Put `delta=U-V` and choose

\[
\zeta=e^{i\delta x_c}.
\tag{12}
\]

For each source coordinate,

\[
\begin{aligned}
|w_U(n)-\zeta w_V(n)|
&=
\frac{|a_n|}{\|a\|_2}
\left|e^{i\delta\log n}-e^{i\delta x_c}\right|\\
&=
\frac{|a_n|}{\|a\|_2}
\left|e^{i\delta(\log n-x_c)}-1\right|\\
&\le
\frac{|a_n|}{\|a\|_2}
|\delta|\,|\log n-x_c|\\
&\le
\frac{|a_n|}{\|a\|_2}
|\delta|\frac\Delta2.
\end{aligned}
\tag{13}
\]

Taking the `ell^2` norm and then the infimum over phases gives the exact uniform estimate

\[
\boxed{
 d_{\mathbb P}(w_U,w_V)
 \le \frac\Delta2|U-V|.
}
\tag{14}
\]

The quotient by scalar phase is essential rather than cosmetic. Rephasing the normalized outputs independently, `h_{U_j}->e^{i theta_j}h_{U_j}`, conjugates `G` by a diagonal unitary and therefore leaves all Gram eigenvalues unchanged. Projective distance is the natural geometry for the rank question.

## 2. A finite projective cover forces a finite spectral tail

Fix `epsilon` and an admissible continuity radius `rho_epsilon` from (5). Equation (14) shows that a height displacement at most

\[
\delta_U:=\frac{2\rho_\varepsilon}{\Delta}
\tag{15}
\]

moves the source carrier by at most `rho_epsilon` projectively. Cover the height interval by a mesh with successive representatives separated by at most `delta_U`. It needs no more than

\[
1+\left\lceil\frac H{\delta_U}\right\rceil
=
1+\left\lceil\frac{H\Delta}{2\rho_\varepsilon}\right\rceil
=N_\varepsilon
\tag{16}
\]

representatives. By (5), every normalized output `h_U` is projectively within `epsilon` of one representative. Multiplying a representative by a scalar phase does not leave its one-dimensional span, so if `V_epsilon` is the linear span of all representative outputs, then

\[
\dim V_\varepsilon\le N_\varepsilon,
\qquad
\operatorname{dist}(h_U,V_\varepsilon)\le\varepsilon
\tag{17}
\]

for every height in the window.

For the sampled vectors define the covariance operator

\[
C:=\sum_{j=1}^m h_{U_j}h_{U_j}^*.
\tag{18}
\]

Its nonzero eigenvalues are exactly those of `G`. If `P` is orthogonal projection onto `V_epsilon`, then

\[
\operatorname{tr}((I-P)C)
=
\sum_{j=1}^m\|(I-P)h_{U_j}\|^2
\le m\varepsilon^2.
\tag{19}
\]

The min--max/Ky Fan characterization of the best rank-`N_epsilon` subspace therefore gives

\[
\sum_{j>N_\varepsilon}\lambda_j(G)
\le
\operatorname{tr}((I-P)C)
\le m\varepsilon^2,
\tag{20}
\]

which is (8). No ambient-dimension bound is used. The argument is simply the passage from a metric cover of a one-parameter projective orbit to the span of its cover centers.

The contrapositive (11) is the rigid part relevant to the bow program. If the normalized Gram matrix is to carry more and more scale-preserving directions at a fixed spectral-tail tolerance, its source-to-feature map must resolve progressively smaller projective changes in the source vector into order-one projective changes in the output. Mere nonsmoothness is not enough; the modulus itself has to deteriorate with `T` at the relevant scale.

## 3. Quantitative Holder and raw-feature corollaries

A useful explicit specialization is a uniform projective Holder estimate. Suppose for some fixed `alpha in (0,1]` and `K<infinity`, independent of `T`,

\[
 d_{\mathbb P}(h(z),h(z'))
 \le
 K\,d_{\mathbb P}(z,z')^\alpha
\tag{21}
\]

on the relevant source carriers. Taking

\[
\rho_\tau=
\left(\frac{\sqrt\tau}{K}\right)^{1/\alpha}
\tag{22}
\]

gives

\[
\boxed{
 r_\tau(G)
 \le
 1+\left\lceil
 \frac{H\Delta}{2}
 \left(\frac K{\sqrt\tau}\right)^{1/\alpha}
 \right\rceil.
}
\tag{23}
\]

Hence at `H Delta<=1`, fixed `alpha,K,tau` imply a uniform rank bound. Conversely, (10) gives the quantitative necessary growth

\[
\boxed{
K
\ge
\sqrt\tau
\left(
\frac{2\,[r_\tau(G)-2]}{H\Delta}
\right)^\alpha
}
\tag{24}
\]

whenever `r_tau(G)>2`. Extensive feature rank therefore forces an extensive sensitivity cost in every fixed-Holder-exponent model.

The same conclusion can be checked before output normalization. Suppose a raw feature map satisfies, for some modulus `Omega`,

\[
\inf_{|\omega|=1}
\|F_T(z)-\omega F_T(z')\|
\le
\Omega(d_{\mathbb P}(z,z'))
\tag{25}
\]

and has a uniform transmission floor

\[
\|F_T(z)\|\ge\mu>0
\tag{26}
\]

on the source orbit. For nonzero vectors `x,y`,

\[
\left\|
\frac x{\|x\|}-\frac y{\|y\|}
\right\|
\le
\frac{2\|x-y\|}{\min(\|x\|,\|y\|)}.
\tag{27}
\]

Applying (27) after the phase optimization in (25) yields

\[
 d_{\mathbb P}(h(z),h(z'))
 \le
 \frac{2}{\mu}
 \Omega(d_{\mathbb P}(z,z')).
\tag{28}
\]

Thus every `T`-uniform raw modulus together with nonvanishing transmission falls under the no-go. In particular, if `Omega(t)=L t^alpha`, then (23) holds with `K=2L/mu`. A fixed-charge phase-equivariant feature map

\[
F_T(\zeta z)=\zeta^q F_T(z),
\qquad q\in\mathbf Z,
\tag{29}
\]

that is ordinarily Holder in the Hilbert norm automatically has the projective form (25): first align the two inputs by a source phase and then align the outputs by its `q`-th power. Phase-invariant maps are the case `q=0`.

This includes broad nonsmooth-but-continuous mechanisms such as fixed-slope projectively compatible soft thresholds or modulus-type features. It deliberately does **not** cover a hard discontinuous threshold, a threshold whose slope diverges with `T`, a phase-sensitive feature that turns the removable global carrier phase into a new output direction, or a map whose normalization is unstable because its output norm tends to zero.

## 4. Prior-art audit and novelty boundary

The general approximation principle used here is classical: a compact one-parameter set with a uniform modulus of continuity has a finite metric cover at each fixed accuracy, and the span of the cover centers gives a finite-dimensional approximation. Metric entropy, approximation numbers, and Kolmogorov widths formalize much broader versions of this compactness/approximability relationship. Relevant standard references are:

- Allan Pinkus, *n-Widths in Approximation Theory*, Springer, 1985, DOI `10.1007/978-3-642-69894-1`.
- Bernd Carl and Irmtraud Stephani, *Entropy, Compactness and the Approximation of Operators*, Cambridge University Press, 1990, DOI `10.1017/CBO9780511897467`.

The line-local chain already contains more specialized versions. WI-343 proves factorial finite-dimensional approximation for the raw exponential carrier on the exact Gallagher window; WI-344 propagates fixed-aperture compression through linear processing; WI-345 handles fixed-degree polynomial/tensor features; WI-346 handles uniformly analytic feature maps and quantifies the analytic coefficient-budget cost of extensive rank. The present deduction removes all of those representation assumptions and retains only the projectively relevant continuity radius.

A bounded prior-art audit found no source that should be used to claim the generic metric-cover argument as new, and no external source was found that states this bow-specific projective Gram consequence. The durable Mathia delta is therefore the exact specialization: equation (14) for the source-fixed bow carrier, equations (7)--(11) turning a projective continuity radius into a Gram-tail rank bound, and the resulting necessary projective-resolution collapse for any extensive one-window feature family. No external priority claim is made.

## 5. Consequence for the RH-oriented research mandate

This is a barrier, not an RH proof and not a better simple-critical-zero percentage. It narrows one of the remaining escapes after WI-346. Replacing an analytic source-side feature bank by a generic nonsmooth feature map cannot produce a growing portfolio of independent bow directions so long as the **normalized projective output remains uniformly continuous at a fixed source scale**.

At natural aperture `H Delta<=1`, an extensive-rank source-side route must now exhibit at least one genuinely structural failure of the hypotheses: a continuity radius tending to zero at fixed output tolerance, a diverging Holder/Lipschitz constant, vanishing output transmission, essential sensitivity to the globally removable carrier phase, growing source aperture, explicit height dependence, or cross-window/cross-scale coupling. The accepted distinguished-twist clue remains unresolved: this finding does not produce the required negative signed off-diagonal. Instead it strengthens the reason to attack that arithmetic covariance directly, because a large class of generic source-feature substitutes cannot manufacture the missing rank without paying an explicit resolution/conditioning cost.

The falsification target for any proposed nonlinear escape is now simple. Exhibit, in the same norm and normalization used by the intended Weil/inertia argument, either a `T`-uniform projective continuity radius at some fixed output tolerance—then (10) kills extensive one-window rank—or a mathematically controlled mechanism by which that radius collapses while scale and transmission survive. Only the second possibility can evade this obstruction.