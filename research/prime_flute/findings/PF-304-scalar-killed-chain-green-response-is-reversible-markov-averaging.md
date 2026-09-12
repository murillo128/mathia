# PF-304 — scalar killed-chain Green response is reversible Markov averaging

**Status:** `EXACT-DERIVED + CLASSICAL-MARKOV/M-MATRIX-MECHANISM + POSITIVE/ROUTE-NARROWING`.

[[research/prime_flute/findings/PF-303-scalar-robin-killing-has-unit-green-potential|PF-303]] identifies the assembled scalar Robin killing vector `d` as the exact Green-potential currency: for the finite constant-mode pant chain,

\[
H_N=L_{c,N}+D_N,\qquad D_N=\operatorname{diag}(d_0,\ldots,d_N),\qquad G_N=H_N^{-1},
\]

with `d_j>0`, `G_N\ge0`, and

\[
G_Nd=\mathbf 1,\qquad d^TG_N=\mathbf 1^T.
\]

PF-303 then uses the strongest endpoint consequence: a source satisfying `|f|\le C d` has a uniformly bounded scalar response. The same identities contain a larger exact structure that is useful for the still-open signed/mixed forcing problem.

Define

\[
\boxed{P_N:=G_ND_N.}
\]

Then `P_N` is a **reversible Markov kernel** with invariant weight `d`:

\[
\boxed{P_N\mathbf 1=\mathbf 1,\qquad d_i(P_N)_{ij}=d_j(P_N)_{ji}.}
\]

Consequently `P_N` is a contraction on every weighted space `\ell^p(d)`, `1\le p\le\infty`. Equivalently, for every real or complex scalar forcing `f`,

\[
\boxed{
\|G_Nf\|_{\ell^p(d)}
\le
\|D_N^{-1}f\|_{\ell^p(d)},
\qquad 1\le p\le\infty.
}
\]

The three most useful forms are

\[
\boxed{
\sum_j d_j |(G_Nf)_j|\le\sum_j|f_j|,
}
\tag{1}
\]

\[
\boxed{
\sum_j d_j |(G_Nf)_j|^2\le\sum_j\frac{|f_j|^2}{d_j},
}
\tag{2}
\]

and

\[
\boxed{
\max_j |(G_Nf)_j|
\le
\max_j\frac{|f_j|}{d_j}.
}
\tag{3}
\]

Thus the pointwise deficit domination used in PF-303 is only the `p=\infty` endpoint of an exact family of source-adapted contraction laws. For nonnegative `f`, (1) is an equality:

\[
\sum_j d_j(G_Nf)_j=\sum_j f_j.
\]

This matters because the physical `P/H` mixed forcing need not be nonnegative and need not be pointwise comparable with `d`. A bounded **integrated source mass** can still give a depth-uniform scalar response bound in the natural killing-weighted norm, with no spectral-gap assumption. The remaining question is whether this weaker response currency is strong enough after the true nonconstant-mode reassembly to control the PF-290 shorting deficit.

## Claim

Let `H_N=L_{c,N}+D_N` be the finite scalar constant-mode chain of PF-303, where `L_{c,N}` is the weighted path Laplacian and

\[
D_N=\operatorname{diag}(d_0,\ldots,d_N),\qquad d_j>0.
\tag{4}
\]

Let `G_N=H_N^{-1}` and `P_N=G_ND_N`. Then:

1. `P_N\ge0` entrywise and `P_N\mathbf1=\mathbf1`;
2. `d_i(P_N)_{ij}=d_j(P_N)_{ji}` for all `i,j`, hence `d^TP_N=d^T`;
3. `P_N` is self-adjoint on `\ell^2(d)` and is similar to the symmetric positive-definite matrix
   \[
   S_N:=D_N^{1/2}G_ND_N^{1/2};
   \tag{5}
   \]
4. every eigenvalue of `P_N` lies in `(0,1]`, with eigenvalue `1` carried by the constant vector;
5. for every `1\le p\le\infty` and every `h\in\mathbb C^{N+1}`,
   \[
   \boxed{\|P_Nh\|_{\ell^p(d)}\le\|h\|_{\ell^p(d)};}
   \tag{6}
   \]
