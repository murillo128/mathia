# FD-034 — square-divisor modes force four-adic linear-prefix saturation gaps

**Status:** `EXACT-DERIVED + LINEAR-PRIME-BREADTH + SCHUR-PROJECTIVE-DEFECT + SQUARE-DIVISOR-RENORMALIZATION + FOUR-ADIC-CESARO-GAP + PHYSICAL-MERTENS-TAIL`.

`FD-031` reduces every fixed positive linear prime-prefix relaxation to a bounded synthetic head plus the physical Mertens tail, while `FD-032` and `FD-033` show that an absolute nonsquarefree support mismatch is real but can be diluted by the superlinear growth of the physical Schur energy. The live obstruction is therefore projective: can the physical tail become asymptotically parallel to the Schur equality direction?

There is still an unconditional multiscale obstruction. The equality direction has **exactly zero Jordan coordinates at every nonsquarefree index**, whereas the physical tail has the quotient-shell coordinates isolated in `FD-033`. Restricting the projective residual to rows divisible by `4` identifies a scaled copy of the same physical energy at horizon `floor(H/4)`. Consequently, for every fixed head dimension `D` and all sufficiently large `H`,

\[
\boxed{
\varepsilon_{H,D}
\ge
\frac34\,
\frac{E_{\lfloor H/4\rfloor,D}}{E_{H,D}},
}
\tag{1}
\]

where

\[
\varepsilon_{H,D}
:=
\frac{\rho_{H,D}^2}{E_{H,D}}
\in[0,1]
\tag{2}
\]

is the normalized transverse Schur residual of `FD-032`. Whenever `Delta_(H,D)>0`, this is exactly

\[
\varepsilon_{H,D}=\sin^2\theta_{H,D}
=\frac{\mathfrak D_{H,D}}{\Delta_{H,D}}.
\tag{3}
\]

The inequality can be iterated because the same fixed `D` reappears at the smaller horizon. A trivial quadratic upper bound for the physical energy then prevents the angle from collapsing on every member of a `4`-adic chain. If

\[
H_j=4^jH_0
\qquad(j\ge0)
\tag{4}
\]

with fixed `D` and sufficiently large `H_0`, then

\[
\boxed{
\liminf_{n\to\infty}
\left(
\prod_{j=1}^{n}\varepsilon_{H_j,D}
\right)^{1/n}
\ge\frac3{64},
}
\tag{5}
\]

and therefore, by arithmetic--geometric mean,

\[
\boxed{
\liminf_{n\to\infty}
\frac1n\sum_{j=1}^{n}\varepsilon_{H_j,D}
\ge\frac3{64}.
}
\tag{6}
\]

Thus the physical tail cannot even **Cesaro-saturate projectively** along a complete `4`-adic chain. Since `C_H -> Z:=zeta(2)` and `Delta_(H,D)=C_H-C_D`, the best relaxed quotient of `FD-031` obeys

\[
\boxed{
\limsup_{n\to\infty}
\frac1n\sum_{j=1}^{n}
\widehat R_{H_j,D}
\le
Z-\frac3{64}(Z-C_D).
}
\tag{7}
\]

The half-linear prime-prefix regime has `D=1` and `C_1=1`. Hence, on every `4`-adic chain, even if a **different admissible source is chosen independently at every horizon** and each source is constrained only through some cutoff `Y_j>=H_j/2`,

\[
\boxed{
\limsup_{n\to\infty}
\frac1n\sum_{j=1}^{n}R_{H_j}(a^{(j)})
\le
\zeta(2)-\frac3{64}\bigl(\zeta(2)-1\bigr)
=1.614702782\ldots .
}
\tag{8}
\]

This is a genuine linear-ancestry effect. `FD-018` shows that an unrestricted common real source can saturate pointwise on a fixed geometric chain with nonsquarefree ratio `q=4`; after half-linear prime ancestry freezes the Mertens tail, the same `4`-adic geometry instead forces a positive average gap. The result still does not give a pointwise gap at every horizon or an RH-critical exponent, but it removes the possibility that the normalized Schur escape of `FD-033` persists densely across one fixed multiplicative scale.

## 1. The longitudinal Schur coordinate is an exact finite Mertens transform

