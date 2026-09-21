# NB-261 — Near-full positive carriers suppress fixed Ford depths but export the obstruction to a shrinking boundary layer

> **Representation:** _Nyman–Beurling / Hardy-projected destination interface._ The line-specific inputs are the exact Euler normalization, the `H`-resolved carrier dictionary and shell-Hilbert/`ell^2` identification of `NB-257`, the legal complex zero evaluation of `NB-259`, and the effective depth scale `N_J=J/A_J` from `NB-260`. The generic engine is the normalized geometric sum. This is a constructive route correction: the fixed-power depth-rank obstruction of `NB-260` is essentially sharp at exponent level for suppressing every fixed positive fraction of the Ford depth ladder. A near-full positive carrier can make the complete fixed-depth destination rectangle uniformly small at bounded—and in fact vanishing shell-Hilbert—cost. It does **not** remove the Ford obstruction: positivity leaves a shrinking boundary layer next to the Euler anchor, and inside that layer a Bellotti-compatible carrier-locked packet at depth `X(1-beta)=log(J/K)+O(1)` still carries order-one residue mass.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + HARDY-PROJECTED-ZERO-EVALUATION + H-SEPARATED-POSITIVE-CARRIER + NEAR-FULL-DEPTH-RANK + GEOMETRIC-SUM-CONSTRUCTION + FIXED-DEPTH-RECTANGLE-SUPPRESSION + SHRINKING-BOUNDARY-LAYER + SHALLOW-REPLACEMENT-PACKET + MATCHED-CONTROL + NB-260-REFINEMENT + DESTINATION-INTERFACE + METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-260` proves that, with

\[
A_J:=\frac{\log J}{Y},
\qquad
N_J:=\frac{J}{A_J}\asymp\frac{J}{\log J},
\]

a bounded-cost resolved scalar carrier cannot suppress a fixed positive fraction of the legal depth ladder while

\[
K\le N_J^{1-\delta}
\]

for any fixed `delta>0`. The surviving question was whether a near-full effective depth rank can actually suppress the two-dimensional destination rectangle, or whether the full Ford ordinate width creates a new coercive obstruction.

There is a simple constructive answer for the fixed-depth rectangle. Let `m=m_J` satisfy

\[
1\ll m\ll A_J,
\]

and take

\[
\boxed{
K:=\left\lfloor\frac{J}{m}\right\rfloor.
}
\]

Then

\[
\frac{K}{N_J}\sim\frac{A_J}{m}\longrightarrow\infty,
\qquad
\frac KJ\sim\frac1m\longrightarrow0,
\]

so this is still an `o(J)`-span carrier but has near-full effective depth rank,

\[
K=N_J^{1+o(1)}.
\]

Put equal positive Euler-normalized mass on the one-sided `H`-grid,

\[
\lambda_J:=\frac1K\sum_{j=0}^{K-1}\delta_{jH}.
\]

Its legal Ford carrier is

\[
\boxed{
C_J(w)
=\frac1K\sum_{j=0}^{K-1}e^{ijw/J}
=\frac{1-e^{iKw/J}}{K(1-e^{iw/J})}.
}
\]

For legal zero coordinates

\[
w=x+i sA_J,
\qquad
x:=R(\gamma-t_0),
\qquad
s:=\frac{X(1-\beta)}{\log J},
\]

write

\[
q=e^{-s/N_J+i x/J}.
\]

Then, for every fixed `s_0>0`,

\[
|C_J(x+i sA_J)|
\le
\frac{2}{K(1-e^{-s/N_J})}
\ll_{s_0}
\frac{N_J}{K}
\sim
\frac{m}{A_J}
\longrightarrow0
\]

uniformly for all real `x` and all `s_0\le s\le1`. In particular, for every fixed hard-window constant `B`,

\[
\boxed{
\sup_{\substack{|x|\le BJ\\ s_0\le s\le1}}
|C_J(x+i sA_J)|
=o(1).
}
\]

Thus the full `Theta(J)` Ford ordinate width does **not** restore coercivity on a depth rectangle bounded away from the Euler edge. The obstruction instead migrates into a shrinking depth layer. At vertical Ford depth

\[
u:=X(1-\beta),
\]

the same carrier satisfies

\[
C_J\!\left(i\frac{u}{Y}\right)
=\frac{1-e^{-Ku/(YJ)}}{K(1-e^{-u/(YJ)})}
=\frac{1-e^{-u/(Ym)+o(1)}}{u/(Ym)+o(u/m)}.
\]

Hence

\[
\boxed{
C_J\!\left(i\frac{u}{Y}\right)=1+o(1)
\qquad\text{whenever }u=o(m).
}
\]

The fixed-depth rectangle is therefore suppressed only because its depths satisfy `u~s log J`, while the normalized positive average keeps order-one coherence throughout a much shallower boundary layer `u=o(m)`.

The old positivity obstruction reappears sharply inside that layer. Set

\[
\boxed{
m=\frac{J}{K}\sim\frac{R}{W},
\qquad W:=KH\sim\frac{R}{m}.
}
\]

At the matched depth

\[
\boxed{
X(1-\beta)=\log m+d_*,
}
\]

with fixed `d_*`, choose `M=floor(delta m)` carrier-locked ordinates

\[
\gamma_n=t_0+\frac{2\pi qn}{X},
\qquad 1\le n\le M,
\]

where `q` is the same fixed spacing integer used in the earlier Bellotti population audit and `delta>0` is sufficiently small. Because

\[
\frac{K}{J}R(\gamma_n-t_0)
=O\!\left(\frac n m\right)
=O(\delta)
\]

and

\[
\frac{K}{J}R(1-\beta)
=\frac{\log m+O(1)}{Ym}
=o(1),
\]

all `K` positive carrier channels remain in a fixed right half-plane on the whole packet. Therefore

\[
\boxed{
\inf_{1\le n\le M}
\Re C_J\!\left(R(\gamma_n-t_0)+iR(1-\beta)\right)
\ge c_0>0.
}
\]

The original shell envelope also satisfies `F(H[(gamma_n-t_0)+i(1-beta)])=F(0)+o(1)` uniformly on the packet, the main carrier phases obey `e^{iX(gamma_n-t_0)}=1`, and the Ford damping is

\[
e^{-X(1-\beta)}=e^{-d_*}m^{-1}.
\]

With `M~delta m`, the complete signed Hardy-projected residue contribution of this matched control remains bounded away from zero. The same zero-free, Bellotti local-count, growing-density and ordinary zero-count ledger already audited for `NB-231`, `NB-254` and `NB-260` permits this replacement packet when `m\to\infty`; this is a compatibility control, not a claim that the actual zeta zeros realize the packet.

The conclusion is a sharper destination-side picture than the one left by `NB-260`:

\[
\boxed{
\begin{array}{c}
K=N_J^{1+o(1)}\text{ can suppress every fixed }s\ge s_0>0\text{ across the full hard ordinate window},\\[2mm]
\text{but if }m=J/K\to\infty\text{ then an order-one matched packet survives at }X(1-\beta)=\log m+O(1).
\end{array}
}
\]

Equivalently, the two-dimensional target cannot be a rectangle with a fixed lower depth edge. As rank grows, the live obstruction chases that edge toward the Euler anchor. A coercive destination theorem capable of closing this scalar route must control a **shrinking Ford boundary layer** whose depth scale follows `log(J/K)`, or use a genuinely different Hardy/Nyman quantity that couples the boundary anchor to the interior.

## 1. The near-full positive dictionary is legal and cheap

Retain the resolved setup of `NB-257`--`NB-260`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR,
\qquad
J:=\frac RH\to\infty,
\]

with `Y` in a fixed compact subinterval of `(0,infinity)`, and fix

\[
0<a<b<1,
\qquad
0\le\phi\in C_c^\infty((a,b)),
\qquad
\operatorname{diam}(\operatorname{supp}\phi)<1.
\]

As before, the support-diameter condition makes `H`-translates of the shell disjoint. Define

\[
A_J:=\frac{\log J}{Y},
\qquad
N_J:=\frac{J}{A_J}.
\]

Choose any auxiliary scale satisfying

\[
\boxed{
1\ll m=m_J\ll A_J
}
\]

and set

\[
K:=\left\lfloor\frac{J}{m}\right\rfloor.
\]

Then

\[
K=o(J),
\qquad
\frac K{N_J}\sim\frac{A_J}{m}\to\infty.
\]

Since `A_J` is logarithmic,

\[
\frac{\log K}{\log N_J}\to1,
\]

so `K=N_J^{1+o(1)}`. This is exactly the scale not excluded by the fixed-power theorem in `NB-260`.

Use one-sided offsets

\[
\xi_j=jH,
\qquad 0\le j<K,
\]

and the positive Euler-normalized measure

\[
\boxed{
\lambda_J=\frac1K\sum_{j=0}^{K-1}\delta_{\xi_j}.
}
\]

As in `NB-255` and `NB-257`, convert back to the physical coefficient measure by

\[
d\nu_J(\xi)=e^{r\xi/X}\,d\lambda_J(\xi).
\]

The exact Euler normalization is then

\[
\int e^{-r\xi/X}\,d\nu_J(\xi)
=\lambda_J(\mathbb R)
=1.
\]

The physical carrier span is

\[
W=(K-1)H\sim KH
\sim\frac{R}{m},
\]

so

\[
\frac WR\sim\frac1m\to0.
\]

Thus all translated shells remain inside `X+o(X)`. In particular,

\[
\max_j\frac{r\xi_j}{X}
\ll\frac{W}{X}
=O(m^{-1})
=o(1).
\]

Disjointness gives the exact shell-Hilbert identity

\[
H\|h_{\nu_J}\|_2^2
=\|\phi\|_2^2
\frac1{K^2}
\sum_{j=0}^{K-1}e^{2rjH/X}.
\]

Hence

\[
\boxed{
H^{1/2}\|h_{\nu_J}\|_2
=(1+o(1))\frac{\|\phi\|_2}{\sqrt K}
\longrightarrow0.
}
\]

So the construction does not buy its near-full depth rank by inflating physical shell-Hilbert cost. The cost actually decreases because the fixed Euler mass is spread over `K` disjoint channels.

This statement concerns the resolved source dictionary used in this branch; it is not by itself a statement about the final Nyman distance.

## 2. The normalized geometric sum kills the whole fixed-depth rectangle

The Euler-normalized extra carrier is

\[
C_J(w)
:=B_{\lambda_J}(w/R)
=\frac1K\sum_{j=0}^{K-1}e^{ijw/J}.
\]

For a legal zero evaluation put

\[
w=x+i sA_J,
\qquad
x=R(\gamma-t_0),
\qquad
s=\frac{X(1-\beta)}{\log J}.
\]

Because `A_J/J=1/N_J`,

\[
C_J(x+i sA_J)
=\frac1K\sum_{j=0}^{K-1}
\left(e^{-s/N_J+i x/J}\right)^j.
\]

Set

\[
q:=e^{-s/N_J+i x/J}.
\]

For `s>0`, `|q|<1`, so the exact geometric-sum identity gives

\[
C_J(x+i sA_J)
=\frac{1-q^K}{K(1-q)}.
\]

The numerator satisfies

\[
|1-q^K|\le1+|q|^K\le2,
\]

while the denominator has the radial lower bound

\[
|1-q|
\ge1-|q|
=1-e^{-s/N_J}.
\]

Fix `s_0>0`. Uniformly for `s_0\le s\le1`,

\[
1-e^{-s/N_J}
\ge\frac{s}{2N_J}
\]

for all sufficiently large `J`. Consequently

\[
\boxed{
|C_J(x+i sA_J)|
\le
\frac{4N_J}{Ks}
\ll_{s_0}\frac{m}{A_J}
=o(1),
}
\]

uniformly in **every real `x`**. In particular the estimate is stronger than what the hard Ford window asks for:

\[
\sup_{\substack{|x|\le BJ\\s_0\le s\le1}}
|C_J(x+i sA_J)|
=o(1)
\]

for every fixed `B` and `s_0`.

The original smooth shell contributes the factor

\[
F\!\left(H[(\gamma-t_0)+i(1-\beta)]\right)
=F\!\left(\frac{w}{J}\right).
\]

On `|x|\le BJ` and `0\le s\le1`, the arguments `w/J` remain in a fixed compact horizontal set with imaginary part `O(A_J/J)=o(1)`. Since `F` is entire and fixed, it is uniformly bounded there. Therefore the complete smooth zero mark inherits the `o(1)` carrier suppression on every rectangle

\[
|x|\le BJ,
\qquad
s_0\le s\le1.
\]

This answers one half of the frontier left by `NB-260`: the simultaneous `Theta(J)` ordinate width does not create a new fixed-depth lower bound once `K` reaches the near-full effective scale.

It also shows that the fixed-power lower bound of `NB-260` is sharp at exponent level. That finding forces `K\ge N_J^{1-o(1)}` to suppress a fixed depth interval. Here

\[
K
=N_J\frac{A_J}{m}(1+o(1))
=N_J^{1+o(1)}
\]

and suppression is explicit.

## 3. What the construction really does is create a shrinking boundary layer

The estimate above degenerates as `s\downarrow0`, and that degeneration is structural rather than technical. Write the physical Ford depth as

\[
u:=X(1-\beta).
\]

Then

\[
s=\frac{u}{\log J},
\qquad
sA_J=\frac{u}{Y}.
\]

On the vertical axis,

\[
C_J\!\left(i\frac uY\right)
=
\frac{1-e^{-Ku/(YJ)}}
{K(1-e^{-u/(YJ)})}.
\]

Because `K/J=1/m+o(1/m)`, if `u=o(m)` then

\[
\frac{Ku}{YJ}=o(1),
\qquad
K(1-e^{-u/(YJ)})
=\frac{Ku}{YJ}(1+o(1)).
\]

Thus

\[
\boxed{
C_J\!\left(i\frac uY\right)
=1+o(1)
\qquad (u=o(m)).
}
\]

More generally the vertical transition profile is governed by

\[
\frac{1-e^{-u/(Ym)}}{u/(Ym)}.
\]

Hence the positive average only begins to attenuate substantially once `u` reaches order `m`. Since `m=o(A_J)=o(log J)`, this transition layer is a vanishing fraction of the normalized depth ladder even though its unscaled Ford depth still tends to infinity.

This is exactly why a rectangle with a fixed lower edge `s_0>0` is too coarse a target. The construction can move all of its unavoidable coherence into

\[
s\lesssim\frac{m}{\log J}=o(1).
\]

The matched zeta-compatible packet below sits even closer to the Euler anchor, at depth `u~log m`, safely inside this coherent layer because

\[
\log m=o(m).
\]

## 4. A shallow `Theta(m)` packet restores order-one residue mass

The span of the positive mixture is

\[
W\sim\frac{R}{m},
\]

so its positive-coherence capacity is

\[
\frac RW\sim m.
\]

This is the `NB-254` parameter, now emerging inside a family that already suppresses every fixed positive depth fraction.

Fix a real constant `d_*`. Place the control packet at

\[
\boxed{
X(1-\beta)=\log m+d_*.
}
\]

Then

\[
R(1-\beta)
=\frac{\log m+d_*}{Y}.
\]

Choose the same fixed carrier-locking spacing integer `q` used in the earlier Bellotti-compatible packet audit and put

\[
\gamma_n
=t_0+\frac{2\pi qn}{X},
\qquad
1\le n\le M,
\qquad
M:=\lfloor\delta m\rfloor,
\]

for a sufficiently small fixed `delta>0`. The main carrier is exactly aligned:

\[
e^{iX(\gamma_n-t_0)}=1.
\]

The real Ford coordinates are

\[
x_n
=R(\gamma_n-t_0)
=\frac{2\pi qn}{Y}.
\]

For every channel index `0\le j<K`,

\[
\left|\frac{j x_n}{J}\right|
\le
\frac{Kx_n}{J}
\le
\frac{2\pi q\delta}{Y}+o(1).
\]

Because `Y` stays in a fixed compact subset of `(0,infinity)`, choose `delta` so small that this angle stays inside a fixed interval strictly contained in `(-pi/2,pi/2)` for all allowed `Y`. The imaginary attenuation across the largest channel is

\[
\frac{jR(1-\beta)}{J}
\le
\frac{K}{J}\frac{\log m+d_*}{Y}
=
\frac{\log m+d_*}{Ym}+o(1)
=o(1).
\]

Therefore every summand in

\[
C_J\!\left(x_n+i\frac{\log m+d_*}{Y}\right)
=\frac1K\sum_{j=0}^{K-1}
\exp\!\left(
\frac{ijx_n}{J}
-
\frac{j(\log m+d_*)}{YJ}
\right)
\]

lies in a common fixed right half-plane for all large `J`, uniformly in `1\le n\le M`. Hence

\[
\boxed{
\Re C_J\!\left(x_n+i\frac{\log m+d_*}{Y}\right)
\ge c_0>0
}
\]

for a constant `c_0` independent of `J` and `n`.

The shell-envelope coordinate is

\[
H[(\gamma_n-t_0)+i(1-\beta)]
=\frac1J\left(
 x_n+i\frac{\log m+d_*}{Y}
\right).
\]

Since `x_n=O(m)` and `m=o(A_J)=o(J)`, this tends uniformly to zero. Thus

\[
F\!\left(H[(\gamma_n-t_0)+i(1-\beta)]\right)
=F(0)+o(1),
\]

and `F(0)=\int\phi>0`.

Finally,

\[
e^{-X(1-\beta)}
=e^{-d_*}m^{-1}.
\]

There are `M~delta m` aligned terms. Up to the same fixed Euler/source prefactor already audited in `NB-231` and `NB-254`, the real part of the complete residue sum therefore obeys

\[
\boxed{
\liminf_{J\to\infty}
\Re\mathcal R_{\mathrm{packet}}
>0.
}
\]

The population ledger remains permissive. The packet has only `Theta(m)` points, with `m=o(A_J)=o(log J)`; its depth `log m+O(1)` tends to infinity in Ford units, so it stays safely away from the fixed zero-free boundary; fixed Bellotti disks see only `O(1)` consecutive carrier-spaced points after the same choice of `q`; and the ordinary/growing density allowances used for the earlier matched controls are looser than this population in the conservative regime. This is deliberately a **matched compatibility control**. It does not assert that zeta has such a packet.

## 5. Consequences for the live two-dimensional frontier

The construction separates two questions that were still conflated after `NB-260`.

First, **near-full effective depth rank really can defeat the fixed-depth rectangle.** The lower bound

\[
K\ge N_J^{1-o(1)}
\]

was not merely an artifact of a weak derivative argument: an explicit legal positive family with `K=N_J^{1+o(1)}` makes the carrier uniformly `o(1)` on every hard-width rectangle bounded away from `s=0`. The full horizontal Ford width does not rescue such a rectangle.

Second, **that does not produce a scalar escape from the Ford obstruction.** The same family has positive span

\[
W\sim R/m,
\]

so the capacity `R/W~m` remains. Positivity forces a coherent patch in a shrinking neighborhood of the Euler anchor, and the exact geometric average shows even more: its vertical carrier is still `1+o(1)` at every depth `u=o(m)`. The matched depth `u=log m` therefore survives with ample margin.

The relevant destination region is no longer a fixed rectangle

\[
s_0\le s\le1.
\]

Its lower edge has to move with the carrier rank. For this positive construction the obstruction is already visible at

\[
\boxed{
s_*(J)
=\frac{\log(J/K)}{\log J}+O\!\left(\frac1{\log J}\right).
}
\]

When `J/K=m\to\infty`, `s_*(J)\to0`. By choosing `m` to grow arbitrarily slowly subject to `m=o(A_J)`, the matched obstruction can be pushed arbitrarily close to the Euler edge while still retaining a growing packet.

Thus a fixed-depth Hardy/Nyman coercivity theorem would not close the scalar route. A genuinely decisive statement has to couple the Euler normalization to **shrinking-depth** complex zero sampling, with the shrinkage quantified against `J/K`, or else use an invariant that cannot concentrate its normalization in this boundary layer.

This also clarifies the role of positivity. `NB-254` already proves abstractly that a positive scalar mixture of span `W` has a `1/W` coherence window. The present construction supplies the complementary upper-side calculation: positive near-full depth rank can erase all fixed positive depths while the mandatory `R/W` coherence capacity survives only in a moving shallow layer. It therefore does not reopen the positive scalar route; it identifies where its unavoidable obstruction lives once the `NB-260` rank barrier is crossed.

## 6. Prior art and representation audit

The generic analytic ingredient is classical: a normalized block of consecutive Fourier modes is a geometric sum, closely related to the normalized Dirichlet kernel, and its decay away from the unit-circle boundary follows from the exact quotient formula. No external theorem is needed for any estimate above.

A fresh targeted search across Nyman--Beurling/Hardy formulations, Dirichlet/Fejer-kernel language, Mellin approximate identities, and recent Hardy-space work around zeta zeros did not locate the specific combination used here: the `N_J=J/log J` legal depth scale, a near-full resolved Mellin carrier that uniformly suppresses the hard-width fixed-depth rectangle, and the simultaneous reappearance of a matched packet at the shrinking depth `log(J/K)`. Recent Hardy-space Nyman--Beurling work continues to study completeness/orthogonality and optimal approximation, but no located source supplies this Ford-scaled boundary-layer statement. This is a prior-art boundary, not a uniqueness claim. Because the proof is direct and no new theorem is load-bearing, `SOURCES.md` needs no new dependency.

The representation split is important. The geometric-sum estimate itself is generic harmonic analysis. The specifically Nyman--Beurling content is the Euler normalization, the conversion from physical shell Hilbert cost to coefficient `ell^2`, the legal complex zero coordinate, the mapping between normalized depth `s` and damping `e^{-X(1-beta)}`, and the Bellotti-compatible matched-packet ledger. The conclusion is therefore a destination-interface method boundary for this scalar resolved architecture, not a general theorem about arbitrary Hardy functions or arbitrary Nyman approximants.

## 7. Adversarial audit

The strongest possible overclaim would be to say that `K=N_J^{1+o(1)}` solves the two-dimensional Hardy/Nyman problem. It does not. The construction only shows that **fixed positive depths** can be suppressed. Its failure as `s\downarrow0` is precisely where the matched obstruction moves.

A second overclaim would be to infer actual near-one zeta packets. None are asserted. The `Theta(m)` packet is a control compatible with the currently imported zero-free and counting information, used to prove that those inputs still do not exclude the geometry left by the carrier.

A third overclaim would be to treat the vanishing shell-Hilbert cost as a vanishing final Nyman distance. The shell source is only the resolved carrier component of the current route. Hardy projection, the full target, and any other terms in the final approximation remain separate. The small source norm merely shows that the fixed-depth suppression is not purchased by blowing up this particular physical cost.

The construction is also deliberately positive and one-sided. That makes the boundary-layer mechanism transparent and places it inside the hypotheses of `NB-254`; it does not prove that every signed/complex near-full carrier has the same transition profile. Signed, vector-valued, unresolved-overlap and alternative legal Hardy constructions remain outside this exact statement.

Finally, the regime `m\to\infty` is essential. If `K` becomes genuinely proportional to `J`, then `m=J/K=O(1)`, the positive matched population no longer grows, the span becomes `Theta(R)`, and the present compatibility control no longer supplies an order-one growing packet. That endpoint is a qualitatively different regime and is not settled here.

## 8. Surviving frontier

`NB-260` suggested attacking the full two-dimensional destination rectangle. The present construction shows that the rectangle must be formulated with a moving lower boundary. At any fixed positive normalized depth, a legal near-full carrier can already be uniformly tiny across the entire `Theta(J)` ordinate range.

The non-circular next question is therefore sharper:

> Can a bounded-cost legal scalar carrier simultaneously suppress the shrinking depth regime `X(1-beta)~log(J/K)` and the associated horizontal Ford capacity `R/W~J/K`, all the way until `K=Theta(J)`; or does the exact Hardy/Nyman destination impose a coercive boundary trace that prevents that migration?

For positive carriers, `NB-254` plus the explicit construction above already answers the first alternative negatively whenever `J/K\to\infty`. The genuinely open scalar case is signed/complex near-full rank, where positivity no longer supplies the boundary trace. Any further work should target that shrinking-depth/rank-coupled regime rather than another fixed-depth cell or fixed proportional depth interval.