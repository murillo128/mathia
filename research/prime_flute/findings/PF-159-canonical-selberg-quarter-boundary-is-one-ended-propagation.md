# PF-159 — canonical Selberg quarter boundary is a one-ended propagation term

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + DECISIVE-NEGATIVE/REFINEMENT` for the `Re s=1/4` boundary isolated in PF-158. PF-158 proves that the exact prime/all-composite-shift relative Selberg cocycle over the complete PF-004 canonical separator family is holomorphic and zero-free on `Re s>1/4`, with a sharp positive-real ordinary-convergence boundary at `1/4`. The present finding identifies the source of that boundary. After subtracting, for each left exterior gap, its exact one-ended far-separator response, the remaining two-ended interaction converges locally normally on the entire half-plane

\[
\boxed{\operatorname{Re}s>0.}
\]

The removed one-ended term alone has the sharp positive-real abscissa `1/4`. Thus the quarter boundary is not a collective prime-tail interaction: it is the long-channel propagation of a single exterior-gap mismatch, precisely the compact-defect mechanism already isolated abstractly by PF-102. This does **not** construct a full Selberg zeta function, a spectral determinant, a meromorphic continuation, or an RH mechanism.

## Claim

Use the exact source/clone endpoint laws

\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad
W(x)=V(x+1)-1,
\qquad
d(x)=W(x)-V(x).
\tag{1}
\]

PF-106 gives

\[
d(x)>0,\qquad d'(x)<0,\qquad d(x)=O(x^{-2}),\qquad d'(x)=O(x^{-3}).
\tag{2}
\]

For a PF-004 canonical separator with consecutive exterior prime pairs

\[
a<b<c<d,
\tag{3}
\]

write

\[
X=V(b)-V(a),\qquad
Y=V(c)-V(b),\qquad
Z=V(d)-V(c),\qquad
S=X+Y+Z.
\tag{4}
\]

The source cross-ratio and length are

\[
\chi=\frac{YS}{XZ},
\qquad
L=4\operatorname{arsinh}\sqrt\chi.
\tag{5}
\]

Put superscript `+` on the corresponding quantities formed with `W`. Since `d` is strictly decreasing,

\[
X^+=X+d(b)-d(a)<X.
\tag{6}
\]

Define the exact left-edge response

\[
\boxed{R_a:=\frac{X}{X^+}>1,}
\tag{7}
\]

and the **one-ended model cross-ratio and length**

\[
\boxed{
\widehat\chi_{a,c}:=R_a\chi_{a,c},
\qquad
\widehat L_{a,c}:=4\operatorname{arsinh}\sqrt{\widehat\chi_{a,c}}.
}
\tag{8}
\]

The multiplier `R_a` is not fitted or chosen: PF-158 proves exactly

\[
\lim_{c\to\infty}\frac{\chi^+_{a,c}}{\chi_{a,c}}=R_a
\tag{9}
\]

for every fixed left pair. Thus (8) removes the canonical one-ended cluster limit of the matched separator response.

For the standard local Selberg factor

\[
Z_L(s)=\prod_{m=0}^{\infty}(1-e^{-(s+m)L}),
\qquad
Q_s(L)=\frac d{ds}\log Z_L(s),
\tag{10}
\]

define the connected canonical logarithmic derivative

\[
\boxed{
G_{\rm conn}(s)
:=
\sum_{\eta\in\mathcal C}
\left[Q_s(L_\eta^+)-Q_s(\widehat L_\eta)\right].
}
\tag{11}
\]

Then:

1. the series (11) converges absolutely and locally uniformly on `Re s>0`;
2. hence `G_conn` is holomorphic there;
3. for any `s_0` with `Re s_0>0`, the normalized finite products
   \[
   D_{{\rm conn},E}(s;s_0)
   :=
   \prod_{\eta\in E}
   \frac{Z_{L_\eta^+}(s)}{Z_{\widehat L_\eta}(s)}
   \frac{Z_{\widehat L_\eta}(s_0)}{Z_{L_\eta^+}(s_0)}
   \tag{12}
   \]
   converge locally uniformly, independently of exhaustion, to
   \[
   D_{\rm conn}(s;s_0)
   =
   \exp\!\left(\int_{s_0}^sG_{\rm conn}(w)\,dw\right),
   \tag{13}
   \]
   and therefore this normalized bookkeeping factor is zero-free on `Re s>0`;
4. on the common ordinary-convergence half-plane `Re s>1/4`, PF-158's canonical logarithmic derivative decomposes exactly as
   \[
   \boxed{
   G_{\rm can}(s)=G_{\rm one}(s)+G_{\rm conn}(s),
   }
   \tag{14}
   \]
   where
   \[
   G_{\rm one}(s)
   :=
   \sum_{\eta\in\mathcal C}
   \left[Q_s(\widehat L_\eta)-Q_s(L_\eta)\right];
   \tag{15}
   \]
5. `G_one` has sharp positive-real ordinary-convergence abscissa `1/4`: it converges locally normally for `Re s>1/4`, while for every real `0<sigma<=1/4`, fixing any one left exterior pair and summing over far right pairs gives an eventually one-sign subseries diverging to `-infinity`.

Consequently the `1/4` obstruction of PF-158 lies entirely in the one-ended term (15); the residual interaction after removing the exact far-right cluster response has no positive-real convergence threshold other than `0`.

## 1. Exact factorization of the cross-ratio defect

From (1) and (4),

\[
\begin{aligned}
X^+&=X+d(b)-d(a),\\
Y^+&=Y+d(c)-d(b),\\
Z^+&=Z+d(d)-d(c),\\
S^+&=S+d(d)-d(a).
\end{aligned}
\tag{16}
\]

Since

\[
\chi^+=\frac{Y^+S^+}{X^+Z^+},
\qquad
R_a\chi=\frac{YS}{X^+Z},
\]

there is the exact identity

\[
\boxed{
\frac{\chi^+}{R_a\chi}
=
\frac{Y^+}{Y}
\frac{S^+}{S}
\frac{Z}{Z^+}.
}
\tag{17}
\]

This identity separates the nondecaying left-edge response `R_a` from the genuinely two-ended remainder. It is the key step: no Selberg manipulation or analytic continuation is used to manufacture the split.

PF-106 also gives

\[
\boxed{R_a=1+O(a^{-3})}
\tag{18}
\]

uniformly in the consecutive prime gap `b-a`, because `d(a)-d(b)=O(a^{-3}(b-a))` while `X^+>=b-a`.

## 2. The connected cross-ratio error gains one full right-endpoint power

Consider the far-span regime

\[
c\ge4a.
\tag{19}
\]

The Baker--Harman--Pintz exponent already audited in S6 gives `b=a+O(a^theta)` with `theta=0.525<1`. Hence, after discarding finitely many `a`,

\[
Y\ge c-b\ge\frac c2,
\qquad
S\ge d-a\ge\frac{3c}{4}.
\tag{20}
\]

By (2),

\[
|Y^+-Y|
=|d(c)-d(b)|
\le d(b)
\le Ca^{-2},
\tag{21}
\]

and similarly

\[
|S^+-S|\le d(a)\le Ca^{-2}.
\tag{22}
\]

For the right exterior interval, the mean-value theorem and `d'(x)=O(x^-3)` give

