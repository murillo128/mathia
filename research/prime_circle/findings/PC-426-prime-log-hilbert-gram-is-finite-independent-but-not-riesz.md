# PC-426 — prime-log Hilbert Gram is finitely independent but never a Riesz family

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE for the attempt to rescue PC-421--PC-425 by turning the full prime-index family of Hilbert--Schmidt commutators into a uniformly conditioned Gram/Riesz or operator-frame spectral system. Every finite prime Gram matrix is positive definite, but the normalized infinite family is neither a Riesz sequence nor a Bessel sequence. No diagonal rescaling can make it a Riesz sequence. The obstruction is clustering of prime logarithms under a continuous unitary translation orbit, and holds unchanged for PC-424's zero-free matched control and for nonprime levels with the same logarithmic clustering.

This does **not** rule out deliberately separated subfamilies, source-forced non-diagonal inter-level metrics, source-sensitive off-diagonal operator couplings, or different renormalized infinite limits. Finite rank, finite determinant positivity, and the nonexistence of uniform Gram bounds must not be conflated.

## 1. Exact source-generated family

Work at a fixed real \(0<\sigma<1\) in the Hilbert space
\[
\mathcal K=\mathcal S_2(L^2(\mathbb R)).
\]
Let
\[
r(x)=\frac1{e^x-1}-\frac1x,\qquad
b_\sigma(u)=e^{\sigma u}r(e^u),\qquad
B_\sigma=[H,M_{b_\sigma}].
\tag{1}
\]
By PC-421/PC-424, \(b_\sigma\in H^1(\mathbb R)\cap C_0(\mathbb R)\), and \(B_\sigma\in\mathcal K\) is nonzero. Nonzeroness follows directly from the Hilbert-commutator kernel: a vanishing commutator forces \(b_\sigma\) to be almost everywhere constant, but this symbol is nonconstant and vanishes at both infinities.

Let \((\tau_a f)(u)=f(u+a)\). Conjugation
\[
\mathcal T_a B:=\tau_a B\tau_{-a}
\]
is a strongly continuous unitary representation of the additive real line on \(\mathcal K\). Equation (7) of PC-424 gives at prime levels
\[
\boxed{
C_{p,\sigma}=B_\sigma-p^{1-\sigma}\mathcal T_{\log p}B_\sigma
}\qquad(p\text{ prime}).
\tag{2}
\]
The sign agrees with \(C_{p,\sigma}=-E_{p,\sigma}\) in PC-424.

For any finite set \(F\) of distinct primes define its Gram matrix
\[
G_F(\sigma)=
\bigl(\langle C_{p,\sigma},C_{q,\sigma}\rangle_{\mathcal K}\bigr)_{p,q\in F}.
\tag{3}
\]
The distinction between finite positivity and uniform lower/upper bounds as \(F\) grows is the live question.

## 2. Every finite Gram matrix is strictly positive definite

In Fourier variables the kernel of \(B_\sigma\) is, with the PC-421 normalization,
\[
\widehat B_\sigma(\xi,\eta)=
-\frac{i}{\sqrt{2\pi}}
\bigl(\operatorname{sgn}\xi-\operatorname{sgn}\eta\bigr)
\widehat b_\sigma(\xi-\eta).
\tag{4}
\]
Moreover, conjugation by translation multiplies this kernel by
\[
\widehat{\mathcal T_a B_\sigma}(\xi,\eta)
=e^{ia(\xi-\eta)}\widehat B_\sigma(\xi,\eta).
\tag{5}
\]
The kernel is nonzero on a set of positive measure with \(\xi>0>\eta\). Consequently, the set of differences \(t=\xi-\eta>0\) on which \(\widehat b_\sigma(t)\ne0\) has positive one-dimensional measure.

