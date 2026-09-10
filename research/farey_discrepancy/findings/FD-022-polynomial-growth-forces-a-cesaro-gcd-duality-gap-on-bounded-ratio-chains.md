# FD-022 — polynomial-growth sources have a uniform Cesàro GCD-duality gap on bounded-ratio chains

**Status:** `EXACT-DERIVED + POLYNOMIAL-SOURCE-CESARO-GAP + BOUNDED-RATIO-MULTIHORIZON + ACCUMULATED-DEFICIT + SOURCE-GROWTH-OBSTRUCTION`.

`FD-020` classifies Cesàro saturation for an **arbitrary real source** on integer-ratio horizon chains: bounded squarefree transition ratios must have density zero, but a density-zero exceptional set can be sacrificed and the unrestricted interpolation can still saturate the sharp constant on average. `FD-021` then shows that polynomial endpoint growth prevents **pointwise** saturation on every bounded-ratio chain, while explicitly leaving Cesàro saturation open because sparse sacrificed horizons might appear to reset the interpolation.

They do not. The missing observation is that a later near-extremal horizon remembers **any earlier near-extremal endpoint** through one quotient coordinate, not merely the immediately preceding horizon. If the current transition is nonsquarefree, that quotient coordinate is nonsquarefree no matter how many horizons were skipped, so the GCD equality ray is exactly zero there. Consequently the endpoint-amplification cost survives density-zero sacrifices. Combining this long-range amplification with the squarefree-transition edge gap of `FD-015` yields a positive average deficit for every bounded-ratio polynomial-growth source.

Retain

