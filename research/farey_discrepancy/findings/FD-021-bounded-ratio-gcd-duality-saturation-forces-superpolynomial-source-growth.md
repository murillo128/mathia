# FD-021 — bounded-ratio GCD-duality saturation forces superpolynomial source growth

**Status:** `EXACT-DERIVED + SOURCE-GROWTH-OBSTRUCTION + BOUNDED-RATIO-NONSATURATION + MULTIHORIZON-BOUNDARY + NEGATIVE/OBSTRUCTION`.

`FD-018`--`FD-020` classify how far common-source coherence alone can obstruct the sharp GCD-duality constant. In particular, a bounded nonsquarefree dilation remains fully saturable in the unrestricted real-source model because inherited prefix collisions land on exact zero coordinates of the equality ray. That interpolation freedom disappears under an extremely weak additional source condition: **polynomial growth**.

Let

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
Z:=\zeta(2),
\tag{1}
\]

and for a real sequence `A(1),A(2),...` define

\[
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H:=\frac{A(H)^2}{E_H}
\tag{2}
\]

when the horizon vector is nonzero, with `R_H:=0` for the zero vector. As in `FD-003`,

\[
0\le R_H\le C_H:=(K_H^{-1})_{11}\le Z,
\qquad C_H\to Z.
\tag{3}
\]

Consider an integer-ratio horizon chain

\[
H_j=q_jH_{j-1},
\qquad 2\le q_j\le Q<\infty.
\tag{4}
\]

The new conclusion is:

\[
\boxed{
R_{H_j}\longrightarrow Z
\quad\Longrightarrow\quad
\frac{|A(H_j)|}{H_j^\alpha}\longrightarrow\infty
\text{ for every fixed }\alpha\ge0.
}
\tag{5}
\]

Thus every source that saturates the unrestricted dual constant on a bounded-ratio chain must have **superpolynomial endpoint growth**. Consequently no source satisfying

\[
|A(n)|\le Cn^\alpha
\tag{6}
\]

for any fixed finite `C,alpha` can have `R_(H_j)->Z` on such a chain.

There is also an explicit quantitative form on an eventually nonsquarefree chain. If (6) holds and all sufficiently late `q_j` are nonsquarefree, then

\[
\boxed{
\liminf_{j\to\infty}R_{H_j}
\le
\kappa_{\alpha,Q}
:=
\left(\frac1Z+\frac{Q^{-2\alpha}}{Z^2}\right)^{-1}
<Z.
}
\tag{7}
\]

For the physical Mertens source, the trivial bound `|M(n)|<=n` gives `alpha=1`. Hence a fixed nonsquarefree geometric chain `H_j=q^jH_0` obeys

\[
\liminf_j R_{H_j}
\le
\left(\frac1Z+\frac1{q^2Z^2}\right)^{-1}<Z.
\tag{8}
\]

For example, at `q=4` the right side is `1.5847218565...`, compared with `Z=1.6449340668...`. This is a genuine source-conditioned duality deficit in a regime where `FD-018` proves full saturation for unrestricted real sources.

## 1. Near saturation at a nonsquarefree transition forces explosive endpoint growth

Write

\[
u^{(H)}:=K_H^{-1}e_1,
\qquad
v^{(H)}:=\frac{u^{(H)}}{C_H}.
\tag{9}
\]

The inverse-column formula used in `FD-014` and `FD-018` is

\[
u_d^{(H)}
=d\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)\mu(k)}{J_2(k)}.
\tag{10}
\]

Therefore

\[
\boxed{v_d^{(H)}=0\quad\text{for every nonsquarefree }d,}
\tag{11}
\]

because every multiple `k` of such a `d` has `mu(k)=0`.

`FD-014` gives the exact stability identity around the equality ray. If `t=m_1=A(H)` and `R_H>0`, then

\[
\frac{\|m-tv^{(H)}\|_{K_H}^2}{t^2}
=
\frac1{R_H}-\frac1{C_H},
\tag{12}
\]

while coordinate evaluation satisfies

\[
(K_H^{-1})_{dd}
=d^2\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)^2}{J_2(k)}
\le Z^2.
\tag{13}
\]

Hence

