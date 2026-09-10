# ANF-153 — distinguished twist unitarily gauges a fixed moving-window spectrum

**Status:** `EXACT-DERIVED + UNITARY-GAUGE + EXACT-INTEGER-KERNEL + SOURCE-GATE-REFINEMENT`. `ANF-152` expresses the bow target as a Rayleigh quotient for a diagonally normalized moving-window Gram matrix and concludes that the post-sieve innovation must concentrate in its vanishing-eigenvalue sector. There is an additional exact simplification: the logarithmic twist does not change that Gram spectrum at all. For every real `U`, the twisted normalized Gram matrix is diagonally unitarily conjugate to the untwisted one. Thus rank, eigenvalues, singular scales, spectral multiplicities, and every spectral threshold are `U`-independent; the distinguished twist acts only by rotating the arithmetic source vector relative to a fixed untwisted geometry. In the integer length-`K` discretization of `ANF-146`, this fixed geometry already has an exact `(K-1)`-dimensional kernel, consisting after de-normalization of zero-mean `K`-periodic sequences. Hence the remaining bow question is not whether the distinguished twist creates a special low spectrum. It is whether the actual post-sieve innovation, after the explicit demodulation `n^{-iU}`, lands in the fixed low-spectrum sector.

## 1. The logarithmic carrier is an exact diagonal unitary gauge

Keep the exact continuous bow setup of `ANF-152`. For each integer site `n` whose moving-window atom is nonzero on `[X,2X]`, write

\[
\psi_n(x)
:=
1_{[X,2X]}(x)
1_{\{x<n\le x+K\}}.
\tag{1}
\]

Let `T_0` be the untwisted synthesis map

\[
(T_0 c)(x):=\sum_n c_n\psi_n(x),
\tag{2}
\]

and let

\[
D_U:=\operatorname{diag}(n^{-iU}).
\tag{3}
\]

Since every diagonal entry of `D_U` has modulus one, `D_U` is unitary. The synthesis map with the exact Archimedean carrier is simply

\[
\boxed{T_U=T_0D_U.}
\tag{4}
\]

Therefore its Gram matrix satisfies

\[
\boxed{
G_U=T_U^*T_U
=D_U^*G_0D_U.
}
\tag{5}
\]

This identity is exact for the original continuous `x`-integral, with arbitrary real `X`, `K`, and `U`; no integer discretization or asymptotic replacement has entered.

The diagonal is independent of `U`:

\[
d_n=(G_U)_{nn}=\|\psi_n\|_2^2.
\tag{6}
\]

Let

\[
W:=\operatorname{diag}(\sqrt{d_n}),
\qquad
C_U:=W^{-1}G_UW^{-1}.
\tag{7}
\]

Because `W` and `D_U` are diagonal and commute, (5) gives

\[
\boxed{
C_U=D_U^*C_0D_U.
}
\tag{8}
\]

Consequently

\[
\boxed{\operatorname{spec}(C_U)=\operatorname{spec}(C_0)}
\tag{9}
\]

with identical multiplicities for every real `U`. The same is true of rank, nullity, operator norm, stable spectral statistics, trace powers, and every eigenvalue-counting function. A spectral event cannot become distinguished merely because `U` lies in the bow range `U\asymp X^2`.

## 2. ANF-152 can be written with one fixed untwisted projector family

For the actual residual `r_X` of `ANF-149`, put as in `ANF-152`

\[
z:=Wr_X.
\tag{10}
\]

The normalized bow variance at twist `U` is

\[
q_X(U;K)
=
\frac{z^*C_Uz}{\|z\|_2^2}.
\tag{11}
\]

Using (8) and defining

\[
y_U:=D_Uz,
\tag{12}
\]

we obtain the exact gauge-fixed form

\[
\boxed{
q_X(U;K)
=
\frac{y_U^*C_0y_U}{\|y_U\|_2^2},
\qquad
\|y_U\|_2=\|z\|_2.
}
\tag{13}
\]

