# RE-026 — quantitative Robin excursions force divergent selected race or superlinear block stretch

**Status:** `LITERATURE+DERIVED + QUANTITATIVE-RH-FAILURE + SELF-TANGENT-BLOCK-MAXIMUM + MIXED-RACE-DICHOTOMY + FINITE-ANNULUS-TRANSFER + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-021`--`RE-023` show that every sufficiently large regular self-tangent CA counterexample has Robin height controlled, at square-root scale, by a CA-selected mixed Mertens--Chebyshev race. Those findings use only the fact that the selected state lies above the Robin barrier. Robin's original false-RH theorem is quantitatively stronger: along colossally abundant integers it produces excursions above the barrier of inverse-power size in `log n`. Passing that quantitative excursion to a self-tangent block maximum yields a new dichotomy.

Assume RH is false and put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12.
\tag{1}
\]

Fix

\[
1-\Theta<b<\frac12.
\tag{2}
\]

Robin's Proposition 1 in Section 4 implies that there is a constant `c_b>0` and infinitely many colossally abundant integers `N` for which, with

\[
X_N:=\log N,
\]

\[
\boxed{
G(N)\ge e^\gamma\left(1+\frac{c_b}{X_N^b}\right).
}
\tag{3}
\]

For each CA counterexample block containing one of these quantitative witnesses, choose `N_B` to be the earliest witness satisfying (3), and choose `C_B` to be the **rightmost** CA state at which `G` attains its maximum on that block. Write

\[
X_B:=\log N_B,
\qquad
Y_B:=\log C_B.
\tag{4}
\]

Then `C_B` is a regular self-tangent CA counterexample, even if the block maximum is tied on its left. Let `p_B` be its largest active first-layer prime. There is a constant `c'_b>0` such that

\[
\boxed{
\mathscr Y(p_B)
\ge
2\sqrt2
+c'_b\frac{\sqrt{Y_B}\log Y_B}{X_B^b}
-O_b\!\left(\frac1{\log Y_B}\right),
}
\tag{5}
\]

where `mathscr Y` is the selected mixed prime-race coordinate of `RE-009`--`RE-023`.

Thus the classical quantitative failure mode cannot hide inside the bare threshold `mathscr Y>=2sqrt(2)+o(1)`. On infinitely many counterexample blocks, **either the CA-selected mixed race itself grows well beyond the threshold, or the quantitative Robin witness must occur at a logarithmic size much larger than the self-tangent block maximum that carries its height**.

More precisely, for every fixed

\[
a<\frac1{2b},
\tag{6}
\]

if infinitely many of these blocks satisfy

\[
X_B\le Y_B^a,
\tag{7}
\]

then along their rightmost self-tangent maxima

\[
\boxed{
\mathscr Y(p_B)
\gg_b
Y_B^{1/2-ab}\log Y_B
\longrightarrow+\infty.
}
\tag{8}
\]

Conversely, if along an infinite family of the selected block maxima

\[
\mathscr Y(p_B)=Y_B^{o(1)},
\tag{9}
\]

then necessarily

\[
\boxed{
\frac{\log X_B}{\log Y_B}
\ge
\frac1{2b}-o(1).
}
\tag{10}
\]

Because `b<1/2`, the exponent on the right is strictly larger than one. In the stronger bounded-race regime `mathscr Y(p_B)=O(1)`, one gets the explicit stretch

\[
\boxed{
X_B
\gg_b
Y_B^{1/(2b)}(\log Y_B)^{1/b}.
}
\tag{11}
\]

The same quantitative lower bound transfers to the finite PNT annulus of `RE-022`. For every fixed `alpha<3/4` and every fixed admissible annulus parameter `A`, if

\[
\mathscr A_{\alpha,A}(p)
:=
\sqrt p\log p
\int_{p+p^\alpha}^{U_A(p)}
\left[
(\vartheta(t)-t)h'(t)-(h(t)-k(t))
\right]dt,
\tag{12}
\]

then on the selected maxima

\[
\boxed{
\mathscr A_{\alpha,A}(p_B)
\ge
2\sqrt2
+c'_b\frac{\sqrt{Y_B}\log Y_B}{X_B^b}
-O_{b,\alpha,A}\!\left(\frac1{\log Y_B}\right).
}
\tag{13}
\]

Hence in the short-stretch branch (7), the forced divergence is carried inside the same finite annulus already isolated by `RE-022`; it cannot be reassigned to the discarded local or remote tails.

