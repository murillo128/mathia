# PC-301 — centered-window cyclic carriers are coordinatewise reflection-blind even under arbitrary source coupling

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL-OBSTRUCTION` + `DECISIVE-BOUNDARY` for the correlated/reused-source escape left open by PC-300.

PC-300 closes independently sampled cyclic boundary-log profiles because expectation factorizes their noncommuting loop into powers of one averaged Hankel matrix. It deliberately leaves reused or correlated source variables open, since in that regime the product need not factor through a single average.

There is nevertheless an earlier exact information-loss gate. With the centered window used by PC-296--300, the same-source cross-Gram carrier is already even in each source residue **before any averaging or independence assumption**. Consequently every cyclic word built from those carriers is invariant under an independent reflection of every source coordinate. Arbitrary source correlations can survive, but their coordinatewise reflection-odd content cannot.

Let

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1\le q,
\]

and retain

\[
c_d:=\frac1N\sum_{h\in H_B}e^{2\pi i d h/q},
\qquad
G_s:=Z_s^*X_s,
\qquad
(G_s)_{n,m}=c_{(m+n)s}.
\tag{1}
\]

Because `H_B` is centered,

\[
\boxed{c_{-d}=c_d\in\mathbb R.}
\tag{2}
\]

Hence for every source residue `s`,

\[
\boxed{G_{-s}=G_s.}
\tag{3}
\]

For the PC-300 cyclic profile loop

\[
L_k(p_1,\ldots,p_k)
:=\operatorname{tr}\!\left(
A^{p_1,p_2}A^{p_2,p_3}\cdots A^{p_k,p_1}
\right),
\]

PC-300 gives the exact deterministic reduction

\[
L_k
=\operatorname{tr}\!\left(
D G_{p_2}D G_{p_3}\cdots D G_{p_k}D G_{p_1}
\right).
\tag{4}
\]

Combining (3) and (4), for every sign vector `epsilon in {+1,-1}^k`,

\[
\boxed{
L_k(\epsilon_1p_1,\ldots,\epsilon_kp_k)
=L_k(p_1,\ldots,p_k).
}
\tag{5}
\]

This is pointwise. It does not use independent sampling, a prime-number theorem, an asymptotic limit, a low-density approximation, or commutativity of the `G_s`.

## 1. Arbitrary joint source laws are projected to the sign quotient

Let `nu` be any probability law on `(Z/qZ)^k`; its coordinates may be maximally correlated, conditioned to be distinct, sampled without replacement, deterministically related, or reused. Define its coordinatewise reflection symmetrization

\[
\mathcal S\nu
:=2^{-k}\sum_{\epsilon\in\{\pm1\}^k}
(\epsilon_1,\ldots,\epsilon_k)_*\nu.
\tag{6}
\]

Equation (5) immediately gives

\[
\boxed{
\mathbb E_{\nu}L_k
=
\mathbb E_{\mathcal S\nu}L_k.
}
\tag{7}
\]

Thus the entire correlated cyclic observable factors through

\[
(\mathbb Z/q\mathbb Z)^k
\longrightarrow
\bigl((\mathbb Z/q\mathbb Z)/\{s\sim-s\}\bigr)^k.
\tag{8}
\]

In Fourier language, replacing `nu` by `S nu` removes every joint Fourier component that is odd under a sign reversal in at least one coordinate. Correlations between the surviving unoriented residue classes remain available; (7) does **not** claim that arbitrary correlated laws reduce to the single matrix of PC-300.

The same obstruction applies to any algebraic observable that factors through the collection of centered same-source Gram matrices `G_{p_j}`: products, traces, determinants, resolvents of such finite words, and tensor contractions formed only after the map `p_j -> G_{p_j}` all inherit (3). Changing the contraction after that map cannot reconstruct the discarded orientation.

## 2. Maximal source reuse still cannot restore the missing phase

At the opposite extreme from PC-300 independence, set every source coordinate equal to one residue `s`. Then

\[
L_k(s,\ldots,s)=\operatorname{tr}\!\left((D G_s)^k\right).
\tag{9}
\]

This hierarchy may contain more information than powers of one averaged matrix, but (3) gives

\[
\boxed{
\operatorname{tr}((DG_{-s})^k)
=
\operatorname{tr}((DG_s)^k)
\quad\text{for every }k.
}
\tag{10}
\]

The loss can also be seen directly in the additive Fourier expansion. Writing `m_{k+1}=m_1`,

\[
\operatorname{tr}((DG_s)^k)
=\frac1{N^k}
\sum_{m_1,\ldots,m_k}
\left(\prod_{j=1}^k d_{m_j}\right)
\sum_{h_1,\ldots,h_k\in H_B}
\exp\!\left(
\frac{2\pi i s}{q}
\sum_{j=1}^k(m_j+m_{j+1})h_j
\right).
\tag{11}
\]

Averaging (11) against an arbitrary one-source law `mu` replaces the exponential by `widehat mu(T)`, where

\[
T=\sum_{j=1}^k(m_j+m_{j+1})h_j.
\]

The involution `(h_1,...,h_k)->(-h_1,...,-h_k)` pairs `T` with `-T`, so only

\[
\frac12\bigl(\widehat\mu(T)+\widehat\mu(-T)\bigr)
=\operatorname{Re}\widehat\mu(T)
\tag{12}
\]

survives. Hence even maximal source reuse cannot recover the reflection-odd additive Fourier phase while the centered Gram carrier is kept.

For the prime source this gives an exact matched control: replace the prime-residue law by its reflected law `p -> -p (mod q)`, or independently randomize the sign of each source coordinate in any correlated prime tuple. The oriented joint Fourier data generally changes, but every observable in (4) is unchanged exactly.

## 3. What this does and does not close

PC-300 showed that **independence** destroys relational information by factorization after averaging. PC-301 is orthogonal to that mechanism: it shows that **centered same-source Gram formation** destroys orientation before averaging. Therefore moving from independent to correlated/reused source variables does not by itself repair the reflection-phase loss already visible in PC-300.

This is not a no-go for all correlated profile constructions. A correlated law can still affect the joint distribution of the unoriented classes `{s,-s}`, and growing-depth or cross-level relations among those classes remain outside (7). Nor is phase loss a generic property of higher-order spectral statistics: ordinary bispectral/polyspectral constructions can retain phase. The obstruction here is specifically the even Dirichlet carrier forced by the centered window in (1).

The surviving requirement is consequently sharper. To access orientation-sensitive source information, a construction must break the map `s -> G_s` itself: retain the oriented frames `X_s` and `Z_s` before their centered same-source contraction, use a genuinely asymmetric window/observable justified by the Prime-Circle geometry, introduce a cross-level carrier that is not a function of `G_s`, or identify an RH-relevant mechanism that provably depends only on the sign-quotiented relational data and therefore does not need the lost phase.

## 4. Prior-art and novelty audit

The analytic ingredient behind (2) is classical: a symmetric finite Fourier window is the Dirichlet kernel and is real and even. Higher-order/bispectral signal analysis also makes clear that phase recovery can occur in generic higher-order statistics, so no generic claim that “higher order loses phase” is made here. The load-bearing result is instead the project-local exact placement of the quotient: in this Prime-Circle boundary-log construction, source orientation is erased at `G_s=Z_s^*X_s` before any correlated cyclic statistic can use it.

Accordingly the finding is an exact obstruction/boundary, not a new RH mechanism and not a novelty claim for Dirichlet kernels or higher-order spectra. It closes the specific proposal that arbitrary correlation or complete reuse of source variables, while retaining the centered `G_s` carrier of PC-300, can restore the missing reflection-odd source phase.
