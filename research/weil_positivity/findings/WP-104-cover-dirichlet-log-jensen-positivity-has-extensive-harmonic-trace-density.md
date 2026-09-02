# WP-104 — The cover-Dirichlet logarithmic Jensen defect is positive but has an extensive harmonic trace density

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + NONDIAGONAL-JENSEN + GLT/FEJER-ASYMPTOTIC + MATCHED-CONTROL + NOT-GLOBAL-WEIL`.

`WP-093` leaves a particularly natural nonlinear test of its strongest positive survivor.  The critical exact-cover form

\[
G=T^*T,
\qquad
(Tx)_j=(j+1)(x_{j+1}-x_j),
\]

is positive for a geometric reason, has the exact cover law

\[
W_n^*GW_n=nG,
\]

and has the continuous-dual-Hahn spectral parameter `1/4+t^2`.  Since `log` is operator concave, the most direct way to turn that scale covariance into a positive logarithmic response is the Davis--Choi--Jensen defect.

On aligned finite sections this defect is indeed positive, but its scalar behavior is rigidly wrong for Weil positivity.  Let `G_K` be the `K x K` finite section used in `WP-093`, including the terminal Dirichlet edge, and let

\[
W_{n,K}:\mathbb C^K\longrightarrow\mathbb C^{nK},
\qquad
W_{n,K}e_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r}.
\]

Then exactly

\[
W_{n,K}^*G_{nK}W_{n,K}=nG_K.
\]

Define

\[
\boxed{
J_{n,K}
:=\log(nG_K)-W_{n,K}^*(\log G_{nK})W_{n,K}.
}
\tag{1}
\]

For every fixed integer `n>=2` and every `K>=1`,

\[
\boxed{J_{n,K}\succeq0.}
\tag{2}
\]

However its trace is extensive.  As `K->infinity`,

\[
\boxed{
\frac1K\operatorname{Tr}J_{n,K}
\longrightarrow
c_n
:=2(H_n-1)-\log n
>0,
}
\tag{3}
\]

where `H_n=sum_{j=1}^n 1/j`.  Equivalently,

\[
\boxed{
\operatorname{Tr}J_{n,K}=Kc_n+o(K).
}
\tag{4}
\]

Thus ordinary trace does not produce a finite cutoff-independent positive response.  Dividing by volume does produce the positive intensive statistic `c_n`, but that statistic is arithmetically universal and has the wrong exact primitive.  With `c_1=0`, its divisor-Mobius primitive is already nonzero at a mixed-prime degree:

\[
\boxed{
c_6-c_3-c_2=\frac7{30}\ne0,}
\tag{5}
\]

whereas `Lambda(6)=0`; at the prime power `4`,

\[
\boxed{
c_4-c_2=\frac76-\log2\ne\log2=\Lambda(4).}
\tag{6}
\]

So the canonical non-diagonal logarithmic Jensen response has a clean independent positivity theorem but neither its raw trace nor its trace density supplies the finite Weil selector.  Removing the extensive term, or subtracting the harmonic correction in `c_n` to isolate `log n`, would be an additional signed renormalization whose sign is no longer inherited from (2).

This closes the direct route

```text
WP-093 critical weighted Dirichlet form
    -> exact cover compression G -> n G
    -> positive logarithmic Jensen defect
    -> ordinary trace or trace density
    -> logarithmic degree / Mangoldt selector / archimedean Weil term.