\[
K_H(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
Z:=\zeta(2),
\tag{1}
\]

and for a real source `A(1),A(2),...` define

\[
m_d^{(H)}:=A\!\left(\left\lfloor\frac Hd\right\rfloor\right),
\qquad
E_H:=(m^{(H)})^TK_Hm^{(H)},
\qquad
R_H:=\frac{A(H)^2}{E_H},
\tag{2}
\]

with `R_H:=0` when the horizon vector is zero. As in `FD-003`,

\[
0\le R_H\le C_H:=(K_H^{-1})_{11}\le Z.
\tag{3}
\]

Consider any integer-ratio chain

\[
H_j=q_jH_{j-1},
\qquad
2\le q_j\le Q<\infty,
\tag{4}
\]

and suppose that for some fixed `C<infinity` and `alpha>=0`,

\[
|A(n)|\le Cn^\alpha.
\tag{5}
\]

For each squarefree `q<=Q`, let `p_-(q)` be its least prime factor and use the `FD-015` constant

\[
\kappa_q^\sharp
:=
\left(
\frac1Z+
\frac{4}{25p_-(q)^2q^2Z^2}
\right)^{-1}.
\tag{6}
\]

Set

\[
\kappa_Q^{\rm sf}
:=
\max_{\substack{2\le q\le Q\\q\ \mathrm{squarefree}}}
\kappa_q^\sharp,
\qquad
\delta_Q:=Z-\kappa_Q^{\rm sf}>0,
\qquad
b_Q:=\frac{\delta_Q}{2}.
\tag{7}
\]

Choose the explicit near-saturation threshold

\[
\theta_{\alpha,Q}:=\frac1{2Q^\alpha},
\qquad
r_{\alpha,Q}
:=
\left(
\frac1Z+
\frac{\theta_{\alpha,Q}^2}{Z^2}
\right)^{-1},
\tag{8}
\]

and define

\[
a_{\alpha,Q}:=Z-r_{\alpha,Q},
\qquad
\rho_{\alpha,Q}
:=
\frac{\alpha\log Q}{\log(2Q^\alpha)}<1.
\tag{9}
\]

Then every source satisfying (5) on every chain (4) obeys the uniform averaged gap

\[
\boxed{
\liminf_{n\to\infty}
\frac1{n+1}
\sum_{j=0}^{n}(Z-R_{H_j})
\ge
\Delta_{\alpha,Q}
:=
\frac{a_{\alpha,Q}b_Q}{a_{\alpha,Q}+b_Q}
\left(1-\rho_{\alpha,Q}\right)
>0.
}
\tag{10}
\]

Equivalently,

\[
\boxed{
\limsup_{n\to\infty}
\frac1{n+1}
\sum_{j=0}^{n}R_{H_j}
\le
Z-\Delta_{\alpha,Q}<Z.
}
\tag{11}
\]

Thus polynomial source growth does more than force recurrent pointwise deficits as in `FD-021`: **it prevents Cesàro saturation by a fixed positive amount on every bounded integer-ratio schedule.** The constant depends only on the growth exponent and the ratio ceiling, not on the envelope constant `C`, the initial horizon, or the transition schedule.

## 1. A nonsquarefree current transition remembers every earlier endpoint

Write as in `FD-014` and `FD-021`

\[
u^{(H)}:=K_H^{-1}e_1,
\qquad
v^{(H)}:=\frac{u^{(H)}}{C_H}.
\tag{12}
\]

The exact inverse-column formula is

\[
u_d^{(H)}
=d\sum_{\substack{k\le H\\d\mid k}}
\frac{\mu(k/d)\mu(k)}{J_2(k)}.
\tag{13}
\]

Hence

\[
\boxed{v_d^{(H)}=0\quad\text{whenever }d\text{ is nonsquarefree}.}
\tag{14}
\]

The equality-ray stability identity and inverse-diagonal bound give, for `t=A(H)` and `R_H>0`,

\[
\left|\frac{m_d^{(H)}}t-v_d^{(H)}\right|
\le
Z\sqrt{\frac1{R_H}-\frac1{C_H}}
\le
Z\sqrt{\frac1{R_H}-\frac1Z}.
\tag{15}
\]

Now take any two chain indices `i<j` and put

\[
d_{i,j}:=\frac{H_j}{H_i}=\prod_{\ell=i+1}^{j}q_\ell.
\tag{16}
\]

This is an integer coordinate at horizon `H_j`, and it samples the earlier endpoint exactly:

\[
m_{d_{i,j}}^{(H_j)}
=A\!\left(\frac{H_j}{d_{i,j}}\right)
=A(H_i).
\tag{17}
\]

If the **current** transition `q_j` is nonsquarefree, then `d_(i,j)` is nonsquarefree because it contains `q_j` as a factor. Equations (14)--(15) therefore give the long-range amplification inequality

\[
\boxed{
\left|\frac{A(H_i)}{A(H_j)}\right|
\le
Z\sqrt{\frac1{R_{H_j}}-\frac1Z}
\qquad
(i<j,\ q_j\ \mathrm{nonsquarefree},\ R_{H_j}>0).
}
\tag{18}
\]

This is the decisive strengthening of the adjacent-horizon estimate in `FD-021`. Skipping a horizon does not erase an earlier endpoint: the later floor-quotient vector sees it at coordinate `H_j/H_i`, and one nonsquarefree factor in that quotient kills the equality-ray coordinate exactly.

## 2. Polynomial growth limits the density of highly saturated nonsquarefree stages

Fix any `r<Z` and put

\[
\theta(r):=
Z\sqrt{\frac1r-\frac1Z}.
\tag{19}
\]

Assume `theta(r)<1`. Let

\[
G_r(n)
:=
\#\{1\le j\le n:
q_j\ \mathrm{nonsquarefree},\ R_{H_j}\ge r\}.
\tag{20}
\]

If there are infinitely many such indices, enumerate them

\[
g_1<g_2<\cdots.
\tag{21}
\]

Both endpoints at these horizons are nonzero because their ratios are positive. Apply (18) at `j=g_k` with `i=g_(k-1)`. Since `R_(H_(g_k))>=r`,

\[
|A(H_{g_k})|
\ge
\theta(r)^{-1}|A(H_{g_{k-1}})|.
\tag{22}
\]

Iteration gives

\[
|A(H_{g_m})|
\ge
|A(H_{g_1})|\,\theta(r)^{-(m-1)}.
\tag{23}
\]

On the other hand, bounded transition ratios imply

\[
H_j\le H_0Q^j,
\tag{24}
\]

so the polynomial envelope (5) gives

\[
|A(H_{g_m})|
\le
CH_0^\alpha Q^{\alpha g_m}.
\tag{25}
\]

Comparing logarithms in (23)--(25) and letting `n` grow yields

\[
\boxed{
\limsup_{n\to\infty}
\frac{G_r(n)}n
\le
\frac{\alpha\log Q}{\log(1/\theta(r))}.
}
\tag{26}
\]

If only finitely many indices occur, the same bound is immediate. In particular, for the choice (8), `theta(r_(alpha,Q))=1/(2Q^alpha)`, so

