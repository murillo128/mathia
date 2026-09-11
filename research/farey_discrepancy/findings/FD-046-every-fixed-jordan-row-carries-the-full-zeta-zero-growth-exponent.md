# FD-046 — every fixed Jordan row carries the full zeta-zero growth exponent

**Status:** `EXACT-DERIVED + LITERATURE-CALIBRATED + SOURCE-INVERTIBILITY + JORDAN-ROW-GROWTH + NONSQUAREFREE-OCCUPATION-BOUNDARY + RH-EQUIVALENT-POWER-SCALE`.

`FD-033` identifies the physical Schur source

\[
\mathcal H(N)
=\sum_{s\le N}\frac{\mathbf M(\lfloor N/s\rfloor)}s
\]

and its coefficient Dirichlet series `zeta(s+1)/zeta(s)`. `FD-038`--`FD-045` then ask whether the full nonsquarefree Jordan-row union can lose a positive fraction of the physical energy, and progressively rule out generic density failures and increasingly broad finite/growing Mellin-packet mechanisms.

There is a simpler source-specific rigidity at the **power-law scale**. The floor-harmonic transform taking the Mertens function to `mathcal H` is exactly invertible by a second floor transform with coefficients `mu(n)/n`. Consequently `mathcal H` has exactly the same polynomial growth exponent as the ordinary Mertens function. Every single fixed Jordan row samples `mathcal H` along a fixed dilation, so every fixed row already carries the full polynomial exponent of the zeta zero frontier.

Let

\[
\Theta
:=
\sup\{\Re\rho:\zeta(\rho)=0,\ 0<\Re\rho<1\}.
\]

Then

\[
\boxed{
\limsup_{N\to\infty}
\frac{\log(1+|\mathcal H(N)|)}{\log N}
=\Theta .
}
\tag{1}
\]

For every fixed Schur-head dimension `D`, let

\[
E_{H,D}
=\sum_{D<r\le H}w(r)
\mathcal H(\lfloor H/r\rfloor)^2,
\qquad
w(r)=\frac{J_2(r)}{r^2},
\]

and retain the nonsquarefree part

\[
U_{H,D}
=\sum_{\substack{D<r\le H\\\mu(r)=0}}
w(r)\mathcal H(\lfloor H/r\rfloor)^2.
\]

Then

\[
\boxed{
\limsup_{H\to\infty}
\frac{\log(1+E_{H,D})}{\log H}
=
\limsup_{H\to\infty}
\frac{\log(1+U_{H,D})}{\log H}
=2\Theta .
}
\tag{2}
\]

More generally, the same exponent `2 Theta` is carried by the energy on **any fixed nonempty set of Jordan rows**: one fixed row is enough. Thus squarefree rows and nonsquarefree rows are indistinguishable at the level of their limsup polynomial growth exponent even though their energy ratio may still oscillate strongly.

A useful equivalent formulation is that, for every fixed `D`,

\[
\boxed{
\mathrm{RH}
\iff
E_{H,D}=O_\varepsilon(H^{1+\varepsilon})\ \forall\varepsilon>0
\iff
U_{H,D}=O_\varepsilon(H^{1+\varepsilon})\ \forall\varepsilon>0.
}
\tag{3}
\]

Therefore a physical escape `U/E -> 0`, if it exists, cannot be explained by a smaller global power exponent of the nonsquarefree energy. In fact, for every fixed `epsilon>0`,

\[
\boxed{
\limsup_{H\to\infty}
H^\varepsilon\frac{U_{H,D}}{E_{H,D}}
=\infty .
}
\tag{4}
\]

So no bound of the form `U/E = O(H^(-epsilon))` can hold globally. This is still far weaker than a positive constant occupation theorem: a vanishing subsequence, or even a globally vanishing ratio slower than every power, remains compatible with (1)--(4).

## 1. The quotient-shell source and Mertens function are exact inverse floor transforms

For arithmetic coefficients `a(n)` define the floor transform

