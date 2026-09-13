# FD-103 — power-dense record ladders saturate the logarithmic source budget at polynomial projective cost

**Status:** `EXACT-DERIVED + FALSE-RH-SOURCE-RECORDS + POWER-DENSE-FOUR-ADIC-SEEDS + SUBPOWER-PROJECTIVE-QUALITY + EXACT-DYADIC-GENEALOGY + LOGARITHMIC-DEPTH-SATURATION + FD102-SHARPNESS-CONTROL + POLYNOMIAL-QUALITY-BOUND + MASS-SELECTION-FRONTIER + NO-RH-CONTRADICTION`.

`FD-102` gives an exact adaptive source-budget theorem. If a nonhead tagged state at horizon `H` samples source quotient `x`, then arbitrary carrier retagging cannot keep that source scale alive for more than

\[
\mathfrak A(H,x)
=
\log_2\frac{H-1}{8x-1}
\]

consecutive nonhead predecessors. On the false-RH frontier core, where `x>=H^(Theta-delta+o(1))`, this becomes the logarithmic upper bound

\[
m\le (1-\Theta+\delta+o(1))\log_2 H.
\]

The remaining question is whether that coefficient is merely a by-product of the universal half-scale estimate, or whether the actual physical source can realize source-neutral nonhead genealogies on the same logarithmic scale.

It can. The power-window record law from `FD-076`, combined with the exact dyadic carrier algebra of `FD-093`/`FD-100`, gives two complementary statements.

First, **every sufficiently large strict normalized source record already seeds a sharp four-adic state with only subpower occupation/defect loss**. The special slow-doubling extraction of `FD-096` is needed for fixed constants, but not for power-exponent quality. Since the strict source records are power-dense, these subpower-quality sharp entry states are power-dense as well.

Second, above any such record `X`, the exact dyadic states

\[
H_j=2^{k-j}X,
\qquad
r_j=2^{k-j}
\]

form a source-neutral nonhead predecessor ladder until row `8`, after which the next step exposes the four-adic head. If `k` grows like `kappa log_2 X`, the ladder has logarithmic depth. More precisely, its nonhead length differs from the `FD-102` adaptive budget by `o(1)`:

\[
\boxed{
 m=k-3
 =\mathfrak A(2^kX,X)+o(1).
}
\]

Writing `X=H_0^(beta+o(1))`, this gives

\[
\boxed{
 m=(1-\beta+o(1))\log_2 H_0.
}
\]

For `1/2<Theta<1`, choosing `beta=Theta` realizes the precise frontier coefficient

\[
\boxed{
 m=(1-\Theta+o(1))\log_2 H_0
}
\]

while the sampled source remains identically `X=H_0^(Theta+o(1))` at every nonhead state.

Thus the logarithmic coefficient in `FD-102` is **geometrically sharp** for the actual quotient-shell source: it cannot be improved using only horizon contraction, floor geometry, nonsquarefree row eligibility, or the power-law recurrence of source records. Any shortening of the source-neutral segment has to exploit the fact that the predecessor theorem follows **mass-selected sharp energy packets**, not merely a legitimate tagged carrier.

The ladder also gives an explicit quality scale. Uniformly for dyadic rows `4<=r<=X^kappa`,

\[
\boxed{
\mathcal Q_\sigma(rX)
\ge
r^{-2\Theta}X^{-o(1)}
}
\]

for the intrinsic projective quality of `FD-097`. At the frontier-scaled top `X=H_0^(Theta+o(1))`, this becomes

\[
\boxed{
\mathcal Q_\sigma(H_0)
\ge
H_0^{-2\Theta(1-\Theta)-o(1)}.
}
\]

This is only a polynomial guarantee, not a fixed occupation theorem for the top of the ladder. That distinction is decisive: the construction is a matched sharpness control for the deterministic source budget, not a counterexample to a future theorem showing that **sharp fixed-occupation packets** must encounter a head/source drop earlier.

## 1. Power-window source records control every fixed-power dilation at subpower precision

Assume a false-RH zero frontier

\[
\Theta:=\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}>\frac12
\]

and fix

\[
\frac12<\sigma<\Theta.
\]

