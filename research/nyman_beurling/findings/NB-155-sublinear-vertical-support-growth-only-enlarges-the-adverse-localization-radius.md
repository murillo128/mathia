# NB-155 — Sublinear vertical support growth only enlarges the adverse localization radius

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-POISSON + GROWING-VERTICAL-SUPPORT + CONDITIONING-LOCALIZATION + NB-154-FRONTIER`.

`NB-154` closes the simplest moving-boundary escape for zero-mass signed exterior samplers, but keeps the sampler's vertical diameter uniformly bounded. One remaining possibility is therefore to let the sample cloud spread farther and farther in ordinate while retaining the same horizontal exterior geometry. This does not change the conditioning threshold as long as the vertical spread is sublinear in the sampling height. It only enlarges the window in which the compensating adverse zero debt may live.

Fix `A>0`. For arbitrarily large `G`, choose

\[
0<a_G\le A,
\qquad
B_G\ge0,
\qquad
B_G=o(G),
\tag{1}
\]

and let

\[
K_G\subset
\{w\in\mathbf C:
 a_G\le\Re w\le A,
\ |\Im w|\le B_G\}
\tag{2}
\]

be compact. Let `mu_G` be a finite real signed Borel measure supported on `K_G` with

\[
\mu_G(K_G)=0,
\qquad
V_G:=\|\mu_G\|_{\rm TV}.
\tag{3}
\]

For a nontrivial zero `rho=beta+i gamma`, counted with multiplicity, define

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

As in `NB-153`--`NB-154`, put

\[
C_G:=\frac{V_G}{q_G},
\qquad
D_G:=\frac{C_G}{a_G}
=\frac{V_G}{a_Gq_G}.
\tag{7}
\]

Then the signed zero sum is absolutely convergent for every `G`, and along every family satisfying `(1)` one has

\[
\boxed{
\sum_\rho Q_G(\rho)
=O_A\!\left(\frac{V_G}{a_G}\right).
}
\tag{8}
\]

Consequently, if

\[
A_G^-:=
\sum_{\substack{\rho\notin F_G\\ \gamma>0}}
(Q_G(\rho))_-,
\tag{9}
\]

then

\[
\boxed{
A_G^-
\ge
q_G\bigl(\kappa\log G-O_A(D_G)\bigr).
}
\tag{10}
\]

In particular,

\[
D_G=o(\log G)
\tag{11}
\]

still implies

\[
A_G^-
\ge(\kappa-o(1))q_G\log G.
\tag{12}
\]

The vertical spread appears only in the localization radius. There is a constant `M=M(A,kappa)` such that, under `(11)`,

\[
R_G:=2B_G+4+M C_G
\tag{13}
\]

satisfies `R_G=o(G)` and captures a fixed fraction of the adverse charge:

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\ \gamma>0\\ |\gamma-G|\le R_G}}
(Q_G(\rho))_-
\gg_{A,\kappa}
q_G\log G.
}
\tag{14}
\]

Moreover that window contains at least

\[
\boxed{
\Omega_{A,\kappa}\!\left(
\frac{\log G}{D_G}
\right)
}
\tag{15}
\]

adverse zeros, counted with multiplicity. Thus any `o(G)` vertical diameter is compatible with the same gap-normalized conditioning threshold as `NB-154`: spreading the cloud vertically can transport the debt by `O(B_G)`, but it does not reduce the forced adverse population or the logarithmic conditioning scale at which completed-function conservation stops deciding the question.

## 1. Growing vertical diameter does not spoil the completed-function cancellation

Fix one reference point `w_0 in K_G`. Zero total mass gives

\[
\int_{K_G}\frac{d\mu_G(w)}{1+w+iG-\rho}
=
\int_{K_G}
\left(
\frac1{1+w+iG-\rho}
-
\frac1{1+w_0+iG-\rho}
\right)d\mu_G(w).
\tag{16}
\]

For each fixed `G`, the support is compact. Once `|G-\gamma|` is larger than a fixed multiple of `B_G+A+1`, the integrand difference in `(16)` is

\[
O\!\left(
\frac{(A+B_G)V_G}{(G-\gamma)^2}
\right).
\tag{17}
\]

The unit-interval Riemann--von Mangoldt bound therefore makes the zero sum absolutely convergent; the finitely many zeros in the central ordinate range cause no convergence issue. Termwise integration in the genus-one Hadamard formula gives exactly as before

\[
\sum_\rho Q_G(\rho)
=
\Re\int_{K_G}
\frac{\xi'}{\xi}(1+w+iG)\,d\mu_G(w).
\tag{18}
\]

Because `B_G=o(G)`, for all sufficiently large `G` the whole cloud lies in `|\Im w|\le G/2`. Uniformly on `(2)`, the rational terms in `xi'/xi` are `O_A(1/G)`, while Stirling gives