Retain the notation of `FD-031`--`FD-033`. Put

\[
w(r):=\frac{J_2(r)}{r^2},
\qquad
\mathcal H(X)
:=
\sum_{s\le X}
\frac{\mathbf M(\lfloor X/s\rfloor)}s,
\tag{9}
\]

so that the physical tail energy is exactly

\[
E_{H,D}
=
\sum_{r>D}
w(r)\,
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)^2.
\tag{10}
\]

There is also a useful exact formula for the longitudinal coordinate `beta` that was left implicit in `FD-031`. Let

\[
u^{(H)}:=K_H^{-1}e_1.
\tag{11}
\]

For its Jordan coordinates set

\[
z_r:=
\sum_{\substack{d\le H\\r\mid d}}
\frac{u_d^{(H)}}d.
\tag{12}
\]

The factorization `K_H=D^{-1}E^TJE D^{-1}` from `FD-003` and the equation `K_Hu=e_1` imply

\[
\sum_{r\mid d}J_2(r)z_r
=
\begin{cases}
1,&d=1,\\
0,&d>1.
\end{cases}
\tag{13}
\]

Möbius inversion therefore gives

\[
\boxed{
z_r=\frac{\mu(r)}{J_2(r)}.}
\tag{14}
\]

Block inversion in `FD-032` identifies the distinguished tail direction as

\[
t=S^{-1}w=-u^{(H)}_{D+1:H}.
\tag{15}
\]

For `r>D`, the head cannot affect the `r`th Jordan row. Hence the `r`th Jordan coordinate of `t` is exactly

\[
-\frac{\mu(r)}{J_2(r)}.
\tag{16}
\]

Pairing this with the physical coordinate

\[
\frac1r\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)
\tag{17}
\]

shows that

\[
\boxed{
\beta_{H,D}
=-\sum_{r>D}
\frac{\mu(r)}r
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right).
}
\tag{18}
\]

This sum itself collapses. `FD-033` writes

\[
\mathcal H(X)=\sum_{n\le X}c(n),
\qquad
\sum_{n\ge1}\frac{c(n)}{n^s}
=\frac{\zeta(s+1)}{\zeta(s)}.
\tag{19}
\]

The sequence `mu(r)/r` has Dirichlet series `1/zeta(s+1)`, so its Dirichlet convolution with `c` is exactly `mu`. Equivalently, regrouping the finite convolution directly gives

\[
\sum_{r\le H}
\frac{\mu(r)}r
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right)
=\mathbf M(H).
\tag{20}
\]

Thus

\[
\boxed{
\beta_{H,D}
=-\mathbf M(H)
+
\sum_{r\le D}
\frac{\mu(r)}r
\mathcal H\!\left(\left\lfloor\frac Hr\right\rfloor\right).
}
\tag{21}
\]

For fixed `D`, the apparently high-dimensional longitudinal projection is therefore only a fixed finite linear combination of the same quotient-shell summatory function together with `M(H)`. In the half-linear case `D=1`, this reduces to the transparent identity

\[
\boxed{
\beta_{H,1}=\mathcal H(H)-\mathbf M(H),
}
\tag{22}
\]

which is also immediate from `beta=r^Ty` in the `D=1` block notation of `FD-031`.

Equation (21) does not by itself bound the angle: its terms inherit the same critical zeta singularities that drive `FD-033`. Its value is that it makes the longitudinal channel exact before the transverse multiscale argument below.

## 2. Square-divisor Jordan rows contain a smaller copy of the physical energy

Define the squared projective residual as in `FD-032`,

\[
\rho_{H,D}^2
:=
\min_{c\in\mathbb R}
(y-ct)^TS(y-ct).
\tag{23}
\]

The row-deletion argument of `FD-033` applies to every tail vector, not only to `y`. Therefore the Schur norm in (23) is exactly the sum of Jordan rows `r>D`. At a nonsquarefree row, equation (16) vanishes identically. Such a row cannot be improved by choosing the scalar `c`.

Let `p` be any prime and put

\[
H':=\left\lfloor\frac{H}{p^2}\right\rfloor.
\tag{24}
\]

Restrict (23) to rows `r=p^2s` with `s>D`. All these rows are nonsquarefree, so their contribution is independent of `c`. Using (17),

