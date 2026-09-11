# RE-051 — off-critical RH failure beyond the short-interval exponent forces polynomial fan complexity

**Status:** `LITERATURE+DERIVED + QUANTITATIVE-RH-FAILURE + SHORT-INTERVAL-PRIME-CAPACITY + POLYNOMIAL-FAN-COMPLEXITY + STRONG-OFF-CRITICAL-SUBCASE + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-038`--`RE-040` leave open a robust escape in the coherent false-RH threshold fan: one state, or only finitely many states, might maximize the adaptive amplitude throughout a fixed compact threshold interval. The exact CA support geometry turns an unconditional prime-in-short-interval theorem into a quantitative obstruction to that escape whenever the hypothetical rightmost zeta zero lies far enough to the right.

Let `theta` be any exponent in `(1/2,1)` for which every sufficiently large interval

\[
[x-x^\theta,x]
\tag{1}
\]

contains a prime. Assume RH is false and write

\[
\Theta:=\sup_{\zeta(\rho)=0}\Re\rho.
\tag{2}
\]

If

\[
\boxed{\Theta>\theta,}
\tag{3}
\]

choose once and for all

\[
J=[b_0,b_1]\Subset(1-\Theta,1-\theta).
\tag{4}
\]

On every sufficiently late common positive CA counterexample block `\mathcal B` from `RE-040`, let `\mathcal E(\mathcal B,J)` be the distinct CA states exposed by the rightmost adaptive amplitude fan on `J`. For an exposed state `C`, write

\[
Y_C:=\log C,
\qquad
I_C:=\{b\in J:C\text{ is the rightmost maximizer of }A_b\}.
\tag{5}
\]

Then uniformly over all exposed states of all sufficiently late blocks,

\[
\boxed{
|I_C|
\ll_J
\frac{Y_C^{\,b_1+\theta-1}}{\log Y_C}.
}
\tag{6}
\]

Since `b_1+theta-1<0`, every individual threshold cell tends uniformly to zero. If

\[
X_{\mathcal B}:=
\min_{C\in\mathcal E(\mathcal B,J)}Y_C
\tag{7}
\]

and

\[
N_{\mathcal B}:=
|\mathcal E(\mathcal B,J)|,
\tag{8}
\]

then the cells partition `J` up to finitely many endpoints, so (6) gives the polynomial lower bound

\[
\boxed{
N_{\mathcal B}
\gg_J
X_{\mathcal B}^{\,1-b_1-\theta}
\log X_{\mathcal B}.
}
\tag{9}
\]

In particular,

\[
\boxed{N_{\mathcal B}\longrightarrow\infty}
\tag{10}
\]

along the escaping false-RH block family. Thus, in the regime `Theta>theta`, false RH cannot be carried by a single-state fan, a bounded-complexity fan, or any family whose number of exposed adaptive maxima stays sub-polynomial below the exponent in (9).

Using the current unconditional result of Runbo Li already anchored in `SOURCES.md`, one may take

\[
\boxed{\theta=0.52.}
\tag{11}
\]

Therefore

\[
\boxed{
\Theta>0.52
\quad\Longrightarrow\quad
\text{every compact }J\Subset(1-\Theta,0.48)
\text{ has polynomially diverging fan complexity.}
}
\tag{12}
\]

This does not settle the near-critical chamber `1/2<Theta<=0.52`. It identifies exactly why the present unconditional prime-gap technology stops there: to force vanishing cell width one needs `b_1<1-theta`, while Robin's quantitative false-RH interval begins only at `1-Theta`.

## 1. Short prime intervals bound every physical CA support chamber around a selected tangent

Fix one exposed state `C` on a sufficiently late block and choose any `b\in I_C`. Write

\[
Y:=Y_C,
\qquad
h:=\log G(C)-\gamma>0,
\qquad
a:=1-e^{-h},
\tag{13}
\]

and let `Z=Z_b(C)` be the regular adaptive tangent parameter from `RE-040`,

\[
g(Z)=g(Y)-\frac{ba}{Y},
\qquad
g(x)=\frac1{x\log x}.
\tag{14}
\]

Let `xi_-<Z<xi_+` be the incoming and outgoing distinct CA event coordinates supporting `C`, so

\[
\varepsilon_-(C)=g(\xi_-),
\qquad
\varepsilon_+(C)=g(\xi_+).
\tag{15}
\]

`RE-040` gives uniformly over the compact fan

\[
\boxed{Z/Y\to1.}
\tag{16}
\]

