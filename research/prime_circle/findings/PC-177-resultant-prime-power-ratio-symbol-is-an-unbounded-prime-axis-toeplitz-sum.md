# PC-177 — resultant prime-power ratio symbol is an unbounded prime-axis Toeplitz sum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the most canonical sparse-rational-symbol escape left by PC-175/PC-176. The exact common-anchor and pairwise-shell resultant identities do canonically select a multiplicative-ratio symbol supported only on prime-power jumps, so this is not a smooth ratio profile inserted by hand. However, the raw symbol does not even define a bounded operator on the PC-174 normalized `ell^2(N)` space. Its simplest valuation-length damping becomes bounded only for exponent `sigma>1`, where it decomposes into independent one-prime Toeplitz chains, has one interval of continuous spectrum, and its exact norm is the classical logarithmic derivative `-2 zeta'(sigma)/zeta(sigma)`. Thus retaining the full sparse prime-power interaction graph before scalar Dirichlet evaluation still does not produce an RH spectral mechanism in the fixed bounded weak-refinement class.

PC-175 left open arithmetically sparse ratio symbols because its zero-Euclidean-mesh theorem only kills ordinary continuous ratio profiles. PC-176 then closed the first denominator-decaying repair, the symmetric valuation power law, by identifying it with the classical GCD/Poisson operator. The most immediate remaining test is therefore not another chosen sparse support: PC-001 and PC-002 already supply one exactly.

## 1. Prime-Circle resultants canonically select the prime-power ratio graph

For `q in Q_{>0}` define the inversion-symmetric prime-power von Mangoldt symbol

\[
\Lambda_\times(q)
=
\begin{cases}
\log p,&q=p^k\text{ or }q=p^{-k},\quad p\text{ prime},\ k\ge1,\\
0,&\text{otherwise}.
\end{cases}
\tag{1}
\]

In particular `Lambda_x(1)=0`. This symbol is already forced by persisted Prime-Circle geometry.

PC-001 gives at the common anchor

\[
\log|\Phi_n(1)|=\Lambda(n),
\tag{2}
\]

while PC-002 gives for distinct primitive shells, whenever `m<n`,

\[
\frac{1}{\varphi(m)}
\log|\operatorname{Res}(\Phi_m,\Phi_n)|
=
\begin{cases}
\log p,&n/m=p^k,\\
0,&\text{otherwise}.
\end{cases}
\tag{3}
\]

Consequently the shell-normalized common-anchor/resultant interaction has the exact ratio form

\[
\boxed{
K(m,n)=\Lambda_\times(m/n),
\qquad m,n\ge1.
}
\tag{4}
\]

The index `1` in (4) is the common-anchor vacuum supplied by (2); for `m,n>1`, (4) is precisely the normalized pairwise-shell resultant coupling (3). Thus `K` lies inside the multiplicative-Toeplitz coordinate class of PC-174 and satisfies the zero ordinary-mesh-density requirement of PC-175, but its sparse support is not arbitrary: it is exactly the prime-power support of the cyclotomic resultant theorem.

This is the natural test that PC-002 itself left open when it said that the additional information, if any, would have to live in the interaction operator before scalar Dirichlet compression.

## 2. The raw geometric ratio symbol is not a bounded operator

Let `S_p` denote multiplication of the scale index by `p`,

\[
S_p e_n=e_{pn}
\tag{5}
\]

on `ell^2(N)`. Unique prime factorization identifies

\[
\ell^2(\mathbb N)
\cong
\bigotimes_p^{e_0}\ell^2(\mathbb N_0),
\tag{6}
\]

where `S_p` is the unilateral shift on the `p`-valuation coordinate and the identity on all other coordinates. Equation (4) is therefore the formal prime-axis sum

\[
\boxed{
K
=
\sum_p(\log p)
\sum_{k\ge1}
\left(S_p^k+S_p^{*k}\right).
}
\tag{7}
\]

The failure of boundedness is stronger than a global Euler-product divergence. Already

\[
Ke_1
=
\sum_{p}\sum_{k\ge1}(\log p)e_{p^k},
\tag{8}
\]

so

\[
\|Ke_1\|_2^2
=
\sum_p\sum_{k\ge1}(\log p)^2
=\infty.
\tag{9}
\]

Even one fixed prime axis is unbounded, because its off-diagonal Toeplitz coefficients are the constant sequence `log p`. Hence the exact PC-001/002 sparse symbol is not a continuous first-order weak form in the bounded normalized category classified by PC-174.

This is an important distinction from PC-175. Arithmetic sparsity is necessary to evade its Euclidean mesh obstruction, but it is not sufficient for boundedness. The most intrinsic sparse support available in the line fails the column test maximally.

## 3. Valuation-length damping repairs each prime axis but the global threshold is still `sigma=1`

The simplest repair compatible with the intrinsic valuation length of PC-176 is to damp a jump `q=p^{\pm k}` by `exp(-sigma L(q))=p^{-k sigma}`. Define

