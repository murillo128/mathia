# NB-031 — moving tail-adjacent sectors are uniformly Gram-whitened target-poor

**Status:** `EXACT-DERIVED + TARGET-AWARE-TAIL-SECTOR + GRAM-WHITENED-TARGET-BOUND + MACROSCOPIC-NUISANCE-UPGRADE + NEGATIVE/METHOD-BOUNDARY`. `NB-025`--`NB-026` show that high-index adjacent cancellations generate many low-Rayleigh directions with small target functional in Euclidean coefficient normalization. `NB-030` shows why that is not enough on the unrestricted adjacent span: the best adjacent approximation can itself be low-Rayleigh and raw-target-poor while becoming maximally target-bearing after Hilbert normalization. The missing distinction can be made exactly for a moving **high-index tail** of the adjacent family.

Let

\[
g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
\qquad
h_n:=g_n-g_{n+1},
\]

and for integers `2<=M<N` define

\[
W_{M,N}^{\rm tail}
:=\operatorname{span}\{h_M,h_{M+1},\ldots,h_{N-1}\}.
\tag{1}
\]

Then every nonzero `w in W_(M,N)^tail` obeys the coordinate-free target-angle estimate

\[
\boxed{
\frac{|\langle e,w\rangle|^2}{\|w\|^2}
\le
\varepsilon_M,
\qquad
\varepsilon_M
:=
\frac1M+
\frac{(H_M-1)^2}{M-H_M}.
}
\tag{2}
\]

In particular,

\[
\boxed{
\varepsilon_M
=O\!\left(\frac{(\log M)^2}{M}\right)
\longrightarrow0,
}
\tag{3}
\]

uniformly in the upper endpoint `N`. The same bound therefore holds on the closed infinite tail

\[
W_M^{\rm tail}
:=\overline{\operatorname{span}}\{h_n:n\ge M\}.
\tag{4}
\]

This is exactly the Gram-relative target-poorness that remained missing after `NB-030`. If `phi_n=g_n/||g_n||`, `widetilde G_N` is the normalized canonical Gram matrix, `widetilde b_N=(<e,phi_n>)`, and

\[
E_{M,N}:=\operatorname{span}\{\beta^{(n)}:M\le n<N\},
\qquad
\beta_n^{(n)}=\|g_n\|,
\quad
\beta_{n+1}^{(n)}=-\|g_{n+1}\|,
\tag{5}
\]

then for every `x in E_(M,N)`,

\[
\boxed{
|\widetilde b_N^*x|^2
\le
\varepsilon_M\,x^*\widetilde G_Nx.
}
\tag{6}
\]

Thus a moving hard lower-index cutoff turns adjacent cancellation into a genuine target-independent nuisance sector even after Gram whitening. Low Rayleigh is not needed for (6); intersecting this tail sector with any low-Rayleigh sector preserves the estimate.

There is an immediate strengthening of `NB-026`. Take `M=ceil(N/2)`. Its explicit disjoint-pair space `U_N`, and hence its `m_N`-dimensional Ritz subspace `L_N`, lie inside `E_(M,N)`. Therefore the same `L_N`, with

\[
\dim L_N=m_N\ge\frac{N-7}{8},
\]

satisfies simultaneously

\[
\boxed{
 v^*\widetilde G_Nv
 \le
 \frac{16(H_N+2)}N\,\|v\|_2^2
}
\tag{7}
\]

and the stronger target estimate

\[
\boxed{
|\widetilde b_N^*v|^2
\le
\varepsilon_{\lceil N/2\rceil}\,
 v^*\widetilde G_Nv,
\qquad
\varepsilon_{\lceil N/2\rceil}
=O\!\left(\frac{(\log N)^2}{N}\right).
}
\tag{8}
\]

So a **linear-dimensional** portion of the canonical weak-Gram geometry is not merely raw-coefficient-target-poor: it is uniformly target-poor after Hilbert normalization. This supplies a rigorous nuisance baseline against which the target-selected weak-mode occupation from `NB-024` must be compared.

## 1. Every sufficiently early shell sees the entire tail through one scalar

Use the harmonic shells

\[
I_t=\left(\frac1{t+1},\frac1t\right],
\]

