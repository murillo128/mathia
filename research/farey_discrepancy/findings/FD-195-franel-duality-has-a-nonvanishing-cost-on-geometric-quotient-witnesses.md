# FD-195 — Franel duality has a nonvanishing cost on geometric quotient witnesses

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** Franel-native stability / moving-coordinate GCD duality / norm boundary / geometric-schedule obstruction
- **Depends on:** FD-002, FD-003, FD-117, FD-193, FD-194
- **Classification:** `EXACT-DERIVED + SHARP-MOVING-COORDINATE-DUALITY + NORM-BOUNDARY + NEGATIVE/ROUTE-RESTRICTION`

## Claim

`FD-194` proves that the exact geometric square-root Fourier inverse is unusually well conditioned when the data error is measured in the raw signed-Fourier `l^infinity` norm: the inverse row recovering a cumulative coordinate has norm `2^{omega(k)}/k=n^{-1+o(1)}` along the canonical witnesses. That tail contraction is **not** present in the quadratic norm supplied by the classical Franel statistic.

Let

\[
m_d:=\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\qquad 1\le d\le N,
\tag{1}
\]

and let

\[
K_N(d,e):=\frac{\gcd(d,e)^2}{de}.
\tag{2}
\]

`FD-003` gives the exact Franel--Mertens energy identity

\[
\boxed{
 m^T K_Nm
 =12\left(L_N\mathfrak F_N+\frac1{12}\right),
}
\tag{3}
\]

where `L_N=sum_(q<=N) phi(q)` is the Farey endpoint scale used in `FD-002` and `mathfrak F_N` is the classical quadratic rank discrepancy.

For **every** coordinate `1<=d<=N`, not only the first coordinate treated in `FD-003`, the sharp unrestricted Hilbert-space extraction constant is

\[
\boxed{
C_{N,d}:=(K_N^{-1})_{d,d}
=d^2\sum_{m\le N/d}\frac{\mu(m)^2}{J_2(dm)}.
}
\tag{4}
\]

Thus every real vector `v in R^N` satisfies the sharp inequality

\[
\boxed{
v_d^2\le C_{N,d}\,v^TK_Nv,
}
\tag{5}
\]

with equality on a nonzero multiple of `K_N^{-1}e_d`. For the physical Mertens staircase this gives

\[
\boxed{
\left|\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right)\right|^2
\le
12C_{N,d}\left(L_N\mathfrak F_N+\frac1{12}\right).
}
\tag{6}
\]

The moving-coordinate constant has an explicit infinite-volume limit:

\[
\boxed{
C_{\infty,d}
:=d^2\sum_{m\ge1}\frac{\mu(m)^2}{J_2(dm)}
=\zeta(2)\prod_{p\mid d}\left(1+\frac1{p^2}\right).
}
\tag{7}
\]

Moreover the truncation is uniformly controlled by

\[
\boxed{
0\le C_{\infty,d}-C_{N,d}
\le \zeta(2)\frac dN.
}
\tag{8}
\]

Consequently, whenever `N/d -> infinity`,

\[
C_{N,d}
=\zeta(2)\prod_{p\mid d}(1+p^{-2})+o(1),
\tag{9}
\]

uniformly even when `d=d(N)` moves. Since

\[
1\le\prod_{p\mid d}(1+p^{-2})
\le\prod_p(1+p^{-2})
=\frac{\zeta(2)}{\zeta(4)}
=\frac{15}{\pi^2},
\tag{10}
\]

the sharp dual cost approaches a quantity between `zeta(2)` and `5/2`; it does **not** tend to zero as the recovered quotient moves deeper into the source.

For the canonical geometric recovery witnesses `(H_n,k_n)` of `FD-193`,

\[
\left\lfloor\frac{H_n}{k_n}\right\rfloor=n,
\qquad
H_n/k_n\in[n,n+1),
\tag{11}
\]

so (8) sharpens to

\[
\boxed{
C_{H_n,k_n}
=
\zeta(2)\prod_{p\mid k_n}(1+p^{-2})
+O(1/n).
}
\tag{12}
\]