To avoid confusion with the historical Schur-energy maximum of `FD-097`, write the normalized **source** running maximum as

\[
P^{\rm src}_\sigma(Y)
:=
\max_{1\le n\le Y}
\frac{|\mathcal H(n)|}{n^\sigma}.
\]

`FD-076`, using the fixed-power-window Mertens maximal-order theorem of Pintz and the exact inverse floor-harmonic transform of `FD-046`, proves

\[
\boxed{
P^{\rm src}_\sigma(Y)
=Y^{\Theta-\sigma+o(1)}.
}
\tag{1}
\]

It also proves that strict `sigma`-record indices are power-dense and that at every such record `X`,

\[
A_X:=|\mathcal H(X)|
=X^{\Theta+o(1)},
\qquad
\frac{A_X}{X^\sigma}
=P^{\rm src}_\sigma(X).
\tag{2}
\]

Equation (1) has a useful uniform consequence which was not needed in `FD-076`. Fix any `kappa>0`. Uniformly for real `r` satisfying

\[
1\le r\le X^\kappa,
\]

one has along strict records

\[
\boxed{
\frac{P^{\rm src}_\sigma(rX)}{P^{\rm src}_\sigma(X)}
\le
r^{\Theta-\sigma}X^{o(1)}.
}
\tag{3}
\]

Indeed, put `d=Theta-sigma>0`. For every fixed `epsilon>0`, (1) gives for all sufficiently large arguments

\[
Y^{d-\epsilon}
\le P^{\rm src}_\sigma(Y)
\le Y^{d+\epsilon}.
\]

Hence

\[
\frac{P^{\rm src}_\sigma(rX)}{P^{\rm src}_\sigma(X)}
\le
r^{d+\epsilon}X^{2\epsilon}
\le
r^d X^{(\kappa+2)\epsilon}.
\]

Since `epsilon` is arbitrary after `kappa` is fixed, (3) follows. The point is that `FD-076` controls not only each fixed multiplicative dilation but every dilation bounded by a fixed power of the record scale, at the cost of a single `X^(o(1))` factor.

## 2. Every dyadic record carrier has explicit projective quality

Retain the complete and nonsquarefree Schur energies

\[
E_{N,1}
=
\sum_{1<s\le N}
\frac{J_2(s)}{s^2}
\mathcal H\!\left(\left\lfloor\frac Ns\right\rfloor\right)^2,
\]

\[
U_{N,1}
=
\sum_{\substack{1<s\le N\\\mu(s)=0}}
\frac{J_2(s)}{s^2}
\mathcal H\!\left(\left\lfloor\frac Ns\right\rfloor\right)^2.
\]

For the energy history use the notation

\[
\mathscr P_\sigma(H)
:=
\max_{2\le N\le H}
\frac{E_{N,1}}{N^{2\sigma}},
\]

so the intrinsic projective quality of `FD-097` is

\[
\mathcal Q_\sigma(H)
=
\frac{U_{H,1}}{H^{2\sigma}\mathscr P_\sigma(H)}.
\tag{4}
\]

Because `sigma>1/2`, the convergent Jordan sum

\[
S_\sigma
:=
\sum_{s=2}^{\infty}
\frac{J_2(s)}{s^{2+2\sigma}}
<\infty
\tag{5}
\]

controls the entire history below a record dilation. If `N<=rX`, every source argument in `E_(N,1)` is at most `rX`, and therefore

\[
\begin{aligned}
E_{N,1}
&\le
\bigl(P^{\rm src}_\sigma(rX)\bigr)^2
N^{2\sigma}
\sum_{s=2}^{\infty}
\frac{J_2(s)}{s^{2+2\sigma}}.
\end{aligned}
\]

Thus

\[
\boxed{
\mathscr P_\sigma(rX)
\le
S_\sigma\bigl(P^{\rm src}_\sigma(rX)\bigr)^2.
}
\tag{6}
\]

Now take a dyadic carrier

\[
r=2^a\ge4,
\qquad
H=rX.
\]

The row `r` is nonsquarefree, samples the strict record exactly, and has the constant Jordan weight

\[
\frac{J_2(r)}{r^2}=1-\frac1{2^2}=\frac34.
\]

Consequently

