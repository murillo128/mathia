# PC-297 — diffuse boundary-log pseudospectrum is universal square-zero geometry

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL-OBSTRUCTION` + `DECISIVE-BOUNDARY` + `PRIOR-ART-CLASSICALIZATION` for the fixed-scale pseudospectral/transient escape left open by PC-296.

PC-295 proves that the normalized one-profile boundary-log matrix has the nonzero deterministic Green singular spectrum under diffuse source averaging, while PC-296 proves that its complete eigenvalue cloud collapses to the origin. PC-296 deliberately leaves open whether the resulting nonnormality can retain source-specific information in pseudospectra, resolvent growth, or transient amplification.

At every **fixed perturbation scale**, that escape also classicalizes. Under exactly the PC-295/296 diffuseness hypothesis, the normalized boundary-log matrix is asymptotically close in operator norm to a square-zero matrix whose norm tends to `1/2`. Consequently its complete fixed-`epsilon` pseudospectrum converges to a universal Euclidean disk determined only by that classical top Green singular value. The same conclusion holds for the prime source and for every matched diffuse control satisfying the same maximal-atom bound.

Let `q` run through odd primes, let

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and use the PC-283 boundary-renormalized profile

\[
k_q(0)=-\log q,
\qquad
k_q(t)=\log\!\left(2\sin\frac{\pi |t|_q}{q}\right)
\quad(t\ne0).
\tag{1}
\]

For source residues `p,r` define

\[
T_{q,B}^{p,r}(h,k)
:=\frac1N k_q(ph+rk),
\qquad h,k\in H_B.
\tag{2}
\]

Let `mu_q` be a probability measure on `Z/qZ`, choose `p,r` independently with law `mu_q`, and write

\[
\beta_q=\|\mu_q\|_\infty.
\tag{3}
\]

Assume

\[
\boxed{
N\to\infty,
\qquad
(\log q)^2\sqrt{\frac{q\beta_q}{N}}\longrightarrow0.
}
\tag{4}
\]

Then there exist random `N x N` matrices `S_{q,B}^{p,r}` such that

\[
\boxed{
(S_{q,B}^{p,r})^2=0,
\qquad
\mathbb E\|T_{q,B}^{p,r}-S_{q,B}^{p,r}\|_{\rm op}\longrightarrow0,
\qquad
\mathbb E\left|\|S_{q,B}^{p,r}\|_{\rm op}-\frac12\right|\longrightarrow0.
}
\tag{5}
\]

Thus the diffuse boundary-log section is asymptotically a nilpotent of order two, not merely quasinilpotent at the eigenvalue level. In particular,

\[
\boxed{
\|(T_{q,B}^{p,r})^2\|_{\rm op}\longrightarrow0
\quad\text{in probability},
}
\tag{6}
\]

while PC-295 gives `||T||op -> 1/2` in mean. The surviving one-step nonnormal mass therefore does not propagate to a second fixed matrix power.

For `epsilon>0`, use the spectral-norm pseudospectrum

\[
\Lambda_\epsilon(A)
:=\{z\in\mathbb C:\sigma_{\min}(zI-A)\le\epsilon\}.
\tag{7}
\]

Then for every fixed `epsilon>0`,

\[
\boxed{
\Lambda_\epsilon(T_{q,B}^{p,r})
\longrightarrow
\left\{z:\ |z|\le
\sqrt{\epsilon\left(\epsilon+\frac12\right)}\right\}
}
\tag{8}
\]

in Hausdorff distance in probability. More strongly, if

\[
g(r):=
\frac{\sqrt{\frac14+4r^2}-\frac12}{2},
\tag{9}
\]

then

\[
\boxed{
\mathbb E\sup_{z\in\mathbb C}
\left|
\sigma_{\min}(zI-T_{q,B}^{p,r})-g(|z|)
\right|
\longrightarrow0.
}
\tag{10}
\]

Hence on every region bounded away from the origin the resolvent norm converges to the radial classical law

\[
\boxed{
\|(zI-T_{q,B}^{p,r})^{-1}\|
\longrightarrow
\frac{\sqrt{\frac14+4|z|^2}+\frac12}{2|z|^2}
}
\tag{11}
\]

uniformly on compact sets in probability.

## 1. The low Fourier block is asymptotically square-zero

Use the exact PC-295 Fourier expansion

\[
T_{q,B}^{p,r}
=
\sum_{m\bmod q}a_q(m)x_{m,p}z_{m,r}^{*},
\tag{12}
\]

where

\[
a_q(0)=0,
\qquad
a_q(m)<0\ (m\ne0),
\qquad
a_q(\pm j)\longrightarrow-\frac1{2j}
\tag{13}
\]

for every fixed positive integer `j`, and

\[
x_{m,p}(h)=N^{-1/2}e^{2\pi i mph/q},
\qquad
z_{m,r}(h)=N^{-1/2}e^{-2\pi i mrh/q}.
\tag{14}
\]

Fix `M`, put `S_M={+-1,...,+-M}`, and write

\[
A_{q,M}=X D Z^*,
\tag{15}
\]

with columns of `X` and `Z` given by the corresponding vectors in (14) and

\[
D=\operatorname{diag}_{m\in S_M}a_q(m).
\]

PC-295 gives the same-side Gram estimates

\[
\mathbb E\|X^*X-I\|_F^2
+
\mathbb E\|Z^*Z-I\|_F^2
=O_M\!\left(\frac{q\beta_q}{N}\right),
\tag{16}
\]

and PC-296 gives the cross-Gram estimate

\[
\boxed{
\mathbb E\|Z^*X\|_F^2
=O_M\!\left(\frac{q\beta_q}{N}\right).
}
\tag{17}
\]

The distinction is structural: the same-side frames become orthonormal while the left and right frames become mutually orthogonal.

On the event that both same-side Gram matrices are within `1/2` of the identity, define the polar-normalized isometries

\[
U=X(X^*X)^{-1/2},
\qquad
V=Z(Z^*Z)^{-1/2}.
\tag{18}
\]

Let

\[
C:=V^*U.
\tag{19}
\]

Equations (16)--(17) imply `||C|| -> 0` in mean for every fixed `M`. When `||C||<1`, project `V` orthogonally away from `U` and renormalize:

\[
W_0=(I-UU^*)V,
\qquad
W=W_0(I-CC^*)^{-1/2}.
\tag{20}
\]

Then exactly

\[
W^*W=I,
\qquad
W^*U=0,
\tag{21}
\]

and standard functional calculus near the identity gives

\[
\|W-V\|=O_M(\|C\|).
\tag{22}
\]

Define

\[
\boxed{
S_{q,M}:=U D W^*.
}
\tag{23}
\]

Because `W^*U=0`,

\[
\boxed{S_{q,M}^2=0}
\tag{24}
\]

exactly, while the two isometries give

\[
\boxed{
\|S_{q,M}\|=\|D\|.
}
\tag{25}
\]

Moreover `X=U(X^*X)^{1/2}` and `Z=V(Z^*Z)^{1/2}`, so for fixed `M`

\[
\boxed{
\mathbb E\|A_{q,M}-S_{q,M}\|_{\rm op}\longrightarrow0.
}
\tag{26}
\]

One may set `S_{q,M}=0` on the vanishing bad Gram event; all fixed-`M` factors are uniformly bounded, so this does not change (26). Finally (13) implies

\[
\boxed{
\|D\|\longrightarrow\frac12.
}
\tag{27}
\]

Thus every fixed dominant Fourier block is asymptotically unitarily equivalent, up to a vanishing perturbation, to mutually orthogonal left/right channels: a square-zero operator carrying the same Green singular values.

## 2. The complete matrix is close to the square-zero class

Write as in PC-295

\[
T_{q,B}^{p,r}=A_{q,M}^{p,r}+R_{q,M}^{p,r}.
\tag{28}
\]

Its exact tail analysis gives

\[
\boxed{
\limsup_{q\to\infty}
\mathbb E\|R_{q,M}^{p,r}\|_{\rm op}
\le
\sqrt{R_M},
\qquad
R_M=\frac12\sum_{j>M}\frac1{j^2},
}
\tag{29}
\]

with `R_M -> 0`. Combining (26) and (29),

\[
\limsup_{q\to\infty}
\mathbb E\inf_{S^2=0}
\|T_{q,B}^{p,r}-S\|_{\rm op}
\le\sqrt{R_M}
\tag{30}
\]

for every fixed `M`. Sending `M -> infinity` gives

\[
\boxed{
\mathbb E\,\operatorname{dist}_{\rm op}
\left(T_{q,B}^{p,r},\{S:S^2=0\}\right)
\longrightarrow0.
}
\tag{31}
\]

A standard diagonal choice `M=M(q)->infinity` in the fixed-`M` estimates produces square-zero approximants satisfying all three assertions in (5): choose `M` slowly enough that the same-side and cross-Gram errors have already entered their asymptotic regime before increasing the cutoff. Equation (27) fixes the approximant norm at `1/2` in the limit.

Equation (6) is now immediate. If `S^2=0`,

\[
T^2=(T-S)T+S(T-S),
\tag{32}
\]

and (5), together with the PC-295 tightness of `||T||` and (5)'s tightness of `||S||`, forces `||T^2|| -> 0` in probability.

## 3. A square-zero operator has an exact radial pseudospectrum

The remaining step is classical finite-dimensional operator geometry. If `S^2=0`, then

\[
\operatorname{ran}S\subseteq\ker S.
\]

Choose singular-vector pairs so that on each active two-dimensional block

\[
S_j=
\begin{pmatrix}
0&\sigma_j\\
0&0
\end{pmatrix},
\tag{33}
\]

with the remaining summand zero. Let

\[
\sigma=\|S\|=\max_j\sigma_j.
\]

A direct two-by-two singular-value calculation gives

\[
\sigma_{\min}(zI-S_j)
=
\frac{\sqrt{\sigma_j^2+4|z|^2}-\sigma_j}{2}.
\tag{34}
\]

The right side decreases with `sigma_j`, so the largest singular value alone controls the minimum over all blocks:

\[
\boxed{
\sigma_{\min}(zI-S)
=
g_\sigma(|z|)
:=
\frac{\sqrt{\sigma^2+4|z|^2}-\sigma}{2}.
}
\tag{35}
\]

Consequently

\[
\boxed{
\Lambda_\epsilon(S)
=
\left\{z:\ |z|\le\sqrt{\epsilon(\epsilon+\sigma)}\right\}.
}
\tag{36}
\]

No finer singular sequence enters the fixed-`epsilon` pseudospectrum of a square-zero operator; only `||S||` does.

For arbitrary matrices, the smallest singular value is 1-Lipschitz under operator-norm perturbation. Hence

\[
\sup_z
\left|
\sigma_{\min}(zI-T)-\sigma_{\min}(zI-S)
\right|
\le\|T-S\|.
\tag{37}
\]

Also `g_sigma(r)` is uniformly Lipschitz in `sigma` (its derivative in `sigma` has modulus at most `1/2`). Combining (5), (35), and (37) proves (10). Since `g_{1/2}` is strictly increasing in `|z|`, its `epsilon` sublevel set is exactly the disk in (8), and the uniform defect in (10) sandwiches `Lambda_epsilon(T)` between disks with radii obtained from `epsilon+-o(1)`. This proves the Hausdorff convergence (8). Taking reciprocals away from the origin gives (11).

## 4. Prime and matched-control consequence

For the normalized prime source below `q`, the prime number theorem gives

\[
\beta_q\asymp\frac{\log q}{q}.
\tag{38}
\]

The count-matched Li-grid control used in PC-290 has the same maximal-atom order. Thus both satisfy (4) whenever

\[
\boxed{
\frac{N}{(\log q)^5}\longrightarrow\infty,
}
\tag{39}
\]

including `N~sqrt(q)`. For every fixed `epsilon>0`, both source families therefore have exactly the same limiting pseudospectral disk (8).

More generally, the proof uses the source law only through the same-side diffuse-frame estimates, the cross-Gram diffuse convolution estimate, and the universal Fourier tail estimate already established in PC-295/296. It therefore applies to **every** source family satisfying (4), independently of any prime structure.

This is stronger than saying that the raw eigenvalues are source-universal. The nonnormal resolvent bulge at fixed scale is real and remains order one, but its entire asymptotic shape is forced by the universal square-zero geometry and the single scalar `||T|| -> 1/2`. It cannot distinguish the prime source from diffuse non-prime controls.

## 5. Prior-art and novelty audit

The abstract ingredients are classical. Pseudospectra as resolvent/minimum-singular-value level sets are standard nonnormal operator theory; see Lloyd N. Trefethen, **Pseudospectra of Linear Operators**, *SIAM Review* 39:3 (1997), 383--406, DOI `10.1137/S0036144595295284`, and L. N. Trefethen and Mark Embree, **Spectra and Pseudospectra**, Princeton University Press (2005). Nilpotent operators of order two are a standard operator class; Stephan Ramon Garcia, Bob Lutz, and Dan Timotin, **Two remarks about nilpotent operators of order two**, *Proceedings of the American Mathematical Society* 142:5 (2014), 1749--1756, DOI `10.1090/S0002-9939-2014-11944-7`, is representative neighboring literature. The block decomposition (33) and disk formula (36) are elementary consequences of singular-value decomposition and are not claimed as novel.

Targeted searches against square-zero/nilpotent pseudospectra, nonnormal Fourier finite sections, log-sine matrices, and asymptotically orthogonal Fourier frames found the expected general pseudospectral and frame theories but no result supplying the Prime-Circle-specific implication from the simultaneous same-side/cross-Gram estimates (16)--(17) and the Green Fourier tail (29). Absence of such a result is not used as evidence of novelty.

The durable project-local delta is instead the exact reduction forced by the already-persisted Prime-Circle representation: **diffuse multiplicative source dilations make the dominant left and right Green Fourier frames mutually orthogonal, while each side separately becomes orthonormal; after the universal tail is removed, this places the whole boundary-log finite section at vanishing operator-norm distance from the square-zero class.** Once that reduction is proved, the fixed-scale pseudospectrum is classical and source-blind.

The proof is self-contained relative to PC-295/296; the external references are neighboring general theory rather than load-bearing mathematical dependencies, so `SOURCES.md` is unchanged.

## 6. Boundaries and remaining nonnormal channels

Equation (8) closes the complete **fixed positive epsilon** pseudospectrum of one diffuse boundary-log profile. It does not control pseudospectra at scales `epsilon=epsilon_q -> 0`. At such shrinking scales, the approximation error in (5) must be compared quantitatively with `epsilon_q`; the present diagonal compactness argument gives no sharp rate. Microscopic pseudospectral structure may therefore survive below the universal fixed-scale disk law.

The theorem also does not classify eigenvector condition numbers at their natural shrinking eigenvalue scale, log-determinants or products that magnify the collapsing origin, rare source-conditioned pairs, concentrated or correlated source laws that violate (4), same-source/extremal configurations, several profiles retained jointly, source-coupled left/right observables before the square-zero compression, or genuine cross-level operators.

The fixed-power consequence (6) should likewise not be overread as a general dynamical theorem. It says that the one-profile normalized matrix has no persistent second-step operator mass in the diffuse regime. A rescaled time/power limit, a source-dependent renormalization, or a multi-operator word may probe information not covered here.

The immediate negative conclusion is decisive but narrow:

\[
\boxed{
\text{one boundary-log profile}
\to
\text{diffuse independent source pair}
\to
\text{fixed-scale pseudospectrum/resolvent bulge}
\to
\text{prime-specific RH discriminator}
}
\]

fails. The complete fixed-scale pseudospectrum converges to the same square-zero disk for the prime source and for matched diffuse controls.

## 7. Falsification and audit tests

1. Reconstruct the exact Fourier expansion (12) and the fixed-block Gram matrices. Any violation of the PC-295 same-side estimates or PC-296 cross-Gram estimate invalidates the reduction.
2. On a good fixed-`M` block, compute `U,V,W` from (18)--(20) and verify numerically or symbolically that `W^*W=I`, `W^*U=0`, and `S_{q,M}^2=0` to numerical precision.
3. Check that `||A_{q,M}-S_{q,M}||` tends to zero for fixed `M` under diffuse product sampling while `||S_{q,M}|| -> 1/2`.
4. The PC-295 tail must satisfy (29). A persistent positive lower bound for the tail operator norm after `q -> infinity` and then `M -> infinity` would falsify the complete square-zero approximation.
5. For any exact square-zero test matrix, direct SVD of `zI-S` must agree with (35). The `epsilon`-pseudospectrum boundary must satisfy `|z|^2=epsilon(epsilon+||S||)`.
6. Under prime-scale diffuse sampling with `N/(log q)^5 -> infinity`, the uniform minimum-singular-value profile in (10) should approach `g(|z|)`. A persistent angular dependence at fixed `epsilon` would contradict the theorem.
7. Correlated, concentrated, same-source, or shrinking-`epsilon` experiments are outside the present hypothesis/conclusion and are the correct falsifiers for the remaining boundary rather than counterexamples to (8).

Finite computations are useful only as stress tests. The durable claim is the analytic square-zero approximation and its deterministic pseudospectral consequence.