Thus all dependence on the distinguished twist has moved into the source vector

\[
\boxed{
(y_U)_n
=
\sqrt{d_n}\,r_X(n)n^{-iU}
=
\sqrt{d_n}\,Q_R(n)\eta_R(n)n^{-iU}.
}
\tag{14}
\]

The destination operator can be frozen once and for all at `U=0`.

The spectral concentration statement of `ANF-152` transforms just as cleanly. If `P_{U,E}` denotes the spectral projector of `C_U` onto a Borel set `E`, unitary functional calculus gives

\[
\boxed{
P_{U,E}=D_U^*P_{0,E}D_U.
}
\tag{15}
\]

Hence for every `tau>0`,

\[
\boxed{
\frac{\|P_{U,(\tau,\infty)}z\|_2^2}{\|z\|_2^2}
=
\frac{\|P_{0,(\tau,\infty)}y_U\|_2^2}{\|y_U\|_2^2}.
}
\tag{16}
\]

A successful bow sequence therefore requires the **demodulated arithmetic innovation** `y_U` to avoid the fixed positive-spectrum sector of `C_0`. The low-spectrum geometry itself is not selected jointly by arithmetic and twist. The arithmetic/twist pair only selects a direction inside one universal moving-window geometry.

This rules out a possible misreading of the source gate. One cannot hope to prove the bow by showing that the Gram spectrum develops unusually small eigenvalues specifically at the distinguished logarithmic twist: (9) makes such a phenomenon impossible. Any twist-specific theorem has to control source projections or an equivalent phase-sensitive quantity.

## 3. In the integer box model the universal geometry has an exact `K-1` dimensional kernel

The finite integer model of `ANF-146` makes the gauge-fixed geometry completely explicit. Let

\[
A_{N,K}:\mathbb C^{N+K-1}\to\mathbb C^N,
\qquad
(A_{N,K}b)_j
=
\sum_{r=1}^{K}b_{j+r},
\quad 0\le j<N,
\tag{17}
\]

with integer `1<=K<=N`. `ANF-146` proves that `A_{N,K}` has rank `N`, so

\[
\boxed{\dim\ker A_{N,K}=K-1.}
\tag{18}
\]

The kernel can be classified exactly. Set

\[
s_j:=\sum_{r=1}^{K}b_{j+r}.
\tag{19}
\]

If `A_{N,K}b=0`, then every `s_j=0`, and consecutive differences give

\[
0=s_{j+1}-s_j=b_{j+K+1}-b_{j+1}
\qquad(0\le j<N-1).
\tag{20}
\]

Thus

\[
b_{n+K}=b_n
\qquad(1\le n\le N-1),
\tag{21}
\]

while the first window gives

\[
\sum_{r=1}^{K}b_r=0.
\tag{22}
\]

Conversely, (21)--(22) make every length-`K` moving sum equal to the first and therefore zero. Hence

\[
\boxed{
A_{N,K}b=0
\iff
b\text{ is the restriction of a }K\text{-periodic sequence with zero period mean}.
}
\tag{23}
\]

Equivalently, the nonconstant `K`th-root characters

\[
b_n^{(\ell)}=e^{2\pi i\ell n/K},
\qquad 1\le\ell\le K-1,
\tag{24}
\]

form a basis of the kernel. The single root-of-unity plane wave used in `ANF-146` was therefore one member of the entire exact null family rather than an isolated cancellation profile.

Diagonal normalization does not remove this kernel. If `d_n` is the number of output windows containing site `n` and `W=\operatorname{diag}(\sqrt{d_n})`, then

\[
C_0=W^{-1}A_{N,K}^*A_{N,K}W^{-1}
\tag{25}
\]

has the same nullity, with

\[
z\in\ker C_0
\iff
W^{-1}z\in\ker A_{N,K}.
\tag{26}
\]

After restoring the logarithmic twist,

