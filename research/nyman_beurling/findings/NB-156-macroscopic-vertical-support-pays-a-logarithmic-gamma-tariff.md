# NB-156 — Macroscopic vertical support pays a logarithmic Gamma tariff

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-POISSON + MACROSCOPIC-VERTICAL-SUPPORT + GAMMA-TARIFF + CONDITIONING-LOCALIZATION + NB-155-FRONTIER`.

`NB-155` shows that allowing a zero-mass signed exterior sampler to spread through any vertical window of half-width `B_G=o(G)` does not change the logarithmic conditioning threshold: the spread only transports the compensating adverse zero debt. The remaining vertical-support escape was therefore described as support on the height scale itself. That boundary is too coarse. A sampler may occupy a macroscopic fraction of the height, and may even have `B_G/G -> 1`, without escaping completed-function conservation. The new cost is controlled by how close the **lowest sampled ordinate** comes to the origin through a logarithmic Gamma-profile term.

Fix `A>0`. For arbitrarily large `G`, choose

\[
0<a_G\le A,
\qquad
0\le B_G<G,
\qquad
H_G:=G-B_G\longrightarrow\infty,
\tag{1}
\]

and let

\[
K_G\subset
\{w=u+iv\in\mathbf C:
 a_G\le u\le A,
\ |v|\le B_G\}
\tag{2}
\]

be compact. Let `mu_G` be a finite real signed Borel measure supported on `K_G` with

\[
\mu_G(K_G)=0,
\qquad
V_G:=\|\mu_G\|_{\rm TV}.
\tag{3}
\]

For every nontrivial zeta zero `rho=beta+i gamma`, counted with multiplicity, define

\[
Q_G(\rho)
:=
\Re\int_{K_G}
\frac{d\mu_G(w)}{1+w+iG-\rho}.
\tag{4}
\]

Suppose a packet `F_G` of positive-ordinate zeros satisfies

\[
d_G:=|F_G|\ge\kappa\log G
\tag{5}
\]

for a fixed `kappa>0`, and every target zero has positive charge

\[
q_G:=\inf_{\rho\in F_G}Q_G(\rho)>0.
\tag{6}
\]

As in `NB-153`--`NB-155`, put

\[
C_G:=\frac{V_G}{q_G},
\qquad
D_G:=\frac{C_G}{a_G}
=\frac{V_G}{a_Gq_G}.
\tag{7}
\]

The vertical geometry contributes one further budget,

\[
\boxed{
E_G
:=
D_G
+
C_G\log\frac{G}{H_G}.
}
\tag{8}
\]

Then the signed zero sum is absolutely convergent for every `G`, and

\[
\boxed{
\sum_\rho Q_G(\rho)
=
O_A(q_GE_G).
}
\tag{9}
\]

Consequently, if

\[
A_G^-:=
\sum_{\substack{\rho\notin F_G\\ \gamma>0}}
(Q_G(\rho))_-,
\tag{10}
\]

then

\[
\boxed{
A_G^-
\ge
q_G\bigl(\kappa\log G-O_A(E_G)\bigr).
}
\tag{11}
\]

In particular,

\[
E_G=o(\log G)
\tag{12}
\]

implies

\[
A_G^-
\ge
(\kappa-o(1))q_G\log G.
\tag{13}
\]

Moreover, under `(12)` there is a constant `M=M(A,kappa)` such that a fixed fraction of this adverse charge lies inside

\[
\boxed{
|\gamma-G|
\le
B_G+M(C_G+1),
}
\tag{14}
\]

and that window contains at least

\[
\boxed{
\Omega_{A,\kappa}\!\left(
\frac{\log G}{D_G}
\right)
}
\tag{15}
\]

adverse zeros, counted with multiplicity.

Thus the vertical-support obstruction does **not** break when `B_G` first becomes comparable with `G`. What matters is the logarithmic variation of the completed Gamma background across the sampled heights. The price of descending from height `G` to the lowest sampled height `H_G` is `C_G log(G/H_G)`.

## 1. Zero mass still gives an absolutely convergent zero charge

Fix one reference point `w_0 in K_G`. Since `mu_G(K_G)=0`,

\[
\int_{K_G}
\frac{d\mu_G(w)}{1+w+iG-\rho}
=
\int_{K_G}
\left(
\frac1{1+w+iG-\rho}
-
\frac1{1+w_0+iG-\rho}
\right)d\mu_G(w).
\tag{16}
\]

For fixed `G`, the support is compact, although its diameter may now be of order `G`. As `|gamma| -> infinity`, the difference in `(16)` is

\[
O_{A,G}\!\left(
\frac{V_G}{\gamma^2}
\right).
\tag{17}
\]

The unit-interval Riemann--von Mangoldt bound therefore makes the zero sum absolutely convergent. Termwise integration in the genus-one Hadamard expansion of `xi'/xi` gives