This is the exact norm contrast with `FD-194`: the raw-Fourier `l^infinity` inverse row contracts like `n^{-1+o(1)}`, while the sharp Franel/GCD-energy dual row remains `Theta(1)`.

The distinction is not cosmetic. It identifies the scalar Franel norm as a genuine normalization boundary for the sparse geometric recovery program. The square-root signed band still recovers the source exactly and stably in its native coordinates, but generic quadratic duality of the **classical Franel energy** gives no improving tail factor on those same recovered coordinates.

## 1. The diagonal of the inverse GCD matrix gives every coordinate constant

`FD-003` factors the normalized square-GCD matrix as

\[
K_N=D^{-1}E^TJE D^{-1},
\tag{13}
\]

where `D=diag(1,...,N)`, `J=diag(J_2(1),...,J_2(N))`, and

\[
E_{r,s}=\mathbf 1_{r\mid s}.
\tag{14}
\]

The inverse divisor-incidence matrix is

\[
(E^{-1})_{r,s}
=\mu(s/r)\mathbf 1_{r\mid s}.
\tag{15}
\]

Hence

\[
K_N^{-1}
=D E^{-1}J^{-1}(E^{-1})^TD.
\tag{16}
\]

Taking the `d`-th diagonal entry yields

\[
\begin{aligned}
(K_N^{-1})_{d,d}
&=d^2\sum_{\substack{r\le N\\d\mid r}}
\frac{\mu(r/d)^2}{J_2(r)}\\
&=d^2\sum_{m\le N/d}
\frac{\mu(m)^2}{J_2(dm)},
\end{aligned}
\tag{17}
\]

which is (4). The coordinate functional `v -> v_d` has squared dual norm `(K_N^{-1})_{d,d}` in the `K_N` inner product, so (5) is immediate and is sharp for unrestricted real vectors.

The first-coordinate specialization `d=1` is exactly the constant `C_N` isolated in `FD-003`. The new point is to keep `d` moving with the quotient coordinate that the geometric Farey sampler is trying to recover.

As always, sharpness here is a statement about the unrestricted GCD quadratic form. The equality vector need not be a physical Mertens staircase. Equation (6) is therefore a rigorous physical upper bound, while the sharpness statement is a route boundary for generic quadratic geometry rather than an arithmetic extremizer claim.

## 2. The moving-coordinate limit is an elementary Euler product

Because `mu(m)^2` restricts `m` to squarefree integers and

\[
J_2(t)=t^2\prod_{p\mid t}(1-p^{-2}),
\tag{18}
\]

the infinite sum in (7) factors prime by prime. A prime `p` not dividing `d` contributes

\[
1+\frac1{p^2-1}
=\frac1{1-p^{-2}},
\tag{19}
\]

while a prime already dividing `d` contributes the same base Jordan factor together with the two squarefree choices for whether `p` also divides `m`. Relative to the generic Euler factor this leaves an extra factor `1+p^{-2}`. Therefore

\[
C_{\infty,d}
=\prod_p(1-p^{-2})^{-1}
\prod_{p\mid d}(1+p^{-2})
=\zeta(2)\prod_{p\mid d}(1+p^{-2}),
\tag{20}
\]

proving (7).

The convergence is uniform enough for moving `d`. Since

\[
J_2(dm)
\ge\frac{d^2m^2}{\zeta(2)},
\tag{21}
\]

every omitted term is at most `zeta(2)/m^2`. Hence

\[
0\le C_{\infty,d}-C_{N,d}
\le\zeta(2)
\sum_{m>N/d}\frac1{m^2}
\le\zeta(2)\frac dN,
\tag{22}
\]

which proves (8).

Finally,

\[
\prod_p(1+p^{-2})
=\frac{\zeta(2)}{\zeta(4)},
\tag{23}
\]

so

\[
\zeta(2)
\le C_{\infty,d}
\le
\frac{\zeta(2)^2}{\zeta(4)}
=\frac52.
\tag{24}
\]

