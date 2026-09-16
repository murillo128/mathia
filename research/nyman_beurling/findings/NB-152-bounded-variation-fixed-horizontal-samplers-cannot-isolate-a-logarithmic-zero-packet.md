# NB-152 — Bounded-variation fixed horizontal samplers cannot isolate a logarithmic zero packet

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-POISSON + XI-CONSERVATION + MANY-POINT-OBSTRUCTION + NB-151-FRONTIER`.

`NB-151` closes the fixed-scale loophole for a two-point same-ordinate horizontal difference: a logarithmic target packet carrying positive charge forces a neighboring logarithmic adverse population through exact horizontal conservation of `xi'/xi`. The natural remaining question is whether several horizontal samples, a continuous signed superposition, or `G`-dependent weights can shape the negative lobe more favorably while staying at a fixed exterior horizontal scale.

They cannot do so under the scale-invariant conditioning needed to charge the target efficiently. The two-point factorization of `NB-151` is not the essential mechanism. What matters is only that the horizontal sampler has zero total mass, remains in a fixed compact subset of `Re s>1`, and has bounded total variation relative to the positive charge it places on the target packet. Under those hypotheses, the completed logarithmic derivative still has only `O(total variation)` total signed zero charge, while a packet of rank `Omega(log G)` contributes `Omega(target charge * log G)`. The resulting negative debt is forced onto actual zeros and quadratic Cauchy decay localizes a fixed fraction of it to bounded ordinate distance.

Fix

\[
0<a_-<a_+<\infty,
\qquad
\kappa>0,
\tag{1}
\]

and, for arbitrarily large `G`, let `mu_G` be a finite real signed Borel measure on

\[
A=[a_-,a_+]
\tag{2}
\]

with

\[
\mu_G(A)=0,
\qquad
V_G:=\|\mu_G\|_{\rm TV}.
\tag{3}
\]

The corresponding same-ordinate exterior sampler evaluates at points

\[
s_a=1+a+iG,
\qquad a\in A.
\tag{4}
\]

For a nontrivial zero `rho=beta+i gamma`, counted with multiplicity, write

\[
\theta=1-\beta\in(0,1),
\qquad
y=G-\gamma,
\tag{5}
\]

and define its signed zero-side charge

\[
Q_G(\rho)
:=
\int_A
\frac{a+\theta}{(a+\theta)^2+y^2}
\,d\mu_G(a).
\tag{6}
\]

Suppose there is a packet `F_G` of positive-ordinate zeros with

\[
d_G:=|F_G|\ge\kappa\log G
\tag{7}
\]

and with strictly positive minimum sampler charge

\[
q_G:=\inf_{\rho\in F_G}Q_G(\rho)>0.
\tag{8}
\]

Assume the sampler is uniformly well conditioned relative to that target charge:

\[
\boxed{
\frac{V_G}{q_G}\le C_*
}
\tag{9}
\]

for a fixed `C_*<infinity`. Condition `(9)` is invariant under rescaling `mu_G`; equivalently one may normalize `q_G=1` and require uniformly bounded total variation.

Then there is a constant

\[
R=R(a_-,a_+,\kappa,C_*)<\infty
\tag{10}
\]

such that, for all sufficiently large members of the sequence,

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\
                  \gamma>0\\
                  |\gamma-G|\le R}}
\bigl(Q_G(\rho)\bigr)_-
\gg_{a_-,a_+,\kappa,C_*}
q_G\log G.
}
\tag{11}
\]

Consequently the bounded window `|gamma-G|<=R` contains

\[
\boxed{\Omega(\log G)}
\tag{12}
\]

zeros, counted with multiplicity, on which the sampler has negative charge. The classical unit-interval zero-count bound gives the matching `O(log G)` upper bound in every fixed window, so the adverse population has logarithmic order.

If in addition the kernel is nonnegative for every nontrivial-zero horizontal coordinate throughout a central ordinate window,

\[
Q_G(\beta+i\gamma)\ge0
\qquad
(|\gamma-G|\le h,\ 0<\beta<1)
\tag{13}
\]

for some fixed `h>0`, then all the negative mass in `(11)` lies in the annulus

\[
h<|\gamma-G|\le R.
\tag{14}
\]

Thus the literal neighboring-packet conclusion of `NB-151` survives whenever the designed many-point kernel has a positive central lobe. Without `(13)`, the theorem is stronger in a different direction: even if the sampler allows horizontal sign changes inside the target ordinate window, it still forces a logarithmic population of adverse actual zeros somewhere within bounded distance of the charged packet.

## 1. Zero total mass gives an absolutely convergent discrete conservation law

The genus-one Hadamard representation gives