\[
\boxed{
\ker C_U=D_U^*\ker C_0.
}
\tag{27}
\]

Thus in the integer bow discretization an unnormalized coefficient vector `r` has exactly zero moving-window energy at twist `U` precisely when

\[
\boxed{
b_n:=r_n n^{-iU}}
\tag{28}
\]

is `K`-periodic on the available range and has zero sum over one period. This is an exact source-versus-geometry interface, with all edge weights retained by (25)--(27).

## 4. Near-nullspace alignment must not be overinterpreted as approximate periodicity

The exact kernel description is useful, but the actual target of `ANF-152` is only `q_X=o(1)`, not `q_X=0`. Without a quantitative spectral gap above the kernel, small Rayleigh quotient does not imply proximity to the exact periodic family (23).

There is a direct stress test. In the integer model, for arbitrary `b`, (19)--(20) give

\[
\sum_{n=1}^{N-1}|b_{n+K}-b_n|^2
=
\sum_{j=0}^{N-2}|s_{j+1}-s_j|^2
\le
4\sum_{j=0}^{N-1}|s_j|^2
=
4V_{N,K}(b).
\tag{29}
\]

If `q=V/D`, then `D<=K\|b\|_2^2`, so (29) yields only

\[
\boxed{
\sum_{n=1}^{N-1}|b_{n+K}-b_n|^2
\le
4qK\,\|b\|_2^2.
}
\tag{30}
\]

The bow requirement `q=o(1)` by itself does not force the right-hand side to be `o(\|b\|_2^2)` because `K\to\infty`. A genuine approximate-periodicity conclusion from this route would require at least the stronger rate `qK=o(1)`, or a new lower bound controlling the small positive spectrum. Therefore (23) should be treated as the exact zero-energy geometry, not silently promoted to a characterization of every near-null vector.

This boundary matters for the next source theorem. The safe exact statement is (16): the twisted source must concentrate below every fixed positive spectral threshold of the **fixed untwisted operator**. Whether that concentration can be converted into a more elementary arithmetic recurrence, high-pass condition, or lag-`K` relation remains a separate quantitative problem.

## 5. Prior-art boundary and frontier consequence

The underlying harmonic analysis is classical. Rectangular moving windows have the familiar geometric-sum/Dirichlet-kernel frequency response, their autocorrelation produces the triangular coefficients of the Fejer kernel, and the nonconstant `K`th-root characters are the standard zeros of a length-`K` box filter. The literature audit found precisely this classical Fourier/filter picture; no external theorem is needed for (4)--(30), which are finite-dimensional identities. `ANF-146` already records the boxcar/Dirichlet-kernel prior-art boundary, so this finding introduces no new load-bearing source and `SOURCES.md` need not change.

The Mathia-specific content is the exact specialization to the post-sieve bow normal form of `ANF-152`. It separates the live problem more sharply than the phrase “near-nullspace alignment at the distinguished twist” can suggest. **The spectrum is not distinguished.** The moving-window spectrum is fixed and source-blind; the distinguished twist appears only in the demodulated vector (14). In the integer model the geometry even supplies an exact `(K-1)`-dimensional nullspace at every twist, related by the trivial gauge (27).

Accordingly the next useful positive theorem should estimate

\[
\|P_{0,(\tau,\infty)}D_UWr_X\|_2
\tag{31}
\]

directly at the source-selected `U`, or find an arithmetic representation that controls the same fixed spectral projection before absolute values destroy phase information. A negative theorem can instead show that a fixed fraction of `D_UWr_X` remains in a positive spectral sector of `C_0`. What cannot contribute is any argument based solely on twist-dependent eigenvalue statistics of the moving-window Gram operator, because those statistics are exactly constant in `U`.

For `analytic_frontier`, this removes one more geometric ambiguity from the bow gate. The unresolved content is entirely **directional source transport under the logarithmic modulation**, not the creation of a special destination spectrum at the distinguished twist.