\[
\rho_{H,D}^2
\ge
\sum_{s>D}
\frac{J_2(p^2s)}{p^4s^2}
\mathcal H\!\left(
\left\lfloor\frac{H}{p^2s}\right\rfloor
\right)^2.
\tag{25}
\]

The floor identity is exact:

\[
\left\lfloor\frac{H}{p^2s}\right\rfloor
=
\left\lfloor\frac{H'}s\right\rfloor.
\tag{26}
\]

Moreover

\[
w(p^2s)
=
\prod_{q\mid p^2s}(1-q^{-2})
\ge
(1-p^{-2})w(s),
\tag{27}
\]

with equality in the new factor when `p` does not already divide `s`. Hence, whenever `H'>D`,

\[
\boxed{
\rho_{H,D}^2
\ge
(1-p^{-2})E_{H',D}.
}
\tag{28}
\]

Dividing by `E_(H,D)>0` gives the scale-renormalization inequality

\[
\boxed{
\varepsilon_{H,D}
\ge
(1-p^{-2})
\frac{E_{\lfloor H/p^2\rfloor,D}}{E_{H,D}}.
}
\tag{29}
\]

The case `p=2` is (1). This strengthens the fixed terminal-block support mismatch in `FD-032`: every square-divisor family imports an entire lower-horizon physical energy into the transverse residual. The price is that the comparison is relative to the possibly much larger energy at the current horizon.

## 3. Energy growth cannot absorb the square-divisor residual at every geometric scale

To iterate (29), only a crude global upper bound is needed. From the definition of `mathcal H` and the trivial inequality `|M(x)|<=x`,

\[
\begin{aligned}
|\mathcal H(X)|
&\le
\sum_{s\le X}
\frac{\lfloor X/s\rfloor}s\\
&\le
X\sum_{s\ge1}\frac1{s^2}
=ZX.
\end{aligned}
\tag{30}
\]

Since `0<w(r)<=1`, equation (10) gives

\[
\boxed{
E_{H,D}
\le
Z^2H^2\sum_{r>D}\frac1{r^2}
\le Z^3H^2.
}
\tag{31}
\]

Now fix a prime `p`, an integer `D`, and a sufficiently large integer `H_0>D`. Set

\[
H_j=p^{2j}H_0,
\qquad
\varepsilon_j:=\varepsilon_{H_j,D},
\qquad
E_j:=E_{H_j,D}.
\tag{32}
\]

Equation (29) gives at every step

\[
\varepsilon_jE_j
\ge
(1-p^{-2})E_{j-1}.
\tag{33}
\]

Iteration yields

\[
\left(\prod_{j=1}^{n}\varepsilon_j\right)E_n
\ge
(1-p^{-2})^nE_0.
\tag{34}
\]

Using (31) and `H_n^2=p^{4n}H_0^2`,

\[
\prod_{j=1}^{n}\varepsilon_j
\ge
\frac{E_0}{Z^3H_0^2}
\left(
\frac{1-p^{-2}}{p^4}
\right)^n.
\tag{35}
\]

Therefore

\[
\boxed{
\liminf_{n\to\infty}
\left(
\prod_{j=1}^{n}\varepsilon_{H_j,D}
\right)^{1/n}
\ge
\frac{1-p^{-2}}{p^4}.
}
\tag{36}
\]

The right side is largest for `p=2`, giving `3/64`. Since every `epsilon_j` lies in `[0,1]`, arithmetic--geometric mean immediately gives (6). In particular,

\[
\boxed{
\limsup_{j\to\infty}\varepsilon_{4^jH_0,D}
\ge\frac3{64},
}
\tag{37}
\]

so projective alignment cannot hold on an entire `4`-adic tail.

There is also a quantitative sparsity statement for exceptionally small angles. From (35), for every fixed `0<eta<3/64`,

\[
\boxed{
\limsup_{n\to\infty}
\frac1n
\#\left\{1\le j\le n:
\varepsilon_{4^jH_0,D}\le\eta
\right\}
\le
\frac{\log(64/3)}{\log(1/\eta)}.
}
\tag{38}
\]

Thus arbitrarily good alignment may still occur on a sparse subsequence, but it cannot occupy asymptotic density one on the fixed `4`-adic scale.

## 4. A fixed Cesaro gap for half-linear prime ancestry

For fixed `D`, `FD-031` gives

\[
\widehat R_{H,D}
=C_H-\mathfrak D_{H,D},
\qquad
\mathfrak D_{H,D}
=\Delta_{H,D}\varepsilon_{H,D},
\tag{39}
\]

once `Delta_(H,D)>0`, with

\[
\Delta_{H,D}=C_H-C_D
\longrightarrow
Z-C_D>0.
\tag{40}
\]

Averaging (39) along `H_j=4^jH_0`, using `C_(H_j)->Z`, (40), and (6), gives (7):

\[
\limsup_{n\to\infty}
\frac1n\sum_{j=1}^{n}\widehat R_{H_j,D}
\le
Z-\frac3{64}(Z-C_D).
\tag{41}
\]

This is stronger than a statement about one common synthetic source. The upper bound `R_H(a)<=widehat R_(H,D)` is horizonwise. Therefore every sequence of independently chosen admissible sources with the same frozen-head dimension `D` inherits the same average obstruction.

If `H/2<=Y<H`, then

\[
D(H,Y)=\left\lfloor\frac{H}{Y+1}\right\rfloor=1.
\tag{42}
\]

Since `C_1=1`, (41) becomes

\[
\limsup_{n\to\infty}
\frac1n\sum_{j=1}^{n}R_{H_j}(a^{(j)})
\le
Z-\frac3{64}(Z-1)
=1.614702782\ldots,
\tag{43}
\]

for arbitrary admissible horizon-dependent sources whose prime-prefix ancestry reaches at least half the horizon at every `H_j`.

The contrast with `FD-018` is structurally useful. In the arbitrary-real-common-source relaxation, a fixed nonsquarefree dilation such as `4` is precisely an escape direction: old/new equality-ray collisions fall on zero coordinates, so one source can saturate all geometric horizons. Here those same zero coordinates become a liability after prime ancestry freezes the growing tail. Rows divisible by `4` cannot be tuned and instead reproduce the lower-scale physical energy inside the transverse defect. The linear ancestry constraint therefore reverses the role of the nonsquarefree dilation.

## 5. Scope, prior-art boundary, and falsification checks

The result is an obstruction, not an RH proof. It gives no pointwise lower bound for `epsilon_(H,D)` at every integer `H`; a sparse sequence of exceptionally aligned horizons remains possible. It gives no rate beyond the fixed-scale product inequality and does not improve the Franel--Landau exponent. The energy upper bound (31) is deliberately trivial, so the constant `3/64` should be read as a certified scale-average barrier, not an optimized constant.

The proof also does not contradict `FD-033`. That finding says `E_(H,D)/H -> infinity`, so the absolute distance lower bound of `FD-032` can be diluted at an individual scale. Equation (29) asks a different question: the amount that must be diluted is itself a copy of the physical energy at a smaller horizon. Persistent dilution would force energy growth faster than the elementary quadratic ceiling, which is impossible along a full fixed geometric chain.

A targeted prior-art audit covered Farey/Franel discrepancy with Mertens functions, normalized GCD matrices and Jordan-totient factorizations, Schur complements, and the quotient `zeta(s+1)/zeta(s)` from `FD-033`. The ingredients are classical and already anchored by `FD-003`, `FD-031`--`FD-033`; no external theorem is load-bearing here, so `SOURCES.md` needs no new entry. No novelty is claimed for GCD-matrix factorization, Möbius convolution, or Schur complements in isolation. The line-specific delta is the exact square-divisor renormalization (29) and its consequence (41) for the physical Mertens tail under linear prime ancestry.

The main failure checks are explicit. The factor in (27) is a lower bound, not an asserted equality when `p|s`; restricting to `s>D` is what allows the smaller energy to use the same fixed head dimension `D`; the floor identity (26) is exact; and the geometric iteration uses only horizons related by the exact integer factor `p^2`. Finally, (43) applies to the linear prime-prefix relaxation because `FD-031` already optimized away every remaining head constraint. It does not assert that arbitrary Farey/Mertens horizons have a uniform scalar gap, and it does not turn a Cesaro gap on one geometric chain into pointwise control of `M(H)`.