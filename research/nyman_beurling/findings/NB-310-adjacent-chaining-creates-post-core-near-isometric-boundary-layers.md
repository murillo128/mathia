# NB-310 — adjacent chaining creates post-core near-isometric boundary layers

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-304, NB-306, NB-308, NB-309
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + PROJECTED-DILATION + POST-CORE-SPECTRUM + ADJACENT-CANCELLATION + EXPLICIT-NEAR-ISOMETRY + STAIRCASE-BOUNDARY-LAYER + MOVING-CUTOFF + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
2\le m\le N,
\]

where `A_m` is the normalized integer dilation from `NB-290`. Put

\[
q:=\left\lfloor\frac Nm\right\rfloor,
\qquad
H_{N,m}:=U_N\ominus U_q.
\]

By `NB-306`, `U_q` is the complete unit right-singular subspace of `T_(N,m)`. Let `s_post(N,m)` be the operator norm of `T_(N,m)` after removing that exact core.

Define the overrun of the first generator outside the core by

\[
\boxed{
h:=m(q+1)-N,
\qquad
1\le h\le m,
}
\tag{1}
\]

and set

\[
n:=N+h=m(q+1).
\tag{2}
\]

Finally write

\[
C_n:=2H_{n-2}+1+\frac{\pi^2}{18},
\tag{3}
\]

where `H_r` is the harmonic number. Then the next canonical innovation after the exact core gives the explicit upper bound

\[
\boxed{
0<1-s_{\rm post}(N,m)^2
\le
\min\left\{
1,
\frac{m h^2 C_n}{n^2\sigma_{q+1}^2}
\right\},
}
\tag{4}
\]

where

\[
\sigma_j
:=
\operatorname{dist}(g_j,U_{j-1}).
\]

Using the universal pivot floor from `NB-308`,

\[
\sigma_{q+1}^2
\ge
\frac{3}{2\pi^2(q+1)^2},
\]

and `n=m(q+1)`, equation (4) becomes the completely explicit estimate

\[
\boxed{
0<1-s_{\rm post}(N,m)^2
\le
\min\left\{
1,
\frac{2\pi^2}{3}\,
\frac{h^2 C_n}{m}
\right\}.
}
\tag{5}
\]

Consequently, for any moving family with

\[
\frac{h^2\log n}{m}\longrightarrow0,
\tag{6}
\]

one has

\[
\boxed{s_{\rm post}(N,m)\longrightarrow1.}
\tag{7}
\]

Thus the loss of an exact unit-singular direction at a finite-section staircase edge is not followed by a uniform macroscopic spectral gap. Whenever the newly excluded product index `m(q+1)` lies only a sufficiently small distance `h` above `N`, the next canonical innovation is an explicit post-core near-isometry.

In the first post-core strip

\[
\frac N2<m\le N,
\]

we have `q=1`, `s_post(N,m)=beta_(N+1)(m)`, and the exact norm

\[
\|g_2\|_2^2=\frac{\log2}{4}
\]

gives the sharper bound

\[
\boxed{
0<1-\beta_{N+1}(m)^2
\le
\min\left\{
1,
\frac{2h^2 C_{N+h}}{(N+h)\log2}
\right\},
\qquad
h=2m-N.
}
\tag{8}
\]

In particular, at the first integer immediately beyond the exact plateau,

\[
m_N:=\left\lfloor\frac N2\right\rfloor+1,
\]

one has `h=1` for odd `N` and `h=2` for even `N`, hence

\[
\boxed{
1-\beta_{N+1}(m_N)^2
=O\!\left(\frac{\log N}{N}\right),
\qquad
\beta_{N+1}(m_N)\to1.
}
\tag{9}
\]

This resolves one branch of the discriminator left by `NB-309`: explicit post-core near-isometries do exist. The result does **not** determine the gap deeper inside the linear-to-quadratic transition, and it remains purely source-side; it gives no target-occupation estimate, finite-section Nyman-distance rate, or consequence for RH.

## 1. The first post-core innovation has an exact escape formula

Let

\[
w_{q+1}:=(I-P_{U_q})g_{q+1},
\qquad
\|w_{q+1}\|_2=\sigma_{q+1}.
\tag{10}
\]

Because `m>=2`, one has `q<=N/2`, so `q+1<=N` and therefore `w_(q+1) in U_N`. By construction it is orthogonal to `U_q`, hence

