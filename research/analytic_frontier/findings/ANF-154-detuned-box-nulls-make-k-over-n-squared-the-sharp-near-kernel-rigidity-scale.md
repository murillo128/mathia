# ANF-154 — detuned box nulls make K/N^2 the sharp near-kernel rigidity scale

**Status:** `EXACT-DERIVED + QUANTITATIVE-NEAR-KERNEL + SHARP-ORDER + SOURCE-GATE-REFINEMENT`. `ANF-153` freezes the bow geometry by unitary gauge and classifies the exact kernel of the integer length-`K` moving-window operator as the zero-mean `K`-periodic sequences. It also warns that the bow requirement `q=o(1)` cannot automatically be promoted to approximate periodicity: the elementary lag-`K` estimate only gives a useful local recurrence when `qK=o(1)`. The quantitative gap can now be located sharply. For the normalized integer box Gram operator, the smallest positive spectral scale is of order `K/N^2` in the bow regime `K=o(N)`. More precisely, every coefficient vector whose normalized moving energy is `q` lies within weighted squared distance `O(K ceil(N/K)^2 q)` of the exact periodic kernel, while a detuned `K`th-root character on the cofinal family `N=mK` is exactly weighted-orthogonal to that kernel and has `q=(pi^2+o(1))K/N^2`. Thus even `qK=o(1)` can coexist with maximal global distance from every exact periodic profile. The exact-kernel picture of `ANF-153` becomes globally rigid only at the much smaller scale `q=o(K/N^2)`; ordinary bow cancellation `q=o(1)` is far too weak to force it.

## 1. The fixed untwisted box geometry has a quantitative global recurrence bound

Keep the integer model of `ANF-146` and `ANF-153`:

\[
A_{N,K}:\mathbb C^{N+K-1}\to\mathbb C^N,
\qquad
(A_{N,K}b)_j=\sum_{r=1}^{K}b_{j+r},
\quad 0\le j<N,
\tag{1}
\]

with `1<=K<=N`. Put

\[
s_j:=(A_{N,K}b)_j,
\qquad
V(b):=\sum_{j=0}^{N-1}|s_j|^2.
\tag{2}
\]

As in `ANF-153`, consecutive windows give the exact lag relation

\[
\Delta_n:=b_{n+K}-b_n=s_n-s_{n-1},
\qquad 1\le n\le N-1,
\tag{3}
\]

and hence

\[
\boxed{
E_K(b):=\sum_{n=1}^{N-1}|\Delta_n|^2
\le 4V(b).
}
\tag{4}
\]

The point of this pass is to integrate (4) along the whole collection of residue chains modulo `K`, rather than use it only as a local recurrence. Let

\[
M:=N+K-1,
\qquad
L:=\left\lceil\frac NK\right\rceil,
\qquad
\mu:=\frac{s_0}{K}.
\tag{5}
\]

For `1<=r<=K`, define the `K`-periodic comparison sequence on the available index range by

\[
p_{r+jK}:=b_r-\mu.
\tag{6}
\]

Its period mean is zero because `s_0=sum_{r=1}^K b_r`, so the exact kernel classification of `ANF-153` gives

\[
\boxed{p\in\ker A_{N,K}.}
\tag{7}
\]

For every existing site `r+jK`, telescoping (3) gives

\[
b_{r+jK}-p_{r+jK}
=
\mu+\sum_{ell=0}^{j-1}\Delta_{r+ell K}.
\tag{8}
\]

Each residue chain has at most `L` lag steps. Cauchy--Schwarz, followed by summation over all residues, therefore yields

\[
\begin{aligned}
\|b-p\|_2^2
&\le 2L^2 E_K(b)+2M|\mu|^2\\
&\le 8L^2V(b)+\frac{2M}{K^2}V(b)\\
&\le 12L^2V(b).
\end{aligned}
\tag{9}
\]

The constants are deliberately nonoptimized. What matters is the exact scaling `L^2`, the square of the number of `K`-steps needed to propagate one period across the full observation horizon.

## 2. The smallest positive normalized box scale is at least order K/N^2

Let `d_n` be the number of output windows containing site `n`, and define the exact diagonal norm

\[
D(b):=\sum_{n=1}^{M}d_n|b_n|^2,
\qquad
q(b):=\frac{V(b)}{D(b)}
\tag{10}
\]

for `b!=0`. Since `1<=d_n<=K`, (9) implies the weighted distance estimate