We now use only the fact that every ordinary first-layer prime supplies a genuine CA event. The short-interval hypothesis (1) gives first-layer events on both sides of `Z` within `O(Z^theta)`.

For the left side, apply (1) at

\[
u:=Z-2Z^\theta.
\]

For all sufficiently large `Z`, there is a prime `r_-` with

\[
u-u^\theta\le r_-\le u.
\tag{17}
\]

The elementary first-layer event bound from `RE-003`,

\[
r<\eta_{r,1}<r+1,
\tag{18}
\]

then gives

\[
Z-O(Z^\theta)<\eta_{r_-,1}<Z.
\tag{19}
\]

For the right side, put

\[
v:=Z+2Z^\theta.
\]

Again by (1), there is a prime `r_+` in `[v-v^theta,v]`. Since `theta<1`,

\[
v-v^\theta>Z
\tag{20}
\]

for all sufficiently large `Z`, while `v=Z+O(Z^theta)`. Hence

\[
Z<\eta_{r_+,1}<Z+O(Z^\theta).
\tag{21}
\]

The CA event staircase contains both first-layer events. Because `xi_-` and `xi_+` are the adjacent event coordinates bracketing the regular selector `Z`, they can only be closer than the exhibited events. Thus

\[
\boxed{
0<\xi_+-\xi_-
\ll Z^\theta
\asymp Y^\theta.
}
\tag{22}
\]

No conjecture on consecutive CA quotients is used. Higher-layer or tied events only shorten the chamber further.

## 2. Event-chamber width converts directly into threshold-cell width

`RE-040` gives the exact threshold-support containment

\[
I_C\subset
\left(
\frac{Y(g(Y)-\varepsilon_-(C))}{a},
\frac{Y(g(Y)-\varepsilon_+(C))}{a}
\right),
\tag{23}
\]

and therefore

\[
|I_C|
\le
\frac{Y\bigl(g(\xi_-)-g(\xi_+)\bigr)}a.
\tag{24}
\]

Equation (22) is `o(Y)`, and (16) places the whole chamber at scale `Y`. By the mean-value theorem and

\[
|g'(x)|
=
\frac{\log x+1}{x^2(\log x)^2}
\asymp
\frac1{x^2\log x},
\tag{25}
\]

we obtain

\[
g(\xi_-)-g(\xi_+)
\ll
\frac{Y^\theta}{Y^2\log Y}
=
\frac{Y^{\theta-2}}{\log Y}.
\tag{26}
\]

Substitution into (24) yields

\[
\boxed{
|I_C|
\ll
\frac{Y^{\theta-1}}{a\log Y}.
}
\tag{27}
\]

The remaining factor is controlled by the quantitative false-RH amplitude, not by prime gaps. On every late common block, `RE-040` gives for every selected state and every `b\in J`

\[
A_b(C)=Y^b(e^h-1)\ge c_0
\tag{28}
\]

for one block-independent `c_0>0`. Since `b<=b_1`,

\[
e^h-1\ge c_0Y^{-b_1}.
\tag{29}
\]

The common fan is in the uniform small-height regime, so

\[
a=1-e^{-h}
=\frac{e^h-1}{e^h}
\gg_J Y^{-b_1}.
\tag{30}
\]

Combining (27) and (30) proves (6).

The mechanism is worth isolating. A state carrying a threshold interval of width `Delta b` moves its tangent selector at speed asymptotic to `aY log Y`; the ordinary first-layer prime events prevent one CA support chamber from extending farther than `O(Y^theta)` in the physical selector coordinate. Quantitative false RH supplies the lower bound on `a`. Equation (6) is the exact splice of those three ingredients.

## 3. A fixed threshold interval therefore requires polynomially many exposed states

Put

\[
\delta:=1-b_1-\theta>0.
\tag{31}
\]

Then (6) is

\[
|I_C|\ll_J\frac{Y_C^{-\delta}}{\log Y_C}.
\tag{32}
\]

The function on the right is decreasing for large `Y_C`. Hence, with `X_B` from (7),

\[
\max_{C\in\mathcal E(\mathcal B,J)}|I_C|
\ll_J
\frac{X_{\mathcal B}^{-\delta}}{\log X_{\mathcal B}}.
\tag{33}
\]

The rightmost-maximizer cells form an ordered finite partition of the fixed interval `J` up to endpoints. Therefore

\[
b_1-b_0
\le
N_{\mathcal B}
\max_C|I_C|,
\tag{34}
\]

which proves

