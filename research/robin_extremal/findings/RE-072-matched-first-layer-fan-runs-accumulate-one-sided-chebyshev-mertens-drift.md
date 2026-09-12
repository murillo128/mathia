# RE-072 — matched first-layer fan runs accumulate one-sided Chebyshev-Mertens drift

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + MATCHED-FIRST-LAYER-RUN + CELL-AND-SWITCH-MONOTONICITY + CHEBYSHEV-MERTENS-NO-CANCELLATION + THRESHOLD-WIDTH-COST + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`.

`RE-070` and `RE-071` show that one matched `0 -> 0` first-layer switch makes

\[
H_\vartheta(x):=x-\vartheta(x)
\]

increase and the logarithmic Mertens-product error

\[
E_\ell(x):=\sum_{p\le x}-\log(1-p^{-1})-\gamma-\log\log x
\]

decrease. The remaining ambiguity was global: repeated matched switches are separated by positive-width threshold cells, so in principle the cell motion could have undone the packet drift before the next switch. It does not. **The fixed-state cells have exactly the same two signs as the matched switches.** Hence a whole consecutive matched first-layer fan run carries a one-sided Chebyshev-Mertens ledger with no internal cancellation.

Assume RH is false, put

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho>\frac12,
\]

fix

\[
J=[b_0,b_1]\Subset(1-\Theta,\tfrac12),
\tag{1}
\]

and work on a sufficiently late common positive CA counterexample block from `RE-040`. Let

\[
\beta_1<\beta_2<\cdots<\beta_m,
\qquad m\ge2,
\tag{2}
\]

be consecutive rightmost-fan breakpoints, with ordered exposed states

\[
C_0<C_1<\cdots<C_m,
\qquad Y_i:=\log C_i.
\tag{3}
\]

At `beta_i`, the states `C_(i-1)` and `C_i` are tied. Assume that for every `i=1,...,m` the **complete physical packet** from `C_(i-1)` to `C_i` is first-layer-only and has matched fringe pattern

\[
\chi_i^- =\chi_i^+=0.
\tag{4}
\]

No packet-cardinality bound is imposed. For each internal state `C_i`, `1<=i<=m-1`, let

\[
I_i=(\beta_i,\beta_{i+1})
\tag{5}
\]

be its threshold cell, omitting an empty interval if several exposed states meet at one breakpoint. Let `Z_i(b)` be its tangent selector. Denote by `Z_L` the selector of `C_0` immediately before the first switch at `beta_1`, and by `Z_R` the selector of `C_m` immediately after the last switch at `beta_m`.

Then, for all sufficiently late blocks,

\[
\boxed{
H_\vartheta(Z_R)>H_\vartheta(Z_L),
\qquad
E_\ell(Z_R)<E_\ell(Z_L).
}
\tag{6}
\]

More strongly, both inequalities hold **monotonically along the whole selected path**: `H_vartheta` increases through every open cell and every matched switch, while `E_ell` decreases through every open cell and every matched switch. Thus neither source can cancel the drift created at an earlier matched packet while the fan remains in this branch.

There is also an additive quantitative ledger. For an internal cell put

\[
h_i:=h(C_i),
\qquad
a_i:=1-e^{-h_i},
\qquad g(x):=\frac1{x\log x}.
\tag{7}
\]

Then exactly on `I_i`,

\[
\boxed{
\frac{dZ_i}{db}
=\frac{a_i}{Y_i[-g'(Z_i)]}>0,
}
\tag{8}
\]

and the matched endpoint condition forces the fringe bit to remain zero throughout that entire cell. Consequently

\[
\boxed{
\frac{d}{db}H_\vartheta(Z_i(b))
=\frac{dZ_i}{db}>0,
}
\tag{9}
\]

and

\[
\boxed{
\frac{d}{db}E_\ell(Z_i(b))
=-g(Z_i)\frac{dZ_i}{db}<0.
}
\tag{10}
\]

Uniformly over the late compact fan, `Z_i/Y_i -> 1`, so

\[
\boxed{
\frac{d}{db}H_\vartheta(Z_i(b))
=a_iY_i\log Y_i\,(1+o_J(1)),
}
\tag{11}
\]

\[
\boxed{
-\frac{d}{db}E_\ell(Z_i(b))
=a_i\,(1+o_J(1)).
}
\tag{12}
\]

At each breakpoint, `RE-070` and `RE-071` supply the positive atomic contributions

\[
\Delta_iH_\vartheta
=b_i(1-b_i)
\int_{Y_{i-1}}^{Y_i}a_{c_i}(t)\log t\,dt\,(1+o_J(1))>0,
\tag{13}
\]

and

\[
-\Delta_iE_\ell
=b_i(1-b_i)
\int_{Y_{i-1}}^{Y_i}\frac{a_{c_i}(t)}t\,dt\,(1+o_J(1))>0,
\tag{14}
\]

where `b_i=beta_i`, `c_i` is the common adaptive amplitude at the tie, and

\[
a_{c_i}(t)=\frac{c_it^{-b_i}}{1+c_it^{-b_i}}.
\tag{15}
\]

Therefore the total run increments split into sums of positive cell masses and positive switch masses:

\[
\boxed{
\begin{aligned}
H_\vartheta(Z_R)-H_\vartheta(Z_L)
&=\sum_{i=1}^{m-1}
\int_{I_i}\frac{dZ_i}{db}\,db
+\sum_{i=1}^{m}\Delta_iH_\vartheta,\\[1mm]
E_\ell(Z_L)-E_\ell(Z_R)
&=\sum_{i=1}^{m-1}
\int_{I_i}g(Z_i)\frac{dZ_i}{db}\,db
+\sum_{i=1}^{m}(-\Delta_iE_\ell).
\end{aligned}
}
\tag{16}
\]

Every displayed term on the right is positive. This is the no-cancellation law.

## 1. A matched endpoint pair freezes the entire intervening cell source

Fix an internal state `C_i`. At the left breakpoint `beta_i`, it is the upper endpoint of a matched switch, so its fringe bit is zero. At the right breakpoint `beta_(i+1)`, it is the lower endpoint of the next matched switch, so its fringe bit is again zero.

`RE-059` proves that inside a fixed support chamber the raw source pair has the form

\[
(\vartheta(Z),M(Z))
=(\text{fixed standard mass},\text{fixed reciprocal mass})
+\chi_i(Z)(\log r_i,-\log(1-r_i^{-1})),
\tag{17}
\]

with at most one fringe prime and with `chi_i(Z_i(b))` changing at most once as `b` increases. More explicitly, if the fringe prime exists then

\[
\chi_i(Z)=\mathbf 1_{\{r_i\le Z\}},
\tag{18}
\]

while `Z_i(b)` is increasing. Since the bit equals zero at **both** ends of the cell, it must be identically zero on the cell. Hence

\[
\boxed{
\vartheta(Z_i(b))=\vartheta_i,
\qquad
M(Z_i(b))=M_i
\quad(b\in I_i)
}
\tag{19}
\]

for two constants depending only on `C_i`.

The tangent equation for this fixed state is

\[
g(Z_i(b))=g(Y_i)-\frac{ba_i}{Y_i}.
\tag{20}
\]

Differentiating and using `g'<0` proves (8). Equations (19) then give the exact cell identities

