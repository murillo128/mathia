# PC-292 — mesoscopic resonance threshold is operator-norm sharp

**Status:** `EXACT-DERIVED` + `DECISIVE-BOUNDARY` + `NEGATIVE/OBSTRUCTION` for the mesoscopic residue-band frontier left open by PC-291.

PC-291 proves that for the exact PC-283 boundary-log finite section, a residue band of width

\[
T=o\!\left(\frac{N}{\log q}\right),\qquad N\asymp\sqrt q,
\]

is uniformly invisible after the natural `1/N` normalization. That estimate leaves open whether the scale `N/\log q` is merely an artifact of the Schur bound or a genuine amplitude threshold.

It is genuine. In the intrinsic same-source configuration `p=r=1`, the PC-291 upper bound is asymptotically attained. More precisely, let

\[
H_B=\{-B,\ldots,B\},\qquad N=2B+1,
\]

with `N/\sqrt q\to\gamma\in(0,\infty)` along odd primes `q`, and use the PC-291 kernel

\[
k_q(0)=-\log q,
\qquad
k_q(t)=\log\!\left(2\sin\frac{\pi |t|_q}{q}\right)
\quad(t\ne0).
\]

For fixed `\alpha>0`, put

\[
T_q=\left\lfloor\frac{\alpha N}{\log q}\right\rfloor
\]

and retain only residues `|h+k|_q\le T_q`. Then

\[
\boxed{
\left\|\frac{K_{q,B}^{1,1,\le T_q}}{N}\right\|_{\rm op}
\longrightarrow \alpha.
}
\tag{1}
\]

Thus the sufficient invisibility range in PC-291 is sharp in order: a band of width comparable to `N/\log q` already carries an order-one normalized operator norm. However, the first order-one contribution occurs in the completely universal same-source Hankel geometry. It therefore does **not** by itself supply source-specific arithmetic, a zeta zero condition, or an RH mechanism.

## 1. Same-source residue selectors are anti-diagonals

For `p=r=1`, the residue selector is

\[
Z_a(h,k)=\mathbf 1_{\{h+k\equiv a\pmod q\}}.
\tag{2}
\]

At square-root resolution, `B=O(\sqrt q)` and `T_q=O(\sqrt q/\log q)`, so for all sufficiently large `q`,

\[
2B+T_q<q.
\]

Hence there is no modular wrap in the retained band and (2) is simply

\[
Z_a(h,k)=\mathbf 1_{\{h+k=a\}}.
\tag{3}
\]

For `|a|\le T_q< N`, this anti-diagonal contains exactly

\[
M(a)=N-|a|
\tag{4}
\]

entries. In particular `Z_0` is the full reversal permutation on the window, not merely a sparse collision.

Write

\[
w_q(0)=\log q,
\qquad
w_q(a)=-k_q(a)>0
\]

on the retained band. Then

\[
A_q:=-K_{q,B}^{1,1,\le T_q}
=
\sum_{|a|\le T_q} w_q(a)Z_a
\tag{5}
\]

is a real symmetric entrywise-nonnegative Hankel matrix. Therefore its operator norm equals its Perron eigenvalue.

## 2. The all-ones vector asymptotically saturates the Schur bound

Let `u=N^{-1/2}(1,\ldots,1)^T`. Equations (4)--(5) give the exact Rayleigh quotient

\[
\left\langle u,\frac{A_q}{N}u\right\rangle
=
\frac1N\left[
\log q
+2\sum_{a=1}^{T_q}w_q(a)\left(1-\frac aN\right)
\right].
\tag{6}
\]

On the other hand, the PC-291 Schur estimate gives

\[
\left\|\frac{A_q}{N}\right\|_{\rm op}
\le
\frac1N\left[
\log q+2\sum_{a=1}^{T_q}w_q(a)
\right].
\tag{7}
\]

Because `T_q/q\to0`, uniformly for `1\le a\le T_q`,

\[
w_q(a)
=
\log\frac qa-\log(2\pi)+o(1).
\tag{8}
\]