\[
w_{q+1}\in H_{N,m}.
\tag{11}
\]

Write

\[
J_{N,m}:=(I-P_{U_N})A_m|_{U_N}.
\tag{12}
\]

The isometry of `A_m` gives the exact defect identity

\[
I-T_{N,m}^*T_{N,m}=J_{N,m}^*J_{N,m}.
\tag{13}
\]

`NB-306` gives

\[
A_mU_q\subseteq U_N.
\tag{14}
\]

Therefore the projection subtracted in (10) creates no escape from the old section:

\[
J_{N,m}w_{q+1}
=J_{N,m}g_{q+1}.
\tag{15}
\]

The exact covariance from `NB-290` is

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right).
\tag{16}
\]

Since `m<=N`, the compensating vector `g_m` belongs to `U_N`. With `n=m(q+1)>N`, equations (15)--(16) therefore give

\[
\boxed{
J_{N,m}w_{q+1}
=
\sqrt m\,(I-P_{U_N})g_n.
}
\tag{17}
\]

Hence

\[
\frac{
\|w_{q+1}\|_2^2-
\|T_{N,m}w_{q+1}\|_2^2
}{
\|w_{q+1}\|_2^2
}
=
\frac{
 m\,\operatorname{dist}(g_n,U_N)^2
}{
\sigma_{q+1}^2
}.
\tag{18}
\]

Since `s_post(N,m)` is the supremum of `||T v||/||v||` over nonzero `v in H_(N,m)`, the single test vector (10) gives

\[
1-s_{\rm post}(N,m)^2
\le
\frac{
 m\,\operatorname{dist}(g_n,U_N)^2
}{
\sigma_{q+1}^2
}.
\tag{19}
\]

The strict positivity on the left follows from `NB-306`: after quotienting the complete unit core `U_q`, no nonzero exact unit-singular direction remains.

## 2. Adjacent scaled cancellations bridge the overrun `h`

For every `j>=3`, use the scaled adjacent defect from `NB-304`,

\[
d_j
:=
g_j-rac{j-1}{j}g_{j-1}.
\tag{20}
\]

`NB-304` proves

\[
\boxed{
\|d_j\|_2^2
\le
\frac{C_j}{j^2},
\qquad
C_j=2H_{j-2}+1+\frac{\pi^2}{18}.
}
\tag{21}
\]

The recurrence

\[
g_j=rac{j-1}{j}g_{j-1}+d_j
\]

telescopes exactly. For every `n>N`, induction gives

\[
\boxed{
g_n
=
\frac Nn g_N
+
\sum_{j=N+1}^{n}
\frac jn d_j.
}
\tag{22}
\]

The first term belongs to `U_N`, so

\[
\operatorname{dist}(g_n,U_N)
\le
\left\|
\sum_{j=N+1}^{n}
\frac jn d_j
\right\|_2.
\tag{23}
\]

By (21), monotonicity of `C_j`, and `n-N=h`,

\[
\begin{aligned}
\operatorname{dist}(g_n,U_N)
&\le
\sum_{j=N+1}^{n}
\frac jn\|d_j\|_2\\
&\le
\frac1n
\sum_{j=N+1}^{n}\sqrt{C_j}\\
&\le
\boxed{
\frac{h\sqrt{C_n}}{n}.
}
\end{aligned}
\tag{24}
\]

This is the only place where adjacent-generator closeness enters. The argument does not assume that the adjacent defects are orthogonal, nor does it infer a lower bound from their small norms. It merely constructs an explicit old-section approximant `(N/n)g_N` for the first product generator `g_n` lying beyond the cutoff.

Substituting (24) into (19) proves (4).

## 3. The pivot floor makes the boundary layer uniform in the core depth

`NB-308` gives

\[
\sigma_{q+1}
\ge
\frac{\sqrt{3/2}}{\pi(q+1)}.
\tag{25}
\]

Since `n=m(q+1)`, equations (4) and (25) yield

\[
\begin{aligned}
1-s_{\rm post}(N,m)^2
&\le
\frac{m h^2 C_n}{n^2}
\frac{2\pi^2(q+1)^2}{3}\\
&=
\boxed{
\frac{2\pi^2}{3}\frac{h^2C_n}{m}.
}
\end{aligned}
\tag{26}
\]