## 1. Robin's false-RH theorem supplies quantitative CA witnesses

Robin's Section 4 starts from the Landau--Nicolas oscillation mechanism. If RH is false and `Theta` is as in (1), his Proposition 1 states, specifically on colossally abundant integers, the positive inverse-power excursion corresponding to every `b` in (2). We use only the one-sided consequence (3).

This is stronger than the qualitative input used in `RE-001`. In particular, (3) gives

\[
\log G(N)-\gamma
=
\log\!\left(\frac{G(N)}{e^\gamma}\right)
\ge
\log\!\left(1+c_bX_N^{-b}\right).
\tag{14}
\]

For all sufficiently large witnesses, `c_bX_N^{-b}<1`, so `log(1+u)>=u/2` yields

\[
\boxed{
\log G(N)-\gamma
\ge
\frac{c_b}{2X_N^b}.
}
\tag{15}
\]

`RE-001` also records Robin's complementary fact that CA values below the barrier occur infinitely often under hypothetical RH failure. Therefore the CA values above `e^gamma` split into infinitely many finite counterexample blocks. Since (3) occurs infinitely often, infinitely many of those finite blocks contain at least one quantitative witness.

No claim of novelty is made for (3) or (15). The new use begins when the quantitative witness is transferred to a self-tangent maximum of the same block.

## 2. The rightmost block maximum is regular self-tangent

Fix one counterexample block containing a witness `N_B`, and let `C_B` be its rightmost CA maximizer. Let

\[
A<C_B<B
\]

be the adjacent CA states and put `Y=log C_B`. Rightmost maximality gives

\[
G(C_B)\ge G(A),
\qquad
G(C_B)>G(B).
\tag{16}
\]

Let `epsilon_-` and `epsilon_+` be the supporting slopes of the transitions `A->C_B` and `C_B->B`. With `H(x)=log log x` and `g(x)=H'(x)=1/(x log x)`, the exact consecutive-CA identities of `RE-001` give from the weak left inequality

\[
\varepsilon_-
\ge
\frac{H(Y)-H(\log A)}{Y-\log A}.
\tag{17}
\]

Strict concavity of `H` makes the backward secant strictly larger than the tangent at its right endpoint, hence

\[
\varepsilon_->g(Y).
\tag{18}
\]

The strict right inequality similarly gives

\[
\varepsilon_+
<
\frac{H(\log B)-H(Y)}{\log B-Y}
<g(Y).
\tag{19}
\]

Consequently

\[
\boxed{
\varepsilon_+<g(Y)<\varepsilon_-,
}
\tag{20}
\]

so `C_B` is a regular self-tangent CA state. This is the rightmost-max analogue of the leftmost-max argument in `RE-001`; it is included because the quantitative witness need not itself be the state used by that earlier selection rule.

Since `C_B` maximizes `G` on the block and `N_B` belongs to the same block,

\[
G(C_B)\ge G(N_B).
\]

Equation (15) therefore gives

\[
\boxed{
\log G(C_B)-\gamma
\ge
\frac{c_b}{2X_B^b}.
}
\tag{21}
\]

This step is exact apart from the harmless large-witness simplification in (15). It does not assume where `N_B` lies relative to `C_B` inside the block.

## 3. Quantitative height transfers to the selected mixed race

Because `C_B` is regular self-tangent, the universal height identity of `RE-021` applies. For its largest active first-layer prime `p_B`,

\[
\sqrt{p_B}\log p_B\,
(\log G(C_B)-\gamma)
=
\mathscr Y(p_B)
-2\sqrt2
+O\!\left(\frac1{\log p_B}\right).
\tag{22}
\]

The more precise coefficient recorded in `RE-021` is not needed here. The same finding gives

\[
p_B\sim Y_B.
\tag{23}
\]

Combining (21)--(23), and absorbing fixed comparison constants into `c'_b`, proves (5).

This is the decisive quantitative splice. The `2sqrt(2)` obstruction of `RE-021` is the limiting CA tax when the Robin excess tends to zero faster than the square-root normalization sees it. Robin's false-RH witnesses have a prescribed excess `X_B^{-b}` with `b<1/2`; unless their block maxima are displaced to a sufficiently larger `Y`-scale, the normalization amplifies that excess rather than losing it.

## 4. Race growth versus block stretch

