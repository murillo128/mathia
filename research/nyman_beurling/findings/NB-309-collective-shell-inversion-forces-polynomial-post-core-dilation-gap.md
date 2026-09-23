# NB-309 — Collective shell inversion forces a polynomial post-core dilation gap

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-014, NB-290, NB-301, NB-306, NB-307, NB-308
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + PROJECTED-DILATION + POST-CORE-SPECTRUM + RECIPROCAL-SHELLS + MOBIUS-COEFFICIENT-OBSERVABILITY + SCHUR-TEST + RESIDUAL-GRAM + POLYNOMIAL-GAP + TARGET-RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
2\le m\le N,
\]

where `A_m` is the normalized integer dilation from `NB-290`, and put

\[
q:=\left\lfloor\frac Nm\right\rfloor,
\qquad
H_{N,m}:=U_N\ominus U_q,
\]

with `U_1={0}`. By `NB-306`, `U_q` is the complete unit right-singular subspace of `T_(N,m)`. Let `s_post(N,m)` denote the operator norm after quotienting that exact core.

`NB-307` identifies the post-core defect with a generalized residual-Gram pencil. The shell coefficient functionals of `NB-308`, used collectively rather than one pivot at a time, give the explicit lower bound

\[
\boxed{
1-s_{\rm post}(N,m)^2
\ge
\frac{1}{5(1+\sqrt2)\,mN^2 H_{mN}(H_N-H_q)}.
}
\tag{1}
\]

Here `H_r=sum_(k=1)^r 1/k` is the harmonic number. In particular, since `m<=N`,

\[
\boxed{
1-s_{\rm post}(N,m)^2
\ge
\frac{1}{5(1+\sqrt2)N^3(1+2\log N)(1+\log N)}.
}
\tag{2}
\]

Thus the first singular value below the exact isometric core cannot remain exponentially or superpolynomially close to one. The determinant/pivot-product certificate of `NB-307`--`NB-308` was therefore highly lossy for this question: direct collective observability of the residual Gram gives a polynomial separation.

In the first post-core strip

\[
\frac N2<m\le N,
\]

we have `q=1`, so the exact core is absent and `s_post(N,m)=beta_(N+1)(m)`. Hence

\[
\boxed{
1-\beta_{N+1}(m)^2
\ge
\frac{1}{5(1+\sqrt2)\,mN^2 H_{mN}(H_N-1)}.
}
\tag{3}
\]

The theorem does **not** show `beta_(N+1)(m)->0` in the linear-scale transition, and it remains purely source-side. It gives a polynomial lower bound on the gap below one, not a macroscopic gap, a target-occupation estimate, a finite-section Nyman-distance rate, or the Riemann hypothesis.

## 1. Exact post-core pencil from NB-307

For

\[
J:=\{q+1,\ldots,N\},
\]

define

\[
r_j:=(I-P_{U_q})g_j,
\qquad
s_j:=(I-P_{U_N})g_{mj},
\qquad j\in J,
\tag{4}
\]

and let

\[
S=(\langle r_i,r_j\rangle)_{i,j\in J},
\qquad
R=(\langle s_i,s_j\rangle)_{i,j\in J}.
\tag{5}
\]

Finite linear independence from `NB-014` makes both residual families independent, hence `S` and `R` are positive definite. `NB-307` proves the exact identity

\[
\boxed{
1-s_{\rm post}(N,m)^2
=
m\,\lambda_{\min}(R,S),
}
\tag{6}
\]

where

\[
\lambda_{\min}(R,S)
=
\inf_{a\ne0}\frac{a^*Ra}{a^*Sa}.
\tag{7}
\]

The task is therefore to lower-bound the numerator residual Gram collectively while keeping only a crude upper bound on the denominator Gram.

## 2. The denominator residual Gram has only harmonic size

The exact reciprocal-shell value from `NB-301` is

\[
g_j|_{I_k}=\frac{k\bmod j}{j},
\qquad
I_k=\left(\frac1{k+1},\frac1k\right].
\tag{8}
\]

For `k<j`, this equals `k/j`, while for `k>=j` its absolute value is at most one. Therefore

\[
\begin{aligned}
\|g_j\|_2^2
&=
\sum_{k\ge1}
\frac{|g_j|_{I_k}|^2}{k(k+1)}\\
&\le
\frac1{j^2}\sum_{k=1}^{j-1}\frac{k}{k+1}
+
\sum_{k=j}^{\infty}\frac1{k(k+1)}\\
&<\frac1j+\frac1j
=\frac2j.
\end{aligned}
\tag{9}
\]

Orthogonal projection cannot increase norm, so

\[
\|r_j\|_2^2\le\|g_j\|_2^2<\frac2j.
\tag{10}
\]

Consequently

\[
\boxed{
\lambda_{\max}(S)
\le\operatorname{tr}S
\le2\sum_{j=q+1}^{N}\frac1j
=2(H_N-H_q).
}
\tag{11}
\]

Thus for every coefficient vector `a`,

