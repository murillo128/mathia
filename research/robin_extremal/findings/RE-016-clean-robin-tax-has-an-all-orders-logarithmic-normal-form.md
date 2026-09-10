# RE-016 — clean Robin tax has an all-orders logarithmic normal form

**Status:** `LITERATURE+DERIVED + UNCONDITIONAL-ASYMPTOTIC + ALL-LOG-ORDERS-CALIBRATION + CLEAN-SELECTED-HEIGHT-THRESHOLD + SECOND-LAYER-DOMINANCE + PRIOR-ART-BOUNDED`. `RE-008` splits the height of a sufficiently large clean regular self-tangent CA local peak into one mixed prime-race coordinate and three CA-side corrections. `RE-010` proves that the two negative corrections each contribute `sqrt(2)` at first square-root order, giving the threshold `2sqrt(2)`, but leaves their approach to that limit inside an undifferentiated `o(1)`.

That `o(1)` can be resolved much further without RH. Let

\[
C=\prod_{r\le p}r^{a_r},\qquad X:=\log C,
\]

be a sufficiently large clean regular self-tangent CA local peak, with consecutive first-layer boundary primes `p<X<q`. Keep the notation of `RE-008`,

\[
\Phi_{\ge2}(X)
:=\sum_{\substack{r\ \mathrm{prime},\ j\ge2\\\eta_{r,j}\le X}}\log r,
\qquad
T(C):=-\sum_{r\le p}\log(1-r^{-(a_r+1)}),
\]

\[
h(p):=\frac{-\log(1-p^{-1})}{\log p},
\qquad
Q(p,X):=\int_p^X\bigl(h(p)-1/(t\log t)\bigr)\,dt,
\]

and define the complete **CA tax** in the normalized height identity by

\[
\boxed{
\mathcal K(C)
:=\sqrt p\log p\,
\bigl(T(C)+\Phi_{\ge2}(X)h(p)-Q(p,X)\bigr).
}
\tag{1}
\]

Then `RE-008` is exactly

\[
\boxed{
\sqrt p\log p\,\bigl(\log G(C)-\gamma\bigr)
=\mathscr Y(p)-\mathcal K(C),
}
\tag{2}
\]

where `mathscr Y(p)=sqrt(p) log(p) M_*(p)` is the mixed standard/reciprocal prime-race coordinate identified in `RE-009`.

Put

\[
L:=\log X,
\qquad
\ell:=\frac12 W(2XL),
\tag{3}
\]

where `W` is the principal Lambert function. Equivalently, if

\[
z:=e^\ell,
\]

then

\[
\boxed{z^2\log z=XL.}
\tag{4}
\]

For every fixed integer `m>=1`, the clean CA tax has the asymptotic normal form

\[
\boxed{
\mathcal K(C)
=
\sqrt{\frac{L}{\ell}}
\left(
2+\sum_{k=1}^{m}(-1)^k\frac{k!}{\ell^k}
\right)
+O_m\!\left(L^{-m-1}\right).
}
\tag{5}
\]

In particular,

\[
\boxed{
\mathcal K(C)
=2\sqrt2
-\frac{\sqrt2\,(2+\log2)}{\log p}
+O\!\left(\frac1{(\log p)^2}\right).
}
\tag{6}
\]

Thus the exact clean Robin threshold approaches `2sqrt(2)` **from below**, with an explicit first correction. Equation (2) becomes

\[
\boxed{
\sqrt p\log p\,\bigl(\log G(C)-\gamma\bigr)
=
\mathscr Y(p)-2\sqrt2
+\frac{\sqrt2\,(2+\log2)}{\log p}
+O\!\left(\frac1{(\log p)^2}\right).
}
\tag{7}
\]

The main structural point is stronger than the first coefficient. At every fixed inverse-logarithmic order, the CA side is controlled entirely by the **second prime-power layer** and the exponent-one Euler-product tail. All layers `j>=3`, the discreteness of the second-layer frontier, the clean prime-gap displacement `X-p`, and the positive correction `Q` are smaller than every fixed power of `1/log X`. They re-enter only beyond the complete logarithmic asymptotic scale.

## 1. The second-layer frontier has a Lambert-W normal form

For the second CA layer the exact abundance increment simplifies to

\[
\lambda_{r,2}
=\log\frac{1-r^{-3}}{1-r^{-2}}
=\log\left(1+\frac1{r(r+1)}\right).
\tag{8}
\]