\[
|Z^+-Z|
\le Cc^{-3}(d-c).
\tag{23}
\]

Since `V'>1`, `Z>=d-c`, and therefore

\[
\left|\frac{Z^+}{Z}-1\right|
\le Cc^{-3}.
\tag{24}
\]

For large enough `a` all three relative errors are small, so (17) yields

\[
\boxed{
\left|
\log\frac{\chi^+}{R_a\chi}
\right|
\le
C\left(\frac{a^{-2}}c+c^{-3}\right).
}
\tag{25}
\]

The finitely many discarded left labels satisfy the same estimate with a constant depending on that fixed label, which is harmless below.

Let

\[
F(u):=4\operatorname{arsinh}\sqrt u.
\]

As used throughout the line,

\[
0<\frac{dF}{d\log u}
=2\sqrt{\frac{u}{1+u}}
\le2.
\tag{26}
\]

Equations (8), (25), and (26) therefore give the crucial connected length estimate

\[
\boxed{
|L^+-\widehat L|
\le
C\left(\frac{a^{-2}}c+c^{-3}\right)
\qquad(c\ge4a).
}
\tag{27}
\]

Compare this with PF-158's unrenormalized all-span `O(a^-3)` bound. The latter does not decay as the right endpoint tends to infinity with `a` fixed; (27) does. That extra right-endpoint decay removes the quarter threshold.