\[
\boxed{
\limsup_{n\to\infty}
\frac{G_{r_{\alpha,Q}}(n)}n
\le
\rho_{\alpha,Q}<1.
}
\tag{27}
\]

This converts endpoint growth into a density statement. Near-saturation at nonsquarefree stages demands multiplicative endpoint amplification; a polynomial envelope allows that demand on at most the fraction `rho_(alpha,Q)` of all transition indices.

## 3. Squarefree stages and low nonsquarefree stages exhaust the missing density

Let

\[
S(n):=
\#\{1\le j\le n:q_j\ \mathrm{squarefree}\},
\qquad
d_j:=Z-R_{H_j}\ge0.
\tag{28}
\]

Because all transition ratios are at most `Q`, the bounded-squarefree edge estimate used in `FD-020` applies with one finite uniform constant. After a finite threshold `J_Q`, every squarefree transition satisfies the `FD-015` hypotheses, and summing the adjacent pair gaps gives

\[
\boxed{
2\sum_{j=0}^{n}d_j
\ge
\delta_Q\bigl(S(n)-J_Q\bigr)
}
\tag{29}
\]

for all sufficiently large `n`. Thus, writing `s_n=S(n)/n`,

\[
\frac1{n+1}\sum_{j=0}^{n}d_j
\ge
b_Qs_n-o(1).
\tag{30}
\]

Now put `r=r_(alpha,Q)`, `a=a_(alpha,Q)`, and `G(n)=G_r(n)`. Among the `n` transition indices, exactly `n-S(n)` have a nonsquarefree current transition. At most `G(n)` of those have `R_(H_j)>=r`; every remaining nonsquarefree stage has

\[
d_j=Z-R_{H_j}>Z-r=a.
\tag{31}
\]

Therefore

\[
\frac1{n+1}\sum_{j=0}^{n}d_j
\ge
a\left(1-s_n-\frac{G(n)}n\right)-o(1).
\tag{32}
\]

By (27), for every `epsilon>0` and all sufficiently large `n`,

\[
\frac{G(n)}n\le\rho_{\alpha,Q}+\epsilon.
\tag{33}
\]

Combining (30) and (32),

\[
\frac1{n+1}\sum_{j=0}^{n}d_j
\ge
\max\left\{
 b_Qs_n-o(1),
 a\bigl(1-\rho_{\alpha,Q}-\epsilon-s_n\bigr)-o(1)
\right\}.
\tag{34}
\]

For `a,b>0` and `c>0`, the elementary minimax identity

\[
\min_{s\in[0,1]}
\max\{bs,a(c-s)\}
=
\frac{ab}{a+b}c
\qquad(0<c\le1)
\tag{35}
\]

follows by equating the two affine terms at `s=ac/(a+b)`. Apply it with

\[
c=1-\rho_{\alpha,Q}-\epsilon.
\tag{36}
\]

Letting first `n->infinity` and then `epsilon->0` proves (10).

The two branches have a clean interpretation. If squarefree transitions occupy noticeable density, `FD-015` supplies an additive edge deficit. If they do not, nonsquarefree transitions occupy nearly all indices, and polynomial endpoint growth prevents most of those horizons from being too close to the equality ray. No transition schedule can make both costs disappear.

## 4. Physical Mertens consequence

For the physical source `A=M`, the trivial increment bound gives

\[
|M(n)|\le n,
\tag{37}
\]

so (10)--(11) apply with `alpha=1` without importing any cancellation estimate. Hence every bounded-ratio integer horizon chain has a fixed averaged duality gap for the actual Mertens staircase.

For example, take `Q=4`. The squarefree transition ratios are `2` and `3`, and the weaker of their `FD-015` pair gaps is attained at `q=p=3`:

\[
\kappa_4^{\rm sf}=1.642961127398\ldots,
\qquad
\delta_4=0.001972939450\ldots.
\tag{38}
\]

The explicit choice (8) gives

\[
\theta_{1,4}=\frac18,
\qquad
r_{1,4}=1.629456089998\ldots,
\qquad
\rho_{1,4}=\frac23,
\tag{39}
\]

and therefore

\[
\boxed{
\Delta_{1,4}=0.000309121749\ldots.
}
\tag{40}
\]

Thus

