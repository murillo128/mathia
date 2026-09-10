# FD-024 — supermultiplicative horizons still saturate GCD duality under every fixed square-root-plus source envelope

**Status:** `EXACT-DERIVED + SOURCE-ENVELOPE-CONTROL + SUPERmultiplicative-HORIZONS + FULL-ASYMPTOTIC-SATURATION + NEGATIVE/OBSTRUCTION`.

`FD-017` shows that when successive sampled horizons become multiplicatively isolated, an unrestricted common real source can attain the full one-horizon GCD-duality constant `zeta(2)`. Its interpolation proof uses arbitrarily large stage amplitudes, so it leaves open whether a Mertens-like growth restriction on the common source itself destroys that sparse-horizon saturation. `FD-023` attacks the converse direction and proves that any polynomial-growth source whose normalized ratios saturate in Cesàro mean must use horizons whose logarithmic growth per retained scale diverges.

The growth envelope alone does not close the sparse side. Fix any

\[
\alpha>\frac12.
\]

For every increasing sequence of integer horizons

\[
H_0<H_1<H_2<\cdots,
\qquad
\frac{H_j}{H_{j-1}}\longrightarrow\infty,
\tag{1}
\]

there exists a **single real source** `A(1),A(2),...` satisfying

\[
\boxed{|A(n)|\le n^\alpha\qquad(n\ge1)}
\tag{2}
\]

such that, with

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
m_d^{(H)}=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\]

\[
E_H=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H=\frac{A(H)^2}{E_H},
\tag{3}
\]

one has

\[
\boxed{R_{H_j}\longrightarrow\zeta(2).}
\tag{4}
\]

Thus even an arbitrarily strong **fixed** power envelope strictly above the square-root exponent does not separate a sparse common source from the sharp GCD equality geometry. In particular, the trivial physical bound `|M(n)|<=n` is far more than is needed for this synthetic obstruction.

The source constructed here is not a Mertens function: no bounded-increment, squarefree-support, divisor, multiplicative-sign, or Möbius consistency condition is imposed. The result therefore sharpens the diagnostic boundary rather than producing an RH estimate. After `FD-023`, source growth can obstruct saturation only through how it interacts with horizon density; on supermultiplicatively separated scales, **endpoint growth by itself remains noncoercive all the way down to every fixed exponent above `1/2`.**

## 1. Equality-ray coordinates already obey a reciprocal envelope

Let

\[
Z:=\zeta(2),
\qquad
C_R:=(K_R^{-1})_{11},
\qquad
u^{(R)}:=K_R^{-1}e_1.
\tag{5}
\]

`FD-003` gives

\[
C_R\uparrow Z.
\tag{6}
\]

The inverse-column formula used in `FD-014` and `FD-022` is

\[
\nu_d^{(R)}
=d\sum_{\substack{k\le R\\d\mid k}}
\frac{\mu(k/d)\mu(k)}{J_2(k)}.
\tag{7}
\]

Since

\[
J_2(k)\ge \frac{k^2}{Z},
\]

putting `k=d ell` and discarding all signs gives the uniform bound

\[
\begin{aligned}
|\nu_d^{(R)}|
&\le dZ\sum_{\ell\ge1}\frac1{d^2\ell^2}\\
&=\frac{Z^2}{d}.
\end{aligned}
\tag{8}
\]

The unrestricted equality direction therefore already decays like `1/d`; no large coordinatewise growth is intrinsic to the extremizer.

For `alpha>1`, it is enough to construct the source below with exponent `1`, because `n<=n^alpha`. Hence assume from now on

\[
\frac12<\alpha\le1.
\tag{9}
\]

Write

\[
\rho_j:=\frac{H_j}{H_{j-1}},
\qquad
R_j:=\left\lfloor
\min\left\{\sqrt{H_j},\frac{\rho_j}{2}\right\}
\right\rfloor
\tag{10}
\]

on a sufficiently late tail. Both entries in the minimum tend to infinity, so

\[
R_j\longrightarrow\infty.
\tag{11}
\]

As in `FD-017`, `H_j>=R_j^2` makes the first `R_j` floor quotients

\[
x_{j,d}:=\left\lfloor\frac{H_j}{d}\right\rfloor,
\qquad1\le d\le R_j,
\tag{12}
\]

pairwise distinct, while `R_j<=rho_j/2` gives

\[
x_{j,R_j}>H_{j-1}.
\tag{13}
\]

Thus all these load-bearing source positions are fresh.

