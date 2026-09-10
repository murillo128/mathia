# FD-021 — bounded-ratio GCD-duality saturation forces superpolynomial source growth

**Status:** `EXACT-DERIVED + SOURCE-GROWTH-OBSTRUCTION + BOUNDED-RATIO-NONSATURATION + MIXED-TRANSITION-QUANTITATIVE-GAP + MULTIHORIZON-BOUNDARY + NEGATIVE/OBSTRUCTION`.

`FD-018`--`FD-020` classify how far common-source coherence alone can obstruct the sharp GCD-duality constant. In particular, a bounded nonsquarefree dilation remains fully saturable in the unrestricted real-source model because inherited prefix collisions land on exact zero coordinates of the equality ray. That interpolation freedom disappears under an extremely weak additional source condition: **polynomial growth**. Combining that source-growth obstruction with the squarefree collision theorem of `FD-015` also gives a uniform quantitative nonsaturation constant for **every** bounded integer-ratio chain, regardless of how squarefree and nonsquarefree transitions are mixed.

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

The first conclusion is the source-growth obstruction

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

There is an explicit quantitative form on an eventually nonsquarefree chain. If (6) holds and all sufficiently late `q_j` are nonsquarefree, then

\[
\boxed{
\liminf_{j\to\infty}R_{H_j}
\le
\kappa_{\alpha,Q}^{\rm ns}
:=
\left(\frac1Z+\frac{Q^{-2\alpha}}{Z^2}\right)^{-1}
<Z.
}
\tag{7}
\]

The mixed-chain strengthening removes the eventual nonsquarefree hypothesis. For squarefree `q`, let `p_-(q)` be its least prime factor and define

\[
B_Q:=
\max_{\substack{2\le q\le Q\\q\ \mathrm{squarefree}}}
q\,p_-(q),
\qquad
\eta_{\alpha,Q}:=
\min\left\{Q^{-\alpha},\frac{2}{5B_Q}\right\}.
\tag{8}
\]

Since `Q>=2`, the maximum is nonempty. Then every source satisfying (6) on every bounded chain (4) obeys

\[
\boxed{
\liminf_{j\to\infty}R_{H_j}
\le
\kappa_{\alpha,Q}^{\rm all}
:=
\left(
\frac1Z+\frac{\eta_{\alpha,Q}^2}{Z^2}
\right)^{-1}
<Z.
}
\tag{9}
\]

Because `B_Q<=Q^2`, the simpler but weaker consequence is

\[
\boxed{
\liminf_jR_{H_j}
\le
\left[
\frac1Z+
\frac{\min\{Q^{-2\alpha},\,4/(25Q^4)\}}{Z^2}
\right]^{-1}.
}
\tag{10}
\]

Thus bounded-ratio polynomial-growth sources do not merely fail to converge to the sharp constant: **some fixed deficit depending only on the growth exponent and the ratio ceiling must recur infinitely often.**

## 1. Near saturation at a nonsquarefree transition forces explosive endpoint growth

Write

\[
u^{(H)}:=K_H^{-1}e_1,
\qquad
v^{(H)}:=\frac{u^{(H)}}{C_H}.
\tag{11}
\]

The inverse-column formula used in `FD-014` and `FD-018` is

\[
u_d^{(H)}
=d\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)\mu(k)}{J_2(k)}.
\tag{12}
\]

Therefore

\[
\boxed{v_d^{(H)}=0\quad\text{for every nonsquarefree }d,}
\tag{13}
\]

because every multiple `k` of such a `d` has `mu(k)=0`.

`FD-014` gives the exact stability identity around the equality ray. If `t=m_1=A(H)` and `R_H>0`, then

\[
\frac{\|m-tv^{(H)}\|_{K_H}^2}{t^2}
=
\frac1{R_H}-\frac1{C_H},
\tag{14}
\]

while coordinate evaluation satisfies

\[
(K_H^{-1})_{dd}
=d^2\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)^2}{J_2(k)}
\le Z^2.
\tag{15}
\]

Hence