\[
H_\vartheta(Z_i(b))=Z_i(b)-\vartheta_i,
\tag{21}
\]

\[
E_\ell(Z_i(b))=M_i-\gamma-\log\log Z_i(b),
\tag{22}
\]

whose derivatives are precisely (9)--(10). Thus the threshold continuum inside a fixed cell does not create new prime-source atoms, as `RE-059` emphasized, but its deterministic normalization drift is **coherent with**, rather than opposite to, the cross-cell drift of `RE-070`--`RE-071`.

## 2. Cell motion has the same local Chebyshev-Mertens kernel as packet motion

The derivative of `g` is

\[
-g'(Z)=\frac{\log Z+1}{Z^2(\log Z)^2}.
\tag{23}
\]

Substituting into (8),

\[
\frac{dZ_i}{db}
=
\frac{a_iZ_i^2(\log Z_i)^2}
{Y_i(\log Z_i+1)}.
\tag{24}
\]

Uniform regularity from `RE-040` gives `Z_i/Y_i->1` over the compact fan, which yields (11). Multiplying (24) by `g(Z_i)` gives

\[
g(Z_i)\frac{dZ_i}{db}
=
\frac{a_iZ_i\log Z_i}{Y_i(\log Z_i+1)}
=a_i(1+o_J(1)),
\tag{25}
\]

