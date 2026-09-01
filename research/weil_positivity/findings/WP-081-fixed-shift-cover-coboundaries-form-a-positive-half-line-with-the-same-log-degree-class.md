# WP-081 — Fixed-shift cover coboundaries form a positive half-line with the same log-degree class

## Claim

Continue the pointed Hardy cover geometry of `WP-073`--`WP-080`. Let

\[
H=\ell^2(\mathbb N_0),\qquad Le_k=(k+\tfrac12)e_k,
\]

and let the normalized degree-`n` cover isometry and its positive transfer be

\[
W_ne_k=\frac1{\sqrt n}\sum_{r=0}^{n-1}e_{nk+r},
\qquad
\rho_n(X)=nW_n^*XW_n.
\]

For a real fixed shift

\[
c>-\frac12,
\qquad
B_c:=(L+cI)^{-1},
\]

define the **fixed-shift cover coboundary**

\[
\boxed{
D_{n,c}:=(\rho_n-I)B_c
= nW_n^*(L+cI)^{-1}W_n-(L+cI)^{-1}.
}
\tag{1}
\]

This family has four exact properties.

1. For every `n>1` and every real `c>-1/2`,
   \[
   D_{n,c}\in S_1(H),
   \qquad
   \boxed{\operatorname{Tr}D_{n,c}=\log n.}
   \tag{2}
   \]
2. Positivity has a sharp threshold:
   \[
   \boxed{
   D_{n,c}\succ0\ \text{for every }n>1
   \iff c\ge0.
   }
   \tag{3}
   \]
   For `-1/2<c<0`, the diagonal of `D_{n,c}` is eventually negative, although its total trace remains `log n>0`.
3. The family is a semigroup `1`-cocycle,
   \[
   \boxed{
   D_{mn,c}=\rho_n(D_{m,c})+D_{n,c},
   }
   \tag{4}
   \]
   and its elementary cross-degree curvature vanishes identically:
   \[
   (\rho_m-I)D_{n,c}-(\rho_n-I)D_{m,c}=0.
   \tag{5}
   \]
   On the diagonal trace-class coefficient module, all shifts `c>-1/2` determine the **same nontrivial cocycle class**: their differences are trace-class coboundaries, while ordinary trace detects the common class by `log n`.
4. For every `c\ge0`, Möbius primitive extraction retains the same positive prime-power mechanism as `WP-078`. If
   \[
   M_{n,c}:=\sum_{d\mid n}\mu(d)D_{n/d,c},
   \tag{6}
   \]
   then
   \[
   \operatorname{Tr}M_{n,c}=\Lambda(n),
   \tag{7}
   \]
   and for every prime power,
   \[
   \boxed{
   M_{p^k,c}=\rho_{p^{k-1}}(D_{p,c})\succeq0,
   \qquad
   \operatorname{Tr}M_{p^k,c}=\log p.
   }
   \tag{8}
   \]
   The cover overlap `p^{-k/2}` is independent of `c`, so the finite scalar coefficient `(log p)p^{-k/2}` survives throughout the whole positive half-line `c\ge0`.

Thus the exact positive finite-place mechanism does **not** by itself distinguish the Riemann half-integer origin `L=N+1/2` from the non-covariant shifted origins `L+c`. What distinguishes `c=0` is the stronger scale-covariance theorem

\[
W_n^*LW_n=nL,
\tag{9}
\]

which fails for every `c\ne0`. Consequently, passing from the pointed-cover geometry to its natural positive log-degree cocycle or to its diagonal trace-class cohomology loses precisely the representative-level datum that singles out the Riemann half shift.