It is positive and strictly decreasing in `r`; division by the increasing positive function `log r` preserves strict decrease. Hence, at a fixed `X`, the active second-layer primes form an initial prime segment. Let `y=y_2(X)` be the unique real solution of

\[
\frac{\lambda_{y,2}}{\log y}
=\frac1{X\log X},
\tag{9}
\]

and let `P_2(X)` be the largest prime not exceeding `y`. Then exactly

\[
\boxed{
\Phi_2(X)=\vartheta(P_2(X)).
}
\tag{10}
\]

The elementary expansion of (8) is

\[
\lambda_{r,2}=r^{-2}\bigl(1+O(r^{-1})\bigr).
\tag{11}
\]

Therefore (9) gives

\[
y^2\log y=XL\bigl(1+O(y^{-1})\bigr).
\tag{12}
\]

The comparison point `z` from (4) satisfies the equation without the relative `O(y^{-1})`. Since the derivative of `t^2 log t` is `t(2log t+1)`, the mean-value theorem applied near `z asymp sqrt(X)` yields

\[
\boxed{y=z+O(1).}
\tag{13}
\]

The unconditional consecutive-prime input already anchored in `SOURCES.md` gives a prime in `[u-u^{0.52},u]` for every sufficiently large `u`. Applied at `u=y`,

\[
P_2(X)=z+O(z^{0.52}).
\tag{14}
\]

The Korobov--Vinogradov PNT remainder used in `RE-015` gives, after the standard transfer from `psi` to `vartheta`,

\[
\vartheta(t)-t
\ll t\exp\!\left(
-a\frac{(\log t)^{3/5}}{(\log\log t)^{1/5}}
\right)
\tag{15}
\]

for some absolute `a>0`. Both the error in (15) at `t asymp sqrt(X)` and the gap error in (14), after division by `sqrt(X)`, are smaller than `L^{-M}` for every fixed `M`. Thus (10)--(15) imply the all-log-orders replacement

\[
\boxed{
\frac{\Phi_2(X)}{\sqrt X}
=
\frac z{\sqrt X}+O_M(L^{-M})
=
\sqrt{\frac L\ell}+O_M(L^{-M})
}
\tag{16}
\]

for every fixed `M>0`, because (4) gives `z/sqrt(X)=sqrt(L/ell)`.

This is the first place where the distinction between logarithmic and power resolution matters. The actual second-layer frontier is discrete and prime-supported, but current unconditional prime distribution is already strong enough to make that discreteness invisible to **every fixed inverse power of `log X`**.

## 2. Every higher CA layer is beyond all inverse-logarithmic orders in the normalized tax

`RE-013` gives the elementary necessary condition for an active layer `(r,j)`:

\[
r^j\log r\le XL,
\tag{17}
\]

and shows that the maximal active depth is `J_*(X)=O(L)`. Chebyshev's bound `vartheta(u)=O(u)` therefore gives

\[
\begin{aligned}
\Phi_{\ge3}(X)
&:=\sum_{j=3}^{J_*(X)}\Phi_j(X)\\
&\ll (XL)^{1/3}
+L(XL)^{1/4}\\
&\ll X^{1/3}L^{1/3}.
\end{aligned}
\tag{18}
\]

Hence

\[
\boxed{
\frac{\Phi_{\ge3}(X)}{\sqrt X}
=O\!\left(X^{-1/6}L^{1/3}\right)
=O_M(L^{-M})
}
\tag{19}
\]

for every fixed `M`. This does **not** contradict the logarithmic-depth resolution barrier of `RE-013`: that finding asks for additive reconstruction of the selector itself at `O(log X)` or unit scale, whereas (19) weights the omitted mass by the Robin square-root normalization. The two questions use different resolutions.

At a clean peak, `RE-014` gives `X-p=O(p^{0.52})`, so

\[
\frac Xp=1+O(p^{-0.48}).
\tag{20}
\]

Also

\[
p\bigl[-\log(1-p^{-1})\bigr]=1+O(p^{-1}).
\tag{21}
\]

Combining (16), (19)--(21) gives, for every fixed `M`,

\[
\boxed{
\sqrt p\log p\,\Phi_{\ge2}(X)h(p)
=
\sqrt{\frac L\ell}+O_M(L^{-M}).
}
\tag{22}
\]

Thus the whole higher-layer side of the selector contributes no inverse-logarithmic correction at all. Its first possible influence occurs at a genuinely smaller, power-scale level.

