# PC-298 — quantitative square-zero approximation reaches shrinking pseudospectral scales

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL-OBSTRUCTION` + `DECISIVE-BOUNDARY` for the shrinking-`epsilon` pseudospectral escape left open by PC-297.

PC-297 proves that every fixed positive pseudospectral scale of the diffuse one-profile boundary-log finite section converges to the same square-zero disk for the prime source and matched diffuse controls. Its proof deliberately uses a diagonal compactness choice and therefore leaves all scales `epsilon=epsilon_q -> 0` open.

That boundary can be made quantitative. The exact digamma multiplier from PC-283 has a uniform `1/j` bound over the whole finite Fourier circle, while the PC-295/296 same-side and cross-Gram estimates remain explicit when the low-mode cutoff grows. Combining those two facts gives an operator-norm distance to the square-zero class with an explicit vanishing rate. Consequently the complete pseudospectrum remains source-universal not only at fixed `epsilon`, but at every shrinking scale above that rate.

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
\]

For source residues `p,r`, write

\[
T_{q,B}^{p,r}(h,k)=\frac1N k_q(ph+rk),
\qquad h,k\in H_B.
\]

Let `p,r` be independent with law `mu_q`, put

\[
\beta_q=\|\mu_q\|_\infty,
\qquad
\delta_q:=\sqrt{\frac{q\beta_q}{N}},
\]

and assume the same diffuseness regime as PC-295--297,

\[
N\to\infty,
\qquad
\delta_q(\log q)^2\longrightarrow0.
\tag{1}
\]

Define

\[
\boxed{
r_q:=
\delta_q^{1/3}
+\delta_q^{1/2}\log q
+\frac{\log q}{N}.
}
\tag{2}
\]

Then there is an absolute constant `C` and, for every sufficiently large `q`, a random `N x N` matrix `S_q=S_q^{p,r}` such that

\[
\boxed{
S_q^2=0,
\qquad
\|S_q\|=\sigma_q,
\qquad
\mathbb E\|T_{q,B}^{p,r}-S_q\|_{\rm op}
\le C r_q,
}
\tag{3}
\]

where the norm is deterministic and satisfies

\[
\boxed{
\sigma_q=\frac12+O(q^{-3}).
}
\tag{4}
\]

In particular `r_q -> 0` under (1), but unlike PC-297 the approximation now carries an explicit scale.

For

\[
g(r)=\frac{\sqrt{\frac14+4r^2}-\frac12}{2},
\]

(3)--(4) imply the quantitative minimum-singular-value law

\[
\boxed{
\mathbb E\sup_{z\in\mathbb C}
\left|
\sigma_{\min}(zI-T_{q,B}^{p,r})-g(|z|)
\right|
\le C r_q.
}
\tag{5}
\]

Therefore, if `epsilon_q -> 0` and

\[
\boxed{
\frac{r_q}{\epsilon_q}\longrightarrow0,
}
\tag{6}
\]

then, with

\[
R_q:=\sqrt{\epsilon_q\left(\epsilon_q+\frac12\right)},
\]

the shrinking pseudospectrum satisfies

\[
\boxed{
\frac{
 d_H\!\left(
 \Lambda_{\epsilon_q}(T_{q,B}^{p,r}),
 \{z:|z|\le R_q\}
 \right)
}{R_q}
\longrightarrow0
\quad\text{in probability}.
}
\tag{7}
\]

Equivalently,

\[
\boxed{
\epsilon_q^{-1/2}\Lambda_{\epsilon_q}(T_{q,B}^{p,r})
\longrightarrow
\{z:|z|\le2^{-1/2}\}
}
\tag{8}
\]

in Hausdorff distance in probability. Thus all shrinking scales satisfying (6) retain the same universal square-zero geometry as the fixed scales of PC-297.

## 1. The exact digamma multiplier has a uniform finite-`q` Green tail

Use the PC-295 normalization

\[
a_q(m)=\frac{\widehat k_q(m)}q.
\]

PC-283 gives, for `1<=j<=q-1`,

\[
a_q(j)
=\frac1q\left[
\gamma+\frac12\left(
\psi\left(\frac jq\right)
+\psi\left(1-\frac jq\right)
\right)
\right].
\tag{9}
\]

For `0<x<=1/2`, the classical digamma partial-fraction series gives

\[
\psi(x)+\gamma
=-\frac1x+\sum_{n\ge1}\frac{x}{n(n+x)},
\]

and, after applying the same series to `psi(1-x)`,

\[
\psi(1-x)+\gamma
=-\sum_{n\ge1}\frac{x}{n(n-x)}.
\]

Averaging therefore yields the exact identity

\[
\boxed{
\frac12\bigl(\psi(x)+\psi(1-x)+2\gamma\bigr)
=-\frac1{2x}
-x^2\sum_{n\ge1}\frac1{n(n^2-x^2)}.
}
\tag{10}
\]

Hence, for `1<=j<q/2`,

\[
\boxed{
a_q(j)
=-\frac1{2j}
-\frac{j^2}{q^3}
\sum_{n\ge1}
\frac1{n\left(n^2-(j/q)^2\right)}.
}
\tag{11}
\]

Since `j/q<=1/2`,

\[
0<
\sum_{n\ge1}
\frac1{n\left(n^2-(j/q)^2\right)}
\le\frac43\zeta(3).
\tag{12}
\]

Using `j^3/q^3<=1/8`, (11)--(12) give the uniform bound

\[
\boxed{
|a_q(\pm j)|
\le\frac{C_0}{j},
\qquad
C_0:=\frac12+\frac{\zeta(3)}6<1.
}
\tag{13}
\]

This upgrades the fixed-mode asymptotic used in PC-295 to a finite-`q` estimate uniform over the complete half-circle. In particular, for

\[
S_M=\{\pm1,\ldots,\pm M\},
\qquad M<q/2,
\]

\[
\boxed{
\sum_{m\notin S_M}|a_q(m)|^2
\le
2C_0^2\sum_{j>M}\frac1{j^2}
\le\frac{2C_0^2}{M}.
}
\tag{14}
\]

Equation (11) also gives

\[
|a_q(1)|
=\frac12+O(q^{-3}).
\tag{15}
\]

For `j>=2`, (13) gives `|a_q(j)|<=C_0/2<1/2`, while (11) gives `|a_q(1)|>1/2`. Thus the largest multiplier in every nonempty low block is exactly

\[
\boxed{\sigma_q=|a_q(1)|.}
\tag{16}
\]

## 2. The growing low block is quantitatively close to square-zero

Write the exact PC-295 rank-one expansion

\[
T_{q,B}^{p,r}
=\sum_{m\bmod q}a_q(m)x_{m,p}z_{m,r}^*.
\tag{17}
\]

For `d=2M`, let `X` and `Z` be the `N x d` matrices whose columns are the modes indexed by `S_M`, and put

\[
A_{q,M}=XDZ^*,
\qquad
D=\operatorname{diag}_{m\in S_M}a_q(m).
\]

The PC-295 same-side estimates and the PC-296 cross-Gram estimate remain explicit before fixing `M`:

\[
\mathbb E\|X^*X-I\|_F^2
\le d(d-1)\delta_q^2,
\]

\[
\mathbb E\|Z^*Z-I\|_F^2
\le d(d-1)\delta_q^2,
\]

and

\[
\mathbb E\|Z^*X\|_F^2
\le d^2\delta_q^2.
\tag{18}
\]

Instead of orthogonalizing the two frames separately as in PC-297, concatenate them:

\[
Y=[X\ Z],
\qquad
G=Y^*Y.
\]

Then (18) gives

\[
\boxed{
\mathbb E\|G-I\|_F^2
\le4d^2\delta_q^2
=16M^2\delta_q^2.
}
\tag{19}
\]

On the good event `||G-I||op<=1/2`, set

\[
Q=YG^{-1/2}=[U\ W].
\]

Then `Q^*Q=I`, so

\[
U^*U=W^*W=I,
\qquad
W^*U=0.
\]

Define

\[
S_{q,M}=UDW^*.
\tag{20}
\]

It satisfies exactly

\[
S_{q,M}^2=0,
\qquad
\|S_{q,M}\|=\|D\|=\sigma_q.
\tag{21}
\]

Functional calculus on the interval `[1/2,3/2]` gives

\[
\|Y-Q\|_{\rm op}
\le C\|G-I\|_{\rm op},
\]

and therefore

\[
\|A_{q,M}-S_{q,M}\|_{\rm op}
\le C\|G-I\|_F
\]

on the good event. From (19),

\[
\mathbb E\left[
\|A_{q,M}-S_{q,M}\|_{\rm op};\,G\text{ good}
\right]
\le C M\delta_q.
\tag{22}
\]

Markov applied to (19) gives

\[
\mathbb P(G\text{ bad})
\le C M^2\delta_q^2.
\tag{23}
\]

On the bad event choose any fixed rank-one square-zero matrix of norm `sigma_q`. By (13),

\[
\|A_{q,M}\|
\le\sum_{m\in S_M}|a_q(m)|
\le C\log(M+1).
\]

Thus the bad event contributes at most

\[
C M^2\delta_q^2\log(M+1).
\]

Altogether there exists a square-zero `S_{q,M}` of deterministic norm `sigma_q` with

\[
\boxed{
\mathbb E\|A_{q,M}-S_{q,M}\|_{\rm op}
\le
C\left[
M\delta_q
+M^2\delta_q^2\log(M+1)
\right].
}
\tag{24}
\]

This is the quantitative replacement for the fixed-`M` compactness step in PC-297.

## 3. The complete Fourier tail has a quantitative operator bound

Let

\[
R_{q,M}=T_{q,B}^{p,r}-A_{q,M}.
\]

PC-295 proves the exact comparison

\[
\left|
\mathbb E_{\mu_q}\|R_{q,M}\|_F^2
-
\mathbb E_{u_q}\|R_{q,M}\|_F^2
\right|
\le2\delta_q(\log q)^2,
\tag{25}
\]

where `u_q` is the uniform source. For the uniform source,

\[
\mathbb E_{u_q}\|R_{q,M}\|_F^2
\le
\sum_{m\notin S_M}|a_q(m)|^2
+\frac{(\log q)^2}{N^2}.
\]

Using (14) and Jensen,

\[
\boxed{
\mathbb E\|R_{q,M}\|_{\rm op}
\le
C M^{-1/2}
+C\delta_q^{1/2}\log q
+\frac{\log q}{N}.
}
\tag{26}
\]

The second term is the price of replacing the uniform source by an arbitrary diffuse source under the same maximal-atom control as PC-295--297.

## 4. Optimizing the cutoff gives the explicit square-zero rate

A probability measure on `q` residues has `beta_q>=1/q`, hence

\[
\delta_q^2=\frac{q\beta_q}{N}\ge\frac1N.
\]

Under (1), `delta_q -> 0`. Choose

\[
M=\left\lfloor\delta_q^{-2/3}\right\rfloor.
\tag{27}
\]

Then `M -> infinity`, while `M=O(N^{1/3})`, so `4M<=N` and `M<q/2` for all sufficiently large `q`. The two balancing terms satisfy

\[
M\delta_q=O(\delta_q^{1/3}),
\qquad
M^{-1/2}=O(\delta_q^{1/3}),
\]

and

\[
M^2\delta_q^2\log(M+1)
=O\!\left(
\delta_q^{2/3}\log\frac1{\delta_q}
\right)
=o(\delta_q^{1/3}).
\]

Combining (24) and (26) proves (3) with `r_q` from (2). Condition (1) gives

\[
\delta_q^{1/2}\log q
=\sqrt{\delta_q(\log q)^2}
\longrightarrow0,
\]

so `r_q -> 0` as claimed.

The exponent `1/3` is a consequence of balancing the explicit growing-frame error `M delta_q` against the universal Green tail `M^{-1/2}`. It is **not claimed sharp**. Improving either estimate could lower the guaranteed universal scale.

## 5. Shrinking pseudospectra remain universal above `r_q`

For every exact square-zero matrix `S` of norm `sigma`, PC-297 gives

\[
\sigma_{\min}(zI-S)
=g_\sigma(|z|)
:=
\frac{\sqrt{\sigma^2+4|z|^2}-\sigma}{2}.
\tag{28}
\]

The smallest singular value is 1-Lipschitz in the matrix argument, while `g_sigma` is uniformly `1/2`-Lipschitz in `sigma`. Equations (3)--(4) therefore imply (5).

Let

\[
\Delta_q(T)
:=\sup_z
\left|
\sigma_{\min}(zI-T)-g(|z|)
\right|.
\]

From (5), `E Delta_q <= C r_q`. If (6) holds, Markov gives

\[
\frac{\Delta_q(T)}{\epsilon_q}
\longrightarrow0
\quad\text{in probability}.
\tag{29}
\]

On the event `Delta_q<epsilon_q`, the pseudospectrum is deterministically sandwiched between two square-zero disks:

\[
\left\{g(|z|)\le\epsilon_q-\Delta_q\right\}
\subseteq
\Lambda_{\epsilon_q}(T)
\subseteq
\left\{g(|z|)\le\epsilon_q+\Delta_q\right\}.
\tag{30}
\]

Their radii are

\[
R(\eta)=\sqrt{\eta(\eta+1/2)}.
\]

When `Delta_q/epsilon_q -> 0`, both `R(epsilon_q+-Delta_q)/R(epsilon_q)` tend to `1`. This proves (7), and (8) follows because

\[
\frac{R_q}{\sqrt{\epsilon_q}}
=\sqrt{\epsilon_q+\frac12}
\longrightarrow\frac1{\sqrt2}.
\]

Thus PC-297's fixed-scale disk is not merely a macroscopic artifact. It persists through a concrete shrinking window whose lower edge is controlled by (2).

## 6. Prime source and matched-control consequence

For the normalized prime source below `q`, the prime number theorem gives

\[
\beta_q\asymp\frac{\log q}{q}.
\]

Hence

\[
\delta_q\asymp\sqrt{\frac{\log q}{N}},
\]

and (2) becomes

\[
\boxed{
r_q
=O\!\left(
\left(\frac{\log q}{N}\right)^{1/6}
+
\frac{(\log q)^{5/4}}{N^{1/4}}
+
\frac{\log q}{N}
\right).
}
\tag{31}
\]

The count-matched Li-grid control of PC-290 has the same maximal-atom order, so exactly the same bound applies to it. Therefore every shrinking scale `epsilon_q` satisfying `epsilon_q >> r_q` has the same rescaled pseudospectral disk for the prime source and for that matched non-prime control.

At the square-root window `N asymp q^{1/2}`,

\[
\boxed{
r_q
=O\!\left(q^{-1/12}(\log q)^{1/6}\right),}
\tag{32}
\]

because the other terms are asymptotically smaller. Consequently

\[
\epsilon_q\gg q^{-1/12}(\log q)^{1/6}
\]

is already too coarse to recover a prime-specific pseudospectral signal from this one-profile diffuse boundary-log matrix.

This is a guaranteed universality range, not a sharp transition. The theorem does not say that source information appears at or below `r_q`; it says only that it cannot appear in the complete pseudospectrum above that scale under the stated diffuse product law.

## 7. Prior-art, novelty, and remaining boundary

The abstract ingredients are classical and were already audited in the immediate dependencies. PC-283 identifies the finite log-sine multiplier with the classical digamma transform and cites the standard digamma partial-fraction machinery. PC-297 audits square-zero operators and pseudospectra against the standard nonnormal-operator literature. The additional steps here are elementary quantitative uses of those same ingredients: one finite-`q` digamma bound, a polar orthogonalization of the concatenated Fourier frame, and the 1-Lipschitz perturbation bound for minimum singular values.

Targeted searches against shrinking pseudospectra, pseudospectral perturbation continuity, square-zero/nilpotent disks, and conditioning of partial/nonuniform Fourier frames found the expected general theories but no result that supplies the Prime-Circle-specific rate (2) from the simultaneous source-dilated same-side/cross-Gram estimates and the exact Green tail. Absence of such a packaged theorem is not used as evidence of mathematical novelty. No novelty is claimed for digamma series, polar decomposition, Fourier-frame conditioning, or pseudospectral perturbation theory.

The durable project-local delta is the explicit quantitative boundary: **the same mechanism that classicalizes fixed-scale pseudospectra remains valid throughout every shrinking scale larger than `r_q`, and at square-root resolution this includes all `epsilon_q` asymptotically larger than `q^{-1/12}(log q)^{1/6}`.** This closes a substantial part of the shrinking-scale escape that PC-297 explicitly left open.

No new external literature dependency is load-bearing beyond the sources already audited inside PC-283 and PC-297, so `SOURCES.md` is unchanged.

What remains genuinely outside the result is now narrower: pseudospectra at `epsilon_q=O(r_q)` or smaller; a sharper rate obtained from source-specific cancellation rather than maximal-atom control; microscopic eigenvalue/eigenvector statistics; exceptional correlated or concentrated source pairs; several profiles retained jointly; source-coupled left/right words before one-profile compression; and genuine cross-level operators. Any claimed prime-specific signal in the one-profile diffuse branch must live below the quantitative stability scale proved here rather than merely below a fixed positive `epsilon`.

## 8. Falsification and audit tests

1. Starting from the exact PC-283 multiplier (9), verify the partial-fraction identity (10). A sign error or a positive correction in (11) invalidates the global tail bound.
2. For every odd prime `q`, check numerically that `j|a_q(j)|<=C_0` for `1<=j<q/2` and that the exact correction in (11) is bounded by `(4/3)zeta(3)j^2/q^3`.
3. Reconstruct the concatenated Gram matrix `G` and verify (19) directly from the PC-295 same-side and PC-296 cross-Gram estimates. The factor grows as `M^2`; replacing it by a fixed-`M` statement is insufficient for this finding.
4. On the good event, verify `Q^*Q=I`, `W^*U=0`, `S^2=0`, and `||S||=sigma_q`. The construction requires `4M<=N`, which follows from (27) only asymptotically.
5. Verify the tail estimate (26) from PC-295's exact source comparison and the new uniform Fourier bound (14). A larger tail at growing `M` would change the optimized exponent.
6. At `M=floor(delta_q^{-2/3})`, check every error term in (24) and (26); the bad-event term must be `o(delta_q^{1/3})` rather than silently discarded.
7. For any proposed shrinking scale satisfying `epsilon_q/r_q -> infinity`, the normalized Hausdorff distance in (7) must vanish in probability. Persistent angular structure or a relative radius defect at such scales would falsify the theorem.
8. Behavior at `epsilon_q=O(r_q)` is explicitly unresolved and is not a counterexample to this result.