6. therefore every forcing `f` satisfies
   \[
   \boxed{
   \|G_Nf\|_{\ell^p(d)}
   \le
   \|D_N^{-1}f\|_{\ell^p(d)}.
   }
   \tag{7}
   \]

Here

\[
\|h\|_{\ell^p(d)}^p:=\sum_jd_j|h_j|^p
\]

for finite `p`, with the usual sup norm at `p=\infty`.

## 1. PF-303 already contains the stochastic normalization

PF-303 proves `G_N\ge0` and `G_Nd=\mathbf1`. Since `D_N\mathbf1=d`,

\[
P_N\mathbf1
=G_ND_N\mathbf1
=G_Nd
=\mathbf1.
\tag{8}
\]

Thus `P_N` is entrywise nonnegative with row sums exactly one. No new gap estimate or asymptotic input is needed: multiplying the Green matrix by the **actual Robin killing** turns the finite response operator into a stochastic kernel exactly.

Because `G_N` is symmetric,

\[
d_i(P_N)_{ij}
=d_i(G_N)_{ij}d_j
=d_j(G_N)_{ji}d_i
=d_j(P_N)_{ji}.
\tag{9}
\]

This is detailed balance. Summing (9) over `i` and using the row sums gives

\[
d^TP_N=d^T.
\tag{10}
\]

So `d` is the invariant reversible measure. Probabilistically, `P_{ij}=G_{ij}d_j` is the finite killed-network absorption-location kernel: Green occupation at `j` multiplied by the local killing rate. That interpretation is classical; the project-specific point is that PF-303 identifies the PF-298 Robin losses as exactly the killing measure that stochasticizes the response.

## 2. Every weighted `L^p` norm contracts

For `1\le p<\infty`, convexity and the row-stochastic property give Jensen's inequality row by row:

\[
|(P_Nh)_i|^p
\le
\sum_j(P_N)_{ij}|h_j|^p.
\tag{11}
\]

Multiply by `d_i`, sum in `i`, and use stationarity (10):

\[
\sum_i d_i|(P_Nh)_i|^p
\le
\sum_j|h_j|^p\sum_i d_i(P_N)_{ij}
=
\sum_jd_j|h_j|^p.
\tag{12}
\]

For `p=\infty`, each row is a convex combination, so

\[
\|P_Nh\|_\infty\le\|h\|_\infty.
\tag{13}
\]

This proves (6). Since every scalar forcing can be written uniquely as `f=D_Nh`,

\[
G_Nf=G_ND_Nh=P_Nh,
\tag{14}
\]

and (7) follows. The cases `p=1,2,\infty` are exactly (1)--(3).

For `f\ge0`, positivity gives `G_Nf\ge0`; PF-303's identity `d^TG_N=\mathbf1^T` then makes (1) an equality. For signed or complex forcing, the only loss is cancellation before absolute values.

## 3. The symmetric representation confirms the spectrum and the absence of a hidden gap

The Markov representation is not merely an `\ell^1` trick. Because

\[
P_N
=D_N^{-1/2}
\bigl(D_N^{1/2}G_ND_N^{1/2}\bigr)
D_N^{1/2},
\tag{15}
\]

`P_N` is similar to the symmetric positive-definite matrix `S_N` in (5). Moreover

\[
H_N=L_{c,N}+D_N\ge D_N
\]

in quadratic-form order. Inverting the positive matrices reverses that order:

\[
0<G_N\le D_N^{-1}.
\tag{16}
\]

Hence

\[
0<S_N\le I.
\tag{17}
\]

All eigenvalues of `P_N` therefore lie in `(0,1]`. Equation (8) supplies the eigenvalue `1`, so there is **no strict contraction on constants** and no depth-uniform spectral gap hidden in this reformulation. This agrees with PF-297/PF-298: the gain is source-adapted normalization, not geometric mixing.

The same calculation is a useful representation audit. In conductance coordinates the object is a positive elliptic inverse; in killing coordinates it is reversible Markov averaging; after the symmetric similarity transform it is a positive contraction. These are three exact views of the same scalar operator, not three independent mechanisms.

## 4. What this changes in the mixed-response test

PF-303 proposed the sufficient comparison `|f|\lesssim d`, which is exactly the `p=\infty` requirement that `D_N^{-1}f` stay uniformly bounded. The present identity shows that this is stronger than necessary for every downstream quantity that can tolerate an integrated killing-weighted response norm.