**Evidence status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + MATCHED-CONTROL`.

## 1. Exact diagonal formula

Write

\[
a=\frac12+c>0.
\]

Since `B_c` is diagonal and

\[
\rho_n(\operatorname{diag}(x_j))e_k
=
\left(\sum_{r=0}^{n-1}x_{nk+r}\right)e_k,
\]

we obtain

\[
D_{n,c}e_k=d_{n,c}(k)e_k,
\]

where

\[
\boxed{
 d_{n,c}(k)
 =
 \sum_{r=0}^{n-1}\frac1{nk+r+a}
 -\frac1{k+a}.
}
\tag{10}
\]

Equivalently,

\[
d_{n,c}(k)
=
\frac1n\sum_{r=0}^{n-1}
\frac1{k+(r+a)/n}
-
\frac1{k+a}.
\tag{11}
\]

A large-`k` expansion gives

\[
\boxed{
 d_{n,c}(k)
 =
 \frac{n-1}{n}\frac{c}{k^2}
 +O_{n,c}(k^{-3}).
}
\tag{12}
\]

In particular `D_{n,c}` is trace class for every fixed admissible `c`. At the covariant point `c=0`, the `k^{-2}` coefficient vanishes, recovering the faster decay of the positive defect `Q_n=D_{n,0}` from `WP-074`.

## 2. The trace stays exactly `log n` for every fixed shift

The finite partial trace telescopes without any analytic continuation:

\[
\begin{aligned}
\sum_{k=0}^{K-1}d_{n,c}(k)
&=
\sum_{j=0}^{nK-1}\frac1{j+a}
-
\sum_{k=0}^{K-1}\frac1{k+a}\\
&=
\psi(nK+a)-\psi(K+a).
\end{aligned}
\tag{13}
\]

Using the elementary asymptotic `psi(x)=log x+O(x^{-1})` as `x -> +infinity`,

\[
\operatorname{Tr}D_{n,c}
=
\lim_{K\to\infty}
[\psi(nK+a)-\psi(K+a)]
=
\log n.
\tag{14}
\]

The logarithmic degree is therefore insensitive to the fixed resolvent shift. This is already a matched-control warning: `log n` is forced by the asymptotic scaling of the harmonic ladder, not by the special value `a=1/2`.

## 3. Positivity holds exactly on the half-line `c>=0`

For (11), set

\[
x_r=k+\frac{r+a}{n}.
\]

Their mean is

\[
\frac1n\sum_{r=0}^{n-1}x_r
=
k+\frac12+\frac cn.
\tag{15}
\]

Because `x -> 1/x` is strictly convex on `(0,infinity)`, Jensen gives, for `n>1`,

\[
\frac1n\sum_{r=0}^{n-1}\frac1{x_r}
>
\frac1{k+1/2+c/n}.
\tag{16}
\]

If `c>=0`, then `c/n<=c`, hence

\[
\frac1{k+1/2+c/n}
\ge
\frac1{k+1/2+c}.
\tag{17}
\]

Combining (11), (16), and (17) yields

\[
d_{n,c}(k)>0
\qquad
(k\ge0,n>1,c\ge0),
\]

so `D_{n,c}` is strictly positive.

Conversely, if `-1/2<c<0`, the leading term in (12) is negative. Hence `d_{n,c}(k)<0` for all sufficiently large `k`, and `D_{n,c}` cannot be positive. This proves the sharp equivalence (3).

The positive object of `WP-074` is therefore not an isolated point: once exact scale covariance is forgotten, it lies at the endpoint of an entire positive half-line of fixed-shift coboundaries with exactly the same trace.

## 4. The fixed-shift family is a flat semigroup cocycle

The normalized covers satisfy `W_mW_n=W_{mn}`, so the transfers satisfy

\[
\rho_n\rho_m=\rho_{mn}.
\tag{18}
\]

Equation (1) then gives

\[
\begin{aligned}
D_{mn,c}
&=(\rho_{mn}-I)B_c\\
&=\rho_n[(\rho_m-I)B_c]+(\rho_n-I)B_c\\
&=\rho_n(D_{m,c})+D_{n,c}.
\end{aligned}
\tag{19}
\]

Since the multiplicative semigroup is commutative, applying one more difference immediately gives

\[
(\rho_m-I)D_{n,c}
=(\rho_n-I)D_{m,c},
\tag{20}
\]

which is (5). Thus the most direct higher interaction built by taking a cross-degree coboundary has zero curvature. Prime factorization may change the sequence of intermediate positive defects, but there is no irreducible two-prime residue in this canonical `1`-cocycle.

This is deliberately **not** a claim that all higher semigroup cohomology of the cover system vanishes. It rules out only the direct attempt to obtain new cross-prime geometry by taking further coboundaries of this fixed-shift positive cocycle.

## 5. All shifts define the same diagonal trace-class cocycle class

Let

\[
\mathfrak D_1
=
\{\operatorname{diag}(x_k):(x_k)\in\ell^1\}
\]

with the restricted action of the transfers `rho_n`. On this diagonal trace-class module, ordinary trace is invariant:

\[
\operatorname{Tr}\rho_n(A)=\operatorname{Tr}A.
\tag{21}
\]

The resolvent potentials themselves are not trace class:

\[
B_c\notin S_1,
\qquad
(B_c)_{kk}\sim\frac1k.
\tag{22}
\]

But for any two admissible shifts,

\[
\boxed{
B_c-B_0
=
-c(L+cI)^{-1}L^{-1}
\in\mathfrak D_1,
}
\tag{23}
\]

because its diagonal is `O(k^{-2})`. Therefore

\[
D_{n,c}-D_{n,0}
=(\rho_n-I)(B_c-B_0)
\tag{24}
\]

is an ordinary trace-class coboundary.

If a cocycle `D_{n,c}` itself were a coboundary `(rho_n-I)A` with `A in mathfrak D_1`, (21) would force

\[
\operatorname{Tr}D_{n,c}=0,
\]

contradicting (2) for `n>1`. Hence each `D_{.,c}` is nontrivial in the diagonal trace-class `H^1`, while (24) shows that **all admissible shifts represent the same class**. On this particular family, trace sees the common class only through the additive character

\[
n\longmapsto\log n.
\tag{25}
\]

The same cocycle becomes literally exact as soon as the coefficient module is enlarged enough to contain its potential `B_c`; for example `B_c` is compact and belongs to every Schatten class `S_p`, `p>1`. Thus this route has a sharp coefficient-module tradeoff:

```text
diagonal trace class:
    cocycle nontrivial, but every shift has the same log-degree class