## 3. The exponent-one tail is an exponential integral with the same frontier

Split `T(C)` as in `RE-010`. Because the active second-layer primes are exactly those `r<=P_2(X)`, while every ordinary prime `r<=p` has its first layer active, the primes of exponent one are exactly

\[
P_2(X)<r\le p.
\tag{23}
\]

Therefore

\[
T_1(C)
:=\sum_{\substack{r\le p\\a_r=1}}
-\log(1-r^{-2})
=
\sum_{P_2<r\le p}-\log(1-r^{-2}).
\tag{24}
\]

Since

\[
-\log(1-r^{-2})=r^{-2}+O(r^{-4}),
\tag{25}
\]

the `r^{-4}` tail is polynomially negligible here. For the main reciprocal-square tail, Stieltjes summation against `vartheta` gives

\[
\sum_{r>u}\frac1{r^2}
=
\int_u^\infty\frac{dt}{t^2\log t}
+O\!\left(
\frac{e^{-aV(u)}}{u\log u}
\right),
\tag{26}
\]

with the same PNT scale `V` as in `RE-015`. The main integral is the standard exponential integral:

\[
\int_u^\infty\frac{dt}{t^2\log t}
=
E_1(\log u),
\qquad
E_1(v):=\int_v^\infty\frac{e^{-s}}s\,ds.
\tag{27}
\]

The omitted tail above `p` contributes `O((p log p)^{-1})`, which is polynomially small after multiplication by `sqrt(p)log p`. Equations (13)--(15) likewise allow `P_2` to be replaced by `z` at every fixed logarithmic order. Consequently, for every fixed `m>=1`,

\[
\sqrt p\log p\,T_1(C)
=
\sqrt X L\,E_1(\ell)+O_m(L^{-m-1}).
\tag{28}
\]

The classical asymptotic expansion

\[
E_1(\ell)
=
\frac{e^{-\ell}}\ell
\left(
1+\sum_{k=1}^{m}(-1)^k\frac{k!}{\ell^k}
+O_m(\ell^{-m-1})
\right)
\tag{29}
\]

and the exact relation `z=e^ell`, `z^2 ell=XL` yield

\[
\boxed{
\sqrt p\log p\,T_1(C)
=
\sqrt{\frac L\ell}
\left(
1+\sum_{k=1}^{m}(-1)^k\frac{k!}{\ell^k}
\right)
+O_m(L^{-m-1}).
}
\tag{30}
\]

The remaining exponent tail is already controlled much more strongly by `RE-010`:

\[
T_{\ge2}(C)=O(X^{-2/3}).
\tag{31}
\]

Hence

\[
\boxed{
\sqrt p\log p\,T_{\ge2}(C)=O_M(L^{-M})
}
\tag{32}
\]

for every fixed `M`. Just as on the selector side, the entire logarithmic asymptotic series of the exponent-tail correction comes from the same second-layer frontier.

## 4. The geometric correction and clean displacement are also beyond all log orders

Write `d=X-p`. `RE-008` proves

\[
0\le Q(p,X)
\ll
\frac{d}{p^2\log p}
+
\frac{d^2}{p^2\log p}.
\tag{33}
\]

Together with `d=O(p^{0.52})`,

\[
\sqrt p\log p\,Q(p,X)
\ll p^{-0.98}+p^{-0.46},
\tag{34}
\]

which is smaller than every fixed inverse power of `log p`. The same is true of replacing `sqrt(p)log p` by `sqrt(X)L` in the preceding normalized terms, by (20).

Thus the only terms surviving at inverse-logarithmic resolution are (22) and (30). Adding them and subtracting the negligible `Q` proves (5).

This gives a useful hierarchy of scales. `RE-013` shows that exact reconstruction of the **selector** requires logarithmically many prime layers. By contrast, the normalized **height tax** forgets all but the second layer to every fixed logarithmic order. The deep CA tower is therefore structurally essential for locating a self-tangent state but asymptotically invisible in the Robin tax until one asks for precision beyond all powers of `1/log X`.

## 5. The first correction is explicit and lowers the clean threshold

From (3), `2ell=W(2XL)`. Equivalently,

\[
2\ell+\log\ell=L+\log L.
\tag{35}
\]

Solving this elementary implicit relation gives

\[
\ell
=
\frac L2+\frac{\log2}{2}
-\frac{\log2}{2L}
+O(L^{-2}).
\tag{36}
\]

