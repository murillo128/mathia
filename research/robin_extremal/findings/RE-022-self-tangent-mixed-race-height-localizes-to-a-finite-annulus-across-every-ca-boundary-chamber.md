# RE-022 — self-tangent mixed-race height localizes to a finite annulus across every CA boundary chamber

**Status:** `EXACT-DERIVED + CLEAN-HYPOTHESIS-REMOVAL + SHORT-HORIZON-BOUND + ALL-LOG-ORDERS-ANNULUS-LOCALIZATION + UNIVERSAL-SELF-TANGENT-COUNTEREXAMPLE-OBSTRUCTION + PRIOR-ART-BOUNDED`. `RE-014` and `RE-015` localized the mixed Mertens--Chebyshev contribution controlling Robin height to a finite future annulus, but only for clean local peaks because their endpoint estimate for `vartheta(p)-p` was obtained from the clean first-layer selector. `RE-021` removes exactly that missing hypothesis: every sufficiently large regular self-tangent CA state has a canonical last active first-layer prime `p` with `X-p=O(p^0.52)`, and the same self-tangent split controls its Chebyshev endpoint.

Consequently the finite-annulus obstruction is not a clean-chamber phenomenon. Let `C` range through any unbounded family of sufficiently large **regular self-tangent colossally abundant states**, with no assumption that the adjacent CA transitions are first-layer, untied, or even that `C` is a local peak. Put

\[
X:=\log C,
\]

and let `p` be the largest prime whose first-layer event is active at `X`. Define

\[
\Delta(t):=\vartheta(t)-t,
\qquad
h(t):=\frac{-\log(1-t^{-1})}{\log t},
\qquad
k(t):=\frac1{t\log t},
\]

\[
I(t):=\Delta(t)h'(t)-\bigl(h(t)-k(t)\bigr),
\qquad
\mathcal M_*(x):=\int_x^\infty I(t)\,dt,
\qquad
\mathscr Y(x):=\sqrt x\log x\,\mathcal M_*(x).
\tag{1}
\]

Then:

1. the selected endpoint obeys
\[
\boxed{|\Delta(p)|=O(p^{0.52});}
\tag{2}
\]

2. for every positive horizon `H=H(p)` satisfying
\[
\boxed{
H=o\!\left(\frac{p^{3/4}}{\sqrt{\log p}}\right),
}
\tag{3}
\]
one has
\[
\boxed{
\sqrt p\log p\int_p^{p+H} I(t)\,dt=o(1);
}
\tag{4}
\]

3. in particular, for every fixed `0<alpha<3/4`, every fixed `M>0`, and `H=p^alpha`,
\[
\boxed{
\sqrt p\log p\int_p^{p+p^\alpha} I(t)\,dt
=
O_{\alpha,M}\bigl((\log p)^{-M}\bigr);
}
\tag{5}
\]

4. let
\[
V(t):=\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}},
\qquad
U_A(p):=
\exp\!\left(
A(\log p)^{5/3}(\log\log p)^{1/3}
\right).
\tag{6}
\]
For the same absolute threshold `A_0` as in `RE-015`, every fixed `A>A_0` and every fixed `M>0` satisfy
\[
\boxed{
\mathscr Y(p)
=
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)}I(t)\,dt
+
O_{\alpha,A,M}\bigl((\log p)^{-M}\bigr).
}
\tag{7}
\]

Thus the **entire inverse-logarithmic asymptotic hierarchy** of self-tangent Robin height is determined by a finite mixed-race annulus, independently of the layers occurring at the two adjacent CA boundaries. With

\[
L:=\log X,
\qquad
\ell:=\frac12W(2XL),
\tag{8}
\]

`RE-021` and (7) give, for every fixed integer `m>=1`,

\[
\boxed{
\begin{aligned}
\sqrt p\log p\,(\log G(C)-\gamma)
&=
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)}I(t)\,dt\\
&\quad-
\sqrt{\frac L\ell}
\left(
2+\sum_{j=1}^{m}(-1)^j\frac{j!}{\ell^j}
\right)
+
O_{\alpha,A,m}(L^{-m-1}).
\end{aligned}
}
\tag{9}
\]

In particular,

\[
\boxed{
\sqrt p\log p\,(\log G(C)-\gamma)
=
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)}I(t)\,dt
-2\sqrt2
+\frac{\sqrt2(2+\log2)}{\log p}
+O((\log p)^{-2}).
}
\tag{10}
\]