Assume first (7). Equation (5) gives

\[
\mathscr Y(p_B)
\ge
2\sqrt2
+c'_bY_B^{1/2-ab}\log Y_B
-o(1),
\]

and `1/2-ab>0` by (6). This proves (8).

For the converse, rearrange (5):

\[
X_B^b
\gg_b
\frac{\sqrt{Y_B}\log Y_B}
{1+\mathscr Y(p_B)}
\tag{24}
\]

along the selected counterexample maxima; the denominator is positive and the fixed CA-tax term is harmless. Under (9), taking logarithms gives

\[
b\log X_B
\ge
\left(\frac12-o(1)\right)\log Y_B,
\]

which is (10). If `mathscr Y(p_B)=O(1)`, (24) directly gives (11).

The meaning of (10) is deliberately in the `X=log n` event coordinate used throughout this line. Because `1/(2b)>1`, subpower selected-race growth would force the earliest quantitative witness in these blocks to lie eventually far to the right of the chosen self-tangent maximum: `X_B>Y_B`, and indeed at a superlinear power of `Y_B` up to the `o(1)` exponent.

This is not contradicted by the local transition bounds of `RE-003`, `RE-017`, or `RE-025`. Those control one or two adjacent CA jumps. A counterexample block may contain many CA transitions, and the current line has no theorem bounding the total span from its rightmost maximum to a later quantitative witness by a fixed or subpower function of `Y_B`.

## 5. The quantitative excess lives in the finite annulus

`RE-022` proves, for every fixed `alpha<3/4` and every fixed sufficiently large admissible `A`, that at every regular self-tangent state

\[
\mathscr A_{\alpha,A}(p)
=
\mathscr Y(p)+O_{\alpha,A,M}((\log p)^{-M})
\tag{25}
\]

for every fixed `M`. Apply this to `p=p_B` and choose `M>1`. Equations (5), (23), and (25) give (13).

Therefore the dichotomy is not an artefact of representing the height by an infinite tail. If the block stretch is shorter than the critical power, the forced growth occurs in the finite, source-sensitive PNT annulus. Conversely, keeping that annular race subpower demands the same superlinear block stretch (10).

This connects Robin's classical quantitative false-RH oscillation directly to the current line's live source problem: one may now try to exclude either side of the dichotomy using CA selection. A theorem showing subpower growth of the selected annular race on the relevant self-tangent maxima would have to be paired with a theorem preventing the block stretch in (10); proving only one side is insufficient.

## 6. Prior art and evidence boundary

Robin's 1984 Proposition 1 of Section 4 is the load-bearing external theorem for (3); it is classical and explicitly formulated for colossally abundant numbers. Lagarias' quantitative restatement confirms the inverse-power false-RH excess, and Zimov's 2025 work invokes the same Robin proposition when studying the least hypothetical CA exception. These sources establish the quantitative excursion itself, not the present block-max/race transfer.

Mantovanelli's 2026 prime-layer workload preprint is the closest prior art for regular self-tangent CA returns and their exact workload representation. `RE-021`--`RE-023` are the local repository authority for the selected mixed-race height dictionary used here. A targeted search of current Robin/CA, self-tangent workload, least-counterexample, and mixed-prime-race literature did not locate the specific implication (5) or the race-versus-block-stretch alternative (8)--(11). This is a bounded prior-art statement, not a claim that the constituent Robin oscillation or CA machinery is new.

Several limitations are load-bearing. First, the witness sequence and constant depend on `b`; one must not pass to `b=1-Theta` or compare different `b`-sequences as though they were one common subsequence. Second, (5) says nothing about the sign or magnitude of `mathscr Y` at arbitrary primes; global one-sided mixed-race control is already RH-equivalent by `RE-009`. Third, the argument does not prove that quantitative witnesses occur near the self-tangent maximum of their block. The entire point of (10)--(11) is to expose that possibility as the remaining geometric escape.

Accordingly this is not an RH proof. It is a stronger necessary-condition theorem under hypothetical failure: the classical inverse-power Robin excursion must manifest either as a genuinely growing **CA-selected finite-annulus mixed race** or as a quantitatively enormous separation, in logarithmic size, between the self-tangent block maximum and the first strong CA witness. The next useful step is a theorem coupling total counterexample-block span to the local CA event geometry of `RE-025`, or a source-conditioned upper bound for the selected annular race on those same block maxima.