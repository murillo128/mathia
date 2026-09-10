# RE-021 — self-tangent Robin height threshold survives exceptional CA boundaries

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + CLEAN-HYPOTHESIS-REMOVAL + UNIVERSAL-SELF-TANGENT-HEIGHT-DICTIONARY + BOUNDED-ENVELOPE-JOINT-RACE-LOCK + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-008`, `RE-010`, and `RE-016` derive the endpoint-subtracted Mertens height dictionary, the sharp `2sqrt(2)` mixed-race threshold, and the all-orders logarithmic CA tax inside the clean first-layer chamber. Their local clean selectors really do need first-layer adjacent transitions. The **height splice does not**. At any regular self-tangent CA state, the largest active first-layer prime supplies the same exact Euler-product/selector cancellation, and the ordinary next-prime bound automatically gives all the displacement control used by the height asymptotics.

Consequently the mixed-race threshold is not an escape hatch of the higher-layer/tied chamber. Let `C` be any sufficiently large regular self-tangent colossally abundant state, not necessarily a local peak, and put

\[
X:=\log C.
\]

Let `p` be the largest prime whose first-layer event is active at `X`, and let `q` be the next ordinary prime. Then

\[
\boxed{p<X<q+1,\qquad X-p=O(p^{0.52}).}
\tag{1}
\]

Writing

\[
\Phi_{\ge2}(X)
:=\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\\eta_{r,j}<X}}\log r,
\qquad
\Delta(p):=\vartheta(p)-p,
\]

regular self-tangency gives the exact frontier split

\[
\boxed{X=\vartheta(p)+\Phi_{\ge2}(X),}
\qquad
\boxed{\Delta(p)=X-p-\Phi_{\ge2}(X).}
\tag{2}
\]

Define, as in `RE-008`--`RE-010`,

\[
h(t):=\frac{-\log(1-t^{-1})}{\log t},
\qquad
k(t):=\frac1{t\log t},
\]

\[
E(p):=\sum_{r\le p}-\log(1-r^{-1})-\gamma-\log\log p,
\]

\[
\mathcal M_*(p):=E(p)-\Delta(p)h(p),
\]

and, if `C=product_(r<=p) r^(a_r)`,

\[
T(C):=-\sum_{r\le p}\log(1-r^{-(a_r+1)}).
\]

Then every such regular self-tangent state satisfies the same exact identity previously proved only in the clean chamber,

\[
\boxed{
\log G(C)-\gamma
=
\mathcal M_*(p)-T(C)-\Phi_{\ge2}(X)h(p)+Q(p,X),
}
\tag{3}
\]

where

\[
Q(p,X):=\int_p^X\bigl(h(p)-k(t)\bigr)\,dt\ge0.
\tag{4}
\]

Moreover the complete normalized CA tax

\[
\mathcal K(C)
:=\sqrt p\log p\,
\bigl(T(C)+\Phi_{\ge2}(X)h(p)-Q(p,X)\bigr)
\tag{5}
\]

has the **same all-orders logarithmic normal form** as in `RE-016`. Put

\[
L:=\log X,
\qquad
\ell:=\frac12W(2XL).
\tag{6}
\]

For every fixed integer `m>=1`,

\[
\boxed{
\mathcal K(C)
=
\sqrt{\frac L\ell}
\left(
2+\sum_{k=1}^{m}(-1)^k\frac{k!}{\ell^k}
\right)
+O_m(L^{-m-1}).
}
\tag{7}
\]

In particular,

\[
\boxed{
\sqrt p\log p\,\bigl(\log G(C)-\gamma\bigr)
=
\mathscr Y(p)-2\sqrt2
+\frac{\sqrt2(2+\log2)}{\log p}
+O\!\left((\log p)^{-2}\right),
}
\tag{8}
\]

where

\[
\mathscr Y(p):=\sqrt p\log p\,\mathcal M_*(p).
\]

Thus every unbounded sequence of regular self-tangent Robin counterexamples, **including sequences whose adjacent CA transitions contain higher layers or ties**, necessarily satisfies

\[
\boxed{
\liminf \mathscr Y(p)\ge2\sqrt2.
}
\tag{9}
\]

Under RH failure, `RE-001` supplies infinitely many regular self-tangent CA counterexamples, so (9) is a universal source-selection obligation for the self-tangent reduction rather than a clean-chamber obligation.

The bounded-envelope branch becomes still more rigid. If `C` is a regular self-tangent CA local peak whose ordinary-prime envelope in `RE-017` has fixed width `g(C)<=G`, then the frontier prime `p` above is exactly the left envelope prime and

\[
0<X-p<G+1.
\tag{10}
\]

For `L_p=log p` and

\[
\ell_p:=\frac12W(2pL_p),
\]

the same second-layer frontier analysis used by `RE-016` now turns (2) into

\[
\boxed{
\frac{\vartheta(p)-p}{\sqrt p}
=-\sqrt{\frac{L_p}{\ell_p}}
+O_{G,M}(L_p^{-M})
\qquad\text{for every fixed }M>0.
}
\tag{11}
\]

Hence

\[
\boxed{
\frac{\vartheta(p)-p}{\sqrt p}
=-\sqrt2
+\frac{\sqrt2\log2}{2\log p}
+O_G\!\left((\log p)^{-2}\right).
}
\tag{12}
\]

Combining this endpoint lock with the exact mixed-race dictionary of `RE-009`,

\[
\mathscr Y(p)
=\mathcal E_{\pi_\ell}(p)-\lambda(p)\mathcal E_\vartheta(p),
\qquad
\lambda(p)=-p\log(1-p^{-1})=1+O(p^{-1}),
\tag{13}
\]

shows that every unbounded fixed-envelope counterexample sequence must hit the joint prime-race corner

\[
\boxed{
\mathcal E_\vartheta(p)\longrightarrow-\sqrt2,
\qquad
\liminf\mathcal E_{\pi_\ell}(p)\ge\sqrt2.
}
\tag{14}
\]

`RE-020` independently proves that, for fixed `G`, the CA event hosts capable of carrying such peaks have counting function only `O_G(1+log^* log Z)` up to event coordinate `Z`, and any infinite fixed-base subsequence has event coordinates separated by event-scale power jumps. Since (10) gives `p=X+O_G(1)`, the same super-lacunary host restriction applies to the frontier primes in (14). The bounded-envelope escape is therefore no longer merely “a sparse event-ladder collision” plus a separate unspecified Robin-height problem: it requires a **specific opposite-sign joint Mertens/Chebyshev race excursion on those super-lacunary CA-selected hosts**.

## 1. The first-layer frontier exists independently of the adjacent CA transitions

For a prime `r`, `RE-003` gives

\[
r\le\eta_{r,1}<r+1,
\tag{15}
\]

and the first-layer event order is exactly ordinary prime order. Because `C` is regular, `X` is not itself an event coordinate. Let `p` be the largest prime with

\[
\eta_{p,1}<X
\]

and let `q` be the next prime. Then

\[
p\le\eta_{p,1}<X<\eta_{q,1}<q+1,
\]

which proves the first part of (1) and the useful deterministic bound

\[
0<X-p<q-p+1.
\tag{16}
\]

The current unconditional consecutive-prime estimate already anchored in `SOURCES.md` gives

\[
q-p=O(p^{0.52}),
\tag{17}
\]

so (1) follows. In particular

\[
\frac Xp=1+O(p^{-0.48}),
\qquad
\log X-\log p=O(p^{-0.48}),
\tag{18}
\]

and these errors are smaller than every fixed inverse power of `log p`.

No local-peak condition and no assumption on the layers at the two **adjacent CA transitions around `X`** has entered. The first-layer frontier is a separate global coordinate of the same event state.

## 2. Self-tangency supplies the selector needed by the height splice

`RE-001` gives, at every regular self-tangent state,

\[
X=\Phi(X),
\qquad
\Phi(X)=\sum_{\eta_{r,j}<X}\log r.
\tag{19}
\]

By the definition of `p`, the active first layers are exactly the primes `r<=p`. Splitting (19) by layer therefore gives (2):

\[
X=\vartheta(p)+\Phi_{\ge2}(X).
\]

The factorization of the CA state at the same coordinate is

\[
C=\prod_{r\le p}r^{a_r},
\]

where `a_r` is exactly the number of active layers of `r`. Therefore the finite Euler-product bookkeeping used in `RE-008` is valid without clean adjacent boundaries:

\[
\log G(C)-\gamma
=E(p)-T(C)+\log\frac{\log p}{\log X}.
\tag{20}
\]

Write `Delta(p)=vartheta(p)-p`. Exact Stieltjes summation, already reconstructed in `RE-008`, gives

\[
E(p)=\mathcal M_*(p)+\Delta(p)h(p).
\tag{21}
\]

Using (2),

\[
\Delta(p)=X-p-\Phi_{\ge2}(X),
\tag{22}
\]

while

\[
\log\frac{\log p}{\log X}
=-\int_p^Xk(t)\,dt.
\tag{23}
\]

Substituting (21)--(23) into (20) yields (3)--(4). The endpoint Chebyshev term therefore cancels at **every regular self-tangent state** when one references the last active first-layer prime. Clean adjacency was one sufficient way to identify that prime, not a necessary hypothesis for the cancellation itself.

This corrects the scope boundary stated in `RE-008` and `RE-010`: their formulas are valid on the clean chamber as proved there, but the clean-boundary condition is not mathematically load-bearing for the height identity or its asymptotic tax. It remains load-bearing for the local residual-window and lower-tail localization results `RE-006`, `RE-007`, `RE-014`, and `RE-015`.

## 3. The all-orders tax proof also survives once the frontier displacement is restored

The only pieces of the `RE-016` tax proof that refer to the clean chamber are the availability of the same first-layer endpoint `p` and the fact that `X-p` is sufficiently small. Sections 1--3 of that proof depend only on the event threshold at `X`:

- the active second layers form an initial prime segment with frontier `P_2(X)`;
- `Phi_2(X)/sqrt(X)` has the Lambert-`W` normal form `sqrt(L/ell)` to every fixed inverse-logarithmic order;
- all layers `j>=3` are below every such logarithmic order after Robin normalization;
- primes with exponent one are exactly `P_2(X)<r<=p`, and their reciprocal-square tail produces the same exponential-integral expansion;
- primes of exponent at least two contribute below every fixed inverse-logarithmic order.

Those statements use only that `a_r` counts active layers at the regular self-tangent coordinate and that `p/X->1` beyond logarithmic resolution. Equation (18) gives the latter for every regular self-tangent state.

For the geometric term, `RE-008` proved for `d=X-p`

\[
0\le Q(p,X)
\ll
\frac d{p^2\log p}
+\frac{d^2}{p^2\log p}.
\tag{24}
\]

By (1),

\[
\sqrt p\log p\,Q(p,X)
=O(p^{-0.98})+O(p^{-0.46}),
\tag{25}
\]

again beyond every inverse-logarithmic order. Thus every step that produced the tax expansion in `RE-016` remains valid, proving (7). Expanding `ell` as there then gives (8).

The significance is not a new value of the deterministic constant. It is the disappearance of the previously advertised clean/exceptional dichotomy at the **height** level. Higher-layer or tied adjacent transitions complicate the peak selector, but they do not change the first-order or all-logarithmic-order CA tax once self-tangency fixes the state.

## 4. Fixed ordinary envelopes add a precise Chebyshev coordinate

Now impose the local-peak setting of `RE-017` and a fixed ordinary envelope `g(C)<=G`. Let `u<v` be the consecutive ordinary primes whose first-layer events enclose the two actual adjacent CA transition coordinates

\[
\eta_{u,1}\le\eta_-<X<\eta_+\le\eta_{v,1}.
\tag{26}
\]

There is no first-layer event between `eta_-` and `eta_+`. Therefore `u` is exactly the largest active first-layer prime at `X`, so `p=u` in the notation above. Since `v-u=g(C)`, (15) and (26) imply

\[
0<X-p<\eta_{v,1}-p<g(C)+1\le G+1,
\]

which is (10).

The second-layer analysis in `RE-016` gives, for every fixed `M`,

\[
\frac{\Phi_{\ge2}(X)}{\sqrt X}
=
\sqrt{\frac{L}{\ell}}+O_M(L^{-M}).
\tag{27}
\]

Insert (10) into the exact selector (22), divide by `sqrt(p)`, and replace `X` by `p` in the smooth Lambert-`W` term; the replacement error is `O_G(p^{-1})`, again smaller than every inverse-logarithmic order. This proves (11). The expansion

\[
\sqrt{\frac{L_p}{\ell_p}}
=\sqrt2\left(1-\frac{\log2}{2L_p}+O(L_p^{-2})\right)
\tag{28}
\]

gives (12).

Thus fixed-envelope self-tangent peaks do not sample an arbitrary value of the ordinary Chebyshev race. They force the normalized theta error into an asymptotically vanishing neighborhood of `-sqrt(2)`.

For a Robin counterexample, (8) gives `mathscr Y(p)>mathcal K(C)`, so (7) implies

\[
\liminf\mathscr Y(p)\ge2\sqrt2.
\tag{29}
\]

Using (13) together with (12) yields (14). Equivalently, the logarithmic Mertens-product error must be positive at least at the opposite square-root scale while the theta error is pinned negatively:

\[
\mathcal E_\vartheta(p)\to-\sqrt2,
\qquad
\liminf\mathcal E_{\pi_\ell}(p)\ge\sqrt2.
\]

This is a necessary condition, not an assertion that the joint corner is impossible.

## 5. Finite exceptional-boundary control

The first local peak in `RE-005`,

\[
C_1=2021649740510400
=2^6 3^3 5^2 7^2\,11\,13\,17\,19\,23\,29\,31,
\]

is a useful regression witness because its adjacent CA transitions are **not clean**: the last included layer is `(7,2)` and the next excluded layer is `(3,4)`. Its first-layer frontier is nevertheless `p=31` and

\[
X=\log C_1
=35.2426902762261620743945348509\ldots.
\]

Direct high-precision reconstruction from the displayed factorization gives

\[
\vartheta(31)=26.0243817346008024648117716931\ldots,
\]

\[
\Phi_{\ge2}(X)=X-\vartheta(31)
=9.21830854162535960958276315781\ldots,
\]

so the exact frontier identity (2) is manifest even though neither adjacent transition is first-layer. Evaluating the two sides of (3) independently, with the finite Euler factors formed from the displayed exponents, gives

\[
\log G(C_1)-\gamma
=-0.0251404552529867732755005564\ldots,
\]

with agreement to better than `5e-16` under ordinary numerical quadrature for `Q`. This is only a finite normalization/sign check; the proof of (3) is algebraic and does not depend on the computation.

## 6. Prior-art boundary and what has actually changed

The ingredients are individually classical or already anchored. Alaoglu--Erdos supplies the CA layer thresholds; Robin supplies the extremal criterion and counterexample reduction; Runbo Li supplies the unconditional short-interval exponent used only for (1); Nicolas records the classical Ramanujan square-root correction; Mantovanelli's August 2026 preprint is direct prior art for self-tangent event measures and prime-frontier decompositions; Bhattacharya--Martin--Simpson is direct prior art for the joint normalized theta/logarithmic-Mertens race and the RH-equivalence of global one-sided mixed bounds.

A targeted current search also found recent work bounding a hypothetical CA counterexample between its primorial and a small power of that primorial, equivalently between `theta(p)` and a multiplicative enlargement of `theta(p)`. That is a much coarser largest-prime-factor window and does not supply the exact self-tangent frontier split (2), the endpoint cancellation (3), or the fixed-envelope joint race corner (14). It is not used as an input here.

No novelty is claimed for the `2sqrt(2)` constant, the second-layer frontier asymptotics, the Mertens/Chebyshev normalization, or the fact that the largest prime factor of a CA number is asymptotic to its logarithmic size. The mathematical delta is the **scope repair and coupling**:

\[
\text{regular self-tangency}
\Longrightarrow
\text{universal frontier height dictionary}
\Longrightarrow
\text{the same }2\sqrt2\text{ selected mixed-race threshold in every transition chamber},
\]

and, under a bounded ordinary envelope,

\[
\text{fixed-base super-lacunary event hosts}
\Longrightarrow
\mathcal E_\vartheta(p)\to-\sqrt2,
\quad
\liminf\mathcal E_{\pi_\ell}(p)\ge\sqrt2
\quad\text{for counterexamples}.
\]

The public Mantovanelli companion describes finite prime-frontier certificates, but the available source record and targeted searches did not locate this removal of first-layer adjacency from the selected height threshold or the resulting fixed-envelope joint-race condition. This is therefore recorded as a bounded Mathia derivation rather than a blanket novelty claim.

## 7. Boundaries and research consequence

The clean hypothesis has **not** disappeared from the whole Robin line. `RE-006`--`RE-007` use clean adjacent first-layer transitions to obtain a sharp local residual window, and `RE-014`--`RE-015` use that clean selector to localize the mixed-race contribution between lower and upper horizons. Those statements are not extended here. Likewise, `RE-017`--`RE-020` remain necessary to understand which higher-layer/tied event gaps can host local peaks and how sparse fixed-envelope hosts become.

What changes is the division of labor. The exceptional chamber can no longer be treated as exempt from the selected mixed-race **height** obstruction merely because its immediate CA transitions are higher-layer. Every regular self-tangent state has a canonical first-layer frontier prime and obeys the same height dictionary. The bounded-envelope branch adds an independent endpoint lock at that prime and, by `RE-020`, forces the joint race event onto an iterated-logarithmically sparse, super-lacunary host set.

This still does not prove Robin's inequality or RH. Bhattacharya--Martin--Simpson shows why a global one-sided bound on `mathscr Y` is circularly strong, and sparsity alone cannot forbid a deterministic subsequence from hitting a rare joint race region. The live source-specific problem is now sharper: **exclude or price the joint corner (14) on the CA-selected event-ladder hosts**, or extend an analogous endpoint lock to ordinary envelopes that grow with `X` strongly enough to cover the remaining self-tangent counterexample geometry.