on which `NB-008` gives the exact canonical formula

\[
g_n|_{I_t}=\left\{\frac tn\right\}.
\tag{9}
\]

If `1<=t<M<=n`, then `0<t/n<1` and `0<t/(n+1)<1`, so the fractional parts in (9) are ordinary quotients. Hence

\[
\boxed{
 h_n|_{I_t}
 =\frac tn-\frac t{n+1}
 =\frac{t}{n(n+1)}
 \qquad(1\le t<M\le n).
}
\tag{10}
\]

Consequently every finite combination

\[
w=\sum_{n=M}^{N-1}c_nh_n
\]

has, on **all** of the first `M-1` shells, the rank-one profile

\[
\boxed{
 w|_{I_t}=A(w)t,
\qquad
A(w):=\sum_{n=M}^{N-1}\frac{c_n}{n(n+1)}.
}
\tag{11}
\]

No Gram estimate or asymptotic approximation is used here. The early-shell restriction of the whole tail-adjacent space has dimension one, regardless of how many tail edges are allowed or how strongly their later shells interact.

This rank-one collapse is precisely what the unrestricted adjacent span of `NB-029`--`NB-030` avoids: when edges beginning at arbitrarily small indices are available, the first-shell profile is not constrained by a lower cutoff tending to infinity.

## 2. Exact early-shell least squares bounds the target projection

The target is `e(x)=1`. Since `|I_t|=1/(t(t+1))`, (11) gives for every `w in W_(M,N)^tail`

\[
\|e-w\|^2
\ge
\sum_{t=1}^{M-1}
\frac{|1-A(w)t|^2}{t(t+1)}.
\tag{12}
\]

For an arbitrary complex scalar `A`, write

\[
S_0:=\sum_{t=1}^{M-1}\frac1{t(t+1)},
\qquad
S_1:=\sum_{t=1}^{M-1}\frac1{t+1},
\qquad
S_2:=\sum_{t=1}^{M-1}\frac{t}{t+1}.
\]

The sums are exact:

\[
S_0=1-\frac1M,
\qquad
S_1=H_M-1,
\qquad
S_2=M-H_M.
\tag{13}
\]

Since `S_2>0`, completing the square in

\[
S_0-2S_1\operatorname{Re}A+S_2|A|^2
\]

gives

\[
\min_{A\in\mathbb C}
\sum_{t=1}^{M-1}
\frac{|1-At|^2}{t(t+1)}
=
1-\frac1M-rac{(H_M-1)^2}{M-H_M}.
\tag{14}
\]

Thus

\[
\operatorname{dist}(e,W_{M,N}^{\rm tail})^2
\ge
1-\varepsilon_M.
\tag{15}
\]

Because `||e||=1`, orthogonal projection gives

\[
\boxed{
\|P_{W_{M,N}^{\rm tail}}e\|^2
=1-\operatorname{dist}(e,W_{M,N}^{\rm tail})^2
\le\varepsilon_M.
}
\tag{16}
\]

For any `w` in the tail space,

\[
\langle e,w\rangle
=\langle P_{W_{M,N}^{\rm tail}}e,w\rangle,
\]

so Cauchy--Schwarz and (16) prove (2). The bound is independent of `N`; taking increasing finite spans and using continuity of orthogonal projection onto the closed union proves the infinite-tail statement (4).

Finally, `H_M=log M+gamma+O(1/M)` and `M-H_M=M+O(log M)` give (3). No prime-number theorem, Möbius estimate, zeta input, or closure assumption enters the result.

## 3. Translation to the normalized Gram geometry

Let

\[
T_Nx:=\sum_{n=2}^Nx_n\phi_n.
\]

By construction of the edge vectors in (5),

\[
T_N\beta^{(n)}=g_n-g_{n+1}=h_n,
\]

so

\[
T_NE_{M,N}=W_{M,N}^{\rm tail}.
\tag{17}
\]

For every `x in E_(M,N)`,

\[
|\widetilde b_N^*x|^2
=|\langle e,T_Nx\rangle|^2,
\qquad
x^*\widetilde G_Nx=\|T_Nx\|^2.
\tag{18}
\]