\[
a^*Sa
\le
2(H_N-H_q)\|a\|_2^2.
\tag{12}
\]

No conditioning information about the original canonical Gram is needed here.

## 3. Collective Möbius shell inversion lower-bounds the numerator Gram

Take `a=(a_j)_(j in J)` and form

\[
w:=\sum_{j\in J}a_js_j.
\tag{13}
\]

Because `j>q=floor(N/m)`, every `mj>N`. The coefficient extractor `L_n` of `NB-308` annihilates every `g_l` with `l<n` and extracts the coefficient of `g_n`. Since

\[
s_j=g_{mj}-P_{U_N}g_{mj},
\]

and the projection term belongs to `U_N`, while all indices `mj` are distinct, we have the exact identities

\[
\boxed{
L_{mj}(w)=a_j,
\qquad j\in J.
}
\tag{14}
\]

Write `w_k` for the value of `w` on `I_k`, with `w_0=0`. `NB-308` gives

\[
L_n(w)=\sum_{k=1}^{n}\lambda_{n,k}w_k,
\tag{15}
\]

where

\[
\lambda_{n,k}
=
-\mathbf1_{k\mid n}\mu(n/k)
+
\mathbf1_{k+1\mid n}\mu(n/(k+1)).
\tag{16}
\]

Introduce weighted shell coordinates

\[
z_k:=\frac{w_k}{\sqrt{k(k+1)}}.
\tag{17}
\]

Then

\[
\sum_{k\ge1}|z_k|^2=\|w\|_2^2.
\tag{18}
\]

Equations (14)--(17) say that `a=Mz`, where the finite matrix indexed by `j in J` and `1<=k<=mN` is

\[
M_{j,k}
:=
\lambda_{mj,k}\sqrt{k(k+1)}.
\tag{19}
\]

We now bound its `ell^2 -> ell^2` norm by a Schur test.

### Row sums

Fix `j` and write `n=mj`. Taking absolute values separately in the two divisor contributions of (16),

\[
\begin{aligned}
\sum_k|M_{j,k}|
&\le
\sum_{d\mid n}\sqrt{d(d+1)}
+
\sum_{\substack{d\mid n\\d\ge2}}\sqrt{(d-1)d}\\
&\le
2\sigma_1(n)+\frac12\tau(n)\\
&\le
\frac52\sigma_1(n).
\end{aligned}
\tag{20}
\]

Here `sigma_1` is the divisor sum and `tau` the divisor count. Since

\[
\frac{\sigma_1(n)}n
=
\sum_{d\mid n}\frac1d
\le H_n,
\tag{21}
\]

and `n=mj<=mN`,

\[
\boxed{
\max_j\sum_k|M_{j,k}|
\le
\frac52\,mN H_{mN}.
}
\tag{22}
\]

### Column sums

Fix `k`. For the first term in (16), the condition `k|mj` is equivalent to

\[
\frac{k}{\gcd(k,m)}\mid j.
\]

Among `1<=j<=N` there are at most `N gcd(k,m)/k` such indices. Therefore its contribution to the `k`-th column sum is at most

\[
\sqrt{k(k+1)}\frac{N\gcd(k,m)}k
\le\sqrt2\,Nm.
\tag{23}
\]

For the second term, `(k+1)|mj` similarly gives at most `N gcd(k+1,m)/(k+1)` possible indices and hence contribution at most

\[
\sqrt{k(k+1)}\frac{N\gcd(k+1,m)}{k+1}
\le Nm.
\tag{24}
\]

Restricting `j` to `J` can only reduce these counts, so

\[
\boxed{
\max_k\sum_j|M_{j,k}|
\le(1+\sqrt2)Nm.
}
\tag{25}
\]

The Schur test applied to (22)--(25) yields

\[
\boxed{
\|M\|_{2\to2}^2
\le
\frac52(1+\sqrt2)m^2N^2H_{mN}.
}
\tag{26}
\]

Using `a=Mz` and (18),

\[
\|a\|_2^2
\le
\frac52(1+\sqrt2)m^2N^2H_{mN}\,\|w\|_2^2.
\tag{27}
\]

But `||w||_2^2=a^*Ra`, so

\[
\boxed{
R\succeq
\frac{2}{5(1+\sqrt2)m^2N^2H_{mN}}I.
}
\tag{28}
\]

This is the key improvement over the pointwise pivot floor of `NB-308`: all residual coefficients are observed simultaneously by the shell data, so no determinant product is taken across `N-q` separate directions.

## 4. Polynomial post-core separation

Combining (12) and (28), every nonzero `a` satisfies

\[
\frac{a^*Ra}{a^*Sa}
\ge
\frac{1}{5(1+\sqrt2)m^2N^2H_{mN}(H_N-H_q)}.
\tag{29}
\]

Therefore

\[
\lambda_{\min}(R,S)
\ge
\frac{1}{5(1+\sqrt2)m^2N^2H_{mN}(H_N-H_q)}.
\tag{30}
\]