\[
\left|\frac{m_d}{t}-v_d^{(H)}\right|
\le
Z\sqrt{\frac1{R_H}-\frac1{C_H}}
\le
Z\sqrt{\frac1{R_H}-\frac1Z}.
\tag{14}
\]

Now take one transition

\[
H_j=q_jH_{j-1}
\tag{15}
\]

with `q_j` nonsquarefree. Coordinate `d=q_j` at the new horizon is exactly the previous endpoint:

\[
m_{q_j}^{(H_j)}
=A\!\left(\frac{H_j}{q_j}\right)
=A(H_{j-1}).
\tag{16}
\]

At the same coordinate, (11) gives `v_(q_j)^(H_j)=0`. Substituting `d=q_j` into (14) therefore yields the load-bearing estimate

\[
\boxed{
\left|\frac{A(H_{j-1})}{A(H_j)}\right|
\le
Z\sqrt{\frac1{R_{H_j}}-\frac1{C_{H_j}}}
\le
Z\sqrt{\frac1{R_{H_j}}-\frac1Z}.
}
\tag{17}
\]

This turns the exact zero-coordinate mechanism of `FD-018` around. In the unrestricted interpolation proof, a nonsquarefree collision is harmless because the newly planted equality ray wants zero there and an arbitrarily large fresh amplitude can dominate the inherited value. Equation (17) quantifies the price: as `R_(H_j)` approaches `Z`, the new endpoint must dominate the inherited previous endpoint by an arbitrarily large factor.

## 2. Polynomial growth gives an explicit nonsaturation constant

Assume that all sufficiently late transitions are nonsquarefree, `q_j<=Q`, and that

\[
|A(n)|\le Cn^\alpha
\tag{18}
\]

for some fixed `C<infinity` and `alpha>=0`. Define `kappa_(alpha,Q)` by (7). Suppose for contradiction that

\[
\liminf_jR_{H_j}>\kappa_{\alpha,Q}.
\tag{19}
\]

Choose `r` strictly between the two sides. Since

\[
Z\sqrt{\frac1{\kappa_{\alpha,Q}}-\frac1Z}
=Q^{-\alpha},
\tag{20}
\]

we have

\[
\theta
:=Z\sqrt{\frac1r-\frac1Z}
<Q^{-\alpha}.
\tag{21}
\]

For all sufficiently large `j`, `R_(H_j)>=r`; these ratios are positive, so the relevant consecutive endpoint values are nonzero. Equation (17) gives

\[
|A(H_j)|\ge\theta^{-1}|A(H_{j-1})|.
\tag{22}
\]

Normalize by the allowed polynomial scale,

\[
B_j:=\frac{|A(H_j)|}{H_j^\alpha}.
\tag{23}
\]

Using `H_j=q_jH_(j-1)` and `q_j<=Q`,

\[
B_j
\ge
\frac1{\theta q_j^\alpha}B_{j-1}
\ge
\frac1{\theta Q^\alpha}B_{j-1}.
\tag{24}
\]

The last multiplier is a fixed number greater than one by (21). Thus `B_j` grows geometrically from a positive value, contradicting the uniform bound `B_j<=C` from (18). This proves (7).

The same argument without (18) proves a stronger necessary condition for actual saturation. If `R_(H_j)->Z`, then for any chosen `alpha>=0` select a fixed `r<Z` so close to `Z` that

\[
Z\sqrt{1/r-1/Z}<Q^{-\alpha}/2.
\tag{25}
\]

Eventually every `R_(H_j)>=r`, and (24) now gives `B_j>=2B_(j-1)`. Therefore

\[
\frac{|A(H_j)|}{H_j^\alpha}\to\infty.
\tag{26}
\]

This proves (5) once the horizon chain is eventually nonsquarefree.

## 3. Bounded integer-ratio saturation itself forces an eventually nonsquarefree tail

For a general bounded chain (4), `FD-019` supplies the complementary unrestricted classification. If `R_(H_j)->Z`, every bounded squarefree transition ratio must eventually disappear. Since all `q_j` already lie in the finite set `{2,...,Q}`, only finitely many transitions can then be squarefree. Thus every saturating bounded-ratio chain has an eventually nonsquarefree tail.

Applying Section 2 to that tail proves (5) for the full bounded-ratio setting. In particular:

