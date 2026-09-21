# FD-253 — Companion incidence controls paired exact-omission conditioning

- **Date:** 2026-09-21
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** divisor-response sampling / exact omissions / paired increments / companion sensors / incidence inversion / conditioning separation
- **Depends on:** FD-225, FD-245, FD-248, FD-250, FD-251, FD-252
- **Classification:** `EXACT-DERIVED + PAIRED-COEFFICIENT-INVERSE + COMPANION-SIDE-CONDITIONING + SUPPORT-NORM-SEPARATION`

## Claim

FD-252 shows that the support constraint

\[
\operatorname{supp}(\Delta Y)\subseteq E\cup(E+1)
\]

cannot by itself improve the free weighted incidence norm `kappa`: a bad divisor support can be embedded into a genuine exact-omission support. The missing question is coefficient-level. The adjacent increments are not free; an isolated omitted response value creates an opposite-sign pair.

That pairing has a strong exact consequence. Let

\[
Y(m)=(\mathscr A b)(m),\qquad Y(0)=0,
\]

and assume

\[
|b_n|\le C_b n\qquad(1\le n\le H).
\tag{1}
\]

Suppose `Y` is supported, up to horizon `H`, on an omission set

\[
E\subseteq\{1,\ldots,H-1\},
\qquad |E|=K,
\tag{2}
\]

with no two consecutive elements. Put

\[
C:=E+1=\{e+1:e\in E\}.
\tag{3}
\]

Assume additionally that omitted starts do not divide companion locations:

\[
\boxed{
 e'\nmid e+1
 \qquad(e,e'\in E).
}
\tag{4}
\]

Let `kappa(C)` be the weighted induced-divisibility Möbius norm of FD-248. Then

\[
\boxed{
\sum_{d\le H}\frac{|\Delta Y(d)|}{d}
\le
\left(2+\frac1{e_{\min}}\right)
C_b K\,\kappa(C),
}
\tag{5}
\]

where `e_min=min(E)`. Consequently,

\[
\boxed{
\sum_{n\le H}|b_n|
\le
\left(2+\frac1{e_{\min}}\right)
C_b H K\,\kappa(C).
}
\tag{6}
\]

Thus, once the true adjacent-pair coefficient map is retained, the relevant incidence conditioning can move entirely from the apparently bad **start/core support** to the **companion support**. In particular, if `C` is a divisibility antichain, then `kappa(C)=1` and

\[
\sum_{n\le H}|b_n|
\le \frac52 C_b H K.
\tag{7}
\]

This can coexist with arbitrarily large free support conditioning. More precisely, let `D` be any finite subset of `{1,...,M}`, choose an integer `L>M`, and define

\[
E_L:=LD=\{Ld:d\in D\},
\qquad
C_L:=LD+1,
\qquad
H:=LM+1.
\tag{8}
\]

Then `C_L` is a divisibility antichain, every exact response supported on `E_L` obeys

\[
\boxed{
\sum_{n\le H}|b_n|
\le
\left(2+\frac1L\right)C_b H|D|,
}
\tag{9}
\]

while for the full active support

\[
S_L:=LD\cup(LD+1)
\]

one still has

\[
\boxed{\kappa(S_L)\ge\kappa(D).}
\tag{10}
\]

Therefore the support norm `kappa(supp(Delta Y))` can be extremely large even though the actual paired exact-omission inverse is uniformly linear in the omission count.

Applying (8)--(10) to the FD-250 supports gives an explicit separation family: there are horizons `H` and exact-omission support shapes with `K=H^{o(1)}` for which

\[
\frac{\kappa(S_H)}{(\log\log H)^A}\to\infty
\qquad\text{for every fixed }A>0,
\tag{11}
\]

but every paired response on the corresponding omission locations satisfying (1) has

\[
\sum_{n\le H}|b_n|
\le H^{1+o(1)},
\tag{12}
\]

and hence carries `o(H^2)` coefficient mass. Large free-support conditioning is therefore not merely quantitatively loose after pairing; it can point in the wrong direction by a super-polylogarithmic factor.

## Isolated omissions create exact opposite-sign increment pairs

Let

\[
g=\mu*b.
\tag{13}
\]

By FD-225,

\[
b=\mathbf1*g,
\qquad
g(m)=Y(m)-Y(m-1).
\tag{14}
\]

Because no two members of `E` are consecutive and `Y` vanishes outside `E`, every `e in E` contributes exactly

\[
\boxed{
g(e)=Y(e),\qquad g(e+1)=-Y(e).}
\tag{15}
\]

There are no other nonzero increments below `H`. Hence

\[
\operatorname{supp}(g)\subseteq E\cup C.
\tag{16}
\]

The support relaxation of FD-248 treats the two coordinates in (15) as independent. Equation (15) is the coefficient relation that FD-252 deliberately did not use.

## Companion rows close under divisibility

Fix a companion `c=e+1 in C`. From `b=1*g`,

\[
b_c=
\sum_{\substack{d\mid c\\d\in E\cup C}}g(d).
\tag{17}
\]

Condition (4) removes every start coordinate from this row. Therefore

\[
\boxed{
b_c=
\sum_{\substack{c'\in C\\c'\mid c}}g(c').}
\tag{18}
\]

So the companion coordinates form a closed induced divisibility system. Normalize

\[
\beta_c:=\frac{b_c}{c},
\qquad
x_c:=\frac{g(c)}c.
\tag{19}
\]

Exactly as in FD-248, if `Z_C` is the zeta matrix of the induced divisibility poset on `C` and `R_C=diag(c:c in C)`, then

\[
\beta=R_C^{-1}Z_C R_C x.
\tag{20}
\]

Its inverse has entries

\[
(R_C^{-1}Z_C R_C)^{-1}(c,c')
=
\mathbf1_{c'\mid c}\,
\mu_C(c',c)\frac{c'}c.
\tag{21}
\]

The envelope (1) gives `|beta_c|<=C_b`, and hence

\[
\frac{|g(c)|}{c}
\le
C_b
\sum_{\substack{c'\in C\\c'\mid c}}
|\mu_C(c',c)|\frac{c'}c
\le C_b\kappa(C).
\tag{22}
\]

Summing over `C`,

\[
\boxed{
\sum_{c\in C}\frac{|g(c)|}{c}
\le C_b K\kappa(C).}
\tag{23}
\]

This is the decisive coefficient-level difference from FD-252. A large incidence row living on the start coordinates is irrelevant unless the opposite-sign companions can themselves be hidden from the coefficient envelope.

## Pairing transfers the companion bound back to the starts

For `c=e+1`, equation (15) gives `|g(e)|=|g(c)|`. Therefore

\[
\frac{|g(e)|}{e}
=
\frac ce\frac{|g(c)|}{c}
\le
\left(1+\frac1{e_{\min}}\right)
\frac{|g(c)|}{c}.
\tag{24}
\]

Combining (23)--(24),

\[
\begin{aligned}
\sum_{d\le H}\frac{|g(d)|}{d}
&=
\sum_{e\in E}\frac{|g(e)|}{e}
+
\sum_{c\in C}\frac{|g(c)|}{c}\\
&\le
\left(2+\frac1{e_{\min}}\right)
C_b K\kappa(C),
\end{aligned}
\tag{25}
\]

which proves (5).

Finally,

\[
\begin{aligned}
\sum_{n\le H}|b_n|
&\le
\sum_{d\le H}|g(d)|
\left\lfloor\frac Hd\right\rfloor\\
&\le
H\sum_{d\le H}\frac{|g(d)|}{d},
\end{aligned}
\tag{26}
\]

and (6) follows.

If `C` is a divisibility antichain, its induced zeta matrix is the identity, so `kappa(C)=1`. Since condition (4) also excludes `e_min=1`, one has `e_min>=2`, which yields the numerical constant `5/2` in (7).

## Large dilation makes every companion a private sensor

Now take `D subseteq {1,...,M}` and `L>M`. The omissions `E_L=LD` are separated by at least `L`, so (15) holds. Moreover no start can divide a companion because

\[
Ld'\equiv0\pmod L,
\qquad
Ld+1\equiv1\pmod L.
\tag{27}
\]

Thus condition (4) is automatic.

The stronger fact is that the companion set is an antichain. Suppose

\[
Lq+1\mid Ld+1,
\qquad q<d\le M.
\tag{28}
\]

Then `Lq+1` divides their difference `L(d-q)`. Since

\[
\gcd(Lq+1,L)=1,
\]

it follows that

\[
Lq+1\mid d-q.
\tag{29}
\]

But

\[
0<d-q<M<Lq+1,
\]

which is impossible. Hence `C_L` is a divisibility antichain and (9) follows from (6), with `e_min>=L`.

This argument is stronger than simply making the full support primitive. The start set `LD` retains **all** divisibility relations of `D`; only the companion sensors have been made primitive.

## The bad core incidence intervals survive unchanged

Let

\[
S_L=LD\cup(LD+1).
\]

If `q|d` in `D`, any element of the induced interval from `Lq` to `Ld` must be divisible by `Lq`, hence by `L`. No companion `Lr+1` is divisible by `L`. Therefore the interval

\[
[Lq,Ld]_{S_L}
\]

contains only core elements and is order-isomorphic to

\[
[q,d]_D
\]

under `Lr -> r`. Incidence Möbius values are interval-local, so

\[
\boxed{
\mu_{S_L}(Lq,Ld)=\mu_D(q,d).}
\tag{30}
\]

The weights are also unchanged:

\[
\frac{Lq}{Ld}=\frac qd.
\tag{31}
\]

Taking the corresponding row contribution inside the nonnegative absolute row sum defining `kappa(S_L)` proves (10).

Thus large dilation produces the sharp separation wanted after FD-252:

- the **free support norm** still sees every bad Möbius merge from `D`;
- the **paired coefficient system** exposes every opposite-sign companion through an antichain sensor row and therefore costs only `O(K)` in weighted increment mass.

The first statement alone is not evidence of bad exact-omission conditioning once the coefficient pairing is restored.

## Super-polylogarithmic support conditioning can still be paired-coercive

FD-250 supplies a sequence of ambient scales `M` and finite supports `D_M subseteq [1,M]` with

\[
|D_M|=M^{o(1)}
\]

and

\[
\frac{\kappa(D_M)}{(\log\log M)^A}\to\infty
\qquad(A>0\text{ fixed}).
\tag{32}
\]

Choose `L=M+1` and

\[
H=L M+1=M^2+M+1.
\tag{33}
\]

Then `|D_M|=H^{o(1)}` and `log log H = log log M + O(1)`. Equations (10) and (32) give (11), while (9) gives

\[
\sum_{n\le H}|b_n|
\le
(2+o(1))C_b H^{1+o(1)}.
\tag{34}
\]

Since coefficient capacity below `H` is of order `H^2`, the paired family is macroscopically coercive despite the super-polylogarithmically large support norm.

This does not contradict FD-250. That finding proves that exact-omission **support geometry** can carry large incidence Möbius rows. The present result proves that such rows need not be reachable by the actual paired coefficient subspace under the coefficient envelope.

## Finite audit

Take

\[
D=\{1,2,3,6\},
\qquad L=7,
\qquad H=43.
\]

The base divisor row at `6` has

\[
\kappa(D)=
1+\frac12+\frac13+\frac16=2.
\]

The lifted support is

\[
S_L=\{7,8,14,15,21,22,42,43\},
\]

and the core interval from `7` to `42` is the same divisor diamond, so `kappa(S_L)>=2`. But the companions

\[
C_L=\{8,15,22,43\}
\]

form an antichain. For an arbitrary response on the four omitted starts, the four companion coefficient rows directly recover the four negative increments, and (9) bounds the whole coefficient mass by

\[
\left(2+\frac17\right)4C_bH.
\]

A direct exact incidence calculation gives `kappa(C_L)=1` and preserves every base Möbius value on the lifted core interval, matching the symbolic proof.

## Prior-art / novelty audit

The literature search again finds the classical Möbius-pair framework of Pollack--Sanna and its poset generalization by Goh, together with the standard incidence-algebra fact that an induced zeta matrix is inverted by the poset Möbius matrix. Those results concern support uncertainty or general incidence inversion. I did not find a statement matching the finite-horizon adjacent-difference pairing above, the companion-row closure (18), or the separation (9)--(10) between arbitrarily bad core support conditioning and uniformly benign paired omission conditioning.

No external theorem is load-bearing. The proof uses only the exact response inversion from FD-225, the weighted finite-poset inverse already proved in FD-248, and elementary divisibility. No new dependency is therefore added to `SOURCES.md`, and no novelty is claimed for Möbius inversion itself.

## Boundary and next audit

The result applies to isolated omissions whose start coordinates do not divide companion locations. It does not prove a better universal exponent than the FD-251 free-support ceiling for arbitrary exact omissions. In a genuinely bad paired family, companion rows must lose the private-sensor property: starts may feed companion rows, or the companion set itself must develop enough divisibility conditioning to hide the opposite-sign increments.

For pure dilations `E=LD`, starts can never feed companion rows, so the remaining problem becomes especially concrete:

\[
\boxed{
\text{How large can }\kappa(LD+1)\text{ be simultaneously with }\kappa(D)
\text{ for a polynomial-size }D?
}
\]

The parity case `L=2` is the first nontrivial test. Large `kappa(D)` alone is now known to be insufficient; one needs matched conditioning on the shifted companion geometry, or a different omission pattern in which the two sides interact.

The theorem remains response-side and signed. It does not impose positivity, prime-reservoir capacity, squarefree source realization, or full Möbius arithmetic coherence, and it does not improve the approximate-residual term of FD-242.

## Status

**Proved.** The companion closure, weighted paired bound (5)--(6), large-dilation antichain corollary, preservation of arbitrary core incidence conditioning, and super-polylogarithmic separation obtained from FD-250 are exact finite statements. The result materially advances the FD-252 frontier by identifying a concrete coefficient-level mechanism that can completely neutralize bad support conditioning.