\[
\boxed{
U_{rX,1}\ge\frac34 A_X^2.
}
\tag{7}
\]

Combining (4), (6), (7), and the record identity in (2),

\[
\begin{aligned}
\mathcal Q_\sigma(rX)
&\ge
\frac{3}{4S_\sigma}
\frac{A_X^2}
{(rX)^{2\sigma}(P^{\rm src}_\sigma(rX))^2}\\
&=
\frac{3}{4S_\sigma}
 r^{-2\sigma}
\left(
\frac{P^{\rm src}_\sigma(X)}
{P^{\rm src}_\sigma(rX)}
\right)^2.
\end{aligned}
\tag{8}
\]

Using (3), uniformly for dyadic `4<=r<=X^kappa`,

\[
\boxed{
\mathcal Q_\sigma(rX)
\ge
c_\sigma r^{-2\Theta}X^{-o(1)}.
}
\tag{9}
\]

The same calculation gives separate coarse occupation and defect estimates. Since `E_(rX,1)/(rX)^(2sigma)<=mathscr P_sigma(rX)`, equations (3), (6), and (7) imply

\[
\boxed{
\frac{U_{rX,1}}{E_{rX,1}}
\ge
c_\sigma r^{-2\Theta}X^{-o(1)}.
}
\tag{10}
\]

On the other hand, (7) gives

\[
\frac{E_{rX,1}}{(rX)^{2\sigma}}
\ge
\frac34 r^{-2\sigma}
\bigl(P^{\rm src}_\sigma(X)\bigr)^2,
\]

and hence the normalized-energy record defect satisfies

\[
\boxed{
\mathfrak R_\sigma(rX)
\le
C_\sigma r^{2\Theta}X^{o(1)}.
}
\tag{11}
\]

The projective estimate (9) is stronger than merely dividing the separate coarse bounds (10) and (11); it keeps their common source-envelope normalization correlated, exactly in the spirit of `FD-097`.

## 3. Every strict source record gives a power-dense sharp four-adic seed

Set `r=4` in the previous section. Equations (7) and (2) give

\[
E_{4X,1}
\ge
U_{4X,1}
\ge
\frac34 X^{2\Theta+o(1)}.
\]

Conversely (6) and (1) give

\[
E_{4X,1}
\le
(4X)^{2\sigma}
S_\sigma
(P^{\rm src}_\sigma(4X))^2
=(4X)^{2\Theta+o(1)}.
\]

Therefore

\[
\boxed{
E_{4X,1}=(4X)^{2\Theta+o(1)}.
}
\tag{12}
\]

Moreover (9)--(11) reduce to

\[
\boxed{
\frac{U_{4X,1}}{E_{4X,1}}
\ge X^{-o(1)},
\qquad
\mathfrak R_\sigma(4X)
\le X^{o(1)},
\qquad
\mathcal Q_\sigma(4X)
\ge X^{-o(1)}.
}
\tag{13}
\]

This is weaker in constants than the special `FD-096` slow-doubling subsequence, where occupation and defect are bounded by fixed constants, but much stronger in recurrence. `FD-076` says that for every fixed `lambda in (0,1)`, every sufficiently large source window

\[
[Y^{1-\lambda},Y]
\]

contains a strict record. Multiplication by `4` preserves that power-window recurrence. Hence **sharp four-adic states with subpower occupation, subpower defect, and subpower projective loss occur in every fixed power window**.

For any argument that only needs power-exponent quality, the entry-state recurrence is therefore no longer restricted to the sparse fixed-quality subsequence of `FD-096`. What is still missing is a predecessor theorem uniform when the occupation itself is allowed to be `H^(-o(1))`; `FD-097` explicitly does not supply that uniformity.

## 4. Pure dyadic ladders exactly saturate the `FD-102` nonhead budget

Fix `kappa>0` and let `X` run through sufficiently large strict `sigma`-records. Put

\[
k=k(X):=\lfloor\kappa\log_2 X\rfloor
\]

and assume `k>=4`. Define

\[
r_j:=2^{k-j},
\qquad
H_j:=r_jX,
\qquad
0\le j\le k-3.
\tag{14}
\]