Adding the trivial upper bound `1` proves (5). Because `n<=N+m<=2N` in the declared regime, `C_n=O(log n)`. Condition (6) therefore forces the right side of (26) to vanish, proving (7).

The cancellation of the core-depth factor `(q+1)^2` is important. The near-isometry is not restricted to a fixed finite core. Even if `q` moves, the universal `1/(q+1)` pivot floor is just strong enough to offset the scaling introduced by transporting the next canonical innovation to the product index `m(q+1)`.

The sufficient boundary-layer width furnished by this argument is

\[
h=o\!\left(\sqrt{\frac{m}{\log n}}\right).
\tag{27}
\]

No optimality is claimed for this width. The triangle inequality in (23) may lose cancellation among adjacent defects, and the pivot floor (25) may be far from sharp for the particular `q+1` under consideration.

## 4. The first post-core strip has an exact denominator

If `N/2<m<=N`, then `q=1` and `U_q={0}`. Hence

\[
w_{q+1}=g_2,
\qquad
s_{\rm post}(N,m)=\beta_{N+1}(m),
\qquad
n=2m=N+h.
\tag{28}
\]

On reciprocal shells `I_k=(1/(k+1),1/k]`,

\[
g_2|_{I_k}
=
\begin{cases}
1/2,&k\text{ odd},\\
0,&k\text{ even}.
\end{cases}
\]

Therefore

\[
\|g_2\|_2^2
=
\frac14
\sum_{k\text{ odd}}
\frac1{k(k+1)}
=
\frac{\log2}{4}.
\tag{29}
\]

Applying (4) with `sigma_2^2=(log2)/4` and `m=n/2` gives

\[
1-\beta_{N+1}(m)^2
\le
\frac{2h^2C_n}{n\log2},
\tag{30}
\]

which is (8).

For

\[
m_N=\left\lfloor\frac N2\right\rfloor+1,
\]

one has

\[
h=2m_N-N
=
\begin{cases}
2,&N\text{ even},\\
1,&N\text{ odd}.
\end{cases}
\tag{31}
\]

Also `n=N+h<=N+2`, so (30) is `O(log N/N)`. `NB-306` simultaneously gives `beta_(N+1)(m_N)<1` for every finite `N`, because `2m_N>N`. Thus the equality plateau ends sharply at the finite level while its immediately adjacent singular value approaches one asymptotically.

This is a genuine near-isometry, not an artifact of source-tail support. The witness is the first canonical innovation excluded from the exact dilation core, and its small defect is measured directly by the projected-dilation operator.

## 5. Relation to the polynomial lower gap of NB-309

In the first post-core strip, `NB-309` gives

\[
1-\beta_{N+1}(m)^2
\ge
\frac{1}
{5(1+\sqrt2)mN^2H_{mN}(H_N-1)}.
\tag{32}
\]

Together with (8), the same exact finite-section gap is now bracketed on both sides:

\[
\frac{1}
{5(1+\sqrt2)mN^2H_{mN}(H_N-1)}
\le
1-\beta_{N+1}(m)^2
\le
\frac{2h^2C_{N+h}}
{(N+h)\log2}.
\tag{33}
\]

At the first integer beyond the plateau, (33) leaves a wide quantitative gap between roughly inverse-cubic/polylogarithmic and `O(log N/N)`. The exact asymptotic order remains open. What is no longer open is the qualitative alternative posed in `NB-309`: a macroscopic lower edge cannot hold uniformly all the way down to the plateau boundary, because the explicit sequence (31) has `beta->1`.

More generally, (5) shows the same soft transition after every unit-core staircase edge whenever the arithmetic overrun `h=m(q+1)-N` is small relative to `sqrt(m/log n)`. A constant spectral gap could still exist in regions bounded away from these staircase edges. The relevant source-side transition variable is therefore not only the coarse ratio `m/N`; the residue of `N` modulo `m`, through `h`, can control how close the first post-core mode remains to an exact isometry.

## 6. Adversarial checks

The proof uses the actual canonical generators and the actual normalized dilation. No arbitrary Hilbert model, support relaxation, or enlarged periodic source space is introduced.

The key direction in (19) is an **upper** bound on the spectral gap. Since `s_post` is a supremum over post-core unit vectors, any explicit test vector gives `1-s_post^2` no larger than its defect Rayleigh quotient. Reversing this inequality would be invalid.