\[
\left|\frac{m_d}{t}-v_d^{(H)}_d\right|
\le
Z\sqrt{\frac1{R_H}-\frac1{C_H}}
\le
Z\sqrt{\frac1{R_H}-\frac1Z}.
\tag{16}
\]

Now take one transition

\[
H_j=q_jH_{j-1}
\tag{17}
\]

with `q_j` nonsquarefree. Coordinate `d=q_j` at the new horizon is exactly the previous endpoint:

\[
m_{q_j}^{(H_j)}
=A\!\left(\frac{H_j}{q_j}\right)
=A(H_{j-1}).
\tag{18}
\]

At the same coordinate, (13) gives `v_(q_j)^(H_j)=0`. Substituting `d=q_j` into (16) yields

\[
\boxed{
\left|\frac{A(H_{j-1})}{A(H_j)}\right|
\le
Z\sqrt{\frac1{R_{H_j}}-\frac1{C_{H_j}}}
\le
Z\sqrt{\frac1{R_{H_j}}-\frac1Z}.
}
\tag{19}
\]

This turns the exact zero-coordinate mechanism of `FD-018` around. In the unrestricted interpolation proof, a nonsquarefree collision is harmless because the newly planted equality ray wants zero there and an arbitrarily large fresh amplitude can dominate the inherited value. Equation (19) quantifies the price: as `R_(H_j)` approaches `Z`, the new endpoint must dominate the inherited previous endpoint by an arbitrarily large factor.

## 2. Polynomial growth gives an explicit nonsquarefree-tail gap

Assume that all sufficiently late transitions are nonsquarefree, `q_j<=Q`, and that (6) holds. Suppose for contradiction that

\[
\liminf_jR_{H_j}>\kappa_{\alpha,Q}^{\rm ns}.
\tag{20}
\]

Choose `r` strictly between the two sides. Since

\[
Z\sqrt{\frac1{\kappa_{\alpha,Q}^{\rm ns}}-\frac1Z}
=Q^{-\alpha},
\tag{21}
\]

we have

\[
\theta
:=Z\sqrt{\frac1r-\frac1Z}
<Q^{-\alpha}.
\tag{22}
\]

For all sufficiently large `j`, `R_(H_j)>=r`; these ratios are positive, so the relevant consecutive endpoint values are nonzero. Equation (19) gives

\[
|A(H_j)|\ge\theta^{-1}|A(H_{j-1})|.
\tag{23}
\]

Normalize by the allowed polynomial scale,

\[
D_j:=\frac{|A(H_j)|}{H_j^\alpha}.
\tag{24}
\]

Using `H_j=q_jH_(j-1)` and `q_j<=Q`,

\[
D_j
\ge
\frac1{\theta q_j^\alpha}D_{j-1}
\ge
\frac1{\theta Q^\alpha}D_{j-1}.
\tag{25}
\]

The last multiplier is a fixed number greater than one by (22). Thus `D_j` grows geometrically from a positive value, contradicting the uniform bound `D_j<=C` from (6). This proves (7).

The same argument without assuming (6) proves a stronger necessary condition for actual saturation on an eventually nonsquarefree tail. If `R_(H_j)->Z`, then for any chosen `alpha>=0` select a fixed `r<Z` so close to `Z` that

\[
Z\sqrt{1/r-1/Z}<Q^{-\alpha}/2.
\tag{26}
\]

Eventually every `R_(H_j)>=r`, and (25) now gives `D_j>=2D_(j-1)`. Therefore

\[
\frac{|A(H_j)|}{H_j^\alpha}\to\infty.
\tag{27}
\]

## 3. Squarefree recurrence and source growth combine into one mixed-chain gap

The quantitative all-chain bound (9) follows by an exact dichotomy on the transition schedule.

Suppose first that infinitely many `q_j` are squarefree. Because every `q_j` lies in the finite set `{2,...,Q}`, one fixed squarefree integer `q` occurs infinitely often. Let `p=p_-(q)`. The repeated-prime collision theorem `FD-015` gives, for every sufficiently late occurrence of that transition,