## 2. Plant the equality prefix without violating the power envelope

Set

\[
t_j:=\frac{H_j^\alpha}{2Z^2}.
\tag{14}
\]

Inductively assign

\[
A(x_{j,d})=t_j\nu_d^{(R_j)}
\qquad(1\le d\le R_j),
\tag{15}
\]

and set every other still-unassigned source value up to `H_j` equal to zero. Values assigned at earlier stages are never changed; (13) prevents collision with the new planted prefix. After the induction, set every never-assigned value to zero.

It remains to check (2). For every planted point, (8) gives

\[
|A(x_{j,d})|
\le \frac{H_j^\alpha}{2d}.
\tag{16}
\]

Because `d<=R_j<=sqrt(H_j)`, eventually `H_j/d>=2`, hence

\[
x_{j,d}\ge\frac{H_j}{2d}.
\tag{17}
\]

Using `1/2<alpha<=1` and `d>=1`,

\[
\frac{H_j^\alpha}{2d}
\le
\frac{H_j^\alpha}{2^\alpha d^\alpha}
\le x_{j,d}^\alpha.
\tag{18}
\]

Zeros satisfy the same bound, and earlier values retain the bound already verified when they were assigned. This proves the global envelope (2).

The point of the fixed scale (14) is that, unlike `FD-017`, no stage amplitude is allowed to tend to infinity independently of its source location. The equality prefix must dominate the inherited tail while remaining inside a prescribed power law.

## 3. A weighted GCD tail is small exactly above the square-root exponent

At horizon `H=H_j`, abbreviate `R=R_j`, `t=t_j`, `nu=nu^(R)`, and embed `nu` into the first `R` coordinates of `R^H` by zeros. The construction gives

\[
m^{(H)}=t\widetilde\nu+b,
\qquad
b_d=0\quad(d\le R).
\tag{19}
\]

For `d>R`, the sampled source value is inherited or zero, and the global envelope gives

\[
|b_d|
\le \left\lfloor\frac Hd\right\rfloor^\alpha
\le\left(\frac Hd\right)^\alpha.
\tag{20}
\]

Because `K_H` has nonnegative entries,

\[
b^TK_Hb
\le H^{2\alpha}S_\alpha(R),
\tag{21}
\]

where

\[
S_\alpha(R)
:=\sum_{d,e>R}
\frac{\gcd(d,e)^2}{d^{\alpha+1}e^{\alpha+1}}.
\tag{22}
\]

Use the exact Jordan identity

\[
\gcd(d,e)^2=\sum_{r\mid d,\,r\mid e}J_2(r).
\]

After writing `d=rk`, `e=r ell`,

\[
S_\alpha(R)
=
\sum_{r\ge1}
\frac{J_2(r)}{r^{2\alpha+2}}
\left(
\sum_{k>R/r}\frac1{k^{\alpha+1}}
\right)^2.
\tag{23}
\]

For `r<=R`, monotonicity and an integral tail bound give

\[
\sum_{k>R/r}k^{-\alpha-1}
\le \frac1\alpha\left(\frac rR\right)^\alpha.
\tag{24}
\]

Since `J_2(r)<=r^2`, the total contribution of `r<=R` is at most

\[
\frac1{\alpha^2}R^{1-2\alpha}.
\tag{25}
\]

For `r>R`, the inner sum is at most `zeta(alpha+1)`, so

\[
\sum_{r>R}
\frac{J_2(r)}{r^{2\alpha+2}}
\left(
\sum_{k\ge1}k^{-\alpha-1}
\right)^2
\le
\frac{\zeta(\alpha+1)^2}{2\alpha-1}
R^{1-2\alpha}.
\tag{26}
\]

Therefore

\[
\boxed{
S_\alpha(R)
\le
B_\alpha R^{1-2\alpha},
\qquad
B_\alpha:=
\frac1{\alpha^2}
+
\frac{\zeta(\alpha+1)^2}{2\alpha-1}.
}
\tag{27}
\]

This is the load-bearing estimate. It tends to zero precisely in the range used here, `alpha>1/2`. Consequently, with

\[
\beta:=b^TK_Hb,
\]

(14), (21), and (27) imply

\[
\frac{\beta}{t^2}
\le
4Z^4B_\alpha R^{1-2\alpha}
\longrightarrow0.
\tag{28}
\]

No operator-norm loss is needed; the GCD/Jordan structure controls the weighted inherited tail directly.