\[
\psi((1+w+iG)/2)
=
\log(iG/2)
+O_A\!\left(\frac{1+B_G}{G}\right).
\tag{19}
\]

The common logarithm and constant terms disappear against `mu_G(K_G)=0`. The remaining Gamma contribution is `o(V_G)`. On the Euler side, absolute convergence in `Re s>1` gives

\[
\left|
\frac{\zeta'}{\zeta}(1+w+iG)
\right|
\le
-\frac{\zeta'}{\zeta}(1+a_G)
\ll_A\frac1{a_G}.
\tag{20}
\]

Since `a_G<=A`, the `o(V_G)` Gamma remainder is also `o_A(V_G/a_G)`. Equations `(18)`--`(20)` prove `(8)`. The important point is that the vertical diameter may diverge: while it remains `o(G)`, its only effect on the completed background is an `o(V_G)` variation after the common logarithm has been cancelled.

## 2. The target packet still creates logarithmic real-zero debt

The target packet contributes

\[
\sum_{\rho\in F_G}Q_G(\rho)
\ge
\kappa q_G\log G.
\tag{21}
\]

Zeros with negative ordinate remain far from the entire growing cloud. If `w=u+iv`, then

\[
\Re\frac1{1+w+iG-\rho}
=
\frac{1+u-\beta}
{(1+u-\beta)^2+(G+v-\gamma)^2}.
\tag{22}
\]

For `gamma<0`, condition `(1)` gives `G+v-gamma >= G-B_G+|gamma|`, which is comparable to `G+|gamma|` for large `G`. Shell counting therefore yields

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_A
V_G\frac{\log G}{G}.
\tag{23}
\]

This is absorbed by the error in `(8)`. Splitting the positive-ordinate zeros outside `F_G` into positive and negative charges then gives

\[
A_G^-
\ge
\kappa q_G\log G
-O_A\!\left(\frac{V_G}{a_G}\right),
\tag{24}
\]

which is `(10)`. Substitution of `(7)` gives `(12)` whenever `D_G=o(log G)`.

The pointwise amplification remains unchanged by the vertical diameter. Since every nontrivial zero has `beta<1`,

\[
1+\Re w-\beta\ge a_G,
\]

and `(22)` implies

\[
\boxed{
|Q_G(\rho)|
\le\frac{V_G}{a_G}
=q_GD_G.
}
\tag{25}
\]

In particular `D_G>=1`, as already in `NB-154`. Vertical spreading creates more possible ordinate locations at which charge may be deposited, but it creates no larger pointwise Poisson amplification than the horizontal boundary gap already provides.

## 3. Vertical spreading buys displacement additively, not population reduction

Let

\[
y:=G-\gamma.
\]

Whenever

\[
|y|\ge 2B_G+4,
\tag{26}
\]

one has `|y+v|>=|y|/2` for every `w=u+iv in K_G`. Since `1+u-beta<=A+1`, equation `(22)` gives the uniform far-field bound

\[
|Q_G(\rho)|
\ll_A
\frac{V_G}{(G-\gamma)^2}.
\tag{27}
\]

Hence, for every `R>=2B_G+4` with `R=o(G)`, Riemann--von Mangoldt shell counting gives

\[
\sum_{\substack{\gamma>0\\ |\gamma-G|\ge R}}
|Q_G(\rho)|
\ll_A
V_G
\left(
\frac{\log G}{R}
+
\frac{\log G}{G}
\right).
\tag{28}
\]

Under `(11)`,

\[
C_G=a_GD_G\le A D_G=o(\log G),
\tag{29}
\]

so `(1)` and `(13)` imply `R_G=o(G)`. Since `R_G>=M C_G`, substituting `R=R_G` in `(28)` gives

\[
\sum_{|\gamma-G|\ge R_G}|Q_G(\rho)|
\le
O_A(M^{-1}q_G\log G)
+o(q_G\log G).
\tag{30}
\]

Choosing `M` sufficiently large relative to `A` and `kappa`, equations `(12)` and `(30)` prove `(14)`. Finally `(25)` bounds the charge of every individual adverse zero by `q_GD_G`; dividing `(14)` by that pointwise maximum proves `(15)`.

The tradeoff is therefore explicit:

\[
\boxed{
\text{adverse radius}
=O(B_G+C_G+1),
\qquad
\text{adverse population}
=\Omega\!\left(\frac{\log G}{D_G}\right).
}
\tag{31}
\]

The two resources separate. `B_G` buys only vertical displacement because the far-field Poisson decay starts after the support itself has been cleared. `D_G` controls both how much completed-function remainder may absorb the target charge and how much charge one individual adverse zero can carry.

## 4. What growing support remains genuinely open

`NB-154` listed growing support diameter as one escape from its fixed compact geometry. The vertical part of that escape is now substantially narrower. An arbitrarily growing vertical diameter

\[
B_G\longrightarrow\infty,
\qquad
B_G=o(G),
\tag{32}
\]

does not alter the logarithmic gap-normalized conditioning threshold. It only changes the localization statement from a bounded/`O(C_G)` neighbor window to an `O(B_G+C_G)` window.

Thus a sampler cannot evade signed conservation merely by mixing an increasing but subheight range of neighboring ordinates. To make vertical support itself a qualitatively different currency, the cloud must reach a **macroscopic fraction of the absolute height**, where the completed Gamma background and the separation between positive- and negative-ordinate zeros can no longer be treated as a common local translate. That macroscopic regime is not classified here.

The theorem also retains the bounded horizontal-width hypothesis `Re w<=A`. Letting the horizontal diameter grow with `G` may change the far-field kernel scale and is not covered. Nor does the theorem classify the threshold `D_G asymp log G`, exploit cancellation in the signed von-Mangoldt/Euler term, or couple the sampler directly to target-bearing Nyman data before the zero charges are separated.

As throughout `NB-151`--`NB-154`, the packet hypothesis is conditional. This is not a zero-spacing theorem or a claim that a logarithmic packet exists. It says that **if** an actual logarithmic zeta-zero packet receives uniformly positive charge from such a sampler, then sublogarithmic gap-normalized conditioning cannot isolate it, even when the sampler's vertical support diverges through every `o(G)` scale.

## Prior-art search

Bruna and Melnikov, *On translates of the Poisson kernel and zeros of harmonic functions*, Bull. London Math. Soc. 39 (2007), 317--326, provide the nearby harmonic-analysis boundary for Poisson translates. Differenced logarithmic derivatives are classical in zero-free-region arguments; Ethan S. Lee's explicit Dedekind-zeta work is a modern example. Chirre and Molero, *Explicit conditional bounds for zeta(s) at the edge of the critical strip*, Port. Math. (published online 19 June 2026), use Guinand--Weil and extremal Poisson majorants/minorants to control logarithmic derivatives on `Re s=1` under RH. A fresh search also located classical work on the distribution and logarithmic derivative of zeta, but not a target-conditioned theorem for zero-mass exterior measures whose vertical support grows with the sampling height.

These sources delimit the generic Poisson/logarithmic-derivative landscape. None is load-bearing for `(8)`--`(31)`: the extension follows directly from the completed-function identity, the exterior Euler bound, Stirling and Riemann--von Mangoldt shell counting already anchored in the line. No `SOURCES.md` update is therefore required.

## Source map

- `NB-148`: zero total mass cancels the universal Hadamard logarithm and creates signed Poisson debt.
- `NB-153`: compact two-dimensional samplers localize that debt on the `C_G` conditioning radius.
- `NB-154`: boundary approach replaces `C_G` by the gap-normalized condition `D_G=C_G/a_G` and leaves growing support as an explicit open regime.
- The completed `xi` logarithmic derivative, the exterior Euler estimate and Riemann--von Mangoldt/unit-interval shell counting are already anchored inputs of the line.

## Consequence for the line

Sublinear vertical support growth is not a new way around the signed-Poisson obstruction. **For every zero-mass exterior sampler with bounded horizontal width, vertical radius `B_G=o(G)` and gap-normalized conditioning `D_G=o(log G)`, an `Omega(log G)` positively charged target packet still forces `Omega(q_G log G)` actual adverse zero charge. A fixed fraction lies within radius `O(B_G+C_G+1)` and requires at least `Omega(log G/D_G)` adverse zeros.**

The live signed frontier is correspondingly smaller: logarithmic-or-worse gap-normalized conditioning with genuine prime-side cancellation, horizontal support growth, macroscopic-height vertical mixing, or a target-aware Nyman/Euler coupling that avoids separating the signed zero charges.