## 3. Near spans are already harmless on every positive half-plane

For

\[
c<4a,
\tag{28}
\]

PF-106/PF-109 give

\[
\left|\log\frac{L^+}{L}\right|=O(a^{-3}).
\tag{29}
\]

Equation (18) and the bounded logarithmic derivative of `F` give likewise

\[
\left|\log\frac{\widehat L}{L}\right|=O(a^{-3}),
\tag{30}
\]

so

\[
\left|\log\frac{L^+}{\widehat L}\right|=O(a^{-3}).
\tag{31}
\]

PF-158's short/long Selberg-sensitivity estimates therefore imply, for every compact `K subset {Re s>0}`,

\[
\sup_{s\in K}
|Q_s(L^+)-Q_s(\widehat L)|
\le C_Ka^{-3}
\tag{32}
\]

uniformly over all near spans. There are at most `O(a)` possible right labels `c<4a`, so

\[
\sum_a\sum_{c<4a}
\sup_{s\in K}
|Q_s(L^+)-Q_s(\widehat L)|
\le C_K\sum_a a^{-2}<\infty.
\tag{33}
\]

No prime-density theorem is used.

## 4. Far spans converge for every `Re s>0`

Let `K subset {Re s>0}` be compact and put

\[
\sigma_K:=\inf_{s\in K}\operatorname{Re}s>0.
\]

Choose

\[
0<\rho<\min(\sigma_K,1/2).
\tag{34}
\]

PF-158 proves, for long lengths,

\[
\sup_{s\in K}
\left|\frac{\partial}{\partial L}Q_s(L)\right|
\le C_K(1+L)e^{-\sigma_KL},
\tag{35}
\]

and in the far-span geometry

\[
L=O(1+\log c),
\tag{36}
\]

\[
\boxed{
e^{-\rho L}
\le C_{rho}
 a^{2\rho\theta}Z^{2\rho}c^{-4\rho}.}
\tag{37}
\]

Since `\widehat L-L=O(a^-3)` and (27) makes `L^+-\widehat L=o(1)` in the tail, after finitely many exceptions every interpolation between `L^+` and `\widehat L` has enough of the same long-length scale to replace `sigma_K` by `rho` in (35). Combining (27), (35)--(37) gives

\[
\sup_{s\in K}|Q_s(L^+)-Q_s(\widehat L)|
\le
C_K
\left(\frac{a^{-2}}c+c^{-3}\right)
(1+\log c)
 a^{2\rho\theta}Z^{2\rho}c^{-4\rho}.
\tag{38}
\]

Put `beta=2rho`, so `0<beta<1`. PF-158's elementary dyadic consecutive-gap moment remains valid:

\[
\boxed{
\sum_{\substack{R\le c<2R\\c\ {\rm prime}}}
Z^{2\rho}
\le C_\rho R.}
\tag{39}
\]

For a dyadic block `R<=c<2R`, `R>=4a`, the first term in (38) contributes at most

\[
C_K
a^{-2+2\rho\theta}
R^{-4\rho}(1+\log R),
\tag{40}
\]

while the `c^-3` term contributes at most

\[
C_K
a^{2\rho\theta}
R^{-2-4\rho}(1+\log R).
\tag{41}
\]

Both dyadic series converge for **every** `rho>0`. Summing from `R=4a` gives