\[
(\mathcal T_aF)(N)
:=
\sum_{d\le N}a(d)F(\lfloor N/d\rfloor).
\tag{5}
\]

The elementary identity

\[
\left\lfloor
\frac{\lfloor N/d\rfloor}{e}
\right\rfloor
=
\left\lfloor\frac{N}{de}\right\rfloor
\]

implies the exact composition law

\[
\boxed{
\mathcal T_a\mathcal T_b
=
\mathcal T_{a*b},
}
\tag{6}
\]

where `*` is Dirichlet convolution.

Put

\[
a(n)=\frac1n,
\qquad
b(n)=\frac{\mu(n)}n.
\tag{7}
\]

For every `n`,

\[
(a*b)(n)
=
\sum_{de=n}\frac1d\frac{\mu(e)}e
=
\frac1n\sum_{e\mid n}\mu(e)
=
\mathbf 1_{n=1}.
\tag{8}
\]

Thus `a` and `b` are exact Dirichlet inverses. The definition of `mathcal H` in `FD-033` is precisely

\[
\mathcal H=\mathcal T_a\mathbf M,
\tag{9}
\]

so (6)--(8) give the inverse identity

\[
\boxed{
\mathbf M(N)
=
\sum_{d\le N}
\frac{\mu(d)}d
\mathcal H(\lfloor N/d\rfloor).
}
\tag{10}
\]

This is stronger than merely observing that the coefficient Dirichlet series of `mathcal H` is `zeta(s+1)/zeta(s)`: the two summatory functions recover one another by bounded floor-convolution operators on every positive polynomial-weight space.

Indeed, fix `sigma>0`. If `|F(N)|<=C N^sigma`, then

\[
|\mathcal T_aF(N)|
\le
CN^\sigma
\sum_{d\le N}d^{-1-\sigma}
\le
C\zeta(1+\sigma)N^\sigma,
\tag{11}
\]

and exactly the same estimate holds for `mathcal T_b` because `|mu(d)|<=1`. Therefore

\[
\boxed{
\mathcal H(N)=O(N^\sigma)
\iff
\mathbf M(N)=O(N^\sigma)
\qquad(\sigma>0).
}
\tag{12}
\]

No asymptotic approximation, cancellation estimate, or zeta-zero assumption enters this equivalence.

## 2. The power exponent of `mathcal H` is the zeta-zero frontier

The classical Littlewood--Titchmarsh Mertens criterion states, in its usual half-plane form, that a power bound for `M(x)` is equivalent to the corresponding zero-free half-plane for `zeta`; in particular RH is equivalent to

\[
\mathbf M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\text{for every }\varepsilon>0.
\tag{13}
\]

The same standard argument parametrized by the rightmost-zero frontier gives

\[
\inf\{\sigma>0:\mathbf M(x)=O(x^{\sigma+\varepsilon})
\ \forall\varepsilon>0\}
=\Theta.
\tag{14}
\]

For completeness, the lower direction needs almost no machinery. If `M(x)=O(x^sigma)`, Abel summation makes

\[
\frac1{\zeta(s)}
=s\int_1^\infty \mathbf M(x)x^{-s-1}\,dx
\tag{15}
\]

analytic for `Re(s)>sigma`; hence there can be no zeta zero there. Conversely, the standard Littlewood/Titchmarsh contour argument gives `M(x)=O(x^(theta+epsilon))` in every half-plane strictly to the right of the zero frontier.

Combining (12) and (14) proves (1). Equivalently, for every `sigma>Theta`,

\[
\mathcal H(N)=O_\sigma(N^\sigma),
\tag{16}
\]

while no exponent `sigma<Theta` can bound `mathcal H` globally.

This is also an internal consistency check on `FD-033`. Hardy's theorem gives `Theta>=1/2`; hence the critical `L^2` divergence found there occurs exactly at the lowest possible polynomial frontier. Under RH, `mathcal H` is `N^(1/2+o_power(1))` in the usual upper-bound sense, but `FD-033` still forces its critical weighted square norm to diverge.