Every row `r_j` in (14) is at least `8` and is therefore a nonhead nonsquarefree dyadic carrier. Its source quotient is exactly

\[
\boxed{
\left\lfloor\frac{H_j}{r_j}\right\rfloor=X
}
\tag{15}
\]

at every level.

For `0<=j<k-3`, the eligible dyadic predecessor of `FD-093` is exact:

\[
(H_j,r_j)
\longmapsto
\left(
\frac{H_j}{2},
\frac{r_j}{2}
\right)
=(H_{j+1},r_{j+1}).
\tag{16}
\]

Thus there are exactly

\[
\boxed{m=k-3}
\tag{17}
\]

consecutive nonhead predecessor steps from row `2^k` down to row `8`, all preserving the same source quotient `X`. The next dyadic predecessor maps `(8X,8)` to `(4X,4)` and exposes the four-adic source-head state, exactly as required by `FD-100` and `FD-102`.

Now evaluate the adaptive potential of `FD-102` at the top:

\[
\begin{aligned}
\mathfrak A(H_0,X)
&=
\log_2\frac{2^kX-1}{8X-1}\\
&=
(k-3)
+
\log_2\left(
\frac{1-(2^kX)^{-1}}
{1-(8X)^{-1}}
\right).
\end{aligned}
\tag{18}
\]

For `k>=4` the last term is positive and `O(1/X)`. Consequently

\[
\boxed{
\mathfrak A(H_0,X)
=m+O(X^{-1}),
\qquad
m=k-3.
}
\tag{19}
\]

So the universal source-neutral upper bound of `FD-102` is not merely of the right order: the physical dyadic genealogy saturates it to a vanishing additive error.

The scaling interpretation is equally explicit. From the definition of `k`,

\[
H_0=2^kX=X^{1+\kappa+o(1)}.
\]

Write

\[
\beta:=\frac1{1+\kappa}.
\]

Then

\[
X=H_0^{\beta+o(1)}
\]

and (17) becomes

\[
\boxed{
 m
=(1-\beta+o(1))\log_2 H_0.
}
\tag{20}
\]

For `1/2<Theta<1`, choose

\[
\kappa=\frac{1-\Theta}{\Theta},
\qquad
\beta=\Theta.
\tag{21}
\]

Then the actual source record lies exactly at the frontier-scale lower source exponent,

\[
X=H_0^{\Theta+o(1)},
\]

while the source-neutral nonhead depth is

\[
\boxed{
 m=(1-\Theta+o(1))\log_2H_0.
}
\tag{22}
\]

This matches the `delta downarrow 0` coefficient in `FD-102`. If `Theta=1`, that coefficient itself vanishes and there is no positive logarithmic frontier budget to saturate; the general `beta<1` construction (20) remains valid.

## 5. The matched ladder pays only a controlled polynomial projective cost

The quality bound (9) applies uniformly at every state (14), because all rows satisfy `r_j<=r_0<=X^kappa`. At the top,

\[
\mathcal Q_\sigma(H_0)
\ge
X^{-2\kappa\Theta-o(1)}.
\tag{23}
\]

Since `X=H_0^(beta+o(1))` and `kappa=(1-beta)/beta`, this is

\[
\boxed{
\mathcal Q_\sigma(H_0)
\ge
H_0^{-2\Theta(1-\beta)-o(1)}.
}
\tag{24}
\]

The same exponent gives a lower occupation bound and an upper defect bound of reciprocal polynomial scale:

\[
\boxed{
\frac{U_{H_0,1}}{E_{H_0,1}}
\ge
H_0^{-2\Theta(1-\beta)-o(1)},
\qquad
\mathfrak R_\sigma(H_0)
\le
H_0^{2\Theta(1-\beta)+o(1)}.
}
\tag{25}
\]

At the frontier-matched choice `beta=Theta`,

\[
\boxed{
\mathcal Q_\sigma(H_0)
\ge
H_0^{-2\Theta(1-\Theta)-o(1)}.
}
\tag{26}
\]

As the ladder descends, `r_j` decreases, so the lower bound (9) only improves. By the time row `8` is reached, all three quality losses in (9)--(11) are subpower in `X`; the next step reaches the sharp power-dense four-adic state (12)--(13).

