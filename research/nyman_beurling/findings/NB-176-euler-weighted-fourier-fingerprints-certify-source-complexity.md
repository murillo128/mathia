# NB-176 — Euler-weighted Fourier fingerprints certify source complexity

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-SPECIFIC + DUAL-CERTIFICATE + EULER-FOURIER + CAPPED-TRANSPORT + NB-175-INSTANTIATION`.

`NB-175` turns any jointly contractive family of capped-Poisson probes into a lower certificate for the approximate source complexity `mathfrak L_T(epsilon)`, but leaves open whether a natural source-side probe family can be chosen without optimizing over arbitrary Lipschitz observables. For the actual logarithmic derivative there is a canonical candidate: use the Euler frequencies `log n` with the same amplitudes `Lambda(n)n^(-1-a_T)` that occur in `zeta'/zeta`.

The resulting infinite Fourier feature map is already contractive for the truncated Poisson metric after a normalization of order one, uniformly for `0<a_T<=1`. Consequently its finite coordinate truncations are admissible `NB-175` witnesses, and their limit gives an explicit Gram-matrix lower certificate for `mathfrak L_T(epsilon)`. This removes the arbitrary probe-design step: one can test source-visible template complexity directly from the squared Euler amplitudes of the real source.

## Claim

Fix one `T` and abbreviate

\[
a:=a_T,\qquad q:=q_T,\qquad 0<a\le1.
\]

For `n>=2` put

\[
c_{n,a}:=\frac{\Lambda(n)}{n^{1+a}},
\]

and define

\[
S_0(a):=\sum_{n\ge2}c_{n,a}^2,
\qquad
S_2(a):=\sum_{n\ge2}c_{n,a}^2(\log n)^2,
\]

\[
Z_a:=\max\left\{2\sqrt{S_0(a)},\ a\sqrt{S_2(a)}\right\}.
\tag{1}
\]

Then

\[
\boxed{Z_a\asymp1\qquad(0<a\le1),}
\tag{2}
\]

with absolute implied constants.

Let

\[
d_a(u,v):=\min\left\{1,\frac{|u-v|}{a}\right\},
\]

and define the real Hilbert-valued Euler feature map

\[
F_a(u)
:=
\left(
\frac{c_{n,a}}{Z_a}\cos(u\log n),
-\frac{c_{n,a}}{Z_a}\sin(u\log n)
\right)_{n\ge2}
\in\ell_2(\mathbf R^2).
\tag{3}
\]

Then

\[
\boxed{
\|F_a(u)-F_a(v)\|_{\ell_2}
\le d_a(u,v)
\qquad(u,v\in\mathbf R).
}
\tag{4}
\]

Thus `F_a` is a canonical jointly contractive capped-Poisson witness in the sense of `NB-175`.

Now choose any realized templates

\[
\nu_1,\ldots,\nu_N\in\mathcal R_T
\]

from `NB-174`, and use the Fourier convention

\[
\widehat\nu_i(\lambda)
:=
\int e^{-i\lambda u}\,d\nu_i(u).
\]

Define the `N x N` real symmetric matrix

\[
\boxed{
G^{\mathrm{Eul}}_{ij}
:=
\frac1{q^2Z_a^2}
\sum_{n\ge2}
\frac{\Lambda(n)^2}{n^{2+2a}}
\Re\!\left(
\widehat\nu_i(\log n)
\overline{\widehat\nu_j(\log n)}
\right).
}
\tag{5}
\]

The series converges absolutely and `G^Eul` is positive semidefinite. For every `epsilon>=0`,

\[
\boxed{
\mathfrak L_T(\epsilon)
\ge
\frac{
\left(
\operatorname{tr}\sqrt{G^{\mathrm{Eul}}}
-\epsilon N
\right)_+^2
}{N}.
}
\tag{6}
\]

Equivalently, defining

\[
\mathfrak C_T^{\mathrm{Eul}}(\epsilon)
:=
\sup_{N\ge1}\ 
\sup_{\nu_1,\ldots,\nu_N\in\mathcal R_T}
\frac{
\left(
\operatorname{tr}\sqrt{G^{\mathrm{Eul}}}
-\epsilon N
\right)_+^2
}{N},
\tag{7}
\]

one has the intrinsic chain

\[
\boxed{
\mathfrak C_T^{\mathrm{Eul}}(\epsilon)
\le
\mathfrak C_T(\epsilon)
\le
\mathfrak L_T(\epsilon),
}
\tag{8}
\]

where `mathfrak C_T` is the unrestricted dual certificate of `NB-175`.

A useful spectral corollary is immediate. If for some `alpha>0`

\[
G^{\mathrm{Eul}}\succeq\alpha^2 I_N,
\]

then