Substitution into the exact identity (6) proves (1).

For `N>=2`,

\[
H_{mN}\le1+\log(mN)\le1+2\log N,
\qquad
H_N-H_q\le H_N\le1+\log N,
\tag{31}
\]

and `m<=N`; hence (2) follows.

If `N/2<m<=N`, then `q=1` and `U_q={0}`. By `NB-306` there is no unit singular core, so `s_post(N,m)=beta_(N+1)(m)`, and (3) follows directly.

The estimate also gives a lower bound on the gap in the singular value itself because

\[
1-s_{\rm post}
=
\frac{1-s_{\rm post}^2}{1+s_{\rm post}}
\ge
\frac12(1-s_{\rm post}^2).
\tag{32}
\]

No claim is made that the displayed polynomial exponents or logarithms are sharp.

## 5. What changed relative to NB-307 and NB-308

`NB-307` reduced the post-core transition to the exact generalized residual-Gram pencil and obtained a determinant lower bound through multiplicative pivot survival. `NB-308` supplied a universal pointwise floor `sigma_n >> 1/n`, but multiplying those individual floors across an `O(N)`-dimensional band produced only an `exp(-Theta(N log N))` certificate.

The present argument reuses the same shell inversion in the correct collective direction. Instead of bounding every pivot and multiplying, it stacks the coefficient functionals into one analysis matrix and controls that matrix by row/column sparsity. The resulting smallest residual-Gram eigenvalue is only polynomially small. Therefore the factorially tiny determinant certificate was not evidence that the first post-core singular value can actually be exponentially close to one; it was principally a loss from converting a minimum-eigenvalue question into a product of all defect eigenvalues.

This does **not** close the source transition. A polynomial lower bound tending to zero is compatible with `s_post(N,m)->1`, and it gives no upper bound forcing `s_post` away from one by a constant. The live source question is now sharper: in the transition window between the exact plateau at `m<=N/2` and the superquadratic decay regime of `NB-303`, can the residual-Gram pencil be shown to have a macroscopic lower edge, or can one construct post-core near-isometries that saturate a vanishing polynomial gap?

The destination-side warning from `NB-284`--`NB-299` is unchanged. Even a strong source spectral gap does not by itself imply that the moving first-free Ford datum occupies the useful singular directions, nor does it give a Nyman-distance rate.

## 6. Adversarial checks

The proof uses only three structural facts already established on this research line: the exact post-core pencil of `NB-307`, the reciprocal-shell coefficient extractor of `NB-308`, and finite independence from `NB-014`. The remaining estimates are elementary.

The most delicate point is the column Schur bound. For fixed `k`, `k|mj` reduces to `(k/gcd(k,m))|j`, so the number of possible `j<=N` is at most `N gcd(k,m)/k`; the adjacent `(k+1)|mj` condition has the analogous count. Thus no hidden factor `N` or divisor count is lost in (23)--(25).

A second potential failure mode would be contamination of `L_(mj)(w)` by the projection terms in `s_j`. This cannot occur because every projection term lies in `U_N`, whereas `mj>N` for every `j>floor(N/m)`. Distinct `j` give distinct indices `mj`, so (14) is exact.

Finally, the denominator is deliberately bounded from above by its trace. This may be very wasteful but is safe and works in the direction needed for a generalized-eigenvalue lower bound.

## 7. Prior-art audit

A fresh audit on 2026-09-23 checked classical and recent neighboring work on the Nyman--Beurling/Baez-Duarte criterion, finite Gram geometry, coefficient control, and multiplicative/dilation structure. The closest general boundaries remain Baez-Duarte's discrete criterion, Alouges--Darses--Hillion on Gram structures in generalized Nyman--Beurling approximation, and recent work on Gram decay along multiplicative ladders. The audit did not locate the specific finite-section statement proved here: after removing the exact projected-dilation core, stack the reciprocal-shell Möbius coefficient extractors for the residual family and use their divisibility sparsity to obtain a polynomial lower bound for the residual-Gram pencil.

No external theorem is load-bearing for the proof: the Schur test, harmonic-number estimate, and elementary divisor-counting inequalities are standard, while the Nyman-specific ingredients are internal results cited above. Accordingly no new durable source dependency is added to `SOURCES.md`. This audit is a boundary check, not a claim of bibliographic novelty.

## 8. Research consequence

The source-side picture is now quantitatively separated into three regimes. Up to `m=N/2`, `NB-306` gives an exact unit singular core. Immediately after that core disappears, the present theorem forces at least a polynomial gap below one. Far beyond quadratic scale, `NB-303` forces the whole projected-dilation norm to zero.

The useful next discriminator is therefore no longer whether a nonzero post-core gap exists. It is whether the exact residual-Gram pencil in the linear-to-quadratic window has a **macroscopic** lower edge, or instead admits explicit near-isometric vectors with a gap that genuinely shrinks. Only after that source transition is understood does it become meaningful to combine it with the moving sample/target occupation machinery.