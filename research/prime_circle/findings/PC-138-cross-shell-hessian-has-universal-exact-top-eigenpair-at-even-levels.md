# PC-138 — cross-shell Hessian has universal exact top eigenpair at even levels

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE`. PC-136 proved that the canonical cross-shell-only resultant Hessian differs from the full inverse-square regular-polygon Laplacian by the positive semidefinite direct sum of the within-shell Laplacians, while PC-137 showed that the first spectral moment of the primorial defect is exactly Nicolas/Mertens data. PC-136 deliberately left open whether an extreme eigenvalue or edge mode could retain arithmetic information invisible to the bulk trace.

For the absolute upper spectral edge, the answer is exact and negative. At **every even level** `N`, not merely asymptotically and not merely along primorials, the cross-shell Hessian has the same unique top eigenvalue as the full polygon,

\[
\boxed{\lambda_{\max}(H_N^\times)=\frac{N^2}{8},}
\]

with the same alternating Fourier eigenvector `((-1)^a)_{a mod N}`. The reason is intrinsic to the exact-order shell decomposition: at even `N`, parity is constant on every primitive shell, so the entire within-shell defect annihilates the alternating mode. Thus the normalized primorial top edge is identically `1/8` and cannot carry an RH-sensitive fluctuation.

## 1. Exact cross-shell decomposition

Index the roots of unity by

\[
z_a=\exp(2\pi i a/N),\qquad a\in\mathbb Z/N\mathbb Z,
\]

and write

\[
\operatorname{ord}(a):=\operatorname{ord}(z_a)=\frac{N}{\gcd(a,N)}.
\]

Let `L_N` be the full inverse-square chord Laplacian with edge weights

\[
w_{ab}:=\frac1{|z_a-z_b|^2}
=\frac1{4\sin^2(\pi(a-b)/N)}
\qquad(a\ne b).
\]

Let `H_N^times` be the PC-136 cross-shell-only Laplacian: the edge `(a,b)` is retained exactly when `ord(a) != ord(b)`. Then

\[
L_N-H_N^\times=D_N
=\bigoplus_{d\mid N}L_d^{\rm int}\succeq0,
\]

where `L_d^int` is the weighted Laplacian on the exact-order shell

\[
S_d:=\{a\bmod N:\operatorname{ord}(a)=d\}.
\]

This is the exact PC-136 decomposition. In particular,

\[
H_N^\times\preceq L_N.
\]

The full polygon spectrum is the classical `csc^2` spectrum already used in PC-032 and anchored in `SOURCES.md` by Calogero--Perelomov:

\[
\lambda_k(L_N)=\frac{k(N-k)}2,
\qquad k=0,\ldots,N-1.
\]

For even `N` the maximum is unique, attained at `k=N/2`, and equals

\[
\lambda_{N/2}(L_N)=\frac{N^2}{8}.
\]

Its Fourier eigenvector is

\[
q_a=e^{2\pi i(N/2)a/N}=(-1)^a.
\]

## 2. Parity is constant on every exact-order shell

Take any divisor `d|N`. Every element of `S_d` has the form

\[
a=\frac Nd\,u,
\qquad u\in(\mathbb Z/d\mathbb Z)^\times.
\]

Assume `N` is even. There are exactly two cases.

If `N/d` is even, then every such `a` is even and hence

\[
q_a=+1.
\]

If `N/d` is odd, then `d` must be even. Since `u` is a unit modulo the even integer `d`, `u` is odd; therefore `a=(N/d)u` is odd and

\[
q_a=-1.
\]

Consequently `q` is constant on each exact-order shell:

\[
\boxed{
q|_{S_d}
=
\begin{cases}
+1,&2\mid N/d,\\
-1,&2\nmid N/d.
\end{cases}}
\]

Every within-shell Laplacian annihilates a constant vector on its shell, so

\[
\boxed{D_Nq=0.}
\]

This is the load-bearing identity. It uses the actual divisor-shell structure rather than a generic trace estimate.

For a squarefree primorial `N`, the sign rule simplifies further: `q=+1` on odd-order shells and `q=-1` on even-order shells. Thus even the shell-level content of the top eigenvector sees only the local factor `2`; it does not encode the other primes of the primorial.

## 3. The upper spectral edge is exactly universal

Since `D_Nq=0`,

\[
H_N^\times q
=(L_N-D_N)q
=L_Nq
=\frac{N^2}{8}q.
\]

On the other hand, `D_N\succeq0` gives

\[
\lambda_{\max}(H_N^\times)
\le
\lambda_{\max}(L_N)
=\frac{N^2}{8}.
\]

The displayed eigenvector attains the bound, hence

\[
\boxed{
\lambda_{\max}(H_N^\times)=\frac{N^2}{8}
\qquad(2\mid N).
}
\]

The top eigenspace is also one-dimensional. Indeed, if a unit vector `x` satisfies

\[
H_N^\times x=\frac{N^2}{8}x,
\]

then

\[
\frac{N^2}{8}
=\langle x,H_N^\times x\rangle
=\langle x,L_Nx\rangle-\langle x,D_Nx\rangle
\le\frac{N^2}{8}.
\]

Equality forces both `x` to lie in the unique top eigenspace of `L_N` and `D_Nx=0`. Therefore

\[
\boxed{
\ker\!\left(H_N^\times-\frac{N^2}{8}I\right)
=\operatorname{span}\{((-1)^a)_a\}.
}
\]

At the lower edge, `H_N^times` is a graph Laplacian and hence has the constant zero mode. It is connected for every `N>1`, because the order-one vertex `a=0` is joined with positive weight to every vertex of order greater than one. Thus the zero mode is simple. For every even `N>1`, both absolute spectral endpoints and both endpoint eigenspaces are therefore fixed exactly:

\[
0=\lambda_{\min}(H_N^\times)
<\cdots<
\lambda_{\max}(H_N^\times)=\frac{N^2}{8},
\]

with endpoint vectors `1` and `(-1)^a` respectively.

## 4. Primorial consequence and the edge no-go

Every primorial from `2` onward is even. Hence for

\[
N_k=\prod_{j\le k}p_j
\]

we have the finite identity

\[
\boxed{
\frac{\lambda_{\max}(H_{N_k}^\times)}{N_k^2}=\frac18
}
\]

for every `k`, with no limiting argument and no Mertens correction. In particular, the first-moment defect of PC-136/PC-137 can tend to zero while the operator defect itself remains nontrivial, but the **absolute upper edge is protected exactly** by the shellwise parity mode.

This rules out the most direct remaining edge statistic from PC-136:

\[
\text{primorial cross-shell Hessian}
\longrightarrow
\text{top eigenvalue / spectral norm}
\longrightarrow
\text{RH-sensitive fluctuation}.
\]

There is no fluctuation to amplify: the normalized top eigenvalue is identically `1/8`. The top eigenvector is equally rigid and, at squarefree even levels, records only whether the shell order contains the prime `2`.

The statement is deliberately narrower than a full edge-spectrum no-go. It does **not** determine the second-largest eigenvalue, the size of the top spectral gap, lower nonzero eigenvalues, internal outliers below the universal top edge, localization of non-extremal modes, or nonlinear/cross-level statistics formed from those modes. Those remain possible carriers of arithmetic data. What is closed is the absolute spectral norm/top-eigenpair route itself.

## 5. Prior-art and novelty audit

The ingredients outside the prime-circle specialization are classical:

- the full `csc^2` regular-polygon spectrum `k(N-k)/2` is the Calogero--Perelomov structure already anchored in `SOURCES.md` for PC-032;
- deleting a set of positive weighted edges subtracts a positive semidefinite Laplacian, so the resulting Laplacian is below the original one in Loewner order;
- constant-on-cell vectors lie in the kernel of the corresponding within-cell Laplacians.

Directed searches for inverse-square/cyclotomic Laplacians partitioned by exact root order, primitive-root `csc^2` shell spectra, Ramanujan-weighted versions, and equitable weighted-graph partitions did not reveal an established RH mechanism or a named theorem matching this exact cross-shell parity edge identity. Nearby equitable-partition and weighted-graph perturbation literature treats the general spectral mechanisms, not this arithmetic specialization. Absence of a matching formulation is **not** being used as a novelty claim: the research value here is the exact negative consequence for the canonical PC-136 operator.

The specialization itself is elementary once the right mode is tested. Its importance is therefore not that it creates a new spectral theorem, but that it removes an explicitly open prime-circle branch without importing any external spectral parameter or asymptotic hypothesis.

## 6. Falsification surface

1. For every even `N` and every divisor `d|N`, direct enumeration of the shell `S_d` must show that all exponents in `S_d` have the same parity. A single mixed-parity exact-order shell would refute the proof.
2. Direct construction of `D_N=L_N-H_N^times` must satisfy `D_N((-1)^a)_a=0`.
3. Direct diagonalization must give `lambda_max(H_N^times)=N^2/8`; for example the exact targets are `9/2` at `N=6`, `225/2` at `N=30`, and `11025/2` at `N=210`.
4. The claim is restricted to even levels. No analogous exact top-mode statement is asserted here for odd `N`.
5. The result does not imply that the rest of the edge spectrum is universal. Any future use of the second eigenvalue, top gap, localized non-extremal modes, or cross-level edge data requires an independent audit rather than being rejected by PC-138.