## 3. One fixed Jordan row already has exponent `2 Theta`

Fix `D`, and choose any fixed integer `r_0>D`. Its single-row energy is

\[
J_{r_0}(H)
:=
w(r_0)
\mathcal H(\lfloor H/r_0\rfloor)^2.
\tag{17}
\]

For an upper bound, take any `sigma>Theta`. Since `Theta>=1/2`, also `sigma>1/2`. Equation (16) gives

\[
\begin{aligned}
E_{H,D}
&\le
C_\sigma^2 H^{2\sigma}
\sum_{r>D}w(r)r^{-2\sigma}\\
&\le
C_\sigma^2\zeta(2\sigma)H^{2\sigma}.
\end{aligned}
\tag{18}
\]

Hence

\[
\limsup_{H\to\infty}
\frac{\log(1+E_{H,D})}{\log H}
\le2\Theta.
\tag{19}
\]

For the reverse inequality, use the exact dilation subsequence `H=r_0N`. Then

\[
J_{r_0}(r_0N)
=w(r_0)\mathcal H(N)^2.
\tag{20}
\]

Equation (1) therefore gives

\[
\limsup_{H\to\infty}
\frac{\log(1+J_{r_0}(H))}{\log H}
=2\Theta.
\tag{21}
\]

Since `J_(r_0)<=E_(H,D)`, (19)--(21) prove the first equality in (2).

The same argument applies to any row subset containing `r_0`: the subset energy lies between the one-row energy and the full energy. Thus every fixed nonempty row class has exponent `2Theta`.

For the nonsquarefree union choose, once and for all, any fixed nonsquarefree `r_ns>D`; for example a sufficiently large multiple of `4`. Then

\[
J_{r_{\rm ns}}(H)
\le U_{H,D}\le E_{H,D},
\tag{22}
\]

and (19)--(21) give the second equality in (2). A fixed squarefree row similarly proves the same exponent for the squarefree union.

The fixed-`D` hypothesis is essential here. The lower bound deliberately uses a row `r_0` independent of `H`; it does not transfer unchanged to a head dimension that itself tends to infinity.

## 4. The nonsquarefree absolute-energy exponent is itself RH-equivalent

If RH holds, (12)--(13) give, for every `eta>0`,

\[
|\mathcal H(N)|\ll_\eta N^{1/2+\eta}.
\tag{23}
\]

Insert this into (18), choosing `eta` small enough for any prescribed `epsilon>0`, to obtain

\[
E_{H,D}=O_\varepsilon(H^{1+\varepsilon}),
\qquad
U_{H,D}=O_\varepsilon(H^{1+\varepsilon}).
\tag{24}
\]

Conversely, suppose the second estimate in (24) holds for every `epsilon>0`. Fix a nonsquarefree `r_ns>D` and put `H=r_ns N`. By (22),

\[
w(r_{\rm ns})\mathcal H(N)^2
\le
U_{r_{\rm ns}N,D}
\ll_\varepsilon N^{1+\varepsilon}.
\tag{25}
\]

Thus

\[
\mathcal H(N)
=O_\varepsilon(N^{1/2+\varepsilon}),
\tag{26}
\]

after harmlessly renaming `epsilon`. Equation (12) transfers (26) to the Mertens function, and the Littlewood--Titchmarsh criterion gives RH. The implication from the full energy bound is identical. This proves (3).

This equivalence is about an **upper power envelope**, not about the occupation fraction. It must not be read as saying that a positive lower bound for `U/E` is RH-equivalent. The latter remains the potentially cheaper projective question.

## 5. Equal exponents forbid only polynomially uniform occupation loss

Equation (2) gives one useful quantitative boundary for the accepted joint-occupation clue. Fix `epsilon>0`. Choose `sigma>Theta` so close that (18) gives

\[
E_{H,D}\ll H^{2\Theta+\varepsilon/4}.
\tag{27}
\]

The limsup exponent of `U` is `2Theta`, so there are arbitrarily large `H` with

