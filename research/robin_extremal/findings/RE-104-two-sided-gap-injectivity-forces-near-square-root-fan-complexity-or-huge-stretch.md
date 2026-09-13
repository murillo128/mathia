# RE-104 — two-sided gap injectivity forces near-square-root fan complexity or huge stretch

**Status:** `LITERATURE+DERIVED + QUANTITATIVE-RH-FAILURE + TWO-SIDED-FIRST-LAYER-GAP-INJECTIVITY + MEAN-SQUARE-PRIME-GAP + FAN-COMPLEXITY/STRETCH-TRADEOFF + BOUNDED-DILATION-NEAR-SQUARE-ROOT-COMPLEXITY + GLOBAL-ASSEMBLY-NARROWING + PRIOR-ART-AUDITED`.

`RE-102` closes the local support-boundary depth hierarchy above

\[
\Theta_*:=\frac{265657}{307200}=0.8647688802\ldots
\tag{1}
\]

and shows that, outside vanishing threshold measure, every selected support chamber is the first-layer image of **one whole consecutive ordinary-prime gap**. Before `RE-102`, the aggregate capacity argument of `RE-052` could not use a prime-gap moment theorem efficiently because several disjoint selected inverse intervals could lie inside the same ambient ordinary-prime gap. Two-sided first-layer contact removes exactly that multiplicity loophole: distinct surviving selected chambers correspond to distinct consecutive-prime gaps.

Combining that injectivity with the exact support-capacity law of `RE-040` and Stadlmann's unconditional mean-square prime-gap theorem yields a new global assembly constraint. Assume RH is false, write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho,
\qquad \Theta>\Theta_*,
\tag{2}
\]

and fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1-\Theta_*).
\tag{3}
\]

On one sufficiently late common positive CA block, call a selected state `C` **good** if both adjacent physical support boundaries contain first-layer events. Put

\[
Y_C:=\log C,
\qquad
I_C:=\{b\in J:C\text{ is the rightmost adaptive-amplitude maximizer}\}.
\tag{4}
\]

For one dyadic shell `X<=Y_C<2X`, let

\[
\mathcal G_X:=\{C\text{ good}:X\le Y_C<2X\},
\qquad
N_X:=\#\mathcal G_X,
\qquad
m_X:=\sum_{C\in\mathcal G_X}|I_C|.
\tag{5}
\]

Then, for every `epsilon>0`,

\[
\boxed{
N_X
\gg_{J,\varepsilon}
 m_X^2\,
 X^{\,77/100-2b_1-\varepsilon}
 (\log X)^2.
}
\tag{6}
\]

Thus a shell carrying a fixed positive amount of surviving threshold measure must contain polynomially many **distinct ordinary-prime-gap chambers**. The exponent is not the `0.48-b_1` obtained in `RE-051` from the pointwise `0.52` short-interval theorem. It is

\[
\kappa_J:=\frac{77}{100}-2b_1.
\tag{7}
\]

Because `b_1<1-Theta_*`,

\[
\boxed{
\kappa_J>
\frac{77}{100}-2\frac{41543}{307200}
=
\frac{76729}{153600}
=0.4995377604\ldots .
}
\tag{8}
\]

So on any bounded-dilation late fan, the number of exposed selected states is forced to grow at **essentially a square-root power** of the minimum physical scale.

There is a useful all-block form. Let

\[
X_{\mathcal B}:=\min_C Y_C,
\qquad
R_{\mathcal B}:=
\frac{\max_CY_C}{\min_CY_C},
\qquad
N_{\mathcal B}:=\#\{\text{exposed selected states on }J\}.
\tag{9}
\]

Then for every fixed `epsilon>0`, along all sufficiently late blocks,

\[
\boxed{
N_{\mathcal B}\,
\bigl(1+\log R_{\mathcal B}\bigr)
\gg_{J,\varepsilon}
X_{\mathcal B}^{\,77/100-2b_1-\varepsilon}
(\log X_{\mathcal B})^2.
}
\tag{10}
\]

Consequently a surviving fan above (1) has a quantitative global dichotomy. If `R_B=O(1)`, then

\[
\boxed{
N_{\mathcal B}
\ge
X_{\mathcal B}^{\,76729/153600-o(1)}.
}
\tag{11}
\]

More generally, if for some `nu<kappa_J`

\[
N_{\mathcal B}\le X_{\mathcal B}^{\nu+o(1)},
\tag{12}
\]

