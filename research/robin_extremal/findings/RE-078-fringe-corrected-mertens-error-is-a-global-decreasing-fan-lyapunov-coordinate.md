# RE-078 — fringe-corrected Mertens error is a global decreasing fan Lyapunov coordinate

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + GLOBAL-FAN-LYAPUNOV + FRINGE-CORRECTED-MERTENS + ARBITRARY-MIXED-PACKETS + RESET-EXCLUSION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-075` identifies first-layer support births as the only currency capable of producing positive raw logarithmic-Mertens recovery across an arbitrary mixed fan segment, while `RE-076`--`RE-077` show that spending that currency necessarily increases the corrected Chebyshev coordinate

\[
\widehat H(C,b)=Z_b(C)-\log\operatorname{rad}(C).
\]

The remaining frontier treated a later Mertens reset as possible but expensive. There is a stronger statement. Once the single unmatched ordinary-prime fringe atom is removed, the logarithmic Mertens error itself is a **strict global Lyapunov coordinate in the opposite direction**.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on the sufficiently late common positive rightmost CA fans of `RE-040`. For a selected regular state `C`, write

\[
Y:=\log C,
\qquad Z:=Z_b(C),
\qquad h:=\log G(C)-\gamma,
\tag{2}
\]

and let

\[
E_\ell(Z)
:=\sum_{p\le Z}-\log(1-p^{-1})-\gamma-\log\log Z.
\tag{3}
\]

Let `delta_ell(Z)` be the first-layer endpoint correction of `RE-059`: it is zero unless one ordinary prime `r<=Z` has been crossed before its delayed first-layer CA event, in which case

\[
\delta_\ell(Z)=-\log(1-r^{-1}).
\tag{4}
\]

Define the corrected reciprocal-source coordinate

\[
\boxed{
\widehat E_\ell(C,b):=E_\ell(Z_b(C))-\delta_\ell(Z_b(C)).
}
\tag{5}
\]

Then, on every sufficiently late common positive fan, `widehat E_ell` is **strictly decreasing as the rightmost fan is traversed in increasing `b`**. It decreases inside every exposed state cell and also across every exposed switch, with no bound on packet cardinality and no restriction on the mixture of first- and higher-layer events.

More precisely, if `C_-<C_+` are consecutive exposed states tied at one breakpoint `b in J`, put

\[
Y_\pm:=\log C_\pm,
\qquad
Z_\pm:=Z_b(C_\pm),
\tag{6}
\]

and let

\[
c:=A_b(C_-)=A_b(C_+)>0,
\qquad
a_c(t):=\frac{ct^{-b}}{1+ct^{-b}}.
\tag{7}
\]

Then uniformly on late fans

\[
\boxed{
\widehat E_{\ell,+}-\widehat E_{\ell,-}
\le
-\bigl(b(1-b)+o_J(1)\bigr)
\int_{Y_-}^{Y_+}\frac{a_c(t)}t\,dt
<0.
}
\tag{8}
\]

The positive part of the finite-exponent tail created by all new first-layer supports is lower order than the negative smooth term in (8), even if the physical packet is arbitrarily large. Higher-layer exponent increments only make the tail smaller.

This immediately upgrades the reset statement. For any two ordered selected fan points `(C_0,b_0')` and `(C_1,b_1')` with the second later on the oriented fan,

\[
\boxed{
\bigl(E_\ell(Z_1)-E_\ell(Z_0)\bigr)_+
\le \delta_\ell(Z_1)
\ll_J \frac1{Z_0}.
}
\tag{9}
\]

If the later endpoint has no fringe prime, the raw logarithmic Mertens error cannot increase at all. The only possible positive endpoint recovery is the single current fringe atom, of size `O(1/Z_0)`; all previous support births and higher-layer motion are already absorbed into the strictly decreasing corrected coordinate.

Consequently the fixed-fraction recovery branch of `RE-075`--`RE-077` is asymptotically empty in the regime for which those findings were designed. If a matched `0 -> 0` first-layer run terminates at scale `W`, has threshold width `w`, and creates the descent

\[
B:=E_\ell(Z_L)-E_\ell(Z_R)
\gg_J W^{-b_1}w,
\tag{10}
\]

then at every later selected endpoint

\[
\boxed{
\frac{igl(E_\ell(Z_*)-E_\ell(Z_R)\bigr)_+}{B}
\ll_J
\frac{W^{b_1-1}}{w}.
}
\tag{11}
\]

Hence whenever

\[
W^{1-b_1}w\longrightarrow\infty,
\tag{12}
\]

no fixed positive fraction of the matched-run descent can ever be recovered later on that fan. `RE-075` and `RE-077` remain valid conditional implications, but their substantial-reset antecedent cannot occur asymptotically under (12).

## 1. The corrected Mertens coordinate is exact inside a fixed state cell

Retain the finite-exponent tail

\[
T(C):=-\sum_{p\mid C}\log\bigl(1-p^{-(a_p+1)}\bigr)>0.
\tag{13}
\]

The exact reciprocal-source invariant of `RE-059` is

\[
h
=E_\ell(Z)-\delta_\ell(Z)-T(C)
+\log\frac{\log Z}{\log Y}.
\tag{14}
\]

Therefore

\[
\boxed{
\widehat E_\ell(C,b)
=h(C)+T(C)-\log\frac{\log Z_b(C)}{\log Y}.
}
\tag{15}
\]

Inside an exposed threshold cell the state `C`, and hence `Y`, `h(C)`, and `T(C)`, are fixed. `RE-052` gives `Z_C'(b)>0`. Away from the possible single raw ordinary-prime crossing,