\[
\boxed{
\operatorname{dist}_{D}(b,\ker A_{N,K})^2
\le
12K L^2 V(b).
}
\tag{11}
\]

Equivalently,

\[
\boxed{
\frac{\operatorname{dist}_{D}(b,\ker A_{N,K})^2}{D(b)}
\le
12K\left\lceil\frac NK\right\rceil^2 q(b).
}
\tag{12}
\]

This already gives a sufficient quantitative rigidity criterion:

\[
q(b)\,K\left\lceil\frac NK\right\rceil^2\to0
\quad\Longrightarrow\quad
\frac{\operatorname{dist}_{D}(b,\ker A_{N,K})^2}{D(b)}\to0.
\tag{13}
\]

In the bow geometry `K=o(N)`, the left factor is asymptotic in scale to `qN^2/K`. Thus global approximation by an exact zero-mean `K`-periodic sequence follows from

\[
\boxed{q=o(K/N^2).}
\tag{14}
\]

The same estimate gives a spectral lower bound. Let

\[
W:=\operatorname{diag}(\sqrt{d_n}),
\qquad
C_0:=W^{-1}A_{N,K}^*A_{N,K}W^{-1}
\tag{15}
\]

as in `ANF-153`, and let `lambda_+(N,K)` denote the smallest positive eigenvalue of `C_0`. If `b` is `D`-orthogonal to `ker A_{N,K}`, then its weighted distance to the kernel equals `D(b)`. Applying (12) gives

\[
\boxed{
\lambda_+(N,K)
\ge
\frac{1}{12K\lceil N/K\rceil^2}
\ge
\frac{K}{48N^2}.
}
\tag{16}
\]

So the fixed operator of `ANF-153` does have a positive gap above its exact `(K-1)`-dimensional kernel, but that gap collapses on the polynomial scale `K/N^2`, not on the much larger `1/K` scale suggested by the first lag estimate alone.

## 3. A detuned root character attains the K/N^2 scale while remaining maximally far from the kernel

The order in (16) cannot be improved uniformly. Consider the cofinal family

\[
N=mK,
\qquad m\to\infty,
\qquad K\to\infty,
\tag{17}
\]

and choose an integer `ell` with `ell=floor(K/2)`. Set

\[
\theta:=\frac{2\pi\ell}{K}+\frac{2\pi}{N},
\qquad
b_n:=e^{in\theta},
\quad 1\le n\le N+K-1.
\tag{18}
\]

This is a `K`th-root box null detuned by only one Fourier quantum `2pi/N` over the full horizon. Since `|b_n|=1`, the exact moving diagonal is

\[
D(b)=NK.
\tag{19}
\]

The plane-wave formula of `ANF-146` gives

\[
V(b)=N|H_K(\theta)|^2,
\qquad
H_K(\theta)=\sum_{r=1}^{K}e^{ir\theta}.
\tag{20}
\]

Using the geometric-sum identity and `N=mK`,

\[
|H_K(\theta)|
=
\frac{\sin(\pi/m)}{\left|\sin(\pi\ell/K+\pi/N)\right|}.
\tag{21}
\]

Therefore

\[
\boxed{
q(b)
=
\frac{\sin^2(\pi/m)}{K\sin^2(\pi\ell/K+\pi/N)}
=
(\pi^2+o(1))\frac{K}{N^2}.
}
\tag{22}
\]

The important point is that this vector is not merely separated from one convenient periodic approximation. It is exactly weighted-orthogonal to the entire `K`-periodic subspace. Indeed, for any `K`th-root character

\[
\chi_a(n):=e^{2\pi ian/K},
\qquad 0\le a<K,
\tag{23}
\]

the moving weights factor as

\[
\begin{aligned}
\langle b,\chi_a\rangle_D
&=
\sum_n d_n e^{in(\theta-2\pi a/K)}\\
&=
\left(\sum_{j=0}^{N-1}e^{ij\phi_a}\right)
\left(\sum_{r=1}^{K}e^{ir\phi_a}\right),
\end{aligned}
\tag{24}
\]

where

\[
\phi_a
=
\frac{2\pi(\ell-a)}{K}+\frac{2\pi}{N}.
\tag{25}
\]

Because `N=mK`, one has `e^{iN phi_a}=1`, while `e^{i phi_a}!=1`. Hence the first geometric sum in (24) vanishes exactly. The `K`th-root characters span the full `K`-periodic subspace, so