which is (12).

There is an exact ratio before taking asymptotics. With `dH_i` denoting the positive Chebyshev cell increment,

\[
\boxed{
-dE_{\ell,i}=g(Z_i)\,dH_i.
}
\tag{26}
\]

The switch law has the same structure after averaging: `RE-071` gives

\[
\frac{-\Delta_iE_\ell}{\Delta_iH_\vartheta}
=\frac{\displaystyle\int_{Y_{i-1}}^{Y_i}a_{c_i}(t)t^{-1}\,dt}
{\displaystyle\int_{Y_{i-1}}^{Y_i}a_{c_i}(t)\log t\,dt}
(1+o_J(1)),
\tag{27}
\]

and the quotient on the right is a positive weighted average of `1/(t log t)`.

Thus the two source errors do not provide two freely orientable currencies on a matched run. They form one positive path measure viewed through two nearby kernels. If all state scales occurring in the run lie between

\[
X\le Y_i\le W,
\tag{28}
\]

then uniform `Z_i/Y_i->1`, (26), and the weighted-average bound from `RE-071` imply

\[
\boxed{
\frac{1-o_J(1)}{W\log W}
\le
\frac{E_\ell(Z_L)-E_\ell(Z_R)}
{H_\vartheta(Z_R)-H_\vartheta(Z_L)}
\le
\frac{1+o_J(1)}{X\log X}.
}
\tag{29}
\]

The global run therefore stays inside the same one-dimensional Chebyshev-Mertens cone already visible for one sublinear packet; interleaving arbitrarily many threshold cells does not create a transverse cancellation mechanism.

## 3. Positive threshold width has a quantitative excursion cost

The common blocks of `RE-040` provide a constant `c_0>0` such that every blockwise maximizer satisfies

\[
A_b(C)=Y^b(e^{h(C)}-1)\ge c_0
\tag{30}
\]

for every `b in J`. Put `R_i=e^{h_i}-1`. Since the whole late fan is in the uniform small-height regime, `R_i=o(1)` and

\[
a_i=\frac{R_i}{1+R_i}\ge\frac{c_0}{2}Y_i^{-b_1}
\tag{31}
\]

for all sufficiently late blocks.

The internal cells partition the threshold interval from the first to the last breakpoint up to finitely many endpoints:

\[
\sum_{i=1}^{m-1}|I_i|=\beta_m-\beta_1.
\tag{32}
\]

Using (11), (31), and `Y_i>=X`, the continuous part of the first identity in (16) alone gives

\[
\boxed{
H_\vartheta(Z_R)-H_\vartheta(Z_L)
\gg_J
X^{1-b_1}\log X\,(\beta_m-\beta_1).
}
\tag{33}
\]

The switch terms only increase the left-hand side. In particular, a matched first-layer run that occupies a threshold width bounded below by a fixed positive constant must consume a monotone Chebyshev excursion of order at least

\[
X^{1-b_1}\log X.
\tag{34}
\]

Because `b_1<1/2`, this is super-square-root in `X`.

For the reciprocal source, if `W` is the largest state scale in the run then (12), (31), and (32) similarly give