\[
N_{\mathcal B}
\gg_J
X_{\mathcal B}^{\delta}\log X_{\mathcal B}.
\tag{35}
\]

The common counterexample blocks escape to infinity, so `X_B->infinity`; (10) follows.

This conclusion is about **exposed amplitude states**, not merely about the raw number of CA states in the block. The synthetic affine-envelope escape from `RE-038`--`RE-041` in which one line, or a bounded number of lines, carries all of `J` is therefore unavailable in the strongly off-critical subcase (3).

## 4. The current unconditional numerical frontier is exactly `Theta>0.52`

Runbo Li proves that `[x-x^0.52,x]` contains primes for every sufficiently large `x`. Taking `theta=0.52`, condition (4) becomes

\[
1-\Theta<b_0<b_1<0.48.
\tag{36}
\]

Such a compact interval exists exactly when

\[
\Theta>0.52.
\tag{37}
\]

For any chosen `b_1<0.48`, the explicit complexity exponent is

\[
\boxed{
\delta=0.48-b_1>0,
}
\tag{38}
\]

so the late block fan must contain at least

\[
\boxed{
N_{\mathcal B}
\gg_J
X_{\mathcal B}^{\,0.48-b_1}\log X_{\mathcal B}
}
\tag{39}
\]

exposed states.

The result also shows what would be needed to push this mechanism to every possible RH failure. A prime-in-short-interval theorem at every exponent `theta>1/2` would let one choose `theta<Theta` for every `Theta>1/2`, and the same proof would force diverging fan complexity in the full false-RH chamber. Present unconditional technology stops at `0.52`, leaving the narrow zero-frontier band

\[
\frac12<\Theta\le0.52
\tag{40}
\]

untouched by this argument.

## 5. Stress tests and exact boundary of the claim

This is not a proof of RH and not an exclusion of false RH with `Theta>0.52`. It excludes only **bounded or insufficiently complex threshold fans** in that subcase. The required polynomially many fan switches may be nonadjacent in the physical CA ladder, may skip many CA states, or may be supported by higher-layer and tied transitions. Therefore (9) does not by itself feed the adjacent first-layer fringe-bit mechanism of `RE-043`--`RE-050`.

The exponent condition is essential to the present proof. If `b_1+theta-1>=0`, equation (6) no longer makes individual cells uniformly small, so the partition argument does not force `N_B` to diverge. In particular, inserting `theta=0.52` does not say anything new when `Theta<=0.52`.

No assumption is made that ordinary prime gaps themselves are monotone, typical, or close to `log Y`. The proof uses only a worst-case prime-in-short-interval theorem to place one first-layer event on each side of the adaptive selector. Exceptional small-prime gaps or intervening higher-layer events only improve the cell-width bound.

The statement also does not require the open Alaoglu--Erdos conjecture that every consecutive CA quotient is prime. It does not even require the immediate support events `xi_\pm` to be first-layer events. The first-layer ladder is used only as an ambient mesh that upper-bounds the gap between the actual adjacent CA support events.

## 6. Prior-art boundary and research consequence

The load-bearing external input is Runbo Li's short-interval theorem, already recorded in `SOURCES.md`. Alaoglu--Erdos and the recent Mantovanelli event representation already bound the CA support/event side. A targeted current search of Robin/CA work, consecutive CA transitions, explicit counterexample windows, and applications of the `0.52` short-interval theorem found no result coupling a **whole adaptive Robin threshold cell** to the nearest first-layer prime events and deriving the cell-count lower bound (9). No new external dependency is needed.

The novelty claim is deliberately narrow. Prime existence in intervals of length `x^0.52` is Li's theorem, and the CA support interval is classical/event-workload structure. The line-specific delta is their splice with the quantitative false-RH amplitude: the same short-prime mesh that is too coarse to close the square-root local-gap problem in `RE-007` is already fine enough to force **polynomial threshold-fan complexity** whenever the zero frontier lies to the right of `0.52`.

This changes one live escape in the coherent-fan program. `RE-038` explicitly allowed the possibility that a single CA state maximizes `A_b` throughout all of `J`; `RE-041` showed that bounded or arbitrarily designed fans are synthetically realizable without source coupling. In the strong off-critical regime `Theta>0.52`, the genuine prime-event mesh rules out that bounded-complexity behavior. Any surviving false-RH model must now realize polynomially many exposed adaptive states on each sufficiently late common block, while still satisfying the uniform nonlinear prime-race calibration of `RE-040` and the interruption constraints of `RE-043`--`RE-050` whenever its switches are adjacent first-layer transitions.