\[
U_{H,D}\ge H^{2\Theta-\varepsilon/4}.
\tag{28}
\]

Along those horizons,

\[
\frac{U_{H,D}}{E_{H,D}}
\gg H^{-\varepsilon/2},
\tag{29}
\]

up to the fixed constant in (27). Therefore

\[
H^\varepsilon\frac{U_{H,D}}{E_{H,D}}
\to\infty
\]

along an unbounded subsequence, proving (4).

This excludes a global polynomial occupation loss. It does **not** exclude any of the following:

- `U/E -> 0` at a subpower rate such as an inverse logarithm;
- a cofinal subsequence on which `U/E` is polynomially small, compensated by other horizons;
- large oscillations in which squarefree and nonsquarefree energies attain their common power exponent on different scales.

Those are precisely the distinctions that the same-horizon occupation program must retain. Equal limsup exponents are not a substitute for a pointwise frame bound.

## 6. Consequence for the post-`FD-045` frontier

`FD-045` shows that a naturally conditioned critical Mellin packet of small dimension cannot evade nonsquarefree occupation merely by pushing its frequency width to the square-root scale. The present result attacks the complementary possibility that the physical source somehow assigns a genuinely smaller **power scale** to nonsquarefree rows. It cannot: one fixed nonsquarefree row already has the full zeta-zero exponent.

This narrows the remaining escape mechanism. A failure of `U/E>=c_D` must live below polynomial resolution: in relative scale oscillations, coefficient/remainder coherence, or a subpower separation between the horizons on which the two energies realize their common exponent. In particular, trying to prove the clue by first establishing different polynomial exponents for `U` and `E` is structurally impossible.

Under RH, (2), `FD-033`, and `FD-038` fit together especially tightly. Both `E` and `U` have polynomial exponent exactly `1`, yet both are unconditionally superlinear in the sense already proved there. Thus the critical question is necessarily in the slowly varying/projective factor, not in a hidden power of `H`.

## 7. Adversarial checks, prior art, and falsification boundary

The main algebraic check is (8): with `a(n)=1/n` and `b(n)=mu(n)/n`, their Dirichlet convolution is exactly the identity coefficient. Direct finite evaluation reproduces `M(N)` from `mathcal H` through (10); no limiting inversion is involved.

The main analytic check is the convergence in (18). It needs `2sigma>1`; this is automatic because Hardy gives `Theta>=1/2` and the upper argument always takes `sigma>Theta`. The lower exponent uses only one fixed positive Jordan weight and the exact horizons `H=r_0N`, so floor errors cannot degrade it. For the nonsquarefree statement, `r_ns` is fixed before `H` varies.

The Mertens power-growth criterion is classical Littlewood/Titchmarsh theory. Titchmarsh and Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed. (1986), Section 14.25, is used as the literature anchor for the RH endpoint and the standard zero-free-half-plane argument. No novelty is claimed for the equivalence between Mertens power bounds and zeta zero-free regions, for Dirichlet convolution, or for the fact that a fixed dilation preserves a limsup exponent.

A targeted prior-art search for the exact quotient `zeta(s+1)/zeta(s)`, the coefficient `mu(rad n) phi(rad n)/n`, and summatory/Mertens formulations did not locate this particular transfer to the Schur/Jordan row energies. Absence from that search is not a novelty claim. The Mathia-specific contribution is the combination of the exact two-sided floor-transform (9)--(10) with the already-derived Jordan energy (17), yielding the rowwise exponent identity (2) and the occupation boundary (4).

The finding is falsified if the floor-transform composition law (6) fails, if `mu(n)/n` is not the Dirichlet inverse of `1/n`, if the classical Mertens zero-frontier criterion is misapplied, or if a fixed Jordan row does not embed as (17). It does not prove `U/E` has a positive liminf, does not rule out the `FD-039` type escape after source-specific constraints are imposed at subpower resolution, and does not improve the Franel--Landau exponent. Its role is to identify exactly what **cannot** distinguish squarefree from nonsquarefree occupation: their absolute polynomial growth exponent.