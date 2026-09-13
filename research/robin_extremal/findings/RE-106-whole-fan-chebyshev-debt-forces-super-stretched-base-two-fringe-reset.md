# RE-106 — whole-fan Chebyshev debt forces super-stretched base-two fringe reset

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + GLOBAL-FAN-THRESHOLD-WIDTH + CORRECTED-CHEBYSHEV-DEBT + RAW-FRINGE-RESET-PRICING + BASE-TWO-HOST-LOCK + EXTREME-STRETCH-DICHOTOMY + ASSEMBLY-NARROWING + PRIOR-ART-AUDITED`.

`RE-104` leaves two global assembly regimes above the current two-sided first-layer frontier: many exposed ordinary-prime-gap chambers, or a very large physical stretch. `RE-105` then shows that higher-layer mass cannot cancel the Chebyshev debt of a matched `0 -> 0` run, while leaving unmatched fringe behavior as the apparent sign interruption. The global corrected coordinate of `RE-076` allows a sharper splice: **matched runs are not needed at all to accumulate a power-scale Chebyshev debt across the whole compact threshold fan.** The only way the *raw* Chebyshev deficit can erase that debt is for the final selected point itself to carry the one unmatched fringe prime; `RE-063` then forces that endpoint onto the lacunary deep base-two successor ladder. Quantitatively, the fringe atom can be large enough only after a dramatically stronger physical stretch than the low-complexity escape of `RE-104`.

Assume RH is false and write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho.
\]

For the direct interface with `RE-102`--`RE-104`, assume

\[
\Theta>\Theta_*:=\frac{265657}{307200}=0.8647688802\ldots
\tag{1}
\]

and fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1-\Theta_*).
\tag{2}
\]

Work on one sufficiently late common positive rightmost CA fan from `RE-040`. For every selected state `C` write

\[
Y_C:=\log C,
\qquad
Z_C(b):=Z_b(C),
\qquad
H_\vartheta(Z):=Z-\vartheta(Z),
\tag{3}
\]

and let `delta_vartheta(Z)` be the binary first-layer fringe correction of `RE-059`. Retain the globally increasing corrected coordinate of `RE-076`,

\[
\widehat H(C,b)
:=H_\vartheta(Z_C(b))+\delta_\vartheta(Z_C(b))
=Z_C(b)-\log\operatorname{rad}(C).
\tag{4}
\]

Let `L` and `R` denote the selected fan points at the left and right ends of `J`, with the usual rightmost tie convention, and put

\[
X_{\mathcal B}:=\min_{b\in J}Y_{C_{\mathcal B}(b)},
\qquad
W_{\mathcal B}:=\max_{b\in J}Y_{C_{\mathcal B}(b)},
\qquad
R_{\mathcal B}:=\frac{W_{\mathcal B}}{X_{\mathcal B}}.
\tag{5}
\]

The monotone fan orientation makes `Y_L=X_B` and `Y_R=W_B`, up to the harmless possibility that one endpoint cell persists over an interval. Then there is a constant `c_J>0`, independent of the late block, such that

\[
\boxed{
\widehat H_R-\widehat H_L
\ge
c_J X_{\mathcal B}^{\,1-b_1}\log X_{\mathcal B}.
}
\tag{6}
\]

This uses **every threshold cell**, not a matched subrun. Across switches the corrected coordinate only increases, regardless of fringe pattern, packet depth, or packet cardinality.

Since the raw deficit differs from `widehat H` only by the current fringe atom,

\[
H_{\vartheta,R}-H_{\vartheta,L}
=
(\widehat H_R-\widehat H_L)
+\delta_{\vartheta,L}-\delta_{\vartheta,R},
\tag{7}
\]

and `delta_(vartheta,L)>=0`, equation (6) gives the whole-fan raw bound

\[
\boxed{
H_{\vartheta,R}-H_{\vartheta,L}
\ge
c_J X_{\mathcal B}^{\,1-b_1}\log X_{\mathcal B}
-\log(X_{\mathcal B}R_{\mathcal B})-O_J(1).
}
\tag{8}
\]

Consequently, if the raw Chebyshev deficit fails even to increase across the full fan,

\[
H_{\vartheta,R}\le H_{\vartheta,L},
\tag{9}
\]

then necessarily

\[
\boxed{
\log R_{\mathcal B}
\ge
c_J X_{\mathcal B}^{\,1-b_1}\log X_{\mathcal B}
}
\tag{10}
\]

for all sufficiently late blocks after decreasing `c_J` if necessary. In particular

\[
\boxed{
R_{\mathcal B}
\ge
\exp\!\left(
 c_J X_{\mathcal B}^{\,1-b_1}\log X_{\mathcal B}
\right).
}
\tag{11}
\]

Moreover, the reset case (9) forces `delta_(vartheta,R)>0`. By `RE-063`, the terminal selected state is then a fringe host whose **immediate physical CA successor quotient is exactly `2`**. Its outgoing event coordinate is one deep base-two event

\[
\xi_R=\eta_{2,j},\qquad j\to\infty,
\tag{12}
\]

with

\[
\lfloor\eta_{2,j}\rfloor=r_R\ \text{prime},
\qquad
\frac{\log2}{2}-o_J(1)
\le\{\eta_{2,j}\}<\frac12.
\tag{13}
\]

Thus unmatched fringe behavior is not a generic local escape from `RE-105`. To erase the debt accumulated by the entire compact fan, the fan must end after a **super-stretched transport** at one of the logarithmically sparse deep base-two predecessor states.

The exponent in (10) is especially strong on the current `RE-104` regime. Since `b_1<1-Theta_*`,

\[
1-b_1>\Theta_*=0.8647688802\ldots .
\tag{14}
\]

By contrast, the `RE-104` complexity/stretch exponent is

\[
\kappa_J=\frac{77}{100}-2b_1,
\tag{15}
\]

and the exact difference is

\[
\boxed{
(1-b_1)-\kappa_J
=\frac{23}{100}+b_1>\frac{23}{100}.
}
\tag{16}
\]

Even the extreme `N_B=O(1)` low-complexity escape in `RE-104` therefore asks only for `log R_B` at the `X_B^(kappa_J-o(1))` scale, whereas a complete raw-Chebyshev reset asks for the strictly larger `X_B^(1-b_1) log X_B` scale. The two escape mechanisms should no longer be treated as equivalent.

## 1. Every positive-width threshold cell pays corrected Chebyshev transport

Fix one exposed selected state `C` and one interior threshold `b` of its cell. Put

\[
Y:=Y_C,
\qquad
h:=\log G(C)-\gamma>0,
\qquad
a:=1-e^{-h}.
\tag{17}
\]

The exact tangent equation of `RE-040` is

\[
g(Z_C(b))=g(Y)-\frac{ba}{Y},
\qquad
g(x)=\frac1{x\log x}.
\tag{18}
\]

Inside the cell `Y` and `a` are fixed. Differentiating (18) gives exactly

\[
\boxed{
Z_C'(b)
=\frac{a}{Y\,[-g'(Z_C(b))]}
=
\frac{a\,Z_C(b)^2(\log Z_C(b))^2}
{Y(\log Z_C(b)+1)}.
}
\tag{19}
\]

`RE-040` supplies two uniform late-fan facts. First,

\[
\frac{Z_C(b)}{Y}\to1
\tag{20}
\]

uniformly in all selected states and `b in J`. Second, the common quantitative false-RH witness gives the amplitude floor

\[
e^h-1\ge c_0Y^{-b}
\ge c_0Y^{-b_1}.
\tag{21}
\]

Since `h log Y ->0` uniformly, `a=(e^h-1)/(1+e^h-1)`, so for all sufficiently late blocks

\[
\boxed{
a\ge c_JY^{-b_1}.}
\tag{22}
\]

Substituting (20)--(22) into (19),

\[
\boxed{
Z_C'(b)
\ge c_JY^{1-b_1}\log Y
\ge c_JX_{\mathcal B}^{1-b_1}\log X_{\mathcal B}.
}
\tag{23}
\]

The endpoint-corrected identity (4) makes the same derivative the exact within-cell Lyapunov speed:

\[
\frac d{db}\widehat H(C,b)=Z_C'(b).
\tag{24}
\]

The finitely many exposed cell interiors partition `J` up to breakpoints of measure zero. Summing (24) and using (23) therefore gives

\[
\sum_C\int_{I_C^\circ}d\widehat H
\ge
c_JX_{\mathcal B}^{1-b_1}\log X_{\mathcal B}\,|J|.
\tag{25}
\]

Absorb the fixed positive factor `|J|` into `c_J`. `RE-076` proves that every exposed switch has an additional **strictly positive** corrected increment, including arbitrary mixed and unmatched packets. Dropping all those positive switch contributions proves (6).

This derivation also explains why the number of exposed states does not appear in (6). Refining the fan into many cells partitions the same threshold width; it does not duplicate it. `RE-079` gives the deeper reason: the corrected Chebyshev and corrected Mertens motions are moments of one positive transport measure, so one cannot manufacture extra same-scale source budget merely by counting more exposed vertices.

## 2. The complete raw reset budget is one final fringe prime

`RE-076` gives the exact relation

\[
H_\vartheta(Z)=\widehat H(C,b)-\delta_\vartheta(Z),
\tag{26}
\]

where the correction is either zero or

\[
\delta_\vartheta(Z)=\log r
\tag{27}
\]

for the unique ordinary prime `r` already crossed by the selector but not yet by its delayed first-layer CA event. Apply (26) at the two ends of the fan. Since the left correction is nonnegative, (6) yields

\[
H_{\vartheta,R}-H_{\vartheta,L}
\ge
c_JX_{\mathcal B}^{1-b_1}\log X_{\mathcal B}
-\delta_{\vartheta,R}.
\tag{28}
\]

If the final correction vanishes, the raw deficit itself inherits the full positive lower bound. If it is nonzero, the fringe geometry says

\[
r_R\le Z_R<\eta_{r_R,1}<r_R+\frac12,
\tag{29}
\]

so

\[
\delta_{\vartheta,R}=\log r_R\le\log Z_R.
\tag{30}
\]

The uniform selector asymptotic `Z_R/Y_R ->1` and `Y_R=W_B=X_BR_B` give

\[
\boxed{
\delta_{\vartheta,R}
\le
\log(X_{\mathcal B}R_{\mathcal B})+O_J(1).
}
\tag{31}
\]

Equations (28)--(31) prove (8). If (9) holds, then the right side of (28) cannot remain positive. Hence the final correction must be nonzero and

\[
\log(X_BR_B)
\ge
c_JX_B^{1-b_1}\log X_B-O_J(1).
\tag{32}
\]

Because `X_B^(1-b_1) -> infinity`, the additive `log X_B` and bounded terms are negligible after reducing the constant, proving (10)--(11).

Notice what has *not* been summed: there is no accumulated negative contribution from all earlier fringe crossings. Those jumps are exactly canceled inside `widehat H`, and when one converts back to the raw endpoint difference they telescope to `delta_L-delta_R`. Thus a fan with thousands or millions of unmatched intermediate fringe episodes still has only **one final raw reset atom** available at its right endpoint.

## 3. A successful raw reset terminates on the deep base-two ladder

Equation (9) and the positivity of (6) imply `delta_(vartheta,R)>0`. `RE-063` applies to every sufficiently late selected state carrying such a nonzero endpoint correction, independently of how the fan entered that state. Therefore the immediate next physical CA state `D_R` satisfies

\[
\boxed{D_R/C_R=2.}
\tag{33}
\]

The outgoing event is the unique deep base-two layer `eta_(2,j)`, and the fringe prime is its integer part. This proves (12)--(13).

The host classification is stronger than a count statement. `RE-063` also shows that these selected fringe-host scales are multiplicatively lacunary, asymptotically by at least a factor `2`. The reset branch of (10) therefore lands not merely at an enormous endpoint but at an enormous endpoint from a one-dimensional lacunary family. This does not itself rule out such endpoints: a finite false-RH counterexample block is not known to have a sufficiently short physical span, and a lacunary sequence can still contain arbitrarily large members. It does, however, remove unmatched fringe behavior as a freely available local sign mechanism.

## 4. Stress tests and evidence boundary

The single-state fan is a useful first control. If one selected CA state carries all of `J`, then `R_B=1`; equation (19) integrates over the full threshold interval and gives the power-scale corrected rise in (6). The raw endpoint correction is only `O(log X_B)`, so it cannot cancel that rise. Thus the theorem does not secretly rely on having many switches or on `RE-104` complexity.

At the other extreme, allow an enormous final state. Then the estimate deliberately permits cancellation: a fringe atom has size `log r_R`, so if `log Y_R` reaches the scale `X_B^(1-b_1) log X_B`, the endpoint term is arithmetically large enough to erase the lower bound. No sign contradiction is claimed beyond that point. This is the matched falsification control that fixes the stretch scale in (10).

The theorem also does **not** multiply (6) by the near-square-root state count from `RE-104`. Such a multiplication would double-count threshold width. The `RE-104` complexity theorem and the present source-debt theorem constrain different projections of the same fan: the former prices how many distinct ordinary-prime-gap chambers are needed to carry threshold measure at moderate scale; the latter prices how much corrected Chebyshev transport that threshold measure forces and how expensive the sole raw endpoint reset is. Additional arithmetic coupling is still required before the two can yield a contradiction.

Finally, the lower exponent `1-b_1` remains below the false-RH zero frontier `Theta` because `b_1>1-Theta`. Thus a genuine off-critical Chebyshev fluctuation can still be large enough to absorb the forced rise. Equation (10) is a structural narrowing of the assembly/reset architecture, not an RH proof and not a hidden use of an RH-strength prime-error estimate.

## 5. Prior-art boundary and research consequence

The load-bearing mathematics is line-internal: `RE-040` supplies the uniform quantitative fan and amplitude floor, `RE-076` supplies the global corrected Chebyshev Lyapunov coordinate, and `RE-063` supplies the base-two classification of a nonzero final fringe. The classical CA event structure behind those findings is already anchored to Alaoglu--Erdos and Robin in `SOURCES.md`. Mantovanelli's August 2026 prime-layer workload remains the closest current event-sweep prior art, while Zimov and recent explicit-counterexample-window work concern consecutive CA transitions or static counterexample windows rather than Mathia's adaptive compact threshold fan. A current directed search found no external result giving the whole-fan estimate (6), the endpoint-only reset inequality (8), or the super-stretch/base-two conclusion (10)--(13). No new external theorem is used, so `SOURCES.md` is unchanged.

The strategic consequence is a correction to the post-`RE-105` frontier. **Unmatched fringe behavior is not an independent moderate-scale cancellation branch.** After endpoint correction, all intermediate fringe activity disappears from the global ledger; in raw Chebyshev coordinates, erasing the resulting power-scale debt requires the final fringe atom itself to be power-large, which forces the fan through the extreme stretch (10) and onto a deep base-two host. The remaining source problem is therefore sharper: either exploit the unavoidable positive raw Chebyshev rise on every sub-extreme-stretch fan, or rule out the exceptionally stretched base-two-terminated fan by a genuine prime-source or same-block height constraint.