\[
\boxed{
K_\sigma(m,n)
=
\Lambda_\times(m/n)
\exp\!\left[-\sigma L(m/n)\right],
\qquad \sigma>0.
}
\tag{10}
\]

This damping is a diagnostic family, not a new claim of geometric canonicity. It tests whether the exact resultant support becomes spectrally interesting under the same multiplicative length already singled out in PC-176.

Put

\[
r_p=p^{-\sigma}.
\tag{11}
\]

Then

\[
K_\sigma
=
\sum_p H_{p,\sigma},
\qquad
H_{p,\sigma}
=(\log p)
\sum_{k\ge1}r_p^k
\left(S_p^k+S_p^{*k}\right).
\tag{12}
\]

On the `p`-valuation half-line, `H_{p,sigma}` is the ordinary scalar Toeplitz operator with real continuous symbol

\[
h_{p,\sigma}(e^{it})
=
2(\log p)\sum_{k\ge1}r_p^k\cos(kt)
=
2(\log p)\operatorname{Re}
\frac{r_pe^{it}}{1-r_pe^{it}}.
\tag{13}
\]

The last expression is monotone in `cos t`, so its exact range is

\[
\boxed{
\operatorname{Spec}(H_{p,\sigma})
=
\left[
-\frac{2(\log p)r_p}{1+r_p},
\frac{2(\log p)r_p}{1-r_p}
\right].
}
\tag{14}
\]

For a finite prime set `F`, compress to the subspace generated by integers whose prime factors lie in `F`. The compression of `K_sigma` is the tensor-coordinate sum of the `H_{p,sigma}`, hence

\[
\operatorname{Spec}(K_{\sigma,F})
=
\left[
-2\sum_{p\in F}\frac{(\log p)r_p}{1+r_p},
2\sum_{p\in F}\frac{(\log p)r_p}{1-r_p}
\right].
\tag{15}
\]

Therefore boundedness of the infinite operator forces

\[
\sup_F
\sum_{p\in F}\frac{(\log p)p^{-\sigma}}{1-p^{-\sigma}}
<\infty.
\tag{16}
\]

The sum in (16) is the ordinary Euler expansion