Applying (2) to `T_Nx` proves (6). This is invariant under any change of coordinates **inside the same Hilbert subspace**: (6) is simply the statement that the target projection onto that subspace has squared norm at most `epsilon_M`. It is therefore not vulnerable to the coefficient-normalization objection that limits the target estimate in `NB-026`.

For `M=ceil(N/2)`, every adjacent vector used to define `U_N` in `NB-026` begins at an index at least `M`; hence

\[
L_N\subset U_N\subset E_{M,N}.
\tag{19}
\]

Equation (8) follows from (6), while (7) and the dimension bound are exactly the previously derived compression/min-max estimates. The new content is their compatibility with a vanishing **Gram-relative** target angle on the same macroscopic subspace.

## 4. Adversarial controls and boundary

This result does **not** contradict `NB-029`, which states that the closed span of all adjacent differences starting from index `2` equals the full canonical Nyman closure. The present spaces move their lower endpoint to infinity. Equation (16) shows that those moving tails lose the target even though the fixed full adjacent family retains it. Hence the target-bearing cooperation exhibited by `NB-030` cannot be supported entirely on edges whose starting indices escape to infinity.

The statement also does not imply that every small eigenvector of the full normalized Gram matrix is target-poor. `L_N` is an explicitly constructed Ritz subspace inside a tail-adjacent family; global Gram eigenvectors need not preserve that subspace. Nor does (8) show that the canonical best-approximation coefficient vector has a large Euclidean projection outside `L_N`: the useful decomposition is in Hilbert/Gram geometry, where nonorthogonal complements must be handled explicitly.

A fixed cutoff `M` does not become asymptotically target-null as `N` grows; the decay in (3) requires `M->infinity`. This is essential. Long-range target-bearing behavior may still be assembled from adjacent edges across many scales, provided enough low-index structure remains available. The theorem rules out only a pure moving-tail explanation.

The early-shell restriction is also special to the canonical integer dictionary and its exact shell formula. It is not an abstract theorem that every adjacent basis difference is harmless. That source-specific structure is the point: unlike a Gram-only nuisance definition, this one has a direct target-relative certificate.

## 5. Prior-art and novelty boundary

The local regularity and Gram geometry of fractional-part dilations belong to the classical Nyman--Beurling autocorrelation literature, and recent work of Werner Ehm studies exact Gram formulae while Hugh Carvill studies a different multiplicative-ladder compressibility regime. A targeted search for consecutive/successive-difference Nyman bases, tail adjacent spans, and target-angle estimates did not locate the specific rank-one early-shell restriction (11) or the resulting uniform Gram-whitened bound (2)/(6). Search absence is not a priority claim.

No external theorem is load-bearing in the proof: (9) is the canonical shell identity already established locally, and the rest is finite weighted least squares plus Hilbert projection geometry. `SOURCES.md` therefore needs no new dependency. The durable delta is the exact target-relative consequence of imposing a moving lower-index cutoff, especially the upgrade (8) of the macroscopic nuisance sector from `NB-026`.

## 6. Consequence for the live spectral question

`NB-030` rules out defining nuisance as “all adjacent directions with low Rayleigh quotient,” because the unrestricted adjacent span can contain a target-selected low-Rayleigh approximant. `NB-031` identifies a proper restriction that survives that objection: **high-index tail adjacency is uniformly target-poor in the correct Gram/Hilbert normalization**, with an explicit rate `O((log M)^2/M)` independent of the upper section size.

This gives a clean baseline for the target-selected occupation problem. The low-Rayleigh sector from `NB-024` should not be credited merely for overlapping the linear-dimensional tail nuisance sector of (7)--(8). Any arithmetic signal must survive after accounting for this Gram-whitened target-poor background, or must use cross-scale cooperation that necessarily reaches below every moving hard cutoff.

What remains unresolved is quantitative separation of the canonical target-selected vector from that nuisance geometry. A useful next theorem would control the Hilbert/Gram mass of the optimal approximant outside a moving tail-adjacent sector, or identify a multiscale orthogonalization in which the tail pieces retain (6) while the surviving cross-scale component is tied to Möbius locking. The present result supplies the missing exact nuisance certificate; it does not yet convert that separation into a new bound for the Nyman distance and does not advance RH by itself.