\[
\boxed{
\sum_{c\ge4a}
\sup_{s\in K}|Q_s(L^+)-Q_s(\widehat L)|
\le
C_K
a^{-2-2\rho(2-\theta)}(1+\log a).
}
\tag{42}
\]

The right side is summable over all large left primes `a`; the finitely many small `a` contribute finite amounts because their dyadic right tails still have the factor `R^{-4rho}`. Together with (33), this proves absolute local-uniform convergence of (11) on the full positive half-plane.

This is exactly where the improvement occurs. PF-158's unrenormalized far block is proportional to `R^(1-4rho)`, forcing `rho>1/4`. Removing the exact one-ended limit inserts an additional `1/R`, leaving `R^(-4rho)`, which is summable for every positive `rho`.

## 5. The quarter boundary survives entirely in the one-ended term

On `Re s>1/4`, both `G_can` from PF-158 and `G_conn` from (11) converge locally normally, so (14) defines `G_one` there and its series (15) converges locally normally.

Now fix one left pair `a<b`. PF-158 proves that for real `sigma>0`, as the right pair tends to infinity,

\[
L^+-L\longrightarrow
\delta_a:=2\log R_a>0
\tag{43}
\]

and that the original fixed-left subseries

\[
\sum_c[Q_\sigma(L^+_{a,c})-Q_\sigma(L_{a,c})]
\tag{44}
\]

is eventually negative and diverges to `-infinity` for every

\[
0<\sigma\le\frac14.
\tag{45}
\]

For the same fixed `a`, (25)--(42) show that

\[
\sum_c
|Q_\sigma(L^+_{a,c})-Q_\sigma(\widehat L_{a,c})|
<\infty
\qquad(\sigma>0).
\tag{46}
\]

Subtracting the absolutely convergent connected subseries from (44) leaves

\[
\sum_c[Q_\sigma(\widehat L_{a,c})-Q_\sigma(L_{a,c})],
\tag{47}
\]

which therefore has the same eventual one-sign divergence at and below `1/4`. Thus `G_one` alone carries the sharp positive-real ordinary-convergence boundary.

Equivalently, the mechanism is

```text
one fixed exterior-gap response R_a != 1
    -> propagated through arbitrarily distant canonical separators
    -> L_hat - L -> 2 log R_a
    -> Selberg sensitivity ~ (log c) c^(-4s)
    -> reciprocal-prime divergence at s <= 1/4.
```

PF-102 already shows that exactly this architecture can be produced by moving **one compact endpoint while leaving the entire sufficiently far prime tail unchanged**. PF-159 upgrades that control from analogy to an exact decomposition of PF-158's prime/shift canonical-sector cocycle.

## 6. What is intrinsic and what is only a counterterm

The quantities entering the decomposition are canonical within the already-selected PF-004 sector:

- `L` and `L^+` are genuine primitive separator lengths on the source and exact all-composite clone;
- `R_a=X/X^+` is the exact relative response of the marked left exterior interval;
- `R_a` is characterized without an arbitrary parameter by the cluster limit (9);
- `\widehat L` is therefore the unique length obtained by retaining only that one-ended limiting cross-ratio response.

Nevertheless `\widehat L` need not be the length spectrum of one globally defined auxiliary hyperbolic surface. Accordingly, `D_conn` in (12)--(13) is a **canonical analytical subtraction of the PF-158 selected sector**, not a new physical Selberg determinant. Its value is diagnostic: it identifies which part of the already-defined relative cocycle creates the convergence wall.

This distinction matters for the research mandate. PF-159 does not propose `D_conn` as a zeta-like object whose zeros should encode arithmetic. In fact its zero-freeness is part of the negative conclusion.

## 7. Prior art and novelty audit

No novelty is claimed for the standard local Selberg factor, relative/normalized products, cluster-style subtraction as a general analytic idea, elementary cross-ratio algebra, dyadic summation, or the principle that a compact perturbation can influence infinitely many long trajectories.