\[
\boxed{
\mathfrak L_T(\epsilon)
\ge
N(\alpha-\epsilon)_+^2.
}
\tag{9}
\]

Thus a family of realized templates whose **actual Euler fingerprints** retain `N` uniformly nondegenerate Hilbert directions above the admissible `NB-174` tolerance forces approximate source complexity of order `N`.

## Derivation

### The full Euler feature map fits inside one capped-Poisson dual budget

Since `Lambda(n)<=log n`,

\[
S_0(a)
\le
\sum_{n\ge2}\frac{(\log n)^2}{n^2},
\qquad
S_2(a)
\le
\sum_{n\ge2}\frac{(\log n)^4}{n^2},
\]

uniformly for `0<a<=1`. Both comparison series converge. On the other hand the single term `n=2` gives a positive uniform lower bound for `2 sqrt(S_0(a))`. Hence (2).

Put

\[
w_{n,a}:=\frac{c_{n,a}}{Z_a}.
\]

For `h=|u-v|`, the elementary identity for two points on the unit circle gives

\[
\|F_a(u)-F_a(v)\|_{\ell_2}^2
=
4\sum_{n\ge2}
 w_{n,a}^2
\sin^2\!\left(\frac{h\log n}{2}\right).
\tag{10}
\]

If `h>=a`, then by the first term in the maximum (1),

\[
\|F_a(u)-F_a(v)\|_{\ell_2}^2
\le
4\sum_{n\ge2}w_{n,a}^2
=
\frac{4S_0(a)}{Z_a^2}
\le1.
\tag{11}
\]

If `h<=a`, use `2|sin(x/2)|<=|x|` and the second term in (1):

\[
\|F_a(u)-F_a(v)\|_{\ell_2}^2
\le
h^2\sum_{n\ge2}w_{n,a}^2(\log n)^2
=
\frac{h^2S_2(a)}{Z_a^2}
\le
\frac{h^2}{a^2}.
\tag{12}
\]

Equations (11)--(12) prove (4). The point worth retaining is that the unbounded Euler frequency set causes no dual-budget divergence: the square-summable Euler amplitudes have enough logarithmic moment to absorb the derivative cost, and the normalizing constant stays `Theta(1)` as the exterior line approaches `Re s=1`.

### The limiting response Gram gives an explicit NB-175 certificate

For each `M`, project `F_a` onto any finite collection of the first `M` nonzero von Mangoldt coordinates. The projected map remains `d_a`-contractive. Its real scalar coordinates therefore give a finite jointly contractive probe family under `NB-175`, with

\[
\ell_{n,c}(\sigma)
=
\frac{w_{n,a}}q
\int\cos(u\log n)\,d\sigma(u),
\]

\[
\ell_{n,s}(\sigma)
=
-\frac{w_{n,a}}q
\int\sin(u\log n)\,d\sigma(u).
\tag{13}
\]

For the selected templates, let `A_M` be the finite response matrix. Its row Gram matrix is

\[
(A_MA_M^{\mathsf T})_{ij}
=
\frac1{q^2Z_a^2}
\sum_{n\in I_M}
\frac{\Lambda(n)^2}{n^{2+2a}}
\Re\!\left(
\widehat\nu_i(\log n)
\overline{\widehat\nu_j(\log n)}
\right).
\tag{14}
\]

Every finite signed template has bounded Fourier transform, while `S_0(a)<infinity`, so these Gram matrices converge entrywise, hence in every finite-dimensional matrix norm, to `G^Eul` in (5). Since

\[
\|A_M\|_*
=
\operatorname{tr}\sqrt{A_MA_M^{\mathsf T}},
\]

continuity of the eigenvalues for fixed `N` gives

\[
\|A_M\|_*
\longrightarrow
\operatorname{tr}\sqrt{G^{\mathrm{Eul}}}.
\tag{15}
\]

For all sufficiently large truncations there are at least `N` real probe coordinates, so the `r=min{N,K}` term in `NB-175` equals `N`. Applying that finding to `A_M` and passing to the limit yields exactly (6). Taking suprema gives (8), while `G^Eul >= alpha^2 I_N` implies `tr sqrt(G^Eul)>=N alpha` and proves (9).

## Why this witness is source-native

For every stationary zero-mass finite signed template `nu`, absolute convergence in `Re s=1+a>1` permits termwise integration in the Euler expansion