Therefore every unbounded sequence of regular self-tangent Robin counterexamples, including higher-layer and tied boundary sequences, must satisfy

\[
\boxed{
\liminf
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)}I(t)\,dt
\ge 2\sqrt2
}
\tag{11}
\]

for every fixed `alpha<3/4` and every fixed `A>A_0`.

The exceptional CA boundary chamber therefore no longer escapes either the mixed-race **height threshold** (`RE-021`) or its **two-sided scale localization** (this finding). What remains exceptional is the geometry selecting the state and, in particular, the fine adjacent-transition information used by `RE-006`, `RE-007`, `RE-017`--`RE-020`.

## 1. The universal self-tangent frontier supplies the only endpoint estimate used by RE-014

`RE-021` proves that every sufficiently large regular self-tangent state has a last active first-layer prime `p`, with next ordinary prime `q`, such that

\[
p<X<q+1,
\qquad
X-p=O(p^{0.52}),
\tag{12}
\]

and the exact self-tangent split is

\[
X=\vartheta(p)+\Phi_{\ge2}(X),
\qquad
\Delta(p)=X-p-\Phi_{\ge2}(X).
\tag{13}
\]

The second-layer analysis of `RE-016`, shown in `RE-021` to survive without clean adjacent boundaries, gives

\[
\Phi_{\ge2}(X)
=
\sqrt X\sqrt{\frac L\ell}
+
O_M\!\left(\sqrt X\,L^{-M}\right)
\tag{14}
\]

for every fixed `M`; in particular `Phi_(>=2)(X)=O(sqrt(X))`. Since (12) implies `X/p->1`, equations (12)--(14) give

\[
|\Delta(p)|
\le X-p+\Phi_{\ge2}(X)
=O(p^{0.52}),
\]

which proves (2).

This is the load-bearing observation. The proof of the short-horizon estimate in `RE-014` used clean adjacency only to obtain this endpoint bound. Once `RE-021` supplies it for the canonical first-layer frontier of every regular self-tangent state, the integral estimate itself has no remaining reference to the adjacent CA transition layers.

## 2. A general sub-three-quarter horizon is invisible at first Robin order

Let `H=o(p^(3/4)/sqrt(log p))`. Since this implies `H=o(p)`, every `t` in `[p,p+H]` is comparable with `p` for large `p`. Monotonicity of `vartheta` and the trivial bound by the number of integers in the interval give

\[
0\le\vartheta(t)-\vartheta(p)
\le (H+1)\log(2p).
\tag{15}
\]

Using (2),

\[
|\Delta(t)|
\le
|\Delta(p)|
+
|\vartheta(t)-\vartheta(p)|
+
(t-p)
=
O\!\left(p^{0.52}+H\log p\right)
\tag{16}
\]

uniformly on the interval.

The elementary kernel bounds used in `RE-014` and `RE-015` are

\[
|h'(t)|\ll\frac1{p^2\log p},
\qquad
0<h(t)-k(t)\ll\frac1{p^2\log p}.
\tag{17}
\]

Therefore

\[
\left|
\int_p^{p+H}I(t)\,dt
\right|
\ll
\frac{Hp^{0.52}}{p^2\log p}
+
\frac{H^2}{p^2}
+
\frac{H}{p^2\log p}.
\tag{18}
\]

After Robin normalization,

\[
\boxed{
\sqrt p\log p
\left|
\int_p^{p+H}I(t)\,dt
\right|
\ll
Hp^{-0.98}
+
\frac{H^2\log p}{p^{3/2}}
+
\frac{H}{p^{3/2}}.
}
\tag{19}
\]

Condition (3) sends all three terms to zero. This proves (4). For `H=p^alpha`, `alpha<3/4`, every term in (19) decays by a fixed positive power of `p`, and hence faster than every fixed inverse power of `log p`; this proves (5).

The horizon in (3) slightly sharpens the fixed-power formulation of `RE-014`. The `3/4` boundary is still a limitation of the deliberately cancellation-free estimate (15), not evidence for an arithmetic phase transition there.

## 3. The remote PNT tail is selection-free and is negligible beyond all logarithmic orders

`RE-015` derives from the unconditional Korobov--Vinogradov PNT remainder that, for some absolute `a>0`,