The upper endpoint need not be attained by any finite `d`; it is the supremum approached as `d` accumulates more small prime factors. What matters for the present boundary is that the entire interval stays at constant scale.

## 3. The direct Fourier-row bound is asymptotically the sharp full-energy bound

There is a useful consistency check with `FD-117/194`. Put

\[
\mathcal B_N(k)
:=\sum_{\substack{e\mid k\\e\le N}}
 e\,m_e.
\tag{25}
\]

For `d<=N`, divisor Möbius inversion gives

\[
m_d
=\frac1d
\sum_{e\mid d}\mu(d/e)\mathcal B_N(e).
\tag{26}
\]

The full Franel spectral norm from `FD-002` is

\[
S_N
:=\sum_{k\ge1}\frac{|\mathcal B_N(k)|^2}{k^2}
=\zeta(2)\,m^TK_Nm.
\tag{27}
\]

Applying weighted Cauchy--Schwarz directly to (26) gives

\[
|m_d|^2
\le
\left(
\sum_{e\mid d}\mu(d/e)^2\frac{e^2}{d^2}
\right)S_N.
\tag{28}
\]

The row factor is exactly

\[
\sum_{e\mid d}\mu(d/e)^2\frac{e^2}{d^2}
=
\prod_{p\mid d}(1+p^{-2}).
\tag{29}
\]

Combining (27)--(29) therefore yields the generic constant

\[
\zeta(2)\prod_{p\mid d}(1+p^{-2})
=C_{\infty,d}.
\tag{30}
\]

Equation (8) now has a sharper interpretation. The complete finite source relation encoded by the full GCD matrix improves the naive divisor-row Cauchy constant from `C_(infinity,d)` to the exact optimum `C_(N,d)`, but the entire improvement is at most `zeta(2)d/N`. Along a geometric square-root witness `d=k_n` with `N/d asymp n`, that gain is only `O(1/n)`.

So the loss of tail contraction is not caused by throwing away the nonskeleton Fourier frequencies in the proof. Generic use of the **whole** Franel quadratic geometry asymptotically gives the same constant-scale tariff.

## 4. Consequence for sparse geometric Franel control

For the physical Farey sequence, combine (6) with the canonical witness of `FD-193`:

\[
\boxed{
|\mathbf M(n)|^2
\le
12C_{H_n,k_n}
\left(L_{H_n}\mathfrak F_{H_n}+\frac1{12}\right),
}
\tag{31}
\]

where `H_n` is the least geometric horizon `B^m>=n(n+1)` and `k_n` is the corresponding exact quotient witness. The coefficient in front of the Franel energy is asymptotically bounded between `12 zeta(2)=2 pi^2` and `30`, with no decaying factor in `n`.

This exposes a scale mismatch. The classical RH-equivalent Franel scale is

\[
\mathfrak F_H=O_\varepsilon(H^{-1+\varepsilon}),
\tag{32}
\]

while `L_H=Theta(H^2)`. Hence its associated energy scale is

\[
L_H\mathfrak F_H=O_\varepsilon(H^{1+\varepsilon}).
\tag{33}
\]

At the geometric recovery horizon `H_n=Theta_B(n^2)`, the generic bound (31) gives only

\[
|\mathbf M(n)|
=O_\varepsilon(n^{1+\varepsilon}),
\tag{34}
\]

which does not improve the trivial power scale. To force the RH-facing Mertens scale `M(n)=O_epsilon(n^(1/2+epsilon))` through this same one-horizon quadratic-duality route, one would instead need roughly

\[
L_{H_n}\mathfrak F_{H_n}
=O_\varepsilon(H_n^{1/2+\varepsilon}),
\tag{35}
\]

or equivalently

\[
\mathfrak F_{H_n}
=O_\varepsilon(H_n^{-3/2+\varepsilon}),
\tag{36}
\]

which is far stronger than the classical RH-equivalent exponent.