\[
\boxed{
E_\ell(Z_L)-E_\ell(Z_R)
\gg_J
W^{-b_1}(\beta_m-\beta_1).
}
\tag{35}
\]

This second lower bound is intentionally stated in terms of `W`: if the fan stretches superpolynomially in physical scale, the reciprocal source can become much smaller while the threshold interval remains macroscopic. The Chebyshev cost (33), by contrast, depends only on the lower scale `X` because `Y^{1-b_1}` grows with `Y`.

Equation (33) gives the matched first-layer branch a new global currency. A long run can avoid the quantized higher-layer charges of `RE-060`--`RE-066`, but it cannot carry a positive amount of threshold parameter without spending a monotone standard-prime excursion. This cost is independent of packet cardinality and survives even if the fan uses very many individually tiny matched packets.

## 4. Falsification and boundary tests

The matched hypothesis at **every** switch is essential. If one endpoint fringe bit is nonzero, the corresponding cell can contain the transient raw prime jump of `RE-059`, and `RE-063`--`RE-067` assign that event a different lacunary charge mechanism. If a higher-layer event occurs in a switch packet, the exact prime-set conservation used by `RE-070`--`RE-071` fails by the higher-layer mass, and its quantized residual charge must be restored.

The result does not claim that `H_vartheta(x)` is globally increasing or that `E_ell(x)` is globally decreasing. Both ordinary error terms oscillate. The monotonicity is only along this **adaptively selected fan path**, and only while every traversed cross-cell packet remains first-layer-only and matched. Leaving that branch is precisely an interruption that the wider fan ledger can count separately.

The threshold-width lower bound does not by itself contradict the false-RH regime. Since `b_1>1-Theta`,

\[
1-b_1<\Theta,
\tag{36}
\]

so the excursion scale in (33) remains below the natural `X^Theta` prime-number-theorem scale allowed by an off-critical zero. This is an important falsification check: the result is a capacity law for the remaining counterexample architecture, not a disguised proof of RH. Likewise, the Mertens lower bound (35) need not exceed the reciprocal-prime error envelope, especially when the fan has large physical span.

A single matched switch is also not strengthened artificially by (33): when `m=1`, the threshold width `beta_m-beta_1` is zero and the theorem reduces to the local positive/negative packet drift of `RE-070`--`RE-071`. The new content starts when matched packets are chained through actual positive-width threshold cells.

## 5. Prior-art boundary and research consequence

Global correlations between normalized Chebyshev and reciprocal-prime errors are established prior art. Bhattacharya--Martin--Simpson analyze the joint behavior of the standard and reciprocal prime-counting errors, including the logarithmic Mertens product, and prove RH-equivalent persistent comparison statements. Mantovanelli's prime-layer workload gives exact CA packet bookkeeping at the classical tangent parameter. Both sources are already anchored in `SOURCES.md`.

The present claim is narrower and fan-specific: it combines the adaptive threshold-cell source freezing of `RE-059` with the matched switch geometry of `RE-070`--`RE-071` to show that **cell motion and switch motion have the same sign and therefore accumulate across an arbitrary consecutive matched run**. The literature audit found no external statement of this adaptive run law. No external theorem is load-bearing in its proof, and no priority claim is made for the elementary differentiation in (8)--(12); `SOURCES.md` therefore needs no new entry.

The live frontier is correspondingly sharper. `RE-071` left open whether repeated matched packets could lose their local signal after the fan traversed the intervening cells. `RE-072` removes that escape. A future global argument can now debit every maximal matched first-layer run by its **threshold width and monotone Chebyshev excursion**, while debiting higher-layer/fringe interruptions by the charge and event-capacity currencies of `RE-060`--`RE-067`. What remains is to show that one of these currencies must exceed the off-critical source budget on the false-RH common blocks, or to identify another architecture capable of carrying a macroscopic threshold fan without paying either cost.