larger standard ideals containing B_c:
    cocycle = (rho_n - I) B_c is exact
```

This narrows the `WP-080` higher-cohomology escape without asserting a general vanishing theorem: the canonical positive log-degree `1`-cocycle itself carries no shift-sensitive archimedean information.

## 6. Prime-power positivity survives every positive matched control

Apply Möbius primitive extraction to the fixed-shift cocycle as in (6). Taking traces and using (2),

\[
\operatorname{Tr}M_{n,c}
=
\sum_{d\mid n}\mu(d)\log(n/d)
=
\Lambda(n).
\tag{26}
\]

For a prime power only divisors `1,p` survive:

\[
M_{p^k,c}
=D_{p^k,c}-D_{p^{k-1},c}.
\tag{27}
\]

Using the cocycle law with `p^k=p^{k-1}p`,

\[
D_{p^k,c}
=\rho_{p^{k-1}}(D_{p,c})+D_{p^{k-1},c},
\]

hence (8). For every `c>=0`, positivity of `D_{p,c}` and positivity of `rho_{p^{k-1}}` make the primitive prime-power operator positive.

Moreover the pointed-cover overlap that supplies the critical half-weight is unchanged:

\[
\langle e_0,W_{p^k}e_0\rangle=p^{-k/2}.
\tag{28}
\]

Consequently the scalar readout

\[
\operatorname{Tr}(D_{p,c})
\langle e_0,W_{p^k}e_0\rangle
=
\frac{\log p}{p^{k/2}}
\tag{29}
\]

is identical for every `c>=0`.

This is stronger than merely observing that `log p` is universal. The **whole positive finite prime-ray package** presently available from the pointed-cover branch -- positive primitive defect, `log p`, and `p^{-k/2}` -- survives a continuum of non-Riemann fixed shifts.

## 7. Why this does not contradict `WP-075` and `WP-076`

Those findings study the reanchored shifted defect

\[
R_{n,c}
=
\rho_n(B_c)-B_{c/n},
\tag{30}
\]

whose trace is

\[
\operatorname{Tr}R_{n,c}
=
\log n
+
\psi(\tfrac12+c/n)
-
\psi(\tfrac12+c).
\tag{31}
\]

The present fixed-shift coboundary instead obeys

\[
\boxed{
D_{n,c}
=
R_{n,c}
+
(B_{c/n}-B_c).
}
\tag{32}
\]

For `c>0`, the second term is positive trace class, with

\[
\operatorname{Tr}(B_{c/n}-B_c)
=
\psi(\tfrac12+c)-\psi(\tfrac12+c/n),
\tag{33}
\]

so it cancels the endpoint digamma correction in (31) exactly and restores `log n`.

Thus `WP-075` remains correct: within the **reanchored** family `R_{n,c}`, exact finite trace singles out `c=0`. The new point is that if one instead uses the ordinary fixed-potential coboundary demanded by semigroup cohomology, exact trace no longer selects that point; a whole positive half-line appears.

## 8. Scale covariance is the surviving discriminator

Although the positive finite cocycle does not distinguish `c=0`, the underlying cover geometry does. From `WP-074`,

\[
W_n^*LW_n=nL.
\tag{34}
\]

For a shifted origin,

\[
W_n^*(L+cI)W_n=nL+cI,
\tag{35}
\]

whereas exact degree covariance would require

\[
n(L+cI)=nL+ncI.
\tag{36}
\]

For any `n>1`, (35) equals (36) if and only if

\[
\boxed{c=0.}
\tag{37}
\]

So the half-integer Hardy origin is still canonical, but its canonicity lives at the **representative/operator-covariance level**, not in the resulting positive `log n` cocycle class and not in the finite Mangoldt prime-ray scalar readout.

Any proposed global completion that passes only through the latter invariants has already discarded the datum that selects the Riemann representative.

## 9. Matched controls and adversarial audit

The controls `c>0` use exactly the same Hilbert space, cover isometries, positive transfers, multiplicative semigroup, and pointed overlaps as `c=0`. They differ only by translating the spectral origin of the resolvent potential. They therefore preserve:

- trace-class positive cover defects;
- exact `log n` traces;
- the semigroup cocycle law;
- positive prime-power Möbius primitives;
- exact `Lambda(n)` primitive traces;
- the critical overlap `p^{-k/2}`.

Yet they violate the unique affine scale covariance (34). This makes them strict matched controls for any claim that the positive cocycle or its primitive finite readout already contains enough geometry to force the Riemann archimedean completion.

Several attempted repairs are also eliminated internally.

- Taking one more semigroup difference produces zero curvature by (20), not a cross-prime interaction.
- Passing to diagonal trace-class cohomology retains only the common class (25), so it cannot recover the shift.
- Enlarging to the standard compact/Schatten coefficient modules containing `B_c` makes this cocycle exact rather than richer.
- Reanchoring the second endpoint to preserve covariance returns to `WP-075`--`WP-076`, where the digamma term is a telescoping scalar coboundary and exact finite weights force `c=0`.

None of these statements excludes a genuinely different coefficient system, a nontrivial derived object, a singular/non-Hausdorff quotient, or a nonseparable finite--archimedean coupling introduced before positivity.

## 10. Prior-art and novelty boundary

The normalized weighted-composition semigroup itself is classical prior art, already anchored in `SOURCES.md` through Noor and Manzur--Noor--Santos and identified in `WP-074`. Jensen convexity, the digamma telescoping identity, Schatten membership of a `1/k` resolvent ladder, and the definition of a semigroup coboundary are also standard ingredients. No novelty is claimed for any of them separately.

A directed audit around Hardy weighted-composition semigroups, resolvent/Jensen defects, semigroup cocycles, logarithmic trace defects, critical operator ideals, and singular-trace language did not identify an external theorem asserting the Mathia-specific classification proved here. The durable contribution is narrower: **within this exact pointed-cover representation, the canonical positive log-degree cocycle has a continuum of positive fixed-shift representatives whose diagonal trace-class cohomology class and positive prime-power Weil readout are identical, while only the stronger cover covariance selects the Riemann representative.**

This is an obstruction/classification result, not a claim of a new general cohomology theory or a global positivity mechanism.

## 11. Exact falsification surface

The finding is falsified if any of the following exact statements fail under the `WP-073`/`WP-074` normalization:

1. the diagonal formula (10);
2. the trace-class asymptotic (12);
3. the partial-trace identity (13) or the limit `Tr D_{n,c}=log n`;
4. positivity for every `c>=0`, or eventual negativity for any `-1/2<c<0`;
5. the semigroup cocycle law (19) or zero-curvature identity (20);
6. trace invariance on the diagonal trace-class module;
7. `B_c-B_0 in S_1` and hence the common cocycle-class identity (24);
8. the prime-power identity (8) or the primitive trace identity (26);
9. the fixed pointed overlap (28);
10. uniqueness of `c=0` in the affine covariance equation (35)--(37).

A construction using a genuinely different action or coefficient object and producing a nonzero finite--archimedean interaction before quotienting would not falsify this finding; it would exit its hypotheses and would be exactly the kind of new structure the research mandate still seeks.

## Research consequence

`WP-079` and `WP-080` showed that the most direct cover coinvariants either collapse positive diagonal information to ordinary trace or collapse the full trace ideal to zero. The natural next escape is to look one cohomological degree higher. `WP-081` shows that the first canonical candidate there is still too poor: the positive fixed-shift `1`-cocycles all have the same diagonal trace-class class, that class is detected only by `log degree`, and the cocycle becomes exact in standard larger operator ideals.

More importantly, the positive prime-power Mangoldt extraction and the critical `p^{-k/2}` overlap survive all `c>=0`. Therefore **finite positivity plus the correct prime-ray weights are not enough to transport the unique half-integer cover covariance into a global Weil sign theorem**. A viable continuation of this branch has to preserve or exploit representative-level covariance while creating a genuinely non-coboundary finite--archimedean interaction before the positivity readout.