In particular,

\[
\sqrt{\frac L\ell}
=\sqrt2\left(
1-\frac{\log2}{2L}+O(L^{-2})
\right),
\qquad
\frac1\ell=\frac2L+O(L^{-2}).
\tag{37}
\]

Taking `m=1` in (5) gives

\[
\begin{aligned}
\mathcal K(C)
&=
\sqrt{\frac L\ell}\left(2-\frac1\ell\right)
+O(L^{-2})\\
&=
2\sqrt2
-\frac{\sqrt2(2+\log2)}L
+O(L^{-2}).
\end{aligned}
\tag{38}
\]

Since `log X-log p=O(p^{-0.48})`, replacing `L=log X` by `log p` changes (38) only beyond the displayed order. This proves (6), and (7) follows from the exact height split (2).

The sign of the correction is worth retaining: the CA tax is eventually **smaller** than `2sqrt(2)` by about

\[
\frac{\sqrt2(2+\log2)}{\log p}.
\tag{39}
\]

Thus `RE-010`'s constant threshold is correct at first order but slightly conservative at finite logarithmic scale. A clean Robin counterexample would satisfy the sharper necessary condition

\[
\mathscr Y(p)
>
2\sqrt2
-\frac{\sqrt2(2+\log2)}{\log p}
+O\!\left((\log p)^{-2}\right).
\tag{40}
\]

This does not make the mixed-race obligation easier to prove or disprove globally. It calibrates exactly what the CA geometry asks of the selected source coordinate near the critical threshold.

## 6. Prior art, adversarial checks, and research consequence

The layer threshold structure is classical Alaoglu--Erdos territory, and Mantovanelli's August 2026 preprint is already the closest prior art for the self-tangent event measure, workload, moment hierarchy, and prime-frontier organization. No novelty is claimed for splitting the event measure by prime-power layer or for using a frontier description. The Mathia-specific step here is narrower: insert that layer structure into the exact selector/height splice of `RE-008` and show that the **complete CA tax in the clean selected Robin height has an unconditional all-orders inverse-logarithmic normal form**, with all deeper layers relegated beyond that scale.

Ramanujan's classical RH-conditional divisor-sum expansion, in the modern treatment of Nicolas already anchored in `SOURCES.md`, also resolves the leading `sqrt(log n)` correction together with a zeta-zero term. It does not supply (5): it assumes RH and does not separate the CA tax from the mixed prime-race source selected in `RE-009`. Equation (5) is instead unconditional and deliberately leaves `mathscr Y(p)` untouched. A targeted search for the explicit coefficient in (6), for an all-orders logarithmic clean-CA tax expansion, and for a Lambert-W/exponential-integral version of this selected threshold did not locate the same statement. This is a bounded novelty claim, not evidence that the asymptotic techniques themselves are new.

Several checks are load-bearing. The result applies only to the clean regular self-tangent local-peak chamber; the exceptional higher-layer/tied chamber of `RE-004` is untouched. The use of the `0.52` prime-gap exponent is only to make the discrete second-layer frontier invisible at every inverse-logarithmic order; any fixed exponent strictly below `1` would suffice for that role. The Korobov--Vinogradov PNT remainder likewise enters only to push the ordinary-prime discrepancy below every inverse-logarithmic order, not to control the RH-equivalent mixed coordinate `mathscr Y`.

Most importantly, (5) does **not** produce a one-sided bound on `mathscr Y`. `RE-009` shows that such a global bound would already be RH-equivalent. Nor does the full logarithmic expansion resolve the first genuinely power-scale correction: after all inverse-logarithmic terms are removed, the third CA layer is of normalized size about `X^{-1/6}`, while the currently available unconditional pointwise PNT remainder at the second-layer frontier is much larger than any fixed negative power of `X`. The all-orders logarithmic normal form therefore marks a real boundary: logarithmic sharpening of the CA tax is essentially solved, but pushing the deterministic calibration to the next power scale again encounters prime-distribution information.

The live clean-chamber problem remains the source-selected mixed race isolated by `RE-009`, `RE-014`, and `RE-015`. The useful change is that future arguments need not spend effort refining deterministic CA corrections at any fixed logarithmic order: those corrections are explicit through (5). Any genuinely new exclusion must exploit the selector's correlation with `mathscr Y`, obtain power-scale information beyond the current PNT frontier, or force hypothetical counterexamples into the exceptional transition chamber.