```

It does **not** classify renormalized subleading anomalies, non-trace states, other nonlinear scalarizations, arbitrary position-dependent infinite-range forms, or a genuinely coupled finite--archimedean construction.

## 1. Finite-section covariance is exact

For `N>=1`, let `T_N` be the upper-bidiagonal finite difference matrix implementing

\[
(T_Nx)_j=(j+1)(x_{j+1}-x_j)
\]

with the terminal convention `x_N=0`.  Then

\[
G_N=T_N^*T_N,
\]

so `G_N` is positive definite.  The same first-order block calculation as in `WP-093` gives the finite identity

\[
T_{nK}W_{n,K}=\sqrt n\,V_{n,K}T_K
\]

for an isometry `V_{n,K}` onto the appropriate residue class.  Hence

\[
\boxed{
W_{n,K}^*G_{nK}W_{n,K}=nG_K.
}
\tag{7}
\]

No infinite-volume domain issue is needed for the argument below.

## 2. Operator concavity of `log` gives a genuine positive defect

For a positive definite matrix `A` and an isometry `W`, the Davis--Choi--Jensen inequality for the operator-concave logarithm gives

\[
\log(W^*AW)\succeq W^*(\log A)W.
\tag{8}
\]

Apply (8) to `A=G_{nK}` and `W=W_{n,K}`.  By (7),

\[
\log(W^*AW)=\log(nG_K),
\]

which proves (2).

This is exactly the kind of sign source demanded by the research mandate at the local geometric level: the nonnegativity is known before any arithmetic readout and does not use zeta, zeros, RH, analytic continuation, or a fitted Weil kernel.

The question is what this positive operator actually says after the most canonical scalarization.

## 3. The relevant large-section symbol is the weighted discrete Laplacian

Set

\[
A_N:=\frac{G_N}{N^2}.
\tag{9}
\]

The tridiagonal coefficients of `G_N` show that `{A_N}` is a standard locally-Toeplitz/GLT discretization with scalar symbol

\[
\boxed{
a(x,\theta)=x^2\bigl(2-2\cos\theta\bigr),
\qquad 0<x<1.}
\tag{10}
\]

For the aligned sequence `N=nK`, group the fine indices into blocks of length `n`.  The block symbol is `x^2 L_n(phi)`, where `L_n(phi)` is the `n x n` Bloch fiber of the discrete circle Laplacian.  Its eigenvalues are

\[
2-2\cos\theta_j,
\qquad
\theta_j=\frac{\phi+2\pi j}{n},
\quad 0\le j<n.
\tag{11}
\]

Let

\[
u_n=\frac1{\sqrt n}(1,\ldots,1)^T,
\qquad
Q_n=u_nu_n^*.
\tag{12}
\]

The fine-space projection

\[
P_{n,K}:=W_{n,K}W_{n,K}^*
\]

is exactly the block-diagonal repetition of `Q_n`.  Therefore

\[
\operatorname{Tr}\bigl(W_{n,K}^*(\log G_{nK})W_{n,K}\bigr)
=
\operatorname{Tr}\bigl(P_{n,K}\log G_{nK}\bigr).
\tag{13}
\]

The only subtlety is that `log a(x,theta)` is unbounded at `x=0` and `theta=0`.  This is nevertheless an integrable logarithmic singularity, and here the passage from bounded continuous GLT test functions to `log` can be audited directly.  `WP-093` gives

\[
\det G_N=(N!)^2,
\]

hence

\[
\frac1N\operatorname{Tr}\log A_N
=
\frac2N\log(N!)-2\log N
\longrightarrow -2.
\tag{14}
\]

On the symbol side,

\[
\int_0^1 2\log x\,dx=-2,
\qquad
\frac1{2\pi}\int_0^{2\pi}\log(2-2\cos\theta)\,d\theta=0.
\tag{15}
\]

Apply ordinary block-GLT calculus first to the clipped functions `log(max(t,epsilon))`.  Equations (14)--(15) show that the clipped-to-unclipped trace error tends to zero after `N->infinity` and then `epsilon->0`.  Since `0<=P_{n,K}<=I`, the corresponding projected error is bounded by the full positive clipping error.  Thus the same limit is valid in (13) for the true logarithm.  No zeta regularization is being inserted.

## 4. Block averaging turns the logarithmic Laplacian into a Fejer integral

The normalized constant vector `u_n` has overlap with the Bloch eigenvector at angle `theta` equal to the normalized Dirichlet kernel.  Consequently the block spectral weight in (13) is the Fejer kernel

\[
F_n(\theta)
=\frac1n\left|1+e^{i\theta}+\cdots+e^{i(n-1)\theta}\right|^2
=
1+2\sum_{m=1}^{n-1}\left(1-\frac mn\right)\cos(m\theta).
\tag{16}
\]

The block-GLT trace calculation therefore gives

\[
\frac1K\operatorname{Tr}\bigl(P_{n,K}\log G_{nK}\bigr)
=
2\log(nK)-2+I_n+o(1),
\tag{17}
\]

where

\[
I_n
:=
\frac1{2\pi}\int_0^{2\pi}
F_n(\theta)\log(2-2\cos\theta)\,d\theta.
\tag{18}
\]

The classical Fourier series

\[
\log(2-2\cos\theta)
=-2\sum_{m\ge1}\frac{\cos(m\theta)}m
\tag{19}
\]

holds in the required `L^1` sense.  Combining (16) and (19) by orthogonality yields the exact finite sum

\[
\begin{aligned}
I_n
&=-2\sum_{m=1}^{n-1}
\frac{1-m/n}{m}\\
&=\boxed{
-2H_{n-1}+\frac{2(n-1)}n.}
\end{aligned}
\tag{20}
\]

The asymptotic is therefore controlled not by the continuous-dual-Hahn Gamma density of `G`, but by the elementary Fejer average of the local discrete-Laplacian logarithm.

## 5. The positive trace density is exact and strictly positive

Again from `WP-093`,

\[
\operatorname{Tr}\log G_K=\log\det G_K=2\log(K!).
\tag{21}
\]

Thus

\[
\frac1K\operatorname{Tr}\log(nG_K)
=
\log n+\frac2K\log(K!)
=
\log n+2\log K-2+o(1).
\tag{22}
\]

Subtract (17), use `N=nK`, and substitute (20):

\[
\begin{aligned}
\frac1K\operatorname{Tr}J_{n,K}
&\longrightarrow
-\log n-I_n\\
&=2H_{n-1}-\frac{2(n-1)}n-\log n\\
&=\boxed{2(H_n-1)-\log n.}
\end{aligned}
\tag{23}
\]

This proves (3)--(4).

The strict positivity can be seen without appealing back to Jensen.  For `n>1`,

\[
H_n-1=\sum_{k=2}^n\frac1k
>\int_1^n\frac{dx}{x+1}
=\log\frac{n+1}{2}.
\tag{24}
\]

Since `(n+1)^2>4n` for `n>1`,

\[
2\log\frac{n+1}{2}>\log n,
\]

and hence `c_n>0`.

For orientation,

\[
c_2=1-\log2,
\qquad
c_3=\frac53-\log3,
\]

and asymptotically

\[
c_n=\log n+2\gamma-2+o(1).
\tag{25}
\]

So the defect does contain logarithmic growth, but with an unavoidable positive harmonic/UV contribution forced by the same block geometry.

## 6. Both natural scalarizations fail the Weil arithmetic test

There are two obvious ways to scalarize the positive matrices `J_{n,K}`.

### 6.1 Raw trace

Equation (4) gives

\[
\operatorname{Tr}J_{n,K}\to+\infty
\]

linearly in `K` for every fixed nontrivial cover degree.  Therefore the ordinary trace does not define a finite global response.  Subtracting `Kc_n` is a renormalization, and the positivity `J_{n,K}>=0` gives no sign theorem for the remainder after that subtraction.

This is structurally different from the diagonal `WP-082` Jensen defect, whose ordinary trace is finite and collapses to a bounded dyadic statistic.  Moving to the non-diagonal positive survivor of `WP-093` does not recover a better finite trace; it moves to the opposite failure mode of an extensive positive anomaly.

### 6.2 Trace per block

The intensive limit `c_n` is finite and positive, so volume normalization is a legitimate matched control rather than something to ignore.  But it still fails exactly.

Put `c_1=0` and take the divisor-Mobius primitive.  At `n=6`, logarithms cancel and

\[
\begin{aligned}
(\mu*c)(6)
&=c_6-c_3-c_2\\
&=2(H_6-H_3-H_2+1)\\
&=\boxed{\frac7{30}},
\end{aligned}
\tag{26}
\]

while `Lambda(6)=0`.  Thus mixed-prime support survives.  At the prime power `4`,

\[
(\mu*c)(4)
=c_4-c_2
=\boxed{\frac76-\log2},
\tag{27}
\]

which is not `Lambda(4)=log2`.

Hence even the canonical finite positive density is not a hidden Mangoldt primitive.

## 7. The all-integer control and archimedean test remain fatal

Nothing in (1)--(27) distinguishes primes.  The cover maps, weighted Dirichlet form, operator Jensen theorem, Fejer kernel, and density `c_n` exist for every integer degree `n>=2`.  The same mechanism therefore survives an all-composite cover control unchanged.

Nor does `c_n` produce the archimedean channel required by the global Weil formula.  `WP-093` genuinely has a continuous-dual-Hahn spectral measure involving Gamma functions and the spectral threshold `1/4+t^2`, but the canonical logarithmic cover trace washes that detailed spectrum into the elementary harmonic number (23).  There is no test-function-dependent Gamma functional or polar/global counterterm in this scalar response.

One can algebraically isolate `log n` from (23) by subtracting `2(H_n-1)`, or search for a finite part after subtracting `Kc_n`.  Neither operation is forced by the positive Jensen theorem.  They are precisely new signed regularizations and must acquire an independent geometric justification before they can count under the research mandate.

## 8. Prior art and novelty audit

The positivity step is classical operator theory.  Chandler Davis, *A Schwarz Inequality for Convex Operator Functions*, Proc. Amer. Math. Soc. 8 (1957), 42--44, and Frank Hansen--Gert K. Pedersen, *Jensen's Operator Inequality*, Bull. London Math. Soc. 35 (2003), 553--564, DOI `10.1112/S0024609303002200`, are standard anchors for the compression/Jensen inequality used in (8).

The large-matrix step uses standard locally-Toeplitz/GLT calculus; a durable reference is Carlo Garoni and Stefano Serra-Capizzano, *Generalized Locally Toeplitz Sequences: Theory and Applications*, Vol. I, Springer (2017), DOI `10.1007/978-3-319-53679-8`.  The Fejer kernel and Fourier expansion (19) are classical harmonic analysis.

No novelty is claimed for operator Jensen, Fejer summation, logarithmic Laplacian Fourier coefficients, Stirling asymptotics, or GLT theory.  The durable Mathia-specific result is their application to the exact `WP-093` cover-positive Jacobi operator, yielding the explicit positive density

\[
2(H_n-1)-\log n
\]

and the exact arithmetic failures (26)--(27).  A directed search did not reveal a separate Weil-positivity mechanism attached to this particular defect; absence of such a source is not used as a novelty claim.

## 9. Boundary of the no-go

This finding closes only the **canonical logarithmic Jensen plus ordinary-trace/trace-density** use of the `WP-093` critical form.  It does not prove that every nonlinear functional of `G` is useless.

In particular it does not rule out:

1. a geometrically forced finite part or relative determinant whose subtraction law is independently canonical and whose sign survives the subtraction;
2. a non-trace state or boundary functional retaining the continuous-dual-Hahn spectral variable;
3. a genuinely position-dependent infinite-range kernel outside `WP-094`--`WP-095`;
4. prime-sensitive incidence acting before the cover reduction;
5. a finite--archimedean coupling that changes the operator before Jensen scalarization;
6. cohomological/intersection or graded sign mechanisms not represented by an ordinary positive Hilbert-space trace.

A falsification of the present claim would require an error in the exact finite covariance (7), Jensen positivity (8), the GLT/Fejer limit (17)--(20), or the arithmetic evaluations (26)--(27).

## Research consequence

The strongest non-diagonal positive cover supplier now has a sharper nonlinear boundary:

\[
\boxed{
\text{exact cover-positive }G
\xrightarrow{\ \log\text{-Jensen}\ }
J_{n,K}\succeq0
\xrightarrow{\ \operatorname{Tr}\ }
K\bigl(2(H_n-1)-\log n\bigr)+o(K).
}
\]

The sign is real and independent, but the scalar response is either divergent (raw trace) or universally harmonic with wrong Mobius support (trace density).  The appearance of `log n` inside the density is therefore not enough: the same geometry forces an additional term that survives mixed composites, while its detailed continuous-dual-Hahn/Gamma spectrum does not become the Riemann archimedean contribution.

A surviving use of `WP-093` must consequently add new intrinsic structure **before** the final scalar sign is read out, rather than rely on the most direct noncommutative logarithmic compression of the existing positive form.