\[
\min\{R_{H_{j-1}},R_{H_j}\}
<
\kappa_{q,p}
:=
\left(
\frac1Z+\frac{4}{25p^2q^2Z^2}
\right)^{-1}.
\tag{28}
\]

The threshold `H_(j-1)>=400q^2` in `FD-015` is eventually automatic because the horizons tend to infinity. By definition `pq<=B_Q`, so

\[
\frac{2}{5pq}\ge\frac{2}{5B_Q}\ge\eta_{\alpha,Q}.
\tag{29}
\]

The map

\[
\epsilon\longmapsto
\left(\frac1Z+\frac{\epsilon^2}{Z^2}\right)^{-1}
\tag{30}
\]

is decreasing for positive `epsilon`. Hence

\[
\kappa_{q,p}
\le
\kappa_{\alpha,Q}^{\rm all}.
\tag{31}
\]

Infinitely many transition pairs therefore contain a horizon with `R_H<kappa_(alpha,Q)^all`. A fixed horizon can belong to at most two adjacent transition pairs, so these produce infinitely many distinct bad horizons and

\[
\liminf_jR_{H_j}\le\kappa_{\alpha,Q}^{\rm all}.
\tag{32}
\]

Suppose instead that only finitely many transitions are squarefree. The chain is then eventually nonsquarefree, so (7) gives

\[
\liminf_jR_{H_j}
\le
\kappa_{\alpha,Q}^{\rm ns}.
\tag{33}
\]

Because `eta_(alpha,Q)<=Q^(-alpha)`, monotonicity in (30) gives

\[
\kappa_{\alpha,Q}^{\rm ns}
\le
\kappa_{\alpha,Q}^{\rm all}.
\tag{34}
\]

Equations (32)--(34) prove (9) for every possible bounded transition schedule. Finally, `B_Q<=Q^2` gives

\[
\eta_{\alpha,Q}
\ge
\min\left\{Q^{-\alpha},\frac{2}{5Q^2}\right\},
\tag{35}
\]

which implies the coarser bound (10).

This combination is stronger than the previous qualitative use of `FD-019`. Squarefree recurrence and nonsquarefree source-growth failure are now two quantitative branches of the same bounded-chain alternative; no transition schedule can evade both when the source has polynomial growth.

## 4. Full saturation on a bounded chain forces superpolynomial growth

For a general bounded chain (4), `FD-019` supplies the complementary unrestricted classification. If `R_(H_j)->Z`, every bounded squarefree transition ratio must eventually disappear. Since all `q_j` already lie in the finite set `{2,...,Q}`, only finitely many transitions can then be squarefree. Thus every saturating bounded-ratio chain has an eventually nonsquarefree tail.

Applying (27) to that tail proves (5) for the full bounded-ratio setting. In particular,

\[
\boxed{
\text{bounded integer-ratio horizon chain}
+\text{ polynomial-growth source}
\Longrightarrow
R_{H_j}\not\to\zeta(2).
}
\tag{36}
\]

The stronger statement (9) shows that, under polynomial growth, the failure is quantitatively recurrent rather than merely qualitative.

## 5. Consequence for the physical Mertens staircase

For `A=M`, no analytic estimate is needed to enter the polynomial-growth class. Since every Möbius increment lies in `{-1,0,1}`,

\[
|M(n)|\le n.
\tag{37}
\]

Taking `alpha=1` in (9) gives an explicit mixed-chain theorem for the physical source:

\[
\boxed{
\liminf_jR_{H_j}
\le
\kappa_{1,Q}^{\rm all}
=
\left[
\frac1Z+
\frac{\min\{Q^{-2},\,4/(25B_Q^2)\}}{Z^2}
\right]^{-1}
<Z.
}
\tag{38}
\]

In particular, the completely schedule-free coarse form is

\[
\boxed{
\liminf_jR_{H_j}
\le
\left(
\frac1Z+\frac{4}{25Q^4Z^2}
\right)^{-1}
<Z
\qquad(A=M).
}
\tag{39}
\]

For `Q=4`, the squarefree transition set is `{2,3}`, so `B_4=max(2*2,3*3)=9`. Equation (38) gives