This is **not** a theorem that Franel information on geometric horizons can never imply RH. Equations (31)--(36) rule out only the direct route that first compresses each horizon to its scalar quadratic Franel energy and then uses generic GCD/Fourier Hilbert-space duality coordinate by coordinate. Arithmetic restrictions on the physical staircase, cross-horizon coherence, or a relation-sensitive Farey statistic could still beat this scale mismatch.

The distinction from the ordinary `d=1` Franel--Landau criterion is important. At horizon `N=n`, the first Fourier coordinate is already `M(n)`, so the classical RH scale transfers correctly. The quadratic loss appears when a **sparse geometric horizon schedule** has to recover an arbitrary `n` as a deep quotient at a horizon of order `n^2`.

## Representation audit

No observation has been strengthened. Equations (3), (13)--(16), and (25)--(27) are the exact Franel/GCD/Fourier representations already established in `FD-002`, `FD-003`, and `FD-117`. The new calculation asks for the dual norm of a moving quotient coordinate inside that same quadratic geometry and then evaluates it on the geometric witnesses of `FD-193`.

The comparison with `FD-194` is norm-specific and deliberate. Raw signed-Fourier sup error assigns the same absolute budget to every mode and yields row norm `2^{omega(d)}/d`; classical Franel energy assigns the spectral weight `1/k^2`, so its dual row weights acquire the compensating factor `e/d`, producing the Euler product (29). Nothing contradictory occurs: the two norms encode different notions of small Fourier error.

The generic sharpness assertion applies to arbitrary real divisor-scale vectors. It does not claim that the actual Mertens staircase realizes the extremizing vector, and therefore does not convert the route obstruction into a lower bound for physical Farey discrepancy.

## Prior-art and novelty boundary

Smith/meet/GCD matrix factorization and inverse formulas are classical. The line already anchors H. J. S. Smith's determinant theorem and Haukkanen--Wang--Sillanpaa's generalized Smith-matrix work in `SOURCES.md`; `FD-003` derives the exact factorization needed here. A targeted literature search also returned the later meet-matrix inverse literature of Korkee and Haukkanen. No novelty is claimed for incidence inversion, the diagonal formula (17) as matrix algebra, or the Euler-product manipulation in isolation.

The Mathia-specific delta is the moving-coordinate splice: compute the exact dual constant for `M(floor(N/d))`, prove its uniform moving-`d` limit (7)--(8), identify the direct Fourier-row constant as that same limit, and then evaluate it on the exact square-root geometric witnesses from `FD-193/194`. This isolates precisely why the tail contraction of the raw-Fourier inverse disappears in the RH-native Franel quadratic norm.

No new external theorem is load-bearing. The required GCD-matrix prior-art boundary is already durable in `SOURCES.md`, so no source-ledger update is needed.

## Formalization disposition

The finite identity (4) and sharp duality (5) are exact, but the new proof surface is a direct moving-coordinate specialization of the already known Smith/Jordan factorization from `FD-003`, followed by an elementary Euler product. It does not currently expose a new combinatorial interface or unresolved finite theorem whose formalization would unlock a broader family of results. No formalization issue is opened in this pass.

## Research consequence

`FD-194` removed one possible obstruction to the signed geometric Fourier program: exact root-band recovery is not badly conditioned in the native raw-coefficient sup norm. `FD-195` identifies the complementary warning. **The classical Franel norm does not inherit the inverse's tail contraction.** Its exact sharp generic moving-coordinate cost remains constant, and the complete GCD energy improves the immediate Fourier-row bound by only `O(d/N)`.

For the root-band witnesses this means the source is algebraically recoverable with only linear total signed data, yet a scalar RH-scale Franel bound at the required quadratic horizon is too weak by a full source power for direct pointwise Mertens recovery. The next useful bridge must therefore exploit information discarded by same-horizon scalar quadratic compression: cross-horizon coherence, arithmetic compatibility between quotient coordinates, or a genuinely relation-sensitive Farey statistic. Widening the signed band or refining generic Hilbert-space conditioning will not repair this particular scale mismatch.