\[
\boxed{
b\perp_D\ker A_{N,K}.}
\tag{26}
\]

Consequently

\[
\boxed{
\frac{\operatorname{dist}_{D}(b,\ker A_{N,K})^2}{D(b)}=1
}
\tag{27}
\]

while (22) tends to zero. Since this vector is admissible in the variational definition of `lambda_+`, (22) also gives

\[
\boxed{
\lambda_+(N,K)
\le
(\pi^2+o(1))\frac{K}{N^2}
}
\tag{28}
\]

on the family (17). Together with (16), this makes `K/N^2` the sharp order of the universal positive spectral scale above the box kernel.

There is a useful stress test hidden in the same example. From (22),

\[
q(b)K
=(\pi^2+o(1))\left(\frac KN\right)^2
\to0,
\tag{29}
\]

so the local lag-`K` criterion isolated in `ANF-153` is satisfied strongly. Indeed, the phase change from one `K`-step to the next is only `2pi/m=o(1)`. But that tiny mismatch accumulates over `m=N/K` blocks to a full `2pi` turn, and weighted orthogonality (27) shows that the global vector remains maximally far from every exact periodic profile. Local approximate recurrence is therefore not global near-kernel rigidity.

## 4. Bow cancellation is far above the periodic-rigidity threshold

The bow regime used by `ANF-102` and `ANF-146` has

\[
N\asymp X,
\qquad
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14.
\tag{30}
\]

Thus the sharp operator scale found above is

\[
\boxed{
\frac{K}{N^2}
=
X^{-1-2\epsilon+o(1)}.
}
\tag{31}
\]

The desired bow conclusion only asks for

\[
q_X(U;K)=\frac{V_X(U;K)}{D_X(K)}=o(1).
\tag{32}
\]

Equations (12), (22), and (31) show that this is separated from global periodic rigidity by a polynomial factor `N^2/K=X^{1+2epsilon+o(1)}`. Therefore the exact periodic kernel in `ANF-153` is a correct zero-energy model but cannot be used as a surrogate characterization of all bow-relevant near-null directions. Even the stronger condition `qK=o(1)` leaves room for vectors that are globally orthogonal to that kernel.

After the unitary gauge of `ANF-153`, the arithmetic source vector is

\[
y_U=D_UWr_X.
\tag{33}
\]

A source theorem proving only that `y_U` is not approximately `K`-periodic would therefore be too weak: detuned root characters already evade exact periodicity while occupying the first positive spectral scale. The correct fixed-geometry question remains the projector statement of `ANF-153`: how much arithmetic mass enters the entire collapsing low-spectrum sector of `C_0`, not merely its exact kernel.

This also sharpens the negative route. To contradict the bow it is enough to retain a fixed amount of source energy above a fixed spectral threshold, as `ANF-152` states. But if one wants to replace that projection language by a recurrence theorem, the recurrence has to resolve accumulated phase drift across `N/K` blocks. A one-step lag estimate cannot do so at the target norm scale.

## 5. Prior-art boundary and next source gate

The ingredients are classical. The boxcar/moving-average transfer function is the geometric sum with regularly spaced unit-circle zeros, and the `L^2` propagation in (8)--(12) is a finite discrete Poincare/telescoping estimate along residue chains. The literature audit found this standard FIR/Dirichlet-kernel picture and general discrete Poincare theory, but no external theorem is needed for the constants or the `K/N^2` bow specialization above. `ANF-146` and `ANF-153` already record the relevant box-filter prior-art boundary, so this finding introduces no new load-bearing source and `SOURCES.md` need not change.

The Mathia-specific consequence is the separation of three scales that had previously been easy to conflate: exact kernel membership, local lag-`K` recurrence, and global near-null spectral concentration. The detuned character proves that the first two do not control the third at bow strength. A natural next target is therefore to describe the low positive spectrum as slowly modulated neighborhoods of the nonconstant `K`th-root characters, or otherwise estimate the fixed projectors `P_{0,(0,tau]}` directly. On the source side, the decisive question is whether the demodulated post-sieve innovation `D_UWr_X` can load these detuned root-character tubes at the distinguished twist.

For `analytic_frontier`, this removes the tempting shortcut from `q=o(1)` to approximate periodic arithmetic structure. The universal geometry itself contains a polynomially thick near-kernel beyond its exact periodic nullspace. Any successful bow argument must control that low-spectrum family directionally, rather than only exclude exact or locally approximate `K`-periodicity.