Two weaker currencies are now available without further scalar analysis:

- bounded source mass `\sum_j|f_j|` gives bounded `\sum_jd_j|(G_Nf)_j|`;
- bounded source energy `\sum_j|f_j|^2/d_j` gives bounded `\sum_jd_j|(G_Nf)_j|^2`.

This gives a precise conditional bridge to [[research/prime_flute/findings/PF-296-weighted-source-row-moment-controls-canonical-fixed-axis-superpositions|PF-296]]. If the true finite `P/H` source extraction maps a coefficient vector `a` into scalar forcing `f` with, for example,

\[
\sum_j|f_j|
\lesssim
\sum_i q_i|a_i|,
\tag{18}
\]

then PF-296's bounded `\ell^1(q)` source moment automatically yields a depth-uniform scalar response in `\ell^1(d)`, even when no componentwise estimate `|f_j|\lesssim d_j` is available. Equation (18) is **not established here**; it is the concrete map-level comparison to test in the actual reassembly.

Likewise, if the physical downstream synthesis is uniformly bounded from `\ell^2(d)` or `\ell^1(d)` into the positive Sobolev space required by PF-292, then the corresponding source norm in (7) would close that scalar part of the PF-290 response. The scalar Green operator itself no longer creates amplification in any of these killing-normalized `L^p` currencies.

## 5. Prior art and novelty audit

The abstract ingredients are classical. PF-303 already records the nonsingular `M`-matrix / Stieltjes-matrix inverse-positivity mechanism and cites Berman--Plemmons, *Nonnegative Matrices in the Mathematical Sciences*. Standard finite-state Markov theory then says that a nonnegative row-stochastic kernel with an invariant measure is contractive on the corresponding `L^p` spaces, and detailed balance is the standard reversibility condition. A targeted literature check found these as ordinary `M`-matrix and reversible/absorbing-Markov-chain structure, not a new abstract theorem.

No novelty is claimed for stochastic kernels, detailed balance, Jensen contraction, the Loewner-order inverse inequality, or the absorption interpretation. The Mathia-specific contribution is the exact identification

\[
\boxed{P_N=G_ND_N}
\]

for the PF-298/PF-303 assembled Robin chain, together with the consequence that the still-open physical source comparison has an entire scale of natural killing-normalized norms rather than only the pointwise `|f|\lesssim d` endpoint.

No external theorem is load-bearing for the project statement: positivity, stochasticity, reversibility, and all norm estimates follow directly from PF-303's finite matrices.

## 6. Boundary conditions and falsification tests

This result remains **finite-section and scalar**. It does not show that the constant mode is invariant under the full boundary DtN/Schur problem, that the physical mixed forcing factors through `D_N`, or that the nonconstant `P/H` reassembly is bounded on any of the weighted spaces above.

The weights can also become very small deep in the flute. Therefore a bounded `\ell^1(d)` or `\ell^2(d)` response can hide large pointwise amplitudes where Robin killing is weak. Equations (1)--(2) do not imply PF-303's `\ell^\infty` bound, a physical `H^{1/2}` estimate, compactness, or vanishing PF-290 shorting deficit without an additional synthesis/reassembly estimate. This weakness is structural, not a proof artifact.

There is no arithmetic discrimination in `P_N`: any finite positive conductance network with positive diagonal killing has the same stochasticization. Shuffling or replacing the prime pant data while preserving positivity leaves the argument intact. Any RH-relevant content must enter through the actual prime-dependent source extraction, nonconstant-mode reassembly, or the observable tested after the scalar response.

The decisive next audit is therefore no longer only the pointwise PF-303 test. Derive the true finite `P/H` source/reassembly map and determine the strongest natural exponent `p` for which both sides of

\[
\|G_Nf\|_{\ell^p(d)}
\le
\|D_N^{-1}f\|_{\ell^p(d)}
\]

can be connected uniformly to the PF-296 source coefficient budget and the PF-292/PF-290 physical response norm. If no such connection survives nonconstant reassembly, the reversible scalar Markov structure is only a calibration invariant; if one does, the need for a uniform scalar spectral gap is removed at that norm level.