Suppose \(\sum_{p\in F}c_pC_{p,\sigma}=0\). On the nonzero part of the Fourier kernel, (2)--(5) give
\[
\boxed{
Q(t)=\sum_{p\in F}c_p
-\sum_{p\in F}c_p p^{1-\sigma}e^{it\log p}=0
}
\tag{6}
\]
for almost every \(t\) in that positive-measure set. The finite exponential polynomial \(Q\) is entire in \(t\); zeros having a finite accumulation point force it to vanish identically. Because \(0,\log p\) for \(p\in F\) are pairwise distinct, independence of the corresponding exponentials forces \(c_pp^{1-\sigma}=0\) for every \(p\), hence every \(c_p=0\).

Therefore
\[
\boxed{\quad G_F(\sigma)\succ0
\quad\text{for every finite set of distinct primes }F.\quad}
\tag{7}
\]
This is strict finite linear independence, not a uniform Riesz estimate. The argument uses only a nonzero Hilbert--Schmidt seed and distinct translation parameters; it does not use a zeta-zero theorem or even primality of the labels.

## 3. Adjacent prime logarithms force normalized vectors to coalesce

Write \(\beta_\sigma=\|B_\sigma\|_{\mathcal K}>0\), \(r_p=p^{1-\sigma}\), and normalize
\[
U_p=\frac{C_{p,\sigma}}{\|C_{p,\sigma}\|_{\mathcal K}},
\qquad
V_p=-\frac{\mathcal T_{\log p}B_\sigma}{\beta_\sigma}.
\tag{8}
\]
Both are unit vectors. Equation (2), the reverse triangle inequality, and \(r_p>1\) give
\[
\beta_\sigma(r_p-1)\le\|C_{p,\sigma}\|_{\mathcal K}
\le\beta_\sigma(r_p+1),
\]
and the elementary normalization estimate gives
\[
\boxed{\|U_p-V_p\|_{\mathcal K}\le\frac{2}{r_p-1}\longrightarrow0.}
\tag{9}
\]
For a fixed positive integer \(m\), the prime number theorem implies, as \(j\to\infty\),
\[
\boxed{\max_{0\le a<m}|\log p_{j+a}-\log p_j|\longrightarrow0,}
\tag{10}
\]
where \(p_j\) is the \(j\)-th prime. This uses only \(p_{j+1}/p_j\to1\), not a delicate prime-gap conjecture.

By strong continuity of \(\mathcal T\), invariance of the Hilbert--Schmidt norm under conjugation, and (9),
\[
\max_{0\le a<m}
\left\|U_{p_{j+a}}+
\frac{\mathcal T_{\log p_j}B_\sigma}{\beta_\sigma}\right\|_{\mathcal K}
\longrightarrow0.
\tag{11}
\]
Thus for every fixed block size \(m\), the normalized prime-block Gram matrix satisfies
\[
\boxed{
\bigl(\langle U_{p_{j+a}},U_{p_{j+b}}\rangle\bigr)_
{0\le a,b<m}
\longrightarrow J_m
}
\tag{12}
\]
in matrix/operator norm; \(J_m\) is the all-ones matrix. In particular its eigenvalues converge, with multiplicity, to \(m,0,\ldots,0\).

## 4. No uniform Riesz bounds, no normalized Bessel bound, no diagonal Riesz repair

Every fixed block in (12) remains positive definite by (7). Nevertheless, for \(m=2\) its least eigenvalue tends to zero. There is **no positive Riesz lower bound** uniform over all finite sets of primes:
\[
\not\exists A>0:\quad
A\sum_p|a_p|^2\le
\left\|\sum_p a_p U_p\right\|_{\mathcal K}^2
\quad\text{for every finitely supported }a.
\tag{13}
\]
For the upper bound, choose \(m\) arbitrarily large and then \(j\) sufficiently large in (12). Its largest eigenvalue is arbitrarily close to \(m\). Hence the normalized family \((U_p)_p\) is **not Bessel** either:
\[
\not\exists B<\infty:\quad
\left\|\sum_p a_p U_p\right\|_{\mathcal K}^2
\le B\sum_p|a_p|^2
\quad\text{for all finitely supported }a.
\tag{14}
\]

