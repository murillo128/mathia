# RE-165 — KV-envelope capacity is sharp and critical equality remains ambiguous

**Status:** `EXACT-DERIVED + GENERALIZED-INSERTION-SHARPNESS + QUANTITATIVE-PNT-INVERSION-BOUNDARY + CORRECTS-RE-164-EQUALITY-CLAUSE + PRIOR-ART-BOUNDED`.

**Parent findings:** RE-015, RE-153, RE-157, RE-164.

`RE-164` proves that quantitative Korobov--Vinogradov PNT fidelity collapses generalized-source freedom once the PNT tail, propagated through the positive Robin kernel, is `o(1)`. Its remote-tail estimate is

\[
|\mathcal A_p(Q_1)-\mathcal A_p(Q_2)|
\ll
\sqrt p\log p\,
\frac{e^{-bV(T)}}{V(T)},
\qquad
V(t):=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}}.
\tag{1}
\]

The upper bound is essentially sharp inside the same generalized-source class. One can discretize an increasing fraction of the allowed PNT error envelope into genuine generalized-prime insertions. The resulting source preserves the quantitative PNT remainder and moves the Robin coordinate by the full scale in (1).

Consequently the natural remote inversion parameter is

\[
\boxed{
\mathfrak K_b(p,T)
:=
\sqrt p\log p\,
\frac{e^{-bV(T)}}{V(T)}.
}
\tag{2}
\]

If `mathfrak K_b(p,T)->0`, `RE-164` gives matched-source rigidity. If `mathfrak K_b(p,T)` stays bounded away from zero or diverges, quantitative PNT fidelity alone does **not** force the source coordinate to be unique: generalized insertion controls can retain a nonvanishing Robin displacement while staying inside the same envelope.

For the canonical lower cutoff

\[
T=U_B(p)
=
\exp\!\left(B(\log p)^{5/3}(\log\log p)^{1/3}\right),
\tag{3}
\]

put

\[
\kappa_B:=B^{3/5}\left(\frac35\right)^{1/5}.
\tag{4}
\]

Then the fixed-`B` phase boundary is

\[
\boxed{
 b\kappa_B>\frac12
 \quad\Longrightarrow\quad
 \text{quantitative-PNT rigidity},
}
\tag{5}
\]

whereas

\[
\boxed{
 b\kappa_B\le\frac12
 \quad\Longrightarrow\quad
 \text{generalized-source ambiguity remains possible}.
}
\tag{6}
\]

The equality direction in (6) matters. The leading relation `V(U_B)=kappa_B log p (1+o(1))` is insufficient at the critical exponent. Its next term has a definite sign and places the fixed canonical horizon **below** the exact inversion point. This also corrects the equality clause in `RE-164` equation (24): for a bounded terminal shell, `b kappa_A=1/2` does not imply `o(1)` source ambiguity from the displayed estimate, and in fact matched insertion controls with order-one separation still fit inside the PNT envelope there.

## 1. An envelope-saturating generalized insertion source

Retain the normalized source coordinate of `RE-153`, with `U=U_A(p)`,