\[
\sum_\rho Q_G(\rho)
=
\Re\int_{K_G}
\frac{\xi'}{\xi}(1+w+iG)\,d\mu_G(w).
\tag{18}
\]

The difference from `NB-155` is not convergence but uniform control of the completed-function background when the sample cloud is no longer a local `o(G)` translate.

## 2. The Gamma factor records only the logarithmic depth of the cloud

Write

\[
t:=G+\Im w.
\tag{19}
\]

By `(1)`--`(2)`, every sampled ordinate lies in

\[
H_G\le t\le 2G-H_G,
\tag{20}
\]

and `H_G -> infinity`. The completed logarithmic derivative is

\[
\frac{\xi'}{\xi}(s)
=
\frac1s+rac1{s-1}
-
\frac12\log\pi
+
\frac12\psi(s/2)
+
\frac{\zeta'}{\zeta}(s).
\tag{21}
\]

Uniform Stirling on `(20)` gives, for `s=1+w+iG`,

\[
\psi(s/2)
=
\log(s/2)+O_A(H_G^{-1}).
\tag{22}
\]

Choose any reference point at ordinate `G`. Since the total mass of `mu_G` is zero, the common `log G`, the constant `-log pi/2`, and every other `w`-independent term disappear after integration. On the upper side, `t/G<=2`; on the lower side, `t/G>=H_G/G`. Hence

\[
\sup_{w\in K_G}
\left|
\log\frac{1+w+iG}{iG}
\right|
\ll_A
1+
\log\frac{G}{H_G},
\tag{23}
\]

and therefore

\[
\left|
\Re\int_{K_G}
\frac12\psi((1+w+iG)/2)
\,d\mu_G(w)
\right|
\ll_A
V_G
\left(
1+
\log\frac{G}{H_G}
+
\frac1{H_G}
\right).
\tag{24}
\]

The rational factors in `(21)` contribute `O_A(V_G/H_G)`. On the Euler side, absolute convergence in `Re s>1` gives exactly the same boundary amplification as in `NB-154`--`NB-155`:

\[
\left|
\frac{\zeta'}{\zeta}(1+w+iG)
\right|
\le
-\frac{\zeta'}{\zeta}(1+a_G)
\ll_A
\frac1{a_G}.
\tag{25}
\]

Because `a_G<=A` and `H_G -> infinity`, the `O_A(V_G)` and `O_A(V_G/H_G)` terms in `(24)` are absorbed by `O_A(V_G/a_G)`. Combining `(18)`--`(25)` yields

\[
\sum_\rho Q_G(\rho)
=
O_A\!\left(
\frac{V_G}{a_G}
+
V_G\log\frac{G}{H_G}
\right)
=
O_A(q_GE_G),
\tag{26}
\]

which is `(9)`.

The new term is therefore not proportional to the diameter `B_G` itself. It is the variation of the real Gamma profile `log t` across the cloud. A sampler can spread through almost the whole interval from `0` to `2G` while paying only a sublogarithmic tariff, provided its lowest height remains sufficiently close to `G` on the logarithmic scale.

## 3. The target packet still forces real adverse zero charge

The target packet contributes

\[
\sum_{\rho\in F_G}Q_G(\rho)
\ge
\kappa q_G\log G.
\tag{27}
\]

Zeros with negative ordinate are separated from every sample by at least `H_G+|gamma|`. Since

\[
\Re\frac1{1+w+iG-\rho}
=
\frac{1+\Re w-\beta}
{(1+\Re w-\beta)^2+(G+\Im w-\gamma)^2},
\tag{28}
\]

Riemann--von Mangoldt shell counting gives

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_A
V_G\frac{\log H_G}{H_G}
=
o_A\!\left(\frac{V_G}{a_G}\right).
\tag{29}
\]

Splitting the positive-ordinate zeros outside `F_G` into positive and negative charges and using `(26)` and `(29)` therefore gives

\[
A_G^-
\ge
\kappa q_G\log G
-
O_A\!\left(
\frac{V_G}{a_G}
+
V_G\log\frac{G}{H_G}
\right),
\tag{30}
\]

which is `(11)`. Under `(12)` this becomes `(13)`.

The maximum charge of one zero is still controlled only by the horizontal boundary gap. Since every nontrivial zero has `beta<1`, equation `(28)` implies

\[
\boxed{
|Q_G(\rho)|
\le
\frac{V_G}{a_G}
=
q_GD_G.
}
\tag{31}
\]

In particular `D_G>=1`. Vertical spreading changes where charge can be placed, while the amount one individual zero can carry continues to be set by the same gap-normalized condition number.

## 4. Macroscopic support transports the debt but does not erase it

Let

\[
y:=G-\gamma.
\tag{32}
\]

Outside the vertical support with an additional margin `r>=1`, namely whenever

\[
|y|\ge B_G+r,
\tag{33}
\]

one has

\[
|G+\Im w-\gamma|
\ge
|y|-B_G
\ge r
\tag{34}
\]

for every `w in K_G`. Resolving the exterior region into unit shells according to the distance `|y|-B_G`, equation `(28)` and Riemann--von Mangoldt give, uniformly for `1<=r=o(G)`,

\[
\sum_{\substack{\gamma>0\\ |\gamma-G|\ge B_G+r}}
|Q_G(\rho)|
\ll_A
V_G\frac{\log G}{r}.
\tag{35}
\]

Condition `(12)` implies `D_G=o(log G)` and therefore

\[
C_G=a_GD_G\le AD_G=o(\log G).
\tag{36}
\]

Take

\[
r_G:=M(C_G+1)
\tag{37}
\]

with `M=M(A,kappa)` sufficiently large. Then `r_G=o(log G)=o(G)`, and `(35)` becomes

\[
\sum_{\substack{\gamma>0\\ |\gamma-G|\ge B_G+r_G}}
|Q_G(\rho)|
\le
O_{A}(M^{-1}q_G\log G).
\tag{38}
\]

Choosing `M` so that the right side is a small fixed fraction of `(13)` proves the localization claim `(14)`. Dividing the localized adverse charge by the pointwise maximum `q_GD_G` from `(31)` proves `(15)`.

The resulting tradeoff is

\[
\boxed{
\text{adverse radius}
=
B_G+O_{A,\kappa}(C_G+1),
\qquad
\text{adverse population}
=
\Omega_{A,\kappa}\!\left(
\frac{\log G}{D_G}
\right),
}
\tag{39}
\]

subject to the combined budget `E_G=o(log G)`. The transport scale and the conservation cost are therefore different quantities: `B_G` determines how far the sampler can move the debt, while only the logarithmic Gamma depth `log(G/H_G)` enters the completed-background budget.

## 5. The actual vertical phase boundary is logarithmic

Several regimes follow immediately from `(8)`.

First, suppose

\[
B_G\le\beta G
\tag{40}
\]

for any fixed `0<=beta<1`. Then `H_G>=(1-beta)G`, so

\[
\log\frac{G}{H_G}
\le
\log\frac1{1-\beta}
=O_\beta(1).
\tag{41}
\]

Because `C_G<=A D_G`, one has `E_G<<_{A,beta}D_G`. Thus

\[
\boxed{
D_G=o(\log G)
\quad\Longrightarrow\quad
A_G^-\ge(\kappa-o(1))q_G\log G
}
\tag{42}
\]

through **every fixed-fraction macroscopic vertical window**. This strictly extends the `B_G=o(G)` regime of `NB-155`.

Second, even `B_G/G -> 1` need not be an escape. For example, if

\[
H_G=G^{1-o(1)}
\tag{43}
\]

and `C_G=O(1)`, then

\[
C_G\log\frac{G}{H_G}
=o(\log G),
\tag{44}
\]

so the same debt conclusion survives whenever `D_G=o(log G)`. The cloud may descend through a `1-o(1)` fraction of the absolute height while completed-function conservation remains decisive.

Third, if `H_G=G^theta` with a fixed `0<theta<1` and `C_G` stays of constant order, then

\[
C_G\log\frac{G}{H_G}
=
(1-\theta)C_G\log G,
\tag{45}
\]

which is already on the same logarithmic scale as the target packet. At that point `(11)` still supplies an explicit constant competition, but the `o(log G)` conclusion no longer follows merely from sublogarithmic `D_G`. When the support reaches heights whose logarithmic distance from `G` is macroscopic, the Gamma factor itself can carry a logarithmic signed budget.

This identifies the genuine vertical frontier for this method:

\[
\boxed{
\text{vertical escape currency}
=
C_G\log(G/H_G),
\quad
H_G=G-B_G,
}
\tag{46}
\]

rather than the binary condition `B_G=o(G)` versus `B_G asymp G`.

## 6. What remains open

The result does not classify the regime

\[
D_G+C_G\log(G/H_G)\asymp\log G,
\tag{47}
\]

where the completed Gamma background, the Euler-side boundary amplification, and the target packet can all live on the same scale. In particular, it does not exclude samplers whose lower support reaches polynomially smaller heights with enough signed cancellation to neutralize the Gamma profile.

It also retains the bounded horizontal-width hypothesis `Re w<=A`. Growing horizontal diameter can change both the Euler-side geometry and the far-field scale. Nor does the argument exploit cancellation inside the signed von-Mangoldt series; equation `(25)` deliberately uses the absolute Euler bound. A sampler with `D_G` or the Gamma tariff on the logarithmic scale could still be useful if its signed prime-side structure is substantially smaller than total variation predicts.

Finally, the packet hypothesis remains conditional. No claim is made that zeta possesses a packet of `Omega(log G)` zeros receiving positive charge from such a sampler. The theorem says that **if** such a target packet exists, then vertical support on a macroscopic height scale does not isolate it unless the sampler also pays the explicit Gamma/conditioning budget in `(8)` or uses information discarded by the completed-function estimate.

## Prior-art search

Bruna and Melnikov, *On translates of the Poisson kernel and zeros of harmonic functions*, Bull. London Math. Soc. 39 (2007), 317--326, give the nearby harmonic-analysis boundary for systems of Poisson translates. Chirre and Molero, *Explicit conditional bounds for zeta(s) at the edge of the critical strip*, Port. Math. (published online 19 June 2026), use Guinand--Weil together with extremal Poisson majorants and minorants to control the logarithmic derivative on `Re s=1` under RH. A fresh search also found recent Poisson-forcing work for the completed xi function, but not a target-conditioned theorem for zero-mass exterior signed samplers whose vertical diameter is comparable with the sampling height and whose Gamma-background cost is quantified by the lower sampled ordinate.

None of those external results is load-bearing here. The proof uses the same Hadamard identity, exterior Euler bound, Stirling estimate and Riemann--von Mangoldt shell counting already used in `NB-151`--`NB-155`; the new step is their uniform splice through the variable lower height `H_G`. Accordingly no new `SOURCES.md` anchor is required.

## Conclusion

`NB-155` left height-scale vertical support as a possible escape because its uniform Stirling step assumed `B_G=o(G)`. The escape is narrower than that. As long as the lowest sampled ordinate `H_G=G-B_G` tends to infinity, zero-mass conservation survives with the explicit extra tariff

\[
C_G\log\frac{G}{H_G}.
\]

Every fixed-fraction macroscopic window therefore remains trapped at the same `D_G=o(log G)` threshold, and even windows with `B_G/G -> 1` remain trapped whenever their logarithmic depth is subcritical. The meaningful new resource is not macroscopic diameter by itself but enough descent in absolute height for the Gamma profile to accumulate a logarithmic budget, or some additional signed prime/Nyman structure capable of cancelling that budget.