\[
\frac{\xi'}{\xi}(s)
=
B+
\sum_\rho
\left(
\frac1{s-\rho}+\frac1\rho
\right).
\tag{15}
\]

Integrating `(15)` against `mu_G` cancels both the constant `B` and every regularizer `1/rho` because of `(3)`. To justify the remaining zero sum without a symmetric limiting convention, fix any `a_0 in A`. Again using `mu_G(A)=0`,

\[
\int_A\frac{d\mu_G(a)}{1+a+iG-\rho}
=
\int_A
\left(
\frac1{1+a+iG-\rho}
-
\frac1{1+a_0+iG-\rho}
\right)d\mu_G(a).
\tag{16}
\]

Hence

\[
\left|
\int_A\frac{d\mu_G(a)}{1+a+iG-\rho}
\right|
\le
\frac{(a_+-a_-)V_G}
{a_-^2+(G-\gamma)^2}.
\tag{17}
\]

The right side is summable over the zero divisor: on unit ordinate shells the zero count is `O(log(t+2))`, while the weight in `(17)` has quadratic decay. Therefore the integrated zero sum is absolutely convergent and

\[
\boxed{
\sum_\rho Q_G(\rho)
=
\Re\int_A
\frac{\xi'}{\xi}(1+a+iG)
\,d\mu_G(a).
}
\tag{18}
\]

The right side has no logarithmic background. Uniformly for `a in A`,

\[
\frac{\xi'}{\xi}(s)
=
\frac1s+
\frac1{s-1}
-
\frac12\log\pi
+
\frac12\psi(s/2)
+
\frac{\zeta'}{\zeta}(s).
\tag{19}
\]

The constant term vanishes after integration. The rational terms are `O(V_G/G)`. Since `Re s>=1+a_->1`, the Euler series for `zeta'/zeta` is absolutely convergent and contributes `O_{a_-}(V_G)`. Finally, uniformly on the compact horizontal interval,

\[
\psi((1+a+iG)/2)
=
\log(iG/2)+O_{a_+,a_-}(1/G),
\tag{20}
\]

and the common logarithm cancels by `(3)`. Thus

\[
\boxed{
\sum_\rho Q_G(\rho)=O_{a_-,a_+}(V_G).
}
\tag{21}
\]

Equation `(21)` is the many-point analogue of `NB-151`'s fixed two-point conservation. The sampler may be discrete, continuous, or vary with `G`; only its zero mass and fixed compact horizontal support enter the estimate.

## 2. A logarithmic target packet forces logarithmic negative actual-zero charge

By `(7)`--`(8)`, the target packet contributes

\[
\sum_{\rho\in F_G}Q_G(\rho)
\ge
q_Gd_G
\ge
\kappa q_G\log G.
\tag{22}
\]

Zeros with negative ordinate are too far from the sampling height to absorb this charge. From `(6)`,

\[
|Q_G(\rho)|
\le
\frac{(a_++1)V_G}
{a_-^2+(G-\gamma)^2},
\tag{23}
\]

and for `gamma<0` the denominator contains `(G+|gamma|)^2`. Riemann--von Mangoldt shell counting therefore gives

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_{a_-,a_+}
V_G\frac{\log G}{G}
=o(V_G).
\tag{24}
\]

Let

\[
A_G^-:=
\sum_{\substack{\rho\notin F_G\\\gamma>0}}
(Q_G(\rho))_-.
\tag{25}
\]

Splitting the positive-ordinate zeros outside `F_G` into positive and negative charges and using `(21)`--`(24)` yields

\[
A_G^-
\ge
q_Gd_G-O_{a_-,a_+}(V_G).
\tag{26}
\]

By `(9)`, the error is only `O(q_G)`, whereas the target term is at least `kappa q_G log G`. Hence

\[
\boxed{
A_G^-\ge
\left(\kappa+o(1)\right)q_G\log G.
}
\tag{27}
\]

The adverse contribution in `(27)` is not a Jordan majorant. It is the negative part sampled by the **actual zeta zeros**, forced by the same completed-function conservation that underlies `NB-151`.

## 3. Bounded variation relative to target charge keeps the debt at bounded distance

For `R>=1`, equation `(23)` and the unit-shell bound

\[
N(t+1)-N(t)\ll\log(t+2)
\tag{28}
\]

give

\[
\sum_{\substack{\gamma>0\\|\gamma-G|\ge R}}
|Q_G(\rho)|
\ll_{a_-,a_+}
V_G
\left(
\frac{\log G}{R}
+
\frac{\log G}{G}
\right).
\tag{29}
\]

Using `(9)`, choose `R` large enough, depending only on `a_-,a_+,kappa,C_*`, that the first term in `(29)` is at most a fixed small fraction of `kappa q_G log G`. Equations `(27)` and `(29)` then prove `(11)`.

A single zero can carry at most

\[
|Q_G(\rho)|
\le
\int_A\frac{d|\mu_G|(a)}{a+\theta}
\le
\frac{V_G}{a_-}
\le
\frac{C_*}{a_-}q_G.
\tag{30}
\]

Therefore the negative mass in `(11)` requires `Omega(log G)` zeros counted with multiplicity. Conversely `(28)` bounds the number of zeros in the fixed window by `O(log G)`, proving `(12)` with logarithmic order. Partitioning the bounded window into finitely many fixed-width ordinate intervals shows that at least one such interval contains `Omega(log G)` adverse zeros.

Condition `(9)` is exactly what prevents a nominal many-point improvement from hiding an arbitrarily large cancellation cost in its coefficients. If `V_G/q_G` diverges, the conservation identity `(21)` still holds, but the radius needed in `(29)` can diverge with that ratio. The theorem therefore identifies an explicit escape parameter rather than silently ruling it out.

## 4. Relation to `NB-148`--`NB-151`

`NB-148` proves that every zero-mass exterior sampler exports equal positive and negative **Lebesgue-integrated** Poisson mass. `NB-149` shows that controlling the adverse lobe by total variation restores the positive `Theta(log G)` Hadamard budget. `NB-150` proves direct actual-zero occupation for a growing two-point horizontal scale, and `NB-151` proves target-conditioned actual-zero occupation for one fixed two-point horizontal difference.

The present finding removes the two-point restriction from the fixed-scale statement. A finite set of three, ten, or arbitrarily many horizontal samples, a continuous signed measure, and even a `G`-adaptive choice of weights are all covered provided their support stays in a fixed compact subset of `Re s>1` and their scale-invariant conditioning `V_G/q_G` remains bounded. There is no special cancellation polynomial to optimize: the zero-total-mass identity already forces the full signed zero sum to be only `O(V_G)`.

The two-point kernel of `NB-151` is recovered by

\[
\mu_G=\delta_L-\delta_{cL}.
\tag{31}
\]

Its total variation is `2`, its positive target charge is bounded below on every fixed central window `h<sqrt(c)L`, and `(13)` holds there. Thus `NB-151` is the explicit two-lobe model of the general conservation principle proved here.

## 5. Stress tests and boundary

The theorem does **not** rule out all signed exterior sampling. It leaves several genuinely different regimes outside its hypotheses. Horizontal offsets may shrink toward the pole at `Re s=1`, causing both the Euler-side cost and kernel conditioning to change; the horizontal support or the ratio `V_G/q_G` may grow with `G`; samples may have nontrivial vertical offsets; or the argument may retain signed prime-side/Nyman target information instead of trying to isolate one zero packet as a positive certificate.

In particular, an increasingly ill-conditioned many-point finite difference with `V_G/q_G->infinity` is not classified as a bounded-neighbor obstruction. Such a family must pay for its apparent localization through coefficient variation, and `(29)` makes that price explicit: the adverse charge may be pushed to a radius comparable to the conditioning ratio. Whether a useful source-side cancellation can compensate for that growth remains open.

No RH, simplicity, pair correlation, local zero asymptotic, or zero-density theorem is used. Multiplicity is retained throughout. The only zero-distribution input beyond the completed-function product is the standard `O(log T)` unit-interval upper bound following from Riemann--von Mangoldt. The theorem also does not contradict logarithmic confluence itself: a second adverse logarithmic population at bounded distance is compatible with the classical local counting budget.

## Prior-art search

Differenced logarithmic derivatives are classical in zero-free-region arguments; for example Ethan S. Lee, *On an explicit zero-free region for the Dedekind zeta-function*, J. Number Theory 224 (2021), 307--322, uses explicit formulas for a differenced logarithmic derivative. Bruna and Melnikov, *On translates of the Poisson kernel and zeros of harmonic functions*, Bull. London Math. Soc. 39 (2007), 317--326, study linear spans of Poisson-kernel translates and harmonic uniqueness. These sources delimit the generic analytic ingredients but are not load-bearing here.

The line-local delta is the target-conditioned zeta statement: zero-total-mass cancellation of the completed logarithmic derivative, plus bounded variation relative to target charge, forces a logarithmic **actual-zero** adverse population within bounded ordinate distance for every fixed-horizontal many-point/measure-valued sampler. The proof is the direct argument `(16)`--`(30)`, so no new `SOURCES.md` dependency is required and no priority claim is made for generic Poisson superposition or logarithmic-derivative differencing.

## Source map

- `NB-148`: zero-total-mass Poisson conservation and the signed-sampling frontier.
- `NB-149`: total-variation/Jordan repair obstruction; motivates retaining actual signed zero information.
- `NB-150`: mesoscopic two-point actual-zero occupation.
- `NB-151`: fixed-scale two-point `xi'/xi` conservation and bounded-neighbor adverse packet.
- Riemann--von Mangoldt/unit-interval zero counting: already anchored in `SOURCES.md` through Bellotti--Wong--Fiori and used in `NB-150`--`NB-151`.
- Classical Poisson/logarithmic-derivative literature in the prior-art paragraph is contextual only.

## Consequence for the line

The fixed-scale same-ordinate horizontal escape is now closed beyond two points. **Adding more horizontal samples does not help while the signed sampler remains uniformly conditioned relative to the charge it places on the target packet.** A logarithmic packet then forces a logarithmic population of adverse actual zeros at bounded distance.

The surviving many-point route must therefore spend a genuinely new resource: diverging coefficient variation/localization, shrinking or growing horizontal scale, vertical geometry, signed Euler-side cancellation, or direct coupling to target-bearing Nyman data before the zero charges are separated. This sharpens the `NB-151` frontier without claiming that exceptional logarithmic confluence itself is impossible.