then (10) forces

\[
\boxed{
\log R_{\mathcal B}
\ge
X_{\mathcal B}^{\,\kappa_J-\nu-o(1)},
}
\tag{13}
\]

so the physical scale ratio itself satisfies

\[
R_{\mathcal B}
\ge
\exp\!\left(
X_{\mathcal B}^{\,\kappa_J-\nu-o(1)}
\right).
\tag{14}
\]

This is the first splice after `RE-102` that constrains the **nonlocal assembly** rather than another local boundary type. It does not close the line: a fan may still pay for low complexity by stretching enormously, and `RE-080`--`RE-082` show that the resulting long-stretch transport front is not contradicted by the smooth selector law alone. What (10) removes is a broad middle escape in which the local cells are ordinary prime-gap chambers, the physical scale stays moderately coherent, and only a sparse family of exposed states carries the whole threshold interval.

## 1. Two-sided first-layer contact makes the prime-gap assignment injective

`RE-102` gives exceptional unions `E_B subset J` with

\[
|\mathcal E_{\mathcal B}|\to0
\tag{15}
\]

such that every selected cell meeting `J\setminus E_B` has two first-layer-contacting physical support boundaries. Therefore the total width of bad selected cells is `o_J(1)`, while the good cells satisfy

\[
\sum_{C\text{ good}}|I_C|
=|J|-o_J(1).
\tag{16}
\]

For each good cell there are consecutive ordinary primes `p_-(C)<p_+(C)` such that

\[
\xi_-(C)=\eta_1(p_-(C)),
\qquad
\xi_+(C)=\eta_1(p_+(C)),
\tag{17}
\]

and the whole open physical support chamber pulls back to

\[
\eta_1^{-1}\bigl((\xi_-(C),\xi_+(C))\bigr)
=(p_-(C),p_+(C)).
\tag{18}
\]

Write

\[
d_C:=p_+(C)-p_-(C),
\qquad
\Delta_C:=\xi_+(C)-\xi_-(C).
\tag{19}
\]

The first-layer expansion in `RE-084`/`RE-102` gives, uniformly in a dyadic physical shell,

\[
\boxed{
\Delta_C=d_C+O(1/\log X)
=(1+o(1))d_C.
}
\tag{20}
\]

The key new point is injectivity. If two distinct good selected states `C` and `D` were assigned the same consecutive-prime gap, (18) would give the same open physical support chamber for both states. But the CA event staircase has exactly one exponent vector on one open chamber. Hence

\[
\boxed{
C\ne D
\quad\Longrightarrow\quad
(p_-(C),p_+(C))\ne(p_-(D),p_+(D)).
}
\tag{21}
\]

Endpoint ties do not affect this statement. `RE-103` allows a depth-two atom to share one first-layer endpoint, but the first-layer label at that coordinate is unique and the open chamber remains the same full ordinary-prime gap. Thus every good selected cell consumes a **different** term of the ordinary consecutive-prime gap sequence.

This is exactly what was unavailable in `RE-052` and in the deep-boundary argument before two-sided contact. There, disjoint inverse selector intervals could occupy disjoint pieces of one larger prime gap, so summing their squared lengths could not be bounded by the ordinary full-gap second moment without extra multiplicity control.

## 2. Threshold width forces a proportional share of its unique prime gap

The exact support-capacity inequality of `RE-040` is

\[
|I_C|
\le
\frac{Y_C\bigl(g(\xi_-(C))-g(\xi_+(C))\bigr)}
{a(C)},
\qquad
 a(C):=1-e^{-h(C)}.
\tag{22}
\]

On the compact false-RH fan, the quantitative amplitude floor gives

\[
a(C)\gg_JY_C^{-b_1},
\tag{23}
\]

uniformly. Also `xi_\pm(C)=(1+o_J(1))Y_C`, and

\[
|g'(x)|\asymp\frac1{x^2\log x}.
\tag{24}
\]

Therefore, on `X<=Y_C<2X`, the mean-value theorem gives

\[
\boxed{
|I_C|
\ll_J
\frac{\Delta_C X^{b_1-1}}{\log X}
\asymp_J
\frac{d_C X^{b_1-1}}{\log X}.
}
\tag{25}
\]

Equivalently,

\[
\boxed{
d_C
\gg_J
|I_C|\,X^{1-b_1}\log X.}
\tag{26}
\]