\[
\mathcal A_p(Q)
=
\int_{J_p}
\frac{t-\vartheta_Q(t)}{\sqrt t}\,d\nu_p(t),
\qquad
\nu_p(dt)
=
\frac{\sqrt p\log p\,\sqrt t\,(-h'(t))}{Z_p}\,dt,
\qquad
Z_p=2+o(1),
\tag{7}
\]

where

\[
h(t)=\frac{-\log(1-t^{-1})}{\log t}.
\tag{8}
\]

Let the ordinary source satisfy, on `[T,U]`,

\[
|\vartheta(t)-t|
\le C_0 t e^{-bV(t)}
\tag{9}
\]

for some fixed `b,C_0>0`. This is exactly the type of quantitative PNT input already anchored in `SOURCES.md`; the construction below only assumes (9), and does not assert it for an arbitrary Beurling system.

Set

\[
E_b(t):=t e^{-bV(t)}.
\tag{10}
\]

Since `V(t)=o(log t)` and

\[
\frac{d}{d\log t}\bigl(\log t-bV(t)\bigr)=1-o(1),
\tag{11}
\]

`E_b` is eventually strictly increasing. Fix `lambda>0` and consider the target cumulative insertion mass

\[
F_{p,\lambda}(t)
:=
\lambda\bigl(E_b(t)-E_b(T)\bigr),
\qquad T\le t\le U.
\tag{12}
\]

A generalized-prime insertion at a real label `q` adds `log q` to the Chebyshev function for every `t>=q`. Because generalized labels may be chosen at arbitrary distinct real positions, the increasing function (12) can be quantized by a finite packet family so that its cumulative inserted Chebyshev mass `F^*_{p,lambda}` satisfies

\[
\boxed{
\sup_{T\le t\le U}
|F^*_{p,\lambda}(t)-F_{p,\lambda}(t)|
=O(\log U).
}
\tag{13}
\]

One explicit greedy construction inserts a new distinct label whenever the unresolved increase of `F_{p,lambda}` first reaches the logarithmic weight of the current label; the residual is always at most one next jump. The super-polynomial size of `T` makes the `O(log U)` quantization error negligible at Robin normalization.

Let `Q_{p,lambda}` be the ordinary source plus these labels. It agrees exactly with the ordinary source below `T`, and from (12)--(13),

\[
0\le
\vartheta_{Q_{p,\lambda}}(t)-\vartheta(t)
\le
\lambda E_b(t)+O(\log U).
\tag{14}
\]

Since `E_b(T)>>log U` at every canonical `U_B(p)` considered here,

\[
\boxed{
|\vartheta_{Q_{p,\lambda}}(t)-t|
\le
(C_0+\lambda+o(1))\,t e^{-bV(t)}
\qquad(T\le t\le U).
}
\tag{15}
\]

Thus the modified source remains in the **same quantitative PNT exponent class**. Only its harmless fixed envelope constant changes.

## 2. The Robin displacement reaches the RE-164 remote-tail scale

The exact matched-source identity from `RE-164` gives

\[
\mathcal A_p(Q_{p,\lambda})-
\mathcal A_p(P)
=
-\frac{\sqrt p\log p}{Z_p}
\int_T^U
F^*_{p,\lambda}(t)(-h'(t))\,dt.
\tag{16}
\]

The quantization error in (13) contributes at most

\[
\ll
\sqrt p\log p\,\log U\,[h(T)-h(U)]
\ll
\frac{\sqrt p\log p\,\log U}{T\log T}
=o(1).
\tag{17}
\]

For large `t`,

\[
-h'(t)
=
\frac{1+o(1)}{t^2\log t}.
\tag{18}
\]

Suppose now that `T=U_B(p)` and `U=U_A(p)` with fixed `A>B>0`. Substituting (12) into (16), the main term is

\[
\lambda\frac{\sqrt p\log p}{Z_p}
\left[
\int_T^U\frac{e^{-bV(t)}}{t\log t}\,dt
-
E_b(T)\int_T^U\frac{dt}{t^2\log t}
\right](1+o(1)).
\tag{19}
\]

The second integral is lower order, because

\[
E_b(T)\int_T^U\frac{dt}{t^2\log t}
\sim
\frac{e^{-bV(T)}}{\log T}
=o\!\left(\frac{e^{-bV(T)}}{V(T)}\right).
\tag{20}
\]

For the first integral, write `y=log t`. Since

\[
\frac{yV'(e^y)}{V(e^y)}
=
\frac35-rac1{5\log y},
\tag{21}
\]

the change of variable `u=V(e^y)` gives the endpoint Laplace asymptotic

\[
\boxed{
\int_T^U\frac{e^{-bV(t)}}{t\log t}\,dt
=
\left(\frac{5}{3b}+o(1)\right)
\frac{e^{-bV(T)}}{V(T)}.
}
\tag{22}
\]

The upper endpoint is exponentially negligible because `A>B` implies `V(U)-V(T) asymp log p`.

Combining (16)--(22) with `Z_p=2+o(1)`,

\[
\boxed{
|\mathcal A_p(Q_{p,\lambda})-
\mathcal A_p(P)|
=
\left(\frac{5\lambda}{6b}+o(1)\right)
\mathfrak K_b(p,T).
}
\tag{23}
\]

Therefore the remote-tail majorant of `RE-164` is sharp up to a fixed multiplicative constant even within the simple class of **positive generalized-prime insertions**. No signed deletion or exotic compensation is required.

If `mathfrak K_b(p,T)->infinity`, choose `lambda=lambda_p->0` with `lambda_p mathfrak K_b -> Delta` for any prescribed `Delta>0`; equation (15) becomes even more faithful while (23) retains the chosen order-one Robin displacement. If `mathfrak K_b` has a positive finite lower limit, a fixed sufficiently small `lambda` already gives a nonvanishing displacement. Conversely, `RE-164` proves that `mathfrak K_b->0` forces every pair of matched sources in this fidelity class to have `o(1)` separation.

Hence (2), rather than a qualitative PNT statement or a finite moment budget, is the exact generalized-source capacity parameter generated by the quantitative PNT envelope.

## 3. Fixed canonical horizons: the equality term has the wrong sign for rigidity

Let

\[
L:=\log p,
\qquad
R:=\log L,
\qquad
S:=\log R.
\tag{24}
\]

For the canonical cutoff `T=U_B(p)`,

\[
\log T=B L^{5/3}R^{1/3},
\tag{25}
\]

and an elementary expansion gives

\[
\boxed{
V(T)
=
\kappa_B L
\left[
1-
\frac{S+3\log B}{25R}
+O\!\left(\frac{S^2+1}{R^2}\right)
\right].
}
\tag{26}
\]

Indeed,

\[
\log\log T
=
\frac53R+rac13S+\log B,
\tag{27}
\]

and (26) follows by expanding the `(-1/5)` power in the denominator of `V`.

From (2),

\[
\log\mathfrak K_b(p,T)
=
\frac12L-bV(T)+\log L-\log V(T).
\tag{28}
\]

Thus the strict regimes are immediate:

\[
b\kappa_B>\frac12
\Longrightarrow
\mathfrak K_b\to0,
\qquad
b\kappa_B<\frac12
\Longrightarrow
\mathfrak K_b\to\infty.
\tag{29}
\]

At the nominal equality `b kappa_B=1/2`, however, (26) yields

\[
\frac12L-bV(T)
=
\frac{L}{50R}
\bigl(S+3\log B+o(S+1)\bigr)
\longrightarrow+\infty.
\tag{30}
\]

The remaining term `log L-log V(T)` is only `O(1)`. Therefore

\[
\boxed{
 b\kappa_B=\frac12
 \quad\Longrightarrow\quad
 \mathfrak K_b(p,U_B(p))\to\infty.
}
\tag{31}
\]

This proves (5)--(6). The leading-order equality lies on the **ambiguous**, not rigid, side. The exact inversion point is determined by `bV(T)`, including its slowly varying correction, rather than by `b kappa_B` alone.

Equivalently, the true remote transition is

\[
\boxed{
\sqrt p\log p\,
\frac{e^{-bV(T)}}{V(T)}\to0,
}
\tag{32}
\]

not the shorthand `b kappa_B>=1/2`.

## 4. Correction to the bounded-terminal equality statement in RE-164

`RE-164` equation (23) wrote the bounded-terminal estimate at `U_A(p)` as

\[
|\Delta\mathcal A_p|
\ll_{L_0}
 p^{1/2-b\kappa_A+o(1)}
 (\log p)^{-2/3}(\log\log p)^{-1/3}
\tag{33}
\]

and equation (24) then included the equality `b kappa_A=1/2` in the `o(1)` conclusion. That inference is not valid: at equality the unspecified `p^{o(1)}` cannot be discarded against a polylogarithm. Expansion (26), with `B=A`, determines its sign and shows that it dominates every logarithmic saving.

More concretely, fix `L_0>0` and let

\[
T=U_A(p)e^{-L_0}.
\tag{34}
\]

Place the same number `m_p` of generalized labels in narrow packets near `T` and near `U_A(p)`, exactly as in `RE-157`. Their per-label Robin influence difference is `asymp sqrt(p) log p/U_A(p)`, while an order-one coordinate separation needs only

\[
m_p\asymp\frac{U_A(p)}{\sqrt p\log p}.
\tag{35}
\]

The corresponding Chebyshev perturbation is

\[
m_p\log U_A(p)
\asymp
U_A(p)\,
\frac{\log U_A(p)}{\sqrt p\log p}.
\tag{36}
\]

At `b kappa_A=1/2`, (26) gives

\[
\frac{\log U_A(p)}{\sqrt p\log p}
\bigg/
 e^{-bV(U_A(p))}
\longrightarrow0,
\tag{37}
\]

because the subpower gain from (30) dominates the factor `log U_A/log p`. Hence both packets fit inside the same quantitative PNT envelope while retaining order-one Robin separation.

Accordingly the safe statement replacing `RE-164` equation (24) is

\[
\boxed{
 b\kappa_A>\frac12
 \Longrightarrow
 \text{bounded-terminal rigidity},
}
\tag{38}
\]

while the fixed-`A` equality `b kappa_A=1/2` remains non-rigid in the generalized insertion class. This is a correction of the equality endpoint only; the strict supercritical results and the matched-source estimates of `RE-164` remain unchanged.

## 5. Prior-art boundary and research consequence

Beurling generalized-prime constructions with prescribed or near-prescribed PNT behavior are classical. A targeted audit found, in particular, the Diamond--Montgomery--Vorhauer/Zhang perturbative tradition and the later Broucke--Vindas random discretization framework, together with modern work on quantitative PNT remainders and zero density for Beurling systems. Those results establish that discretizing controlled generalized-prime distributions is a standard and powerful construction mechanism. They do not supply the Robin source coordinate (7), the capacity parameter (2), the endpoint asymptotic (23), or the canonical-horizon inversion calculation (26)--(31). No external theorem from that literature is load-bearing here: the insertion quantization is elementary, and the analytic input is the PNT envelope already anchored in `SOURCES.md`. Therefore `SOURCES.md` requires no change.

The consequence for the live `robin_extremal` frontier is sharper than in `RE-164`. Quantitative PNT fidelity does remove the artificial upper-terminal ambiguity, but **only once its propagated tail capacity actually tends to zero**. Below that inversion point, and even at the nominal fixed-`B` equality `b kappa_B=1/2`, generalized sources can saturate the allowed remainder and preserve nonvanishing Robin leverage.

This remains an information-theoretic generalized-source result, not a construction involving the ordinary primes or a counterexample to Robin. It does not weaken the accepted selector-height coupling clue. Rather, it identifies exactly where quantitative source fidelity stops being enough: any positive argument operating at or below the inversion boundary must use ordinary-prime/CA structure, a stronger local source constraint, or a selector/source coupling that generalized insertions do not satisfy.