\[
\boxed{
\text{bounded integer-ratio horizon chain}
+\text{ polynomial-growth source}
\Longrightarrow
R_{H_j}\not\to\zeta(2).
}
\tag{27}
\]

This closes the principal artificial escape left by `FD-018` and `FD-019`: fixed or bounded nonsquarefree transitions can still interpolate the equality rays only because the unrestricted source is allowed to choose amplitudes that eventually outrun every polynomial in the horizon.

## 4. Consequence for the physical Mertens staircase

For `A=M`, no analytic estimate is needed to enter the polynomial-growth class. Since every Möbius increment lies in `{-1,0,1}`,

\[
|M(n)|\le n.
\tag{28}
\]

Therefore the GCD-duality ratios of the physical Mertens staircase cannot converge to `Z` along **any** bounded integer-ratio chain. On an eventually nonsquarefree chain, (7) with `alpha=1` gives the explicit bound

\[
\boxed{
\liminf_jR_{H_j}
\le
\left(\frac1Z+\frac{Q^{-2}}{Z^2}\right)^{-1}.
}
\tag{29}
\]

For a fixed nonsquarefree dilation `q`, put `Q=q`. With the `FD-003` physical normalization

\[
E_H=12\left(M_H\mathfrak F_H+\frac1{12}\right),
\tag{30}
\]

(29) means that for every `epsilon>0`, infinitely many horizons in the geometric chain satisfy

\[
|M(H)|^2
\le
12\bigl(\kappa_{1,q}+\epsilon\bigr)
\left(M_H\mathfrak F_H+\frac1{12}\right).
\tag{31}
\]

At `q=4`, `12 kappa_(1,4)=19.0166622781...`, strictly below the unrestricted coefficient `12Z=2pi^2=19.7392088022...`.

This is a constant-level subsequential improvement only. It does not bound either `M(H)` or the Franel energy separately and therefore does not improve the RH-critical exponent.

## 5. Stress tests, prior art, and boundary

The proof uses only three established ingredients: the exact GCD equality ray and inverse diagonal from `FD-003`/`FD-014`, its exact zero on nonsquarefree coordinates from `FD-018`, and the bounded-transition consequence of the unrestricted classification `FD-019`. The new step is the source-growth comparison (17)--(24). No prime number theorem, zero-free region, probabilistic Möbius model, or unproved cancellation estimate enters it.

The zero cases are harmless. If `R_(H_j)->Z>0`, then the horizon endpoint `A(H_j)` is nonzero for all sufficiently large `j`, and hence so are the consecutive endpoints used in (17). Coordinate `q_j` is always valid because `q_j<=H_j`, and (16) has no floor error because `H_j/q_j=H_(j-1)` exactly.

A targeted prior-art search by the GCD-matrix equality geometry, Mertens floor-quotient matrices, geometric horizon chains, and polynomial-growth saturation did not locate an equivalent theorem. Jean-Paul Cardinal's work on symmetric matrices related to the Mertens function and Lagarias--Richman's floor-quotient partial order are neighboring matrix/floor-quotient prior art already audited in `FD-018`; neither is used as a theorem here. The Smith/Jordan GCD-matrix ingredients are already anchored in `SOURCES.md`. No broad novelty claim is made beyond the explicit consequence in the present Farey--Mertens duality framework.

Several boundaries remain. The quantitative constant (7) needs an eventually nonsquarefree bounded-ratio tail; if squarefree transitions recur, the separate collision obstruction of `FD-015`/`FD-019` applies instead. The theorem does not classify **Cesàro** saturation: a density-zero set of sacrificed horizons, as in `FD-020`, can reset amplitudes and is not controlled by the pointwise growth argument above. It also does not treat unbounded transition ratios, where no fixed `Q` converts (17) into geometric growth relative to every polynomial scale.

Most importantly, (27) is a nonsaturation theorem for the normalized dual ratio, not a Mertens estimate. It proves that one large class of artificial common-source extremizers is unavailable to the physical source, but it does not convert that obstruction into `M(x)=O(x^(1/2+epsilon))`, a Franel--Landau exponent, or RH. The live continuation is to determine whether the weak source restrictions available for Möbius values can produce a **scale-sensitive accumulated deficit** rather than only forcing a fixed or subsequential gap in the dual ratio.