This resembles the local capacity law of `RE-052`, but the interpretation is now stronger. The right side cannot be paid by an arbitrary subinterval carved from a gap that is reused by other selected cells. It must be paid by the **whole unique consecutive-prime gap attached to that state**.

## 3. Stadlmann's second moment turns injectivity into a shell complexity theorem

The load-bearing external theorem is the same one already anchored for `RE-091`: for every `epsilon>0`, Stadlmann proves

\[
\boxed{
\sum_{p_n\le x}(p_{n+1}-p_n)^2
\ll_\varepsilon x^{123/100+\varepsilon}.
}
\tag{27}
\]

The physical localization of the compact fan puts the prime labels of every good cell in the shell below `O_J(X)`. By (21), the `d_C` are distinct consecutive-prime gaps. Hence

\[
\boxed{
\sum_{C\in\mathcal G_X}d_C^2
\ll_{J,\varepsilon}X^{123/100+\varepsilon}.
}
\tag{28}
\]

Squaring (25), summing, and using (20), (28),

\[
\begin{aligned}
\sum_{C\in\mathcal G_X}|I_C|^2
&\ll_J
\frac{X^{2b_1-2}}{(\log X)^2}
\sum_{C\in\mathcal G_X}d_C^2\\
&\ll_{J,\varepsilon}
\frac{X^{-77/100+2b_1+\varepsilon}}
{(\log X)^2}.
\end{aligned}
\tag{29}
\]

Cauchy--Schwarz on the threshold widths now gives

\[
m_X^2
=\left(\sum_{C\in\mathcal G_X}|I_C|\right)^2
\le
N_X\sum_{C\in\mathcal G_X}|I_C|^2.
\tag{30}
\]

Combining (29)--(30) proves (6).

The exponent has a transparent general form. If one had a full prime-gap second moment

\[
\sum_{p_n\le x}d_n^2\ll x^{1+\nu+o(1)},
\tag{31}
\]

then the same argument would give

\[
\boxed{
N_X
\ge
m_X^2 X^{1-\nu-2b_1-o(1)}.
}
\tag{32}
\]

Stadlmann's current `nu=0.23` gives `1-nu=0.77`. A conjectural optimal second moment with `nu=0` would replace `kappa_J` by `1-2b_1`; even that would still be a complexity theorem, not an exclusion theorem, because the total number of ordinary prime gaps available in a shell is much larger.

## 4. Dyadic aggregation gives the complexity/stretch tradeoff

Let the good exposed states of one late block be assigned to dyadic shells

\[
[2^kX_{\mathcal B},2^{k+1}X_{\mathcal B}),
\qquad 0\le k<L_{\mathcal B},
\tag{33}
\]

where

\[
L_{\mathcal B}\le 2+\log_2R_{\mathcal B}.
\tag{34}
\]

Write `m_k` and `N_k` for the good threshold measure and number of good selected states in shell `k`. By (16), for all sufficiently late blocks,

\[
\sum_km_k\ge\frac12|J|.
\tag{35}
\]

Apply (6) in every shell. Since

\[
2^kX_{\mathcal B}\ge X_{\mathcal B}
\]

and `kappa_J>0`, after decreasing `epsilon` harmlessly if needed,

\[
N_k
\gg_{J,\varepsilon}
 m_k^2
 X_{\mathcal B}^{\kappa_J-\varepsilon}
(\log X_{\mathcal B})^2.
\tag{36}
\]

Summing over shells and applying Cauchy once more,

\[
\sum_km_k^2
\ge
\frac{(\sum_km_k)^2}{L_{\mathcal B}}
\gg_J
\frac1{1+\log R_{\mathcal B}}.
\tag{37}
\]

Since `N_B>=sum_k N_k`, equations (36)--(37) prove (10).

This second Cauchy step is important: spreading the threshold measure over many physical scales costs only one factor `1+log R_B`, not its square. Therefore low fan complexity can evade the near-square-root shell requirement only by paying an extremely large physical stretch. Equations (13)--(14) are the direct rearrangement of (10).

For bounded dilation, `1+log R_B=O(1)`, and (11) follows from (8) after letting `epsilon` be arbitrarily small. More generally, any stretch with

\[
\log R_B=X_B^{o(1)}
\tag{38}
\]

still leaves the same power exponent `kappa_J` in the complexity lower bound. A genuinely lower-power fan therefore has to enter the much more severe regime (13), where the logarithm of the physical stretch itself grows by a positive power of the starting scale.