\[
|\mathcal M_*(U)|
\ll
\frac{e^{-aV(U)}}{V(U)}
+
\frac1{U\log U}.
\tag{20}
\]

This statement is global in the real input `U`; it never used clean CA selection. For `U=U_A(p)`, `RE-015` computes

\[
V(U_A(p))
=
\kappa_A\log p\,(1+o(1)),
\qquad
\kappa_A=A^{3/5}(3/5)^{1/5}.
\tag{21}
\]

Choose `A>A_0` so that `a kappa_A>1/2`. Then there is a fixed `delta_A>0` for which

\[
\sqrt p\log p\,|\mathcal M_*(U_A(p))|
\ll p^{-\delta_A+o(1)}
\tag{22}
\]

and therefore, for every fixed `M`,

\[
\boxed{
\sqrt p\log p\,\mathcal M_*(U_A(p))
=
O_{A,M}\bigl((\log p)^{-M}\bigr).
}
\tag{23}
\]

The strict inequality `A>A_0` is important: it supplies a genuine positive power margin after the external `sqrt(p)` normalization.

Now use the exact real-input tail decomposition

\[
\mathcal M_*(p)
=
\int_p^{p+p^\alpha}I(t)\,dt
+
\int_{p+p^\alpha}^{U_A(p)}I(t)\,dt
+
\mathcal M_*(U_A(p)).
\tag{24}
\]

Equations (5) and (23) prove (7). Unlike the first-order `o(1)` splice in `RE-015`, both discarded pieces are now seen to be below **every fixed inverse-logarithmic order** along the universal self-tangent selector.

## 4. The complete Robin tax can therefore be attached to the finite annulus

`RE-021` proves for every regular self-tangent state, without any clean-boundary hypothesis,

\[
\sqrt p\log p\,(\log G(C)-\gamma)
=
\mathscr Y(p)-\mathcal K(C),
\tag{25}
\]

where the complete deterministic CA tax has, for every fixed `m>=1`,

\[
\mathcal K(C)
=
\sqrt{\frac L\ell}
\left(
2+\sum_{j=1}^{m}(-1)^j\frac{j!}{\ell^j}
\right)
+
O_m(L^{-m-1}).
\tag{26}
\]

Take `M` in (7) larger than `m+1` and use `log p=L+o(1)` beyond every inverse-logarithmic order, again from (12). Substitution of (7) into (25)--(26) gives (9). Expanding `ell` as in `RE-016` and `RE-021` gives (10).

Hence the higher-layer/tied chamber does not introduce an additional first-order or logarithmic-order height channel outside the annulus. Any effect of exceptional adjacent transitions on a counterexample must enter through **which self-tangent states are selected**, not through a different asymptotic decomposition of their Robin height.

## 5. Counterexamples force the same annular excursion in every transition chamber

If a selected self-tangent state is a Robin counterexample, then

\[
\log G(C)-\gamma>0.
\]

Equation (10) therefore implies

\[
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)}I(t)\,dt
>
2\sqrt2
-
\frac{\sqrt2(2+\log2)}{\log p}
+
O((\log p)^{-2}).
\tag{27}
\]

Taking the lower limit along any unbounded counterexample sequence proves (11).

Under hypothetical RH failure, `RE-001` supplies infinitely many regular self-tangent CA counterexample peaks. `RE-021` already showed that all of them must cross the mixed-race threshold even if their adjacent CA transitions are exceptional. Equation (11) now shows that the required signed mass must also be carried inside the same finite PNT annulus. Thus concentration on higher-layer or tied event gaps is not a way to move the first-order height obligation either into a short local window or into an arbitrarily remote tail.

For local peaks, `RE-017`--`RE-020` remain complementary rather than superseded. They control how exceptional adjacent transitions can be hosted by ordinary-prime envelopes and show that fixed envelopes force super-lacunary event-ladder synchronization. The present result says that every such host, if it is a counterexample, must simultaneously support the annular mixed-race excursion (11). It does not show that super-lacunarity makes that excursion impossible.

## 6. A useful reciprocal-error corollary, and why it is not by itself progress

There is a simpler necessary condition worth recording as a consistency check. The exact finite Euler-product factorization is

\[
\log G(C)-\gamma
=
E(p)-T(C)+\log\frac{\log p}{\log X},
\tag{28}
\]

with