## 4. The planted prefix dominates and recovers the full constant

The top-left `R x R` block of `K_H` is exactly `K_R`, so

\[
(\widetilde\nu)^TK_H\widetilde\nu
=(\nu^{(R)})^TK_R\nu^{(R)}
=C_R.
\tag{29}
\]

Cauchy--Schwarz in the `K_H` inner product gives

\[
\left| (\widetilde\nu)^TK_Hb\right|
\le\sqrt{C_R\beta}
\le\sqrt{Z\beta}.
\tag{30}
\]

Combining (28)--(30),

\[
E_H
=t^2C_R
+2t(\widetilde\nu)^TK_Hb
+\beta
=t^2(C_R+o(1)).
\tag{31}
\]

Also, since `nu_1^(R)=C_R`,

\[
A(H)=tC_R.
\tag{32}
\]

Hence

\[
R_H
=
\frac{t^2C_R^2}{t^2(C_R+o(1))}
=C_R+o(1).
\tag{33}
\]

Finally `R=R_j->infinity` and (6) yield (4).

The construction works for arbitrary integer horizons satisfying (1); no integer-ratio relation, squarefree transition, or prescribed geometric progression is required.

## 5. Consequence for the Farey/Mertens route

`FD-023` shows that polynomial source growth rules out Cesàro saturation whenever the retained horizon hierarchy has bounded logarithmic growth per scale. The present result gives the complementary obstruction to pushing that argument using **growth alone**: once successive horizons separate multiplicatively, even the much smaller synthetic envelope

\[
|A(n)|\le n^{1/2+\varepsilon}
\]

for any one fixed `epsilon>0` remains compatible with pointwise saturation of the sharp GCD-duality constant.

This does not reproduce the RH-equivalent Mertens statement, which concerns the actual Möbius summatory function and requires the corresponding bound for every fixed positive `epsilon`. Here the source may depend on the chosen exponent and horizon schedule, and its increments are unconstrained.

The remaining source-specific leverage is therefore narrower than a mere endpoint-growth estimate. A successful sparse-horizon argument must exploit information such as bounded increments, the exact squarefree zero set and sign amplitudes, divisor identities across horizons, multiplicative sign correlation, or genuinely pre-cumulative Farey structure. Conversely, adding only a fixed `O(n^alpha)` envelope with `alpha>1/2` to the unrestricted common-source relaxation cannot close the supermultiplicative interpolation mechanism of `FD-017`.

## 6. Stress tests, prior-art boundary, and failure modes

The proof depends on four exact checks. First, the inverse-column bound (8) uses the correct `K_R^{-1}e_1` orientation and only the elementary inequality `J_2(k)>=k^2/Z`. Second, freshness (13) is what prevents later stages from overwriting earlier source data. Third, (20) applies to every inherited tail coordinate because the envelope is global, not merely a statement at sampled endpoints. Fourth, the exponent threshold enters through the convergent weighted GCD tail (23)--(27), not through a heuristic analogy with square-root cancellation.

The argument does **not** establish the endpoint `alpha=1/2`. At that exponent the bound (27) no longer decays, so this proof gives no saturation construction and no obstruction theorem. The threshold is therefore a boundary of the present tail estimate, not a claim that `1/2` is a sharp phase transition for all synthetic sources.

A targeted prior-art search covered GCD/Smith matrices, floor-quotient formulations of Mertens, sparse matrix representations of Mertens, and GCD-sum literature. Those sources concern static matrix structure, Möbius/floor-quotient identities, or other GCD extremal questions; no directly matching theorem about one common power-bounded source saturating the coordinate GCD-duality constant on prescribed supermultiplicative horizons was located. No novelty claim is inferred from search absence. The proof uses only the Smith/Jordan and local GCD-duality ingredients already anchored in `SOURCES.md`, so no new bibliographic dependency is required.

A decisive falsification would be a failure of one of the exact inequalities (8), (18), or (27), or a hidden collision showing that (13) does not keep the planted source locations fresh. The strongest conceptual counterargument is also explicit: the construction exploits complete freedom of the increments between planted source values. Any later theorem imposing genuine Möbius increment/divisor consistency lies outside this obstruction and could still produce a sparse-horizon deficit.

The durable conclusion is therefore limited but sharp for its relaxation: **for every fixed exponent strictly above one half, power-growth control on a common source does not improve the asymptotically sharp GCD coordinate constant along any prescribed horizon sequence with diverging successive multiplicative gaps.**