The closest standard Selberg theories remain finite-geometry ones. Borthwick--Judge--Perry, *Selberg's zeta function and the spectral geometry of geometrically finite hyperbolic surfaces*, Comment. Math. Helv. 80 (2005), 483--515, DOI `10.4171/CMH/23`, relates Selberg zeta, relative scattering phase and resonances for geometrically finite surfaces. Borthwick--Judge--Perry, *Determinants of Laplacians and isopolar metrics on surfaces of infinite area*, Duke Math. J. 118 (2003), 61--102, DOI `10.1215/S0012-7094-03-11814-1`, treats relative determinants for metrics hyperbolic near infinity in a finite-geometry setting. Neither framework supplies an Euler product for the present infinitely generated flute with the PF-069/PF-077 non-locally-finite primitive length data.

Directed searches for relative Selberg zeta functions under compact perturbations, cluster/connected decompositions of geodesic Euler products, and infinite-type relative length-spectrum products recovered those finite-geometry determinant/scattering theories and ordinary compact/convex-cocompact dynamical-zeta settings, but no theorem giving the project-specific decomposition (17) or the improvement from `Re s>1/4` to `Re s>0` after the exact one-ended subtraction.

The durable new content is deliberately project-specific:

\[
\boxed{
\text{PF-106 exact shift displacement}
+\text{PF-004 cross-ratio}
+\text{PF-158 Selberg sensitivity}
\Longrightarrow
\text{one-ended }1/4\text{ term}
+\text{connected remainder holomorphic on }Re\,s>0.
}
\tag{48}
\]

It should be read as a structural negative about the PF-158 boundary, not as a new general theorem about Selberg zeta functions.

## 8. Stress tests and falsification boundary

A later adversary can audit the result through the following finite chain:

1. verify PF-106's `d(x)=O(x^-2)` and `d'(x)=O(x^-3)` bounds;
2. derive the exact factorization (17) directly from the four interval increments;
3. check `R_a=1+O(a^-3)` and the exact fixed-left limit (9);
4. in the far regime `c>=4a`, verify the lower bounds (20) and derive the three relative estimates (21)--(24);
5. take logarithms to obtain (25), then use (26) for the connected length bound (27);
6. for near spans, combine PF-109 with (18) and the short/long local Selberg estimates to obtain (32)--(33);
7. for far spans, insert (27) into PF-158's long-length sensitivity and reproduce the dyadic bounds (40)--(42); the crucial exponent must be `R^(-4rho)`, not `R^(1-4rho)`;
8. verify that the finite set of small left labels still has convergent right tails for every `rho>0`;
9. subtract the absolutely convergent fixed-left connected series from PF-158's divergent fixed-left series to establish sharpness of the one-ended term;
10. keep the distinction between the diagnostic counterterm `\widehat L` and the length spectrum of an actual auxiliary surface.

The result would be false if the residual factor in (17) failed to gain the `1/c` decay, if the dyadic prime-gap moment required `rho>1/4`, or if PF-158's fixed-left sharpness did not survive subtraction. None of those failures occurs under the displayed estimates.

No claim is made about `Re s<=0`, analytic or meromorphic continuation across the imaginary axis, noncanonical primitive words, the full relative Selberg/Ruelle product, cusp/parabolic terms, the global Laplacian scattering determinant, resonances, or Riemann zeros.

## Research consequence

PF-158 removed the entire canonical consecutive-block family as a source of matched relative zeros on the RH line but left a sharp `1/4` convergence wall that could still look like a nontrivial collective feature of the exact prime/clone tail. PF-159 removes that interpretation:

\[
\boxed{
\text{the }1/4\text{ wall is one-ended long-channel propagation,}
\qquad
\text{the connected canonical interaction is regular on }Re\,s>0.
}
\]

Thus no RH-relevant significance should be assigned to the canonical-sector quarter abscissa. Any surviving Selberg/scattering mechanism must come from genuinely noncanonical primitive-word coupling, a justified full operator/scattering construction, or other global data not reducible to the one-ended response isolated here.