\[
\limsup_{n\to\infty}
\frac1{n+1}\sum_{j=0}^{n}R_{H_j}
\le
1.644624945099\ldots.
\tag{41}
\]

Under the `FD-003` Franel normalization, multiplying the ratio constant by `12` changes the unrestricted coefficient `2pi^2=19.7392088022...` to the averaged bound `19.7354993412...` for this particular `Q=4` choice. The numerical constant is not optimized; its role is only to certify a schedule-independent positive average gap.

## 5. What this resolves and what it does not

This closes the explicit Cesàro loophole left in `FD-021` for bounded-ratio polynomial-growth sources. Sparse sacrificed horizons **cannot reset** the near-equality interpolation, because long-range quotient coordinates preserve every earlier endpoint and remain exact zero coordinates of the new equality ray whenever the current transition is nonsquarefree. The unrestricted construction of `FD-020` therefore necessarily relies on endpoint amplitudes that violate every fixed polynomial envelope if it is to saturate on average along a bounded-ratio schedule.

The result is stronger than a recurrent `liminf R_H<Z` statement: it gives a fixed positive deficit in the unweighted Cesàro mean of the normalized dual ratio. It still remains a **constant-level** theorem. It does not bound `M(H)` or the Franel energy separately, does not improve the `1/2+epsilon` exponent required by the Franel--Landau/RH criterion, and does not treat chains with unbounded transition ratios. A scale-sensitive transport theorem would need the accumulated deficit itself to grow or survive a normalization that controls the physical Mertens/Franel quantities rather than only their dual ratio.

The theorem also does not use the correlated Möbius sign law, divisor identities beyond those already encoded in the GCD equality ray, or probabilistic cancellation. Polynomial endpoint growth alone is sufficient. Thus the next source-specific question is narrower than before: on bounded-ratio chains, the missing issue is no longer whether constant deficits accumulate, but whether their accumulation can be converted into a **scale-dependent** estimate; alternatively, one must understand what happens when the transition breadth is allowed to grow with the horizon.

## 6. Stress tests and prior-art boundary

The proof uses only exact local ingredients already canonical in this line: the Smith/Jordan equality-ray formula and coordinate stability from `FD-003`/`FD-014`, the nonsquarefree zero coordinates isolated in `FD-018`/`FD-021`, and the squarefree two-horizon gap of `FD-015` as accumulated in `FD-020`. Equation (18) is a direct finite identity for any pair of chain horizons; no limiting number-theory estimate enters it. The density count uses only `H_j<=H_0Q^j` and the assumed polynomial envelope.

Zero cases do not create an escape. Every index counted by `G_r` has `R_H>=r>0`, so its endpoint is nonzero and the amplification ratio is defined. If only finitely many such indices exist, their density is already zero. The quotient coordinate `d_(i,j)=H_j/H_i` is always an integer between `1` and `H_j`, and its floor quotient is exactly `H_i`, so there is no floor error. Once `q_j` is nonsquarefree, the entire product `d_(i,j)` is nonsquarefree even if all intervening transitions except the last are squarefree.

The explicit constants were independently recomputed from (6)--(10); for `alpha=1,Q=4` they give (38)--(41). The minimax step was also checked at the two extreme schedules: a squarefree-heavy schedule is controlled by (29), while an eventually nonsquarefree schedule is controlled by the density bound (27). Mixed schedules interpolate between those two costs and cannot lower their maximum below (10).

A targeted literature search around Farey--Mertens discrepancy, symmetric/divisibility matrices for the Mertens function, GCD-matrix extremality, floor-quotient formulations, and Cesàro averaging did not locate this bounded-horizon-chain polynomial-growth accumulation statement. Cardinal--Overholt's symmetric-matrix Möbius inversion and the Lagarias--Richman floor-quotient partial order remain neighboring matrix/floor-quotient prior art already noted in the local audit trail, but no theorem from them is imported here. The Smith/Jordan GCD-matrix ingredients on which the proof actually depends are already anchored in `SOURCES.md`, so this finding adds no new durable bibliographic dependency and does not require a source-anchor edit.

The durable conclusion is precise: **on every integer-ratio horizon chain with a fixed transition ceiling, any polynomial-growth source has a schedule-independent positive Cesàro gap below the sharp one-horizon GCD-duality constant.** This removes the density-zero-reset escape available to unrestricted sources, while leaving the RH-critical scale problem open.