Stirling's formula therefore yields

\[
\sum_{a=1}^{T_q}w_q(a)
=
T_q\log\frac{q}{T_q}+O(T_q).
\tag{9}
\]

Since `N\asymp\sqrt q`,

\[
\frac{\log(q/T_q)}{\log q}\longrightarrow\frac12,
\qquad
\frac{T_q}{N}\sim\frac{\alpha}{\log q},
\tag{10}
\]

and hence

\[
\frac1N\left[
\log q+2\sum_{a=1}^{T_q}w_q(a)
\right]
\longrightarrow\alpha.
\tag{11}
\]

The boundary loss in the Rayleigh quotient is negligible:

\[
0\le
\frac{2}{N^2}\sum_{a=1}^{T_q}a\,w_q(a)
\le
\frac{2T_q}{N^2}\sum_{a=1}^{T_q}w_q(a)
=O\!\left(\frac1{\log q}\right).
\tag{12}
\]

Thus (6) has the same limit `\alpha` as the upper bound (7), proving (1).

More generally, for any fixed `0<\eta<1` and `1\le T\le\eta N` in the same square-root regime, the same argument gives the order-sharp estimate

\[
\boxed{
\left\|\frac{K_{q,B}^{1,1,\le T}}{N}\right\|_{\rm op}
\asymp
\frac{T\log(q/T)}{N},
}
\tag{13}
\]

with constants uniform away from `T/N=1`.

## 3. What the sharpness does and does not mean

Equation (1) closes the main quantitative ambiguity left by PC-291. The transition near `T\asymp N/\log q` is not caused by slack in the partial-permutation/Schur argument: an intrinsic Prime-Circle configuration actually reaches that scale. Consequently no uniform improvement of PC-291 can make all `T\asymp N/\log q` residue bands spectrally negligible under the same `1/N` normalization.

But the saturating example is the least arithmetic one available. For `p=r=1`, the congruence foliation has become the elementary Hankel family `h+k=a`; the order-one norm comes from accumulating the classical log-sine singularity across `\asymp N/\log q` adjacent anti-diagonals. Nothing in (1) distinguishes prime-source placements, introduces a spectral parameter, produces `s\leftrightarrow1-s`, or singles out the critical line.

The research consequence is therefore restrictive: **mesoscopic size alone is not evidence for a source-specific critical mechanism.** Any attempt to use the newly non-negligible band must first remove or quotient this universal same-source contribution and then show that a cross-source remainder retains order-one information that survives the existing classical reductions.

## 4. Prior-art and novelty audit

No new general theorem about Hankel, Toeplitz, or Fisher--Hartwig operators is claimed. Finite-section Toeplitz/Hankel theory and spectral-norm asymptotics for singular symbols are classical subjects; targeted checks included Böttcher--Silbermann finite-section theory and Böttcher--Virtanen norm asymptotics for Fisher--Hartwig symbols. The log-sine singularity itself is already classicalized inside Prime Circle by PC-283.

The project-local contribution is narrower: PC-291 produced a line-specific upper threshold from the exact residue-selector decomposition, and (1) proves that this threshold is attained inside the same exact geometry. The proof needs only the explicit anti-diagonal count, Perron/Schur bounds, the elementary small-angle log-sine asymptotic, and Stirling. No external novelty claim is needed, so `SOURCES.md` is unchanged.

## 5. Boundary and next discriminator

This finding does not show that every source pair has an order-one band at `T\asymp N/\log q`, nor that the mesoscopic band is spectrally universal after subtracting the same-source baseline. Those are now the meaningful questions. A surviving Prime-Circle mechanism would need a source-dependent cross-configuration effect of comparable size that cannot be reduced to the universal Hankel accumulation above.

What is now ruled out is the weaker interpretation of the PC-291 frontier: **`N/\log q` is not merely a proof artifact. It is a real operator-norm transition, but its first explicit realization is classical and source-blind rather than an RH carrier.**