\[
\frac{\zeta'}{\zeta}(s)
=-\sum_{n\ge2}\frac{\Lambda(n)}{n^s}.
\]

Hence

\[
\boxed{
\int
\frac{\zeta'}{\zeta}(1+a+i(t+u))
\,d\nu(u)
=
-\sum_{n\ge2}
\frac{\Lambda(n)}{n^{1+a}}
 n^{-it}
\widehat\nu(\log n).
}
\tag{16}
\]

The coordinates measured by `G^Eul` are therefore not arbitrary harmonic-analysis probes attached after the fact. They are the individual template multipliers of the actual Euler modes that are coherently summed by the source itself. Prime powers appear automatically through `Lambda`; no prime-only surrogate is introduced.

There is nevertheless an important distinction. Equation (16) is a scalar coherent sum with phases `n^{-it}`, whereas (5) measures the `ell_2` geometry of the same mode amplitudes. The present result says that many mutually independent Euler-mode fingerprints are sufficient to force large source-resolved template complexity. It does **not** say that this Hilbert fingerprint is equivalent to the scalar arithmetic rescue problem.

## Stress test and limitations

The normalization cannot be inflated by adding more frequencies. All coordinates share the single budget fixed by `Z_a`, and the complete infinite feature map already satisfies the joint contraction (4). Duplicating a mode would require renormalizing the feature energy and gives no free gain, matching the anti-duplication purpose of the joint `ell_2` condition in `NB-175`.

The lower certificate remains one-sided. A small or low-rank `G^Eul` does not prove that `mathfrak L_T(epsilon)` is small: another capped-Lipschitz witness may detect template distinctions that the Euler frequencies suppress. Conversely, a large Euler Gram proves source-visible geometric complexity but not useful arithmetic phase alignment. The coefficients in (16) may still fail to combine with the phases `n^{-it}` into logarithmic rescue on the required heights.

At the admissible `NB-174` scale

\[
\epsilon_T=\Theta\!\left(\frac{\log T}{H_T}\right),
\]

(9) has content only for Euler fingerprint singular values that themselves survive this tolerance. That is a feature rather than a defect: sub-resolution distinctions are precisely the template motion that `NB-174` quotients away.

Nothing here removes the sparse-height escape, the ultra-thin `a_T\lesssim T^{-1/2}` limitation inherited from the stationary mean-square theorem, or the final gap back to global Nyman--Beurling approximation. No claim is made that a natural admissible sampler already supplies arbitrarily large nondegenerate Euler Gram matrices.

## Representation and prior-art audit

The Hilbert feature-map viewpoint is generic. Fourier/RKHS embeddings of measures and Gram metrics generated by translation-invariant spectral features are classical; for example, Sriperumbudur, Gretton, Fukumizu, Schölkopf and Lanckriet, *Hilbert Space Embeddings and Metrics on Probability Measures*, JMLR 11 (2010), 1517--1561, develops this general representation technology. The capped Lipschitz/transport duality used to certify contractivity is likewise classical background already separated from the arithmetic content in `NB-167` and `NB-175`.

The source-specific step is narrower and proved directly here: choose the Fourier spectrum with the **actual squared Euler amplitudes** `Lambda(n)^2 n^(-2-2a)`, show that its full feature map is dominated by the capped Poisson metric with an order-one normalization uniformly in `a`, and feed the resulting response Gram into the `NB-175` source-complexity inequality. A focused search over Nyman--Beurling, Fourier/RKHS measure embeddings and logarithmic-derivative Euler expansions located the standard surrounding ingredients but not this particular transfer. That absence is not used as evidence of novelty.

No new external theorem is load-bearing. The Euler expansion is classical and elementary in `Re s>1`; all summability, contractivity and matrix-limit steps needed above are proved here. The only structural dependencies are the already-persisted capped-Poisson geometry and dual certificate. Therefore `research/nyman_beurling/SOURCES.md` is unchanged.

## Evidence ledger

**Internal load-bearing dependencies:** `NB-167` for the capped Poisson metric; `NB-174` for `mathfrak L_T(epsilon)` and the admissible source resolution; `NB-175` for the finite jointly contractive nuclear-response lower certificate.

**External load-bearing dependencies:** none.

**Context-only prior art consulted:** classical Fourier/RKHS embeddings of measures, including Sriperumbudur et al. (JMLR 2010), and classical bounded-Lipschitz/Kantorovich--Rubinstein geometry.

## Frontier moved

`NB-175` left the dual certificate existential: a useful lower bound still required designing a jointly contractive Hilbert-valued observable. Equations (3)--(8) supply a canonical source-native choice. **The Euler expansion itself defines an order-one capped-Poisson feature map, and the singular geometry of its response Gram is now a directly computable sufficient witness for large approximate source complexity.**

The next sharp question is no longer whether a natural probe family exists. It is whether source-natural adaptive Nyman templates can realize many Euler fingerprints whose singular values remain above `epsilon_T`, and, separately, whether a large Euler-fingerprint rank can be converted into the coherent phase alignment required by (16). Failure of the first would show that the approximate-complexity escape is unavailable to that architecture; failure of the second would expose a stricter arithmetic obstruction beyond geometric source complexity.