\[
\liminf_jR_{H_j}
\le 1.6429611273\ldots,
\qquad
12\kappa_{1,4}^{\rm all}=19.7155335288\ldots,
\tag{40}
\]

compared with `Z=1.6449340668...` and the unrestricted coefficient `12Z=2pi^2=19.7392088022...`.

If the chain is known to be eventually nonsquarefree, (7) remains much stronger. For a fixed nonsquarefree dilation `q`, putting `Q=q` gives

\[
\liminf_j R_{H_j}
\le
\left(\frac1Z+\frac1{q^2Z^2}\right)^{-1}.
\tag{41}
\]

With the `FD-003` physical normalization

\[
E_H=12\left(M_H\mathfrak F_H+\frac1{12}\right),
\tag{42}
\]

any liminf bound `R_(H_j)<=kappa` means that for every `epsilon>0`, infinitely many horizons in the chain satisfy

\[
|M(H)|^2
\le
12(\kappa+\epsilon)
\left(M_H\mathfrak F_H+\frac1{12}\right).
\tag{43}
\]

At fixed `q=4`, the stronger eventually-nonsquarefree value from (41) is `1.5847218565...`, or coefficient `19.0166622781...` after multiplying by `12`.

Both (38) and (41) are constant-level subsequential improvements only. They do not bound either `M(H)` or the Franel energy separately and therefore do not improve the RH-critical exponent.

## 6. Stress tests, prior art, and boundary

The proof uses only established local ingredients: the exact GCD equality ray and inverse diagonal from `FD-003`/`FD-014`, its exact zero on nonsquarefree coordinates from `FD-018`, the squarefree repeated-prime collision bound of `FD-015`, and the bounded-transition saturation classification of `FD-019`. The source-growth comparison (19)--(25) and the mixed-transition combination (28)--(35) are exact finite arguments. No prime number theorem, zero-free region, probabilistic Möbius model, or unproved cancellation estimate enters them.

The zero cases are harmless. If a ratio is near `Z>0`, its horizon endpoint is nonzero. Coordinate `q_j` is always valid because `q_j<=H_j`, and (18) has no floor error because `H_j/q_j=H_(j-1)` exactly. In the squarefree branch, infinitely many bad transition pairs force infinitely many distinct bad horizons because each horizon participates in at most two adjacent pairs. The maxima and constants in (8) are finite because `q_j<=Q` and `q=2` ensures the squarefree set is nonempty.

A targeted prior-art search by the GCD-matrix equality geometry, Mertens floor-quotient matrices, bounded geometric horizon chains, squarefree transition collisions, and polynomial-growth saturation did not locate an equivalent combined theorem. Jean-Paul Cardinal's work on symmetric matrices related to the Mertens function and Lagarias--Richman's floor-quotient partial order are neighboring matrix/floor-quotient prior art already audited in `FD-018`; neither is used as a theorem here. The Smith/Jordan GCD-matrix ingredients are already anchored in `SOURCES.md`. No broad novelty claim is made: (9) is a Mathia-specific consequence obtained by coupling the already canonical squarefree collision theorem with the new source-growth obstruction.

Several boundaries remain. The sharper nonsquarefree constant (7) itself needs an eventually nonsquarefree tail, but the universal mixed-chain constant (9) does not. Neither theorem classifies **Cesàro** saturation: a density-zero set of sacrificed horizons, as in `FD-020`, can reset amplitudes and is not controlled by the pointwise growth argument above. The result also does not treat unbounded transition ratios, where no fixed `Q` converts (19) into geometric growth relative to every polynomial scale.

Most importantly, (9) is a recurrent nonsaturation theorem for the normalized dual ratio, not a Mertens estimate. It proves that every bounded transition schedule has a fixed source-conditioned obstruction for polynomial-growth sources, but it does not convert that obstruction into `M(x)=O(x^(1/2+epsilon))`, a Franel--Landau exponent, or RH. The live continuation is still to determine whether source restrictions available for Möbius values can turn these recurrent constant gaps into a **scale-sensitive accumulated deficit** at the cumulative Farey normalization.