No choice of nonzero scalar weights \(w_p\), including arbitrary phases, can turn \((w_p C_{p,\sigma})_p\) into a Riesz sequence. Indeed Riesz bounds \(0<A\le B<\infty\) would force
\[
A\le \|w_pC_{p,\sigma}\|_{\mathcal K}^2\le B
\]
for each \(p\). Dividing each element by its norm would then preserve Riesz bounds up to the constant factor \(A/B\), whereas its normalized Gram has exactly the same off-diagonal correlation moduli as (12), irrespective of phase. The two-vector minimum eigenvalue tends to zero, a contradiction.

Equivalently, finite normalized Gram matrices can have arbitrarily bad condition numbers despite being strictly positive definite. The result is a **failure of the uniform frame/Riesz architecture**, not a claim that every finite determinant vanishes. Degenerate weights tending to zero may enforce some upper estimates, but cannot provide the positive diagonal lower bounds required of a Riesz family.

## 5. Matched zero-free and non-arithmetic controls

Replace \(r,b_\sigma,B_\sigma\) everywhere by the explicit zero-free matched seed \(r_0,\widetilde b_\sigma,\widetilde B_\sigma\) of PC-424. That seed also defines a nonzero Hilbert--Schmidt commutator, a strongly continuous translation orbit, and the exact prime-shell formula
\[
\widetilde C_{p,\sigma}=
\widetilde B_\sigma-
p^{1-\sigma}\mathcal T_{\log p}\widetilde B_\sigma.
\tag{15}
\]
All proofs (4)--(14) hold verbatim with tildes, although its Mellin transform has **no zeros** in the open critical strip.

An even simpler non-arithmetic control replaces the prime indices by any distinct increasing real labels \(x_j\to\infty\) with \(x_{j+1}/x_j\to1\), using
\[
C_{x_j,\sigma}=B_\sigma-x_j^{1-\sigma}\mathcal T_{\log x_j}B_\sigma.
\tag{16}
\]
For example \(x_j=j+1\) has the same finite-independence and infinite-clustering conclusions. Thus neither the finite positive determinants nor the collapsing normalized Gram blocks are selected by cyclotomic primality or by the zeta zero set.

## 6. Prior art, falsification, and exact boundary

The Hilbert--Schmidt commutator and source kernel come from the classical singular-integral/Hankel framework audited in PC-421 and PC-424. Finite independence of distinct translates here is the elementary exponential-polynomial uniqueness argument in (6). The failure of Riesz/Bessel bounds for a translation system with locally clustering parameters belongs to standard irregular-frame theory: O. Christensen, *An Introduction to Frames and Riesz Bases*, 2nd ed., Birkhäuser (2016), DOI 10.1007/978-3-319-25613-9, especially the chapters on Riesz sequences and frames of translates; P. Balazs and S. Heineken, *An Operator Based Approach to Irregular Frames of Translates*, *Mathematics* 7 (2019), 449, DOI 10.3390/math7050449. Those references provide nearby general frame theory, not a claim that they prove this particular Prime-Circle Hilbert--Schmidt formula. The number-theoretic input (10) follows from the classical prime number theorem.

No novelty is asserted for the abstract facts about translates or for the prime number theorem. The project-specific consequence is that **the exact source-generated PC-424 family has positive finite prime Gram determinants but no infinite Riesz stabilization by diagonal weights**, and the zero-free control reproduces that failure. This closes an exact prime-index Gram/Riesz escape after PC-425 without claiming to classify other completions.

Load-bearing tests are: (2)'s scaling/sign, (4)--(6)'s translation multiplier and exponential-polynomial uniqueness, (9)'s unitary-normalization estimate, (10)'s log-prime clustering, and (12)'s Gram limit. A violation at any of these points would invalidate the asserted obstruction.

Not ruled out are a prescribed log-separated subsequence, intrinsically **non-diagonal** cross-level metrics, source-dependent angular/old--new couplings before scalar Mellinization, or a renormalized large-block spectral statistic supplied with its own topology and matched control. Such a proposed structure must be derived from the original roots-of-unity geometry and must distinguish its outcome from (15)--(16); simply observing positive finite Gram determinants or inserting a diagonal normalization does not cross the current obstruction.