\[
\boxed{
\sum_p\frac{(\log p)p^{-\sigma}}{1-p^{-\sigma}}
=
-\frac{\zeta'(\sigma)}{\zeta(\sigma)},
\qquad \sigma>1.
}
\tag{17}
\]

It diverges as `sigma -> 1+`, and for `sigma<=1` the finite-prime lower bounds in (16) diverge. Conversely, for `sigma>1`, the sum of the local operator norms converges, so (12) converges in operator norm. Hence

\[
\boxed{
K_\sigma\in\mathcal B(\ell^2(\mathbb N))
\iff
\sigma>1.
}
\tag{18}
\]

The same absolute-Euler-product barrier encountered in PC-055 and PC-176 has returned, now for a symbol whose **support itself is forced by the exact resultant geometry**.

## 4. In the bounded region the complete spectrum is one classical interval

For `sigma>1`, the finite-prime sums in (15) converge in norm. Set

\[
A_\sigma
=
\sum_p\frac{(\log p)p^{-\sigma}}{1-p^{-\sigma}}
=
-\frac{\zeta'(\sigma)}{\zeta(\sigma)},
\tag{19}
\]

and

\[
C_\sigma
=
\sum_p\frac{(\log p)p^{-2\sigma}}{1-p^{-2\sigma}}
=
-\frac{\zeta'(2\sigma)}{\zeta(2\sigma)}.
\tag{20}
\]

Since

\[
\frac{r}{1+r}
=
\frac{r}{1-r}-2\frac{r^2}{1-r^2},
\tag{21}
\]

the norm-limit of (15) gives

\[
\boxed{
\operatorname{Spec}(K_\sigma)
=
\left[
-2A_\sigma+4C_\sigma,
2A_\sigma
\right].
}
\tag{22}
\]

In particular

\[
\boxed{
\|K_\sigma\|
=2A_\sigma
=-2\frac{\zeta'(\sigma)}{\zeta(\sigma)},
\qquad \sigma>1.
}
\tag{23}
\]

and `0` lies in the spectrum for every allowed `sigma`. There is no discrete divisor that could select special values of a spectral parameter: the entire self-adjoint spectrum is one interval assembled by Minkowski addition of independent prime-axis intervals.

This is the infinite weak-form analogue of the prime-local separability already exposed for the finite renormalized boundary birth energy in PC-057. The exact cyclotomic prime-power support survives, but it organizes the operator as independent valuation directions rather than a nonseparable collective spectrum.

## 5. Complexifying the damping recovers `-zeta'/zeta` only as a classical multiplier evaluation

One may try to turn the damping exponent into a complex spectral parameter. The analytic half of (12) is

\[
T_s
=
\sum_p(\log p)
\sum_{k\ge1}p^{-ks}S_p^k.
\tag{24}
\]

Under the Hedenmalm--Lindqvist--Seip/Bohr identification, this is multiplication by

\[
\boxed{
a_s(z)
=
\sum_p(\log p)
\frac{p^{-s}z_p}{1-p^{-s}z_p}.
}
\tag{25}
\]

For `Re(s)=sigma>1`, absolute convergence gives

\[
\boxed{
\|T_s\|
=A_\sigma
=-\frac{\zeta'(\sigma)}{\zeta(\sigma)}.
}
\tag{26}
\]

The lower bound is sharp because the independent Bohr phases can align the factors `p^{-it}` simultaneously, prime by prime. At the distinguished torus point `z_p=1`, equation (25) becomes the familiar scalar identity

\[
\boxed{
a_s(1,1,\ldots)
=-\frac{\zeta'(s)}{\zeta(s)}.
}
\tag{27}
\]

But the multiplier exists boundedly only in `Re(s)>1`. Meromorphically continuing the scalar right-hand side of (27) across `Re(s)=1` does not continue the bounded Prime-Circle operator: the finite-prime compressions already force the norm to diverge at the boundary. Thus zeta zeros seen after analytic continuation belong to the classical scalar logarithmic derivative, not to a Hilbert--Pólya spectrum generated by (4).

This is exactly the distinction required by the research mandate: recovering `-zeta'/zeta` is not progress by itself, even when the recovery starts from an intrinsic geometric interaction graph.

## 6. Prior art and novelty audit

No historical novelty is claimed for any ambient ingredient. Apostol's cyclotomic resultant theorem, already anchored in `research/prime_circle/SOURCES.md`, supplies the prime-power support in (3). The Dirichlet identity (17) is the classical von Mangoldt logarithmic derivative already recorded with PC-001. Hedenmalm--Lindqvist--Seip provide the Hardy--Dirichlet/infinite-polydisc model; Hilberdink and Guo--Yan place multiplicative ratio matrices and infinite-polydisc Toeplitz operators in the established operator-theoretic setting used by PC-174.

Targeted literature searches around von-Mangoldt multiplicative-Toeplitz matrices, prime-power ratio kernels, divisibility adjacency and infinite-polydisc prime shifts did not locate this exact line-specific compression as a named theorem. That absence is not used as a novelty claim. The durable result is narrower: **the particular sparse symbol selected jointly by PC-001 and PC-002, when inserted into the exact PC-174 weak-refinement class, is unbounded; its simplest intrinsic-length damping exists only in the absolute-convergence half-plane and has the explicit interval spectrum (22).**

The result also explains why merely noticing that the resultant graph is prime-selective is insufficient. Prime selectivity here is coordinate support in the free commutative valuation lattice, and the Bohr lift separates those coordinates completely.

## 7. Exact boundary and falsification tests

The negative result concerns the shell-normalized scalar common-anchor/resultant interaction (4) and its uniform valuation-length power damping (10). It does **not** collapse the full vertexwise resultant Hessian, chord blocks, shell-dependent families, nonlinear tensors, multioperator couplings, or growing-level constructions before shell scalarization. It also does not exclude an unbounded normalized form equipped with a separately geometry-derived self-adjoint domain; PC-174 deliberately classified continuous first-order forms, and (9) says only that the raw resultant ratio symbol lies outside that bounded category.

Prime-dependent anisotropic damping also remains logically possible, but it faces the same novelty gate as PC-176: if the weights merely produce independent one-prime Toeplitz chains, the construction remains prime-separable and any extra decay must be justified geometrically rather than selected to restore boundedness. A surviving fixed weak-form mechanism must create genuine coupling between valuation directions or otherwise leave the one-symbol PC-174 setting.

The claims are directly falsifiable. A counterexample to (9) would require the exact PC-001/002 column to be square summable. A counterexample to (18) would require bounded finite-prime compressions while their upper spectral endpoint in (15) diverges. A counterexample to (22) would have to break the exact tensor-coordinate decomposition (6)/(12) or the one-variable Toeplitz range (14).

## 8. Consequence for the Prime-Circle/RH search

PC-175 left two broad fixed-symbol possibilities: denominator-decaying arithmetic symbols and genuinely sparse rational support. PC-176 closed the canonical symmetric decay. This finding closes the **canonical sparse support actually furnished by Prime-Circle resultants**:

\[
\boxed{
\text{common-anchor + shell resultants}
\longrightarrow
\Lambda_\times(m/n)
\longrightarrow
\text{independent prime-axis Toeplitz chains}.
}
\]

Without damping the operator is not bounded. With the simplest valuation-length damping it is bounded exactly for `sigma>1`, where its norm is the classical `-2 zeta'/zeta` value and its spectrum is a featureless interval containing zero. The sparse resultant graph therefore retains literal prime-power provenance, but not the nonseparable spectral structure required for a new route to the functional equation, zeta zeros, or the critical line.