\[
\mathcal E_{\pi_\ell}(p)
=
\sqrt p\log p\,E(p).
\]

Since `X>p`, a Robin counterexample satisfies exactly

\[
\mathcal E_{\pi_\ell}(p)
>
\sqrt p\log p\,T(C)
+
\sqrt p\log p\log\frac{\log X}{\log p}.
\tag{29}
\]

The universal exponent-tail analysis inherited from `RE-016` gives

\[
\sqrt p\log p\,T(C)=\sqrt2+O((\log p)^{-1}),
\tag{30}
\]

while, with `d=X-p=O(p^0.52)`,

\[
\sqrt p\log p\log\frac{\log X}{\log p}
=
\frac d{\sqrt p}+O(p^{-0.46}).
\tag{31}
\]

Consequently every unbounded self-tangent counterexample sequence has

\[
\liminf \mathcal E_{\pi_\ell}(p)\ge\sqrt2.
\tag{32}
\]

This removes the bounded-envelope hypothesis from the reciprocal-error half of the joint corner recorded in `RE-021`. However, (29) is algebraically the original height factorization, so it is **not** promoted as the main mechanism of this finding and supplies no independent upper bound. The substantive gain is (7)--(11): unconditional short-horizon and PNT-tail estimates force the surviving mixed-race obligation into a finite, explicitly scaled annulus.

## 7. Prior art and novelty boundary

The external ingredients are already anchored in `SOURCES.md`.

- Runbo Li's unconditional short-interval theorem is used only through the consequence, already established in `RE-021`, that the next-prime displacement of the universal self-tangent first-layer frontier is `O(p^0.52)`.
- Chiara Bellotti's Korobov--Vinogradov-scale PNT remainder supplies the remote-tail estimate (20), exactly as in `RE-015`.
- Bhattacharya--Martin--Simpson identify the global normalized reciprocal/standard prime-error geometry and show that one-sided global control of the mixed difference is RH-equivalent; `RE-009` supplies the exact normalization dictionary.
- Mantovanelli's recent prime-layer workload preprint is the closest prior art for self-tangent CA event geometry and prime-frontier decompositions, but its public description and companion do not supply the two-sided future-tail localization proved here.

A fresh targeted search of current Robin/CA, Mertens-product, weighted-prime-error, and PNT-tail literature did not locate the specific conclusion that the mixed-race height of **every** regular self-tangent CA state can be localized, to all inverse-logarithmic orders, between the lower scale `p+p^alpha` and the PNT-inverted upper scale `U_A(p)` independently of the adjacent CA transition chamber.

No blanket external novelty claim is made. The mathematical step is a repository-level synthesis with a genuine hypothesis removal: `RE-021` supplies the universal selected endpoint estimate that `RE-014` lacked, while `RE-015` supplies a selection-free upper truncation. The new durable consequence is that the clean/exceptional distinction disappears not only from the height threshold but also from its two-sided scale localization.

No new source anchor is needed.

## 8. Falsification boundaries and current frontier

The self-tangent hypothesis remains essential. Equation (2) is not asserted at arbitrary primes; without the CA relation (13), the known unconditional global PNT remainder does not give a `p^0.52` pointwise bound for `vartheta(p)-p`. The lower horizon must satisfy (3); the proof uses no cancellation in short intervals and gives no statement at a fixed positive multiple of `p^(3/4)`. For the all-logarithmic statement (7)--(10), `alpha<3/4` and `A>A_0` are fixed independently of `p`.

The annulus remains enormous. Its upper endpoint is super-polynomial in `p`, and the theorem localizes the **direct integral contribution**, not causal dependence: prime data before the lower cutoff are carried forward through `Delta(t)`. Nothing here bounds the annular integral by less than `2sqrt(2)` or prevents it from taking the required sign on a sparse CA-selected sequence.

The remaining obstruction is therefore sharper than after `RE-021`. Every hypothetical self-tangent counterexample, clean or exceptional, must align the CA selector with a positive mixed Mertens--Chebyshev excursion of size `2sqrt(2)` carried inside the finite PNT annulus (11). Exceptional local peaks may additionally have to satisfy the event-ladder constraints of `RE-017`--`RE-020`, but they no longer possess a separate height-localization escape. A positive continuation must control this selector-conditioned annular correlation, or derive a new restriction on the selector strong enough to make such annular excursions impossible on its host set.