This polynomial scale is not claimed to be optimal. The bound comes only from the global source-record law and the one designated dyadic row. Its role is to show that the exact logarithmic source-neutral geometry is compatible with the actual source without requiring exponentially or superpolynomially bad certificates.

## 6. What is sharp now, and what still has to use mass selection

The main consequence is a separation of two questions that were still mixed after `FD-102`.

The **deterministic source budget is finished** at the exponent level. No argument using only

- the universal nonhead contraction `H'<=ceil(H/2)`,
- the quotient relation `x=floor(H/r)`,
- nonsquarefree row eligibility,
- exact dyadic reembedding, and
- the power-law recurrence of the true source

can replace the coefficient `1-Theta` in (7) of `FD-102` by a smaller universal coefficient. The dyadic record ladder (14)--(22) attains that coefficient with the genuine source and exact predecessor maps.

The remaining route must exploit information absent from this matched control. Most naturally, it must show that a **sharp mass-selected packet with fixed or subpower occupation cannot keep choosing the harmless dyadic genealogy for the full budget**, or else prove a quantitative predecessor theorem that survives polynomially weakening projective quality and then extracts useful progress from the head exposed at the bottom.

There is an important nonclaim. For polynomially large `r_0`, the top horizon `H_0=r_0X` is **not proved sharp** by the designated source row. Equation (7) only contributes `X^(2Theta+o(1))`, whereas the global frontier capacity at `H_0` is `H_0^(2Theta+o(1))`. The ladder is therefore a physical tagged-carrier control, not a proof that the adaptive energy argument can select the same chain from a sharp fixed-occupation parent. This is exactly why it sharpens the frontier rather than blocking it.

Conversely, the endpoint `4X` *is* sharp by (12), and those endpoints are power-dense. This supplies a potentially useful reservoir for any future argument able to start from subpower rather than fixed projective quality.

A concise next target is therefore:

\[
\boxed{
\text{use sharp mass selection to beat the dyadic record ladder,}
\quad\text{or make the predecessor theorem quantitative down to}
\quad
\mathcal Q_\sigma(H)=H^{-c+o(1)}.
}
\tag{27}
\]

The first route would genuinely shorten the `FD-102` logarithmic source-neutral window. The second would accept that the window is sharp and ask whether its polynomial quality loss can still be converted into enough source-head progress.

## 7. Adversarial checks and prior-art boundary

The most important stress test is the distinction between a tagged carrier and a sharp selected packet. The construction does not claim that `H_0=2^kX` is a false-RH energy record, that row `2^k` carries a fixed share of its total energy, or that the packet-selection proof of `FD-091`/`FD-093` is forced to follow this row. Equations (24)--(26) explicitly show the polynomial weakening at the top. Any future theorem that uses sharpness to exclude such weakly occupied ancestors is fully compatible with this finding.

The second check is the endpoint. The ladder does not violate `FD-102`: its `k-3` source-neutral nonhead steps end exactly at row `8`, and the next dyadic step exposes row `4`, which is the excluded source-head channel. Equation (19) shows that the shifted potential `H-1` and denominator `8x-1` capture the finite-integer boundary correctly.

Third, the uniform estimate (3) does not assume a hidden slow-doubling subsequence. It is a direct consequence of the full asymptotic power law `P^(src)_sigma(Y)=Y^(Theta-sigma+o(1))` from `FD-076`; the fixed-power restriction `r<=X^kappa` is exactly what makes the `o(1)` uniform. Fixed constants such as those in `FD-096` do not follow from this argument, and none are claimed.

Finally, the external load-bearing input remains the same one already recorded for `FD-076`: Pintz's 2026 fixed-power-window maximal-order theorem for the Mertens function. A fresh prior-art check against that paper, García's 2025 recursive/local Farey discrepancy formulas, and García's 2026 average local-discrepancy work found no published counterpart of the internal statement proved here: the exact dyadic Schur-carrier genealogy, its saturation of the adaptive potential `mathfrak A`, or the projective quality law (9). Those objects arise from the Mathia quotient-shell/Jordan-energy representation, so no priority claim is made beyond that representation-specific derivation. No new literature dependency is introduced, and `SOURCES.md` therefore needs no change.