## 5. Relation to the existing bounded- and long-stretch branches

`RE-051` already forces polynomial fan complexity from a pointwise short-interval theorem whenever `Theta>0.52`. With the currently available exponent `0.52`, its lower complexity power is

\[
0.48-b_1.
\tag{39}
\]

The present theorem has stronger hypotheses -- it uses the two-sided first-layer normal form, available only above `Theta_*` -- but on that regime it improves the bounded-dilation complexity exponent to

\[
0.77-2b_1.
\tag{40}
\]

Their difference is

\[
(0.77-2b_1)-(0.48-b_1)
=0.29-b_1>0.154\ldots
\tag{41}
\]

through the entire band (3). At the worst admissible endpoint the new exponent remains `0.499537...`, whereas the pointwise `0.52` argument gives only about `0.344769`.

This does **not** supersede `RE-051` globally. `RE-051` has no two-sided-contact hypothesis and its complexity lower bound is independent of the physical stretch. `RE-104` instead exploits the stronger local normal form to get a much larger exponent and the new tradeoff (10).

The result also interfaces directly with `RE-080`--`RE-082`. Those findings isolate the `R_B->infinity` branch and show that a long same-block fan must realize a complementary transport front which the smooth common-amplitude selector can reproduce. The present theorem says that staying away from that branch is expensive: a bounded or moderately stretched fan must assemble almost square-root-many distinct exposed ordinary-prime-gap chambers. Conversely, avoiding that combinatorial load forces the fan into an **extreme** long-stretch regime quantified by (13), much stronger than merely asking that `R_B->infinity`.

Thus the current global assembly frontier can be sharpened to a quantitative choice:

\[
\boxed{
\text{many distinct selected ordinary-prime-gap chambers}
\quad\text{or}\quad
\text{power-large }\log R_B.
}
\tag{42}
\]

Neither side is currently impossible, but they are now separated into very different arithmetic obligations.

## 6. Stress tests, evidence boundary, and prior art

Several stronger conclusions are deliberately not claimed.

First, (6) is a lower bound on the **number of selected states**, not on the density of large ordinary-prime gaps. The selected gaps may be highly atypical, and the total number of available consecutive-prime gaps in `[X,O(X)]` is of order `X/log X`, far above the near-square-root requirement. Stadlmann's theorem therefore supplies capacity, not a contradiction.

Second, the exceptional threshold union from `RE-102` is controlled only in measure. It may contain many cells and arithmetically important isolated states. The proof never deletes them from the CA staircase; it uses only that the good cells carry `|J|-o(1)` of threshold measure. Consequently (10) constrains the fan required to support the continuum threshold family, not every individual potential Robin counterexample.

Third, endpoint depth-two ties do not improve the estimate and are not assumed absent. `RE-103` shows that such ties are the Four-Exponentials boundary. The present argument is robust to that unresolved binary decoration because the two first-layer endpoint labels and their complete ordinary-prime gap remain well defined.

Fourth, no independence or randomness of prime gaps is used. The only analytic input is the deterministic complete second-moment estimate (27). A matched synthetic gap family can saturate a Cauchy--Schwarz complexity inequality without violating any principle; hence the near-square-root exponent should be read as a necessary assembly cost, not as probabilistic evidence against false RH.

The load-bearing external theorem is exactly Stadlmann's mean-square gap result already recorded in `SOURCES.md`; a current September 2026 audit still finds it cited as the best unconditional complete second-moment exponent `1.23+epsilon`, with no later primary improvement located. Mantovanelli's 2026 CA prime-layer workload remains the closest event-staircase prior art, but its published companion concerns exact event/workload bookkeeping and finite certificates, not Mathia's adaptive false-RH threshold fan or the prime-gap-injective complexity tradeoff (6)--(10). No new external dependency is introduced, so `SOURCES.md` is unchanged.

The durable delta is therefore not another local support theorem. `RE-102` supplied the local normal form; `RE-104` makes that normal form **globally expensive to assemble**. Above `Theta_*`, a surviving false-RH block cannot simultaneously have ordinary-looking local prime-gap chambers, moderate physical stretch, and low exposed-state complexity. The remaining work is to attack one of the two surviving global regimes: source constraints on the near-square-root family of selected gaps, or source constraints on the extreme long-stretch transport front.