\[
\frac{d}{db}\widehat E_\ell(C,b)
=-\frac{Z_C'(b)}{Z_C(b)\log Z_C(b)}<0.
\tag{16}
\]

At a fringe crossing, `E_ell` jumps upward by exactly `-log(1-r^{-1})` and `delta_ell` jumps by the same amount, so `widehat E_ell` has no jump. Thus (16) extends across the whole cell: the corrected coordinate is continuous and strictly decreasing throughout every positive-width exposed cell.

This is the reciprocal-source analogue of the fixed-cell compression in `RE-059`, but with the normalization retained rather than discarded. The adjusted prime sum is frozen; increasing `b` moves the tangent selector to the right, so the only surviving change in (15) is the strictly negative `-log log Z` normalization.

## 2. Across a switch, the common-amplitude geometry already supplies a negative main term

Fix one exposed breakpoint and use (6)--(7). The tied endpoints lie on the same common-amplitude curve

\[
h_c(t):=\log(1+ct^{-b}),
\tag{17}
\]

and the same smooth tangent-selector curve `Z_c(t)` defined by

\[
g(Z_c(t))
=g(t)-\frac{b\,a_c(t)}t,
\qquad
g(x):=\frac1{x\log x}.
\tag{18}
\]

Thus

\[
h(C_\pm)=h_c(Y_\pm),
\qquad
Z_\pm=Z_c(Y_\pm).
\tag{19}
\]

Introduce the smooth part already isolated in `RE-071`,

\[
F_c(t):=h_c(t)+\log\log t-\log\log Z_c(t).
\tag{20}
\]

Equation (15) gives the exact endpoint decomposition

\[
\boxed{
\widehat E_{\ell,+}-\widehat E_{\ell,-}
=F_c(Y_+)-F_c(Y_-)+T(C_+)-T(C_-).
}
\tag{21}
\]

The derivative computation in `RE-071` depends only on the common-amplitude tangent geometry, not on the packet being first-layer-only. Uniformly over late tied segments,

\[
F_c'(t)
=-\frac{b(1-b)a_c(t)}t
\left(
1+O_J\left(\frac1{\log t}+a_c(t)\log t\right)
\right).
\tag{22}
\]

The common small-height regime makes the error `o_J(1)` uniformly, so with

\[
I:=\int_{Y_-}^{Y_+}\frac{a_c(t)}t\,dt>0,
\tag{23}
\]

we have

\[
\boxed{
F_c(Y_+)-F_c(Y_-)
=-b(1-b)I\,(1+o_J(1)).
}
\tag{24}
\]

The only possible obstruction to global decrease is therefore a positive increase of the finite-exponent tail `T`. That increase can come only from genuinely new first-layer supports.

## 3. First-layer births cannot offset the smooth decrease, even in an unbounded packet

Consider one prime `p`. If its exponent in the CA state increases from `a>=1` to `a+1`, its contribution to (13) changes from

\[
-\log(1-p^{-(a+1)})
\]

to

\[
-\log(1-p^{-(a+2)}),
\]

which is strictly smaller. Thus every higher-layer event decreases `T`. A first-layer birth is the only positive case: when `p` enters the support, it creates

\[
\tau_p:=-\log(1-p^{-2})>0.
\tag{25}
\]

If `mathcal E_1` is the set of new first-layer supports in the complete physical packet, then exactly

\[
\boxed{
T(C_+)-T(C_-)
\le
\sum_{p\in\mathcal E_1}\tau_p.
}
\tag{26}
\]

For `p>=2`,

\[
\tau_p\le\frac{2}{p^2}.
\tag{27}
\]

Put `X:=Y_-`. By `RE-040`, `Z_-/X ->1` uniformly on the compact fan. The arbitrary-packet prime-set identity of `RE-075` says that every support birth is either an ordinary selector prime crossed after `Z_-` or the single possible initial fringe prime. Hence, for all sufficiently late switches,

\[
p\ge X/2
\qquad(p\in\mathcal E_1).
\tag{28}
\]

Also the physical logarithmic mass of the complete packet contains the first-layer mass, so

\[
\sum_{p\in\mathcal E_1}\log p
\le Y_+-Y_-.
\tag{29}
\]

Suppose first that `Y_+<=2X`. Equations (28)--(29) give

\[
\#\mathcal E_1
\ll \frac{Y_+-Y_-}{\log X},
\tag{30}
\]

and therefore

\[
\sum_{p\in\mathcal E_1}\tau_p
\ll
\frac{Y_+-Y_-}{X^2\log X}.
\tag{31}
\]

The fan amplitude has the uniform positive floor supplied by `RE-040`, so on `[X,2X]`

\[
a_c(t)\gg_J X^{-b_1}.
\tag{32}
\]

Consequently

\[
I
\gg_J
(Y_+-Y_-)X^{-1-b_1}.
\tag{33}
\]

Comparing (31) with (33),

\[
\frac{\sum_{p\in\mathcal E_1}\tau_p}{I}
\ll_J
\frac{X^{b_1-1}}{\log X}
\longrightarrow0.
\tag{34}
\]

Now suppose `Y_+>2X`. The first dyadic subinterval alone gives

\[
I
\ge
\int_X^{2X}\frac{a_c(t)}t\,dt
\gg_J X^{-b_1},
\tag{35}
\]

while (27)--(28), even after replacing primes by all integers, gives

\[
\sum_{p\in\mathcal E_1}\tau_p
\le
2\sum_{n\ge X/2}\frac1{n^2}
\ll\frac1X.
\tag{36}
\]

Hence

\[
\frac{\sum_{p\in\mathcal E_1}\tau_p}{I}
\ll_J X^{b_1-1}
\longrightarrow0.
\tag{37}
\]

Equations (34) and (37) prove, uniformly over **all** exposed switches,

\[
\boxed{
T(C_+)-T(C_-)
\le o_J(I).
}
\tag{38}
\]

No packet-cardinality hypothesis appears. Large higher-layer packets only improve the inequality because every such exponent increment contributes negatively to `T`.

Combining (21), (24), and (38) proves (8). Compactness of `J` keeps `b(1-b)` uniformly separated from zero, so the eventual sign is strict.

## 4. Concatenation leaves only one raw fringe atom as reset capacity

An oriented rightmost fan is a concatenation of fixed-state cell pieces and exposed switches. Section 1 gives strict decrease on every nontrivial cell piece, while Sections 2--3 give strict decrease across every switch. Therefore

\[
\boxed{
\widehat E_\ell\text{ is strictly decreasing along the entire sufficiently late rightmost fan.}
}
\tag{39}
\]

Take two ordered selected points, labelled `0` and `1`. Since `delta_ell>=0`,

\[
\begin{aligned}
E_\ell(Z_1)-E_\ell(Z_0)
&=
\widehat E_{\ell,1}-\widehat E_{\ell,0}
+\delta_\ell(Z_1)-\delta_\ell(Z_0)\\
&<
\delta_\ell(Z_1)-\delta_\ell(Z_0)\\
&\le\delta_\ell(Z_1).
\end{aligned}
\tag{40}
\]

If the final fringe bit is zero, the right-hand side vanishes and the raw Mertens error has strictly decreased. If the final fringe bit is one, its host prime `r_1` satisfies

\[
r_1\le Z_1<\eta_{r_1,1}<r_1+\frac12.
\tag{41}
\]

Selector order and `Z_0\asymp Y_0` imply `r_1\gg_J Z_0`, so

\[
\delta_\ell(Z_1)
=-\log(1-r_1^{-1})
\le\frac1{r_1-1}
\ll_J\frac1{Z_0}.
\tag{42}
\]

This proves (9). The many-support upper bound of `RE-075` was therefore deliberately permissive: support births can create positive increments in the finite-exponent tail, but after the tied selector geometry is imposed their total `p^{-2}` contribution is too small to overcome the negative normalization drift. Net raw recovery at selected endpoints can only be a currently unmatched fringe atom.

There can still be transient raw jumps inside the fan when a fringe prime enters. Equation (39) does not say that uncorrected `E_ell` is pointwise monotone at every real selector value. It says that the **entire recoverable endpoint discrepancy is one binary atom**, and that removing precisely that atom yields a strict Lyapunov law.

## 5. Matched-run Mertens descent is asymptotically irreversible

Let `(C_L,Z_L)` to `(C_R,Z_R)` be a matched `0 -> 0` first-layer run as in `RE-072`, terminating at physical scale `W`, with total threshold width

\[
w>0.
\tag{43}
\]

Its raw Mertens descent satisfies

\[
B:=E_\ell(Z_L)-E_\ell(Z_R)
\gg_J W^{-b_1}w.
\tag{44}
\]

The terminal fringe bit is zero. Apply (9) from `(C_R,Z_R)` to any later selected endpoint `(C_*,Z_*)`. Since `Z_R\asymp W`,

\[
\bigl(E_\ell(Z_*)-E_\ell(Z_R)\bigr)_+
\ll_J\frac1W.
\tag{45}
\]

Dividing by (44) gives (11). Under (12), the ratio tends to zero. Hence for every fixed `lambda>0`, eventually there is **no** later selected endpoint satisfying

\[
E_\ell(Z_*)-E_\ell(Z_R)\ge\lambda B.
\tag{46}
\]

This strengthens the live frontier after `RE-077`. The chain

`Mertens recovery -> support births -> physical transport -> corrected-Chebyshev surcharge`

remains mathematically valid, but on the asymptotic scale where a matched-run descent dominates one fringe atom, its first step cannot occur. The reciprocal-source loss is essentially irreversible along one oriented fan.

There is also a useful pointwise consistency check. From (15), `RE-040`, and the square-root finite-exponent tail scale of `RE-037`, uniformly over the compact fan,

\[
T(C)=o_J(h(C)),
\qquad
\log\frac{\log Z}{\log Y}=b h(C)(1+o_J(1)),
\tag{47}
\]

so

\[
\boxed{
\widehat E_\ell(C,b)
=(1-b)h(C)(1+o_J(1))>0.
}
\tag{48}
\]

This is not used to prove monotonicity—the differences between neighboring selected states can be much smaller than the pointwise errors in (48)—but it confirms that the decreasing coordinate is exactly the positive reciprocal-source component naturally carried by the adaptive Robin height.

Together with `RE-076`, the late fan therefore carries two oppositely oriented corrected source coordinates:

\[
\widehat H(C,b)=Z_b(C)-\log\operatorname{rad}(C)
\quad\text{strictly increases},
\tag{49}
\]

while

\[
\widehat E_\ell(C,b)
=E_\ell(Z_b(C))-\delta_\ell(Z_b(C))
\quad\text{strictly decreases}.
\tag{50}
\]

The remaining obstruction is no longer a reset architecture between these two ledgers. It is to show that the false-RH fan is forced to spend enough threshold width in source-bearing matched motion, or otherwise enough nonmatched/higher-layer complexity, that these finite source budgets become incompatible with the same selected states.

## 6. Falsification boundary and prior-art audit

Several boundary cases are load-bearing. Subtracting `delta_ell` is essential: a single ordinary prime crossed before its delayed first-layer event produces a raw positive jump of order `1/Y`, while the smooth decrease across a very small fan interval can be smaller. The corrected coordinate removes exactly this unavoidable binary mismatch and no more.

The tail comparison must also be done at the **switch-difference scale**. The pointwise estimate `T=o(h)` is not sufficient, because a tiny switch can have a main term much smaller than either endpoint tail. Equations (26)--(38) instead compare the actual positive change of `T` with the actual common-amplitude integral `I`; this is why the proof remains valid for arbitrarily short switches and arbitrarily large packets.

No first-layer-only assumption is used. First-layer births are the worst case because they increase `T`; every higher-layer occurrence decreases it. Tied physical events do not cause a problem because (29) counts event mass with multiplicity while `mathcal E_1` counts only the distinct positive tail births. Nor is any prime-number-theorem estimate used in the tail domination: the long-packet case is bounded by the elementary convergent sum `sum n^{-2}`.

The result does **not** prove RH. It does not show that matched first-layer runs occupy a fixed amount of threshold width, does not exclude a fan dominated by other packet architectures, and does not by itself turn the finite decrease of `widehat E_ell` into a contradiction. It removes one specific global escape: later selected motion cannot substantially restore a matched-run Mertens descent once that descent is larger than one fringe atom.

The prior-art boundary remains the one already recorded in `SOURCES.md`. Classical Alaoglu--Erdos theory supplies CA exponent thresholds; Mantovanelli's 2026 prime-layer framework is neighboring prior art for event packets and finite-exponent workload; recent work of Vega combines Chebyshev and Mertens estimates to constrain hypothetical CA counterexamples. A directed current search found no external statement giving the adaptive-fan monotonicity (39), the arbitrary-packet tail comparison (38), or the reset exclusion (45)--(46). No external theorem beyond sources already anchored in `SOURCES.md` is load-bearing, so that file requires no change.

The durable research consequence is therefore sharper than after `RE-077`: **on sufficiently late false-RH fans, corrected Chebyshev growth is globally irreversible upward and corrected logarithmic-Mertens drift is globally irreversible downward.** Future progress should attack how much of the compact threshold interval must be carried by transitions that spend these two monotone source budgets, rather than budgeting hypothetical reciprocal resets that the exact fan geometry already forbids asymptotically.