The vector `w_(q+1)` is genuinely post-core: it is orthogonal to `U_q`. Subtracting its `U_q` projection does not alter escape because `A_mU_q subset U_N`. The compensating `g_m` term in the covariance also disappears only because the theorem assumes `m<=N`; no extension of (4) to `m>N` is asserted.

The telescoping approximant `(N/n)g_N` belongs to `U_N` and is used only to upper-bound `dist(g_n,U_N)`. The adjacent-defect estimate from `NB-304` controls the full `L^2(0,1)` norm, including its periodic tail. Thus no shell truncation or unproved tail omission enters (24).

When `N` is an exact multiple of `m`, one has `h=m`; the bound (5) can be larger than one and becomes uninformative. This is expected: the theorem identifies a boundary layer near the *next* product inclusion, not a uniform near-isometry throughout each staircase cell.

There is no contradiction with `NB-306`. Every finite post-core pair still has `s_post<1`; equations (7) and (9) say only that this strict gap may vanish along moving families. There is also no contradiction with the superquadratic decay of `NB-303`, because the boundary-layer construction here lies in `m<=N`, far below the regime `m/N^2->infinity` where the entire projected-dilation norm is forced to zero.

Finally, no target vector, zeta zero, first-free sample, or Nyman residual enters the construction. A near-isometric source direction may have negligible target occupation. The destination-side warning from `NB-284`--`NB-299` therefore remains unchanged.

## 7. Prior-art audit

A fresh audit on 2026-09-23 checked classical and recent work on integer fractional-part dilations, multiplicative autocorrelation, Nyman--Beurling Gram geometry, and finite-dimensional approximation. The closest classical boundary is Michel Balazard, *Sur les dilatations entières de la fonction partie fractionnaire*, Functiones et Approximatio Commentarii Mathematici 35 (2006), DOI `10.7169/facm/1229442615`, which gives two-sided scale information for the distance of an integer fractional-part dilation from the span of its predecessors. Báez-Duarte--Balazard--Landreau--Saias study the underlying multiplicative fractional-part autocorrelation, and Werner Ehm (`arXiv:2405.06349`) gives modern Gram formulae and decompositions. Recent multiplicative-ladder Gram decay is studied by Carvill (`arXiv:2510.18132`).

These sources make clear that neighboring-dilation closeness and innovation estimates are classical territory; no novelty is claimed for those ingredients. The targeted search did not locate the specific finite-section statement proved here: remove the exact unit-singular core of the canonical projected integer dilation, use its first excluded canonical innovation, and control the resulting spectral gap by the arithmetic overrun `m(q+1)-N`, yielding explicit asymptotic near-isometries at the staircase boundaries. Search absence is not a priority claim.

No external theorem is load-bearing for the proof. Equations (16), (21), and (25) are already canonical line findings, while the remaining steps are elementary projection geometry and telescoping. `SOURCES.md` therefore requires no update.

## 8. Research consequence

`NB-309` left a clean source-side dichotomy: either the post-core residual-Gram pencil develops a macroscopic lower edge somewhere in the linear-to-quadratic transition, or explicit near-isometries force a genuinely vanishing gap. The present finding resolves that dichotomy **at every sufficiently thin staircase boundary layer** in favor of near-isometries.

The first transition is especially sharp conceptually. `NB-306` says

\[
2m\le N
\quad\Longrightarrow\quad
\beta_{N+1}(m)=1,
\]

while the first integer beyond that plateau satisfies

\[
\beta_{N+1}\!\left(\left\lfloor\frac N2\right\rfloor+1\right)
=1-O\!\left(\frac{\log N}{N}\right)
\]

at the level of squared gap. Thus the exact finite-dimensional core disappears discontinuously, but the operator norm does not develop a uniform asymptotic jump.

The next useful source-side question is now more localized: determine the post-core lower edge **away from small-overrun staircase layers**. One can ask whether a macroscopic gap emerges when `h` is a fixed proportion of `m`, or whether different explicit vectors create near-isometries deeper inside the staircase cells. Improving the boundary-layer width in (27) would also be meaningful, but another support-only estimate would not address this operator-level question.

Only after that source transition is understood should it be recombined with the target-occupation machinery. The present result changes the source spectrum; it does not certify that the moving Ford datum sees the near-isometric direction or any complementary defect direction.